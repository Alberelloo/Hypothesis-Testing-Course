# 2.П3. Double-ML

> **Модуль:** Квази-эксперименты · **Блок:** практический · **Время:** 2.5 ч · **Опирается на:** 2.11, 2.10, 2.08 · **Статус:** ✅ готово

## Обзор
Сквозной кейс: онлайн-сервис полгода возвращает спящих пользователей бонусами, решения принимает CRM-правило, A/B-теста не было. Пишем Double ML вручную с интервалами, проверяем мешающие модели, перекрытие и зависимость от разбиения, разбираем ловушки выбора признаков. Отдельно рассматриваем бинарное воздействие (отправлять ли бонус: PLR, IRM, ATE, ATT) и непрерывное (какой размер: наклон и кривая отклика). Затем сверяемся с библиотекой `DoubleML`, оцениваем чувствительность к скрытым конфаундерам, решаем, кому и сколько платить, глядя на прибыль. В конце открываем случайную группу и проверяем все выводы. Главный вывод: Double ML убирает только то смещение, которое ему показали.

## Цели занятия
- Реализовывать Double ML с кросс-фиттингом и стандартной ошибкой из ортогональной оценки.
- Проводить диагностику: качество мешающих моделей, перекрытие, устойчивость к разбиению.
- Выбирать признаки по причинному графу и узнавать плохие контроли.
- Различать PLR, ATE и ATT и понимать, на какой вопрос отвечает каждая оценка.
- Оценивать эффект непрерывного воздействия и кривую отклика, видеть границы экстраполяции.
- Проводить анализ чувствительности к скрытым конфаундерам и читать robustness value.
- Строить правила таргетинга по эффекту на прибыль и честно оценивать их на случайных данных.

## Материалы
- [Практика](practice.ipynb): задания со свёрнутыми решениями (раскрываются кликом в Colab, Jupyter и VS Code).
- Данные: синтетические [data/reactivation.csv](data/reactivation.csv) (решения CRM) и [data/reactivation_holdout.csv](data/reactivation_holdout.csv) (случайная группа). Их генерирует скрипт [data/generate_data.py](data/generate_data.py), в нём же зашиты истинные эффекты.

## Источники
### Основные источники
1. [Chernozhukov et al. — Double/Debiased Machine Learning for Treatment and Structural Parameters (The Econometrics Journal, 2018)](https://arxiv.org/abs/1608.00060)
2. [Chernozhukov, Cinelli, Newey, Sharma, Syrgkanis — Long Story Short: Omitted Variable Bias in Causal Machine Learning](https://arxiv.org/abs/2112.13398)
3. [Bach et al. — Sensitivity Analysis for Causal ML: A Use Case at Booking.com (2025)](https://arxiv.org/abs/2510.09109)
4. [Документация DoubleML: чувствительность](https://docs.doubleml.org/stable/guide/sensitivity.html), [модели](https://docs.doubleml.org/stable/guide/models.html) и [неоднородность эффекта](https://docs.doubleml.org/stable/guide/heterogeneity.html)
5. [Xu et al. — Causal Machine Learning for Promotions: Industry Evidence and Applications (DoorDash, KDD 2025 Workshop)](https://causal-machine-learning.github.io/kdd2025-workshop/papers/16.pdf)
6. [Ascarza — Retention Futility: Targeting High-Risk Customers Might Be Ineffective (Journal of Marketing Research, 2018)](https://doi.org/10.1509/jmr.16.0163)
7. [Hünermund, Louw, Caspi — Double Machine Learning and Automated Confounder Selection: A Cautionary Tale (Journal of Causal Inference, 2023)](https://doi.org/10.1515/jci-2022-0078)
8. [Cinelli, Forney, Pearl — A Crash Course in Good and Bad Controls (Sociological Methods & Research, 2024)](https://ftp.cs.ucla.edu/pub/stat_ser/r493.pdf)

### Дополнительные материалы
1. [Smarter promotions with causal machine learning (блог DoorDash)](https://careersatdoordash.com/blog/doordash-smarter-promotions-with-causal-machine-learning)
2. [Bach et al. — DoubleML: An Object-Oriented Implementation of Double Machine Learning in Python](https://arxiv.org/abs/2104.03220)
3. [Bach et al. — Hyperparameter Tuning for Causal Inference with Double Machine Learning: A Simulation Study (2024)](https://arxiv.org/abs/2402.04674)
