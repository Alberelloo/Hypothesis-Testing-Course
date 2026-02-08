# Lesson 05 — Sequential Testing

## Обзор
Последовательное тестирование позволяет останавливать эксперименты в любой момент без роста уровня ложных срабатываний. Урок объясняет проблему подглядывания, знакомит с классическими и современными методами (SPRT, mSPRT, AVI, GST) и сравнивает их с фиксированным горизонтом.

## Цели занятия
- Разобраться, почему peeking ломает фиксированные тесты и как последовательные процедуры решают эту проблему.
- Научиться отличать и применять основные алгоритмы последовательного тестирования.
- Сравнивать sequential-подходы между собой и со стандартными fixed-horizon A/B тестами.

## Материалы
- [Лекции](lecture.ipynb)

## Источники
### Основные источники
1. [Sequential Probability Ratio Test (лекция)](https://nowak.ece.wisc.edu/ece830/ece830_fall11_lecture9.pdf)
2. [Sequential Probability Ratio Test (реализация)](https://towardsdatascience.com/experiments-peeking-and-optimal-stopping-954506cec665/)
3. [mSPRT в Райффайзенбанке](https://www.youtube.com/watch?v=B5CfU2jV-nY&t=483s)
4. [mSPRT: практическое объяснение](https://websitelytics.top/blog/post/msprt/)
5. [Always Valid Inference (статья)](https://arxiv.org/pdf/1512.04922)
6. [Always Valid Inference (презентация)](https://simons.berkeley.edu/sites/default/files/docs/5572/simonsrj.pdf)
7. [Group Sequential Testing: объяснение](https://habr.com/ru/companies/tbank/articles/876984/)
8. [Group Sequential Testing: реализация](https://matteocourthoud.github.io/post/group_sequential_testing/)
9. [Сравнение последовательных методов](https://engineering.atspotify.com/2023/03/choosing-sequential-testing-framework-comparisons-and-discussions)

### Дополнительные материалы
- [Fixed-Power Design от Spotify](https://arxiv.org/abs/2405.03487)
- [YEAST от Zalando](https://arxiv.org/pdf/2406.16523v1)
- [Corrected-alpha Approach](https://arxiv.org/pdf/1905.10493)
- [Sequential Analysis: Hypothesis Testing and Changepoint Detection](https://www.amazon.com/Sequential-Analysis-Hypothesis-Changepoint-Probability/dp/1439838208)
- [Sequential Experimentation in Clinical Trials](https://www.amazon.com/Sequential-Experimentation-Clinical-Trials-Statistics/dp/1461461138)
