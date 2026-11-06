"""
Генератор синтетических данных для практики 1.П2 «Тестирование новой страницы чекаута».

Одна строка — один пользователь, дошедший до чекаута за время теста (14 дней):

    user_id            идентификатор пользователя
    date               день первого захода на чекаут
    group              A — старый чекаут, B — новый (20% трафика)
    converted          оформил ли заказ (0/1)
    revenue            выручка с пользователя, ₽ (0, если заказа нет)
    checkout_time_sec  время на странице чекаута, с
    payment_error      была ли ошибка оплаты (0/1)

В данные специально подложены проблемы логирования: дубли строк и пользователи,
попавшие в обе группы. Истинные эффекты заданы в TRUE_PARAMS — не подсматривайте
в них до конца практики.

Запуск: python generate_data.py  (перезаписывает checkout_ab.csv рядом со скриптом)
"""

import hashlib
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2035
SALT = "checkout-v2"
SHARE_B = 0.20
START_DATE = "2026-09-07"            # понедельник
N_DAYS = 14
USERS_PER_DAY = 7_500

TRUE_PARAMS = {
    #            A        B
    "conv":     (0.700,   0.711),    # конверсия в заказ
    "aov_mu":   (7.80,    7.80),     # log-среднее суммы заказа (средний чек не меняется)
    "aov_sigma": 0.80,
    "time_mu":  (np.log(95), np.log(95 * 0.98)),   # медиана времени на чекауте: −2% в B
    "time_sigma": 0.60,
    "pay_err":  (0.0200,  0.0225),   # доля пользователей с ошибкой оплаты
}

N_DUPLICATES = 250                   # строки, записанные в лог дважды
N_BOTH_GROUPS = 60                   # пользователи, попавшие в обе группы


def assign_group(user_id, salt=SALT, share_b=SHARE_B):
    """Детерминированное назначение группы хешем от соли и user_id."""
    h = int(hashlib.md5(f"{salt}:{user_id}".encode()).hexdigest(), 16)
    return "B" if h % 10_000 < share_b * 10_000 else "A"


def generate(seed=SEED):
    rng = np.random.default_rng(seed)

    users_per_day = rng.poisson(USERS_PER_DAY, size=N_DAYS)
    n = int(users_per_day.sum())
    dates = np.repeat(pd.date_range(START_DATE, periods=N_DAYS).strftime("%Y-%m-%d"), users_per_day)
    user_ids = rng.choice(np.arange(1_000_000, 10_000_000), size=n, replace=False)
    groups = np.array([assign_group(u) for u in user_ids])
    is_b = (groups == "B").astype(int)

    def pick(param):
        a, b = TRUE_PARAMS[param]
        return np.where(is_b, b, a)

    converted = (rng.random(n) < pick("conv")).astype(int)
    order_value = rng.lognormal(pick("aov_mu"), TRUE_PARAMS["aov_sigma"])
    revenue = np.round(converted * order_value, 2)
    checkout_time = np.round(rng.lognormal(pick("time_mu"), TRUE_PARAMS["time_sigma"]), 1)
    payment_error = (rng.random(n) < pick("pay_err")).astype(int)

    df = pd.DataFrame({
        "user_id": user_ids,
        "date": dates,
        "group": groups,
        "converted": converted,
        "revenue": revenue,
        "checkout_time_sec": checkout_time,
        "payment_error": payment_error,
    })

    # Пользователи в обеих группах: повторная запись с «чужой» группой и своими метриками
    both = df.sample(N_BOTH_GROUPS, random_state=seed).copy()
    both["group"] = np.where(both["group"] == "A", "B", "A")
    both["converted"] = (rng.random(N_BOTH_GROUPS) < 0.7).astype(int)
    both["revenue"] = np.round(both["converted"] * rng.lognormal(7.8, 0.8, N_BOTH_GROUPS), 2)

    # Дубли: те же строки ещё раз
    dups = df.sample(N_DUPLICATES, random_state=seed + 1)

    df = pd.concat([df, both, dups], ignore_index=True)
    return df.sample(frac=1, random_state=seed + 2).reset_index(drop=True)


if __name__ == "__main__":
    out = Path(__file__).with_name("checkout_ab.csv")
    data = generate()
    data.to_csv(out, index=False)
    print(f"{out.name}: {len(data)} строк")
