# 2.П2. Synthetic Control

> **Модуль:** Квази-эксперименты · **Блок:** практический · **Время:** 3 ч · **Опирается на:** 2.09, 2.03 · **Статус:** ✅ готово

## Обзор
Сквозной кейс: сервис доставки запустил платную подписку в Екатеринбурге без A/B-теста, и руководство ждёт решения о раскатке. Реализуем синтетический контроль и получаем +11.7% при точке окупаемости +9.9%, значимо и с красивым графиком. Основная часть практики отвечает на вопрос, можно ли этому верить: проверяем применимость метода, подгонку на отложенных данных, плацебо, бэкдейтинг, конформный вывод, устойчивость к донорам и спецификациям, A/A и контрольную метрику. Первая оценка проходит стандартные проверки, но проваливает две последние: часть разрыва создали проблемы с донорами. После очистки эффект равен +4.2–5.3%, и подписка не окупается. Заканчиваем Synthetic DiD, паспортом валидации и регламентом для команды. Главный вывод: значимый результат не доказывает эффект, доверие дают только проверки, которые могли провалиться.

## Цели занятия
- Реализовать синтетический контроль: веса, предикторы, выбор настроек на отложенных данных.
- Понимать, когда метод применять нельзя, и уметь ответить «оценить нельзя».
- Различать проверки по смыслу: подгонка, шум, устойчивость, сам рецепт, причина разрыва.
- Использовать плацебо, бэкдейтинг и конформный вывод и знать их ограничения.
- Отличать обоснованное исключение доноров от перебора спецификаций.
- Реализовать Synthetic DiD и сверить его с опубликованными результатами.
- Собирать паспорт валидации и принимать решение относительно бизнес-порога, а не нуля.

## Материалы
- [Практика](practice.ipynb): задания со свёрнутыми решениями (раскрываются кликом в Colab, Jupyter и VS Code). Целиком выполняется около 4 минут.
- Данные: синтетическая панель [data/delivery_panel.csv](data/delivery_panel.csv), свойства городов [data/cities.csv](data/cities.csv), журнал событий [data/events.csv](data/events.csv) и истинный эффект [data/truth.csv](data/truth.csv). Всё это генерирует скрипт [data/generate_data.py](data/generate_data.py), в нём же зашиты заложенные проблемы.
- [data/california_cigsale.csv](data/california_cigsale.csv): данные из лекции 2.09 для сверки Synthetic DiD с опубликованными числами.

## Источники
### Основные источники
1. [Abadie — Using Synthetic Controls: Feasibility, Data Requirements, and Methodological Aspects (JEL, 2021)](https://economics.mit.edu/sites/default/files/publications/jel.20191450.pdf)
2. [Arkhangelsky, Athey, Hirshberg, Imbens, Wager — Synthetic Difference-in-Differences (AER, 2021)](https://www.aeaweb.org/doi/10.1257/aer.20190159)
3. [Clarke, Pailañir, Athey, Imbens — Synthetic Difference-in-Differences Estimation](https://arxiv.org/abs/2301.11859)
4. [Ferman, Pinto, Possebom — Cherry Picking with Synthetic Controls (JPAM, 2020)](https://mpra.ub.uni-muenchen.de/85138/1/MPRA_paper_85138.pdf)
5. [Chernozhukov, Wüthrich, Zhu — An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Controls (JASA, 2021)](https://arxiv.org/abs/1712.09089)
6. [Kaul, Klößner, Pfeifer, Schieler — Synthetic Control Methods: Never Use All Pre-Intervention Outcomes Together With Covariates](https://mpra.ub.uni-muenchen.de/83790/1/MPRA_paper_83790.pdf)
7. [Abadie, Zhao — Synthetic Controls for Experimental Design](https://arxiv.org/abs/2108.02196)

### Кейсы
1. [Wildberries: синтетический контроль для оценки офлайн и онлайн экспериментов](https://habr.com/ru/companies/wildberries/articles/885602/)
2. [Uber: Synthetic Control Experimentation Framework (PyData Amsterdam 2019)](https://pydata.org/amsterdam2019/schedule/presentation/19/ubers-synthetic-control-experimentation-framework-when-ab-tests-are-not-possible/)
3. [Uber: Experimental Design For Causal Inference Through An Optimization Lens](https://arxiv.org/abs/2408.09607)
4. [Netflix: Round 2: A Survey of Causal Inference Applications at Netflix](https://netflixtechblog.com/round-2-a-survey-of-causal-inference-applications-at-netflix-fd78328ee0bb)

### Дополнительные материалы
1. [Firpo, Possebom — Synthetic Control Method: Inference, Sensitivity Analysis and Confidence Sets](https://ideas.repec.org/a/bpj/causin/v6y2018i2p26n1.html)
2. [Klößner, Kaul, Pfeifer, Schieler — Comparative politics and the synthetic control method revisited](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6214290/)
3. [Doudchenko, Imbens — Balancing, Regression, Difference-In-Differences and Synthetic Control Methods: A Synthesis](https://arxiv.org/abs/1610.07748)
4. [Ben-Michael, Feller, Rothstein — The Augmented Synthetic Control Method](https://arxiv.org/abs/1811.04170)
