# 1.П3. Тестирование в оффлайн

> **Модуль:** A/B тестирование · **Блок:** практический · **Время:** 3 ч · **Опирается на:** 1.02, 1.04, 1.П2 · **Статус:** ✅ готово

## Обзор
Сквозной кейс: сеть дрогери проверяет бьюти-зону с консультантом. История продаж настоящая (Rossmann Store Sales), пилот вшит поверх неё, поэтому в конце выводы сверяются с правдой. На A/A по истории измеряем цену неверной единицы анализа, сравниваем дизайны и считаем мощность инъекцией эффекта. Первая волна идёт со случайным назначением внутри пар: эффект значим, но окупаемость не доказана. Во второй волне магазины выбрал бизнес, и наивный DiD обещает +10.9%, из которых больше половины составляет сезон. Заканчиваем проверкой групп, каннибализацией, переносом на сеть, решением и регламентом для команды. Главный вывод: в оффлайне основная работа делается до старта, а значимость не отвечает на вопрос, окупится ли изменение.

## Цели занятия
- Выбирать единицу анализа и понимать, почему магазино-дни нельзя считать независимыми.
- Проверять методы на истории: A/A и инъекция эффекта.
- Планировать пилот: понимать, что мощность покупается магазинами, а не неделями.
- Проводить анализ по парам, раскладывать выручку на трафик и чек, сравнивать интервал с порогом окупаемости.
- Узнавать неслучайный отбор и понимать, какие методы от него защищают, а какие нет.
- Проверять сопоставимость групп, учитывать каннибализацию и переносить результат на сеть.

## Материалы
- [Практика](practice.ipynb): задания со свёрнутыми решениями (раскрываются кликом в Colab, Jupyter и VS Code).
- Данные: история продаж скачивается с Kaggle через `kagglehub`, авторизация не нужна. Легенда пилота лежит в [data/pilot_stores.csv](data/pilot_stores.csv), её генерирует скрипт [data/generate_pilots.py](data/generate_pilots.py) (в нём же зашиты истинные эффекты).

## Источники
### Основные источники
1. [Rossmann Store Sales (Kaggle)](https://www.kaggle.com/competitions/rossmann-store-sales)
2. [Наша методология A/B-тестирования (X5)](https://habr.com/ru/post/466349)
3. [Подход к A/B-тестам в офлайне (М.Видео)](https://habr.com/ru/post/697282)
4. [Офлайн А/Б-тесты (Бургер Кинг)](https://habr.com/p/902778)
5. [Тестирование в оффлайне от МТС](https://habr.com/ru/companies/ru_mts/articles/648063/): adversarial validation для проверки групп.
6. [Эксперимент с наружной рекламой от Amazon](https://www.amazon.science/blog/a-first-of-its-kind-experiment-to-measure-the-impact-of-out-of-home-advertising)
7. [Bertrand, Duflo, Mullainathan — How Much Should We Trust Differences-in-Differences Estimates? (QJE, 2004)](https://www.nber.org/system/files/working_papers/w8841/w8841.pdf)
8. [Imai, King, Nall — The Essential Role of Pair Matching in Cluster-Randomized Experiments (Statistical Science, 2009)](https://gking.harvard.edu/files/cluster.pdf)
9. [Bruhn, McKenzie — In Pursuit of Balance: Randomization in Practice in Development Field Experiments (AEJ: Applied, 2009)](https://conference.iza.org/ELMPDC2009/mckenzie_d2795.pdf)
10. [Chen, Longfils, Remy — Trimmed Match Design for Randomized Paired Geo Experiments (2021)](https://arxiv.org/abs/2105.07060)

### Дополнительные материалы
1. [Видео #1](https://www.youtube.com/watch?v=OZ1Ywpm4kIY)
2. [Видео #2](https://www.youtube.com/watch?v=jC20dtKoUGU&t=1811s)
3. [От A/B-тестирования к Causal Inference в офлайн ритейле (X5 Tech)](https://habr.com/ru/companies/X5Tech/articles/768008/)
4. [Abadie, Zhao — Synthetic Controls for Experimental Design](https://arxiv.org/abs/2108.02196)
