"""Иллюстрации к лекции 10 (Futility-анализ), раздел про β-spending-рекурсию.

Генерирует четыре файла:
    l10_init.png       — шаг 1: две стартовые плотности B(t_1) (под H0 и под H1);
    l10_trunc.png      — шаг 2: отсечение правого хвоста (efficacy, H0) и левого (futility, H1);
    l10_conv.png       — шаг 3: свёртка выживших с независимым приращением;
    l10_recursion.gif  — вся рекурсия по взглядам (отсечение + свёртка).

Обозначения границ: efficacy e_k (Z-шкала) -> e_k*sqrt(t_k) на B-шкале,
futility f_k (Z-шкала) -> f_k*sqrt(t_k) на B-шкале.

Все числа на картинках вычисляются той же рекурсией, что и в лекции
(group_sequential_boundaries, non-binding), ничего не захардкожено.

Запуск:  python make_figures.py [OUT_DIR]   (по умолчанию — папка скрипта)
"""
import io
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from scipy.stats import norm

# ---------------------------------------------------------------- дизайн
ALPHA = 0.05                    # односторонняя ошибка I рода
BETA = 0.20                     # ошибка II рода (мощность 80%)
THETA = norm.ppf(1 - ALPHA) + norm.ppf(1 - BETA)   # θ_MDE на B-шкале, ≈2.49
T = np.array([0.30, 0.50, 0.70, 0.85, 1.00])       # доли информации на взглядах
GRID_DX = 0.01
N_SIGMA = 6.0

C_EFF = "#1b9e77"   # efficacy
C_FUT = "#d95f02"   # futility
C_CONT = "#999999"  # продолжение
C_DARK = "#555555"
WHITE = dict(fc="white", ec="none", alpha=0.85, pad=1.5)   # подложка под подписи

plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans"})


# ---------------------------------------------------------------- рекурсия (как в лекции)
def alpha_spending(t, alpha=ALPHA):
    t = np.asarray(t, dtype=float)
    return 2 - 2 * norm.cdf(norm.ppf(1 - alpha / 2) / np.sqrt(t))   # OBF-подобная


def beta_spending(t, beta=BETA):
    t = np.asarray(t, dtype=float)
    return beta * t ** 3                                             # OBF-подобная


def _convolve(p, grid, loc, scale):
    dx = grid[1] - grid[0]
    K = norm.pdf(grid[:, None], loc=grid[None, :] + loc, scale=scale)
    return (K @ p) * dx


def _quantile(p, grid, target, tail):
    dx = grid[1] - grid[0]
    cdf = np.cumsum(p) * dx
    vals = (cdf[-1] - cdf) if tail else cdf
    return grid[int(np.argmin(np.abs(vals - target)))]


def run_recursion(t=T, theta=THETA):
    """Возвращает по каждому взгляду: плотности до отсечения и точки отсечения на B-шкале."""
    K = len(t)
    dt = np.diff(np.concatenate(([0.0], t)))
    grid = np.arange(-N_SIGMA, N_SIGMA + GRID_DX, GRID_DX)
    d_alpha = np.diff(np.concatenate(([0.0], alpha_spending(t))))
    d_beta = np.diff(np.concatenate(([0.0], beta_spending(t))))
    p_eff = norm.pdf(grid, loc=0.0, scale=math.sqrt(dt[0]))
    p_fut = norm.pdf(grid, loc=theta * dt[0], scale=math.sqrt(dt[0]))
    looks = []
    for k in range(K):
        eb = _quantile(p_eff, grid, d_alpha[k], tail=True)    # e_k * sqrt(t_k)
        fb = _quantile(p_fut, grid, d_beta[k], tail=False)    # f_k * sqrt(t_k)
        looks.append(dict(k=k + 1, t=t[k], p_eff=p_eff.copy(), p_fut=p_fut.copy(),
                          eb=eb, fb=fb, e=eb / math.sqrt(t[k]), f=fb / math.sqrt(t[k]),
                          d_alpha=d_alpha[k], d_beta=d_beta[k]))
        if k < K - 1:
            d = dt[k + 1]
            p_eff = _convolve(p_eff * (grid <= eb), grid, 0.0, math.sqrt(d))           # non-binding
            p_fut = _convolve(p_fut * ((grid > fb) & (grid <= eb)), grid, theta * d, math.sqrt(d))
    return grid, looks


def mass(p, grid, mask=None):
    return float(np.sum(p if mask is None else p * mask) * (grid[1] - grid[0]))


# ---------------------------------------------------------------- рисунки
def fig_init(grid, looks, out):
    L = looks[0]
    t1 = L["t"]
    x = np.linspace(-2.4, 3.8, 800)
    pe = norm.pdf(x, 0, math.sqrt(t1))
    pf = norm.pdf(x, THETA * t1, math.sqrt(t1))
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=120)
    ax.plot(x, pe, color=C_EFF, lw=2.5,
            label=r"$p_1^{eff}(x)=\varphi(x;\,0,\,t_1)$  под $H_0$ (efficacy)")
    ax.fill_between(x, pe, color=C_EFF, alpha=0.12)
    ax.plot(x, pf, color=C_FUT, lw=2.5,
            label=r"$p_1^{fut}(x)=\varphi(x;\,\theta t_1,\,t_1)$  под $H_1$ (futility)")
    ax.fill_between(x, pf, color=C_FUT, alpha=0.12)
    ax.axvline(0, color=C_EFF, ls=":", lw=1.3)
    ax.axvline(THETA * t1, color=C_FUT, ls=":", lw=1.3)
    ax.text(0.02, 0.97,
            "ещё ни одна траектория\nне отброшена — это\nбезусловное распределение $B(t_1)$\n"
            + rf"($t_1={t1:.2f}$, $\theta t_1={THETA * t1:.2f}$)",
            transform=ax.transAxes, ha="left", va="top", fontsize=10, color="#444444")
    ax.set_title(r"Инициализация: до первого взгляда вся масса на месте, $\int p_1=1$")
    ax.set_xlabel(r"$B(t_1)$ — положение процесса в момент первого взгляда")
    ax.set_ylabel("плотность")
    ax.set_ylim(0, pe.max() * 1.12)
    ax.legend(loc="upper right", fontsize=10)
    fig.tight_layout()
    fig.savefig(out / "l10_init.png")
    plt.close(fig)


def fig_trunc(grid, looks, out):
    L = looks[0]
    t1 = L["t"]
    x = np.linspace(-2.4, 3.8, 1200)
    pe = norm.pdf(x, 0, math.sqrt(t1))
    pf = norm.pdf(x, THETA * t1, math.sqrt(t1))
    eb, fb = L["eb"], L["fb"]
    # массы хвостов = приращения бюджетов (по ним и подбирается точка отсечения)
    m_eff, m_fut = L["d_alpha"], L["d_beta"]

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.6), dpi=120)
    ymax = pe.max() * 1.15

    a1.plot(x, pe, color=C_EFF, lw=2.5)
    a1.fill_between(x, pe, where=x >= eb, color=C_EFF, alpha=0.6)
    a1.axvline(eb, color=C_EFF, ls="--", lw=1.8)
    a1.text(eb + 0.08, 0.62 * ymax, rf"$e_1\sqrt{{t_1}}={eb:.2f}$", color=C_EFF, fontsize=12,
            ha="left", va="bottom")
    a1.annotate("правый хвост\n" + rf"масса $=\Delta\alpha_1={m_eff:.4f}$",
                xy=(eb + 0.25, norm.pdf(eb + 0.25, 0, math.sqrt(t1)) + 0.005),
                xytext=(eb + 0.05, 0.38 * ymax), color=C_EFF, fontsize=10.5, ha="left",
                arrowprops=dict(arrowstyle="->", color=C_EFF, lw=1.2))
    a1.set_title(r"Efficacy: отсекаем ПРАВЫЙ хвост (под $H_0$)")
    a1.set_ylabel(r"плотность $p_1^{eff}$")

    a2.plot(x, pf, color=C_FUT, lw=2.5)
    a2.fill_between(x, pf, where=x <= fb, color=C_FUT, alpha=0.6)
    a2.axvline(fb, color=C_FUT, ls="--", lw=1.8)
    a2.text(fb - 0.08, 0.62 * ymax, rf"$f_1\sqrt{{t_1}}={fb:.2f}$", color=C_FUT, fontsize=12,
            ha="right", va="bottom")
    a2.annotate("левый хвост,\nмасса\n" + rf"$=\Delta\beta_1={m_fut:.4f}$",
                xy=(fb - 0.12, norm.pdf(fb - 0.12, THETA * t1, math.sqrt(t1)) * 0.5),
                xytext=(x[0] + 0.12, 0.38 * ymax), color=C_FUT, fontsize=10.5, ha="left",
                arrowprops=dict(arrowstyle="->", color=C_FUT, lw=1.2))
    a2.set_title(r"Futility: отсекаем ЛЕВЫЙ хвост (под $H_1$)")
    a2.set_ylabel(r"плотность $p_1^{fut}$")

    for ax in (a1, a2):
        ax.set_xlabel(r"$B(t_1)$")
        ax.set_ylim(0, ymax)
        ax.set_xlim(x[0], x[-1])
    fig.suptitle("Шаг 2 — отсечение: направление хвоста задаёт тип контролируемой ошибки",
                 fontsize=13)
    fig.tight_layout()
    fig.savefig(out / "l10_trunc.png")
    plt.close(fig)


def fig_conv(grid, looks, out):
    """Шаг 3 на примере перехода от взгляда 1 к взгляду 2 (под H1)."""
    L0, L1 = looks[0], looks[1]
    d = L1["t"] - L0["t"]
    eb, fb = L0["eb"], L0["fb"]
    p = L0["p_fut"]
    keep = (grid > fb) & (grid <= eb)
    xlim = (-3, 5)
    sel = (grid >= xlim[0]) & (grid <= xlim[1])

    fig, (a1, a2) = plt.subplots(2, 1, figsize=(10, 7.2), dpi=120, sharex=True)

    # верх: p_k и область продолжения
    a1.plot(grid[sel], p[sel], color=C_DARK, lw=1.8, label=r"$p_k(x)$ — дожившие к взгляду $k$")
    a1.fill_between(grid, p, where=grid <= fb, color=C_FUT, alpha=0.5)
    a1.fill_between(grid, p, where=grid > eb, color=C_EFF, alpha=0.5)
    a1.axvline(fb, color=C_FUT, ls="--", lw=1.3)
    a1.axvline(eb, color=C_EFF, ls="--", lw=1.3)
    ytop = p.max() * 1.25
    a1.text(fb - 0.06, 0.80 * ytop, r"$f_k\sqrt{t_k}$", color=C_FUT, fontsize=13, ha="right")
    a1.text(eb + 0.06, 0.80 * ytop, r"$e_k\sqrt{t_k}$", color=C_EFF, fontsize=13, ha="left")
    shift = THETA * d
    for x0 in (fb + 0.3, 0.5 * (fb + eb), eb - 0.3):
        y0 = np.interp(x0, grid, p) * 0.45
        a1.annotate("", xy=(x0 + shift, y0), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="->", color=C_DARK, lw=1.4))
        a1.plot([x0], [y0], "o", color=C_DARK, ms=4)
    a1.text(0.5 * (fb + eb) + shift / 2, np.interp(0.5 * (fb + eb), grid, p) * 0.45 + 0.03,
            r"$+\theta\Delta$", ha="center", va="bottom", fontsize=11, color=C_DARK)
    a1.set_ylim(0, ytop)
    a1.set_ylabel("плотность")
    a1.set_title(r"Шаг 3а: каждая выжившая точка $x$ порождает гауссиану "
                 r"$N(x+\theta\Delta,\ \Delta)$")
    a1.legend(loc="upper right", fontsize=9.5)

    # низ: «капли» от отдельных кусков области продолжения и их сумма
    edges = np.linspace(fb, eb, 9)
    cmap = plt.get_cmap("viridis")
    total = np.zeros_like(grid)
    for j in range(len(edges) - 1):
        piece = keep & (grid > edges[j]) & (grid <= edges[j + 1])
        drop = _convolve(p * piece, grid, shift, math.sqrt(d))
        total += drop
        a1.fill_between(grid, p, where=piece, color=cmap(j / 8), alpha=0.25, lw=0)
        a2.plot(grid[sel], drop[sel], color=cmap(j / 8), lw=1.0, alpha=0.9)
    p_next = L1["p_fut"]
    a2.plot(grid[sel], p_next[sel], color=C_DARK, lw=2.5,
            label=r"$p_{k+1}(y)$ — свёртка (сумма всех «капель»)")
    a2.fill_between(grid[sel], p_next[sel], color=C_CONT, alpha=0.3)
    a2.plot([], [], color=cmap(0.5), lw=1.0, label="«капли» от кусков области продолжения")
    a2.axvline(THETA * L1["t"], color="black", ls=":", lw=1.3)
    a2.text(THETA * L1["t"] + 0.06, 1.12 * p_next.max(), rf"$\theta t_{{k+1}}={THETA * L1['t']:.2f}$",
            fontsize=10)
    a2.set_ylim(0, p_next.max() * 1.3)
    a2.set_ylabel("плотность")
    a2.set_xlabel(r"$B(t_{k+1})$")
    a2.set_title("Шаг 3б: результат — сдвинутая вправо и размазанная плотность выживших;\n"
                 + rf"масса упала с 1.00 до {mass(p_next, grid):.2f}"
                 + rf" (пример: $t_k={L0['t']:.2f}$, $t_{{k+1}}={L1['t']:.2f}$, $\Delta={d:.2f}$)",
                 fontsize=11)
    a2.legend(loc="upper left", fontsize=9.5)
    a2.set_xlim(*xlim)
    assert np.allclose(total, p_next, atol=1e-6)   # капли действительно складываются в p_{k+1}
    fig.suptitle("Свёртка = «добавить независимое приращение» к каждой выжившей траектории",
                 fontsize=13)
    fig.tight_layout()
    fig.savefig(out / "l10_conv.png")
    plt.close(fig)


def fig_recursion_gif(grid, looks, out):
    xlim = (-3.2, 4.6)
    sel = (grid >= xlim[0]) & (grid <= xlim[1])
    ymax = looks[0]["p_fut"].max() * 1.15
    cum_a = np.cumsum([L["d_alpha"] for L in looks])
    cum_b = np.cumsum([L["d_beta"] for L in looks])
    K = len(looks)
    frames = []

    def base(title, spent):
        fig, ax = plt.subplots(figsize=(10, 5.6), dpi=108)
        ax.set_xlim(*xlim)
        ax.set_ylim(0, ymax)
        ax.set_title(title, fontsize=14)
        ax.set_xlabel(r"$B(t)$ — положение процесса")
        ax.set_ylabel("плотность выживших (под $H_1$)")
        ax.text(0.985, 0.965, spent, transform=ax.transAxes, ha="right", va="top", fontsize=10.5,
                bbox=dict(boxstyle="round", fc="white", ec="#bbbbbb"))
        return fig, ax

    def grab(fig):
        fig.tight_layout()
        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        plt.close(fig)
        buf.seek(0)
        return Image.open(buf).convert("RGB")

    def theta_line(ax, t):
        ax.axvline(THETA * t, color="black", ls=":", lw=1)
        ax.text(THETA * t + 0.05, 0.012 * ymax, rf"$\theta t={THETA * t:.2f}$", fontsize=10)

    for i, L in enumerate(looks):
        k, t, p, eb, fb = L["k"], L["t"], L["p_fut"], L["eb"], L["fb"]
        m_fut = mass(p, grid, grid <= fb)
        m_eff = mass(p, grid, grid > eb)
        m_cont = mass(p, grid, (grid > fb) & (grid <= eb))
        fig, ax = base(rf"Взгляд {k}  ($t={t:.2f}$): отсекаем хвосты от плотности выживших",
                       rf"потрачено: $\alpha$={cum_a[i]:.3f}, $\beta$={cum_b[i]:.3f}")
        ax.plot(grid[sel], p[sel], color="#888888", lw=2.5)
        ax.fill_between(grid, p, where=(grid > fb) & (grid <= eb), color=C_CONT, alpha=0.25)
        ax.fill_between(grid, p, where=grid <= fb, color=C_FUT, alpha=0.6)
        ax.fill_between(grid, p, where=grid > eb, color=C_EFF, alpha=0.55)
        ax.axvline(fb, color=C_FUT, ls="--", lw=1.8)
        ax.axvline(eb, color=C_EFF, ls="--", lw=1.8)
        ax.text(fb - 0.07, 0.80 * ymax, f"futility\n{100 * m_fut:.1f}%", color=C_FUT,
                ha="right", va="top", fontsize=12, bbox=WHITE)
        ax.text(eb + 0.07, 0.80 * ymax, f"efficacy\n{100 * m_eff:.1f}%", color=C_EFF,
                ha="left", va="top", fontsize=12, bbox=WHITE)
        ax.text(fb - 0.07, 0.62 * ymax, rf"$f_{k}\sqrt{{t_{k}}}={fb:.2f}$", color=C_FUT,
                ha="right", va="top", fontsize=11, bbox=WHITE)
        ax.text(eb + 0.07, 0.62 * ymax, rf"$e_{k}\sqrt{{t_{k}}}={eb:.2f}$", color=C_EFF,
                ha="left", va="top", fontsize=11, bbox=WHITE)
        cont_label = "продолжаем" if k < K else "между границами"
        ax.text(xlim[0] + 0.15, 0.45 * ymax,
                f"{cont_label}\n{100 * m_cont:.1f}%\n(было {100 * mass(p, grid):.1f}%)",
                color="#333333", ha="left", va="top", fontsize=12)
        theta_line(ax, t)
        frames.append(grab(fig))

        if i < K - 1:
            N = looks[i + 1]
            pn = N["p_fut"]
            fig, ax = base(rf"Свёртка: выжившие из взгляда {k} переместились к взгляду {k + 1}  "
                           rf"($t={N['t']:.2f}$)",
                           rf"потрачено: $\alpha$={cum_a[i]:.3f}, $\beta$={cum_b[i]:.3f}")
            ax.plot(grid[sel], pn[sel], color="#888888", lw=2.5)
            ax.fill_between(grid, pn, color=C_CONT, alpha=0.3)
            ax.axvline(N["fb"], color=C_FUT, ls=":", lw=1.3)
            ax.axvline(N["eb"], color=C_EFF, ls=":", lw=1.3)
            ax.text(xlim[0] + 0.15, 0.80 * ymax,
                    f"новая плотность к взгляду {k + 1}\n(после свёртки),\n"
                    f"масса {100 * mass(pn, grid):.1f}%",
                    color="#333333", ha="left", va="top", fontsize=12)
            ax.text(xlim[0] + 0.15, 0.50 * ymax,
                    "пунктир — границы\nследующего взгляда", color="#666666",
                    ha="left", va="top", fontsize=10)
            theta_line(ax, N["t"])
            frames.append(grab(fig))

    frames[0].save(out / "l10_recursion.gif", save_all=True, append_images=frames[1:],
                   duration=1500, loop=0, optimize=True)
    return frames


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    out.mkdir(parents=True, exist_ok=True)
    grid, looks = run_recursion()
    fig_init(grid, looks, out)
    fig_trunc(grid, looks, out)
    fig_conv(grid, looks, out)
    fig_recursion_gif(grid, looks, out)

    # сводка для сверки с текстом лекции
    print(f"theta={THETA:.4f}, t={T.tolist()}")
    fut_total = eff_total = 0.0
    for L in looks:
        p = L["p_fut"]
        mf = mass(p, grid, grid <= L["fb"]); me = mass(p, grid, grid > L["eb"])
        fut_total += mf; eff_total += me
        print(f"look {L['k']}: t={L['t']:.2f} mass={mass(p, grid):.3f} "
              f"e={L['e']:.3f} f={L['f']:.3f} eb={L['eb']:.3f} fb={L['fb']:.3f} "
              f"dA={L['d_alpha']:.4f} dB={L['d_beta']:.4f} fut={mf:.3f} eff={me:.3f}")
    print(f"sum futility={fut_total:.3f}, power={eff_total:.3f}")


if __name__ == "__main__":
    main()
