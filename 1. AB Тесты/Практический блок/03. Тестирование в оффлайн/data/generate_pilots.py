"""
Генератор легенды для практики 1.П3 «Тестирование в оффлайн».

История продаж настоящая: открытый датасет Rossmann Store Sales. В репозитории её нет,
ноутбук скачивает данные с Kaggle. Пилот вымышленный: скрипт только выбирает магазины
и задаёт, насколько изменились бы их показатели, если бы там появилась бьюти-зона.

Одна строка pilot_stores.csv — один магазин:

    store                номер магазина в Rossmann
    in_pool              входит в пул первой волны (0/1)
    business_list        входит в список директора для второй волны (0/1)
    traffic_uplift       изменение логарифма числа покупателей, если зона есть
    check_uplift         изменение логарифма среднего чека, если зона есть
    stockout_if_treated  если магазин попадёт в пилот, на 3-4 неделе закончится товар (0/1)

Истинные эффекты заданы в TRUE_PARAMS. Не подсматривайте в них до раздела 9.

Запуск: python generate_pilots.py  (перезаписывает pilot_stores.csv рядом со скриптом)
"""

from pathlib import Path

import kagglehub
import numpy as np
import pandas as pd

SEED = 2027
DATA_START, DATA_END = "2013-01-07", "2015-07-26"   # полные недели с понедельника по воскресенье
WAVE1_START = "2015-02-02"
PRE_WEEKS = 12
POOL_FORMAT_A, POOL_OTHER = 60, 20                  # формат a чаще подходит под зону
BUSINESS_SIZE = 40
STOCKOUT_SHARE = 1 / 3                              # товар заканчивается в самых крупных магазинах

TRUE_PARAMS = {
    "check_uplift_a": 0.050,         # средний чек в формате a
    "check_uplift_other": 0.025,     # средний чек в остальных форматах
    "traffic_uplift": -0.012,        # часть покупателей раздражает консультант
    "store_noise": 0.010,            # разброс эффекта между магазинами
}


def weekly_panel():
    """Собирает недельные продажи и оставляет магазины без дыр в данных."""
    path = kagglehub.dataset_download("pratyushakar/rossmann-store-sales")
    sales = pd.read_csv(f"{path}/train.csv", parse_dates=["Date"], low_memory=False)
    info = pd.read_csv(f"{path}/store.csv").set_index("Store")
    sales = sales[sales["Date"].between(DATA_START, DATA_END)].copy()
    sales["week"] = sales["Date"].dt.to_period("W-SUN").dt.start_time
    weekly = sales.groupby(["week", "Store"]).agg(revenue=("Sales", "sum"), open_days=("Open", "sum")).reset_index()
    revenue = weekly.pivot(index="week", columns="Store", values="revenue")
    open_days = weekly.pivot(index="week", columns="Store", values="open_days")
    good = (revenue > 0).all() & (open_days >= 4).all()
    return revenue.loc[:, good], info


def generate(seed=SEED, params=TRUE_PARAMS):
    rng = np.random.default_rng(seed)
    revenue, info = weekly_panel()
    log_rev = np.log(revenue)
    stores = log_rev.columns.to_numpy()
    formats = info.loc[stores, "StoreType"].to_numpy()

    # Список директора: самый сильный летний пик в отчёте за 2013 год.
    weeks = log_rev.index
    summer = log_rev[(weeks >= "2013-07-01") & (weeks < "2013-09-02")].mean()
    spring = log_rev[(weeks >= "2013-03-04") & (weeks < "2013-05-06")].mean()
    business = (summer - spring).sort_values(ascending=False).index[:BUSINESS_SIZE]

    rest = np.setdiff1d(stores, business)
    is_a = info.loc[rest, "StoreType"].to_numpy() == "a"
    pool = np.r_[rng.choice(rest[is_a], POOL_FORMAT_A, replace=False),
                 rng.choice(rest[~is_a], POOL_OTHER, replace=False)]

    start = pd.Timestamp(WAVE1_START)
    pre = log_rev[(weeks >= start - pd.Timedelta(weeks=PRE_WEEKS)) & (weeks < start)].mean()
    largest = pre[pool].sort_values(ascending=False).index[:int(len(pool) * STOCKOUT_SHARE)]

    check = np.where(formats == "a", params["check_uplift_a"], params["check_uplift_other"])
    table = pd.DataFrame({
        "store": stores,
        "in_pool": np.isin(stores, pool).astype(int),
        "business_list": np.isin(stores, business).astype(int),
        "traffic_uplift": (params["traffic_uplift"] + rng.normal(0, params["store_noise"], len(stores))).round(5),
        "check_uplift": (check + rng.normal(0, params["store_noise"], len(stores))).round(5),
        "stockout_if_treated": np.isin(stores, largest).astype(int),
    })
    return table


if __name__ == "__main__":
    table = generate()
    table.to_csv(Path(__file__).with_name("pilot_stores.csv"), index=False)
    print(table.shape, table[["in_pool", "business_list", "stockout_if_treated"]].sum().to_dict())
