### Занятие №9

**Название** : Causal Inference. Potential Outcome Framework (Rubin-Causal-Model)
**Темы** : 
  * Необходимость причинно-следственного анализа (Casual Inference)
  * Casusation vs Correlation
  * Базовые методы
    * Regressions
      * Виды 
        * Linear Regression
        * Ordinal Regression
        * Zero-inflated Regression
        * Grouped & Dummy Regression
        * Regression Discontinuity Design
      * Проблема Omitted Variable Bias
        * Confounders
        * Instrumental Variables (IV)
      * Non-compliance ситуации и гетерогенные эффекты
    
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
    * Casual Impact
  * Продвинутые методы
    * Doubly-robust Estimator
    * Debiased ML
    * Plug-and-Play Estimator
    * Meta Learners
      * S-learner
      * X-learner
      * T-learner
      * R-learner
      * DR-learner
    * Casual Forest
    
**Цели**
  1. 

**Используемые Источники**
1. [Причинно-следственный анализ](https://matheusfacure.github.io/python-causality-handbook/01-Introduction-To-Causality.html)
2. [Potential Outcome Framework](https://alexdeng.github.io/causal/rcm.html#randomization-and-unconfoundedness)
3. [Correlation vs Casusation](https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation)
4. Что-то про регрессии
5. [Методы Баланисировки групп](https://habr.com/ru/companies/X5Tech/articles/780690/)
6. [Propensity Score и IPTW](https://matheusfacure.github.io/python-causality-handbook/11-Propensity-Score.html)
7. [Inverse  Probability of Treatment Weightening](https://alexdeng.github.io/causal/rcm.html#ipw)
8. [Мэтчинг](https://matheusfacure.github.io/python-causality-handbook/10-Matching.html)
9. [Методы Мэтчинга](https://cran.r-project.org/web/packages/MatchIt/vignettes/matching-methods.html)
10. [Propensity Score Matching](https://www.youtube.com/watch?v=rBv39pK1iEs&t=2148s)
11. [Неплохая статья по Diff-in-Diff](https://habr.com/ru/companies/X5Tech/articles/867734/)
12. [Интуитивное объяснение Diff-in-Diff](https://matheusfacure.github.io/python-causality-handbook/13-Difference-in-Differences.html)
13. [Статья Synthetic Control](https://economics.mit.edu/sites/default/files/publications/jel.20191450.pdf)
14. [Объяснение Synthetic Control](https://matheusfacure.github.io/python-causality-handbook/15-Synthetic-Control.html)
15. [Кейс Synthetic Control от Uber](https://www.youtube.com/watch?v=j5DoJV5S2Ao)



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
