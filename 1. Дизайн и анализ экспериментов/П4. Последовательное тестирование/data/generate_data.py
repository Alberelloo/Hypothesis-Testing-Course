"""
Генератор синтетических данных для практики 2.П1 «Последовательное тестирование».

Сервис бронирования отелей тестирует блок «Горящие предложения» на главной странице.
Одна строка — один пользователь, впервые попавший в тест (28 дней, сплит 50/50):

    user_id    идентификатор пользователя
    date       день первого захода
    group      A — без блока, B — с блоком
    booked     сделал ли бронирование (0/1)
    revenue    стоимость бронирования, ₽ (0, если брони нет)
    cancelled  отменил ли бронирование (0/1)

Истинные эффекты заданы в TRUE_PARAMS. Не подсматривайте в них до раздела 7:
там они раскрываются и в самой практике.

Запуск: python generate_data.py  (перезаписывает hotdeals_ab.csv рядом со скриптом)
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2027
START_DATE = "2026-09-07"            # понедельник
N_DAYS = 28
USERS_WEEKDAY, USERS_WEEKEND = 5_600, 7_000

TRUE_PARAMS = {
    "conv_weekday": 0.050,           # базовая конверсия в будни
    "conv_weekend": 0.056,           # базовая конверсия в выходные
    "effect_late": 0.002,            # долгосрочный эффект на конверсию
    "effect_early": 0.010,           # эффект на когорте первого дня
    "effect_decay_days": 4.0,        # скорость затухания эффекта по когортам
    "check_median": 12_000,          # медиана стоимости брони в группе A
    "check_sigma": 1.2,              # log-стандартное отклонение стоимости брони
    "check_ratio_b": 0.95,           # брони в B на 5% дешевле: скидки
    "cancel_a": 0.18,                # доля отмен среди броней в A
    "cancel_b": 0.195,               # доля отмен среди броней в B
}


def effect_by_cohort(day, params=TRUE_PARAMS):
    """Истинный эффект на конверсию для пользователей, пришедших в день day (с нуля)."""
    late, early = params["effect_late"], params["effect_early"]
    return late + (early - late) * np.exp(-day / params["effect_decay_days"])


def generate(seed=SEED, params=TRUE_PARAMS):
    rng = np.random.default_rng(seed)
    dates = pd.date_range(START_DATE, periods=N_DAYS)
    frames = []
    next_id = 100_000
    for day, date in enumerate(dates):
        weekend = date.dayofweek >= 5
        n_users = rng.poisson(USERS_WEEKEND if weekend else USERS_WEEKDAY)
        group = np.where(rng.random(n_users) < 0.5, "B", "A")
        is_b = group == "B"

        conv = params["conv_weekend"] if weekend else params["conv_weekday"]
        booked = rng.random(n_users) < conv + is_b * effect_by_cohort(day, params)

        median = params["check_median"] * np.where(is_b, params["check_ratio_b"], 1.0)
        check = rng.lognormal(np.log(median), params["check_sigma"])
        cancel = rng.random(n_users) < np.where(is_b, params["cancel_b"], params["cancel_a"])

        frames.append(pd.DataFrame({
            "user_id": np.arange(next_id, next_id + n_users),
            "date": date.strftime("%Y-%m-%d"),
            "group": group,
            "booked": booked.astype(int),
            "revenue": np.round(check * booked).astype(int),
            "cancelled": (booked & cancel).astype(int),
        }))
        next_id += n_users
    return pd.concat(frames, ignore_index=True)


if __name__ == "__main__":
    out = Path(__file__).with_name("hotdeals_ab.csv")
    df = generate()
    df.to_csv(out, index=False)
    print(f"{out.name}: {len(df):,} строк")
    print(df.groupby("group")[["booked", "revenue", "cancelled"]].mean().round(4))
