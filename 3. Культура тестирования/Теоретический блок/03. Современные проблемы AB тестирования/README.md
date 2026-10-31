# 3.03. Современные проблемы A/B тестирования

> **Модуль:** Культура тестирования · **Мини-блок:** A/B культура · **Время:** 1.5 ч · **Статус:** ✅ готово

## Обзор
Обзорное занятие о состоянии области на ноябрь 2026 года, в первую очередь для IT-продуктов. Базовая статистика A/B уже встроена в крупные платформы, и фронт сместился: от значимости отдельного теста к ценности всего потока экспериментов, от коротких замеров к долгосрочным эффектам, от взаимодействия пользователей к общим данным обучения. Отдельно разбираем то, чего почти нет в обзорах 2023 года: A/B для AI-продуктов, оффлайн-оценки и замену людей моделями. У каждого результата указан статус источника, потому что многие работы вышли недавно и не прошли рецензирование.

## Цели занятия
- Видеть карту области: что стало стандартом, что частично решено, что появилось нового.
- Понимать, почему значимость часто ложна, и как сравнивают правила решений по суммарной отдаче.
- Знать, что индустрия думает о долгосрочных эффектах и суррогатах и где заканчивается её согласие.
- Распознавать symbiosis bias и проблему пересекающихся тестов.
- Отличать согласие оффлайн-оценки с людьми от её способности предсказывать онлайн-эффект.
- Критически читать заявления о замене A/B-тестов на LLM и агентов.

## Материалы
- [Лекция](lecture.ipynb)

## Источники
### Основные источники
1. [Обзор проблем A/B тестирования (arXiv:2212.11366)](https://arxiv.org/pdf/2212.11366)
2. [Sigerson et al. — Evaluating for the Long Term: Learnings from Industry (2026)](https://arxiv.org/abs/2608.08043)
3. [Chou et al. — Evaluating Decision Rules Across Many Weak Experiments (KDD 2025)](https://arxiv.org/abs/2502.08763)
4. [Berman, Van den Bulte — False Discovery in A/B Testing (Management Science, 2022)](https://pubsonline.informs.org/doi/10.1287/mnsc.2021.4207)
5. [Spotify — Experiments with Learning](https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework)
6. [Azevedo et al. — A/B Testing with Fat Tails (JPE, 2020)](https://econpapers.repec.org/RePEc:ucp:jpolec:doi:10.1086/710607)
7. [Zhang et al. — Evaluating the Surrogate Index Using 200 A/B Tests at Netflix](https://arxiv.org/abs/2311.11922)
8. [Athey, Chetty, Imbens, Kang — The Surrogate Index](https://opportunityinsights.org/paper/the-surrogate-index/)
9. [Brennan et al. — Reducing Symbiosis Bias Through Better A/B Tests of Recommendation Algorithms (WWW 2025)](https://arxiv.org/abs/2309.07107)
10. [Hosseini — Multi-Experiment Analysis (LinkedIn, 2026)](https://arxiv.org/abs/2604.16671)
11. [Schultzberg — When Can You Ship on Evals Alone? (Spotify, 2026)](https://arxiv.org/abs/2610.10142)
12. [Persson, Schultzberg, Ankargren — Statistical Foundations of LLM-based A/B Testing (Spotify, 2026)](https://arxiv.org/abs/2606.17165)
13. [Hut, Masoero — Can AI Agents Simulate A/B Test Outcomes? (Amazon, 2026)](https://arxiv.org/abs/2608.02345)
14. [Платформа A/B-экспериментов Trisigma (Авито)](https://habr.com/ru/companies/avito/articles/947358/)

### Дополнительные материалы
1. [Agent A/B: A/B-тесты с LLM-агентами на живых сайтах](https://arxiv.org/abs/2504.09723)
2. [A/B Agent: агент для стратегий рекомендаций](https://arxiv.org/abs/2608.04625)
3. [Experimentation Accelerator (Adobe)](https://arxiv.org/abs/2602.13852)
4. [Si — Tackling Interference Induced by Data Training Loops](https://arxiv.org/abs/2310.17496)
5. [Bibaut et al. — Learning the Covariance of Treatment Effects Across Many Weak Experiments](https://arxiv.org/abs/2402.17637)
6. [Пять вопросов о CUPED (ByteDance)](https://arxiv.org/abs/2606.18750)
7. [Шесть причин, почему ваши A/B-тесты не работают (Ozon)](https://habr.com/en/companies/ozontech/articles/712306)
8. [Самописная платформа Trisigma (Авито)](https://habr.com/ru/companies/avito/articles/890272/)
9. [OpenAI объясняет подхалимство ChatGPT (TechCrunch)](https://techcrunch.com/2025/04/29/openai-explains-why-chatgpt-became-too-sycophantic)
10. [Разбор релиза GPT-4o (Cointelegraph)](https://cointelegraph.com/news/openai-ignored-experts-overly-agreeable-chatgpt-model-release)
11. [Разбор сделки Amplitude и Statsig (Convert)](https://www.convert.com/blog/a-b-testing/statsig-moves-to-amplitude/)
