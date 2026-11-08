# 10. Futility-анализ

> **Курс:** Дизайн и анализ экспериментов · **Мини-блок:** Альтернативные дизайны · **Время:** 1.5 ч · **Статус:** ✅ готово

## Обзор
Лекция раскрывает «обратную сторону» ранней остановки эксперимента: как вовремя остановить тест, который почти наверняка не достигнет значимости, и сэкономить трафик. Вводятся conditional power, predictive power (PPoS), stochastic curtailment и β-spending как зеркало α-spending из предыдущей лекции, а также разбирается влияние futility-остановки на ошибки I и II рода.

## Цели занятия
- Понять разницу между остановкой по эффективности и по бесперспективности (futility).
- Научиться считать conditional power и predictive power, переводить порог на CP в futility-границу.
- Понимать β-spending как зеркало α-spending и уметь строить полный двухграничный дизайн.
- Различать binding и non-binding futility-границы и их влияние на ошибку I рода.
- Оценивать через Monte-Carlo «цену» futility: потерю мощности и экономию размера выборки (ASN).

## Материалы
- [Лекция](lecture.ipynb)

## Источники
### Основные источники
1. [Jennison C., Turnbull B. W. Group Sequential Methods with Applications to Clinical Trials](https://doi.org/10.1201/9780367805326)
2. [Pampallona S., Tsiatis A. A. Group sequential designs with provision for early stopping in favor of the null hypothesis](https://zbmath.org/pdf/00696996.pdf)
3. [Lan K. K. G., DeMets D. L. Discrete sequential boundaries for clinical trials](https://zbmath.org/pdf/0543.62059.pdf)
4. [Spiegelhalter D. J., Freedman L. S., Parmar M. K. B. Bayesian approaches to randomized trials](https://academic.oup.com/jrsssa/article/157/3/357/7106848)
5. [Proschan M. A., Lan K. K. G., Wittes J. T. Statistical Monitoring of Clinical Trials: A Unified Approach](https://doi.org/10.1007/978-0-387-44970-8)
6. [Johari R. et al. Peeking at A/B Tests: Why It Matters, and What to Do About It](https://kdd.org/kdd2017/papers/view/peeking-at-ab-tests-why-it-matters-and-what-to-do-about-it)

### Дополнительные материалы
1. [Lan K. K. G., Wittes J. T. The B-value: a tool for monitoring data](https://scholar.google.com/scholar?q=Lan+Wittes+%22The+B-value%22+Biometrics+1988)
2. [Wassmer G., Brannath W. Group Sequential and Confirmatory Adaptive Designs in Clinical Trials](https://doi.org/10.1007/978-3-319-32562-0)
3. [Courthoud M. Understanding Group Sequential Testing](https://towardsdatascience.com/understanding-group-sequential-testing-befb35cec07a/)
4. [Последовательный анализ в AB-тестировании: mSPRT](https://habr.com/ru/articles/991582/)
5. [Одинаковые данные, разные p-value: почему важно правило остановки](https://habr.com/ru/articles/1084294/)
6. [Проблема подглядывания и последовательное А/Б тестирование](https://temofeev.com/info/articles/problema-podglyadyvaniya-i-posledovatelnoe-a-b-testirovanie/)
