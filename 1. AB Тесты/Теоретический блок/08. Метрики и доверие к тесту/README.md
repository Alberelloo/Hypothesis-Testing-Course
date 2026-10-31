# 1.08. Метрики и доверие к тесту

> **Модуль:** A/B тестирование · **Мини-блок:** Дополнительные главы A/B тестирования · **Время:** 3 ч · **Статус:** ✅ готово

## Обзор
Тест можно провести идеально и всё равно сделать неверный вывод: из-за метрики, которую накрутили, прокси, который не предсказывает цель, или ratio-метрики, у которой в группах разный знаменатель. Занятие разбирает, как выбирать и проверять метрики и какие ловушки интерпретации встречаются чаще всего. Каждая ловушка показана на симуляции с известной истиной: сначала убедительный результат, потом причина, по которой ему нельзя верить, и способ заметить это заранее. В тексте есть шесть коротких вопросов «Проверьте себя» с раскрывающимися ответами.

## Цели занятия
- Различать роли метрик (качество данных, OEC, guardrail, диагностические) и читать результат теста в правильном порядке.
- Понимать, как работает закон Гудхарта, и защищаться от него guardrail- и контрметриками.
- Проверять метрики на корпусе прошлых тестов: чувствительность и согласие с целью; понимать, почему прокси и суррогаты нужно проверять на уровне экспериментов.
- Замечать ловушки интерпретации: метрический SRM, ratio-метрики, потерю телеметрии, неверный триггер, парадокс Симпсона, сегменты, неполные воронки.
- Применять чек-лист доверия к тесту до запуска, во время и после.

## Материалы
- [Лекция](lecture.ipynb)

## Источники
### Основные источники
1. [A Dirty Dozen: Twelve Common Metric Interpretation Pitfalls in Online Controlled Experiments (Dmitriev et al., KDD 2017)](https://www.microsoft.com/en-us/research/uploads/prod/2020/08/2017-08-KDDMetricInterpretationPitfalls.pdf)
2. [Measuring Metrics (Dmitriev, Wu, CIKM 2016)](https://exp-platform.com/Documents/2016CIKM_MeasuringMetrics.pdf)
3. [Data-Driven Metric Development for Online Controlled Experiments: Seven Lessons Learned (Deng, Shi, KDD 2016)](https://doi.org/10.1145/2939672.2939700)
4. [Diluted Treatment Effect Estimation for Trigger Analysis in Online Controlled Experiments (Deng, Hu, WSDM 2015)](https://exp-platform.com/dilution/)
5. [Seven Pitfalls to Avoid when Running Controlled Experiments on the Web (Crook et al., KDD 2009)](https://exp-platform.com/seven-pitfalls/)
6. [The Surrogate Index (Athey, Chetty, Imbens, Kang, NBER w26463)](https://nber.org/papers/w26463.pdf)
7. [Online Experimentation with Surrogate Metrics: Guidelines and a Case Study (Duan, Ba, Zhang, WSDM 2021)](https://arxiv.org/abs/2106.01421)
8. [Focusing on the Long-term: It's Good for Users and Business (Hohnhold, O'Brien, Tang, KDD 2015)](https://research.google/pubs/focus-on-the-long-term-its-better-for-users-and-business/)
9. Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing* (Cambridge University Press, 2020).

### Дополнительные материалы
Дополнительных материалов нет.
