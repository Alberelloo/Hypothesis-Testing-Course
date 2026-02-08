# Lesson 09 — Causal Discovery (Graphical Causal Model)

## Обзор
Урок знакомит с графовыми моделями причинности: от описания процессов генерации данных до инструментов идентификации причинных эффектов. Разбираются Directed Acyclic Graphs, d-separation, do-оператор, критерии Backdoor/Frontdoor и способы проверки гипотез о структуре графа.

## Цели занятия
- Понять, как DAG описывает причинные зависимости и чем он отличается от потенциальных исходов.
- Научиться использовать d-separation и do-оператор для определения, какие переменные нужно контролировать.
- Оценивать уверенность в структуре DGP и знакомиться с инструментами библиотеки DoWhy.

## Материалы
- [Лекция](lecture.ipynb)

## Источники
### Основные источники
1. [Association vs Causation](https://biologyinsights.com/association-vs-causation-why-it-matters-in-biology/)
2. [Глава по GCM](https://alexdeng.github.io/causal/cgm.html#structural-equation-model-causal-diagram-and-d-separation)
3. [Идентификация](https://theeffectbook.net/ch-Identification.html)
4. [Типы путей](https://theeffectbook.net/ch-CausalPaths.html)
5. [Парадокс Берксона](https://ru.wikipedia.org/wiki/Парадокс_Берксона)
6. [d-separation (объяснение #1)](https://www.andrew.cmu.edu/user/scheines/tutor/d-sep.html)
7. [d-separation (объяснение #2)](https://networkx.org/documentation/stable/reference/algorithms/d_separation.html)
8. [d-separation (объяснение #3)](https://bayes.cs.ucla.edu/BOOK-2K/d-sep.html)
9. [d-separation (объяснение #4)](https://ericmjl.github.io/causality/03-d-separation/)
10. [do-оператор](https://ericmjl.github.io/causality/07-do-operator/)
11. [Frontdoor criterion](https://readmedium.com/causal-inference-part-xii-front-door-criterion-38bec5172f3e)
12. [Backdoor criterion](https://readmedium.com/causal-inference-part-xi-backdoor-criterion-e29627a1da0e)
13. [Уверенность в DGP](https://theeffectbook.net/ch-CausalitywithLessModeling.html)
14. [Опровержение DAG](https://www.pywhy.org/dowhy/main/example_notebooks/gcm_falsify_dag.html)

### Дополнительные материалы
- [What If? — учебник по causal inference](https://miguelhernan.org/whatifbook)
- [Causal Inference: The Mixtape](https://library.fa.ru/files/Imbens.pdf)
- [Курс по causal inference](https://www.youtube.com/watch?v=CfzO4IEMVUk&list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0)
- [Мини-курс по причинно-следственности](https://github.com/DataForScience/Causality?tab=readme-ov-file)
- [The Effect Book](https://theeffectbook.net/index.html)
- [DoWhy: примеры по GCM](https://www.pywhy.org/dowhy/main/example_notebooks/nb_index.html)
