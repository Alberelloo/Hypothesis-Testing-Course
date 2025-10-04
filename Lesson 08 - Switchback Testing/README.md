# Lesson 08 — Switchback Testing

## Overview
Switchback тесты помогают корректно измерять эффект в условиях сетевых внешних воздействий и нарушений SUTVA. Занятие объясняет природу зависимостей между пользователями, вводит базовую реализацию switchback-дизайна и рассматривает практические кейсы.

## Learning goals
- Понять, как сетевые эффекты и нарушения SUTVA искажают результаты классических A/B тестов.
- Освоить принципы построения switchback экспериментов и интерпретации их результатов.
- Познакомиться с реальными кейсами внедрения метода.

## Session materials
- [Lecture notebook](lecture.ipynb)

## References
### Основные источники
1. [Switchback Experiments at Scale](https://arxiv.org/pdf/2009.00148)
2. [Кейс Delivery Club](https://habr.com/ru/companies/deliveryclub/articles/670762/)
3. [Кейс Citymobil. Часть 1](https://habr.com/ru/companies/citymobil/articles/560426/)
4. [Кейс Citymobil. Часть 2](https://habr.com/ru/companies/citymobil/articles/575218/)
5. [How to optimize your switchback A/B test configuration](https://towardsdatascience.com/how-to-optimize-your-switchback-a-b-test-configuration-791a28bee678/)

### Дополнительные материалы
- [EXPF о switchback и MLM-оценке](https://medium.com/statistics-experiments/switchback-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BA%D0%B0%D0%BA-%D0%B1%D0%BE%D1%80%D0%BE%D1%82%D1%8C%D1%81%D1%8F-%D1%81-%D1%81%D0%BE%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC%D0%B8-%D1%8D%D1%84%D1%84%D0%B5%D0%BA%D1%82%D0%B0%D0%BC%D0%B8-%D0%B2-a-b-%D1%82%D0%B5%D1%81%D1%82%D0%B0%D1%85-39aab4f87cf7)
- [Пайплайн для switchback тестов](https://github.com/omar-elmaria/switchback_test_dag)
