# 2.П1. Последовательное тестирование (Sequential Testing)

> **Модуль:** Квази-эксперименты · **Блок:** практический · **Время:** 2.5 ч · **Опирается на:** 2.01, 1.03, 1.06, 1.П2 · **Статус:** ✅ готово

## Обзор
Сквозной кейс: сервис бронирования отелей тестирует блок «Горящие предложения», а продакт хочет смотреть результаты каждый день. Измеряем цену подглядывания на своём расписании, планируем GST (границы и запас выборки), реализуем mSPRT и выводим настройку τ из плана. Разбираем, что на самом деле делает тяжёлый хвост выручки. Затем прогоняем логи по дням и получаем честную остановку на 6-й день с оценкой +0.94 п.п. Дальше выясняем, почему этому результату нельзя верить: оценка завышена отбором, эффект затухает по когортам, а контрольная метрика на момент остановки ещё не успела сработать. Заканчиваем проверкой отклонений от плана, решением и регламентом для команды. Главный вывод: статистически честная остановка не гарантирует верного продуктового решения.

## Цели занятия
- Планировать GST: считать границы и запас выборки для своего расписания взглядов.
- Реализовывать mSPRT, always-valid p-value и доверительные последовательности, выбирать τ из плана теста.
- Понимать, когда тяжёлый хвост действительно опасен для последовательных методов, а когда нет.
- Отчитываться о рано остановленном тесте честно: завышение оценки, повторные интервалы.
- Отличать затухание эффекта от шума, анализировать когорты, задавать минимальную длительность.
- Понимать, какие отклонения от плана ломают гарантию.

## Материалы
- [Практика](practice.ipynb): задания со свёрнутыми решениями (раскрываются кликом в Colab, Jupyter и VS Code).
- Данные: синтетические логи [data/hotdeals_ab.csv](data/hotdeals_ab.csv), их генерирует скрипт [data/generate_data.py](data/generate_data.py) (в нём же зашиты истинные эффекты).

## Источники
### Основные источники
1. [Johari, Pekelis, Walsh — Always Valid Inference: Bringing Sequential Analysis to A/B Testing](https://arxiv.org/abs/1512.04922)
2. [Waudby-Smith et al. — Time-uniform central limit theory and asymptotic confidence sequences (Annals of Statistics, 2024)](https://doi.org/10.1214/24-AOS2408)
3. [Schultzberg, Ankargren — Choosing a sequential testing framework (Spotify)](https://engineering.atspotify.com/2023/03/choosing-sequential-testing-framework-comparisons-and-discussions)
4. [Sequential Testing (документация GrowthBook)](https://docs.growthbook.io/statistics/sequential)
5. [Kohavi, Deng, Longbotham, Xu — Seven Rules of Thumb for Web Site Experimenters (KDD 2014)](https://exp-platform.com/rules-of-thumb/)
6. [Kohavi et al. — Trustworthy Online Controlled Experiments: Five Puzzling Outcomes Explained (KDD 2012)](https://exp-platform.com/puzzling-outcomes/)
7. Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing* (Cambridge University Press, 2020).
8. [Whitehead — On the bias of maximum likelihood estimation following a sequential test (Biometrika, 1986)](https://doi.org/10.1093/biomet/73.3.573)
9. [Fan, DeMets, Lan — Conditional bias of point estimates following a group sequential test (Journal of Biopharmaceutical Statistics, 2004)](https://doi.org/10.1081/bip-120037195)
10. [Walter et al. — Randomised trials with provision for early stopping for benefit (or harm) (Statistics in Medicine, 2019)](https://doi.org/10.1002/sim.8142)
11. [Wang et al. — On Heavy-user Bias in A/B Testing (CIKM 2019)](https://arxiv.org/abs/1902.02021)
12. [Lindon et al. — Rapid Regression Detection in Software Deployments through Sequential Testing (Netflix, KDD 2022)](https://arxiv.org/abs/2205.14762)

### Дополнительные материалы
1. [Использование последовательного тестирования для уменьшения размера выборки (Т-Банк)](https://habr.com/ru/articles/876984/)
2. [Проблема подглядывания и последовательное А/Б тестирование (X5 Tech)](https://habr.com/ru/companies/X5Tech/articles/926546/)
3. [Proschan, Follmann, Waclawiw — Effects of assumption violations on type I error rate in group sequential monitoring (Biometrics, 1992)](https://doi.org/10.2307/2532704)
