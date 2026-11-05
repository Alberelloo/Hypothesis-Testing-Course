# 3.01. Мета-анализ A/B тестов

> **Модуль:** Культура тестирования · **Мини-блок:** A/B культура · **Время:** 1.5 ч · **Статус:** ✅ готово

## Обзор
Мета-анализ объединяет результаты независимых исследований, позволяя повысить статистическую мощность и устойчивость выводов. Урок рассматривает типы мета-анализа, методы синтеза и визуализации, а также демонстрирует пример реализации в Python.

## Цели занятия
- Понять назначение мета-анализа и его ограничения.
- Разобраться в ключевых подходах: fixed- и random-effects модели, методы синтеза значимостей, регрессионный мета-анализ.
- Освоить базовые инструменты визуализации (forest, funnel plot) и повторить пример вычислений в Python.

## Материалы
- [Лекция](lecture.ipynb)
- [Пример разбора мета-анализа (PDF)](meta_analysis_example.pdf)
- [Данные Haloperidol](Haloperidol.txt)

## Источники
### Основные источники
1. [Конспект курса по мета-анализу](http://www.stat-help.com/meta.pdf)
2. [Что такое мета-анализ](https://en.wikipedia.org/wiki/Meta-analysis)
3. [Синтез значимостей в мета-анализах](https://habr.com/ru/companies/X5Tech/articles/862202/)
4. [Регрессионный мета-анализ](https://en.wikipedia.org/wiki/Meta-regression)
5. [Weighted z-score в eBay](https://innovation.ebayinc.com/stories/increase-a-b-testing-power-by-combining-experiments/)
6. [Forest plot](https://en.wikipedia.org/wiki/Forest_plot)
7. [Funnel plot](https://www.researchgate.net/publication/24096583_Funnel_Plots_in_Meta-analysis)
8. [Мета-анализ в Python](https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-022-01673-y)

### Дополнительные материалы
1. [Курс по мета-анализу](https://www.coursera.org/learn/systematic-review)
2. [Учебник по мета-анализу](https://link.springer.com/book/10.1007/978-981-15-5032-4)
3. [Оценка общего эффекта от экспериментов от Airbnb](https://dl.acm.org/doi/epdf/10.1145/3219819.3219905)
2. [Goeman, Rosenblatt, Nichols (2019): The harmonic mean p-value](https://pmc.ncbi.nlm.nih.gov/articles/PMC6876242)
3. [Vovk, Wang (2020): Combining p-values via averaging](https://arxiv.org/abs/1212.4966)
4. [Bradburn et al. (2007): Much ado about nothing](https://www.bibsonomy.org/bibtex/2e637e4988f9f47ea54c20116f8602340/jepcastel)
5. [Whitlock (2005): the weighted Z-method](https://scilit.com/publications/ab05b8b6dc9402262c9851a832654a7f)
