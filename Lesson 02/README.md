### Занятие №2 Введение в тестирование гипотез: A/B тестирование: основы и дизайн

**Название** : Методы ускорения A/B тестов

**Темы** : 
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
  * Проверка корректности критерия
  * Основные проблемы тестов
    
  **Цели**

  1.  
  2.  
  3.  

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
11. [Сборник статистических критериев #1](https://www.statskingdom.com/index.html)
12. [Сборник статистических критериев #2](https://www.biostathandbook.com/testchoice.html)
13. [z-test](https://bytepawn.com/ab-testing-and-the-ztest.html#ab-testing-and-the-ztest)
14. [t-test #1](https://habr.com/ru/companies/X5Tech/articles/807001/)
15. [t-test #2](https://bytepawn.com/ab-testing-and-the-ttest.html#ab-testing-and-the-ttest)
16. [Welch test](https://habr.com/ru/companies/X5Tech/articles/896182/)
17. [U-test (Mann–Whitney)](https://habr.com/ru/companies/avito/articles/709596/)
18. [χ²-test #1](https://habr.com/ru/companies/mygames/articles/677074/)
19. [χ²-test #2](https://bytepawn.com/ab-testing-and-the-chi-squared-test.html#ab-testing-and-the-chi-squared-test)
20. [Bootstrap](https://habr.com/ru/companies/X5Tech/articles/679842/)
21. [Проверка валидности критерия](https://habr.com/ru/companies/X5Tech/articles/706388/)
