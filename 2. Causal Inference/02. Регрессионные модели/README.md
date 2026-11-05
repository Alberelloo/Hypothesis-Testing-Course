# 2.08. Регрессионные модели

> **Модуль:** Квази-эксперименты · **Мини-блок:** Причинно-следственность. Causal Inference · **Время:** 1.5 ч · **Статус:** ✅ готово

## Обзор
Введение в потенциальные исходы охватывает необходимость причинно-следственного анализа, базовые понятия корреляции против причинности и набор классических методов оценки эффектов в наблюдательных данных.

## Цели занятия
- Понять, почему одной корреляции недостаточно и когда требуется causal inference.
- Изучить ключевые инструменты потенциальных исходов, основанных на регрессиях

## Материалы
- [Лекция](lecture.ipynb)
- Папка [data](data/) с исходными наборами для практики.

## Источники
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

### Дополнительные материалы
1. [What If? — учебник по causal inference](https://miguelhernan.org/whatifbook)
2. [Causal Inference: The Mixtape](https://library.fa.ru/files/Imbens.pdf)
3. [Университетский курс по causal inference](https://www.cs.uic.edu/~elena/courses/fall19/cs594cil.html)
4. [Краткий курс по causal inference](https://www.youtube.com/watch?v=CfzO4IEMVUk&list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0)
5. [Мини-курс по causal inference](https://www.youtube.com/watch?v=zvrcyqcN9Wo&t=4243s)
6. [Causal ML Book](https://causalml-book.org/)
7. [Angrist, Krueger (1991): данные о квартале рождения](https://economics.mit.edu/faculty/angrist/data1/data/angkru1991)
8. [Buckles, Hungerman (2013): сезон рождения и характеристики матерей](https://www.nber.org/papers/w14573)
9. [Bound, Jaeger, Baker (1995): слабые инструменты](https://research-portal.st-andrews.ac.uk/en/publications/problems-with-instrumental-variables-estimation-when-the-correlat/)
10. [Lee, McCrary, Moreira, Porter (2022): Valid t-ratio Inference for IV](https://arxiv.org/abs/2010.05058)
11. [Carpenter, Dobkin (2009): минимальный возраст и смертность](https://www.aeaweb.org/articles?id=10.1257/app.1.1.164)
12. [Clark, Martorell (2014): The Signaling Value of a High School Diploma](https://faculty.smu.edu/millimet/classes/eco7321/papers/clark%20martorell%202014.pdf)
