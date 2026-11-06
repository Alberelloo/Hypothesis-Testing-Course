"""
Генератор синтетических данных для практики 2.П3 «Double-ML».

Онлайн-сервис полгода возвращает спящих пользователей: CRM-правило решает, кому отправить
бонус на следующий заказ и какого размера. Одна строка — один пользователь в одной кампании:

    user_id          идентификатор пользователя (один пользователь бывает в нескольких кампаниях)
    campaign         номер ежемесячной кампании, от 1 до 6
    days_since_order дней с последнего заказа на момент кампании
    orders_total     заказов за всё время
    avg_check        средний чек, ₽
    tenure_days      дней с регистрации
    promo_share      доля прошлых заказов с промокодом
    tickets_90d      обращений в поддержку за 90 дней
    app_installed    установлено ли приложение (0/1)
    sent             отправили ли бонус (0/1)
    bonus            размер бонуса, ₽ (0, если не отправили)
    opened           открыл ли письмо с бонусом (0/1, известно только после отправки)
    returned         сделал ли заказ за 30 дней после кампании (0/1)
    margin           маржа с заказов за эти 30 дней до списания бонуса, ₽

Файлы:

    reactivation.csv          наблюдательные данные, решения принимала CRM
    reactivation_holdout.csv  случайная группа: отправка 50/50, бонус равновероятно от 50 до 500 ₽

Истинные параметры заданы в TRUE_PARAMS, а важный скрытый признак (свежая активность в
приложении) в файлы не попадает. Не подсматривайте сюда до раздела 10 практики.

Запуск: python generate_data.py  (перезаписывает оба файла рядом со скриптом)
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2031
N_USERS = 112_000
HOLDOUT_SHARE = 0.25
N_CAMPAIGNS = 6
BONUS_GRID = np.arange(50, 501, 50)

TRUE_PARAMS = {
    "hidden_send": 0.4,       # влияние скрытой активности на отправку (логит)
    "hidden_return": 0.4,     # её же влияние на возврат (логит)
    "user_frailty": 0.5,      # постоянная склонность пользователя возвращаться (логит)
    "saturation_rub": 150,    # масштаб насыщения: эффект бонуса b равен 1 - exp(-b / 150)
    "effect_scale": 1.5,      # общий масштаб эффекта (логит)
    "hard_ticket_rule": 3,    # с этого числа обращений CRM никогда не отправляет бонус
}


def expit(v):
    return 1 / (1 + np.exp(-v))


def saturation(bonus, params=TRUE_PARAMS):
    return 1 - np.exp(-bonus / params["saturation_rub"])


def sensitivity(days, promo_share, app, tickets):
    """Чувствительность к бонусу: те, кто ещё помнит сервис и любит промокоды; обиженным бонус вреден."""
    fresh = np.exp(-(((days - 70) / 40) ** 2))
    return 0.15 + 0.75 * fresh + 0.8 * promo_share + 0.2 * app - 1.3 * (tickets >= 2)


def base_logit(days, value, promo_share, app, tickets, campaign):
    season = np.array([0.0, 0.1, -0.1, 0.05, -0.15, 0.1])[campaign - 1]
    return (-1.15 - 0.011 * (days - 30) + 0.55 * value + 0.25 * app - 0.2 * tickets
            + 0.6 * promo_share + 0.35 * np.sin(days / 25) + season)


def crm_risk(days, value, tickets):
    """Оценка срочности у CRM: ценный пользователь, давно не заказывал, были проблемы."""
    return 0.03 * (days - 90) + 0.25 * (value - 1.6) + 0.5 * np.minimum(tickets, 2)


def generate(seed=SEED, params=TRUE_PARAMS):
    rng = np.random.default_rng(seed)
    n_users = N_USERS
    holdout_user = rng.random(n_users) < HOLDOUT_SHARE
    orders0 = rng.poisson(np.exp(1.6 + 0.6 * rng.normal(size=n_users))) + 1
    check0 = np.exp(rng.normal(7.3, 0.4, n_users))
    tenure0 = rng.gamma(3, 220, n_users) + 60
    promo0 = rng.beta(1.3, 2.6, n_users)
    app0 = (rng.random(n_users) < 0.6).astype(int)
    days0 = rng.uniform(30, 150, n_users)
    frailty = rng.normal(size=n_users)
    activity0 = rng.normal(size=n_users)

    # пользователь входит в 1-3 кампании подряд
    waves = rng.choice([1, 2, 3], n_users, p=[0.55, 0.3, 0.15])
    first = rng.integers(1, N_CAMPAIGNS + 1, n_users)
    idx = np.repeat(np.arange(n_users), waves)
    step = np.concatenate([np.arange(k) for k in waves])
    n = idx.size
    campaign = (first[idx] + step - 1) % N_CAMPAIGNS + 1
    days = np.clip(days0[idx] + 30 * step + rng.normal(0, 3, n), 30, 240)
    orders = orders0[idx]
    check = np.round(check0[idx], -1)
    tenure = np.round(tenure0[idx] + 30 * step)
    promo = np.round(promo0[idx], 3)
    app = app0[idx]
    tickets = rng.poisson(0.55, n)
    hidden = 0.8 * activity0[idx] + 0.6 * rng.normal(size=n)   # свежая активность, в выгрузку не попала
    holdout = holdout_user[idx]

    value = np.log(orders) + 0.5 * (np.log(check) - 7.3)
    risk = crm_risk(days, value, tickets)
    budget = np.array([0.0, 0.3, -0.3, 0.2, -0.2, 0.1])[campaign - 1]

    send_p = expit(0.3 + 1.2 * risk + budget + params["hidden_send"] * hidden)
    send_p = np.where(tickets >= params["hard_ticket_rule"], 0.0, np.clip(send_p, 0.01, 0.99))
    sent = (rng.random(n) < send_p).astype(int)
    bonus = np.clip(np.round((250 + 45 * risk + 60 * budget + 8 * hidden + rng.normal(0, 65, n)) / 10) * 10, 50, 500)

    sent[holdout] = rng.integers(0, 2, holdout.sum())
    bonus[holdout] = rng.choice(BONUS_GRID, holdout.sum())
    bonus = bonus * sent

    sens = sensitivity(days, promo, app, tickets)
    base = (base_logit(days, value, promo, app, tickets, campaign)
            + params["user_frailty"] * frailty[idx] + params["hidden_return"] * hidden)
    index = params["effect_scale"] * sens

    def prob(b):
        return expit(base + index * saturation(b, params))

    p1 = prob(bonus)
    returned = (rng.random(n) < p1).astype(int)
    order_margin = 0.22 * check * np.exp(rng.normal(0, 0.45, n)) * (1 + rng.poisson(0.5, n))
    margin = np.round(order_margin * returned)
    opened = sent * (rng.random(n) < expit(-0.6 + 0.5 * app + 1.3 * returned + 0.3 * hidden)).astype(int)

    df = pd.DataFrame({
        "user_id": 100_000 + idx, "campaign": campaign, "days_since_order": np.round(days).astype(int),
        "orders_total": orders, "avg_check": check.astype(int), "tenure_days": tenure.astype(int),
        "promo_share": promo, "tickets_90d": tickets, "app_installed": app, "sent": sent,
        "bonus": bonus.astype(int), "opened": opened, "returned": returned, "margin": margin.astype(int),
    })
    truth = pd.DataFrame({"holdout": holdout, "hidden": hidden, "base": base, "index": index, "send_p": send_p})
    return df, truth


def true_effects(truth, df, bonus_rule=None, params=TRUE_PARAMS):
    """Истинный эффект каждой строки при бонусе bonus_rule (по умолчанию фактический бонус)."""
    bonus = df["bonus"].to_numpy() if bonus_rule is None else bonus_rule
    return expit(truth["base"] + truth["index"] * saturation(bonus, params)) - expit(truth["base"])


def truth_report(df, truth, params=TRUE_PARAMS):
    """Истинные значения для сверки в разделе 10. Считаются по наблюдательной части без строк с жёстким правилом."""
    keep = (~truth["holdout"]).to_numpy() & (df["tickets_90d"].to_numpy() < params["hard_ticket_rule"])
    part, part_truth = df[keep], truth[keep]
    sent = part["sent"].to_numpy() == 1
    crm_bonus = np.resize(part.loc[sent, "bonus"].to_numpy(), len(part))   # бонус CRM как у отправленных
    effect = true_effects(part_truth, part, crm_bonus).to_numpy()
    weight = part_truth["send_p"].to_numpy() * (1 - part_truth["send_p"].to_numpy())
    return {
        "ATE при бонусах CRM": effect.mean(),
        "ATT": true_effects(part_truth, part).to_numpy()[sent].mean(),
        "Средний эффект с весами e(1-e)": (effect * weight).sum() / weight.sum(),
        "Эффект 200 -> 300 ₽": (expit(part_truth["base"] + part_truth["index"] * saturation(300, params))
                                - expit(part_truth["base"] + part_truth["index"] * saturation(200, params))).mean(),
        "Эффект 400 -> 500 ₽": (expit(part_truth["base"] + part_truth["index"] * saturation(500, params))
                                - expit(part_truth["base"] + part_truth["index"] * saturation(400, params))).mean(),
    }


if __name__ == "__main__":
    data, hidden_part = generate()
    folder = Path(__file__).resolve().parent
    data[~hidden_part["holdout"]].to_csv(folder / "reactivation.csv", index=False)
    data[hidden_part["holdout"]].to_csv(folder / "reactivation_holdout.csv", index=False)
    print(data.shape, f"доля строк в случайной группе: {hidden_part['holdout'].mean():.3f}")
    for name, value in truth_report(data, hidden_part).items():
        print(f"{name}: {value:+.4f}")
