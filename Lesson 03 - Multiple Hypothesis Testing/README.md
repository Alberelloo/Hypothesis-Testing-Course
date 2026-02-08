# Lesson 03 — Multiple Hypothesis Testing

## Обзор
Занятие раскрывает проблемы множественных сравнений: как p-hacking и рост вероятности ложных срабатываний влияют на интерпретацию результатов. Рассматриваются ключевые подходы к контролю FWER и FDR, а также практические аспекты планирования экспериментов с несколькими гипотезами.

## Цели занятия
- Понять, почему в многократных проверках стандартные критерии и уровни значимости перестают работать без корректировок.
- Освоить популярные методы контроля ошибки первого рода (Bonferroni, Holm, Šidák) и доли ложных открытий (Benjamini–Hochberg, Benjamini–Yekutieli).
- Научиться учитывать множественные сравнения при планировании A/B тестов и принятии решений.

## Session materials
- [Лекция](lecture.ipynb)
- [Презентация по принятию решений на множестве метрик](https://docs.google.com/presentation/d/1v7PzCJONgs8wFC6D61VXhpF6vIv-lPNBfxbF0NQP1hg/edit?usp=sharing)

## Источники
### Основные источники
1. Georgi Z. Georgiev, *Statistical Methods in Online A/B Testing* (глава 6)
2. [Проблема множественного сравнения гипотез](https://en.wikipedia.org/wiki/Multiple_comparisons_problem)
3. [Family-Wise Error Rate](http://www.machinelearning.ru/wiki/index.php?title=FWER)
4. [False Discovery Rate](http://www.machinelearning.ru/wiki/index.php?title=FDR)
5. [Поправки на множественное сравнение гипотез](https://ru.wikipedia.org/wiki/Поправка_на_множественную_проверку_гипотез)
6. [Краткий обзор методов множественных проверок](https://habr.com/ru/articles/818287/)
7. [Поправки на множественное тестирование в A/B тестах](https://habr.com/ru/companies/X5Tech/articles/842426/)
8. [Поправки на множественное тестирование на практике](https://habr.com/ru/articles/772940/)
9. [Оптимальное разбиение трафика по группам](https://habr.com/ru/companies/X5Tech/articles/763656/)
10. [Принятие решения на множестве метрик от Sporify](https://arxiv.org/pdf/2402.11609)
    
### Дополнительные материалы
- Дополнительных материалов нет.
