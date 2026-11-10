"""Генерирует панель городов для практики 2.П2.

Данные полностью синтетические, названия городов использованы только как подписи.
Запуск: python generate_data.py

Истинные значения зашиты здесь и раскрываются в конце практики.
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 2602
WEEKS_PRE, WEEKS_POST = 104, 12
START = "2023-03-06"
TREATED = "Екатеринбург"
OUTLIER = "Москва"

TRUE_EFFECT = 0.06            # установившийся эффект подписки на заказы
RAMP_WEEKS = 2.0              # постоянная времени выхода на установившийся эффект
ANTICIPATION_WEEKS = 4        # анонс за 4 недели до запуска
ANTICIPATION_DROP = 0.035     # часть клиентов откладывает заказы
SPILLOVER_CITIES = ["Челябинск", "Курган", "Тюмень"]
SPILLOVER_DROP = 0.07         # курьеров перебросили в город запуска
WAREHOUSE_CITY = "Красноярск"     # у этого донора после запуска закрылся склад
WAREHOUSE_WEEK = 3            # неделя после запуска
WAREHOUSE_DROP = 0.14

CITIES = {
    "Центр": ["Воронеж", "Ярославль", "Рязань", "Тула", "Липецк", "Тверь", "Иваново", "Брянск", "Курск",
              "Белгород", "Владимир", "Калуга"],
    "Северо-Запад": ["Санкт-Петербург", "Калининград", "Вологда", "Мурманск", "Архангельск", "Псков"],
    "Поволжье": ["Казань", "Нижний Новгород", "Самара", "Уфа", "Саратов", "Тольятти", "Ижевск", "Ульяновск",
                 "Оренбург", "Пенза", "Набережные Челны", "Чебоксары"],
    "Урал": ["Екатеринбург", "Челябинск", "Пермь", "Тюмень", "Магнитогорск", "Сургут", "Курган"],
    "Сибирь": ["Новосибирск", "Омск", "Красноярск", "Иркутск", "Томск", "Кемерово", "Барнаул", "Новокузнецк"],
    "Юг": ["Краснодар", "Ростов-на-Дону", "Волгоград", "Сочи", "Ставрополь", "Астрахань", "Махачкала"],
    "Дальний Восток": ["Владивосток", "Хабаровск", "Якутск", "Чита", "Улан-Удэ"],
}


def smooth_walk(rng, n, sd, keep=0.97):
    """Медленный случайный процесс: авторегрессия с коэффициентом keep."""
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = keep * x[t - 1] + rng.normal(0, sd)
    return x


def ar_noise(rng, n, sd, phi=0.3):
    """Недельный шум города с небольшой автокорреляцией."""
    x = np.zeros(n)
    x[0] = rng.normal(0, sd)
    for t in range(1, n):
        x[t] = phi * x[t - 1] + rng.normal(0, sd * np.sqrt(1 - phi ** 2))
    return x


def build():
    rng = np.random.default_rng(SEED)
    weeks = WEEKS_PRE + WEEKS_POST
    t = np.arange(weeks)
    dates = pd.date_range(START, periods=weeks, freq="W-MON")
    season = np.sin(2 * np.pi * (t + 8) / 52)
    winter = np.cos(2 * np.pi * (t - 44) / 26)
    new_year = np.isin(dates.isocalendar().week.values, [52, 1]).astype(float)
    common = smooth_walk(rng, weeks, 0.006)
    regions = {r: smooth_walk(rng, weeks, 0.010) for r in CITIES}
    after = np.maximum(t - WEEKS_PRE + 1, 0)

    rows, meta = [], []
    for region, names in CITIES.items():
        region_growth = rng.normal(0.12, 0.012)
        for name in names + ([OUTLIER] if region == "Центр" else []):
            income = rng.normal(0, 1)
            growth = region_growth + 0.010 * income + rng.normal(0, 0.006)
            base = 95 * np.exp(0.06 * income + rng.normal(0, 0.05))
            loading_season = rng.normal(0.06, 0.010)
            loading_winter = rng.normal(0.02, 0.006)
            loading_common = rng.normal(1.0, 0.15)
            loading_region = rng.normal(1.0, 0.15)
            population = int(np.exp(rng.normal(13.4, 0.5)))
            young = 0.24 + 0.012 * income + rng.normal(0, 0.012)
            if name == TREATED:
                growth, income, base = region_growth + 0.008, 0.7, 101.0
            if name == OUTLIER:
                growth, income, base, population = 0.24, 2.9, 190.0, 13_000_000
                loading_season, young = 0.11, 0.30
            shared = (growth * t / 52 + loading_season * season + loading_winter * winter
                      + 0.10 * new_year + loading_common * common + loading_region * regions[region])
            noise = ar_noise(rng, weeks, 0.016)
            b2b_noise = ar_noise(rng, weeks, 0.03)
            physical = np.zeros(weeks)    # затрагивает все заказы, в том числе B2B
            demand = np.zeros(weeks)      # затрагивает только розничных клиентов
            if name == TREATED:
                demand += np.log1p(TRUE_EFFECT * (1 - np.exp(-after / RAMP_WEEKS)))
                announced = (t >= WEEKS_PRE - ANTICIPATION_WEEKS) & (t < WEEKS_PRE)
                demand[announced] += np.log1p(-ANTICIPATION_DROP)
            if name in SPILLOVER_CITIES:
                physical += np.log1p(-SPILLOVER_DROP * (1 - np.exp(-after / RAMP_WEEKS)))
            if name == WAREHOUSE_CITY:
                physical[after >= WAREHOUSE_WEEK] += np.log1p(-WAREHOUSE_DROP)
            meta.append({"city": name, "region": region, "population": population,
                         "income_index": round(100 + 12 * income, 1), "young_share": round(young, 3)})
            rows.append(pd.DataFrame({
                "city": name, "week": dates,
                "orders": (base * np.exp(shared + noise + physical + demand)).round(2),
                "b2b_orders": (0.22 * base * np.exp(shared + b2b_noise + physical)).round(2),
                "counterfactual": base * np.exp(shared + noise)}))
    return pd.concat(rows, ignore_index=True), pd.DataFrame(meta)


def event_log():
    launch = pd.Timestamp(START) + pd.Timedelta(weeks=WEEKS_PRE)
    week = pd.Timedelta(weeks=1)
    return pd.DataFrame([
        ("Омск", launch - 40 * week, "Обновление приложения", "Новый экран корзины для всех городов"),
        ("Казань", launch - 22 * week, "Промо", "Недельная скидка на первый заказ"),
        (TREATED, launch - ANTICIPATION_WEEKS * week, "Коммуникации", "Анонс подписки в приложении и рассылке"),
        (TREATED, launch, "Запуск", "Платная подписка с бесплатной доставкой"),
        ("Сочи", launch + 1 * week, "Промо", "Сезонная реклама на билбордах"),
        ("Челябинск", launch, "Операции", "Часть курьеров перераспределена в соседний город"),
        ("Курган", launch, "Операции", "Часть курьеров перераспределена в соседний город"),
        ("Тюмень", launch, "Операции", "Часть курьеров перераспределена в соседний город"),
        (WAREHOUSE_CITY, launch + WAREHOUSE_WEEK * week, "Инцидент", "Закрыт крупный склад, зона доставки сократилась"),
        ("Томск", launch + 5 * week, "Операции", "Плановая смена подрядчика сортировки"),
    ], columns=["city", "week", "type", "description"]).sort_values("week", ignore_index=True)


if __name__ == "__main__":
    here = Path(__file__).parent
    panel, cities = build()
    panel.drop(columns="counterfactual").to_csv(here / "delivery_panel.csv", index=False)
    cities.to_csv(here / "cities.csv", index=False)
    event_log().to_csv(here / "events.csv", index=False)
    treated = panel[(panel["city"] == TREATED) & (panel["week"] >= pd.Timestamp(START) + pd.Timedelta(weeks=WEEKS_PRE))]
    truth = treated.assign(true_effect_pct=(100 * (treated["orders"] / treated["counterfactual"] - 1)).round(3))
    truth[["week", "true_effect_pct"]].to_csv(here / "truth.csv", index=False)
    print(panel.shape, cities.shape)
