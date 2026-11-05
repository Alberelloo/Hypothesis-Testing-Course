# 2.03. Кластерные A/B тесты

> **Модуль:** Квази-эксперименты · **Мини-блок:** Альтернатива A/B тестам · **Время:** 3 ч · **Статус:** ✅ готово

## Обзор
Иногда воздействие нельзя назначить пользователю: мешают готовые группы, интерференция или география. Занятие показывает, как рандомизировать кластеры, сколько это стоит по мощности и как корректно анализировать результаты при малом числе кластеров.

## Цели занятия
- Понять, когда нужен кластерный дизайн, и выбрать его среди других альтернатив A/B-тесту.
- Планировать мощность через ICC и эффект дизайна.
- Выбрать схему рандомизации и соответствующий ей метод анализа.
- Строить кластеры на графе и проверять остаточную интерференцию.
- Проводить геоэксперименты и оценивать их шум с помощью плацебо.

## Материалы
- [Лекция](lecture.ipynb)
- Папка [data](data/) с данными для примера со школами.

## Источники
### Основные источники
1. [Imai, King, Nall (2009): парный дизайн в кластерных экспериментах](https://gking.harvard.edu/publication/the-essential-role-of-pair-matching-in-cluster-randomized-experiments-with-application-to-the-mexican-universal-health-insurance-evaluation/)
2. [Abadie, Athey, Imbens, Wooldridge: When Should You Adjust Standard Errors for Clustering?](https://arxiv.org/abs/1710.02926)
3. [Cameron, Miller (2015): A Practitioner's Guide to Cluster-Robust Inference](https://jhr.uwpress.org/content/50/2/317)
4. [MacKinnon, Nielsen, Webb: Cluster-Robust Inference, A Guide to Empirical Practice](https://arxiv.org/pdf/2205.03285)
5. [Ugander et al. (2013): Graph Cluster Randomization](https://arxiv.org/abs/1305.6979)
6. [Eckles, Karrer, Ugander: Design and Analysis of Experiments in Networks](https://arxiv.org/abs/1404.7530)
7. [Hudgens, Halloran (2008): Toward Causal Inference With Interference](https://pmc.ncbi.nlm.nih.gov/articles/PMC2600548)
8. [Viviano et al.: Causal Clustering](https://arxiv.org/abs/2310.14983)
9. [Vaver, Koehler (2011): Measuring Ad Effectiveness Using Geo Experiments](https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/)
10. [Обзор методов для неравных кластеров](https://pmc.ncbi.nlm.nih.gov/articles/PMC8320970/)

### Кейсы
1. [Meta: Network Experimentation at Scale](https://ar5iv.labs.arxiv.org/html/2012.08591)
2. [Meta: How Meta tests products with strong network effects](https://medium.com/@AnalyticsAtMeta/how-meta-tests-products-with-strong-network-effects-96003a056c2c)
3. [LinkedIn: Detecting Network Effects](https://faculty.washington.edu/msaveski/assets/publications/2017_detecting_network_effects/paper.pdf)
4. [Airbnb: мета-эксперимент с кластерной рандомизацией](https://business.columbia.edu/faculty/research/reducing-interference-bias-online-marketplace-experiments-using-cluster)
5. [Авито: почему A/B-тест не подходит для оценки ранжирования](https://habr.com/ru/companies/avito/articles/1043880/)
6. [Авито: сетап A/B-теста, снизивший MDE выручки в 2 раза](https://habr.com/ru/companies/avito/articles/929894/)
7. [Авито: подбор групп генетическим алгоритмом](https://habr.com/ru/companies/avito/articles/1040162/)
8. [X5: A/B-тестирование на 15 000 офлайн-магазинах](https://habr.com/ru/companies/X5Tech/articles/466349/)
9. [Google: Time-Based Regression](https://research.google/pubs/estimating-ad-effectiveness-using-geo-experiments-in-a-time-based-regression-framework/)
10. [Google: Trimmed Match Design](https://pdf.arxiv.org/pdf/2105.07060)
11. [Meta: GeoLift](https://rdrr.io/github/facebookincubator/GeoLift/f/website/docs/Methodology/Methodology.md)
12. [DoorDash: кластеризованные ошибки на практике](https://careersatdoordash.com/?p=6696)

### Дополнительные материалы
1. Hayes, Moulton. Cluster Randomised Trials: учебник.
2. [Кластерные A/B-тесты: обзор на Хабре](https://habr.com/ru/companies/otus/articles/924356/)
