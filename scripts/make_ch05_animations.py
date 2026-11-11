"""Chapter 5 animations and deck stills, authored ONCE here (same pipeline as chapters 2 to 4).

Each registered function builds one figure (and, for animations, a FuncAnimation) and is
self-contained: it uses only numpy, matplotlib.pyplot, FuncAnimation and the colour
constants below (plus local matplotlib imports). Running this script bakes the GIFs /
PNG stills for the slide decks into ch05/images/. `scripts/sync_ch05_cells.py` copies the SAME
function bodies into the `{code-cell}` blocks of the lecture pages (marker line
`# synced: <name>`), where animations play in the matplotlib JS player.

Run from the repo root:
    .venv/bin/python scripts/make_ch05_animations.py                 # bake everything
    .venv/bin/python scripts/make_ch05_animations.py three_wells     # a subset
    .venv/bin/python scripts/sync_ch05_cells.py                      # refresh page cells

Page weight: the JS player embeds every frame as a PNG, so keep animations to 24-48 frames.
Sync strips every line starting with `return`, so inner helpers must not use it (write a
lambda, or fill an array in place) and `update` must not return artists (use blit=False).

Lecture 5.1 (page ch05/01, deck slides/ch05/01) uses the figures in the "lecture 5.1" section; Lecture 5.2
(page ch05/02, deck slides/ch05/02) those in "lecture 5.2".
Units in every figure: lengths in the Bohr radius a0, energies in the hartree E_h (Z = 1).
Colours of the angular momentum, kept the same in every figure: s TEAL, p PURPLE, d ORANGE,
f GRAY; nodes CARDINAL. The Coulomb well is ORANGE (electrons, as in 4.1's model_map).
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = "ch05/images"
GIF_DPI = 200    # 2x: an 8 in figure bakes 1600 px wide, crisp full screen
TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"

REGISTRY = {}


def register(fn):
    REGISTRY[fn.__name__] = fn
    return fn


# ============================================================ lecture 5.1: hydrogenlike atoms

# ------------------------------------------------------------ the three model wells and their ladders: box, spring, Coulomb (still)
@register
def three_wells():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx, cx) = plt.subplots(1, 3, figsize=(9.6, 3.9), gridspec_kw={"wspace": 0.3})
    # box: V = 0 between walls at 0 and L, levels n^2 in units of E_1
    ax.plot([0, 0], [0, 18], color="k", lw=2.4); ax.plot([1, 1], [0, 18], color="k", lw=2.4)
    ax.plot([0, 1], [0, 0], color="k", lw=2.4)
    for n in range(1, 5):
        ax.hlines(n * n, 0, 1, color=GRAY, lw=2.4)
        ax.text(1.05, n * n, rf"$n = {n}$", va="center", fontsize=11, color=GRAY)
    ax.set_xlim(-0.25, 1.55); ax.set_ylim(-0.6, 18.5)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "$L$"]); ax.set_yticks([0, 1, 4, 9, 16])
    ax.set_ylabel(r"energy (units of $E_1$)", fontsize=11)
    ax.set_title("box", fontsize=13.5, color=GRAY, weight="bold")
    # spring: V = x^2/2, levels v + 1/2 in units of hbar omega, drawn between the turning points
    x = np.linspace(-3.4, 3.4, 300)
    bx.plot(x, 0.5 * x**2, color="k", lw=2.4)
    for v in range(5):
        E = v + 0.5
        xt = np.sqrt(2 * E)
        bx.hlines(E, -xt, xt, color=TEAL, lw=2.4)
        bx.text(3.45, E, rf"$v = {v}$", va="center", fontsize=11, color=TEAL)
    bx.set_xlim(-3.6, 4.8); bx.set_ylim(-0.2, 5.6)
    bx.set_xticks([0]); bx.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5]); bx.set_yticklabels(["1/2", "3/2", "5/2", "7/2", "9/2"])
    bx.set_ylabel(r"energy (units of $\hbar\omega$)", fontsize=11)
    bx.set_title("spring", fontsize=13.5, color=TEAL, weight="bold")
    # Coulomb: V = -1/r, levels -1/2n^2 in hartree, drawn out to the turning point r = 2n^2; a continuum above zero
    r = np.linspace(0.45, 36, 400)
    cx.axhspan(0, 0.16, color="#dee2e6", lw=0, zorder=0)
    cx.axhline(0, color=GRAY, lw=0.8, ls=":")
    cx.plot(r, -1 / r, color="k", lw=2.4)
    for n in range(1, 5):
        E = -0.5 / n**2
        cx.hlines(E, 0, min(2 * n * n, 36), color=ORANGE, lw=2.4)
        cx.text(36.8, E + {3: -0.012, 4: 0.016}.get(n, 0), rf"$n = {n}$", va="center", fontsize=11, color=ORANGE)
    cx.set_xlim(-0.5, 48); cx.set_ylim(-0.62, 0.16)
    cx.set_xticks([0, 10, 20, 30]); cx.set_yticks([-0.5, -0.125, 0]); cx.set_yticklabels(["-1/2", "-1/8", "0"])
    cx.set_xlabel(r"$r$ (units of $a_0$)", fontsize=11)
    cx.set_ylabel(r"energy (units of $E_h$)", fontsize=11)
    cx.set_title("Coulomb", fontsize=13.5, color=ORANGE, weight="bold")
    for a_ in (ax, bx, cx):
        a_.tick_params(labelsize=10)
    fig.subplots_adjust(left=0.07, right=0.98, top=0.9, bottom=0.14)
    fig.savefig(f"{OUT}/three_wells.png", dpi=200)
    print("wrote", f"{OUT}/three_wells.png")
    return fig, None


# ------------------------------------------------------------ the plan: one equation, split by the central force into angles (done) and radius (new) (still)
@register
def hatom_roadmap():
    from matplotlib.patches import FancyBboxPatch
    W, Ht = 10.1, 4.1
    fig = plt.figure(figsize=(W, Ht))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, Ht); ax.axis("off")
    tint = {GRAY: "#f1f3f5", PURPLE: "#f1ecf7", TEAL: "#e3f1f5", ORANGE: "#fdf0e0", "k": "#f8f9fa"}

    def box(x, y, w, h, lines, col, sizes=(13, 11.5)):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                    fc=tint[col], ec=col, lw=1.6, zorder=2))
        n = len(lines)
        for k, line in enumerate(lines):
            dy = (n - 1) / 2 - k
            ax.text(x, y + 0.3 * dy, line, ha="center", va="center", fontsize=sizes[0] if k == 0 else sizes[1],
                    color=col if k == 0 else "k", weight="bold" if k == 0 else None, zorder=3)

    arrow = lambda p, q, col=GRAY: ax.annotate("", xy=q, xytext=p, zorder=1, arrowprops=dict(
        arrowstyle="-|>", color=col, lw=1.5, mutation_scale=15, shrinkA=2, shrinkB=2))
    x1, x2, x3, x4 = 1.25, 3.75, 6.35, 8.85
    yt, yb, ym = 3.15, 1.15, 2.15
    box(x1, ym, 2.1, 1.25, [r"$\hat{H}\psi = E\psi$", r"$r, \theta, \phi$", "three coordinates"], "k")
    box(x2, ym, 2.25, 1.25, [r"$V(r)$ only", r"$[\hat{H}, \hat{L}^2] = 0$", r"$[\hat{H}, \hat{L}_z] = 0$"], "k")
    box(x3, yt, 2.45, 1.1, ["angles: solved", r"$Y_l^m(\theta, \phi)$, Lecture 4.4", r"$l = 0, 1, 2, \dots \quad m = -l, \dots, l$"],
        PURPLE)
    box(x3, yb, 2.45, 1.1, ["radius: new", r"$R_{nl}(r)$, this lecture", r"$n = l + 1, l + 2, \dots$"], ORANGE)
    box(x4, ym, 2.25, 1.25, ["the atom", r"$\psi_{nlm} = R_{nl}(r)\,Y_l^m(\theta, \phi)$", r"$E_n = -\dfrac{Z^2 E_h}{2n^2}$"], TEAL,
        sizes=(13, 12))
    arrow((x1 + 1.05, ym), (x2 - 1.13, ym))
    arrow((x2 + 1.13, ym + 0.25), (x3 - 1.23, yt - 0.1), PURPLE)
    arrow((x2 + 1.13, ym - 0.25), (x3 - 1.23, yb + 0.1), ORANGE)
    arrow((x3 + 1.23, yt - 0.1), (x4 - 1.13, ym + 0.25), PURPLE)
    arrow((x3 + 1.23, yb + 0.1), (x4 - 1.13, ym - 0.25), ORANGE)
    fig.savefig(f"{OUT}/hatom_roadmap.png", dpi=200)
    print("wrote", f"{OUT}/hatom_roadmap.png")
    return fig, None


# ------------------------------------------------------------ the effective radial potential: Coulomb attraction plus the centrifugal term (still)
@register
def effective_potential():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    r = np.linspace(0.12, 16, 800)
    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    ax.axhline(0, color=GRAY, lw=0.8, ls=":")
    for n, dy in ((1, 0), (2, -0.012), (3, 0.018)):
        E = -0.5 / n**2
        ax.axhline(E, color=GRAY, lw=0.9, ls=(0, (3, 3)))
        ax.text(16.1, E + dy, rf"$E_{n}$", fontsize=11.5, color=GRAY, va="center")
    labels = {0: (1.15, -0.72), 1: (2.0, -0.36), 2: (4.4, -0.0)}  # beside each curve, clear of the others
    for l, col in ((0, TEAL), (1, PURPLE), (2, ORANGE)):
        V = -1 / r + l * (l + 1) / (2 * r**2)
        ax.plot(r, V, color=col, lw=2.6)
        ax.text(*labels[l], rf"$l = {l}$", fontsize=13, color=col, ha="left", va="center")
    ax.set_xlim(0, 17.5); ax.set_ylim(-1.05, 0.42)
    ax.set_xticks([0, 2, 4, 6, 8, 10, 12, 14, 16])
    ax.set_yticks([-1, -0.5, 0]); ax.tick_params(labelsize=10.5)
    ax.set_xlabel(r"$r$ (units of $a_0$)", fontsize=12)
    ax.set_ylabel(r"$V_{\mathrm{eff}}(r)$ (units of $E_h$)", fontsize=12)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.97, bottom=0.14)
    fig.savefig(f"{OUT}/effective_potential.png", dpi=200)
    print("wrote", f"{OUT}/effective_potential.png")
    return fig, None


# ------------------------------------------------------------ why the atom does not collapse: exponential trial states of three sizes, and E of every size (still)
@register
def coulomb_tradeoff():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    rs = np.linspace(0, 10, 500)
    trials = [("a", 1 / 3, "squeezed", GRAY), ("b", 1.0, "the ground state", CARDINAL), ("c", 3.0, "spread out", GRAY)]
    fig = plt.figure(figsize=(9.6, 5.6))
    for j, (tag, a, name, col) in enumerate(trials):
        ax = fig.add_axes([0.07 + 0.31 * j, 0.6, 0.27, 0.33])
        P = 4 * rs**2 * np.exp(-2 * rs / a) / a**3                  # radial density of psi = e^{-r/a}, normalized
        ax.fill_between(rs, 0, P, color=TEAL, alpha=0.3, lw=0)
        ax.plot(rs, P, color=TEAL, lw=2)
        h = 0.5 * P.max()
        ax.annotate("", xy=(a, h), xytext=(0, h), arrowprops=dict(arrowstyle="<->", color="k", lw=1.2, shrinkA=0, shrinkB=0))
        ax.text(a / 2, h * 1.08, "$a$", ha="center", va="bottom", fontsize=12)
        ax.set_xlim(0, 10); ax.set_ylim(0, 1.3 * P.max()); ax.set_yticks([]); ax.set_xticks([0, 5, 10])
        ax.spines["left"].set_visible(False); ax.tick_params(labelsize=10)
        ax.set_title(f"({tag}) {name}: " + rf"$a = {a:.2g}\,a_0$", fontsize=12, color=col)
        K, V = 1 / (2 * a**2), -1 / a
        ax.text(0.3, -0.38 * P.max(), f"kinetic {K:.2f}", color=ORANGE, fontsize=11.5, va="top")
        ax.text(5.1, -0.38 * P.max(), f"potential {V:.2f}", color=TEAL, fontsize=11.5, va="top")
    ax = fig.add_axes([0.08, 0.1, 0.9, 0.38])
    s = np.linspace(0.25, 4.5, 400)
    ax.plot(s, 1 / (2 * s**2), color=ORANGE, lw=2.4, label=r"kinetic $\hbar^2/2\mu a^2$")
    ax.plot(s, -1 / s, color=TEAL, lw=2.4, label=r"potential $-e^2/4\pi\varepsilon_0 a$")
    ax.plot(s, 1 / (2 * s**2) - 1 / s, color="k", lw=2.8, label=r"total $\langle E\rangle$")
    ax.axhline(0, color=GRAY, lw=0.8, ls=":")
    for tag, a, name, col in trials:
        E = 1 / (2 * a**2) - 1 / a
        ax.plot([a], [E], "o", color=col, ms=9, zorder=5)
        dx, dy = (0.12, -0.3) if tag == "a" else (0.07, 0.12)
        ax.text(a + dx, E + dy, f"({tag})", fontsize=12, color=col)
    ax.annotate(r"lowest: $-\frac{1}{2}E_h = -13.6$ eV at $a = a_0$", xy=(1, -0.5), xytext=(1.9, -0.95), fontsize=12,
                color=CARDINAL, arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.2, mutation_scale=12, shrinkB=6))
    ax.set_xlim(0.25, 4.5); ax.set_ylim(-1.25, 1.6)
    ax.set_yticks([-1, -0.5, 0, 0.5, 1, 1.5]); ax.set_yticklabels(["-1", r"$-\frac{1}{2}$", "0", r"$\frac{1}{2}$", "1", r"$\frac{3}{2}$"])
    ax.set_xlabel(r"size $a$ of the state $e^{-r/a}$ (units of $a_0$)", fontsize=11.5)
    ax.set_ylabel(r"average energy ($E_h$)", fontsize=11.5)
    ax.legend(loc="upper right", frameon=False, fontsize=11)
    fig.savefig(f"{OUT}/coulomb_tradeoff.png", dpi=200)
    print("wrote", f"{OUT}/coulomb_tradeoff.png")
    return fig, None


# ------------------------------------------------------------ the energy of every size alone: the lower panel of coulomb_tradeoff (still, deck-only)
@register
def coulomb_energy():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    s = np.linspace(0.25, 4.5, 400)
    ax.plot(s, 1 / (2 * s**2), color=ORANGE, lw=2.4, label=r"kinetic $\hbar^2/2\mu a^2$")
    ax.plot(s, -1 / s, color=TEAL, lw=2.4, label=r"potential $-e^2/4\pi\varepsilon_0 a$")
    ax.plot(s, 1 / (2 * s**2) - 1 / s, color="k", lw=2.8, label=r"total $\langle E\rangle$")
    ax.axhline(0, color=GRAY, lw=0.8, ls=":")
    for a, name, col, dx, dy in ((1 / 3, "squeezed", GRAY, 0.12, -0.3), (1.0, "the ground state", CARDINAL, 0.1, 0.14),
                                 (3.0, "spread out", GRAY, 0.08, 0.14)):
        E = 1 / (2 * a**2) - 1 / a
        ax.plot([a], [E], "o", color=col, ms=9, zorder=5)
        ax.text(a + dx, E + dy, name, fontsize=12, color=col)
    ax.annotate(r"lowest: $-\frac{1}{2}E_h = -13.6$ eV at $a = a_0$", xy=(1, -0.5), xytext=(1.9, -0.95), fontsize=12.5,
                color=CARDINAL, arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.2, mutation_scale=12, shrinkB=6))
    ax.set_xlim(0.25, 4.5); ax.set_ylim(-1.25, 1.6)
    ax.set_yticks([-1, -0.5, 0, 0.5, 1, 1.5]); ax.set_yticklabels(["-1", r"$-\frac{1}{2}$", "0", r"$\frac{1}{2}$", "1", r"$\frac{3}{2}$"])
    ax.set_xlabel(r"size $a$ of the state $e^{-r/a}$ (units of $a_0$)", fontsize=12)
    ax.set_ylabel(r"average energy ($E_h$)", fontsize=12)
    ax.tick_params(labelsize=11)
    ax.legend(loc="upper right", frameon=False, fontsize=12)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.97, bottom=0.14)
    fig.savefig(f"{OUT}/coulomb_energy.png", dpi=200)
    print("wrote", f"{OUT}/coulomb_energy.png")
    return fig, None


# ------------------------------------------------------------ shooting: only at E = -1/2n^2 does the radial tail die (animation, unused since 2026-11-09)
@register
def hydrogen_shooting():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    dr = 0.01
    r = np.arange(dr, 40 + dr / 2, dr); V = -1 / r                   # l = 0, atomic units
    u = np.zeros_like(r)

    def integrate(E, jend):                                          # raw Numerov, outward from u(0) = 0 up to index jend
        f = 1.0 + dr * dr * 2.0 * (E - V) / 12.0
        u[0], u[1] = r[0] * (1 - r[0]), r[1] * (1 - r[1])            # u = r(1 - r + ...) near the nucleus, l = 0
        for j in range(1, jend):
            u[j + 1] = ((12.0 - 10.0 * f[j]) * u[j] - f[j - 1] * u[j - 1]) / f[j + 1]

    def numerov(E):                                                  # the drawn curve: normalized, dead tail dropped
        integrate(E, len(r) - 1)
        rt = max(1.0, -1 / E)                                        # outer turning point, -1/r = E
        m = np.abs(u[r <= rt]).max()
        u[:] = u / m
        k = np.argmax(r > rt)                                        # beyond the turning point, once |u| < 1e-4: dead
        dead = np.where(np.abs(u[k:]) < 1e-4)[0]
        if len(dead):
            u[k + dead[0]:] = 0.0

    def tail(E):                                                     # sign of u where round-off has not yet grown
        jend = min(len(r) - 1, int(round((4 * max(1.0, -1 / E) + 6) / dr)))
        integrate(E, jend)
        return np.sign(u[jend])

    levels = []
    for n in (1, 2, 3):                                              # the grid's own eigenvalues, by bisection on the tail
        a, b = -0.5 / n**2 - 0.01, -0.5 / n**2 + 0.01
        sa = tail(a)
        for _ in range(60):
            c = 0.5 * (a + b)
            if tail(c) == sa:
                a = c
            else:
                b = c
        levels.append(0.5 * (a + b))
    E1, E2, E3 = levels
    Es = np.concatenate([np.linspace(-0.64, E1, 6)[:-1], [E1, E1, E1], np.linspace(E1, E2, 12)[1:-1], [E2, E2, E2],
                         np.linspace(E2, E3, 10)[1:-1], [E3, E3, E3], np.linspace(E3, -0.03, 5)[1:]])
    fig, (ax, axe) = plt.subplots(1, 2, figsize=(8, 3.8), gridspec_kw={"width_ratios": [6, 1.1], "wspace": 0.12})
    ax.axhline(0, color=GRAY, lw=0.8)
    (wave,) = ax.plot([], [], lw=2.6)
    turn = ax.axvline(2, color=GRAY, lw=1, ls=":")
    ax.set_xlim(0, 40); ax.set_ylim(-1.6, 1.6); ax.set_yticks([-1, 0, 1])
    ax.set_xlabel(r"$r$ (units of $a_0$)", fontsize=11.5); ax.set_ylabel(r"$u(r) = r\,R(r)$", fontsize=11.5)
    readout = ax.text(0.98, 0.95, "", transform=ax.transAxes, ha="right", va="top", fontsize=12.5)
    axe.set_xlim(0, 1); axe.set_ylim(-0.66, 0.03); axe.set_xticks([])
    axe.spines["bottom"].set_visible(False)
    axe.set_yticks(levels); axe.set_yticklabels([r"$-\frac{1}{2}$", r"$-\frac{1}{8}$", r"$-\frac{1}{18}$"], fontsize=11)
    axe.set_ylabel(r"$E$ (units of $E_h$)", fontsize=11.5)
    axe.axhline(0, color=GRAY, lw=0.8, ls=":")
    for n, E0 in zip((1, 2, 3), levels):
        axe.text(1.05, E0, rf"$n = {n}$", fontsize=10.5, va="center", color=GRAY)
    (marker,) = axe.plot([], [], ">", color=GRAY, ms=9)
    found = [axe.plot([0.3, 0.95], [E0, E0], color=TEAL, lw=3, visible=False)[0] for E0 in levels]
    fig.subplots_adjust(left=0.085, right=0.9, top=0.95, bottom=0.15)

    def update(i):
        E = Es[i]
        numerov(E)
        hit = min(abs(E - E0) for E0 in levels) < 1e-9
        wave.set_data(r, np.clip(u, -9, 9))
        wave.set_color(TEAL if hit else CARDINAL)
        turn.set_xdata([-1 / E, -1 / E])
        marker.set_data([0.12], [E])
        for ln, E0 in zip(found, levels):
            ln.set_visible(E >= E0 - 1e-9)
        readout.set_text(rf"$E = {E:.3f}\,E_h$")
        readout.set_color(TEAL if hit else CARDINAL)

    ani = FuncAnimation(fig, update, frames=len(Es), interval=200, blit=False)
    return fig, ani


hydrogen_shooting.fps = 5


# ------------------------------------------------------------ the radial functions for n <= 3: polynomial times exponential, nodes in red (still)
@register
def radial_functions():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
    R = {(1, 0): lambda p: 2 * np.exp(-p),
         (2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
         (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
         (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
         (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
         (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
    nodes = {(1, 0): [], (2, 0): [2.0], (2, 1): [], (3, 0): [1.902, 7.098], (3, 1): [6.0], (3, 2): []}
    names = {(1, 0): "1s", (2, 0): "2s", (2, 1): "2p", (3, 0): "3s", (3, 1): "3p", (3, 2): "3d"}
    fig, axes = plt.subplots(2, 3, figsize=(9.6, 5.0), gridspec_kw={"hspace": 0.5, "wspace": 0.22})
    for ax, key in zip(axes.flat, [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]):
        n, l = key
        xm = 12 if n < 3 else 24
        p = np.linspace(0, xm, 500)
        y = R[key](p)
        ax.axhline(0, color=GRAY, lw=0.8)
        ax.plot(p, y, color=cols[l], lw=2.4)
        ax.plot(nodes[key], [0] * len(nodes[key]), "o", color=CARDINAL, ms=7, zorder=5)
        top = max(y.max(), 0.08) if n > 1 else y.max()
        ax.set_xlim(0, xm); ax.set_ylim(min(-0.22 * top, 1.15 * y.min()), 1.15 * top)
        ax.set_title(names[key], fontsize=13.5, color=cols[l], weight="bold")
        ax.tick_params(labelsize=10)
    for ax in axes[1]:
        ax.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5)
    for ax in axes[:, 0]:
        ax.set_ylabel(r"$R_{nl}(r)$", fontsize=11.5)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.11)
    fig.savefig(f"{OUT}/radial_functions.png", dpi=200)
    print("wrote", f"{OUT}/radial_functions.png")
    return fig, None


# ------------------------------------------------------------ the hydrogen ladder: every level n holds n^2 states, one bar per (l, m) (still)
@register
def hydrogen_ladder():
    fig, ax = plt.subplots(figsize=(8.4, 5.0))
    cols = {0: TEAL, 1: PURPLE, 2: ORANGE, 3: GRAY}
    letters = "spdf"
    w, g = 0.13, 0.04                                                # width of one state's bar, gap between bars
    xc = [0, 1.0, 2.1, 3.4]                                          # column centers: wider columns for the wider ladders
    Eh2 = 13.606
    ax.axhspan(0, 1.0, color="#dee2e6", lw=0, zorder=0)
    ax.axhline(0, color=GRAY, lw=0.8, ls=":")
    ax.text(4.1, 0.5, "free electron, any $E > 0$", ha="right", va="center", fontsize=11, color=GRAY)
    for n in range(1, 5):
        E = -Eh2 / n**2
        ax.hlines(E, -0.35, 4.1, color="#ced4da", lw=0.8, zorder=1)
        ax.text(-0.5, E, rf"$n = {n}$", ha="right", va="center", fontsize=12.5)
        ax.text(4.3, E, rf"${n * n}$", ha="left", va="center", fontsize=12.5)
        for l in range(n):
            k = 2 * l + 1
            x0 = xc[l] - 0.5 * (k * w + (k - 1) * g)
            for j in range(k):
                ax.plot([x0 + j * (w + g), x0 + j * (w + g) + w], [E, E], color=cols[l], lw=4, solid_capstyle="butt", zorder=3)
    for l in range(4):
        ax.text(xc[l], 2.05, letters[l], ha="center", va="center", fontsize=15, color=cols[l], weight="bold")
        ax.text(xc[l], 1.35, rf"$l = {l}$", ha="center", va="center", fontsize=11, color=cols[l])
    ax.text(4.3, 2.05, "states", ha="left", va="center", fontsize=12.5)
    ax.set_xlim(-1.5, 4.9); ax.set_ylim(-14.6, 2.5)
    ax.set_xticks([]); ax.set_yticks([-13.6, -3.4, -1.51, -0.85, 0])
    ax.set_yticklabels(["-13.6", "-3.40", "-1.51", "-0.85", "0"], fontsize=10.5)
    ax.set_ylabel("energy (eV)", fontsize=12)
    for sp in ("top", "right", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.spines["left"].set_bounds(-13.6, 0)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.97, bottom=0.03)
    fig.savefig(f"{OUT}/hydrogen_ladder.png", dpi=200)
    print("wrote", f"{OUT}/hydrogen_ladder.png")
    return fig, None


# ------------------------------------------------------------ the Balmer lines as seen through a spectroscope, and the H / D pair at H-alpha (still)
@register
def balmer_lines():
    RH, RD = 109677.58, 109707.43                                    # Rydberg constants of H and D, cm^-1
    lam = lambda R, n: 1e7 / (R * (0.25 - 1 / n**2))                 # Balmer wavelength in nm, vacuum
    w = np.linspace(355, 700, 1381)                                  # colour of each wavelength, a piecewise rainbow
    Rc = np.where(w < 440, (440 - w) / 60, np.where(w < 510, 0, np.where(w < 580, (w - 510) / 70, 1)))
    Gc = np.where(w < 440, 0, np.where(w < 490, (w - 440) / 50, np.where(w < 580, 1, np.where(w < 645, (645 - w) / 65, 0))))
    Bc = np.where(w < 490, 1, np.where(w < 510, (510 - w) / 20, 0))
    fade = np.clip(np.where(w < 420, 0.3 + 0.7 * (w - 380) / 40, np.where(w > 650, 0.35 + 0.65 * (700 - w) / 50, 1)), 0, 1)
    rgb = np.clip(np.stack([Rc, Gc, Bc], -1) * fade[:, None], 0, 1)
    colour_at = lambda x: rgb[np.argmin(np.abs(w - x))]
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.6, 4.6), gridspec_kw={"height_ratios": [1.15, 1], "hspace": 0.75})
    for a_ in (ax, bx):
        a_.set_facecolor("#111111"); a_.set_yticks([])
        for sp in a_.spines.values():
            sp.set_color("#444444")
        a_.tick_params(labelsize=10.5)
    ax.imshow((0.22 * rgb)[None, :, :], extent=[355, 700, 0, 1], aspect="auto", zorder=0)
    for n in range(3, 11):
        x = lam(RH, n)
        ax.vlines(x, 0, 1, color=colour_at(x), lw=2.6 if n < 7 else 1.4, zorder=2)
        if n <= 6:
            ax.text(x, 1.06, rf"$n = {n}$", ha="center", va="bottom", fontsize=11)
    xl = lam(RH, 1e9)
    ax.vlines(xl, 0, 1, color="#cccccc", lw=1.4, ls="--", zorder=2)
    ax.text(xl, 1.06, "limit", ha="center", va="bottom", fontsize=11, color=GRAY)
    ax.set_xlim(355, 700); ax.set_ylim(0, 1)
    ax.set_xlabel("wavelength (nm)", fontsize=11.5)
    xH, xD = lam(RH, 3), lam(RD, 3)
    for x, name in ((xH, "H"), (xD, "D")):
        bx.vlines(x, 0, 1, color=colour_at(656.4), lw=3, zorder=2)
        bx.text(x, 1.06, name, ha="center", va="bottom", fontsize=12.5)
    bx.annotate("", xy=(xD, 0.5), xytext=(xH, 0.5), arrowprops=dict(arrowstyle="<->", color="white", lw=1.2, shrinkA=3, shrinkB=3))
    bx.text(0.5 * (xH + xD), 0.57, f"{xH - xD:.2f} nm", ha="center", va="bottom", fontsize=11, color="white")
    bx.set_xlim(655.9, 656.85); bx.set_ylim(0, 1)
    bx.set_xticks([656.0, 656.2, 656.4, 656.6, 656.8])
    bx.set_xlabel(r"wavelength (nm), near $n = 3 \to 2$", fontsize=11.5)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.9, bottom=0.12)
    fig.savefig(f"{OUT}/balmer_lines.png", dpi=200)
    print("wrote", f"{OUT}/balmer_lines.png")
    return fig, None


# ============================================================ lecture 5.2: atomic orbitals

# the real angular functions in x, y, z (unit vectors), normalized on the sphere; shared by the figures below
# s: 1/sqrt(4 pi); p: sqrt(3/4pi) {x, y, z}; d: sqrt(15/4pi) {xy, yz, xz}, sqrt(15/16pi)(x^2 - y^2), sqrt(5/16pi)(3z^2 - 1)

# ------------------------------------------------------------ why r^2: the density of 1s, the area of a shell, and their product P(r) (still)
@register
def shell_volume():
    from matplotlib.colors import LinearSegmentedColormap
    from matplotlib.patches import Wedge, Circle
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx, cx, dx) = plt.subplots(1, 4, figsize=(9.6, 2.9), gridspec_kw={"wspace": 0.42, "width_ratios": [1.0, 1, 1, 1]})
    # (a) the 1s cloud cut through the nucleus, with a thin shell between r and r + dr
    g = np.linspace(-3, 3, 301)
    X, Y = np.meshgrid(g, g)
    cmap = LinearSegmentedColormap.from_list("ts", ["white", TEAL])
    ax.imshow(np.exp(-2 * np.hypot(X, Y)), extent=(-3, 3, -3, 3), cmap=cmap, vmin=0, vmax=1, origin="lower", zorder=0)
    r0, dr0 = 1.7, 0.3
    ax.add_patch(Wedge((0, 0), r0 + dr0, 0, 360, width=dr0, facecolor=ORANGE, edgecolor=ORANGE, alpha=0.75, lw=1.2, zorder=2))
    ax.add_patch(Circle((0, 0), r0, fill=False, ec=ORANGE, lw=1.2, zorder=3))
    ax.annotate("", xy=(r0 * np.cos(0.6), r0 * np.sin(0.6)), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="#212529", lw=1.3, shrinkA=0, shrinkB=0), zorder=4)
    ax.text(0.95, 0.3, r"$r$", fontsize=12, color="#212529", zorder=5)
    ax.text(r0 + dr0 + 0.12, -0.05, r"$dr$", fontsize=11, color=ORANGE, va="center", zorder=5)
    ax.plot(0, 0, "o", color="#212529", ms=4, zorder=5)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_aspect("equal"); ax.axis("off")
    # (b) the density, (c) the area of the shell, (d) their product
    r = np.linspace(0, 5, 400)
    dens, area = np.exp(-2 * r) / np.pi, 4 * np.pi * r**2
    for a_, y, col, lab in ((bx, dens, TEAL, r"$|\psi_{1s}|^2$"), (cx, area, GRAY, r"$4\pi r^2$"), (dx, dens * area, TEAL, r"$P(r)$")):
        a_.plot(r, y, color=col, lw=2.4)
        a_.set_xlim(0, 5); a_.set_ylim(0, 1.12 * y.max())
        a_.set_xlabel(r"$r$ ($a_0$)", fontsize=11); a_.set_yticks([])
        a_.set_title(lab, fontsize=13, color=col)
        a_.set_xticks([0, 1, 2, 3, 4, 5])
    cx.set_ylim(0, 4 * np.pi * 4.2)
    dx.axvline(1, color=CARDINAL, lw=1.2, ls=":")
    dx.text(1.12, 0.52 * (dens * area).max(), r"$a_0$", fontsize=11.5, color=CARDINAL)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.86, bottom=0.2)
    fig.savefig(f"{OUT}/shell_volume.png", dpi=200)
    print("wrote", f"{OUT}/shell_volume.png")
    return fig, None


# ------------------------------------------------------------ the radial distributions P(r) = r^2 R^2 for n <= 3, one panel per shell (still)
@register
def radial_distributions():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    R = {(1, 0): lambda p: 2 * np.exp(-p),
         (2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
         (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
         (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
         (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
         (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
    cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.3), gridspec_kw={"wspace": 0.28, "width_ratios": [0.8, 1, 1.2]})
    for ax, n, xm in zip(axes, (1, 2, 3), (6, 16, 30)):
        r = np.linspace(0, xm, 600)
        for l in range(n):
            P = r**2 * R[(n, l)](r)**2
            ax.plot(r, P, color=cols[l], lw=2.4, label=f"{n}{'spd'[l]}")
        ax.axvline(n * n, color=GRAY, lw=1.1, ls=":")
        ax.text(n * n + 0.02 * xm, 0.56, f"${n * n if n > 1 else ''}a_0$", fontsize=11, color=GRAY)
        leg = ax.legend(loc="upper right", frameon=False, fontsize=12, handlelength=1.2, borderaxespad=0.2)
        for t, h in zip(leg.get_texts(), leg.legend_handles):
            t.set_color(h.get_color()); t.set_weight("bold")
        ax.set_xlim(0, xm); ax.set_ylim(0, 0.6)
        ax.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5)
        ax.set_title(f"$n = {n}$", fontsize=13)
        ax.tick_params(labelsize=10)
    axes[0].set_ylabel(r"$P(r) = r^2R_{nl}^2$  (per $a_0$)", fontsize=11.5)
    for ax in axes[1:]:
        ax.set_yticklabels([])
    fig.subplots_adjust(left=0.08, right=0.99, top=0.88, bottom=0.18)
    fig.savefig(f"{OUT}/radial_distributions.png", dpi=200)
    print("wrote", f"{OUT}/radial_distributions.png")
    return fig, None


# ------------------------------------------------------------ how much of the electron lies inside r: 1s shaded to a0 and to the 90% radius; cumulative curves for n <= 3 (still)
@register
def probability_inside():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    R = {(1, 0): lambda p: 2 * np.exp(-p),
         (2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
         (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
         (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
         (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
         (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
    cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.6), gridspec_kw={"wspace": 0.3, "width_ratios": [1, 1.25]})
    r = np.linspace(0, 6, 601)
    P = 4 * r**2 * np.exp(-2 * r)
    ax.plot(r, P, color=TEAL, lw=2.4)
    ax.fill_between(r, P, where=r <= 1, color=TEAL, alpha=0.45, lw=0)
    ax.fill_between(r, P, where=(r > 1) & (r <= 2.661), color=TEAL, alpha=0.18, lw=0)
    ax.axvline(1, color=CARDINAL, lw=1.2, ls=":"); ax.axvline(2.661, color=GRAY, lw=1.2, ls=":")
    ax.text(0.5, 0.1, "32%", ha="center", fontsize=12, color="white", weight="bold")
    ax.text(1.8, 0.1, "58%", ha="center", fontsize=12, color=TEAL, weight="bold")
    ax.text(1.06, 0.57, r"$a_0$", fontsize=11.5, color=CARDINAL)
    ax.text(2.72, 0.57, r"$2.66\,a_0$", fontsize=11.5, color=GRAY)
    ax.set_xlim(0, 6); ax.set_ylim(0, 0.62)
    ax.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5); ax.set_ylabel(r"$P(r)$ for 1s  (per $a_0$)", fontsize=11.5)
    ax.tick_params(labelsize=10)
    rr = np.linspace(0, 32, 3201)
    dr = rr[1] - rr[0]
    for (n, l), f in R.items():
        c = np.cumsum(rr**2 * f(rr)**2) * dr
        bx.plot(rr, c, color=cols[l], lw=2.2, ls={1: "-", 2: "-", 3: "-"}[n])
        k = np.searchsorted(c, 0.9)
        bx.plot(rr[k], 0.9, "o", color=cols[l], ms=5.5, zorder=5)
        dx_, dy_, ha_ = {(1, 0): (0.0, 0.95, "center"), (2, 1): (-0.5, 0.82, "right"), (2, 0): (0.5, 0.82, "left"),
                         (3, 2): (0.0, 0.68, "center"), (3, 1): (-0.5, 0.82, "right"), (3, 0): (0.5, 0.82, "left")}[(n, l)]
        bx.text(rr[k] + dx_, dy_, f"{n}{'spd'[l]}", fontsize=11, color=cols[l], weight="bold", ha=ha_)
    bx.axhline(0.9, color=GRAY, lw=1, ls=":")
    bx.text(31.5, 0.905, "90%", ha="right", va="bottom", fontsize=11, color=GRAY)
    bx.set_xlim(0, 32); bx.set_ylim(0, 1.04)
    bx.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5); bx.set_ylabel("probability inside $r$", fontsize=11.5)
    bx.tick_params(labelsize=10)
    fig.subplots_adjust(left=0.07, right=0.99, top=0.95, bottom=0.17)
    fig.savefig(f"{OUT}/probability_inside.png", dpi=200)
    print("wrote", f"{OUT}/probability_inside.png")
    return fig, None


# ------------------------------------------------------------ the m = +1 state runs around z while p_x stands: real parts in time, and the two densities (animation, 30 frames)
@register
def p_running():
    from scipy.special import sph_harm_y
    from matplotlib.colors import to_rgb
    S = 221
    u = np.linspace(-1, 1, S)
    U, V = np.meshgrid(u, u[::-1])
    inside = U**2 + V**2 < 1
    W = np.sqrt(np.clip(1 - U**2 - V**2, 0, None))
    el, az = np.radians(22), np.radians(-55)
    cam = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])
    ex = np.array([-np.sin(az), np.cos(az), 0.0])
    ey = np.cross(cam, ex)
    Pt = U[..., None] * ex + V[..., None] * ey + W[..., None] * cam
    TH, PH = np.arccos(np.clip(Pt[..., 2], -1, 1)), np.arctan2(Pt[..., 1], Pt[..., 0])
    light = np.array([-0.45, 0.55, 0.7]) / np.linalg.norm([-0.45, 0.55, 0.7])
    shade = (0.5 + 0.5 * np.clip(U * light[0] + V * light[1] + W * light[2], 0, 1))[..., None]
    white, pos, neg, dcol = np.ones(3), np.array(to_rgb(TEAL)), np.array(to_rgb(ORANGE)), np.array(to_rgb(PURPLE))
    paint = lambda s: np.dstack([np.clip(np.where(s[..., None] > 0, white + s[..., None] * (pos - white), white - s[..., None] * (neg - white)), 0, 1) * shade, inside.astype(float)])
    dens = lambda d: np.dstack([np.clip(white + d[..., None] * (dcol - white), 0, 1) * shade, inside.astype(float)])
    Yp = sph_harm_y(1, 1, TH, PH)                                   # m = +1
    px = ((sph_harm_y(1, -1, TH, PH) - Yp) / np.sqrt(2)).real       # p_x
    top1, top2 = np.sqrt(3 / (8 * np.pi)), np.sqrt(3 / (4 * np.pi))
    fig, axes = plt.subplots(2, 2, figsize=(6.0, 6.2), gridspec_kw={"wspace": 0.05, "hspace": 0.12})
    ims = []
    for row, (Y, top, lab) in enumerate(((Yp, top1, r"$Y_1^{+1}$"), (px, top2, r"$p_x$"))):
        ax, bx = axes[row]
        for a_ in (ax, bx):
            a_.set_xlim(-1.08, 1.08); a_.set_ylim(-1.08, 1.3); a_.set_aspect("equal"); a_.axis("off")
            a_.add_patch(plt.Circle((0, 0), 1, fill=False, ec="#868e96", lw=0.8, zorder=3))
            a_.plot([0, 0], [ey[2], ey[2] + 0.28], color="#495057", lw=1.4, zorder=3)
            a_.text(0.07, ey[2] + 0.26, "$z$", fontsize=10.5, color="#495057", va="center")
        ims.append(ax.imshow(paint(Y.real / top), extent=(-1, 1, -1, 1), interpolation="bilinear", zorder=1))
        bx.imshow(dens(np.abs(Y)**2 / top**2), extent=(-1, 1, -1, 1), interpolation="bilinear", zorder=1)
        ax.text(-1.22, 0, lab, fontsize=15, ha="right", va="center")
    axes[0, 0].set_title(r"Re $\psi(t)$", fontsize=13.5); axes[0, 1].set_title(r"$|\psi|^2$", fontsize=13.5)
    frames = 30
    def update(k):
        ph = np.exp(-1j * 2 * np.pi * k / frames)
        ims[0].set_data(paint((Yp * ph).real / top1))
        ims[1].set_data(paint((px * ph).real / top2))
    fig.subplots_adjust(left=0.14, right=0.99, top=0.93, bottom=0.02)
    ani = FuncAnimation(fig, update, frames=frames, interval=100, blit=False)
    return fig, ani


p_running.fps = 10


# ------------------------------------------------------------ the three L_z eigenstates of l = 1 (densities: two rings, one dumbbell) and the three real p orbitals (still)
@register
def complex_to_real():
    from matplotlib.colors import LightSource, to_rgb
    th, ph = np.meshgrid(np.linspace(0, np.pi, 73), np.linspace(0, 2 * np.pi, 145), indexing="ij")
    st, ct, cp, sp = np.sin(th), np.cos(th), np.cos(ph), np.sin(ph)
    x, y, z = st * cp, st * sp, ct
    ls = LightSource(azdeg=300, altdeg=40)
    pos, neg, dcol = np.array(to_rgb(TEAL)), np.array(to_rgb(ORANGE)), np.array(to_rgb(PURPLE))
    fig = plt.figure(figsize=(9.6, 5.6))
    def balloon(ax, dens, sign, lab):
        rho = dens / dens.max()
        fc = np.where(sign[..., None] >= 0, pos, neg) if sign is not None else np.broadcast_to(dcol, rho.shape + (3,))
        ax.plot_surface(rho * x, rho * y, rho * z, facecolors=fc, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=True, lightsource=ls)
        for v, name, off in (((1.15, 0, 0), "$x$", (1.12, 0, 0)), ((0, 1.15, 0), "$y$", (0, 1.12, 0)), ((0, 0, 1.05), "$z$", (0.16, 0, 0.98))):
            ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color="#868e96", lw=1.0)
            ax.text(v[0] * off[0] + off[0] * (v[0] == 0), v[1] * off[1] + off[1] * (v[1] == 0), v[2] * off[2] + off[2] * (v[2] == 0), name, fontsize=11, color="#495057", ha="center", va="center")
        ax.set_xlim(-0.9, 0.9); ax.set_ylim(-0.9, 0.9); ax.set_zlim(-0.9, 0.9)
        ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=20, azim=-58); ax.set_axis_off()
        ax.set_title(lab, fontsize=14, y=0.97)
    # top row: |Y_1^m|^2 for m = +1, 0, -1 (densities, purple: no sign to show)
    for k, (m, lab) in enumerate(((1, r"$|Y_1^{+1}|^2$"), (0, r"$|Y_1^{0}|^2$"), (-1, r"$|Y_1^{-1}|^2$"))):
        ax = fig.add_subplot(2, 3, k + 1, projection="3d")
        d = (3 / (8 * np.pi)) * st**2 if m else (3 / (4 * np.pi)) * ct**2
        balloon(ax, d, None, lab)
    # bottom row: the real combinations, coloured by sign
    for k, (f, lab) in enumerate(((x, r"$p_x$"), (y, r"$p_y$"), (z, r"$p_z$"))):
        ax = fig.add_subplot(2, 3, k + 4, projection="3d")
        balloon(ax, f**2, f, lab)
    fig.subplots_adjust(left=0.0, right=1.0, top=0.96, bottom=0.0, wspace=0.0, hspace=0.0)
    fig.savefig(f"{OUT}/complex_to_real.png", dpi=200)
    print("wrote", f"{OUT}/complex_to_real.png")
    return fig, None


# ------------------------------------------------------------ the nine real orbitals with l <= 2 as angular densities, coloured by the sign of the wavefunction (still)
@register
def orbital_shapes():
    from matplotlib.colors import LightSource, to_rgb
    th, ph = np.meshgrid(np.linspace(0, np.pi, 73), np.linspace(0, 2 * np.pi, 145), indexing="ij")
    st, ct, cp, sp = np.sin(th), np.cos(th), np.cos(ph), np.sin(ph)
    x, y, z = st * cp, st * sp, ct
    ls = LightSource(azdeg=300, altdeg=40)
    pos, neg = np.array(to_rgb(TEAL)), np.array(to_rgb(ORANGE))
    shapes = [("s", np.ones_like(x), TEAL), (r"$p_x$", x, PURPLE), (r"$p_y$", y, PURPLE), (r"$p_z$", z, PURPLE), None,
              (r"$d_{xy}$", x * y, ORANGE), (r"$d_{yz}$", y * z, ORANGE), (r"$d_{xz}$", x * z, ORANGE),
              (r"$d_{x^2-y^2}$", x**2 - y**2, ORANGE), (r"$d_{z^2}$", 3 * z**2 - 1, ORANGE)]
    fig = plt.figure(figsize=(9.6, 4.4))
    for k, item in enumerate(shapes):
        if item is None:
            continue
        lab, f, col = item
        ax = fig.add_subplot(2, 5, k + 1, projection="3d")
        rho = f**2 / (f**2).max()
        fc = np.where(f[..., None] >= 0, pos, neg)
        ax.plot_surface(rho * x, rho * y, rho * z, facecolors=fc, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=True, lightsource=ls)
        for v, name, off in (((1.15, 0, 0), "$x$", (1.12, 0, 0)), ((0, 1.15, 0), "$y$", (0, 1.12, 0)), ((0, 0, 1.05), "$z$", (0.16, 0, 0.98))):
            ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color="#868e96", lw=0.9)
            ax.text(v[0] * off[0] + off[0] * (v[0] == 0), v[1] * off[1] + off[1] * (v[1] == 0), v[2] * off[2] + off[2] * (v[2] == 0), name, fontsize=10, color="#495057", ha="center", va="center")
        ax.set_xlim(-0.9, 0.9); ax.set_ylim(-0.9, 0.9); ax.set_zlim(-0.9, 0.9)
        ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=20, azim=-58); ax.set_axis_off()
        ax.set_title(lab, fontsize=13.5, color=col, y=0.97)
    fig.subplots_adjust(left=0.0, right=1.0, top=0.95, bottom=0.0, wspace=0.0, hspace=0.0)
    fig.savefig(f"{OUT}/orbital_shapes.png", dpi=200)
    print("wrote", f"{OUT}/orbital_shapes.png")
    return fig, None


# ------------------------------------------------------------ cross-sections of psi through the nucleus for n <= 3: radial nodes are circles, angular nodes lines or cones (still)
@register
def orbital_slices():
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("ot", [ORANGE, "white", TEAL])
    Rf = {(1, 0): lambda p: 2 * np.exp(-p),
          (2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
          (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
          (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
          (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
          (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
    # (name, n, l, angular factor of (h, v) = the two in-plane coordinates over r, plane labels, box, colour clip)
    panels = [("1s", 1, 0, lambda h, v, r: np.full_like(r, 1 / np.sqrt(4 * np.pi)), ("x", "z"), 4, 1.0),
              ("2s", 2, 0, lambda h, v, r: np.full_like(r, 1 / np.sqrt(4 * np.pi)), ("x", "z"), 10, 0.35),
              (r"2p$_z$", 2, 1, lambda h, v, r: np.sqrt(3 / (4 * np.pi)) * v / r, ("x", "z"), 10, 0.6),
              ("3s", 3, 0, lambda h, v, r: np.full_like(r, 1 / np.sqrt(4 * np.pi)), ("x", "z"), 20, 0.2),
              (r"3p$_z$", 3, 1, lambda h, v, r: np.sqrt(3 / (4 * np.pi)) * v / r, ("x", "z"), 20, 0.5),
              (r"3d$_{z^2}$", 3, 2, lambda h, v, r: np.sqrt(5 / (16 * np.pi)) * (3 * v**2 - r**2) / r**2, ("x", "z"), 20, 0.6),
              (r"3d$_{xz}$", 3, 2, lambda h, v, r: np.sqrt(15 / (4 * np.pi)) * h * v / r**2, ("x", "z"), 20, 0.6),
              (r"3d$_{x^2-y^2}$", 3, 2, lambda h, v, r: np.sqrt(15 / (16 * np.pi)) * (h**2 - v**2) / r**2, ("x", "y"), 20, 0.6)]
    cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
    fig, axes = plt.subplots(2, 4, figsize=(9.6, 5.3), gridspec_kw={"wspace": 0.3, "hspace": 0.42})
    for ax, (name, n, l, ang, (hl, vl), box, clip) in zip(axes.flat, panels):
        g = np.linspace(-box, box, 361)
        Hc, Vc = np.meshgrid(g, g)
        r = np.hypot(Hc, Vc) + 1e-9
        psi = Rf[(n, l)](r) * ang(Hc, Vc, r)
        top = clip * np.abs(psi).max()
        ax.contourf(Hc, Vc, np.clip(psi, -top, top), levels=np.linspace(-top, top, 41), cmap=cmap)
        if n > 1 or l > 0:
            ax.contour(Hc, Vc, psi, levels=[0], colors=CARDINAL, linewidths=1.3, linestyles="--")
        ax.set_aspect("equal"); ax.set_xlim(-box, box); ax.set_ylim(-box, box)
        ax.set_xticks([-box, 0, box]); ax.set_yticks([-box, 0, box]); ax.tick_params(labelsize=9.5)
        ax.set_xlabel(f"${hl}$ ($a_0$)", fontsize=10.5, labelpad=1); ax.set_ylabel(f"${vl}$ ($a_0$)", fontsize=10.5, labelpad=0)
        ax.set_title(name, fontsize=13, color=cols[l], weight="bold")
    fig.subplots_adjust(left=0.06, right=0.99, top=0.94, bottom=0.08)
    fig.savefig(f"{OUT}/orbital_slices.png", dpi=200)
    print("wrote", f"{OUT}/orbital_slices.png")
    return fig, None


if __name__ == "__main__":
    names = sys.argv[1:] or list(REGISTRY)
    for name in names:
        fig, ani = REGISTRY[name]()
        if ani is not None:
            path = f"{OUT}/{name}.gif"
            ani.save(path, writer=PillowWriter(fps=getattr(REGISTRY[name], "fps", 15)), dpi=GIF_DPI)
            print("wrote", path)
        plt.close(fig)
