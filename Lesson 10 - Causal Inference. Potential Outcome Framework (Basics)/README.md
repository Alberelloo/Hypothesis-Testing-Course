# Lesson 10 — Causal Inference: Potential Outcome Framework (Basics)

## Overview
Введение в потенциальные исходы охватывает необходимость причинно-следственного анализа, базовые понятия корреляции против причинности и набор классических методов оценки эффектов в наблюдательных данных.

## Learning goals
- Понять, почему одной корреляции недостаточно и когда требуется causal inference.
- Изучить ключевые инструменты потенциальных исходов: регрессии, IV, matching, propensity score, difference-in-differences и synthetic control.
- Научиться формулировать предпосылки и выбирать подходящий метод под задачу.

## Session materials
- [Lecture notebook](lecture.ipynb)
- Папка [data](data/) с исходными наборами для практики.

## References
### Основные источники
1. [Введение в причинно-следственный анализ](https://matheusfacure.github.io/python-causality-handbook/01-Introduction-To-Causality.html)
2. [Potential Outcome Framework](https://alexdeng.github.io/causal/rcm.html#randomization-and-unconfoundedness)
3. [Correlation vs Causation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation)
4. [Линейная регрессия — часть 1](https://matheusfacure.github.io/python-causality-handbook/05-The-Unreasonable-Effectiveness-of-Linear-Regression.html)
5. [Линейная регрессия — часть 2](https://theeffectbook.net/ch-StatisticalAdjustment.html)
6. [Включение переменных в регрессию](https://matheusfacure.github.io/python-causality-handbook/07-Beyond-Confounders.html)
7. [Instrumental Variables](https://matheusfacure.github.io/python-causality-handbook/08-Instrumental-Variables.html)
8. [Non-compliance ситуации](https://matheusfacure.github.io/python-causality-handbook/09-Non-Compliance-and-LATE.html)
9. [Regression Discontinuity Design — часть 1](https://matheusfacure.github.io/python-causality-handbook/16-Regression-Discontinuity-Design.html)
10. [Regression Discontinuity Design — часть 2](https://theeffectbook.net/ch-RegressionDiscontinuity.html)
11. [Методы балансировки групп](https://habr.com/ru/companies/X5Tech/articles/780690/)
12. [Propensity Score и IPTW](https://matheusfacure.github.io/python-causality-handbook/11-Propensity-Score.html)
13. [Inverse Probability of Treatment Weighting](https://alexdeng.github.io/causal/rcm.html#ipw)
14. [Matching — часть 1](https://matheusfacure.github.io/python-causality-handbook/10-Matching.html)
15. [Matching — часть 2](https://theeffectbook.net/ch-Matching.html)
16. [Обзор методов matching](https://cran.r-project.org/web/packages/MatchIt/vignettes/matching-methods.html)
17. [Propensity Score Matching](https://www.youtube.com/watch?v=rBv39pK1iEs&t=2148s)
18. [Difference-in-Differences: обзор](https://habr.com/ru/companies/X5Tech/articles/867734/)
19. [Difference-in-Differences: объяснение](https://matheusfacure.github.io/python-causality-handbook/13-Difference-in-Differences.html)
20. [Synthetic Control: статья](https://economics.mit.edu/sites/default/files/publications/jel.20191450.pdf)
21. [Synthetic Control: объяснение](https://matheusfacure.github.io/python-causality-handbook/15-Synthetic-Control.html)
22. [Кейс Synthetic Control от Uber](https://www.youtube.com/watch?v=j5DoJV5S2Ao)
23. [Panel Data & Fixed Effects](https://matheusfacure.github.io/python-causality-handbook/14-Panel-Data-and-Fixed-Effects.html)
24. [Fixed Effects](https://theeffectbook.net/ch-FixedEffects.html)
25. [Обзор методов RCM](https://koch-kir.medium.com/causal-inference-from-observational-data-%D0%B8%D0%BB%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%81%D1%82%D0%B8-a-b-%D1%82%D0%B5%D1%81%D1%82-%D0%B1%D0%B5%D0%B7-a-b-%D1%82%D0%B5%D1%81%D1%82%D0%B0-afb84f2579f2#507b)
26. [Кейс causal inference в X5](https://habr.com/ru/companies/X5Tech/articles/768008/)

### Дополнительные материалы
- [What If? — учебник по causal inference](https://miguelhernan.org/whatifbook)
- [Causal Inference: The Mixtape](https://library.fa.ru/files/Imbens.pdf)
- [Университетский курс по causal inference](https://www.cs.uic.edu/~elena/courses/fall19/cs594cil.html)
- [Краткий курс по causal inference](https://www.youtube.com/watch?v=CfzO4IEMVUk&list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0)
- [Мини-курс по causal inference](https://www.youtube.com/watch?v=zvrcyqcN9Wo&t=4243s)
- [Causal ML Book](https://causalml-book.org/)
