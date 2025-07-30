### Занятие №6

**Название** : Байесовские A/B тесты

**Темы** : 
  * Байесовский vs Частотный подход
  * Байесовская статистика
    * Теоретическая справка
    * Кейс для понимания теории
    * Байесовская статистика в PYMC
  * Байесовский A/B Тест
  * Сравнение Байесовского и Частотного A/B тестирования

    
**Цели**
  1. Познакомить с учениями основных школ поздей истории статистики
  2. Дать минимальную теоретическую базу по байесовской статистикой
  3. Показать основной функционал PYMC для работы с байесовской статистикой
  4. Показать, как проводится байесовское A/B тестирование 

**Используемые Источники**
1. [История статистики](https://en.wikipedia.org/wiki/History_of_statistics)
2. [Байесовский подход vs Частотный подход](https://www.youtube.com/watch?v=8wVq5aGzSqY&list=PLEDdkzD9hUd4iebXTR6CYbAZI9eMDyfPk)
3. [Суть байесовской статистики](https://www.youtube.com/watch?v=3jP4H0kjtng&list=PLEDdkzD9hUd4iebXTR6CYbAZI9eMDyfPk&index=7)
4. [Сопряжённые распределения](https://ru.wikipedia.org/wiki/Сопряжённое_априорное_распределение)
5. [Пример подсчёта с приором из бета распределения](https://towardsdatascience.com/beta-distributions-a-cornerstone-of-bayesian-calibration-801f96e21498/)
6. [Байесовская статистика в PYMC](https://www.pymc.io/projects/examples/en/latest/case_studies/bayesian_workflow.html#the-bayesian-workflow-an-overview)
7. [Байесовский A/B тест](https://www.pymc.io/projects/examples/en/2022.01.0/case_studies/bayesian_ab_testing.html#bernoulli-conversions)
8. [Планирование Байесовский A/B тестов](https://www.youtube.com/watch?v=1fnXvWwtFss)
9. [Байесовский подход к A/B тестированию](https://habr.com/ru/companies/glowbyte/articles/732024/)

**Доп источники**
* [История статистики до 1750](https://www.amazon.com/History-Probability-Statistics-Applications-before/dp/0471471291)
* [История статистики с 1750 до 1930](https://www.amazon.com/History-Mathematical-Statistics-Wiley-Probability/dp/0471179124)
* [MCMC](https://ru.wikipedia.org/wiki/Марковская_цепь_Монте-Карло)
* [Методы MCMC](https://m-clark.github.io/docs/ld_mcmc/)
* [Variational Inference](https://ermongroup.github.io/cs228-notes/inference/variational/)
* [Метод Лапласа](https://en.wikipedia.org/wiki/Laplace%27s_method)
* [Вывод формул для Байесовского A/B](https://www.evanmiller.org/bayesian-ab-testing.html)
* [Честная статья про Байесовский A/B для разных случаев](https://arxiv.org/pdf/2307.14628)
* [Байесовкий A/B в PYMC пример](https://towardsdatascience.com/bayesian-a-b-testing-in-pymc3-54dceb87af74/)
* [Байесовский A/B через регрессии](https://matteocourthoud.github.io/post/bayesian_ab_test/)
* [Мифы Байесовского A/B](https://habr.com/ru/companies/X5Tech/articles/900032/)
* [Байесовский A/B/C тест](https://www.researchgate.net/publication/335340064_Bayesian_ABC_testing)
* [Байесовский A/B часть 1. Конверсии](https://towardsdatascience.com/bayesian-ab-testing-part-i-conversions-ac2635f878ec/)
* [Байесовский A/B часть 2. Выручка](https://towardsdatascience.com/bayesian-ab-testing-part-ii-revenue-1fbcf04f96cd/)
* [Байесовский A/B часть 3. Длительность теста](https://towardsdatascience.com/bayesian-ab-testing-part-iii-test-duration-f2305215009c/)
* [Байесовский A/B часть 4. Выбор приора](https://towardsdatascience.com/bayesian-ab-testing-part-iv-choosing-a-prior-5a4fe3223bfd/)
