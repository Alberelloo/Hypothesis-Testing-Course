# Lesson 06 — Bayesian AB Testing

## Обзор
Занятие сопоставляет частотный и байесовский подходы к статистике, показывает, как интерпретация результатов меняется в байесовской парадигме, и демонстрирует применение PyMC для практического A/B тестирования.

## Цели занятия
- Вспомнить историю развития статистики и отличия частотного и байесовского взглядов.
- Освоить базовую теорию байесовских апостериорных распределений и сопряжённых приоров.
- Применять инструменты PyMC для настройки и анализа байесовских A/B тестов.

## Материалы
- [Лекция](lecture.ipynb)

## Источники
### Основные источники
1. [История статистики](https://en.wikipedia.org/wiki/History_of_statistics)
2. [Байесовский подход vs частотный подход](https://www.youtube.com/watch?v=8wVq5aGzSqY&list=PLEDdkzD9hUd4iebXTR6CYbAZI9eMDyfPk)
3. [Суть байесовской статистики](https://www.youtube.com/watch?v=3jP4H0kjtng&list=PLEDdkzD9hUd4iebXTR6CYbAZI9eMDyfPk&index=7)
4. [Основные семейства распределений](https://betanalpha.github.io/assets/case_studies/probability_densities.html#1_eye_of_the_tiger)
5. [Сопряжённые распределения](https://ru.wikipedia.org/wiki/Сопряжённое_априорное_распределение)
6. [Пример расчёта с бета-приором](https://towardsdatascience.com/beta-distributions-a-cornerstone-of-bayesian-calibration-801f96e21498/)
7. [Байесовская статистика в PyMC](https://www.pymc.io/projects/examples/en/latest/case_studies/bayesian_workflow.html#the-bayesian-workflow-an-overview)
8. [Байесовский A/B тест](https://www.pymc.io/projects/examples/en/2022.01.0/case_studies/bayesian_ab_testing.html#bernoulli-conversions)
9. [Планирование байесовских A/B тестов](https://www.youtube.com/watch?v=1fnXvWwtFss)
10. [Байесовский подход к A/B тестированию](https://habr.com/ru/companies/glowbyte/articles/732024/)

### Дополнительные материалы
- [История статистики до 1750](https://www.amazon.com/History-Probability-Statistics-Applications-before/dp/0471471291)
- [История статистики с 1750 до 1930](https://www.amazon.com/History-Mathematical-Statistics-Wiley-Probability/dp/0471179124)
- [MCMC](https://ru.wikipedia.org/wiki/Марковская_цепь_Монте-Карло)
- [Методы MCMC](https://m-clark.github.io/docs/ld_mcmc/)
- [Variational Inference](https://ermongroup.github.io/cs228-notes/inference/variational/)
- [Метод Лапласа](https://en.wikipedia.org/wiki/Laplace%27s_method)
- [Вывод формул для байесовского A/B](https://www.evanmiller.org/bayesian-ab-testing.html)
- [Практический обзор байесовского A/B](https://arxiv.org/pdf/2307.14628)
- [Bayesian A/B testing in PyMC3](https://towardsdatascience.com/bayesian-a-b-testing-in-pymc3-54dceb87af74/)
- [Байесовский A/B через регрессии](https://matteocourthoud.github.io/post/bayesian_ab_test/)
- [Мифы о байесовском A/B](https://habr.com/ru/companies/X5Tech/articles/900032/)
- [Bayesian A/B/C testing](https://www.researchgate.net/publication/335340064_Bayesian_ABC_testing)
- [Bayesian A/B testing. Part I — Conversions](https://towardsdatascience.com/bayesian-ab-testing-part-i-conversions-ac2635f878ec/)
- [Bayesian A/B testing. Part II — Revenue](https://towardsdatascience.com/bayesian-ab-testing-part-ii-revenue-1fbcf04f96cd/)
- [Bayesian A/B testing. Part III — Test duration](https://towardsdatascience.com/bayesian-ab-testing-part-iii-test-duration-f2305215009c/)
- [Bayesian A/B testing. Part IV — Choosing a prior](https://towardsdatascience.com/bayesian-ab-testing-part-iv-choosing-a-prior-5a4fe3223bfd/)
