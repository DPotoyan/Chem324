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
(page ch05/02, deck slides/ch05/02) those in "lecture 5.2"; Lecture 5.3 (page ch05/03, deck slides/ch05/03) those
in "lecture 5.3".
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


# ------------------------------------------------------------ the s states 1s, 2s, 3s on one axis: farther out and one more peak each step (still)
@register
def radial_s_series():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    R = {1: lambda p: 2 * np.exp(-p),
         2: lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
         3: lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3))}
    shades = {1: "#0a4a5c", 2: TEAL, 3: "#63b4c8"}                 # one family (s): three shades of teal
    fig, ax = plt.subplots(figsize=(9.6, 3.4))
    r = np.linspace(0, 26, 1300)
    for n in (1, 2, 3):
        P = r**2 * R[n](r)**2
        ax.plot(r, P, color=shades[n], lw=2.6)
        k = np.argmax(P)
        ax.text(r[k], P[k] + 0.018, f"{n}s", fontsize=13, color=shades[n], weight="bold", ha="center", va="bottom")
    ax.set_xlim(0, 26); ax.set_ylim(0, 0.6)
    ax.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5)
    ax.set_ylabel(r"$P(r) = r^2R_{n0}^2$  (per $a_0$)", fontsize=11.5)
    ax.tick_params(labelsize=10)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.96, bottom=0.18)
    fig.savefig(f"{OUT}/radial_s_series.png", dpi=200)
    print("wrote", f"{OUT}/radial_s_series.png")
    return fig, None


# ------------------------------------------------------------ same n, different l: the radial distributions of the n = 2 and n = 3 shells (still)
@register
def radial_distributions():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    R = {(2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
         (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
         (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
         (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
         (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
    cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.4), gridspec_kw={"wspace": 0.18, "width_ratios": [1, 1.3]})
    for ax, n, xm in zip(axes, (2, 3), (16, 30)):
        r = np.linspace(0, xm, 600)
        for l in range(n):
            ax.plot(r, r**2 * R[(n, l)](r)**2, color=cols[l], lw=2.4, label=f"{n}{'spd'[l]}")
        ax.axvline(n * n, color=GRAY, lw=1.1, ls=":")
        ax.text(n * n + 0.02 * xm, 0.22, f"${n * n}a_0$", fontsize=11, color=GRAY)
        ax.set_xlim(0, xm); ax.set_ylim(0, 0.24)
        ax.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5)
        ax.set_title(f"$n = {n}$", fontsize=13)
        ax.tick_params(labelsize=10)
        leg = ax.legend(loc="upper right", frameon=False, fontsize=12, handlelength=1.2, borderaxespad=0.2)
        for t, h in zip(leg.get_texts(), leg.legend_handles):
            t.set_color(h.get_color()); t.set_weight("bold")
    axes[0].set_ylabel(r"$P(r) = r^2R_{nl}^2$  (per $a_0$)", fontsize=11.5)
    axes[1].set_yticklabels([])
    fig.subplots_adjust(left=0.08, right=0.99, top=0.88, bottom=0.18)
    fig.savefig(f"{OUT}/radial_distributions.png", dpi=200)
    print("wrote", f"{OUT}/radial_distributions.png")
    return fig, None


# ------------------------------------------------------------ count the peaks: P(r) for every state with n <= 3, radial nodes as red dots (still)
@register
def radial_nodes():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    R = {(1, 0): lambda p: 2 * np.exp(-p),
         (2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
         (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
         (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
         (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
         (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
    nodes = {(1, 0): [], (2, 0): [2.0], (2, 1): [], (3, 0): [1.902, 7.098], (3, 1): [6.0], (3, 2): []}
    cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
    fig, axes = plt.subplots(2, 3, figsize=(9.6, 4.3), gridspec_kw={"hspace": 0.55, "wspace": 0.12})
    for ax, key in zip(axes.flat, [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]):
        n, l = key
        xm = {1: 6, 2: 16, 3: 30}[n]
        r = np.linspace(0, xm, 600)
        P = r**2 * R[key](r)**2
        ax.plot(r, P, color=cols[l], lw=2.4)
        ax.fill_between(r, P, color=cols[l], alpha=0.12, lw=0)
        ax.plot(nodes[key], [0] * len(nodes[key]), "o", color=CARDINAL, ms=7.5, zorder=5, clip_on=False)
        ax.set_xlim(0, xm); ax.set_ylim(0, 1.15 * P.max())
        ax.set_yticks([]); ax.tick_params(labelsize=10)
        ax.set_title(f"{n}{'spd'[l]}", fontsize=13.5, color=cols[l], weight="bold")
    for ax in axes[1]:
        ax.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5)
    for ax in axes[:, 0]:
        ax.set_ylabel(r"$P(r)$", fontsize=11.5)
    fig.subplots_adjust(left=0.05, right=0.99, top=0.92, bottom=0.13)
    fig.savefig(f"{OUT}/radial_nodes.png", dpi=200)
    print("wrote", f"{OUT}/radial_nodes.png")
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
        yl = 1.2 if l == 0 and n > 1 else 1.08                      # labels above the curves, in two rows
        bx.plot([rr[k], rr[k]], [0.92, yl - 0.03], color=cols[l], lw=0.9, ls=":")
        bx.text(rr[k], yl, f"{n}{'spd'[l]}", fontsize=11.5, color=cols[l], weight="bold", ha="center", va="center")
    bx.axhline(0.9, color=GRAY, lw=1, ls=":")
    bx.text(31.5, 0.905, "90%", ha="right", va="bottom", fontsize=11, color=GRAY)
    bx.set_xlim(0, 32); bx.set_ylim(0, 1.27); bx.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    bx.spines["left"].set_bounds(0, 1.0)
    bx.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5); bx.set_ylabel("probability inside $r$", fontsize=11.5)
    bx.tick_params(labelsize=10)
    fig.subplots_adjust(left=0.07, right=0.99, top=0.95, bottom=0.17)
    fig.savefig(f"{OUT}/probability_inside.png", dpi=200)
    print("wrote", f"{OUT}/probability_inside.png")
    return fig, None


# ------------------------------------------------------------ the l = 1 states of definite m as 2D cuts: a dumbbell along z, and a ring around z seen from the side and from above (still)
@register
def m_states_cuts():
    t = np.linspace(0, 2 * np.pi, 721)
    DARK = "#495057"
    fig, axes = plt.subplots(1, 3, figsize=(8.0, 3.1))
    # (density in the direction at angle t, measured from the vertical axis; horizontal and vertical axis names; title)
    panels = [(np.cos(t)**2, "x", "z", r"$|Y_1^{0}|^2 \propto \cos^2\theta$"),
              (np.sin(t)**2, "x", "z", r"$|Y_1^{\pm1}|^2 \propto \sin^2\theta$"),
              (np.ones_like(t), "x", "y", r"$|Y_1^{\pm1}|^2$ from above")]
    for ax, (rho, hl, vl, lab) in zip(axes, panels):
        ax.plot([-1.3, 1.3], [0, 0], color="#adb5bd", lw=1.1, zorder=1)
        ax.plot([0, 0], [-1.3, 1.3], color="#adb5bd", lw=1.1, zorder=1)
        ax.text(1.36, 0, f"${hl}$", fontsize=15, color=DARK, ha="left", va="center")
        ax.text(0, 1.36, f"${vl}$", fontsize=15, color=DARK, ha="center", va="bottom")
        ax.fill(rho * np.sin(t), rho * np.cos(t), color=PURPLE, alpha=0.16, zorder=2)
        ax.plot(rho * np.sin(t), rho * np.cos(t), color=PURPLE, lw=2.6, zorder=3)
        ax.set_xlim(-1.62, 1.62); ax.set_ylim(-1.5, 1.74); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(lab, fontsize=15.5, pad=6)
        if vl == "z":       # a turn about z changes nothing: the curved arrow around the axis
            a = np.radians(np.linspace(115, 425, 80))
            ax.plot(0.2 * np.cos(a), 1.17 + 0.065 * np.sin(a), color=DARK, lw=1.5, zorder=4)
            ax.annotate("", xy=(0.2 * np.cos(a[-1]), 1.17 + 0.065 * np.sin(a[-1])), xytext=(0.2 * np.cos(a[-4]), 1.17 + 0.065 * np.sin(a[-4])),
                        arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.5, mutation_scale=13), zorder=4)
        else:               # seen from above, z points at the viewer: a dot in a circle
            ax.plot(0, 0, "o", ms=11, mfc="white", mec=DARK, mew=1.4, zorder=4)
            ax.plot(0, 0, "o", ms=3.4, color=DARK, zorder=5)
            ax.text(0.14, -0.2, "$z$", fontsize=15, color=DARK, ha="left", va="center")
    fig.subplots_adjust(left=0.0, right=1.0, top=0.9, bottom=0.0, wspace=0.0)
    fig.savefig(f"{OUT}/m_states_cuts.png", dpi=200)
    print("wrote", f"{OUT}/m_states_cuts.png")
    return fig, None


# ------------------------------------------------------------ z is the axis we measured theta from: the same point, the same dumbbell, with the polar axis along z or along x (still)
@register
def axis_choice():
    t = np.linspace(0, 2 * np.pi, 721)
    DARK = "#495057"
    beta = np.radians(52)                                  # the sample point, 52 degrees above the x axis
    P = 1.22 * np.array([np.cos(beta), np.sin(beta)])
    fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.45))
    # (polar axis, angle of that axis in the drawing, arc from, arc to, name of the angle and where it sits, title)
    panels = [("z", np.pi / 2, beta, np.pi / 2, r"$\theta$", (0.21, 0.64), r"$\cos\theta = z/r$"),
              ("x", 0.0, 0.0, beta, r"$\theta_x$", (0.63, 0.19), r"$\cos\theta_x = x/r$")]
    for ax, (pol, a0, a1, a2, name, at, lab) in zip(axes, panels):
        for nm, d in (("x", np.array([1.0, 0.0])), ("z", np.array([0.0, 1.0]))):
            bold = nm == pol
            ax.plot([-1.4 * d[0], 1.4 * d[0]], [-1.4 * d[1], 1.4 * d[1]], color=DARK if bold else "#adb5bd", lw=2.6 if bold else 1.1, zorder=4 if bold else 1, solid_capstyle="butt")
            if bold:
                ax.annotate("", xy=1.58 * d, xytext=1.36 * d, arrowprops=dict(arrowstyle="-|>", color=DARK, lw=2.6, mutation_scale=20), zorder=4)
            ax.text(1.7 * d[0], 1.7 * d[1], f"${nm}$", fontsize=17, color=DARK if bold else GRAY, weight="bold" if bold else "normal", ha="center", va="center")
        f = np.cos(t - a0)                                 # the wavefunction: cosine of the angle from the polar axis
        rho = f**2
        for sgn, col in ((1, TEAL), (-1, ORANGE)):
            keep = np.where(sgn * f >= 0, rho, 0.0)
            ax.fill(keep * np.cos(t), keep * np.sin(t), color=col, alpha=0.3, lw=0, zorder=2)
            ax.plot(np.where(sgn * f >= 0, rho * np.cos(t), np.nan), np.where(sgn * f >= 0, rho * np.sin(t), np.nan), color=col, lw=2.6, zorder=3)
        ax.plot([0, P[0]], [0, P[1]], color=CARDINAL, lw=1.6, zorder=5)
        ax.plot(P[0], P[1], "o", ms=7.5, color=CARDINAL, zorder=6)
        arc = np.linspace(a1, a2, 40)
        ax.plot(0.46 * np.cos(arc), 0.46 * np.sin(arc), color=CARDINAL, lw=1.6, zorder=5)
        ax.text(at[0], at[1], name, fontsize=17, color=CARDINAL, ha="center", va="center", zorder=6)
        ax.set_xlim(-1.85, 1.85); ax.set_ylim(-1.55, 1.85); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(lab, fontsize=17, pad=4)
    fig.subplots_adjust(left=0.0, right=1.0, top=0.91, bottom=0.0, wspace=0.0)
    fig.savefig(f"{OUT}/axis_choice.png", dpi=200)
    print("wrote", f"{OUT}/axis_choice.png")
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

# ============================================================ lecture 5.3: electron spin
# Colours in this section: m_s = +1/2 TEAL and m_s = -1/2 ORANGE (the sign colours of 5.2), orbital angular
# momentum and p levels PURPLE (j = 3/2 PURPLE, j = 1/2 a lighter purple), magnetic moments CARDINAL, fields and
# apparatus GRAY. The letter mu is a magnetic moment in this lecture (the reduced mass does not appear).

# ------------------------------------------------------------ an orbiting electron is a loop of current: L up, magnetic moment down, the loop's field lines behind (still)
@register
def current_loop():
    from scipy.special import ellipk, ellipe
    fig, ax = plt.subplots(figsize=(5.6, 4.7))
    a, b = 1.5, 0.46                                             # the orbit: a circle of radius a seen at a tilt
    # field lines of a circular current loop in the plane of the page: contours of the flux rho * A_phi
    g = np.linspace(-3.6, 3.6, 361)
    X, Z = np.meshgrid(g, np.linspace(-3.0, 3.0, 301))
    rho = np.abs(X) + 1e-6
    k2 = 4 * a * rho / ((a + rho)**2 + Z**2)
    flux = np.sqrt(a * rho) * ((2 - k2) * ellipk(k2) - 2 * ellipe(k2)) / np.sqrt(k2)
    ax.contour(X, Z, flux, levels=[0.12, 0.3, 0.6, 1.05, 1.7], colors="#ced4da", linewidths=1.1, zorder=0)
    t = np.linspace(0, 2 * np.pi, 400)
    ax.fill(a * np.cos(t), b * np.sin(t), color=PURPLE, alpha=0.07, lw=0, zorder=1)
    ax.plot(a * np.cos(t), b * np.sin(t), color="#343a40", lw=2.0, zorder=2)
    arrow = lambda p0, p1, col, lw, ms: ax.annotate("", xy=p1, xytext=p0, zorder=6, arrowprops=dict(
        arrowstyle="-|>", color=col, lw=lw, mutation_scale=ms, shrinkA=0, shrinkB=0))
    arrow((0, 0), (0, 2.05), PURPLE, 3.0, 20)                    # angular momentum, up for counterclockwise motion
    arrow((0, 0), (0, -2.05), CARDINAL, 3.0, 20)                 # magnetic moment, opposite: the charge is negative
    ax.text(0.18, 1.95, r"$\vec{L}$", fontsize=19, color=PURPLE, va="center")
    ax.text(0.18, -1.95, r"$\vec{\mu}$", fontsize=19, color=CARDINAL, va="center")
    f = np.radians(-58)                                          # the electron, on the near side of the orbit
    pe = np.array([a * np.cos(f), b * np.sin(f)])
    ax.plot([0, pe[0]], [0, pe[1]], color=GRAY, lw=1.3, ls=(0, (4, 3)), zorder=3)
    ax.text(0.5, -0.07, r"$r$", fontsize=16, color=GRAY, ha="center", va="center")
    tv = np.array([-a * np.sin(f), b * np.cos(f)]); tv = tv / np.hypot(*tv)
    arrow(pe, pe + 1.0 * tv, TEAL, 2.4, 17)
    ax.text(*(pe + 1.0 * tv + np.array([0.2, 0.05])), r"$\vec{v}$", fontsize=17, color=TEAL, va="center")
    ax.plot(*pe, "o", color=TEAL, ms=12, zorder=7)
    ax.text(pe[0] - 0.05, pe[1] - 0.36, r"$-e$", fontsize=16, color=TEAL, ha="center", va="center")
    f2 = np.radians(118)                                         # the current runs against the electron
    pc = np.array([a * np.cos(f2), b * np.sin(f2)])
    tc = np.array([a * np.sin(f2), -b * np.cos(f2)]); tc = tc / np.hypot(*tc)
    arrow(pc - 0.01 * tc, pc + 0.3 * tc, "#343a40", 2.0, 20)
    ax.text(pc[0] - 0.12, pc[1] + 0.3, r"$I$", fontsize=17, color="#343a40", ha="center", va="center")
    ax.set_xlim(-3.3, 3.3); ax.set_ylim(-2.75, 2.75); ax.set_aspect("equal"); ax.axis("off")
    fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
    fig.savefig(f"{OUT}/current_loop.png", dpi=200)
    print("wrote", f"{OUT}/current_loop.png")
    return fig, None


# ------------------------------------------------------------ a magnet in a uniform field feels no net force; between a wedge and a groove it is pulled or pushed (still)
@register
def gradient_force():
    from matplotlib.patches import Polygon, Rectangle
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.2), gridspec_kw={"wspace": 0.04})
    arrow = lambda a_, p0, p1, col, lw, ms: a_.annotate("", xy=p1, xytext=p0, zorder=6, arrowprops=dict(
        arrowstyle="-|>", color=col, lw=lw, mutation_scale=ms, shrinkA=0, shrinkB=0))
    # a small bar magnet centred at (x0, 0): its moment (red arrow, S to N), the forces on its two poles, the net force.
    # The field pushes the N pole along B (up) and the S pole against it (down), harder where B is stronger.
    magnets = [(ax, 0.0, 1, 0.85, 0.85), (bx, -1.05, 1, 0.55, 1.15), (bx, 1.05, -1, 0.55, 1.15)]
    for a_, x0, up, f_top, f_bot in magnets:
        a_.add_patch(Rectangle((x0 - 0.2, -0.62), 0.4, 1.24, fc="white", ec="#343a40", lw=1.6, zorder=4))
        arrow(a_, (x0, -0.48 * up), (x0, 0.5 * up), CARDINAL, 3.0, 17)
        a_.text(x0 - 0.38, 0.42 * up, "N", fontsize=14, ha="center", va="center", weight="bold", color="#343a40")
        a_.text(x0 - 0.38, -0.42 * up, "S", fontsize=14, ha="center", va="center", weight="bold", color="#343a40")
        for end, f in ((1, f_top), (-1, f_bot)):                 # end = +1 the top pole, -1 the bottom pole
            ends = [(x0, end * 0.68), (x0, end * (0.68 + f))]    # from the pole outward
            if up < 0:                                           # N below, S above: both forces point into the magnet, draw them pushing
                ends = ends[::-1]
            arrow(a_, ends[0], ends[1], GRAY, 2.0, 14)
        net = up * (f_top - f_bot)
        if abs(net) > 0.01:
            arrow(a_, (x0 + 0.6, -0.5 * np.sign(net)), (x0 + 0.6, 0.7 * np.sign(net)), "#212529", 4.2, 24)
            a_.text(x0 + 0.82, 0.1 * np.sign(net), r"$\vec{F}$", fontsize=18, va="center", color="#212529")
    # left: a uniform field
    for x in np.linspace(-2.4, 2.4, 9):
        ax.plot([x, x], [-2.3, 2.3], color="#ced4da", lw=1.2, zorder=0)
        arrow(ax, (x, 1.9), (x, 2.3), "#ced4da", 1.2, 11)
    ax.text(2.62, 2.05, r"$\vec{B}$", fontsize=17, color=GRAY, va="center")
    ax.set_title("uniform field", fontsize=14)
    # right: the Stern-Gerlach magnet in cross-section, a sharp edge below and a groove above; B is strongest at the edge
    bx.add_patch(Polygon([[-2.6, -2.9], [2.6, -2.9], [2.6, -2.45], [0, -1.75], [-2.6, -2.45]], fc="#dee2e6", ec=GRAY, lw=1.3, zorder=2))
    th = np.linspace(np.pi, 2 * np.pi, 80)
    top = [[-2.6, 2.9], [-2.6, 2.0]] + [[1.5 * np.cos(q), 2.0 - 0.62 * np.sin(q)] for q in th] + [[2.6, 2.0], [2.6, 2.9]]
    bx.add_patch(Polygon(top, fc="#dee2e6", ec=GRAY, lw=1.3, zorder=2))
    for xt in np.linspace(-1.35, 1.35, 9):                       # field lines fan out from the edge to the groove
        zz = np.linspace(0, 1, 60)
        zt = 2.0 + 0.62 * np.sqrt(max(0.0, 1 - (xt / 1.5)**2))
        xs = xt * (0.06 + 0.94 * zz**1.25)
        zs = (-1.75 + 0.33 * abs(xt)) + (zt - (-1.75 + 0.33 * abs(xt))) * zz
        bx.plot(xs, zs, color="#ced4da", lw=1.2, zorder=0)
        arrow(bx, (xs[-9], zs[-9]), (xs[-1], zs[-1]), "#ced4da", 1.2, 11)
    bx.text(2.05, 1.55, r"$\vec{B}$", fontsize=17, color=GRAY, va="center")
    bx.set_title("non-uniform field", fontsize=14)
    for a_ in (ax, bx):
        a_.set_xlim(-3.0, 3.0); a_.set_ylim(-3.0, 3.0); a_.set_aspect("equal"); a_.axis("off")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.92, bottom=0.01)
    fig.savefig(f"{OUT}/gradient_force.png", dpi=200)
    print("wrote", f"{OUT}/gradient_force.png")
    return fig, None


# ------------------------------------------------------------ the orbital Zeeman effect: 2p fans into three levels, one line becomes three (still)
@register
def zeeman_orbital():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"width_ratios": [1.2, 1], "wspace": 0.1})
    B = np.linspace(0, 1, 50)
    E2, E1, s = 3.2, 0.0, 0.85                                   # schematic: the real 2p - 1s gap is 10^5 splittings
    for m in (1, 0, -1):
        ax.plot(B, E2 + s * m * B, color=PURPLE, lw=2.6)
        ax.text(1.04, E2 + s * m, rf"$m_l = {m:+d}$" if m else r"$m_l = 0$", va="center", fontsize=13, color=PURPLE)
    ax.plot(B, E1 + 0 * B, color=TEAL, lw=2.6)
    ax.text(1.04, E1, r"$m_l = 0$", va="center", fontsize=13, color=TEAL)
    ax.text(-0.05, E2, "2p", ha="right", va="center", fontsize=15, color=PURPLE, weight="bold")
    ax.text(-0.05, E1, "1s", ha="right", va="center", fontsize=15, color=TEAL, weight="bold")
    for k, m in enumerate((-1, 0, 1)):                           # the three lines: Delta m_l = -1, 0, +1
        x = 0.66 + 0.11 * k
        ax.annotate("", xy=(x, E2 + s * m * x), xytext=(x, E1), arrowprops=dict(arrowstyle="-|>", color="#495057", lw=1.8,
                                                                              mutation_scale=14, shrinkA=0, shrinkB=0))
    ax.set_xlim(-0.25, 1.42); ax.set_ylim(-0.5, 4.5)
    ax.set_xticks([0]); ax.set_xticklabels(["0"], fontsize=11); ax.set_yticks([])
    ax.set_xlabel(r"magnetic field $B$", fontsize=12.5); ax.set_ylabel("energy", fontsize=12.5)
    ax.spines["bottom"].set_bounds(0, 1)
    # the spectrum: one line without the field, three with it
    for y0, lines in ((1.25, (0,)), (0.0, (-1, 0, 1))):
        bx.add_patch(plt.Rectangle((-2.2, y0), 4.4, 0.8, fc="#f1f3f5", ec="#ced4da", lw=1))
        for d in lines:
            bx.plot([d, d], [y0, y0 + 0.8], color="#495057", lw=3.2, solid_capstyle="butt")
    bx.text(-2.35, 1.65, r"$B = 0$", ha="right", va="center", fontsize=13.5)
    bx.text(-2.35, 0.4, r"$B > 0$", ha="right", va="center", fontsize=13.5)
    bx.set_xlim(-3.6, 2.3); bx.set_ylim(-0.25, 2.3)
    bx.set_xticks([-1, 0, 1]); bx.set_xticklabels([r"$\nu_0 - \mu_BB/h$", r"$\nu_0$", r"$\nu_0 + \mu_BB/h$"], fontsize=11.5)
    bx.set_yticks([]); bx.spines["left"].set_visible(False); bx.spines["bottom"].set_bounds(-2.2, 2.2)
    bx.set_xlabel("frequency", fontsize=12.5, labelpad=6)
    fig.subplots_adjust(left=0.05, right=0.99, top=0.97, bottom=0.2)
    fig.savefig(f"{OUT}/zeeman_orbital.png", dpi=200)
    print("wrote", f"{OUT}/zeeman_orbital.png")
    return fig, None


# ------------------------------------------------------------ Stern and Gerlach: a beam of atoms splits in two in a non-uniform field (animation, 36 frames)
@register
def stern_gerlach():
    from matplotlib.patches import Rectangle
    rng = np.random.default_rng(5)
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.2, 3.5), gridspec_kw={"width_ratios": [4.3, 1], "wspace": 0.03})
    xm0, xm1, xp, kk = 2.5, 5.5, 8.7, 0.043                     # magnet from xm0 to xm1, plate at xp; z = +-kk (x - xm0)^2 inside
    n_fr, per, dx = 36, 3, 0.36                                  # frames, atoms launched per frame, distance per frame
    N = n_fr * per
    sgn = rng.choice([1, -1], N)                                 # which way each atom goes: decided only at the magnet
    z0 = rng.normal(0, 0.03, N)
    zland = rng.normal(0, 0.09, N)
    yland = rng.uniform(-0.8, 0.8, N)
    frac = rng.uniform(0, 1, N)
    bend = lambda x: np.where(x < xm0, 0.0, np.where(x < xm1, (x - xm0)**2, (xm1 - xm0)**2 + 2 * (xm1 - xm0) * (x - xm1)))
    zend = kk * float(bend(np.array(xp)))
    ax.add_patch(Rectangle((0.0, -0.6), 1.05, 1.2, fc="#dee2e6", ec=GRAY, lw=1.3))
    ax.text(0.52, -0.85, "oven", ha="center", va="top", fontsize=12.5, color=GRAY)
    for s in (1, -1):
        ax.plot([1.75, 1.75], [s * 0.2, s * 0.8], color=GRAY, lw=3.5, solid_capstyle="butt")
        ax.add_patch(Rectangle((xm0, 0.62 if s > 0 else -1.62), xm1 - xm0, 1.0, fc="#dee2e6", ec=GRAY, lw=1.3))
    ax.text(0.5 * (xm0 + xm1), 1.12, "magnet", ha="center", va="center", fontsize=12.5, color=GRAY)
    ax.plot([xp, xp], [-2.0, 2.0], color="#343a40", lw=4, solid_capstyle="butt")
    ax.text(xp, -2.2, "plate", ha="center", va="top", fontsize=12.5, color=GRAY)
    xs = np.linspace(1.05, xp, 200)
    for s, col in ((1, TEAL), (-1, ORANGE)):
        ax.plot(xs, s * kk * bend(xs), color=col, lw=1.0, alpha=0.35, zorder=1)
    fly = ax.scatter([], [], s=26, zorder=5)
    ax.set_xlim(-0.2, 9.1); ax.set_ylim(-2.6, 2.3); ax.axis("off")
    bx.add_patch(Rectangle((-1.05, -2.0), 2.1, 4.0, fc="#f1f3f5", ec="#343a40", lw=1.6))
    hits = bx.scatter([], [], s=20, zorder=5)
    bx.text(0, -2.2, "plate, face on", ha="center", va="top", fontsize=12.5, color=GRAY)
    bx.set_xlim(-1.5, 1.5); bx.set_ylim(-2.6, 2.3); bx.axis("off")
    dark, cols = np.array([0.29, 0.31, 0.34, 1.0]), {1: np.array([0.063, 0.471, 0.584, 1.0]), -1: np.array([0.878, 0.482, 0.0, 1.0])}

    def update(f):
        x = 1.05 + (f - np.arange(N) // per + frac) * dx          # how far each atom has flown by frame f
        on = (x >= 1.05) & (x < xp)
        z = z0 * (x < 1.75) + sgn * kk * bend(x)
        c = np.array([dark if xi < xm0 else cols[si] for xi, si in zip(x[on], sgn[on])]).reshape(-1, 4)
        fly.set_offsets(np.c_[x[on], z[on]]); fly.set_facecolors(c)
        done = x >= xp
        hits.set_offsets(np.c_[yland[done], sgn[done] * zend + zland[done]])
        hits.set_facecolors(np.array([cols[si] for si in sgn[done]]).reshape(-1, 4))

    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.02)
    ani = FuncAnimation(fig, update, frames=n_fr, interval=100, blit=False)
    return fig, ani


stern_gerlach.fps = 10


# ------------------------------------------------------------ what the plate should show (classical smear, one spot for l = 0, three for l = 1) and what it showed (still)
@register
def sg_screens():
    from matplotlib.patches import Rectangle
    rng = np.random.default_rng(11)
    fig, axes = plt.subplots(1, 4, figsize=(9.6, 3.7), gridspec_kw={"wspace": 0.12})
    n = 360
    cases = [("classical magnet", rng.uniform(-1.25, 1.25, n), "#343a40"),
             (r"$l = 0$", np.zeros(n), "#343a40"),
             (r"$l = 1$", rng.choice([-1.25, 0, 1.25], n), "#343a40"),
             ("silver, observed", rng.choice([-1.25, 1.25], n), CARDINAL)]
    for ax, (name, z, col) in zip(axes, cases):
        ax.add_patch(Rectangle((-1.05, -2.0), 2.1, 4.0, fc="#f1f3f5", ec="#343a40", lw=1.6))
        ax.scatter(rng.uniform(-0.8, 0.8, n), z + rng.normal(0, 0.1, n), s=11, color="#495057", alpha=0.55, lw=0)
        ax.set_title(name, fontsize=14.5, color=col)
        ax.set_xlim(-1.3, 1.3); ax.set_ylim(-2.15, 2.15); ax.set_aspect("equal"); ax.axis("off")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.01)
    fig.savefig(f"{OUT}/sg_screens.png", dpi=200)
    print("wrote", f"{OUT}/sg_screens.png")
    return fig, None


# ------------------------------------------------------------ the vector model, orbital l = 1 beside spin s = 1/2 on one scale: three cones and two, no angle marks (still)
@register
def spin_cones():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.1), gridspec_kw={"wspace": 0.0})
    t = np.linspace(0, 2 * np.pi, 300)
    LIGHT = "#cdb9e3"
    half = lambda k: ("+" if k > 0 else "-") + r"\frac{1}{2}"
    # (panel, length in hbar, [(height m, arrow colour, cone colour, two label lines)], title, length label)
    panels = [(ax, np.sqrt(2), [(1, PURPLE, LIGHT, (r"$m_l = +1$", r"$L_z = +\hbar$")), (0, PURPLE, LIGHT, (r"$m_l = 0$", r"$L_z = 0$")),
                                (-1, PURPLE, LIGHT, (r"$m_l = -1$", r"$L_z = -\hbar$"))],
               r"orbital, $l = 1$", r"$|\vec{L}| = \sqrt{2}\,\hbar$"),
              (bx, np.sqrt(3) / 2, [(0.5, TEAL, TEAL, (rf"$m_s = {half(1)}$", rf"$S_z = {half(1)}\hbar$")),
                                    (-0.5, ORANGE, ORANGE, (rf"$m_s = {half(-1)}$", rf"$S_z = {half(-1)}\hbar$"))],
               r"spin, $s = \frac{1}{2}$", r"$|\vec{S}| = \frac{\sqrt{3}}{2}\hbar$")]
    for a_, R, states, title, lenlab in panels:
        a_.plot(R * np.cos(t), R * np.sin(t), color=GRAY, lw=1, ls=":")
        a_.annotate("", xy=(0, 1.9), xytext=(0, -1.7), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=14,
                                                                        shrinkA=0, shrinkB=0))
        a_.text(0.09, 1.84, "$z$", fontsize=17, va="center")
        for m, col, cone, (l1, l2) in states:
            rm = np.sqrt(R * R - m * m)                          # radius of the cone's rim: the part of the vector off the z axis
            alpha = 1.0 if cone == LIGHT else 0.45
            a_.plot(rm * np.cos(t), m + 0.2 * rm * np.sin(t), color=cone, lw=1.6, alpha=alpha)
            a_.plot([-rm, 0, rm], [m, 0, m], color=cone, lw=1.3, alpha=alpha)
            a_.annotate("", xy=(rm, m), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2.8, mutation_scale=18,
                                                                       shrinkA=0, shrinkB=0))
            a_.plot([0], [m], "o", color=col, ms=5.5, zorder=5)
            a_.plot([rm + 0.05, 1.5], [m, m], color=GRAY, lw=0.8, ls=(0, (2, 3)))
            a_.text(1.58, m + 0.17, l1, va="center", fontsize=18, color=col)
            a_.text(1.58, m - 0.19, l2, va="center", fontsize=18, color=col)
        a_.text(-0.2, -1.52, lenlab, fontsize=18, color=GRAY, ha="right", va="center")
        a_.set_title(title, fontsize=18)
        a_.set_xlim(-1.72, 2.85); a_.set_ylim(-1.78, 1.98)
        a_.set_aspect("equal"); a_.axis("off")
    fig.subplots_adjust(left=0.0, right=1.0, top=0.91, bottom=0.0)
    fig.savefig(f"{OUT}/spin_cones.png", dpi=200)
    print("wrote", f"{OUT}/spin_cones.png")
    return fig, None


# ------------------------------------------------------------ one magnet after another: z then z, z then x, z then x then z (still)
@register
def sg_sequence():
    from matplotlib.patches import Rectangle, FancyBboxPatch
    fig, ax = plt.subplots(figsize=(9.6, 4.4))
    w, hgt, gap = 1.25, 0.9, 2.55                                 # analyser width and height, spacing
    rows = [("(a)", 2.5, ["z", "z"], [("+z", "100%"), ("-z", "0")]),
            ("(b)", 0.0, ["z", "x"], [("+x", "50%"), ("-x", "50%")]),
            ("(c)", -2.5, ["z", "x", "z"], [("+z", "50%"), ("-z", "50%")])]
    for tag, y, axes_, outs in rows:
        ax.text(-0.75, y, tag, fontsize=14.5, ha="center", va="center", color="#343a40")
        ax.add_patch(Rectangle((-0.3, y - 0.3), 0.75, 0.6, fc="#dee2e6", ec=GRAY, lw=1.2))
        if tag == "(a)":
            ax.text(0.08, y - 0.42, "oven", fontsize=12, ha="center", va="top", color=GRAY)
        ax.plot([0.45, 1.6], [y, y], color="#495057", lw=2.2)
        for i, name in enumerate(axes_):
            x0 = 1.6 + gap * i
            ax.add_patch(FancyBboxPatch((x0, y - hgt / 2), w, hgt, boxstyle="round,pad=0,rounding_size=0.12", fc="white", ec="#343a40", lw=1.8, zorder=3))
            ax.text(x0 + w / 2, y, f"${name}$", fontsize=20, ha="center", va="center", zorder=4)
            last = i == len(axes_) - 1
            if not last:                                         # keep the + beam, block the - beam
                ax.plot([x0 + w, x0 + w + 0.45, x0 + gap], [y + 0.25, y + 0.25, y], color=TEAL, lw=2.4, zorder=2)
                ax.plot([x0 + w, x0 + w + 0.5], [y - 0.25, y - 0.25], color=ORANGE, lw=2.4, zorder=2)
                ax.plot([x0 + w + 0.5, x0 + w + 0.5], [y - 0.5, y - 0.02], color="#343a40", lw=4.5, solid_capstyle="butt", zorder=3)
            else:
                for (lab, pct), sgn, col in zip(outs, (1, -1), (TEAL, ORANGE)):
                    none = pct == "0"
                    ax.annotate("", xy=(x0 + w + 1.0, y + sgn * 0.25), xytext=(x0 + w, y + sgn * 0.25), zorder=2,
                                arrowprops=dict(arrowstyle="-|>", color="#ced4da" if none else col, lw=2.4, mutation_scale=16,
                                                shrinkA=0, shrinkB=0, ls=(0, (3, 2)) if none else "-"))
                    ax.text(x0 + w + 1.15, y + sgn * 0.3, f"${lab}$", fontsize=15, va="center", color=GRAY if none else col)
                    ax.text(x0 + w + 1.85, y + sgn * 0.3, pct, fontsize=15, va="center", weight="bold", color=GRAY if none else col)
    ax.set_xlim(-1.1, 10.6); ax.set_ylim(-3.3, 3.3); ax.axis("off")
    fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
    fig.savefig(f"{OUT}/sg_sequence.png", dpi=200)
    print("wrote", f"{OUT}/sg_sequence.png")
    return fig, None


# ------------------------------------------------------------ a spin 1/2 in a field has two levels: the electron (GHz, EPR) and the proton (MHz, NMR) (still)
@register
def spin_resonance():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"wspace": 0.72})
    # (panel, slope of the splitting in frequency per tesla, largest field, field of the arrow, its label, m label, which state is lower)
    panels = [(ax, 2.0023 * 13.996, 0.5, 0.34, "9.5 GHz", "m_s", -1), (bx, 42.577, 12.0, 9.4, "400 MHz", "m_I", 1)]
    for a_, slope, Bmax, B0, lab, mname, low in panels:
        B = np.linspace(0, Bmax, 50)
        for m, col, name in ((0.5, TEAL, r"\alpha"), (-0.5, ORANGE, r"\beta")):
            a_.plot(B, -low * m * slope * B, color=col, lw=2.6)
            a_.text(1.02 * Bmax, -low * m * slope * Bmax, rf"${name}$, ${mname} = {'+' if m > 0 else '-'}\frac{{1}}{{2}}$", color=col,
                    fontsize=13, va="center")
        a_.annotate("", xy=(B0, 0.5 * slope * B0), xytext=(B0, -0.5 * slope * B0), arrowprops=dict(arrowstyle="<|-|>", color="#343a40",
                                                                                         lw=1.8, mutation_scale=14, shrinkA=0, shrinkB=0))
        a_.text(B0 - 0.03 * Bmax, 0, lab, fontsize=13.5, ha="right", va="center", color="#343a40",
                bbox=dict(fc="white", ec="none", pad=1.5))
        a_.set_xlim(0, Bmax); a_.set_ylim(-0.6 * slope * Bmax, 0.6 * slope * Bmax)
        a_.set_xlabel(r"magnetic field $B$ (T)", fontsize=12); a_.tick_params(labelsize=10.5)
    ax.set_ylabel(r"energy / $h$ (GHz)", fontsize=12); bx.set_ylabel(r"energy / $h$ (MHz)", fontsize=12)
    ax.set_title("electron", fontsize=14); bx.set_title("proton", fontsize=14)
    fig.subplots_adjust(left=0.075, right=0.855, top=0.9, bottom=0.17)
    fig.savefig(f"{OUT}/spin_resonance.png", dpi=200)
    print("wrote", f"{OUT}/spin_resonance.png")
    return fig, None


# ------------------------------------------------------------ spin-orbit coupling: seen from the electron, the nucleus circles it and makes a field at the spin (still)
@register
def spin_orbit_frames():
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"wspace": 0.02})
    a, b = 1.6, 0.5
    t = np.linspace(0, 2 * np.pi, 400)
    arrow = lambda a_, p0, p1, col, lw, ms: a_.annotate("", xy=p1, xytext=p0, zorder=6, arrowprops=dict(
        arrowstyle="-|>", color=col, lw=lw, mutation_scale=ms, shrinkA=0, shrinkB=0))
    f = np.radians(-52)
    pe = np.array([a * np.cos(f), b * np.sin(f)])
    tv = np.array([-a * np.sin(f), b * np.cos(f)]); tv = tv / np.hypot(*tv)
    for a_ in (ax, bx):
        a_.fill(a * np.cos(t), b * np.sin(t), color=PURPLE, alpha=0.06, lw=0, zorder=1)
        a_.plot(a * np.cos(t), b * np.sin(t), color="#868e96", lw=1.6, zorder=2)
        a_.set_xlim(-2.6, 2.6); a_.set_ylim(-1.75, 2.2); a_.set_aspect("equal"); a_.axis("off")
    # left: the nucleus at rest, the electron circles it
    ax.plot(0, 0, "o", color="#343a40", ms=13, zorder=7)
    ax.text(-0.12, -0.36, r"$+Ze$", fontsize=14.5, color="#343a40", ha="center", va="center")
    ax.plot(*pe, "o", color=TEAL, ms=9, zorder=7)
    ax.text(pe[0] + 0.02, pe[1] - 0.33, r"$-e$", fontsize=14.5, color=TEAL, ha="center", va="center")
    arrow(ax, pe, pe + 0.85 * tv, TEAL, 2.2, 15)
    arrow(ax, (0, 0), (0, 1.75), PURPLE, 3.0, 19)
    ax.text(0.16, 1.62, r"$\vec{L}$", fontsize=18, color=PURPLE, va="center")
    ax.set_title("nucleus at rest", fontsize=14)
    # right: the electron at rest; the nucleus circles it the same way, a loop of positive current whose field is along L
    f2 = np.radians(-128)
    pn = np.array([a * np.cos(f2), b * np.sin(f2)])
    tn = np.array([-a * np.sin(f2), b * np.cos(f2)]); tn = tn / np.hypot(*tn)
    bx.plot(*pn, "o", color="#343a40", ms=13, zorder=7)
    bx.text(pn[0] - 0.1, pn[1] - 0.38, r"$+Ze$", fontsize=14.5, color="#343a40", ha="center", va="center")
    arrow(bx, pn, pn + 0.85 * tn, "#343a40", 2.2, 15)
    arrow(bx, (-0.62, -0.1), (-0.62, 1.75), GRAY, 3.0, 19)
    bx.text(-0.78, 1.62, r"$\vec{B}$", fontsize=18, color=GRAY, va="center", ha="right")
    bx.plot(0, 0, "o", color=TEAL, ms=9, zorder=7)
    arrow(bx, (0, 0), (0, 1.2), TEAL, 2.8, 17)
    bx.text(0.16, 1.1, r"$\vec{S}$", fontsize=18, color=TEAL, va="center")
    arrow(bx, (0, 0), (0, -1.2), CARDINAL, 2.8, 17)
    bx.text(0.16, -1.12, r"$\vec{\mu}_s$", fontsize=18, color=CARDINAL, va="center")
    bx.text(0.2, -0.02, r"$-e$", fontsize=14.5, color=TEAL, ha="left", va="center")
    bx.set_title("electron at rest", fontsize=14)
    fig.subplots_adjust(left=0.0, right=1.0, top=0.92, bottom=0.0)
    fig.savefig(f"{OUT}/spin_orbit_frames.png", dpi=200)
    print("wrote", f"{OUT}/spin_orbit_frames.png")
    return fig, None


# ------------------------------------------------------------ adding l = 1 and s = 1/2: six states sorted by m_j = m_l + m_s make a ladder of four and a ladder of two (still)
@register
def adding_momenta():
    from matplotlib.patches import Rectangle, Polygon
    LIGHT = "#b9a3dc"
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"width_ratios": [1.25, 1], "wspace": 0.05})
    frac = lambda k: (r"+" if k > 0 else r"-") + rf"\frac{{{abs(k)}}}{{2}}"          # k halves, as a signed fraction
    cw, ch = 1.3, 1.0
    for i, ml in enumerate((1, 0, -1)):
        ax.text(i * cw + cw / 2, 2 * ch + 0.28, rf"$m_l = {ml:+d}$" if ml else r"$m_l = 0$", ha="center", va="center", fontsize=14, color=PURPLE)
        for j, ms2 in enumerate((1, -1)):                        # ms2 = 2 m_s
            x0, y0 = i * cw, (1 - j) * ch
            mj2 = 2 * ml + ms2                                   # 2 m_j
            if abs(mj2) == 3:                                    # m_j = +-3/2 occurs once: it belongs to j = 3/2
                ax.add_patch(Rectangle((x0, y0), cw, ch, fc=PURPLE, alpha=0.75, lw=0))
            else:                                                # m_j = +-1/2 occurs twice: shared between j = 3/2 and j = 1/2
                ax.add_patch(Polygon([[x0, y0], [x0 + cw, y0 + ch], [x0, y0 + ch]], fc=PURPLE, alpha=0.75, lw=0))
                ax.add_patch(Polygon([[x0, y0], [x0 + cw, y0], [x0 + cw, y0 + ch]], fc=LIGHT, alpha=0.9, lw=0))
            ax.add_patch(Rectangle((x0, y0), cw, ch, fill=False, ec="white", lw=3))
            ax.text(x0 + cw / 2, y0 + ch / 2, rf"${frac(mj2)}$", ha="center", va="center", fontsize=19, color="white", weight="bold")
    for j, (ms2, col) in enumerate(((1, TEAL), (-1, ORANGE))):
        ax.text(-0.15, (1 - j) * ch + ch / 2, rf"$m_s = {frac(ms2)}$", ha="right", va="center", fontsize=14, color=col)
    ax.text(1.5 * cw, -0.32, r"$m_j = m_l + m_s$", ha="center", va="center", fontsize=14, color="#343a40")
    ax.set_xlim(-1.75, 3 * cw + 0.2); ax.set_ylim(-0.75, 2.75); ax.axis("off")
    # the same six states as two ladders
    for xc, j2, col in ((0.0, 3, PURPLE), (1.9, 1, LIGHT)):
        for mj2 in range(-j2, j2 + 1, 2):
            bx.plot([xc - 0.6, xc + 0.6], [mj2 / 2, mj2 / 2], color=col, lw=5, solid_capstyle="butt")
        bx.text(xc, 2.05, rf"$j = \frac{{{j2}}}{{2}}$", ha="center", va="center", fontsize=16, color=PURPLE if j2 == 3 else "#8566c2")
    for mj2 in (3, 1, -1, -3):
        bx.text(-0.85, mj2 / 2, rf"${frac(mj2)}$", ha="right", va="center", fontsize=14.5, color="#343a40")
    bx.text(-1.05, 2.05, r"$m_j$", ha="right", va="center", fontsize=15, color="#343a40")
    bx.set_xlim(-2.2, 2.9); bx.set_ylim(-2.25, 2.55); bx.axis("off")
    fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
    fig.savefig(f"{OUT}/adding_momenta.png", dpi=200)
    print("wrote", f"{OUT}/adding_momenta.png")
    return fig, None


# ------------------------------------------------------------ fine structure: spin-orbit coupling splits a p level into j = 3/2 and j = 1/2; the sodium D doublet (still)
@register
def fine_structure():
    LIGHT = "#b9a3dc"
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.3), gridspec_kw={"width_ratios": [1.15, 1], "wspace": 0.12})
    w, g = 0.2, 0.06                                             # one bar per state, as in the hydrogen ladder of 5.1
    bars = lambda xc, E, k, col: [ax.plot([xc - 0.5 * (k * w + (k - 1) * g) + i * (w + g), xc - 0.5 * (k * w + (k - 1) * g) + i * (w + g) + w],
                                          [E, E], color=col, lw=5, solid_capstyle="butt") for i in range(k)]
    bars(1.0, 0.0, 6, PURPLE)
    bars(3.6, 0.5, 4, PURPLE)
    bars(3.6, -1.0, 2, LIGHT)
    for E in (0.5, -1.0):
        ax.plot([1.85, 2.9], [0, E], color="#adb5bd", lw=1.1, ls=(0, (4, 3)))
    ax.text(1.0, 0.24, r"$n$p", ha="center", va="bottom", fontsize=15, color=PURPLE)
    ax.text(4.25, 0.5, r"$^2$P$_{3/2}$", ha="left", va="center", fontsize=15, color=PURPLE)
    ax.text(4.25, -1.0, r"$^2$P$_{1/2}$", ha="left", va="center", fontsize=15, color="#8566c2")
    ax.text(5.35, 0.5, r"$+\frac{1}{2}A$", ha="left", va="center", fontsize=15, color="#343a40")
    ax.text(5.35, -1.0, r"$-A$", ha="left", va="center", fontsize=15, color="#343a40")
    ax.annotate("", xy=(3.6, 0.42), xytext=(3.6, -0.92), arrowprops=dict(arrowstyle="<|-|>", color=GRAY, lw=1.3, mutation_scale=12, shrinkA=0, shrinkB=0))
    ax.text(3.72, -0.25, r"$\frac{3}{2}A$", ha="left", va="center", fontsize=15, color=GRAY)
    ax.text(1.0, 1.25, "no coupling", ha="center", va="center", fontsize=13, color=GRAY)
    ax.text(3.9, 1.25, "spin-orbit coupling", ha="center", va="center", fontsize=13, color=GRAY)
    ax.set_xlim(0.0, 6.4); ax.set_ylim(-1.6, 1.55); ax.axis("off")
    # the sodium D lines, as in a spectroscope (wavelengths in air)
    bx.set_facecolor("#111111"); bx.set_yticks([])
    for sp in bx.spines.values():
        sp.set_color("#444444")
    D2, D1 = 588.995, 589.592
    for x, name in ((D2, r"D$_2$"), (D1, r"D$_1$")):
        bx.vlines(x, 0, 1, color="#ffd43b", lw=3.2, zorder=2)
        bx.text(x, 1.06, name, ha="center", va="bottom", fontsize=14)
    bx.annotate("", xy=(D1, 0.5), xytext=(D2, 0.5), arrowprops=dict(arrowstyle="<->", color="white", lw=1.2, shrinkA=3, shrinkB=3))
    bx.text(0.5 * (D1 + D2), 0.57, f"{D1 - D2:.2f} nm", ha="center", va="bottom", fontsize=12.5, color="white")
    bx.set_xlim(588.5, 590.1); bx.set_ylim(0, 1)
    bx.set_xticks([588.6, 589.0, 589.4, 589.8]); bx.tick_params(labelsize=11)
    bx.set_xlabel("wavelength (nm), sodium", fontsize=12)
    fig.subplots_adjust(left=0.0, right=0.98, top=0.88, bottom=0.17)
    bx.set_position([0.57, 0.27, 0.4, 0.5])
    fig.savefig(f"{OUT}/fine_structure.png", dpi=200)
    print("wrote", f"{OUT}/fine_structure.png")
    return fig, None


# ------------------------------------------------------------ the six states of a p level against the field: weak field (j, m_j) to strong field (m_l + 2 m_s) (still)
@register
def zeeman_crossover():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    LIGHT = "#b9a3dc"
    Lz = np.diag([1.0, 0.0, -1.0])                               # l = 1 in the basis m_l = +1, 0, -1
    Lp = np.sqrt(2) * np.diag([1.0, 1.0], 1)                     # L+ raises m_l
    Sz = np.diag([0.5, -0.5])                                    # s = 1/2 in the basis alpha, beta
    Sp = np.diag([1.0], 1)                                       # S+ turns beta into alpha
    LS = np.kron(Lz, Sz) + 0.5 * (np.kron(Lp, Sp.T) + np.kron(Lp.T, Sp))   # L.S = Lz Sz + (L+ S- + L- S+)/2, units of hbar^2
    Zm = np.kron(Lz, np.eye(2)) + 2 * np.kron(np.eye(3), Sz)     # Lz + 2 Sz
    mj2 = np.rint(2 * np.diag(np.kron(Lz, np.eye(2)) + np.kron(np.eye(3), Sz))).astype(int)
    b = np.linspace(0, 3, 301)                                   # mu_B B / A
    fig, ax = plt.subplots(figsize=(8.6, 4.6))
    ax.axvspan(0, 0.35, color="#f1f3f5", lw=0, zorder=0)
    for k in (3, 1, -1, -3):                                     # m_j stays sharp at every field: diagonalize block by block
        idx = np.where(mj2 == k)[0]
        E = np.array([np.linalg.eigvalsh((LS + x * Zm)[np.ix_(idx, idx)]) for x in b])
        for c in range(len(idx)):
            upper = len(idx) == 1 or c == 1                      # the branch that starts in j = 3/2
            ax.plot(b, E[:, c], color=PURPLE if upper else LIGHT, lw=2.6)
    for y, lab, col in ((0.5, r"$^2$P$_{3/2}$", PURPLE), (-1.0, r"$^2$P$_{1/2}$", "#8566c2")):
        ax.text(-0.07, y, lab, ha="right", va="center", fontsize=17, color=col)
    ends = [(6.5, "+2"), (3.14, "+1"), (-0.47, r"0, 0"), (-3.19, "-1"), (-5.5, "-2")]
    for y, lab in ends:
        ax.text(3.07, y, rf"${lab}$", ha="left", va="center", fontsize=17, color="#343a40")
    ax.text(3.07, 7.6, r"$m_l + 2m_s$", ha="left", va="center", fontsize=16.5, color="#343a40")
    ax.text(0.175, 7.6, "weak", ha="center", va="center", fontsize=15, color=GRAY)
    ax.text(2.4, 7.6, "strong field", ha="center", va="center", fontsize=15, color=GRAY)
    ax.set_xlim(0, 3); ax.set_ylim(-6.3, 8.2)
    ax.set_xlabel(r"magnetic field, $\mu_BB/A$", fontsize=14.5); ax.set_ylabel(r"energy / $A$", fontsize=14.5)
    ax.set_yticks([-4, -2, 0, 2, 4, 6]); ax.tick_params(labelsize=12.5)
    ax.spines["left"].set_position(("outward", 74)); ax.spines["left"].set_bounds(-6, 6.5)
    fig.subplots_adjust(left=0.2, right=0.85, top=0.98, bottom=0.15)
    fig.savefig(f"{OUT}/zeeman_crossover.png", dpi=200)
    print("wrote", f"{OUT}/zeeman_crossover.png")
    return fig, None


# ------------------------------------------------------------ which lines hydrogen has: levels sorted by l, allowed lines join neighbouring columns (still)
@register
def hydrogen_grotrian():
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
    xc = {0: 0.0, 1: 2.0, 2: 4.0}
    lev = {1: -13.6, 2: -6.0, 3: -2.0}                           # schematic heights
    w = 0.5
    for n in range(1, 4):
        for l in range(n):
            ax.plot([xc[l] - w, xc[l] + w], [lev[n], lev[n]], color=cols[l], lw=3.6, solid_capstyle="butt", zorder=3)
            ax.text(xc[l] + w + 0.08, lev[n], f"{n}{'spd'[l]}", va="center", fontsize=16, color=cols[l])
        ax.text(-1.0, lev[n], rf"$n = {n}$", ha="right", va="center", fontsize=16, color="#343a40")
    # allowed lines: (upper n, l, where on its bar) to (lower n, l, where on its bar); every one joins neighbouring columns
    allowed = [((2, 1, -0.4), (1, 0, 0.2)), ((3, 1, -0.1), (1, 0, 0.45)),
               ((3, 0, 0.3), (2, 1, -0.15)), ((3, 1, -0.35), (2, 0, 0.3)), ((3, 2, -0.3), (2, 1, 0.3))]
    for (n1, l1, d1), (n2, l2, d2) in allowed:
        ax.annotate("", xy=(xc[l2] + d2, lev[n2]), xytext=(xc[l1] + d1, lev[n1]), zorder=2,
                    arrowprops=dict(arrowstyle="-|>", color="#495057", lw=1.7, mutation_scale=13, shrinkA=0, shrinkB=1))
    # forbidden: 2s to 1s (l does not change) and 3d to 1s (l changes by two)
    for (n1, l1, d1), (n2, l2, d2), where in (((2, 0, -0.3), (1, 0, -0.3), 0.5), ((3, 2, 0.45), (1, 0, 0.5), 0.62)):
        p1, p2 = np.array([xc[l1] + d1, lev[n1]]), np.array([xc[l2] + d2, lev[n2]])
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#adb5bd", lw=1.6, ls=(0, (4, 3)), zorder=1)
        pm = p1 + where * (p2 - p1)
        for sg in (1, -1):
            ax.plot([pm[0] - 0.13, pm[0] + 0.13], [pm[1] - sg * 0.48, pm[1] + sg * 0.48], color=CARDINAL, lw=2.8, solid_capstyle="round", zorder=4)
    for l in range(3):
        ax.text(xc[l], 1.3, "spd"[l], ha="center", va="center", fontsize=19, color=cols[l], weight="bold")
        ax.text(xc[l], 0.2, rf"$l = {l}$", ha="center", va="center", fontsize=15, color=cols[l])
    ax.set_xlim(-2.0, 5.3); ax.set_ylim(-14.5, 2.0); ax.axis("off")
    fig.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
    fig.savefig(f"{OUT}/hydrogen_grotrian.png", dpi=200)
    print("wrote", f"{OUT}/hydrogen_grotrian.png")
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
