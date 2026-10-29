# 1.П2. Тестирование новой страницы чекаута. A/B тест на z-тесте

> **Модуль:** A/B тестирование · **Блок:** практический · **Время:** 1.5 ч · **Опирается на:** 1.02, 1.03, 1.П1 · **Статус:** ✅ готово

## Обзор
Сквозной кейс A/B теста конверсии: интернет-магазин тестирует новую страницу чекаута на 20% трафика. Сначала дизайним тест: уточняем MDE (абсолютный или относительный), выбираем альтернативу, считаем размер выборки и длительность, смотрим цену неравного сплита. Затем на симуляциях проверяем, что z-тест держит α и даёт заложенную мощность. После теста проверяем качество данных и SRM, оцениваем эффект с доверительными интервалами и принимаем решение по четырём метрикам с разными ролями. Главный результат: контрольная метрика (ошибки оплаты) ловит вред, который исчез бы, если «для надёжности» применить поправку на множественность ко всем метрикам сразу. В конце смотрим, от каких параметров и как зависит размер выборки.

## Цели занятия
- Научиться проходить пайплайн A/B теста целиком: гипотеза → размер выборки и длительность → проверка критерия → анализ → решение.
- Понимать, во что обходятся решения дизайна: неравный сплит, относительный MDE, односторонняя альтернатива.
- Проверять данные перед анализом: дубли, пользователи в обеих группах, Sample Ratio Mismatch.
- Отчитываться эффектом с доверительным интервалом, а не только p-value.
- Разводить метрики по ролям (основная, вторичные, контрольные) и правильно применять поправки на множественность.

## Материалы
- [Практика](practice.ipynb): задания со свёрнутыми решениями (раскрываются кликом в Colab, Jupyter и VS Code).
- Данные: синтетическая выгрузка [data/checkout_ab.csv](data/checkout_ab.csv), её генерирует скрипт [data/generate_data.py](data/generate_data.py) (в нём же зашиты истинные эффекты).

## Источники
### Основные источники
1. [A/B testing and the z-test (Bytepawn)](https://bytepawn.com/ab-testing-and-the-ztest.html)
2. [Power Analysis (Chabé-Ferret, Statistical Tools for Causal Inference)](https://chabefer.github.io/STCI/Power.html#basics-of-traditional-power-analysis-using-test-statistics)
3. [Проверка валидности критерия (X5 Tech)](https://habr.com/ru/companies/X5Tech/articles/706388/)
4. [Schultzberg, Ankargren, Frånberg — Risk-aware product decisions in A/B tests with multiple metrics (Spotify)](https://arxiv.org/abs/2402.11609)
5. [Superiority vs Non-inferiority тесты (Analytics-Toolkit)](https://blog.analytics-toolkit.com/2017/case-non-inferiority-designs-ab-testing/)
6. Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing* (Cambridge University Press, 2020), глава 21 о Sample Ratio Mismatch.

### Дополнительные материалы
1. Исходный семинар, на основе которого сделана практика: [Lesson 02 - AB Testing Basics/seminar.ipynb](<../../../Lesson 02 - AB Testing Basics/seminar.ipynb>) (ячейки 46–62).
