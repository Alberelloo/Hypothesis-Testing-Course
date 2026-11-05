# 2.06. Interleaving тестирование

> **Модуль:** Квази-эксперименты · **Мини-блок:** Альтернатива A/B тестам · **Время:** 1.5 ч · **Статус:** ✅ готово

## Обзор
Interleaving сравнивает два алгоритма ранжирования внутри одной выдачи: каждый пользователь видит смешанный список, а по его выбору определяется предпочтение. Занятие разбирает методы смешивания, статистический анализ, проверку корректности и ограничения метода, а также кейсы Airbnb, Amazon, Авито и LinkedIn.

## Цели занятия
- Понять, почему парный дизайн чувствительнее A/B-теста и от чего зависит выигрыш в трафике.
- Освоить Balanced, Team Draft и competitive pairs и уметь считать результат с правильной единицей анализа.
- Научиться проверять работоспособность interleaving: A/A, контроль качества данных, парные эксперименты с A/B.
- Понимать, чего interleaving не измеряет и чем counterfactual interleaving отличается от классического.

## Материалы
- [Лекция](lecture.ipynb)

## Источники
### Основные источники
1. [Доклад про interleaving (Матемаркетинг)](https://lms.matemarketing.ru/content/talk/617)
2. [Interleaving в поиске Airbnb](https://airbnb.tech/data/beyond-a-b-test-speeding-up-airbnb-search-ranking-experimentation-through-interleaving/)
3. [Online testing for learning to rank: interleaving](https://sease.io/2020/05/online-testing-for-learning-to-rank-interleaving.html)
4. [Generalized Team Draft Interleaving (Kharitonov et al., 2015)](https://eprints.gla.ac.uk/108076/1/108076.pdf)
5. [Large-Scale Validation and Analysis of Interleaved Search Evaluation (Chapelle et al., 2012)](https://www.cs.cornell.edu/people/tj/publications/chapelle_etal_12a.pdf)
6. [How Does Clickthrough Data Reflect Retrieval Quality? (Radlinski et al., 2008)](https://www.cs.cornell.edu/people/tj/publications/radlinski_etal_08b.pdf)
7. [Harnessing the Power of Interleaving and Counterfactual Evaluation for Airbnb Search Ranking (Zhang et al., 2025)](https://arxiv.org/abs/2508.00751)
8. [Debiased Balanced Interleaving at Amazon Search (Bi et al., 2022)](https://www.amazon.science/publications/debiased-balanced-interleaving-at-amazon-search)
9. [Interleaved Online Testing in Large-Scale Systems (Bi et al., 2023)](https://cdn.amazon.science/c1/4d/7945330e47539fdd870cb5c73613/interleaved-online-testing-in-large-scale-systems.pdf)
10. [Почему A/B-тест не подходит для оценки ранжирования (Авито)](https://habr.com/ru/companies/avito/articles/1043880/)
11. [Producer-Side Experiments Based on Counterfactual Interleaving Designs (Wang, Ba, LinkedIn, 2023)](https://arxiv.org/abs/2310.16294)

### Дополнительные материалы
1. [A Probabilistic Method for Inferring Preferences from Clicks (Hofmann et al., 2011)](https://dare.uva.nl/id/628c8aaf-9dec-4c98-a3d8-b6bbf3962581)
2. [Interleaving в Netflix (Parks et al., 2017)](https://netflixtechblog.com/interleaving-in-online-experiments-at-netflix-a04ee392ec55)
3. [Статья Airbnb про interleaving на Medium](https://medium.com/airbnb-engineering/beyond-a-b-test-speeding-up-airbnb-search-ranking-experimentation-through-interleaving-7087afa09c8e)
