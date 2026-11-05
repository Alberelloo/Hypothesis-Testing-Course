# 1.06. Опасность малой мощности. Ошибки S и M типов

> **Модуль:** A/B тестирование · **Мини-блок:** Дополнительные главы A/B тестирования · **Время:** 1.5 ч · **Статус:** ✅ готово

## Обзор
В классическом подходе к планированию эксперимента обычно обсуждают ошибки I и II рода, уровень значимости $\alpha$, мощность теста $1-\beta$ и MDE.
Этого достаточно, чтобы ответить на вопрос: **"с какой вероятностью мы обнаружим эффект заданного размера?"**. Но для практики A/B-тестов этого часто недостаточно. Даже если результат оказался статистически значимым, остаются два важных вопроса:

1. **Не перепутали ли мы направление эффекта?**
   Например, решили, что новая фича улучшает метрику, хотя в реальности она её ухудшает.

2. **Не завышаем ли мы размер эффекта?**
   Например, увидели uplift $+1.2\text{ п.п.}$, а реальный эффект ближе к $+0.3\text{ п.п.}$.

## Цели занятия
- Понять, какие проблемы несут в себе недостаточно мощные тесты.
- Научиться считать ошибки Type S и Type M и проводить Design Analysis до и после теста.
- Понять, почему нельзя считать мощность по наблюдённому эффекту и что происходит, если истинный эффект меньше MDE.
- Научиться контролировать достоверность оценок тестов с малыми мощностями: планированием, сжатием оценок и репликацией.

## Материалы
- [Лекция](lecture.ipynb)

## Источники
### Основные источники
1. [Статья "Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors"](https://sites.stat.columbia.edu/gelman/research/published/retropower_final.pdf)
2. [Обзор статьи на habr](https://habr.com/ru/articles/996474/)

### Дополнительные материалы
1. [Точные формулы: "A note on Type S/M errors in hypothesis testing"](https://doi.org/10.1111/bmsp.12132)
2. [Почему не работает наблюдаемая мощность: "The Abuse of Power"](https://doi.org/10.1198/000313001300339897)
3. [Assessing Type S and Type M Errors (UVA StatLab)](https://library.virginia.edu/data/articles/assessing-type-s-and-type-m-errors)
4. [More on my paper with John Carlin on Type M and Type S errors](https://statmodeling.stat.columbia.edu/2016/11/13/more-on-my-paper-with-john-carlin-on-type-m-and-type-s-errors/)
5. [Statistically significant results from low-power analyses: A comedy of errors](https://doi.org/10.1016/j.gloepi.2026.100250)
6. [Пакет retrodesign для R](https://cran.r-project.org/package=retrodesign)
