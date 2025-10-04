# Lesson 02 — AB Testing Basics

## Overview
Урок посвящён ключевым элементам дизайна экспериментов: от RCT и пайплайна проверки гипотез до выбора статистических критериев под различные типы метрик. Отдельное внимание уделено ошибкам 1 и 2 рода, определению MDE и типовым проблемам практических запусков.

## Learning goals
- Понять место экспериментов в иерархии доказательности и структуру полного пайплайна A/B тестов.
- Разобраться в классификации тестов и метрик, а также в критериях, используемых для сравнения групп.
- Осознать основные риски (peeking, SRM, нарушения независимости) и способы контроля корректности.

## Session materials
- [Lecture notebook](lecture.ipynb)
- [Seminar notebook](seminar.ipynb)

## References
### Основные источники
1. [Уровень доказательности экспериментов](https://en.wikipedia.org/wiki/Hierarchy_of_evidence)
2. [Рандомизированные Контролируемые Испытания (RCT)](https://en.wikipedia.org/wiki/Randomized_controlled_trial)
3. [Superiority vs Non-inferiority Tests](https://blog.analytics-toolkit.com/2017/case-non-inferiority-designs-ab-testing/)
4. [Типы тестов для two-sample test](https://www.ncss.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Two_Proportions-Non-Inferiority,_Superiority,_Equivalence,_and_Two-Sided_Tests_vs_a_Margin.pdf)
5. [Общий флоу проведения A/B тестов](http://www.machinelearning.ru/wiki/index.php?title=Проверка_статистических_гипотез)
6. [Прокси метрики](https://www.youtube.com/watch?v=fSRKOr3L6AI)
7. [Типы тестов + типы метрик по целям](https://arxiv.org/pdf/2402.11609)
8. [Метрики отношений и дельта метод](https://habr.com/ru/companies/X5Tech/articles/740476/)
9. [Матрица ошибок](https://en.wikipedia.org/wiki/Confusion_matrix#cite_ref-22)
10. [Ошибки 1 и 2 рода](https://ru.wikipedia.org/wiki/Ошибки_првого_и_второго_рода)
11. [Power Analysis](https://chabefer.github.io/STCI/Power.html#basics-of-traditional-power-analysis-using-test-statistics)
12. [Определение размера выборки на исторических данных](https://habr.com/ru/companies/lamoda/articles/707816/)
13. [Определение размера выборки для ratio метрик](https://medium.com/expedia-group-tech/how-to-size-for-online-experiments-with-ratio-metrics-3d57362f1967)
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
26. [A/A/B тесты](https://koch-kir.medium.com/%D0%BD%D0%B5-%D1%81%D1%82%D0%BE%D0%B8%D1%82-%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D1%8C-%D0%B0-%D0%B0-%D0%B2-%D1%82%D0%B5%D1%81%D1%82-936e9e7a3b96)

### Дополнительные материалы
1. [A/B тесты для продактов](https://www.youtube.com/live/gMx-juYkNCw)
2. [Статистическая значимость](https://en.wikipedia.org/wiki/Statistical_significance)
3. [Новые подходы к вычислению размера выборки](https://arxiv.org/pdf/2305.16459)
4. [z статистика в Python](https://habr.com/ru/articles/557424/)
5. [t статистика в Python](https://habr.com/ru/articles/559062/)
