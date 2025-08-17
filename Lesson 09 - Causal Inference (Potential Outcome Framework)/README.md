### Занятие №9

**Название** : Causal Inference. Potential Outcome Framework (Rubin-Causal-Model)

___
**Часть 1. Основы Casual Inference (Базовые методы)**

**Темы** : 
  * Необходимость причинно-следственного анализа (Casual Inference)
  * Casusation vs Correlation
  * Базовые методы
    * Regressions
      * Linear Regression 
      * Проблема Omitted Variable Bias
      * Instrumental Variables (IV)
      * Non-compliance ситуации
      * Regression Discontinuity Design
    * Propensity Score. Inverse  Probability of Treatment Weightening  (IPTW)
    * Matching
      * Mahalanobis Distance Matching
      * Coarsened Exact Matching
      * Mahalanobis Distance Matching
      * Curse of Dimensionality
      * Propensity Score Matching (PSM) 
    * Difference-in-Difference
    * Synthetic Control
    * Panel Data & Fixed Effects
___
**Часть 2. ML в Casual Inference (Продвинутые методы)**

**Темы** : 
* Продвинутые методы
  * Doubly-robust Estimator
  * Plug-and-Play Estimator
  * Meta Learners
    * S-learner
    * X-learner
    * T-learner
    * R-learner
    * Domain Adaptation learner
  * Debiased ML
  * Casual Forest
  * Casual Impact
* Кейс-стади  

___
**Цели**
  1. 



**Используемые Источники**

`Часть 1`

1. [Причинно-следственный анализ](https://matheusfacure.github.io/python-causality-handbook/01-Introduction-To-Causality.html)
2. [Potential Outcome Framework](https://alexdeng.github.io/causal/rcm.html#randomization-and-unconfoundedness)
3. [Correlation vs Casusation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation)
4. [Линейная регсессия #1](https://matheusfacure.github.io/python-causality-handbook/05-The-Unreasonable-Effectiveness-of-Linear-Regression.html)
5. [Линейная регсессия #2](https://theeffectbook.net/ch-StatisticalAdjustment.html)
6. [Включение переменных в регрессию](https://matheusfacure.github.io/python-causality-handbook/07-Beyond-Confounders.html)
7. [Instrumental Variables](https://matheusfacure.github.io/python-causality-handbook/08-Instrumental-Variables.html)
8. [Non-compliance ситуации](https://matheusfacure.github.io/python-causality-handbook/09-Non-Compliance-and-LATE.html)
9. [Regression Discontinuity Design #1](https://matheusfacure.github.io/python-causality-handbook/16-Regression-Discontinuity-Design.html)
10. [Regression Discontinuity Design #2](https://theeffectbook.net/ch-RegressionDiscontinuity.html)
11. [Методы Баланисировки групп](https://habr.com/ru/companies/X5Tech/articles/780690/)
12. [Propensity Score и IPTW](https://matheusfacure.github.io/python-causality-handbook/11-Propensity-Score.html)
13. [Inverse  Probability of Treatment Weightening](https://alexdeng.github.io/causal/rcm.html#ipw)
14. [Мэтчинг #1](https://matheusfacure.github.io/python-causality-handbook/10-Matching.html)
15. [Мэтчинг #2](https://theeffectbook.net/ch-Matching.html)
16. [Методы Мэтчинга](https://cran.r-project.org/web/packages/MatchIt/vignettes/matching-methods.html)
17. [Propensity Score Matching](https://www.youtube.com/watch?v=rBv39pK1iEs&t=2148s)
18. [Неплохая статья по Diff-in-Diff](https://habr.com/ru/companies/X5Tech/articles/867734/)
19. [Интуитивное объяснение Diff-in-Diff](https://matheusfacure.github.io/python-causality-handbook/13-Difference-in-Differences.html)
20. [Статья Synthetic Control](https://economics.mit.edu/sites/default/files/publications/jel.20191450.pdf)
21. [Объяснение Synthetic Control](https://matheusfacure.github.io/python-causality-handbook/15-Synthetic-Control.html)
22. [Кейс Synthetic Control от Uber](https://www.youtube.com/watch?v=j5DoJV5S2Ao)
23. [Panel Data & Fixed Effects](https://matheusfacure.github.io/python-causality-handbook/14-Panel-Data-and-Fixed-Effects.html)
24. [Fixed Effects](https://theeffectbook.net/ch-FixedEffects.html)

`Часть 2`

1. [Doubly-robust Estimator](https://matheusfacure.github.io/python-causality-handbook/12-Doubly-Robust-Estimation.html)
2. [Plug-and-Play Estimator](https://matheusfacure.github.io/python-causality-handbook/20-Plug-and-Play-Estimators.html)
3. [Meta Learners](https://matheusfacure.github.io/python-causality-handbook/21-Meta-Learners.html)
4. [Advanced методы моделирования Casual Inference](https://www.youtube.com/watch?v=Kx6W-Jq3OWE)
5. 


[Статья Casual Impact](https://projecteuclid.org/journals/annals-of-applied-statistics/volume-9/issue-1/Inferring-causal-impact-using-Bayesian-structural-time-series-models/10.1214/14-AOAS788.full)
[Объяснение Casual Impact](https://www.youtube.com/watch?v=0_bl0A-cXcY)

[Кейс приминения Casual Inference от X5](https://habr.com/ru/companies/X5Tech/articles/768008/)
[Краткий обзор методов RCM](https://koch-kir.medium.com/causal-inference-from-observational-data-или-как-провести-а-в-тест-без-а-в-теста-afb84f2579f2#507b)

**Доп источники**
* [Учебник по Casual Inference #1](https://miguelhernan.org/whatifbook)
* [Учебник по Casual Inference #2](https://library.fa.ru/files/Imbens.pdf)
* [Университетский курс по Casual Inference](https://www.cs.uic.edu/~elena/courses/fall19/cs594cil.html)
* [Краткий курс по Casual Inference](https://www.youtube.com/watch?v=CfzO4IEMVUk&list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0)
* [Мини-курс по Casual Inference](https://www.youtube.com/watch?v=zvrcyqcN9Wo&t=4243s)
* [Книга ML В Casual Inference](https://causalml-book.org/)
