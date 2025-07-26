### Занятие №2 Введение в тестирование гипотез: A/B тестирование: основы и дизайн

**Название** : Методы ускорения A/B тестов

**Темы лекции** : 
  * Концепция идеального тестирования: уровень доказательности и Рандомизированные Контролируемые Испытания (RCT)
  * Пайплайн тестирования гипотез
  * Виды тестов
    * Superiority / Non-Inferiority / Equivalence / Futility
    * Односторонние / Двусторонние
    * Fixed-horizon design / Sequential design / Adaptive design
  * Формализация A/B тестирования
    * Типы метрики:
      * Прокси метрики
      * Success / Guardrail / Deterioration / Quaility
      * User-level Метрики vs Ratio Метрики  -> дельта метод
      * прокси-метрики
    * Матрица ошибок (Confusion matrix), ошибки 1 и 2 рода 
      * Матрица ошибок
      * Ошибки 1 и 2 рода
    * MDE & sample size calculation
    * Статистические критерии
      * Параметрические
        * $z$ тест
        * $t$ тест
      * Непараметрические
        * $\chi^2$ тест
        * $U$ тест (Mann–Whitney)
        * Bootstrap
  * Проверка корректности критерия
  * Основные проблемы тестов
    * Проблемы подглядывания (peeking problem)
    * Проблемы предпосылок RCT
      * Проблемы рандомизации (SRM + A/A/B тесты)
      * Проблемы гомогенности групп
      * Проблемы независимости групп

**Темы семинара** : 
  * Доказательство центральной придельной теоремы с помощью Монте-Карло
  * Проведение теста с помощью z-теста
  * Проведение теста с помощью t-теста
  * Проведение теста с помощью $\chi^2$-теста

  **Цели**

  1. Познакомить с доказательствами в науке
  2. Познакомить с полным пайплайном A/B тестов
  3. Пройтись по основным статистическим понятиям и критериям для A/B тестов
  4. Познакомить с основными проблемами в A/B тестах

**Используемые Источники** 

1. [Уровень доказательности экспериментов](https://en.wikipedia.org/wiki/Hierarchy_of_evidence) 
2. [Рандомизированные Контролируемые Испытания (RCT)](https://en.wikipedia.org/wiki/Randomized_controlled_trial)
3. [Superiority vs Non-inferiority Tests](https://blog.analytics-toolkit.com/2017/case-non-inferiority-designs-ab-testing/)
4. [Типы тестов для two-sample test](https://www.ncss.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Two_Proportions-Non-Inferiority,_Superiority,_Equivalence,_and_Two-Sided_Tests_vs_a_Margin.pdf) (главное - разные виды тестов)
5. [Общий флоу проведения A/B тестов](http://www.machinelearning.ru/wiki/index.php?title=Проверка_статистических_гипотез)
6. [Прокси метрики](https://www.youtube.com/watch?v=fSRKOr3L6AI) 
7. [Типы тестов + типы метрик по целям](https://arxiv.org/pdf/2402.11609)  (глава 2)
8. [Метрики отношений и дельта метод](https://habr.com/ru/companies/X5Tech/articles/740476/)
9. [Матрица ошибок](https://en.wikipedia.org/wiki/Confusion_matrix#cite_ref-22)
10. [Ошибки 1 и 2 рода](https://ru.wikipedia.org/wiki/Ошибки_первого_и_второго_рода)
11. [Power Analysis](https://chabefer.github.io/STCI/Power.html#basics-of-traditional-power-analysis-using-test-statistics)
12. [Определение размера выборки на исторических данных](https://habr.com/ru/companies/lamoda/articles/707816/)
13. [Определение размера выборов для ratio метрик](https://medium.com/expedia-group-tech/how-to-size-for-online-experiments-with-ratio-metrics-3d57362f1967)
14. [Сборник статистических критериев #1](https://www.statskingdom.com/index.html)
15. [Сборник статистических критериев #2](https://www.biostathandbook.com/testchoice.html)
16. [z-test](https://bytepawn.com/ab-testing-and-the-ztest.html#ab-testing-and-the-ztest)
17. [Центральная Предельная Теорема](https://ru.wikipedia.org/wiki/Центральная_предельная_теорема)
18. [t-test #1](https://habr.com/ru/companies/X5Tech/articles/807001/)
19. [t-test #2](https://bytepawn.com/ab-testing-and-the-ttest.html#ab-testing-and-the-ttest)
20. [Welch test](https://habr.com/ru/companies/X5Tech/articles/896182/)
21. [$U$-test (Mann–Whitney)](https://habr.com/ru/companies/avito/articles/709596/)
22. [χ²-test #1](https://habr.com/ru/companies/mygames/articles/677074/)
23. [χ²-test #2](https://bytepawn.com/ab-testing-and-the-chi-squared-test.html#ab-testing-and-the-chi-squared-test)
24. [Bootstrap](https://habr.com/ru/companies/X5Tech/articles/679842/)
25. [Проверка валидности критерия](https://habr.com/ru/companies/X5Tech/articles/706388/)
26. [A/A/B тесты](https://koch-kir.medium.com/не-стоит-проводить-а-а-в-тест-936e9e7a3b96)

**Дополнительные Источники**
1. [A/B тесты для продактов](https://www.youtube.com/live/gMx-juYkNCw)
2. [Статистическая значимость](https://en.wikipedia.org/wiki/Statistical_significance)
3. [Новые подходы к вычисление размера выборки](https://arxiv.org/pdf/2305.16459)
4. [z статистика в python](https://habr.com/ru/articles/557424/)
5. [t статистика в python](https://habr.com/ru/articles/559062/)
