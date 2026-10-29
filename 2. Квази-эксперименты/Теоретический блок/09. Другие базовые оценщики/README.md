# 2.09. Другие базовые оценщики

> **Модуль:** Квази-эксперименты · **Мини-блок:** Причинно-следственность. Potential Outcome Framework · **Время:** 1.5 ч · **Статус:** ✅ готово

## Обзор
Введение в потенциальные исходы охватывает необходимость причинно-следственного анализа, базовые понятия корреляции против причинности и набор классических методов оценки эффектов в наблюдательных данных.

## Цели занятия
- Понять, почему одной корреляции недостаточно и когда требуется causal inference.
- Изучить ключевые инструменты потенциальных исходов: matching, propensity score, difference-in-differences и synthetic control.
- Научиться формулировать предпосылки и выбирать подходящий метод под задачу.

## Материалы
- [Лекция](lecture.ipynb)
- Папка [data](data/) с исходными наборами для практики.

## Источники
### Основные источники
1. [Методы балансировки групп](https://habr.com/ru/companies/X5Tech/articles/780690/)
2. [Propensity Score и IPTW](https://matheusfacure.github.io/python-causality-handbook/11-Propensity-Score.html)
3. [Inverse Probability of Treatment Weighting](https://alexdeng.github.io/causal/rcm.html#ipw)
4. [Matching — часть 1](https://matheusfacure.github.io/python-causality-handbook/10-Matching.html)
5. [Matching — часть 2](https://theeffectbook.net/ch-Matching.html)
6. [Обзор методов matching](https://cran.r-project.org/web/packages/MatchIt/vignettes/matching-methods.html)
7. [Propensity Score Matching](https://www.youtube.com/watch?v=rBv39pK1iEs&t=2148s)
8. [Difference-in-Differences: обзор](https://habr.com/ru/companies/X5Tech/articles/867734/)
9. [Difference-in-Differences: объяснение](https://matheusfacure.github.io/python-causality-handbook/13-Difference-in-Differences.html)
10. [Synthetic Control: статья](https://economics.mit.edu/sites/default/files/publications/jel.20191450.pdf)
11. [Synthetic Control: объяснение](https://matheusfacure.github.io/python-causality-handbook/15-Synthetic-Control.html)
12. [Кейс Synthetic Control от Uber](https://www.youtube.com/watch?v=j5DoJV5S2Ao)
13. [Panel Data & Fixed Effects](https://matheusfacure.github.io/python-causality-handbook/14-Panel-Data-and-Fixed-Effects.html)
14. [Fixed Effects](https://theeffectbook.net/ch-FixedEffects.html)
15. [Обзор методов RCM](https://koch-kir.medium.com/causal-inference-from-observational-data-%D0%B8%D0%BB%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%81%D1%82%D0%B8-a-b-%D1%82%D0%B5%D1%81%D1%82-%D0%B1%D0%B5%D0%B7-a-b-%D1%82%D0%B5%D1%81%D1%82%D0%B0-afb84f2579f2#507b)
16. [Кейс causal inference в X5](https://habr.com/ru/companies/X5Tech/articles/768008/)

### Дополнительные материалы
1. [What If? — учебник по causal inference](https://miguelhernan.org/whatifbook)
2. [Causal Inference: The Mixtape](https://library.fa.ru/files/Imbens.pdf)
3. [Университетский курс по causal inference](https://www.cs.uic.edu/~elena/courses/fall19/cs594cil.html)
4. [Краткий курс по causal inference](https://www.youtube.com/watch?v=CfzO4IEMVUk&list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0)
5. [Мини-курс по causal inference](https://www.youtube.com/watch?v=zvrcyqcN9Wo&t=4243s)
6. [Causal ML Book](https://causalml-book.org/)
