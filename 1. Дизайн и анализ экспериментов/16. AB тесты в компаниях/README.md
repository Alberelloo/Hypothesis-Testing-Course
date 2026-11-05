# 3.02. A/B тесты в компаниях

> **Модуль:** Культура тестирования · **Мини-блок:** A/B культура · **Время:** 2 ч · **Статус:** ✅ готово

## Обзор
Занятие показывает, как устроены A/B-платформы глазами аналитика и как компании запускают сотни тестов одновременно. Разбираем компоненты платформы, сплитование от простых правил до хеша с солью и двойного посола, проверку качества хеша, слои и домены, остаточный эффект. Отдельно смотрим на пересечения тестов: ортогональность и аддитивность, мощность таких проверок, реальные данные о взаимодействиях и выбор между изоляцией и пересечением. Заканчиваем надёжностью платформы, культурой и кейсами компаний.

## Цели занятия
- Понимать компоненты A/B-платформы и то, какая поломка на каждом шаге превращается в ложный эффект.
- Проверять сплитование: равномерность, независимость солей, множество A/A.
- Различать ортогональность и аддитивность и уметь проверять обе.
- Понимать мощность теста на взаимодействие и цену проверки всех пар.
- Выбирать между изоляцией, слоями и пересечением.
- Использовать SRM как монитор и понимать его ограничения.

## Материалы
- [Лекция](lecture.ipynb)

## Источники
### Основные источники
1. [System Design A/B платформы](https://www.youtube.com/watch?app=desktop&v=YlIQ9GcRYXk)
2. [Без А/B результат XЗ, или Как построить высоконагруженную платформу А/B-тестов (Ozon)](https://habr.com/ru/companies/ozontech/articles/689052/)
3. [Многослойная система A/B платформ (Tang et al., Google, KDD 2010)](https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/36500.pdf)
4. [О необходимости проверки hash-функций](https://medium.com/@thisisflea/a-good-hash-is-hard-to-find-6edbbf6a78b0)
5. [Controlled experiments on the web: survey and practical guide (Kohavi et al., 2009)](https://ai.stanford.edu/~ronnyk/2009controlledExperimentsOnTheWebSurvey.pdf)
6. [A/B Interactions: A Call to Relax (Microsoft)](https://www.microsoft.com/en-us/research/articles/a-b-interactions-a-call-to-relax/)
7. [Влияние экспериментов друг на друга](https://koch-kir.medium.com/влияние-экспериментов-друг-на-друга-bb7e41674db7)
8. [Пересекающиеся эксперименты: как мы навели порядок в A/B-тестах (hh)](https://habr.com/ru/companies/hh/articles/1084724/)
9. [Embracing overlapping A/B tests and the danger of isolating experiments (Statsig)](https://blog.statsig.com/embracing-overlapping-a-b-tests-and-the-danger-of-isolating-experiments-cb0a69e09d3)
10. [Top Challenges from the first Practical Online Controlled Experiments Summit (Gupta et al., 2019)](https://research.fb.com/wp-content/uploads/2019/06/Top-Challenges-from-the-first-Practical-Online-Controlled-Experiments-Summit.pdf)
11. [Diagnosing Sample Ratio Mismatch in A/B Testing (Microsoft)](https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/)
12. [From Infrastructure to Culture: A/B Testing Challenges in Large Scale Social Networks (Xu et al., LinkedIn, 2015)](https://engineering.linkedin.com/data/publications/resources/2015/from-infrastructure-to-culture-a-b-testing-challenges)
13. [Spotify's New Experimentation Platform (Part 2)](https://engineering.atspotify.com/2020/11/spotifys-new-experimentation-platform-part-2/)
14. [Spotify's New Experimentation Coordination Strategy](https://engineering.atspotify.com/2021/03/10/spotifys-new-experimentation-coordination-strategy/)

### Дополнительные материалы
1. [Detecting interaction effects in online experimentation (Vermeer)](https://www.lukasvermeer.nl/publications/2023/06/26/detecting-interaction-effects-in-online-experimentation.html)
2. [Interaction effect detection (Statsig)](https://statsig.com/blog/interaction-effect-detection)
3. [Автоматизация A/B-тестов (Delivery Club)](https://habr.com/ru/post/557308)
4. [The Evolution of Continuous Experimentation in Software Product Development (Fabijan et al., ICSE 2017)](https://bibtex.github.io/ICSE-2017-FabijanDOB.html)
