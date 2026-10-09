"""Chapter 3 animations and deck stills, authored ONCE here (same pipeline as chapter 2).

Each registered function builds one figure (and, for animations, a FuncAnimation) and is
self-contained: it uses only numpy, matplotlib.pyplot, FuncAnimation and the colour
constants below. Running this script bakes the GIFs / PNG stills for the slide decks into
ch03/images/. `scripts/sync_ch03_cells.py` copies the SAME function bodies into the
`{code-cell}` blocks of the lecture pages (marker line `# synced: <name>`), where they are
shown with the matplotlib JS player (house rule: JS player on pages, GIF in decks).

Run from the repo root:
    .venv/bin/python scripts/make_ch03_animations.py                 # bake everything
    .venv/bin/python scripts/make_ch03_animations.py phase_clock     # a subset
    .venv/bin/python scripts/sync_ch03_cells.py                      # refresh page cells

Page weight: the JS player embeds every frame as a PNG, so keep animations to 24-44 frames.
Sync strips every line starting with `return`, so inner helpers must not use it (write a
lambda, or fill an array in place) and `update` must not return artists (use blit=False).
`shooting` is deck-only: the page shows the same idea with a marimo slider instead.
`phase_direction` is deck-only too (the 3.1 deck's ramp to expectation values), and so is
everything under "deck 3.1b" at the bottom (slides/ch03/01b-one-path-or-many.qmd).
From the "deck 3.2" section, page ch03/02 syncs box_bounce, pib_ladder and box_slosh; the page
shows box length, large n and degeneracy with marimo sliders instead, so box_squeeze,
correspondence and degeneracy_split stay deck-only, as do box_fit (ch03/01's trial-energy
slider already makes that point), box_model, box2d_states and all of "deck 3.3".
From the "deck 3.4" section, page ch03/03 syncs barrier_packet, wall_leak, fsw_match, fsw_ladder,
barrier_setup, barrier_width, stm_scan and ammonia_flip; fsw_circle and barrier_mass stay deck-only
(the page's marimo sliders show the graphical solution and the electron/H/D comparison instead), and
so do curvature_signs and curvature_tracer (ch03/01 already teaches the curvature rule on its page)
and barrier_counts (the page defines T in words).
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = "ch03/images"
GIF_DPI = 200    # 2x: an 8 in figure bakes 1600 px wide, crisp full screen (dpi 100 was blurry on projectors, retina)
TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"

REGISTRY = {}


def register(fn):
    REGISTRY[fn.__name__] = fn
    return fn


# ------------------------------------------------------------ free particle: complex wave, flat |Psi|^2
@register
def complex_plane_wave():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    k, w = 2 * np.pi / 4.0, 2 * np.pi            # lambda = 4, one period per loop
    x = np.linspace(0, 12, 600)
    ts = np.linspace(0, 1, 36, endpoint=False)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.0), sharex=True,
                                   gridspec_kw={"height_ratios": [1.25, 1]})
    (re,) = ax1.plot([], [], color=TEAL, lw=2.4, label=r"Re $\Psi = \cos(kx-\omega t)$")
    (im,) = ax1.plot([], [], color=ORANGE, lw=2.0, ls="--", label=r"Im $\Psi = \sin(kx-\omega t)$")
    ax1.axhline(0, color=GRAY, lw=0.6)
    ax1.set_ylim(-1.3, 1.95); ax1.set_yticks([-1, 0, 1]); ax1.set_ylabel(r"$\Psi$")
    ax1.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=2)
    ax1.set_title(r"free particle $\Psi = e^{i(kx-\omega t)}$: two real waves, a quarter cycle apart",
                  loc="left", fontsize=11)

    real2 = ax2.fill_between(x, 0 * x, color=GRAY, alpha=0.25, lw=0)
    (real2_line,) = ax2.plot([], [], color=GRAY, lw=1.4, label=r"a real wave, $\cos^2(kx-\omega t)$: moving dead spots")
    ax2.plot(x, np.ones_like(x), color=CARDINAL, lw=2.8, label=r"$|\Psi|^2 = \mathrm{Re}^2 + \mathrm{Im}^2 = 1$ everywhere")
    ax2.set_xlim(0, 12); ax2.set_ylim(0, 1.75); ax2.set_yticks([0, 1])
    ax2.set_xlabel("x"); ax2.set_ylabel("probability density")
    ax2.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=1)
    fig.tight_layout()

    def update(i):
        ph = k * x - w * ts[i]
        re.set_data(x, np.cos(ph)); im.set_data(x, np.sin(ph))
        real2_line.set_data(x, np.cos(ph) ** 2)
        real2.set_data(x, 0 * x, np.cos(ph) ** 2)

    ani = FuncAnimation(fig, update, frames=len(ts), interval=85, blit=False)
    return fig, ani


# ------------------------------------------------------------ sign of E - V: oscillate vs decay (still)
@register
def allowed_forbidden():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    a, V0, N = 1.2, 30.0, 700                     # half width, depth (units hbar^2/2m = 1)
    x = np.linspace(-3.4, 3.4, N); h = x[1] - x[0]
    V = np.where(np.abs(x) < a, 0.0, V0)
    H = (np.diag(2.0 / h**2 + V) - np.diag(np.ones(N - 1) / h**2, 1)
         - np.diag(np.ones(N - 1) / h**2, -1))
    En, vec = np.linalg.eigh(H)
    n = 3                                         # fourth level: three nodes, long tails
    E, psi = En[n], vec[:, n] / np.abs(vec[:, n]).max()
    psi = psi * np.sign(psi[np.argmax(np.abs(psi))])

    fig, ax = plt.subplots(figsize=(8, 3.4))
    ax.axvspan(-a, a, color=TEAL, alpha=0.08, lw=0)
    ax.axvspan(-3.4, -a, color=CARDINAL, alpha=0.06, lw=0)
    ax.axvspan(a, 3.4, color=CARDINAL, alpha=0.06, lw=0)
    ax.plot(x, V, color="k", lw=2.0)
    ax.axhline(E, color=GRAY, lw=1.2, ls="--")
    ax.plot(x, E + 7.5 * psi, color=TEAL, lw=2.6)
    ax.text(3.35, E + 0.9, "E", color=GRAY, fontsize=11, ha="right")
    ax.text(3.35, V0 + 0.9, "V(x)", color="k", fontsize=11, ha="right")
    ax.text(0, 38.5, r"allowed, $E > V$" + "\n" + r"$\psi$ curves toward the axis: oscillates",
            ha="center", va="top", fontsize=10, color=TEAL)
    for xc in (-2.35, 2.35):
        ax.text(xc, 38.5, r"forbidden, $E < V$" + "\n" + "curves away: decays",
                ha="center", va="top", fontsize=10, color=CARDINAL)
    ax.set_xlim(-3.4, 3.4); ax.set_ylim(-2, 39.5)
    ax.set_xlabel("x"); ax.set_ylabel("energy"); ax.set_yticks([])
    fig.tight_layout()
    fig.savefig(f"{OUT}/allowed_forbidden.png", dpi=200)
    print("wrote", f"{OUT}/allowed_forbidden.png")
    return fig, None


# ------------------------------------------------------------ shooting: only special E give a bounded psi (deck GIF)
@register
def shooting():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4.6, 4.6, 1800); h = x[1] - x[0]
    V = 0.5 * x**2                                # units hbar = m = omega = 1, so E_n = n + 1/2
    levels = [0.5, 1.5, 2.5]
    Es = np.concatenate([np.linspace(0.2, 0.5, 5), [0.5, 0.5], np.linspace(0.5, 1.5, 10)[1:], [1.5, 1.5],
                         np.linspace(1.5, 2.5, 10)[1:], [2.5, 2.5], np.linspace(2.5, 2.8, 4)[1:]])
    psi = np.zeros_like(x)

    def numerov(E):                               # fills psi in place, integrating left to right
        f = 1.0 + h * h * 2.0 * (E - V) / 12.0
        psi[0], psi[1] = 0.0, 1e-8
        for j in range(1, len(x) - 1):
            psi[j + 1] = ((12.0 - 10.0 * f[j]) * psi[j] - f[j - 1] * psi[j - 1]) / f[j + 1]
        psi[:] = psi / np.abs(psi[np.abs(x) < 2.6]).max()

    fig, (ax, axe) = plt.subplots(1, 2, figsize=(8, 3.8), gridspec_kw={"width_ratios": [6, 1], "wspace": 0.12})
    ax.plot(x, V, color="k", lw=1.8)
    ax.text(0, 4.55, r"$V(x) = \frac{1}{2}kx^2$", fontsize=12, ha="center")
    eline = ax.axhline(0.5, color=GRAY, lw=1.1, ls="--")
    (wave,) = ax.plot([], [], lw=2.6)
    ax.set_xlim(-4.6, 4.6); ax.set_ylim(-1.2, 5.2); ax.set_yticks([])
    ax.set_xlabel("x"); ax.set_ylabel(r"energy, with $\psi$ drawn on its level")
    axe.set_xlim(0, 1); axe.set_ylim(-1.2, 5.2); axe.set_xticks([])
    axe.spines["bottom"].set_visible(False)
    axe.set_yticks(levels); axe.set_yticklabels(["1/2", "3/2", "5/2"], fontsize=11)
    axe.set_title("allowed E", fontsize=10.5)
    (marker,) = axe.plot([], [], ">", color=GRAY, ms=9)
    found = [axe.plot([0.25, 0.95], [E0, E0], color=TEAL, lw=3, visible=False)[0] for E0 in levels]
    fig.subplots_adjust(left=0.075, right=0.97, top=0.90, bottom=0.14)

    def update(i):
        E = Es[i]
        numerov(E)
        hit = min(abs(E - E0) for E0 in levels) < 1e-9
        wave.set_data(x, E + 0.85 * np.clip(psi, -9, 9))
        wave.set_color(TEAL if hit else CARDINAL)
        eline.set_ydata([E, E]); marker.set_data([0.1], [E])
        for ln, E0 in zip(found, levels):
            ln.set_visible(E >= E0 - 1e-9)
        ax.set_title(rf"E = {E:.2f} $\hbar\omega$: " + (r"$\psi \to 0$ on both sides, allowed" if hit
                     else r"$\psi$ blows up, not allowed"), loc="left", fontsize=11,
                     color=TEAL if hit else CARDINAL)

    ani = FuncAnimation(fig, update, frames=len(Es), interval=160, blit=False)
    return fig, ani


# ------------------------------------------------------------ stationary state: the phase turns, |Psi|^2 stays
@register
def phase_clock():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 300)
    ts = np.linspace(0, 1, 36, endpoint=False)    # one full turn of the n = 1 clock
    th = np.linspace(0, 2 * np.pi, 200)
    fig = plt.figure(figsize=(8, 4.3))
    gs = fig.add_gridspec(2, 2, width_ratios=[3.4, 1], hspace=0.5, wspace=0.08)
    rows = []
    for r, n in enumerate((1, 2)):
        ax, axc = fig.add_subplot(gs[r, 0]), fig.add_subplot(gs[r, 1])
        psi = np.sqrt(2) * np.sin(n * np.pi * x)
        ax.fill_between(x, psi**2, color=CARDINAL, alpha=0.12, lw=0)
        ax.plot(x, psi**2, color=CARDINAL, lw=1.8, label=r"$|\Psi|^2$ (does not move)")
        (re,) = ax.plot([], [], color=TEAL, lw=2.4, label=r"Re $\Psi$")
        (im,) = ax.plot([], [], color=ORANGE, lw=2.0, ls="--", label=r"Im $\Psi$")
        ax.axhline(0, color=GRAY, lw=0.6)
        ax.set_xlim(0, 1); ax.set_ylim(-1.7, 2.3); ax.set_yticks([-1, 0, 1, 2])
        ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"])
        ax.set_title(rf"$\Psi_{n}(x,t) = \psi_{n}(x)\,e^{{-iE_{n}t/\hbar}}$" + ("" if n == 1 else r",  $E_2 = 4E_1$"),
                     loc="left", fontsize=11)
        if r == 0:
            ax.legend(loc="upper right", frameon=False, fontsize=9, ncol=3, bbox_to_anchor=(1.0, 1.32))
        axc.plot(np.cos(th), np.sin(th), color=GRAY, lw=1, ls="--")
        axc.axhline(0, color=GRAY, lw=0.6); axc.axvline(0, color=GRAY, lw=0.6)
        (hand,) = axc.plot([], [], color=PURPLE, lw=2.8)
        (tip,) = axc.plot([], [], "o", color=PURPLE, ms=7)
        axc.set_aspect("equal"); axc.set_xlim(-1.25, 1.25); axc.set_ylim(-1.25, 1.25); axc.set_axis_off()
        axc.set_title("phase clock" if r == 0 else "4 times faster", fontsize=10, color=PURPLE)
        rows.append((n, psi, re, im, hand, tip))
    fig.subplots_adjust(left=0.06, right=0.99, top=0.86, bottom=0.08)

    def update(i):
        for n, psi, re, im, hand, tip in rows:
            z = np.exp(-2j * np.pi * n**2 * ts[i])
            re.set_data(x, psi * z.real); im.set_data(x, psi * z.imag)
            hand.set_data([0, z.real], [0, z.imag]); tip.set_data([z.real], [z.imag])

    ani = FuncAnimation(fig, update, frames=len(ts), interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ Born rule: detections pile up into |psi|^2
@register
def born_buildup():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(7)
    cand = rng.random(14000)
    hits = cand[rng.random(14000) < np.sin(2 * np.pi * cand) ** 2][:3000]   # samples of 2 sin^2(2 pi x)
    yj = rng.random(3000)
    counts = np.unique(np.round(np.geomspace(1, 3000, 40)).astype(int))
    edges = np.linspace(0, 1, 31); mid = 0.5 * (edges[1:] + edges[:-1]); dx = edges[1] - edges[0]
    xs = np.linspace(0, 1, 300)

    fig, (ax_s, ax_h) = plt.subplots(2, 1, figsize=(8, 4.0), sharex=True,
                                     gridspec_kw={"height_ratios": [1, 2.3]})
    scat = ax_s.scatter([], [], s=5, color=TEAL, alpha=0.6, lw=0)
    ax_s.set_ylim(0, 1); ax_s.set_yticks([])
    for sp in ("left", "bottom"):
        ax_s.spines[sp].set_visible(False)
    ax_s.tick_params(bottom=False)
    bars = ax_h.bar(mid, np.zeros_like(mid), width=0.92 * dx, color=TEAL, alpha=0.5, label="detections per bin")
    (curve,) = ax_h.plot([], [], color=CARDINAL, lw=2.6, label=r"prediction $N\,|\psi(x)|^2\,\Delta x$")
    ax_h.set_xlim(0, 1); ax_h.set_yticks([])
    ax_h.set_xticks([0, 0.5, 1]); ax_h.set_xticklabels(["0", "L/2", "L"])
    ax_h.set_xlabel("position x"); ax_h.set_ylabel("detections")
    ax_h.legend(loc="upper center", frameon=False, fontsize=9.5, ncol=2, bbox_to_anchor=(0.5, 1.17))
    ax_s.set_title("N = 1 detection, one dot each", loc="left", fontsize=11)
    fig.tight_layout()

    def update(i):
        N = counts[i]
        scat.set_offsets(np.column_stack([hits[:N], yj[:N]]))
        hist = np.histogram(hits[:N], bins=edges)[0]
        for b, c in zip(bars, hist):
            b.set_height(c)
        curve.set_data(xs, N * dx * 2 * np.sin(2 * np.pi * xs) ** 2)
        ax_h.set_ylim(0, 1.3 * max(1.0, hist.max(), 2 * N * dx))
        ax_s.set_title(f"N = {N} detection" + ("" if N == 1 else "s") + ", one dot each", loc="left", fontsize=11)

    ani = FuncAnimation(fig, update, frames=len(counts), interval=160, blit=False)
    return fig, ani


# ------------------------------------------------------------ normalization fixes the area (still)
@register
def normalization_area():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 300)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 2.9), sharey=True)
    for ax, c, col, lab, area in ((ax1, 1.0, GRAY, r"$\psi' = x$", "area = 1/3"),
                                  (ax2, 3.0, TEAL, r"$\psi = \sqrt{3}\,x$", "area = 1")):
        ax.fill_between(x, c * x**2, color=col, alpha=0.25, lw=0)
        ax.plot(x, c * x**2, color=col, lw=2.6)
        ax.text(0.06, 2.55, lab, fontsize=12, color=col)
        ax.text(0.80, 0.18 * c + 0.05, area, fontsize=11, ha="center", color="k")
        ax.set_xlim(0, 1); ax.set_ylim(0, 3.1); ax.set_xlabel("x")
    ax1.set_ylabel(r"$|\psi(x)|^2$")
    ax1.set_title("not normalized", loc="left", fontsize=11)
    ax2.set_title("normalized: a probability density", loc="left", fontsize=11)
    fig.tight_layout()
    fig.savefig(f"{OUT}/normalization_area.png", dpi=200)
    print("wrote", f"{OUT}/normalization_area.png")
    return fig, None


# ------------------------------------------------------------ hydrogen 1s: every dot is one measurement (still)
@register
def h1s_cloud():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(11)
    N = 5000
    r = 0.5 * rng.gamma(shape=3.0, scale=1.0, size=N)       # P(r) = 4 r^2 exp(-2r), r in units of a0
    cos_t = 1 - 2 * rng.random(N); phi = 2 * np.pi * rng.random(N)
    xx, zz = r * np.sqrt(1 - cos_t**2) * np.cos(phi), r * cos_t
    rr = np.linspace(0, 6, 300)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5), gridspec_kw={"width_ratios": [1, 1.35]})
    ax1.scatter(xx, zz, s=2, color=TEAL, alpha=0.45, lw=0)
    ax1.plot([0], [0], "+", color=CARDINAL, ms=9, mew=1.8)
    ax1.set_aspect("equal"); ax1.set_xlim(-5, 5); ax1.set_ylim(-5, 5)
    ax1.set_xlabel(r"x / $a_0$"); ax1.set_ylabel(r"z / $a_0$")
    ax1.set_title(f"{N} position measurements", loc="left", fontsize=11)
    ax2.hist(r, bins=np.linspace(0, 6, 49), density=True, color=TEAL, alpha=0.45, label="measured distances")
    ax2.plot(rr, 4 * rr**2 * np.exp(-2 * rr), color=CARDINAL, lw=2.6, label=r"$4\pi r^2\,|\psi_{1s}|^2$")
    ax2.set_xlim(0, 6); ax2.set_xlabel(r"distance from the nucleus r / $a_0$"); ax2.set_ylabel("probability density")
    ax2.legend(frameon=False, fontsize=10)
    ax2.set_title("the dots follow the wavefunction", loc="left", fontsize=11)
    fig.tight_layout()
    fig.savefig(f"{OUT}/h1s_cloud.png", dpi=200)
    print("wrote", f"{OUT}/h1s_cloud.png")
    return fig, None


# ------------------------------------------------------------ mean = balance point, sigma = spread (still)
@register
def mean_and_spread():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 2001)
    fig, axes = plt.subplots(1, 2, figsize=(8, 3.0), sharey=True)
    for ax, p, col, lab in ((axes[0], 3 * x**2, TEAL, r"$|\psi|^2 = 3x^2$"),
                            (axes[1], 2 * np.sin(np.pi * x) ** 2, ORANGE, r"$|\psi_1|^2 = 2\sin^2(\pi x)$")):
        mu = np.trapezoid(x * p, x)
        sig = np.sqrt(np.trapezoid(x**2 * p, x) - mu**2)
        ax.fill_between(x, p, color=col, alpha=0.2, lw=0); ax.plot(x, p, color=col, lw=2.6)
        ax.axvspan(mu - sig, mu + sig, color=PURPLE, alpha=0.12, lw=0)
        ax.axvline(mu, color=PURPLE, lw=1.6)
        ax.plot([mu], [-0.16], marker="^", color=PURPLE, ms=11, clip_on=False, zorder=6)
        ax.set_title(lab + rf":  $\langle x\rangle = {mu:.2f}$,  $\sigma_x = {sig:.2f}$", loc="left", fontsize=10.5)
        ax.set_xlim(0, 1); ax.set_ylim(0, 3.2); ax.set_xlabel("x")
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1]); ax.tick_params(axis="x", pad=9)
    axes[0].set_ylabel("probability density")
    axes[0].text(0.75 - 0.21, 2.75, r"$\pm\sigma_x$", color=PURPLE, fontsize=11, ha="right")
    fig.tight_layout()
    fig.savefig(f"{OUT}/mean_and_spread.png", dpi=200)
    print("wrote", f"{OUT}/mean_and_spread.png")
    return fig, None


# ------------------------------------------------------------ eigenfunction test: same shape or not (still)
@register
def eigen_test():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-3, 3, 500); a = 1.5
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.0))
    ax1.plot(x, np.sin(a * x), color=TEAL, lw=2.6, label=r"$f = \sin(ax)$")
    ax1.plot(x, -a**2 * np.sin(a * x), color=CARDINAL, lw=2.2, ls="--", label=r"$f'' = -a^2 \sin(ax)$")
    ax1.set_title(r"same shape, rescaled: eigenfunction of $d^2/dx^2$", loc="left", fontsize=10.5)
    ax2.plot(x, np.exp(-x**2), color=TEAL, lw=2.6, label=r"$f = e^{-x^2}$")
    ax2.plot(x, (4 * x**2 - 2) * np.exp(-x**2), color=CARDINAL, lw=2.2, ls="--", label=r"$f'' = (4x^2-2)\,e^{-x^2}$")
    ax2.set_title("new shape: not an eigenfunction", loc="left", fontsize=10.5)
    for ax in (ax1, ax2):
        ax.axhline(0, color=GRAY, lw=0.6); ax.set_xlim(-3, 3); ax.set_ylim(-2.6, 3.6); ax.set_xlabel("x")
        ax.legend(loc="upper right", frameon=False, fontsize=9.5)
    fig.tight_layout()
    fig.savefig(f"{OUT}/eigen_test.png", dpi=200)
    print("wrote", f"{OUT}/eigen_test.png")
    return fig, None


# ------------------------------------------------------------ direction lives in the phase, not in |psi|^2 (deck still)
@register
def phase_direction():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4, 4, 1200); k0 = 5.0
    phi = np.exp(-x**2 / 2.4)                     # real envelope, peak 1
    fig, axes = plt.subplots(2, 1, figsize=(7.0, 4.6), sharex=True)
    for ax, s, word in ((axes[0], 1, "moving right"), (axes[1], -1, "moving left")):
        psi = phi * np.exp(1j * s * k0 * x)
        ax.fill_between(x, np.abs(psi) ** 2, color=CARDINAL, alpha=0.15, lw=0)
        ax.plot(x, np.abs(psi) ** 2, color=CARDINAL, lw=2.6, label=r"$|\psi|^2$")
        ax.plot(x, psi.real, color=TEAL, lw=1.8, label=r"Re $\psi$")
        ax.plot(x, psi.imag, color=ORANGE, lw=1.6, ls="--", label=r"Im $\psi$")
        ax.axhline(0, color=GRAY, lw=0.6)
        ax.annotate("", xy=(3.7 * s, 0.75), xytext=(2.5 * s, 0.75),
                    arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.4, mutation_scale=18))
        ax.set_xlim(-4, 4); ax.set_ylim(-1.15, 1.25); ax.set_yticks([])
        ax.set_title(word + (r":  $\psi = \varphi(x)\,e^{+ik_0x}$" if s > 0 else r":  $\psi = \varphi(x)\,e^{-ik_0x}$"),
                     loc="left", fontsize=12)
    axes[0].legend(loc="upper left", frameon=False, fontsize=10.5, ncol=3, bbox_to_anchor=(0.0, 1.02))
    axes[1].set_xlabel("x")
    fig.tight_layout()
    fig.savefig(f"{OUT}/phase_direction.png", dpi=200)
    print("wrote", f"{OUT}/phase_direction.png")
    return fig, None


# ============================================================ deck 3.1b "One path or many" (all deck-only GIFs)
# slides/ch03/01b-one-path-or-many.qmd. Every update() below is a pure function of the frame
# index (state is precomputed), because FuncAnimation calls frame 0 more than once.

# ------------------------------------------------------------ Newton's spring and Hamilton's phase-space point
@register
def hamilton_phase():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    A, n, wall = 1.6, 40, -2.75
    ts = np.linspace(0, 2 * np.pi, n, endpoint=False)          # one period, m = omega = 1
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 5.2), sharex=True,
                                   gridspec_kw={"height_ratios": [1, 2.6], "hspace": 0.34})
    ax1.axvline(wall, color="k", lw=5)
    ax1.axhline(-0.5, color=GRAY, lw=0.8)
    (spring,) = ax1.plot([], [], color=GRAY, lw=1.6)
    (block,) = ax1.fill([0, 0, 0, 0], [0, 0, 0, 0], color=TEAL, alpha=0.9)
    arrow = ax1.annotate("", xy=(0, 0.8), xytext=(0, 0.8),
                         arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=2.4, mutation_scale=18))
    ax1.set_ylim(-0.6, 1.15); ax1.set_yticks([]); ax1.spines["left"].set_visible(False)
    ax1.set_title("Newton: a mass on a spring (arrow = momentum)", loc="left", fontsize=11)
    th = np.linspace(0, 2 * np.pi, 300)
    for r in (0.6, 1.1, 2.1):
        ax2.plot(r * np.cos(th), r * np.sin(th), color=GRAY, lw=0.7, alpha=0.5)
    ax2.plot(A * np.cos(th), A * np.sin(th), color=TEAL, lw=2.0)
    for a0 in (0.25, 0.75, 1.25, 1.75):                         # the point runs clockwise
        x0, y0 = A * np.cos(a0 * np.pi), A * np.sin(a0 * np.pi)
        ax2.annotate("", xy=(x0 + 0.2 * np.sin(a0 * np.pi), y0 - 0.2 * np.cos(a0 * np.pi)), xytext=(x0, y0),
                     arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.6, mutation_scale=14))
    ax2.text(1.25, 1.75, r"$H = E$", color=TEAL, fontsize=12)
    ax2.axhline(0, color=GRAY, lw=0.6)
    (trail,) = ax2.plot([], [], color=CARDINAL, lw=3, alpha=0.45)
    (dot,) = ax2.plot([], [], "o", color=CARDINAL, ms=11, zorder=5)
    g1 = ax1.axvline(0, color=GRAY, lw=1, ls="--")
    g2 = ax2.axvline(0, color=GRAY, lw=1, ls="--")
    ax2.set_xlim(-2.95, 2.9); ax2.set_ylim(-2.3, 2.3)
    ax2.set_xlabel("position x"); ax2.set_ylabel("momentum p")
    ax2.set_title("Hamilton: the same motion as one point (x, p)", loc="left", fontsize=11)
    fig.subplots_adjust(left=0.11, right=0.97, top=0.93, bottom=0.1)
    frac = np.linspace(0, 12, 80) % 1

    def update(i):
        q, p = A * np.cos(ts[i]), -A * np.sin(ts[i])
        ys = 0.22 * (4 * np.abs(frac - 0.5) - 1)
        ys[0] = ys[-1] = 0.0
        spring.set_data(np.linspace(wall, q - 0.26, 80), ys - 0.05)
        block.set_xy([[q - 0.26, -0.5], [q + 0.26, -0.5], [q + 0.26, 0.42], [q - 0.26, 0.42]])
        arrow.xy = (q + 0.55 * p, 0.8); arrow.set_position((q, 0.8)); arrow.set_visible(abs(p) > 0.2)
        k = np.arange(i - 7, i + 1) % n
        trail.set_data(A * np.cos(ts[k]), -A * np.sin(ts[k]))
        dot.set_data([q], [p]); g1.set_xdata([q, q]); g2.set_xdata([q, q])

    ani = FuncAnimation(fig, update, frames=n, interval=80, blit=False)
    return fig, ani


# ------------------------------------------------------------ pendulum phase flow: each point keeps its energy
@register
def phase_flow():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    qg, pg = np.linspace(-np.pi, np.pi, 300), np.linspace(-2.6, 2.6, 300)
    Q, P = np.meshgrid(qg, pg)
    H = 0.5 * P**2 - np.cos(Q)                                  # pendulum, m = g/l = 1
    rng = np.random.default_rng(3)
    n, F, sub, dt = 600, 60, 3, 0.05
    r, a = 0.32 * np.sqrt(rng.random(n)), 2 * np.pi * rng.random(n)
    q, p = r * np.cos(a), 1.55 + r * np.sin(a)
    E = 0.5 * p**2 - np.cos(q)
    Qs, Ps = np.empty((F, n)), np.empty((F, n))
    for f in range(F):                                          # leapfrog keeps the flow symplectic
        Qs[f], Ps[f] = q, p
        for _ in range(sub):
            p = p - 0.5 * dt * np.sin(q); q = q + dt * p; p = p - 0.5 * dt * np.sin(q)

    fig, ax = plt.subplots(figsize=(6.4, 5.0))
    ax.contour(Q, P, H, levels=np.linspace(-0.8, 2.2, 11), colors=GRAY, linewidths=0.7, alpha=0.55)
    ax.contour(Q, P, H, levels=[1.0], colors="k", linewidths=1.0, linestyles="--")
    sc = ax.scatter(Qs[0], Ps[0], c=E, cmap="viridis", s=10, lw=0, zorder=4)
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(-np.pi, np.pi); ax.set_ylim(-2.6, 2.6)
    ax.set_xlabel("angle x"); ax.set_ylabel("momentum p")
    ax.set_title("a pendulum: every point stays on its own energy contour", loc="left", fontsize=11)
    ax.text(0.98, 0.03, "color = energy H", transform=ax.transAxes, ha="right", fontsize=10, color=GRAY)
    fig.tight_layout()

    def update(i):
        sc.set_offsets(np.column_stack([Qs[i], Ps[i]]))

    ani = FuncAnimation(fig, update, frames=F, interval=80, blit=False)
    return fig, ani


# ------------------------------------------------------------ least action: the true path minimizes S
@register
def least_action():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    T, g = 2.0, 1.0
    t = np.linspace(0, T, 400)
    z0, zd0 = 0.5 * g * t * (T - t), g * (T / 2 - t)            # thrown up at A, lands at B
    eta, etad = np.sin(np.pi * t / T), (np.pi / T) * np.cos(np.pi * t / T)
    eg = np.linspace(-0.75, 0.75, 151)
    Sg = np.array([np.trapezoid(0.5 * (zd0 + e * etad) ** 2 - g * (z0 + e * eta), t) for e in eg])
    F = 48
    eps = 0.7 * np.cos(2 * np.pi * np.arange(F) / F) ** 3        # cubed: lingers near the true path

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 5.2), gridspec_kw={"height_ratios": [1.5, 1], "hspace": 0.5})
    for e in np.linspace(-0.7, 0.7, 8):
        ax1.plot(t, z0 + e * eta, color=GRAY, lw=0.8, alpha=0.35)
    ax1.plot(t, z0, color=TEAL, lw=2.4, ls="--", label="true path (Newton)")
    (cur,) = ax1.plot([], [], lw=2.8)
    ax1.plot([0, T], [0, 0], "o", color="k", ms=8, zorder=5)
    ax1.text(0.0, -0.3, "A", fontsize=12, ha="center"); ax1.text(T, -0.3, "B", fontsize=12, ha="center")
    ax1.set_xlim(-0.08, T + 0.08); ax1.set_ylim(-0.4, 1.4)
    ax1.set_xlabel("time t"); ax1.set_ylabel("height z")
    ax1.legend(loc="upper right", frameon=False, fontsize=9.5)
    ax2.plot(eg, Sg, color="k", lw=1.8)
    ax2.axvline(0, color=TEAL, lw=1.2, ls="--")
    (sdot,) = ax2.plot([], [], "o", ms=11, zorder=5)
    ax2.set_xlabel(r"size of the detour $\varepsilon$"); ax2.set_ylabel("action S"); ax2.set_yticks([])
    ax2.set_title("the true path has the smallest action", loc="left", fontsize=11)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.93, bottom=0.1)

    def update(i):
        e = eps[i]
        col = TEAL if abs(e) < 0.03 else CARDINAL
        cur.set_data(t, z0 + e * eta); cur.set_color(col)
        sdot.set_data([e], [np.interp(e, eg, Sg)]); sdot.set_color(col)
        ax1.set_title(rf"a ball thrown up, trial path $\varepsilon$ = {e:+.2f}", loc="left", fontsize=11)

    ani = FuncAnimation(fig, update, frames=F, interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ Feynman: drill more holes, add more screens
@register
def drill_holes():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(5)
    L, per = 10.0, 14
    stages = []
    for xs_, hl, label in (([5.0], [np.array([-1.0, 1.0])], "1 screen, 2 holes: 2 paths (the double slit)"),
                           ([5.0], [np.linspace(-2, 2, 5)], "1 screen, 5 holes: 5 paths"),
                           ([10 / 3, 20 / 3], [np.linspace(-2, 2, 5)] * 2, "2 screens, 5 holes each: 25 paths"),
                           ([2.0, 4.0, 6.0, 8.0], [np.linspace(-2.4, 2.4, 7)] * 4,
                            "4 screens, 7 holes each: 2401 paths")):
        grid = np.array(np.meshgrid(*hl, indexing="ij")).reshape(len(hl), -1).T   # every choice of holes
        if len(grid) > 220:
            grid = grid[rng.choice(len(grid), 220, replace=False)]
        X = np.concatenate([[0.0], xs_, [L]])
        stages.append((xs_, hl, [(X, np.concatenate([[0.0], row, [0.0]])) for row in grid], label))
    s = np.linspace(0, 1, 80)
    free = []
    for _ in range(220):                                         # no screens left: smooth random histories
        a = rng.normal(0, 1.0, 4) / np.arange(1, 5)
        free.append((L * s, 1.2 * sum(a[k] * np.sin((k + 1) * np.pi * s) for k in range(4))))
    stages.append((stages[-1][0], stages[-1][1], free, "drill everywhere, remove the screens: every path from A to B"))

    fig, ax = plt.subplots(figsize=(9, 3.9))

    def update(i):
        si, f = divmod(i, per)
        xs_, hl, paths, label = stages[si]
        last = si == len(stages) - 1
        ax.cla()
        for xsc, holes in zip(xs_, hl):
            edges = np.concatenate([[-3.4], np.repeat(holes, 2) + np.tile([-0.14, 0.14], len(holes)), [3.4]])
            for y0, y1 in edges.reshape(-1, 2):
                ax.plot([xsc, xsc], [y0, y1], color="k", lw=4, alpha=max(0.0, 1 - f / 5) if last else 1.0,
                        solid_capstyle="butt")
        a = min(0.9, 3.2 / np.sqrt(len(paths)))
        for X, Y in paths[:int(np.ceil(len(paths) * min(1.0, (f + 1) / 8)))]:
            ax.plot(X, Y, color=PURPLE if last else TEAL, lw=2.2 if len(paths) < 10 else 0.9, alpha=a)
        ax.plot([0, L], [0, 0], "o", color=CARDINAL, ms=11, zorder=5)
        ax.text(-0.35, 0.0, "A", fontsize=14, ha="right", va="center")
        ax.text(L + 0.35, 0.0, "B", fontsize=14, ha="left", va="center")
        ax.set_xlim(-0.8, L + 0.8); ax.set_ylim(-3.4, 3.4); ax.set_axis_off()
        ax.set_title(label, loc="left", fontsize=13)

    ani = FuncAnimation(fig, update, frames=per * len(stages), interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ many histories at once, each with a phase clock
@register
def ghost_paths():
    from matplotlib.colors import LinearSegmentedColormap
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    cyc = LinearSegmentedColormap.from_list("cyc", [TEAL, PURPLE, CARDINAL, ORANGE, TEAL])
    rng = np.random.default_rng(8)
    n, F, hold = 36, 48, 14
    s = np.linspace(0, 1, 400)
    amp = np.sort(np.abs(rng.normal(0, 0.17, n)))
    wig = np.array([np.sin((k + 1) * np.pi * s) for k in range(3)])
    X, Y = np.empty((n, s.size)), np.empty((n, s.size))
    for j in range(n):
        a, b = rng.normal(0, 1, 3) / np.arange(1, 4), rng.normal(0, 1, 3) / np.arange(1, 4)
        X[j], Y[j] = s + 0.35 * amp[j] * (b @ wig), amp[j] * (a @ wig)
    v2 = np.gradient(X, s, axis=1) ** 2 + np.gradient(Y, s, axis=1) ** 2
    rate = 40 * (v2 - 1)                                         # extra kinetic action per unit time, in hbar
    ph = np.concatenate([np.zeros((n, 1)), np.cumsum(0.5 * (rate[:, 1:] + rate[:, :-1]) * np.diff(s), axis=1)], axis=1)

    fig, ax = plt.subplots(figsize=(7.2, 4.6))

    instep = np.abs(ph[:, -1]) < np.pi / 2                      # arrive within a quarter turn of the classical phase

    def update(i):
        idx = int(round(min(i, F - 1) / (F - 1) * (s.size - 1)))
        done = i >= F
        ax.cla()
        for j in range(n):
            c = cyc((ph[j, idx] % (2 * np.pi)) / (2 * np.pi))
            hi = done and instep[j]
            ax.plot(X[j, :idx + 1], Y[j, :idx + 1], color=c, lw=2.0 if hi else 1.0,
                    alpha=(0.95 if hi else 0.15) if done else 0.45)
            ax.plot(X[j, idx], Y[j, idx], "o", color=c, ms=6.5, alpha=0.95)
        ax.plot([0, s[idx]], [0, 0], color="k", lw=1.2, ls="--", zorder=5)
        ax.plot([s[idx]], [0], "o", color="k", ms=9, zorder=6)
        ax.plot([0, 1], [0, 0], "s", color="k", ms=6, zorder=6)
        ax.text(-0.03, 0.0, "A", fontsize=13, ha="right", va="center")
        ax.text(1.03, 0.0, "B", fontsize=13, ha="left", va="center")
        ax.set_xlim(-0.1, 1.1); ax.set_ylim(-0.8, 0.8); ax.set_axis_off()
        ax.set_title("every history at once, color = its phase clock S/ħ  (dashed: the classical path)",
                     loc="left", fontsize=11)
        if done:
            ax.text(0.5, -0.76, f"bold: the {instep.sum()} histories that arrive in step with the classical one."
                    "\nthe others arrive with every color and cancel", ha="center", fontsize=10.5, color="k")

    ani = FuncAnimation(fig, update, frames=F + hold, interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ add the arrows: the Cornu spiral
@register
def phasor_sum():
    from matplotlib.colors import LinearSegmentedColormap
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    cyc = LinearSegmentedColormap.from_list("cyc", [TEAL, PURPLE, CARDINAL, ORANGE, TEAL])
    N, hold = 61, 14
    y = np.linspace(-1, 1, N)
    th = 3 * np.pi * y**2                                        # extra action of each detour, in hbar
    z = np.exp(1j * th)
    tips = np.concatenate([[0], np.cumsum(z)])
    cols = cyc((th % (2 * np.pi)) / (2 * np.pi))
    pad = 0.8
    lim = (tips.real.min() - pad, tips.real.max() + pad, tips.imag.min() - pad, tips.imag.max() + pad)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 4.4), gridspec_kw={"width_ratios": [1, 1.1]})

    def update(i):
        k = min(i + 1, N)
        done = i >= N
        ax1.cla(); ax2.cla()
        ax1.axvline(0.5, color=GRAY, lw=0.8, ls=":")
        for j in range(k):
            near = th[j] < np.pi
            ax1.plot([0, 0.5, 1], [0, y[j], 0], color=cols[j], lw=2.0 if (done and near) else 1.3,
                     alpha=0.95 if (not done or near) else 0.3)
        ax1.plot([0, 1], [0, 0], "o", color="k", ms=8, zorder=5)
        ax1.text(-0.03, 0, "A", fontsize=13, ha="right", va="center")
        ax1.text(1.03, 0, "B", fontsize=13, ha="left", va="center")
        ax1.set_xlim(-0.12, 1.12); ax1.set_ylim(-1.1, 1.1); ax1.set_axis_off()
        ax1.set_title("paths through one screen, color = phase", loc="left", fontsize=11)
        al = np.where((th[:k] < np.pi) | (not done), 1.0, 0.3)
        c = cols[:k].copy(); c[:, 3] = al
        ax2.quiver(tips[:k].real, tips[:k].imag, z[:k].real, z[:k].imag, color=c,
                   angles="xy", scale_units="xy", scale=1, width=0.007, headwidth=3.5, headlength=4)
        ax2.annotate("", xy=(tips[k].real, tips[k].imag), xytext=(0, 0),
                     arrowprops=dict(arrowstyle="-|>", color="k", lw=2.6, mutation_scale=20))
        ax2.set_xlim(lim[0], lim[1]); ax2.set_ylim(lim[2], lim[3]); ax2.set_aspect("equal"); ax2.set_axis_off()
        ax2.set_title("the total: set by the paths near the straight one" if done
                      else f"add the arrows head to tail ({k} of {N})", loc="left", fontsize=11)

    ani = FuncAnimation(fig, update, frames=N + hold, interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ turn down hbar: the band of agreeing paths shrinks
@register
def hbar_limit():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    hs = np.concatenate([np.full(6, 0.6), np.geomspace(0.6, 0.004, 44), np.full(12, 0.004)])
    Np = 41
    yp, yy = np.linspace(-1, 1, Np), np.linspace(-1, 1, 8000)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 5.2), gridspec_kw={"height_ratios": [1.5, 1], "hspace": 0.5})

    def update(i):
        h = hs[i]
        w = np.sqrt(np.pi * h)                                  # detour action y^2 below pi*hbar: in step
        ax1.cla(); ax2.cla()
        agree = np.abs(yp) < w
        for yj, ok in zip(yp, agree):
            ax1.plot([0, 0.5, 1], [0, yj, 0], color=TEAL if ok else GRAY,
                     lw=1.3 if ok else 0.6, alpha=0.9 if ok else 0.25)
        ax1.plot([0, 1], [0, 0], color="k", lw=2.2)
        ax1.plot([0, 1], [0, 0], "o", color="k", ms=8, zorder=5)
        ax1.set_xlim(-0.05, 1.05); ax1.set_ylim(-1.1, 1.1); ax1.set_axis_off()
        ax1.set_title(rf"$\hbar$ = {h:.3f}:  {agree.sum()} of {Np} paths in step", loc="left", fontsize=12)
        ax2.plot(yy, np.cos(yy**2 / h), color=PURPLE, lw=0.8)
        ax2.axvspan(-min(w, 1), min(w, 1), color=TEAL, alpha=0.15, lw=0)
        ax2.set_xlim(-1, 1); ax2.set_ylim(-1.25, 1.25); ax2.set_yticks([-1, 0, 1])
        ax2.set_xlabel("detour height y"); ax2.set_ylabel(r"cos(S/$\hbar$)")
        ax2.set_title("phase: flat near the straight path, wild far away", loc="left", fontsize=11)
        fig.subplots_adjust(left=0.12, right=0.97, top=0.93, bottom=0.1)

    ani = FuncAnimation(fig, update, frames=hs.size, interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ superposition: adding waves makes a blur
@register
def superposition_blur():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-20, 20, 1500)
    k0, dk, sk = 1.5, 2 * np.pi / 80, 0.2                       # spacing: the sum repeats only every 80
    order = [0] + [m for j in range(1, 8) for m in (j, -j)]
    ks = k0 + dk * np.array(order)
    ck = np.exp(-(ks - k0) ** 2 / (4 * sk**2))
    kk = np.linspace(k0 - 0.7, k0 + 0.7, 200)
    per, hold = 3, 12

    fig = plt.figure(figsize=(7.4, 4.8))
    gs = fig.add_gridspec(2, 2, width_ratios=[3.2, 1], hspace=0.5, wspace=0.28)
    axw, axs, axk = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[:, 1])

    def update(i):
        N = min(len(order), i // per + 1)
        axw.cla(); axs.cla(); axk.cla()
        for j in range(N):
            new = j == N - 1
            axw.plot(x, ck[j] * np.cos(ks[j] * x), color=ORANGE if new else GRAY,
                     lw=1.6 if new else 0.7, alpha=1.0 if new else 0.4)
        axw.set_xlim(-20, 20); axw.set_ylim(-1.2, 1.2); axw.set_yticks([])
        axw.set_title(f"{N} wave{'s' if N > 1 else ''} with definite momentum", loc="left", fontsize=11)
        psi = (ck[:N, None] * np.exp(1j * ks[:N, None] * x)).sum(0)
        psi = psi / np.abs(psi).max()
        axs.fill_between(x, np.abs(psi) ** 2, color=CARDINAL, alpha=0.18, lw=0)
        axs.plot(x, np.abs(psi) ** 2, color=CARDINAL, lw=2.2, label=r"$|\psi|^2$")
        axs.plot(x, psi.real, color=TEAL, lw=1.1, label=r"Re $\psi$")
        axs.set_xlim(-20, 20); axs.set_ylim(-1.1, 1.3); axs.set_yticks([]); axs.set_xlabel("x")
        axs.legend(loc="upper right", frameon=False, fontsize=9, ncol=2)
        axs.set_title("one wave: found anywhere" if N == 1 else "their sum: localized in x",
                      loc="left", fontsize=11)
        axk.plot(np.exp(-(kk - k0) ** 2 / (2 * sk**2)), kk, color=GRAY, lw=1, ls="--")
        axk.barh(ks[:N], ck[:N] ** 2, height=0.8 * dk, color=TEAL)
        axk.set_ylim(kk[0], kk[-1]); axk.set_xlim(0, 1.1); axk.set_xticks([]); axk.set_yticks([])
        axk.set_ylabel("momentum p"); axk.set_title("spread in p", fontsize=11)

    ani = FuncAnimation(fig, update, frames=per * len(order) + hold, interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ a point becomes a blur (coherent state)
@register
def point_vs_blur():
    from matplotlib.colors import LinearSegmentedColormap
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    wt = LinearSegmentedColormap.from_list("wt", ["white", TEAL])
    A, hb, n = 2.0, 0.3, 40                                     # m = omega = 1, a visible hbar
    sig = np.sqrt(hb / 2)
    ts = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = np.linspace(-3.4, 3.4, 500)
    Q, P = np.meshgrid(np.linspace(-3.4, 3.4, 170), np.linspace(-3.0, 3.0, 150))
    th = np.linspace(0, 2 * np.pi, 300)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 5.4), sharex=True,
                                   gridspec_kw={"height_ratios": [1, 2.1], "hspace": 0.32})

    def update(i):
        qc, pc = A * np.cos(ts[i]), -A * np.sin(ts[i])
        ax1.cla(); ax2.cla()
        ax1.plot(x, 0.1 * x**2, color=GRAY, lw=1.0)
        rho = np.exp(-(x - qc) ** 2 / (2 * sig**2))
        ax1.fill_between(x, rho, color=TEAL, alpha=0.3, lw=0)
        ax1.plot(x, rho, color=TEAL, lw=2.2, label=r"quantum: $|\psi|^2$")
        ax1.plot([qc], [0.06], "o", color="k", ms=8, zorder=5, label="classical: a point")
        ax1.set_ylim(0, 1.35); ax1.set_yticks([])
        ax1.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=2)
        ax1.set_title("position", loc="left", fontsize=11)
        W = np.exp(-((Q - qc) ** 2 + (P - pc) ** 2) / (2 * sig**2))
        ax2.contourf(Q, P, W, levels=[0.08, 0.25, 0.45, 0.65, 0.85, 1.01], cmap=wt, vmin=-0.1, vmax=1.0)
        ax2.plot(A * np.cos(th), A * np.sin(th), color=GRAY, lw=1.0, ls="--")
        ax2.plot([qc], [pc], "o", color="k", ms=8, zorder=5)
        ax2.axhline(0, color=GRAY, lw=0.5); ax2.axvline(0, color=GRAY, lw=0.5)
        ax2.set_xlim(-3.4, 3.4); ax2.set_ylim(-3.0, 3.0)
        ax2.set_xlabel("position x"); ax2.set_ylabel("momentum p")
        ax2.set_title(r"phase space: a point, or a blob of area $\sim\hbar$ riding the same orbit",
                      loc="left", fontsize=11)
        fig.subplots_adjust(left=0.11, right=0.97, top=0.94, bottom=0.1)

    ani = FuncAnimation(fig, update, frames=n, interval=90, blit=False)
    return fig, ani


# ============================================================ deck 3.2 "Particle in a box" (deck GIFs and stills)
# slides/ch03/02-particle-in-a-box.qmd. Box units: L = 1, energies in units of E1 = h^2/8mL^2.
# As in 3.1b, every update() is a pure function of the frame index.

# ------------------------------------------------------------ classical vs quantum: where do we catch it?
@register
def box_bounce():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(5)
    xc = rng.random(4000)                                       # classical: snapshots at random times
    cand = rng.random(16000)
    xq = cand[rng.random(16000) < np.sin(3 * np.pi * cand) ** 2][:4000]   # quantum: samples of |psi_3|^2
    yj = rng.random(4000)
    counts = np.unique(np.round(np.geomspace(1, 4000, 44)).astype(int))
    counts = np.concatenate([counts, np.full(8, counts[-1])])
    edges = np.linspace(0, 1, 31); mid = 0.5 * (edges[1:] + edges[:-1]); dx = edges[1] - edges[0]
    xs = np.linspace(0, 1, 300)
    fig, axes = plt.subplots(2, 2, figsize=(8, 3.9), sharex=True,
                             gridspec_kw={"height_ratios": [1, 2.2], "hspace": 0.12, "wspace": 0.1})
    (ta, tb), (ha, hb) = axes
    for ax in (ta, tb):
        ax.axvline(0, color="k", lw=3); ax.axvline(1, color="k", lw=3)
        ax.set_ylim(0, 1); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.tick_params(bottom=False)
    ta.set_title("classical: a ball bouncing at constant speed", loc="left", fontsize=10.5)
    tb.set_title(r"quantum, $n = 3$: each dot is one detection", loc="left", fontsize=10.5)
    (trail,) = ta.plot([], [], "o", color=ORANGE, ms=9, alpha=0.25)
    (ball,) = ta.plot([], [], "o", color=ORANGE, ms=12)
    scat = tb.scatter([], [], s=5, color=TEAL, alpha=0.6, lw=0)
    bars_c = ha.bar(mid, 0 * mid, width=0.92 * dx, color=ORANGE, alpha=0.5)
    bars_q = hb.bar(mid, 0 * mid, width=0.92 * dx, color=TEAL, alpha=0.5)
    (pc,) = ha.plot([], [], color=GRAY, lw=2.4, ls="--", label=r"flat: $1/L$")
    (pq,) = hb.plot([], [], color=CARDINAL, lw=2.4, label=r"$|\psi_3(x)|^2$")
    for ax in (ha, hb):
        ax.set_xlim(-0.02, 1.02); ax.set_yticks([])
        ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("position x")
        ax.legend(loc="upper right", frameon=False, fontsize=9.5)
    ha.set_ylabel("times caught here")
    fig.subplots_adjust(left=0.05, right=0.99, top=0.84, bottom=0.13)
    sup = fig.suptitle("", fontsize=11.5)
    tri = lambda s: 0.04 + 0.92 * (1 - np.abs(2 * (s % 1) - 1))  # bounce between the walls

    def update(i):
        N = counts[i]
        pos = tri(np.arange(i - 3, i + 1) / 11.0)
        trail.set_data(pos[:-1], np.full(3, 0.5)); ball.set_data(pos[-1:], [0.5])
        scat.set_offsets(np.column_stack([xq[:N], yj[:N]]))
        hc = np.histogram(xc[:N], bins=edges)[0]; hq = np.histogram(xq[:N], bins=edges)[0]
        for b, c in zip(bars_c, hc):
            b.set_height(c)
        for b, c in zip(bars_q, hq):
            b.set_height(c)
        pc.set_data(xs, np.full_like(xs, N * dx)); pq.set_data(xs, N * dx * 2 * np.sin(3 * np.pi * xs) ** 2)
        top = 1.3 * max(1.0, hc.max(), hq.max(), 2 * N * dx)
        ha.set_ylim(0, top); hb.set_ylim(0, top)
        sup.set_text(f"N = {N} position measurement" + ("" if N == 1 else "s"))

    ani = FuncAnimation(fig, update, frames=len(counts), interval=150, blit=False)
    return fig, ani


# ------------------------------------------------------------ the model: flat floor, infinite walls (still)
@register
def box_model():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 300)
    fig, ax = plt.subplots(figsize=(5.0, 3.5))
    for x0, x1 in ((-0.38, 0), (1, 1.38)):
        ax.axvspan(x0, x1, color=GRAY, alpha=0.18, lw=0)
    ax.plot([0, 0, 1, 1], [1.15, 0, 0, 1.15], color="k", lw=3)
    ax.text(-0.19, 0.55, r"$V = \infty$", ha="center", fontsize=13)
    ax.text(1.19, 0.55, r"$V = \infty$", ha="center", fontsize=13)
    ax.text(0.5, 0.06, r"$V = 0$", ha="center", fontsize=13)
    ax.plot(x, 0.3 + 0.42 * np.sin(np.pi * x), color=TEAL, lw=2.6)
    ax.axhline(0.3, xmin=0.275, xmax=0.725, color=GRAY, lw=0.8, ls="--")
    ax.plot([0, 1], [0.3, 0.3], "o", color=CARDINAL, ms=9, zorder=5)
    ax.text(0.5, 0.8, r"$\psi(0) = \psi(L) = 0$", ha="center", fontsize=12, color=CARDINAL)
    ax.set_xlim(-0.38, 1.38); ax.set_ylim(-0.02, 1.15)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "L"], fontsize=12); ax.set_yticks([])
    ax.spines["left"].set_visible(False); ax.set_xlabel("x", fontsize=12)
    fig.tight_layout()
    fig.savefig(f"{OUT}/box_model.png", dpi=200)
    print("wrote", f"{OUT}/box_model.png")
    return fig, None


# ------------------------------------------------------------ only whole half-waves fit: raise E, each fit adds a rung
@register
def box_fit():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 400)
    up = lambda a, b, k: np.linspace(a, b, k + 1)[1:]
    es = np.concatenate([np.linspace(0.3, 1, 10), np.full(18, 1.0), up(1, 4, 16), np.full(18, 4.0),
                         up(4, 9, 18), np.full(18, 9.0), up(9, 10.6, 8), np.full(24, 10.6)])
    fig, (ax, axe) = plt.subplots(1, 2, figsize=(8, 3.8), gridspec_kw={"width_ratios": [2.3, 1], "wspace": 0.1})
    ax.plot([0, 0], [-1.3, 1.3], color="k", lw=3); ax.plot([1, 1], [-1.3, 1.3], color="k", lw=3)
    ax.axhline(0, color=GRAY, lw=0.8, ls="--")
    (wave,) = ax.plot([], [], lw=2.8)
    (miss,) = ax.plot([], [], color=CARDINAL, lw=5, solid_capstyle="butt")
    ax.plot([0], [0], "o", color=TEAL, ms=9, zorder=5)               # psi(0) = 0 holds for every E
    (right,) = ax.plot([], [], "o", ms=11, zorder=5)
    ax.set_xlim(-0.03, 1.06); ax.set_ylim(-1.3, 1.3); ax.set_yticks([])
    ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "L"], fontsize=13); ax.set_xlabel("x", fontsize=13)
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
    rungs = []
    for n in (1, 2, 3):
        rungs.append((n * n, axe.hlines(n * n, 0, 0.3, color=TEAL, lw=3.5),
                      axe.text(0.38, n * n, rf"$n = {n}$,  " + (r"$E_1$" if n == 1 else rf"${n * n}E_1$"),
                               va="center", fontsize=13, color=TEAL)))
    (now,) = axe.plot([], [], lw=5, solid_capstyle="butt")
    axe.set_xlim(0, 1); axe.set_ylim(0, 11.3); axe.set_xticks([]); axe.set_yticks([])
    axe.spines["bottom"].set_visible(False); axe.set_ylabel("energy", fontsize=13)
    axe.set_title("allowed energies", loc="left", fontsize=13, color=TEAL)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.15)

    def update(i):
        e = es[i]; r = np.sqrt(e); n = round(r)
        fit = abs(r - n) < 1e-9
        end = np.sin(np.pi * r)                                     # psi(L) for psi = sin kx, kL = pi sqrt(E/E1)
        wave.set_data(x, np.sin(np.pi * r * x)); wave.set_color(TEAL if fit else ORANGE)
        miss.set_data([1.03, 1.03], [0, end]); miss.set_visible(not fit)
        right.set_data([1], [end]); right.set_color(TEAL if fit else CARDINAL)
        now.set_data([0, 0.3], [e, e]); now.set_color(TEAL if fit else ORANGE)
        for E, rung, lb in rungs:
            rung.set_visible(e >= E - 1e-9); lb.set_visible(e >= E - 1e-9)
        if fit:
            ax.set_title((r"$E = E_1$" if n == 1 else rf"$E = {n * n}E_1$") + f":  {n} half-wave" + ("s fit" if n > 1 else " fits")
                         + r", $\psi(L) = 0$", loc="left", fontsize=14, color=TEAL)
        else:
            ax.set_title(rf"$E = {e:.2f}\,E_1$:  {r:.2f} half-waves, $\psi(L) \neq 0$", loc="left", fontsize=14, color=CARDINAL)

    ani = FuncAnimation(fig, update, frames=len(es), interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ the ladder: psi_n and |psi_n|^2 on their levels (still)
@register
def pib_ladder():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 400)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.4), sharey=True, gridspec_kw={"wspace": 0.08})
    for ax in (ax1, ax2):
        ax.plot([0, 0, 1, 1], [18.3, 0, 0, 18.3], color="k", lw=2.6)
        ax.set_xlim(-0.04, 1.04); ax.set_ylim(-0.4, 18.3)
        ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("x")
        ax.spines["left"].set_visible(False)
    for n in range(1, 5):
        E, s = n * n, np.sin(n * np.pi * x)
        for ax in (ax1, ax2):
            ax.hlines(E, 0, 1, color=GRAY, lw=0.8, ls="--")
        ax1.plot(x, E + 1.25 * s, color=TEAL, lw=2.4)
        ax2.fill_between(x, E, E + 1.6 * s**2, color=CARDINAL, alpha=0.18, lw=0)
        ax2.plot(x, E + 1.6 * s**2, color=CARDINAL, lw=2.2)
        ax2.plot(np.arange(1, n) / n, np.full(n - 1, E), "o", color="k", ms=5, zorder=5)
        ax2.text(1.06, E, rf"$n = {n}$,  " + (r"$E_1$" if n == 1 else rf"${E}E_1$"), va="center", fontsize=11.5)
    ax1.set_yticks([]); ax1.set_ylabel("energy")
    ax1.set_title(r"$\psi_n(x)$, drawn on its level $E_n$", loc="left", fontsize=11)
    ax2.set_title(r"$|\psi_n(x)|^2$: dots mark the $n-1$ nodes", loc="left", fontsize=11)
    fig.subplots_adjust(left=0.05, right=0.83, top=0.92, bottom=0.12)
    fig.savefig(f"{OUT}/pib_ladder.png", dpi=200)
    print("wrote", f"{OUT}/pib_ladder.png")
    return fig, None


# ------------------------------------------------------------ squeeze the box: every level rises as 1/L^2
@register
def box_squeeze():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    nf = 44
    Ls = 0.775 + 0.225 * np.cos(2 * np.pi * np.arange(nf) / nf)        # L0 -> 0.55 L0 -> L0
    Lg = np.linspace(0.5, 1.05, 200)
    fig, (ax, axl) = plt.subplots(1, 2, figsize=(8, 3.7), gridspec_kw={"width_ratios": [1.55, 1], "wspace": 0.32})

    def update(i):
        L = Ls[i]; xl, xr = -L / 2, L / 2
        x = np.linspace(xl, xr, 300)
        ax.cla(); axl.cla()
        ax.plot([xl, xl, xr, xr], [34, 0, 0, 34], color="k", lw=2.6)
        for n, col in zip((1, 2, 3), (TEAL, ORANGE, PURPLE)):
            E = n * n / L**2
            ax.hlines(E, xl, xr, color=col, lw=0.9, ls="--")
            ax.plot(x, E + 1.3 * np.sin(n * np.pi * (x - xl) / L), color=col, lw=2.4)
            ax.text(0.58, E, rf"$E_{n} = {E:.1f}$", color=col, va="center", fontsize=11)
        ax.set_xlim(-0.6, 0.98); ax.set_ylim(-0.6, 33); ax.set_xticks([]); ax.set_yticks([])
        ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
        ax.set_title(rf"box length $L = {L:.2f}\,L_0$  (energies in units of $E_1$ at $L_0$)", loc="left", fontsize=10.5)
        axl.plot(Lg, 1 / Lg**2, color=TEAL, lw=2.2)
        axl.plot([L], [1 / L**2], "o", color=TEAL, ms=10)
        axl.set_xlim(0.5, 1.05); axl.set_ylim(0, 4.2)
        axl.set_xlabel(r"$L / L_0$"); axl.set_ylabel(r"$E_1$")
        axl.set_title(r"$E_1 = h^2/8mL^2$: never zero", loc="left", fontsize=10.5)
        fig.subplots_adjust(left=0.03, right=0.97, top=0.9, bottom=0.14)

    ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ large n: the lobes wash out into the classical 1/L
@register
def correspondence():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    ns = [1, 2, 3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 30, 40, 50]
    frames = [n for n in ns for _ in range(5)] + [ns[-1]] * 6
    x = np.linspace(0, 1, 3000)
    fig, ax = plt.subplots(figsize=(8, 3.2))

    def update(i):
        n = frames[i]
        P = 1 / 3 + (np.sin(2 * n * np.pi / 3) - np.sin(4 * n * np.pi / 3)) / (2 * n * np.pi)
        p = 2 * np.sin(n * np.pi * x) ** 2
        ax.cla()
        ax.axvspan(1 / 3, 2 / 3, color=PURPLE, alpha=0.09, lw=0)
        ax.fill_between(x, p, color=CARDINAL, alpha=0.2, lw=0)
        ax.plot(x, p, color=CARDINAL, lw=1.4 if n < 12 else 0.8, label=r"$|\psi_n|^2$")
        ax.axhline(1, color="k", lw=2.2, ls="--", label=r"classical: $1/L$")
        ax.plot([0, 0, 1, 1], [2.6, 0, 0, 2.6], color="k", lw=2.6)
        ax.set_xlim(-0.02, 1.02); ax.set_ylim(0, 2.6); ax.set_yticks([0, 1, 2]); ax.set_yticklabels(["0", "1/L", "2/L"])
        ax.set_xticks([0, 1 / 3, 2 / 3, 1]); ax.set_xticklabels(["0", "L/3", "2L/3", "L"]); ax.set_xlabel("x")
        ax.legend(loc="upper right", frameon=False, fontsize=10, ncol=2, bbox_to_anchor=(1.0, 1.16))
        ax.set_title(rf"$n = {n}$:   P(middle third) = {P:.3f}   (classical: 0.333)", loc="left", fontsize=12, color=PURPLE)
        fig.subplots_adjust(left=0.07, right=0.98, top=0.86, bottom=0.17)

    ani = FuncAnimation(fig, update, frames=len(frames), interval=120, blit=False)
    return fig, ani


# ------------------------------------------------------------ superposition of n = 1 and n = 2: the cross term sloshes the density
@register
def box_slosh():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 400)
    p1, p2 = np.sqrt(2) * np.sin(np.pi * x), np.sqrt(2) * np.sin(2 * np.pi * x)
    fixed, cross = 0.5 * (p1**2 + p2**2), p1 * p2               # |Psi|^2 = fixed + cross cos(wt): even + odd about L/2
    nf = 60
    ts = np.linspace(0, 2 * np.pi, nf, endpoint=False)          # E1 = 1, E2 = 4, hbar = 1: w = 3, three sloshes
    xbar = lambda t: 0.5 - 16 / (9 * np.pi**2) * np.cos(3 * t)  # <x>(t) = L/2 + x12 cos(wt), x12 = -16L/9pi^2
    th = np.linspace(0, 2 * np.pi, 200)
    fig = plt.figure(figsize=(7.2, 3.4))
    gs = fig.add_gridspec(2, 2, width_ratios=[2.3, 1], height_ratios=[2, 1], hspace=0.42, wspace=0.08)
    ax, axx = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[1, 0])
    axc, axl = fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])
    ax.plot(x, fixed, color=GRAY, lw=1.8, ls="--", label=r"$\frac{1}{2}(\psi_1^2 + \psi_2^2)$")
    (dens,) = ax.plot([], [], color=CARDINAL, lw=2.8, label=r"$|\Psi|^2$")
    band = [ax.fill_between(x, 0 * x, color=CARDINAL, alpha=0.18, lw=0)]
    (mark,) = ax.plot([], [], marker="^", color=PURPLE, ms=14, zorder=6, ls="none", label=r"$\langle x\rangle$")
    ax.plot([0, 0, 1, 1], [3.35, 0, 0, 3.35], color="k", lw=2.6)          # peak of |Psi|^2 is 3.10
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(0, 3.35); ax.set_xticks([]); ax.set_yticks([])
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
    ax.legend(loc="lower left", bbox_to_anchor=(0, 0.97), ncol=3, frameon=False, fontsize=13,
              handlelength=1.6, columnspacing=1.4)
    axx.axhline(0, color=GRAY, lw=0.8)
    (crs,) = axx.plot([], [], color=PURPLE, lw=2.6)
    cband = [axx.fill_between(x, 0 * x, color=PURPLE, alpha=0.18, lw=0)]
    axx.set_xlim(-0.02, 1.02); axx.set_ylim(-1.7, 1.7); axx.set_yticks([])
    axx.set_xticks([0, 0.5, 1]); axx.set_xticklabels(["0", "L/2", "L"], fontsize=13)
    axx.spines["left"].set_visible(False)
    axx.set_title(r"cross term $\psi_1\psi_2\cos\omega t$", loc="left", fontsize=13, color=PURPLE)
    for a in (ax, axx):
        a.axvline(0.5, color=GRAY, lw=0.8, ls=":")
    axc.plot(np.cos(th), np.sin(th), color=GRAY, lw=1, ls="--")
    (arc,) = axc.plot([], [], color=PURPLE, lw=3.2, label=r"$\omega t$")
    (h1,) = axc.plot([], [], color=TEAL, lw=3.2, label=r"$E_1$")
    (h2,) = axc.plot([], [], color=ORANGE, lw=3.2, label=r"$E_2 = 4E_1$")
    axc.set_aspect("equal"); axc.set_xlim(-1.15, 1.15); axc.set_ylim(-1.15, 1.15); axc.set_axis_off()
    axc.set_title("phase clocks", fontsize=13)
    axl.set_axis_off()
    axl.legend(handles=[h1, h2, arc], loc="center", frameon=False, fontsize=13, handlelength=1.2)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.87, bottom=0.1)

    def update(i):
        t = ts[i]
        c = cross * np.cos(3 * t)
        dens.set_data(x, fixed + c)
        band[0].remove(); band[0] = ax.fill_between(x, fixed + c, color=CARDINAL, alpha=0.18, lw=0)
        mark.set_data([xbar(t)], [0.14])
        crs.set_data(x, c)
        cband[0].remove(); cband[0] = axx.fill_between(x, c, color=PURPLE, alpha=0.18, lw=0)
        a1, a2 = -t, -4 * t                                     # clock hands: e^{-iE1 t}, e^{-iE2 t}
        d = (a1 - a2) % (2 * np.pi)                             # angle between the hands, w t
        s = np.linspace(a2, a2 + d, 40) if d <= np.pi else np.linspace(a1, a1 + 2 * np.pi - d, 40)
        arc.set_data(0.42 * np.cos(s), 0.42 * np.sin(s))
        h1.set_data([0, np.cos(a1)], [0, np.sin(a1)]); h2.set_data([0, np.cos(a2)], [0, np.sin(a2)])

    ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ 2D box: products of 1D waves (still)
@register
def box2d_states():
    from matplotlib.colors import LinearSegmentedColormap
    cm = LinearSegmentedColormap.from_list("ct", [CARDINAL, "white", TEAL])
    g = np.linspace(0, 1, 160)
    X, Y = np.meshgrid(g, g)
    fig, axes = plt.subplots(2, 2, figsize=(5.0, 5.2))
    for ax, (nx, ny) in zip(axes.flat, [(1, 1), (2, 2), (2, 1), (1, 2)]):
        ax.contourf(X, Y, np.sin(nx * np.pi * X) * np.sin(ny * np.pi * Y), levels=np.linspace(-1, 1, 15), cmap=cm)
        for j in range(1, nx):
            ax.axvline(j / nx, color="k", lw=1.2, ls="--")
        for j in range(1, ny):
            ax.axhline(j / ny, color="k", lw=1.2, ls="--")
        ax.set_aspect("equal"); ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(True); sp.set_linewidth(2.4)
        deg = (nx, ny) in ((2, 1), (1, 2))
        ax.set_title(rf"$({nx},{ny})$:  $E = {nx * nx + ny * ny}\,E_0$", fontsize=12,
                     color=PURPLE if deg else "k")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.93, bottom=0.02, wspace=0.12, hspace=0.22)
    fig.savefig(f"{OUT}/box2d_states.png", dpi=200)
    print("wrote", f"{OUT}/box2d_states.png")
    return fig, None


# ------------------------------------------------------------ break the square's symmetry: the (2,1)/(1,2) level splits
@register
def degeneracy_split():
    from matplotlib.colors import LinearSegmentedColormap
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    cm = LinearSegmentedColormap.from_list("ct", [CARDINAL, "white", TEAL])
    nf = 40
    bs = 1.25 - 0.25 * np.cos(2 * np.pi * np.arange(nf) / nf)          # b/a: 1 -> 1.5 -> 1
    u = np.linspace(0, 1, 90)
    U, W = np.meshgrid(u, u)
    fig = plt.figure(figsize=(8, 3.6))
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.35], wspace=0.15)
    a1, a2, al = fig.add_subplot(gs[0]), fig.add_subplot(gs[1]), fig.add_subplot(gs[2])

    def update(i):
        b = bs[i]
        for ax, (nx, ny), col in ((a1, (2, 1), TEAL), (a2, (1, 2), ORANGE)):
            ax.cla()
            ax.contourf(U, b * W, np.sin(nx * np.pi * U) * np.sin(ny * np.pi * W), levels=np.linspace(-1, 1, 15), cmap=cm)
            ax.plot([0, 1, 1, 0, 0], [0, 0, b, b, 0], color="k", lw=2.4)
            ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.05, 1.55); ax.set_aspect("equal"); ax.set_axis_off()
            ax.set_title(f"({nx},{ny})", fontsize=12, color=col)
        al.cla()
        E11, E21, E12 = 1 + 1 / b**2, 4 + 1 / b**2, 1 + 4 / b**2
        al.hlines(E11, 0, 1, color=GRAY, lw=3); al.text(1.08, E11, "(1,1)", va="center", fontsize=11, color=GRAY)
        al.hlines(E21, 0, 1, color=TEAL, lw=3); al.hlines(E12, 0, 1, color=ORANGE, lw=3)
        if E21 - E12 < 0.35:
            al.text(1.08, E21, "(2,1) and (1,2)", va="center", fontsize=11, color=PURPLE)
        else:
            al.text(1.08, E21, "(2,1)", va="center", fontsize=11, color=TEAL)
            al.text(1.08, E12, "(1,2)", va="center", fontsize=11, color=ORANGE)
        al.set_xlim(-0.1, 2.3); al.set_ylim(0, 5.6); al.set_xticks([]); al.set_yticks([])
        al.spines["bottom"].set_visible(False); al.set_ylabel("energy")
        al.set_title("square: degenerate" if b < 1.02 else f"stretched, b = {b:.2f}a: split",
                     loc="left", fontsize=11.5, color=PURPLE if b < 1.02 else "k")
        fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.04)

    ani = FuncAnimation(fig, update, frames=nf, interval=110, blit=False)
    return fig, ani


# ============================================================ deck 3.3 "Applications of the particle in a box"
# slides/ch03/03-applications-of-particle-in-a-box.qmd. Polyene model: C=C 1.35 A, C-C 1.54 A, and the
# box runs one carbon radius (0.77 A) past each end carbon, so L = 1.445 N A for N carbons.

# ------------------------------------------------------------ butadiene: pi electrons spread over a box (still)
@register
def polyene_box():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    xs = np.array([0.0, 1.35, 2.89, 4.24])                      # carbons, spaced by bond length along the chain (A)
    ys = np.array([0.0, 0.7, 0.0, 0.7]) + 2.35
    x = np.linspace(-0.77, 5.01, 400); L = 5.78
    s = (x + 0.77) / L
    rho = 2 * (2 / L) * np.sin(np.pi * s) ** 2 + 2 * (2 / L) * np.sin(2 * np.pi * s) ** 2
    fig, ax = plt.subplots(figsize=(7.6, 3.8))
    for j, lab in zip(range(3), ("1.35 Å", "1.54 Å", "1.35 Å")):
        d = np.array([xs[j + 1] - xs[j], ys[j + 1] - ys[j]]); nrm = np.array([-d[1], d[0]]) / np.hypot(*d)
        ax.plot(xs[j:j + 2], ys[j:j + 2], color="k", lw=2.4)
        up = 1 if j == 1 else -1                                # label on the outside of the zigzag
        if j != 1:                                              # C=C: an inner second line, shortened
            a = np.array([xs[j], ys[j]]) + 0.18 * d - 0.16 * nrm * (1 if j == 0 else 1)
            b = np.array([xs[j + 1], ys[j + 1]]) - 0.18 * d - 0.16 * nrm
            ax.plot([a[0], b[0]], [a[1], b[1]], color="k", lw=2.4)
        mid = 0.5 * np.array([xs[j] + xs[j + 1], ys[j] + ys[j + 1]]) + 0.32 * nrm * (1 if j != 1 else -1)
        ax.text(mid[0], mid[1], lab, ha="center", va="center", fontsize=10.5)
    ax.plot(xs, ys, "o", color="k", ms=15, zorder=5)
    for xj, yj in zip(xs, ys):
        ax.text(xj, yj, "C", color="white", ha="center", va="center", fontsize=9, fontweight="bold", zorder=6)
    ax.plot([-0.77, -0.77, 5.01, 5.01], [1.9, 0, 0, 1.9], color="k", lw=2.6)
    for xe in (0.0, 4.24):
        ax.plot([xe, xe], [0, 2.2], color=GRAY, lw=1, ls=":")
    ax.fill_between(x, 1.3 * rho, color=TEAL, alpha=0.25, lw=0)
    ax.plot(x, 1.3 * rho, color=TEAL, lw=2.4)
    ax.text(5.25, 0.75, r"$\pi$ electron density" + "\n" + r"$2|\psi_1|^2 + 2|\psi_2|^2$", fontsize=11, color=TEAL, va="center")
    ax.text(-0.39, 1.72, "0.77 Å", ha="center", fontsize=9, color=GRAY)
    ax.text(4.62, 1.72, "0.77 Å", ha="center", fontsize=9, color=GRAY)
    ax.annotate("", xy=(-0.77, -0.3), xytext=(5.01, -0.3), arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.8))
    ax.text(2.12, -0.62, "L = 1.35 + 1.54 + 1.35 + 2(0.77) = 5.78 Å", ha="center", va="top", fontsize=11.5, color=CARDINAL)
    ax.set_xlim(-1.0, 7.6); ax.set_ylim(-1.05, 3.45); ax.set_axis_off()
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(f"{OUT}/polyene_box.png", dpi=200)
    print("wrote", f"{OUT}/polyene_box.png")
    return fig, None


# ------------------------------------------------------------ fill two per level: HOMO -> LUMO (still)
@register
def homo_lumo():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    for n in range(1, 5):
        E = n * n
        ax.hlines(E, 0, 1, color="k" if n <= 2 else GRAY, lw=2.6)
        ax.text(1.08, E, f"n = {n}" + ("   HOMO" if n == 2 else "   LUMO" if n == 3 else ""), va="center", fontsize=11.5,
                color=TEAL if n == 2 else CARDINAL if n == 3 else "k")
        if n <= 2:
            for xa, d in ((0.36, 1), (0.64, -1)):
                ax.annotate("", xy=(xa, E + 0.75 * d), xytext=(xa, E - 0.75 * d),
                            arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2, mutation_scale=14))
    ax.annotate("", xy=(0.5, 8.8), xytext=(0.5, 4.2), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.6, mutation_scale=20))
    ax.text(0.56, 6.4, r"$h\nu = E_3 - E_2$", color=PURPLE, fontsize=12.5)
    ax.set_xlim(-0.1, 2.0); ax.set_ylim(-0.5, 17.5); ax.set_xticks([]); ax.set_yticks([])
    ax.spines["bottom"].set_visible(False); ax.set_ylabel(r"energy, $E_n \propto n^2$")
    ax.set_title(r"butadiene: 4 $\pi$ electrons", loc="left", fontsize=11.5)
    fig.tight_layout()
    fig.savefig(f"{OUT}/homo_lumo.png", dpi=200)
    print("wrote", f"{OUT}/homo_lumo.png")
    return fig, None


# ------------------------------------------------------------ longer chain, smaller gap, redder light (box model)
@register
def chain_color():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    Ns = [2, 4, 6, 8, 10, 12]
    frames = [N for N in Ns for _ in range(8)] + [Ns[-1]] * 4
    wl = np.linspace(100, 800, 701)
    anchors = [380, 440, 490, 510, 580, 645, 700, 780]          # a smooth visible-spectrum colormap
    rgb = np.stack([np.interp(wl, anchors, [0.4, 0.0, 0.0, 0.0, 1.0, 1.0, 0.8, 0.4]),
                    np.interp(wl, anchors, [0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]),
                    np.interp(wl, anchors, [0.5, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0])], axis=-1)
    fade = np.clip(np.minimum((wl - 380) / 40, (780 - wl) / 80), 0, 1)[:, None]
    strip = (fade * rgb + (1 - fade) * 0.93)[None, :, :]
    fig = plt.figure(figsize=(8, 4.2))
    gs = fig.add_gridspec(2, 2, width_ratios=[1, 2.4], height_ratios=[1, 1.25], hspace=0.6, wspace=0.22)
    axe, axm, axs = fig.add_subplot(gs[:, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])

    def update(i):
        N = frames[i]; L = 1.445 * N
        En = 37.6 * np.arange(1, N // 2 + 2) ** 2 / L**2          # eV, h^2/8m = 37.6 eV A^2; up to the LUMO
        gap = En[N // 2] - En[N // 2 - 1]; lam = 1239.8 / gap
        axm.cla(); axe.cla(); axs.cla()
        cx = 1.2 * np.arange(N); cy = 0.5 * (np.arange(N) % 2)
        for j in range(N - 1):
            axm.plot(cx[j:j + 2], cy[j:j + 2], color="k", lw=2)
            if j % 2 == 0:
                axm.plot(cx[j:j + 2], cy[j:j + 2] - 0.16, color="k", lw=2)
        axm.plot(cx, cy, "o", color="k", ms=9)
        axm.set_xlim(-0.6, 14.2); axm.set_ylim(-0.4, 0.9); axm.set_axis_off()
        axm.set_title(f"{N} carbons, {N} $\\pi$ electrons, box L = {L:.1f} Å", loc="left", fontsize=11.5)
        for n, E in enumerate(En, start=1):
            occ = n <= N // 2
            axe.hlines(E, 0, 1, color="k" if occ else GRAY, lw=2.2 if occ else 1.6)
        axe.annotate("", xy=(0.5, En[N // 2]), xytext=(0.5, En[N // 2 - 1]),
                     arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.4, mutation_scale=16, shrinkA=0, shrinkB=0))
        axe.text(1.08, 0.5 * (En[N // 2] + En[N // 2 - 1]), f"{gap:.1f} eV", color=PURPLE, fontsize=12, va="center")
        axe.text(1.08, En[N // 2 - 1], "HOMO", color="k", fontsize=9.5, va="top")
        axe.text(1.08, En[N // 2], "LUMO", color=GRAY, fontsize=9.5, va="bottom")
        axe.set_xlim(0, 2.1); axe.set_ylim(0, 19); axe.set_xticks([])
        axe.spines["bottom"].set_visible(False)
        axe.set_ylabel("energy (eV)"); axe.set_title("levels", loc="left", fontsize=11)
        axs.imshow(strip, extent=[100, 800, 0, 1], aspect="auto")
        axs.text(240, 0.5, "ultraviolet", ha="center", va="center", fontsize=11, color=GRAY)
        axs.plot([lam], [1.12], marker="v", color="k", ms=13, clip_on=False)
        axs.text(lam, 1.3, f"{lam:.0f} nm", ha="center", fontsize=12)
        axs.set_xlim(100, 800); axs.set_ylim(0, 1); axs.set_yticks([]); axs.set_xlabel("absorbed wavelength predicted by the box (nm)")
        fig.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.12)

    ani = FuncAnimation(fig, update, frames=len(frames), interval=120, blit=False)
    return fig, ani


# ------------------------------------------------------------ quantum dots: a 3D box whose size sets the color (still)
@register
def quantum_dots():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    R = np.array([1.0, 1.3, 1.6, 2.0, 2.5, 3.1])
    lam = np.array([460, 500, 530, 565, 600, 630])               # schematic emission colors, small to large
    anchors = [380, 440, 490, 510, 580, 645, 700, 780]
    cols = np.stack([np.interp(lam, anchors, [0.4, 0.0, 0.0, 0.0, 1.0, 1.0, 0.8, 0.4]),
                     np.interp(lam, anchors, [0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]),
                     np.interp(lam, anchors, [0.5, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0])], axis=-1)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.1), gridspec_kw={"width_ratios": [1.5, 1], "wspace": 0.25})
    xc = np.cumsum(np.r_[0, R[:-1] + R[1:] + 0.5])
    for x0, r, c in zip(xc, R, cols):
        a1.add_patch(plt.Circle((x0, 0), r, color=c, alpha=0.9))
    a1.set_xlim(-1.3, xc[-1] + 3.3); a1.set_ylim(-3.4, 3.4); a1.set_aspect("equal"); a1.set_axis_off()
    a1.annotate("", xy=(xc[-1], -3.35), xytext=(xc[0], -3.35), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.6))
    a1.text(0.5 * (xc[0] + xc[-1]), -3.2, "bigger dot", ha="center", va="bottom", fontsize=10.5, color=GRAY)
    a1.set_title("same material, different sizes", loc="left", fontsize=11)
    rr = np.linspace(0.85, 3.3, 200)
    a2.plot(rr, 1 + 1.2 / rr**2, color=GRAY, lw=2)
    a2.scatter(R, 1 + 1.2 / R**2, s=90, c=cols, zorder=5)
    a2.axhline(1, color=GRAY, lw=1, ls="--"); a2.text(0.9, 1.06, "bulk gap", ha="left", va="bottom", fontsize=9.5, color=GRAY)
    a2.set_xlabel("dot radius R"); a2.set_ylabel("gap"); a2.set_xticks([]); a2.set_yticks([])
    a2.set_title(r"gap = bulk + $\propto 1/R^2$", loc="left", fontsize=11)
    fig.subplots_adjust(left=0.01, right=0.98, top=0.88, bottom=0.12)
    fig.savefig(f"{OUT}/quantum_dots.png", dpi=200)
    print("wrote", f"{OUT}/quantum_dots.png")
    return fig, None


# ============================================================ deck 3.4 "Tunneling and the finite square well"
# Page ch03/03 syncs barrier_packet, wall_leak, fsw_match, fsw_ladder, barrier_width, stm_scan and
# ammonia_flip. fsw_circle and barrier_mass are deck-only: the page shows the graphical solution and
# the width and mass dependence of T with marimo sliders instead.

# ------------------------------------------------------------ a ball bounces back, a wave gets through
@register
def barrier_packet():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    N = 4096                                                    # hbar = m = 1, split-operator steps on a periodic grid
    x = np.linspace(-60, 60, N, endpoint=False); dx = x[1] - x[0]
    kk = 2 * np.pi * np.fft.fftfreq(N, dx)
    k0, V0, a, sig, x0 = 5.0, 20.0, 0.35, 1.5, -14.0             # E = k0^2/2 = 12.5, well below the top V0 = 20
    E0 = 0.5 * k0**2
    V = np.where((x > 0) & (x < a), V0, 0.0)
    psi = np.exp(-(x - x0)**2 / (4 * sig**2) + 1j * k0 * x)
    psi = psi / np.sqrt(np.sum(np.abs(psi)**2) * dx)
    dt, per, nmove = 0.002, 85, 36                              # each frame advances t by 0.17
    half, kin = np.exp(-0.5j * V * dt), np.exp(-0.5j * kk**2 * dt)
    dens = np.zeros((nmove, N))
    for i in range(nmove):
        dens[i] = np.abs(psi)**2
        for _ in range(per):
            psi = half * np.fft.ifft(kin * np.fft.fft(half * psi))
    order = np.concatenate([np.zeros(4, int), np.arange(nmove), np.full(8, nmove - 1)])
    thit = (-0.35 - x0) / k0                                    # the classical ball turns at the wall
    win = (x > -24) & (x < 24); xs = x[win]
    sc = 0.92 * (25.5 - E0) / dens.max()                       # the tallest fringe, at the barrier, just fits
    fig, (axc, ax) = plt.subplots(2, 1, figsize=(8, 3.6), sharex=True,
                                  gridspec_kw={"height_ratios": [1, 2.7], "hspace": 0.18})
    axc.axvspan(0, a, color=GRAY, alpha=0.5, lw=0)
    axc.axhline(0.4, color=GRAY, lw=0.8, ls=":")
    (ball,) = axc.plot([], [], "o", color=CARDINAL, ms=11)
    axc.set_ylim(0, 1); axc.set_yticks([]); axc.spines["left"].set_visible(False); axc.tick_params(bottom=False)
    axc.set_title("classical ball with the same energy: it always turns back", loc="left", fontsize=12)
    ax.fill_between([0, a], 0, V0, color=GRAY, alpha=0.3, lw=0)
    ax.plot([-24, 0, 0, a, a, 24], [0, 0, V0, V0, 0, 0], color="k", lw=2)
    ax.axhline(E0, color=GRAY, lw=1, ls="--")
    (dline,) = ax.plot([], [], color=TEAL, lw=2)
    band = [ax.fill_between(xs, E0, E0, color=TEAL, alpha=0.25, lw=0)]
    tlab = ax.text(23.6, 24.6, "", ha="right", va="top", color=TEAL, fontsize=13)
    ax.set_xlim(-24, 24); ax.set_ylim(8, 25.5); ax.set_xticks([])
    ax.set_yticks([E0, V0]); ax.set_yticklabels(["E", r"$V_0$"], fontsize=13)
    ax.set_xlabel("x", fontsize=12)
    ax.set_title(r"quantum wave: $|\Psi(x,t)|^2$ drawn on its energy", loc="left", fontsize=12)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.92, bottom=0.08)

    def update(i):
        d = dens[order[i]]
        t = order[i] * per * dt
        dline.set_data(xs, E0 + sc * d[win])
        band[0].remove(); band[0] = ax.fill_between(xs, E0, E0 + sc * d[win], color=TEAL, alpha=0.25, lw=0)
        ball.set_data([x0 + k0 * t if t < thit else -0.35 - k0 * (t - thit)], [0.4])
        tr = d[x > a].sum() * dx
        tlab.set_text(f"through the barrier: {100 * tr:.0f}%" if tr > 0.005 else "")

    ani = FuncAnimation(fig, update, frames=len(order), interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ finite walls: the state leaks a distance 1/beta (still)
@register
def wall_leak():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    z0 = 2.0                                                    # well strength; x in units of L/2, E in units of V0
    lo, hi = 1e-9, np.pi / 2 - 1e-9                             # even ground state: z tan z = sqrt(z0^2 - z^2)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if mid * np.tan(mid) < np.sqrt(z0**2 - mid**2) else (lo, mid)
    z = 0.5 * (lo + hi); b = np.sqrt(z0**2 - z**2); E = (z / z0)**2    # here beta = b, since L/2 = 1
    x = np.linspace(-3.3, 3.3, 900)
    psi = np.where(np.abs(x) < 1, np.cos(z * x), np.cos(z) * np.exp(-b * (np.abs(x) - 1)))
    sc = 0.42
    fig, ax = plt.subplots(figsize=(8, 3.1))
    ax.axvspan(-1, 1, color=TEAL, alpha=0.07, lw=0)
    for x1, x2 in ((-3.3, -1), (1, 3.3)):
        ax.axvspan(x1, x2, color=CARDINAL, alpha=0.06, lw=0)
    ax.plot([-3.3, -1, -1, 1, 1, 3.3], [1, 1, 0, 0, 1, 1], color="k", lw=2.4)
    ax.axhline(E, color=GRAY, lw=1.1, ls="--")
    ax.text(3.25, E + 0.03, "E", ha="right", va="bottom", color=GRAY, fontsize=13)
    ax.fill_between(x, E, E + sc * psi, where=np.abs(x) >= 1, color=CARDINAL, alpha=0.3, lw=0)
    ax.plot(x, E + sc * psi, color=TEAL, lw=2.6)
    d = 1 / b
    ax.annotate("", xy=(1 + d, E - 0.08), xytext=(1, E - 0.08),
                arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(1 + d / 2, E - 0.12, r"$1/\beta$", ha="center", va="top", color=CARDINAL, fontsize=14)
    ax.text(1.75, E + 0.14, r"$\psi \propto e^{-\beta x}$", color=CARDINAL, fontsize=13)
    ax.text(0, 0.86, r"$V = 0$:  $E > V$, $\psi$ oscillates", ha="center", color=TEAL, fontsize=12.5)
    for xc in (-2.15, 2.15):
        ax.text(xc, 1.07, r"$V_0$:  $E < V$, $\psi$ decays", ha="center", color=CARDINAL, fontsize=12.5)
    ax.set_xlim(-3.3, 3.3); ax.set_ylim(-0.05, 1.27); ax.set_yticks([])
    ax.set_xticks([-1, 0, 1]); ax.set_xticklabels([r"$-L/2$", "0", r"$L/2$"], fontsize=13)
    ax.spines["left"].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"{OUT}/wall_leak.png", dpi=200)
    print("wrote", f"{OUT}/wall_leak.png")
    return fig, None


# ------------------------------------------------------------ join psi and psi': at most energies the join has a kink (still)
@register
def fsw_match():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    z0 = 2.0                                                    # the same well as wall_leak
    lo, hi = 1e-9, np.pi / 2 - 1e-9
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if mid * np.tan(mid) < np.sqrt(z0**2 - mid**2) else (lo, mid)
    zr = 0.5 * (lo + hi)
    x = np.linspace(-2.6, 2.6, 900)
    fig, axes = plt.subplots(2, 1, figsize=(4.8, 4.4), sharex=True, gridspec_kw={"hspace": 0.45})
    for ax, z, col, head in ((axes[0], 0.45 * zr, CARDINAL, "trial E: the slopes disagree, a kink"),
                             (axes[1], zr, TEAL, r"allowed E: $\psi$ and $\psi'$ both match")):
        b = np.sqrt(z0**2 - z**2); E = (z / z0)**2
        psi = np.where(np.abs(x) < 1, np.cos(z * x), np.cos(z) * np.exp(-b * (np.abs(x) - 1)))
        ax.plot([-2.6, -1, -1, 1, 1, 2.6], [1, 1, 0, 0, 1, 1], color="k", lw=2)
        ax.axhline(E, color=GRAY, lw=0.9, ls="--")
        ax.plot(x, E + 0.45 * psi, color=col, lw=2.6)
        ax.plot([-1, 1], [E + 0.45 * np.cos(z)] * 2, "o", mfc="none", mec=col, mew=2, ms=17)
        ax.set_title(head, loc="left", fontsize=12.5, color=col)
        ax.set_xlim(-2.6, 2.6); ax.set_ylim(-0.04, 1.08); ax.set_yticks([])
        ax.spines["left"].set_visible(False)
    axes[0].tick_params(bottom=False)
    axes[1].set_xticks([-1, 0, 1]); axes[1].set_xticklabels([r"$-L/2$", "0", r"$L/2$"], fontsize=12)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.92, bottom=0.1)
    fig.savefig(f"{OUT}/fsw_match.png", dpi=200)
    print("wrote", f"{OUT}/fsw_match.png")
    return fig, None


# ------------------------------------------------------------ graphical solution: the circle z0 grows across the branches (deck GIF)
@register
def fsw_circle():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    z0s = np.concatenate([np.full(6, 0.5), np.linspace(0.5, 7.2, 47)[1:], np.full(12, 7.2)])
    fig, (ax, axw) = plt.subplots(1, 2, figsize=(8, 3.5), gridspec_kw={"width_ratios": [1, 1.3], "wspace": 0.14})
    for m in range(5):                                          # even branches z tan z, odd branches -z cot z
        zz = np.linspace(m * np.pi / 2 + 1e-4, (m + 1) * np.pi / 2 - 1e-4, 400)
        ee = zz * np.tan(zz) if m % 2 == 0 else -zz / np.tan(zz)
        ee[ee > 8] = np.nan
        ax.plot(zz, ee, color=TEAL if m % 2 == 0 else PURPLE, lw=2.2)
    for m in range(1, 5):
        ax.axvline(m * np.pi / 2, color=GRAY, lw=0.7, ls=":")
    th = np.linspace(0, np.pi / 2, 200)
    (circ,) = ax.plot([], [], color="k", lw=1.8)
    dots = [ax.plot([], [], "o", color=TEAL if m % 2 == 0 else PURPLE, ms=9, mec="k", mew=0.8, zorder=5)[0]
            for m in range(5)]
    ax.set_aspect("equal"); ax.set_xlim(0, 7.7); ax.set_ylim(0, 7.7); ax.set_yticks([])
    ax.set_xticks(np.arange(1, 5) * np.pi / 2)
    ax.set_xticklabels([r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"], fontsize=13)
    ax.set_xlabel(r"$z = kL/2$", fontsize=12); ax.set_ylabel(r"$\eta = \beta L/2$", fontsize=12)
    ax.text(0.74, 1.03, "even", color=TEAL, fontsize=12.5, ha="right", transform=ax.transAxes)
    ax.text(1.0, 1.03, "odd", color=PURPLE, fontsize=12.5, ha="right", transform=ax.transAxes)
    (walls,) = axw.plot([], [], color="k", lw=2.4)             # depth fixed, L/2 grows in step with z0
    lev = [axw.plot([], [], color=TEAL if m % 2 == 0 else PURPLE, lw=3.2)[0] for m in range(5)]
    axw.set_xlim(-8.4, 8.4); axw.set_ylim(-0.04, 1.12); axw.set_xticks([])
    axw.set_yticks([0, 1]); axw.set_yticklabels(["0", r"$V_0$"], fontsize=13)
    axw.set_xlabel("widen the well, depth fixed", fontsize=12)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.88, bottom=0.16)

    def update(i):
        z0 = z0s[i]
        circ.set_data(z0 * np.cos(th), z0 * np.sin(th))
        walls.set_data([-8.4, -z0, -z0, z0, z0, 8.4], [1, 1, 0, 0, 1, 1])
        n = int(2 * z0 / np.pi) + 1                             # one more state each time z0 passes a multiple of pi/2
        for m in range(5):
            if m < n:
                lo, hi = m * np.pi / 2 + 1e-9, min((m + 1) * np.pi / 2, z0) - 1e-9
                for _ in range(50):
                    mid = 0.5 * (lo + hi)
                    f = (mid * np.tan(mid) if m % 2 == 0 else -mid / np.tan(mid)) - np.sqrt(z0**2 - mid**2)
                    lo, hi = (mid, hi) if f < 0 else (lo, mid)
                z = 0.5 * (lo + hi)
                dots[m].set_data([z], [np.sqrt(z0**2 - z**2)])
                lev[m].set_data([-z0, z0], [(z / z0)**2] * 2)   # E = V0 (z/z0)^2
            else:
                dots[m].set_data([], []); lev[m].set_data([], [])
        ax.set_title(rf"$z_0 = {z0:.2f}$", loc="left", fontsize=13)
        axw.set_title(f"{n} bound state" + ("s" if n > 1 else ""), loc="left", fontsize=13)

    ani = FuncAnimation(fig, update, frames=len(z0s), interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ bound states of a finite well, what leaks, vs the infinite box (still)
@register
def fsw_ladder():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    V0, L = 5.0, 10.0                                           # electron in a 5 eV, 10 Angstrom well (the page's example)
    z0 = 0.5 * L * 0.5123 * np.sqrt(V0)                         # 0.5123 = sqrt(2 m_e (1 eV)) / hbar, in 1/Angstrom
    n = int(2 * z0 / np.pi) + 1
    zs = np.zeros(n)
    for m in range(n):
        lo, hi = m * np.pi / 2 + 1e-9, min((m + 1) * np.pi / 2, z0) - 1e-9
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            f = (mid * np.tan(mid) if m % 2 == 0 else -mid / np.tan(mid)) - np.sqrt(z0**2 - mid**2)
            lo, hi = (mid, hi) if f < 0 else (lo, mid)
        zs[m] = 0.5 * (lo + hi)
    E = V0 * (zs / z0)**2
    Einf = 0.3760 * np.arange(1, n + 1)**2                      # n^2 h^2 / 8 m L^2 for L = 10 Angstrom, in eV
    x = np.linspace(-12, 12, 1600); dx = x[1] - x[0]
    out = np.abs(x) > L / 2
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(8, 3.6), sharey=True,
                                        gridspec_kw={"width_ratios": [1, 1, 0.5], "wspace": 0.08})
    for ax in (ax1, ax2):
        ax.plot([-12, -5, -5, 5, 5, 12], [V0, V0, 0, 0, V0, V0], color="k", lw=2.2)
        ax.set_xlim(-12, 12); ax.set_xticks([-5, 5]); ax.set_xticklabels([r"$-L/2$", r"$L/2$"], fontsize=12)
    for m in range(n):
        k, b = 2 * zs[m] / L, 2 * np.sqrt(z0**2 - zs[m]**2) / L
        if m % 2 == 0:
            psi = np.where(out, np.cos(k * L / 2) * np.exp(-b * (np.abs(x) - L / 2)), np.cos(k * x))
        else:
            psi = np.where(out, np.sign(x) * np.sin(k * L / 2) * np.exp(-b * (np.abs(x) - L / 2)), np.sin(k * x))
        p = psi**2 / (np.sum(psi**2) * dx)
        col = TEAL if m % 2 == 0 else PURPLE
        for ax in (ax1, ax2):
            ax.hlines(E[m], -12, 12, color=GRAY, lw=0.8, ls="--")
        ax1.plot(x, E[m] + 0.36 * psi / np.abs(psi).max(), color=col, lw=2.2)
        pn = 0.6 * p / p.max()
        ax2.fill_between(x, E[m], E[m] + pn, where=out, color=CARDINAL, alpha=0.5, lw=0)
        ax2.plot(x, E[m] + pn, color=CARDINAL, lw=1.8)
        ax2.text(11.8, E[m] + 0.08, f"{100 * np.sum(p[out]) * dx:.1f}%", ha="right", va="bottom",
                 fontsize=11.5, color=CARDINAL)
        ax3.plot([0.06, 0.42], [E[m]] * 2, color=col, lw=3)
        ax3.plot([0.58, 0.94], [Einf[m]] * 2, color=GRAY, lw=3)
        ax3.plot([0.42, 0.58], [E[m], Einf[m]], color=GRAY, lw=0.9, ls=":")
    ax3.axhline(V0, color="k", lw=1.6)
    ax3.set_xlim(0, 1); ax3.set_xticks([0.24, 0.76]); ax3.set_xticklabels(["finite", "infinite"], fontsize=11.5)
    ax3.tick_params(bottom=False)
    ax1.set_ylim(-0.15, 6.5); ax1.set_yticks(range(7)); ax1.set_ylabel("energy (eV)", fontsize=12)
    ax1.set_title(r"$\psi_n$ on its level", loc="left", fontsize=12)
    ax2.set_title(r"$|\psi_n|^2$, shaded: outside", loc="left", fontsize=12)
    ax3.set_title("levels", loc="left", fontsize=12)
    for ax in (ax2, ax3):
        ax.tick_params(left=False)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.91, bottom=0.1)
    fig.savefig(f"{OUT}/fsw_ladder.png", dpi=200)
    print("wrote", f"{OUT}/fsw_ladder.png")
    return fig, None


# ------------------------------------------------------------ a barrier: widen it and the transmitted wave shrinks
@register
def barrier_width():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    E, V0 = 0.5, 1.0                                            # hbar = m = 1: k = beta = 1, so the exact T is sech^2(a)
    k, q = np.sqrt(2 * E), np.sqrt(2 * (V0 - E))
    x = np.linspace(-12.5, 15.5, 1400)
    nf = 44
    aa = np.concatenate([np.linspace(0.15, 3.0, nf - 10), np.full(10, 3.0)])
    ph = 2 * np.pi * np.arange(nf) / 11                         # e^{-i omega t}: one turn every 11 frames
    ag = np.linspace(0, 3.2, 200)
    fig, (ax, axt) = plt.subplots(1, 2, figsize=(8, 3.0), gridspec_kw={"width_ratios": [2.4, 1], "wspace": 0.22})
    (pot,) = ax.plot([], [], color="k", lw=2)
    blk = [ax.fill_between([0, 1], 0, 1, color=GRAY, alpha=0.25, lw=0)]
    ax.axhline(E, color=GRAY, lw=1, ls="--")
    (wave,) = ax.plot([], [], color=TEAL, lw=2.2)
    (envp,) = ax.plot([], [], color=TEAL, lw=1.1, ls=":")
    (envm,) = ax.plot([], [], color=TEAL, lw=1.1, ls=":")
    ax.text(-6.5, 1.06, "incident + reflected", ha="center", color=GRAY, fontsize=12)
    ax.text(9.5, 1.06, r"transmitted, amplitude $|t|$", ha="center", color=TEAL, fontsize=12)
    ax.set_xlim(-12.5, 15.5); ax.set_ylim(-0.02, 1.2); ax.set_xticks([])
    ax.set_yticks([E, V0]); ax.set_yticklabels(["E", r"$V_0$"], fontsize=13)
    ax.set_xlabel("x", fontsize=12)
    axt.semilogy(ag, 1 / np.cosh(ag)**2, color=GRAY, lw=2.2)
    axt.semilogy(ag, 4 * np.exp(-2 * ag), color=GRAY, lw=1, ls="--")
    axt.text(1.45, 0.55, r"$\approx 4\,e^{-2\beta a}$", fontsize=12, color=GRAY)
    (dot,) = axt.plot([], [], "o", color=CARDINAL, ms=9, zorder=5)
    axt.set_xlim(0, 3.2); axt.set_ylim(5e-3, 1.6)
    axt.set_xlabel(r"width $a$, units of $1/\beta$", fontsize=11.5)
    axt.set_title(r"$T$, log scale", loc="left", fontsize=12)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.88, bottom=0.17)

    def update(i):
        a = aa[i]
        M = np.array([[1, -1, -1, 0], [-1j * k, -q, q, 0],                     # psi and psi' continuous at 0 and a
                      [0, np.exp(q * a), np.exp(-q * a), -np.exp(1j * k * a)],
                      [0, q * np.exp(q * a), -q * np.exp(-q * a), -1j * k * np.exp(1j * k * a)]])
        r, C, D, t = np.linalg.solve(M, np.array([-1, -1j * k, 0, 0]))
        psi = np.where(x < 0, np.exp(1j * k * x) + r * np.exp(-1j * k * x),
                       np.where(x < a, C * np.exp(q * x) + D * np.exp(-q * x), t * np.exp(1j * k * x)))
        wave.set_data(x, E + 0.2 * np.real(psi * np.exp(-1j * ph[i])))
        xr = x[x >= a]
        envp.set_data(xr, E + 0.2 * abs(t) + 0 * xr); envm.set_data(xr, E - 0.2 * abs(t) + 0 * xr)
        pot.set_data([-12.5, 0, 0, a, a, 15.5], [0, 0, V0, V0, 0, 0])
        blk[0].remove(); blk[0] = ax.fill_between([0, a], 0, V0, color=GRAY, alpha=0.25, lw=0)
        dot.set_data([a], [abs(t)**2])
        ax.set_title(rf"$a = {a:.2f}/\beta$:  $T = |t|^2 = {abs(t)**2:.3f}$", loc="left", fontsize=13)

    ani = FuncAnimation(fig, update, frames=nf, interval=120, blit=False)
    return fig, ani


# ------------------------------------------------------------ width and mass sit in the exponent: electron, H, D (still)
@register
def barrier_mass():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    dE = 0.2                                                    # barrier height above E, eV
    a = np.linspace(0, 10, 2000)                                # width, Angstrom
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    for name, m, col, xy, ha in (("electron", 1.0, TEAL, (9.9, -1.1), "right"),
                                 ("H", 1836.15, PURPLE, (1.6, -12.4), "left"),
                                 ("D", 3670.48, CARDINAL, (0.8, -12.4), "right")):
        lt = -2 * 0.5123 * np.sqrt(m * dE) * a / np.log(10)     # log10 of e^{-2 beta a}
        ok = lt > -16.2
        ax.plot(a[ok], lt[ok], color=col, lw=2.8)
        ax.text(*xy, name, color=col, fontsize=14, ha=ha)
    ax.set_xlim(0, 10); ax.set_ylim(-16, 0.6)
    ax.set_yticks([0, -4, -8, -12, -16])
    ax.set_yticklabels(["1", r"$10^{-4}$", r"$10^{-8}$", r"$10^{-12}$", r"$10^{-16}$"], fontsize=12)
    ax.tick_params(axis="x", labelsize=12)
    ax.set_xlabel("barrier width a (Å)", fontsize=12); ax.set_ylabel(r"$T \approx e^{-2\beta a}$", fontsize=13)
    ax.set_title(r"the same barrier, $V_0 - E = 0.2$ eV, for three particles", loc="left", fontsize=12)
    fig.tight_layout()
    fig.savefig(f"{OUT}/barrier_mass.png", dpi=200)
    print("wrote", f"{OUT}/barrier_mass.png")
    return fig, None


# ------------------------------------------------------------ the STM: a tip scans at constant height, the current maps the atoms
@register
def stm_scan():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    beta, h = 1.09, 3.6                                         # 1/Angstrom for a 4.5 eV work function; apex height
    cx = np.append(1.5 + 3.0 * np.arange(6), 12.0)              # six surface atoms and one adatom in a hollow
    cy = np.append(np.zeros(6), 1.2)
    R = np.append(np.full(6, 1.0), 0.8)                         # the adatom's top sits 1 Angstrom above the others
    xs = np.linspace(-0.2, 18.2, 1500)
    gap = (np.sqrt((xs[:, None] - cx)**2 + (h - cy)**2) - R).min(axis=1)
    cur = np.exp(-2 * beta * (gap - (h - 1.0)))                 # current relative to the value over a surface atom
    nf = 46
    xt = np.concatenate([np.linspace(-0.2, 18.2, nf - 6), np.full(6, 18.2)])
    fig, (ax, axi) = plt.subplots(2, 1, figsize=(8, 3.8), sharex=True,
                                  gridspec_kw={"height_ratios": [2.0, 1], "hspace": 0.14})
    for x0, y0, r0, c in zip(cx, cy, R, [GRAY] * 6 + [ORANGE]):
        ax.add_patch(plt.Circle((x0, y0), r0, facecolor=c, alpha=0.45 if c == GRAY else 0.85, edgecolor=c, lw=1.5))
    tip = plt.Polygon([[0, h], [-1.6, h + 3.2], [1.6, h + 3.2]], closed=True, facecolor=GRAY, edgecolor="k", lw=1.2)
    ax.add_patch(tip)
    (spark,) = ax.plot([], [], color=TEAL, solid_capstyle="round")
    ax.set_aspect("equal"); ax.set_xlim(-0.2, 18.2); ax.set_ylim(-0.6, 5.4); ax.axis("off")
    ax.set_title("the tip scans at constant height; electrons tunnel across the gap", loc="left", fontsize=13)
    axi.plot(xs, cur, color=TEAL, lw=1, alpha=0.15)
    (trace,) = axi.plot([], [], color=TEAL, lw=2.4)
    (now,) = axi.plot([], [], "o", color=TEAL, ms=7)
    axi.set_ylim(0, 10); axi.set_yticks([0, 4, 8]); axi.set_xticks([]); axi.tick_params(labelsize=12)
    axi.set_ylabel("current", fontsize=13)
    fig.subplots_adjust(left=0.07, right=0.99, top=0.93, bottom=0.04)

    def update(i):
        x0 = xt[i]
        tip.set_xy([[x0, h], [x0 - 1.6, h + 3.2], [x0 + 1.6, h + 3.2]])
        j = np.argmin(np.sqrt((x0 - cx)**2 + (h - cy)**2) - R)   # nearest atom: the electrons tunnel to it
        u = np.array([x0 - cx[j], h - cy[j]]); u = u / np.linalg.norm(u)
        I = np.interp(x0, xs, cur)
        spark.set_data([x0, cx[j] + R[j] * u[0]], [h, cy[j] + R[j] * u[1]])
        spark.set_linewidth(1.2 + 1.8 * I**0.6); spark.set_alpha(min(1.0, 0.35 + 0.12 * I))
        ok = xs <= x0
        trace.set_data(xs[ok], cur[ok]); now.set_data([x0], [I])

    ani = FuncAnimation(fig, update, frames=nf, interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ ammonia: start on one side of a double well, tunnel across and back
@register
def ammonia_flip():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    Vb, N = 14.0, 700                                           # V = Vb (x^2 - 1)^2 with H = -d^2/dx^2 + V
    x = np.linspace(-2.2, 2.2, N); h = x[1] - x[0]
    V = Vb * (x**2 - 1)**2
    H = np.diag(2 / h**2 + V) - np.diag(np.ones(N - 1) / h**2, 1) - np.diag(np.ones(N - 1) / h**2, -1)
    En, vec = np.linalg.eigh(H)
    s, an = vec[:, 0] / np.sqrt(h), vec[:, 1] / np.sqrt(h)
    s = s * np.sign(s[N // 2]); an = an * np.sign(an[N // 4])  # an > 0 on the left, so s + an starts on the left
    D, Em = En[1] - En[0], 0.5 * (En[0] + En[1])
    nf = 44
    ph = 2 * np.pi * np.arange(nf) / nf                         # Delta t over one full period h/Delta, a seamless loop
    rho0 = 0.5 * (s + an)**2
    sc = 0.36 * Vb / rho0.max()
    fig = plt.figure(figsize=(8, 3.6))
    gs = fig.add_gridspec(1, 2, width_ratios=[2.2, 1], wspace=0.22)
    ax, axp = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    ax.plot(x, V, color="k", lw=2)
    ax.axhline(En[0], color=TEAL, lw=1.2); ax.axhline(En[1], color=PURPLE, lw=1.2)
    ax.annotate(r"split by $\Delta$", xy=(0, En[0] - 0.1), xytext=(0, 3.2), ha="center", fontsize=12, color=GRAY,
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.2))
    (dline,) = ax.plot([], [], color=TEAL, lw=2)
    band = [ax.fill_between(x, Em, Em, color=TEAL, alpha=0.25, lw=0)]
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(0, 1.75 * Vb); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("umbrella coordinate", fontsize=12); ax.set_ylabel("energy", fontsize=12)
    ax.set_title("start on the left: it tunnels across and back", loc="left", fontsize=12)
    axp.axhline(0.5, color=GRAY, lw=0.7, ls=":")
    (trace,) = axp.plot([], [], color=TEAL, lw=2.4)
    (now,) = axp.plot([], [], "o", color=TEAL, ms=7)
    axp.set_xlim(0, 1); axp.set_ylim(-0.04, 1.06)
    axp.set_xticks([0, 0.5, 1]); axp.set_xticklabels(["0", r"$h/2\Delta$", r"$h/\Delta$"], fontsize=12)
    axp.set_yticks([0, 1]); axp.set_yticklabels(["0", "1"], fontsize=12); axp.set_xlabel("time", fontsize=12)
    axp.set_title("probability on the right", loc="left", fontsize=12)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.9, bottom=0.15)
    p = ax.get_position()
    mols = []                                                   # NH3 seen side on: N above (left well) or below (right)
    for xc, sg in ((-1.0, 1), (1.0, -1)):
        u = (xc + 2.2) / 4.4
        axm = fig.add_axes([p.x0 + p.width * u - 0.07, p.y0 + p.height * 0.68, 0.14, 0.24])
        axm.set_xlim(-1, 1); axm.set_ylim(-1, 1); axm.set_aspect("equal"); axm.axis("off")
        hx, hy = np.array([-0.62, 0.62, 0.16]), sg * np.array([-0.18, -0.18, -0.42])
        bonds = [axm.plot([0, hx[j]], [sg * 0.5, hy[j]], color=GRAY, lw=2.2)[0] for j in range(3)]
        hs = axm.scatter(hx, hy, s=170, facecolor="white", edgecolor=GRAY, lw=1.6, zorder=3)
        nn = axm.scatter([0], [sg * 0.5], s=420, facecolor=TEAL, edgecolor="k", lw=1, zorder=4)
        mols.append(bonds + [hs, nn])
    xg = np.linspace(0, 1, 300)
    pr = np.sum((s * an)[x > 0]) * h                            # P_right(t) = 1/2 + pr cos(Delta t), pr close to -1/2

    def update(i):
        c = np.cos(ph[i])
        rho = 0.5 * (s**2 + an**2) + s * an * c                 # |Psi|^2: a fixed part and a cross term at frequency Delta
        dline.set_data(x, Em + sc * rho)
        band[0].remove(); band[0] = ax.fill_between(x, Em, Em + sc * rho, color=TEAL, alpha=0.25, lw=0)
        Pr = 0.5 + pr * c
        for art in mols[0]:
            art.set_alpha(0.12 + 0.88 * (1 - Pr))
        for art in mols[1]:
            art.set_alpha(0.12 + 0.88 * Pr)
        tt = i / nf
        ok = xg <= tt
        trace.set_data(xg[ok], 0.5 + pr * np.cos(2 * np.pi * xg[ok])); now.set_data([tt], [Pr])

    ani = FuncAnimation(fig, update, frames=nf, interval=100, blit=False)
    return fig, ani


# ------------------------------------------------------------ the sign of V - E decides which way psi bends (deck still)
@register
def curvature_signs():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (axa, axf) = plt.subplots(1, 2, figsize=(8, 2.7), gridspec_kw={"wspace": 0.08})
    x = np.linspace(-0.3, 2 * np.pi + 0.3, 400)
    axa.axvspan(-0.3, 2 * np.pi + 0.3, color=TEAL, alpha=0.07, lw=0)
    axa.plot(x, np.cos(x), color=TEAL, lw=2.8)
    for x0, y0, dy, lab in ((0, 1.0, -0.45, r"$\psi > 0$, $\psi'' < 0$"), (np.pi, -1.0, 0.45, r"$\psi < 0$, $\psi'' > 0$")):
        axa.annotate("", xy=(x0, y0 + dy), xytext=(x0, y0),
                     arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2.4, mutation_scale=18))
        axa.text(x0 + 0.3, y0 + 0.45 * dy, lab, va="center", fontsize=12)
    axa.set_title(r"$E > V$: opposite signs", loc="left", fontsize=13, color=TEAL)
    axa.text(np.pi, -1.62, "bends back toward the axis: oscillates", ha="center", fontsize=12, color=TEAL)
    x = np.linspace(0, 3.2, 300)
    axf.axvspan(0, 3.2, color=CARDINAL, alpha=0.06, lw=0)
    for sg in (1, -1):                                          # e^{-x} and -e^{-x}: both bend away from the axis
        axf.plot(x, sg * 1.25 * np.exp(-0.9 * x), color=TEAL, lw=2.8 if sg > 0 else 1.8, alpha=1 if sg > 0 else 0.55)
        x0 = 0.9; y0 = sg * 1.25 * np.exp(-0.81)
        axf.annotate("", xy=(x0, y0 + sg * 0.45), xytext=(x0, y0),
                     arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=2.4, mutation_scale=18))
        axf.text(x0 + 0.15, y0 + sg * 0.32, r"$\psi > 0$, $\psi'' > 0$" if sg > 0 else r"$\psi < 0$, $\psi'' < 0$",
                 va="center", fontsize=12)
    axf.set_title(r"$E < V$: the same sign", loc="left", fontsize=13, color=CARDINAL)
    axf.text(1.6, -1.62, "bends away: grows or decays", ha="center", fontsize=12, color=CARDINAL)
    for ax, x1 in ((axa, 2 * np.pi + 0.3), (axf, 3.2)):
        ax.axhline(0, color=GRAY, lw=1)
        ax.text(x1, 0.06, r"$\psi = 0$", ha="right", va="bottom", fontsize=11, color=GRAY)
        ax.set_ylim(-1.8, 1.45); ax.set_xticks([]); ax.set_yticks([])
        for s in ("left", "bottom"):
            ax.spines[s].set_visible(False)
    axa.set_xlim(-0.3, 2 * np.pi + 0.3); axf.set_xlim(0, 3.2)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.02)
    fig.savefig(f"{OUT}/curvature_signs.png", dpi=200)
    print("wrote", f"{OUT}/curvature_signs.png")
    return fig, None


# ------------------------------------------------------------ read psi from V(x): a tracer draws psi, the arrow is psi'' (deck GIF)
@register
def curvature_tracer():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    N = 1400                                                    # hbar^2/2m = 1, so psi'' = (V - E) psi
    x = np.linspace(-3.0, 8.0, N); h = x[1] - x[0]
    V = np.where(x < 0, 12.0, np.where(x < 3, 7.0, np.where(x < 5.5, 0.0, 30.0)))
    H = np.diag(2 / h**2 + V) - np.diag(np.ones(N - 1) / h**2, 1) - np.diag(np.ones(N - 1) / h**2, -1)
    En, vec = np.linalg.eigh(H)
    E = En[4]                                                   # four nodes; E lies between the 7 and 12 steps
    psi = vec[:, 4] / np.abs(vec[:, 4]).max()
    psi = psi * np.sign(psi[np.argmin(np.abs(x - 0.4))])
    curv = (V - E) * psi                                        # psi'' from the Schrodinger equation
    cmax = np.abs(curv).max()
    sc = 3.0
    nf = 52
    xt = np.concatenate([np.linspace(-3.0, 8.0, nf - 8), np.full(8, 8.0)])
    fig, ax = plt.subplots(figsize=(8, 3.5))
    for x1, x2, al in ((-3, 0, False), (0, 3, True), (3, 5.5, True), (5.5, 8, False)):
        ax.axvspan(x1, x2, color=TEAL if al else CARDINAL, alpha=0.07 if al else 0.06, lw=0)
    ax.plot(x, np.minimum(V, 17.5), color="k", lw=2)
    ax.axhline(E, color=GRAY, lw=1, ls="--")
    for xc, top, bot, c in ((-1.5, r"$V - E$ small", "slow decay", CARDINAL), (1.5, r"$E - V$ small", "long wavelength", TEAL),
                            (4.25, r"$E - V$ large", "short wavelength", TEAL), (6.75, r"$V - E$ large", "fast decay", CARDINAL)):
        ax.text(xc, 17.0, top, ha="center", va="top", fontsize=11.5, color=c)
        ax.text(xc, 15.6, bot, ha="center", va="top", fontsize=11.5, color=c)
    (trace,) = ax.plot([], [], color=TEAL, lw=2.6)
    (tip,) = ax.plot([], [], "o", color="k", ms=6, zorder=6)
    arrow = ax.annotate("", xy=(0, E), xytext=(0, E), arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2.6, mutation_scale=18))
    ax.set_xlim(-3, 8); ax.set_ylim(-0.4, 17.5); ax.set_xticks([]); ax.set_yticks([E]); ax.set_yticklabels(["E"], fontsize=13)
    ax.set_xlabel("x", fontsize=12)
    fig.subplots_adjust(left=0.05, right=0.99, top=0.9, bottom=0.09)

    def update(i):
        x0 = xt[i]
        j = min(N - 1, np.searchsorted(x, x0))
        ok = x <= x0
        trace.set_data(x[ok], E + sc * psi[ok])
        y0 = E + sc * psi[j]
        tip.set_data([x0], [y0])
        c = curv[j]
        toward = c * psi[j] < 0                                 # psi'' opposite to psi: bends back toward the axis
        show = abs(c) > 0.03 * cmax
        arrow.set_visible(show)
        arrow.xy = (x0, y0 + np.sign(c) * (1.0 + 2.6 * np.sqrt(abs(c) / cmax)))
        arrow.set_position((x0, y0))
        arrow.arrow_patch.set_color(TEAL if toward else CARDINAL)
        if show:
            ax.set_title(r"$\psi''$ arrow: " + ("opposite sign to $\\psi$, bends toward the axis" if toward
                         else "same sign as $\\psi$, bends away from the axis"),
                         loc="left", fontsize=12.5, color=TEAL if toward else CARDINAL)

    ani = FuncAnimation(fig, update, frames=nf, interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ what T means: send particles one at a time and count (deck GIF)
@register
def barrier_counts():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    T = 0.27                                                    # the barrier of barrier_packet
    rng = np.random.default_rng(17)                             # 33 of 120 get through, close to T
    n = 120
    through = rng.random(n) < T
    yj = rng.uniform(0.18, 0.82, n)
    t0 = 0.5 * np.arange(n)                                     # two particles leave the source per frame
    v, L = 1.5, 12.0
    tdet = 2 * L / v                                            # frames from launch to a detector
    nf = int(t0[-1] + tdet) + 10
    frac = np.cumsum(through) / np.arange(1, n + 1)
    fig, (ax, axf) = plt.subplots(2, 1, figsize=(8, 3.6), gridspec_kw={"height_ratios": [1.1, 1], "hspace": 0.62})
    ax.axvspan(-0.4, 0.4, color=GRAY, alpha=0.55, lw=0)
    for xd, c in ((-L - 0.6, ORANGE), (L + 0.6, TEAL)):
        ax.axvspan(xd - 0.5, xd + 0.5, color=c, alpha=0.35, lw=0)
    dots = ax.scatter([], [], s=26, zorder=4)
    lab_l = ax.text(-L - 1.2, 1.12, "", ha="left", va="bottom", fontsize=12, color=ORANGE)
    lab_r = ax.text(L + 1.2, 1.12, "", ha="right", va="bottom", fontsize=12, color=TEAL)
    ax.text(0, 1.12, "barrier", ha="center", va="bottom", fontsize=11, color=GRAY)
    ax.set_xlim(-L - 1.2, L + 1.2); ax.set_ylim(0, 1); ax.axis("off")
    axf.axhline(T, color=GRAY, lw=1.2, ls="--")
    axf.text(n, T + 0.04, f"T = {T}", ha="right", va="bottom", fontsize=12, color=GRAY)
    (run,) = axf.plot([], [], color=TEAL, lw=2.4)
    axf.set_xlim(0, n); axf.set_ylim(0, 0.8); axf.set_yticks([0, 0.4, 0.8])
    axf.set_xlabel("particles detected", fontsize=12); axf.set_ylabel("fraction\non the right", fontsize=11)
    fig.subplots_adjust(left=0.1, right=0.98, top=0.86, bottom=0.17)

    def update(i):
        age = i - t0
        live = (age >= 0) & (age < tdet)
        xr = -L + v * age                                       # position if nothing happened at the barrier
        xs = np.where(xr > 0, np.where(through, xr, -xr), xr)   # past the barrier: carry on, or come back
        col = np.where(xr <= 0, GRAY, np.where(through, TEAL, ORANGE))
        dots.set_offsets(np.c_[xs[live], yj[live]]); dots.set_color(col[live])
        k = int((age >= tdet).sum())                            # detected so far
        lab_l.set_text(f"found on the left: {k - int(through[:k].sum())}")
        lab_r.set_text(f"found on the right: {int(through[:k].sum())}")
        run.set_data(np.arange(1, k + 1), frac[:k])
        axf.set_title(f"fraction on the right after {k} particles: " + (f"{frac[k - 1]:.2f}" if k else "-"),
                      loc="left", fontsize=12)

    ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ T from the wave: incident, reflected and transmitted pieces (still)
@register
def barrier_setup():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    E, V0, a = 0.5, 1.0, 1.0                                    # hbar = m = 1: k = beta = 1, so T = sech^2(1) = 0.42
    k, q = np.sqrt(2 * E), np.sqrt(2 * (V0 - E))
    M = np.array([[1, -1, -1, 0], [-1j * k, -q, q, 0],
                  [0, np.exp(q * a), np.exp(-q * a), -np.exp(1j * k * a)],
                  [0, q * np.exp(q * a), -q * np.exp(-q * a), -1j * k * np.exp(1j * k * a)]])
    r, C, D, t = np.linalg.solve(M, np.array([-1, -1j * k, 0, 0]))
    R, T = abs(r)**2, abs(t)**2
    fig, ax = plt.subplots(figsize=(8, 3.3))
    ax.fill_between([0, a], 0, 1, color=GRAY, alpha=0.3, lw=0)
    ax.plot([-9.5, 0, 0, a, a, 10.5], [0, 0, 1, 1, 0, 0], color="k", lw=2)
    ax.text(a / 2, 1.04, r"$V_0$", ha="center", va="bottom", fontsize=13)
    xl, xr = np.linspace(-9.3, -0.4, 400), np.linspace(a + 0.4, 10.3, 400)
    w = 0.1                                                     # drawn amplitude of a unit wave
    ax.plot(xl, 0.8 + w * np.cos(k * xl), color=TEAL, lw=2.4)
    ax.plot(xl, 0.28 + w * abs(r) * np.cos(-k * xl + np.angle(r)), color=ORANGE, lw=2.4)
    ax.plot(xr, 0.55 + w * abs(t) * np.cos(k * xr + np.angle(t)), color=TEAL, lw=2.4)
    for (x1, x2), y, f, c in (((-7.5, -2.5), 0.62, 1.0, TEAL), ((-2.5, -7.5), 0.1, R, ORANGE), ((3.0, 8.0), 0.37, T, TEAL)):
        ax.annotate("", xy=(x2, y), xytext=(x1, y), arrowprops=dict(
            arrowstyle=f"simple,head_length=0.8,head_width={0.4 + 1.1 * f:.2f},tail_width={0.6 * f:.2f}",
            color=c, alpha=0.75, mutation_scale=22))
    ax.text(-9.3, 0.96, r"incident $e^{ikx}$: flux 1", fontsize=12.5, color=TEAL, va="bottom")
    ax.text(-9.3, 0.42, rf"reflected $r\,e^{{-ikx}}$: $R = |r|^2 = {R:.2f}$", fontsize=12.5, color=ORANGE, va="bottom")
    ax.text(10.3, 0.69, rf"transmitted $t\,e^{{ikx}}$: $T = |t|^2 = {T:.2f}$", fontsize=12.5, color=TEAL,
            va="bottom", ha="right")
    ax.set_xlim(-9.5, 10.5); ax.set_ylim(-0.05, 1.2); ax.axis("off")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.02)
    fig.savefig(f"{OUT}/barrier_setup.png", dpi=200)
    print("wrote", f"{OUT}/barrier_setup.png")
    return fig, None


# ============================================================ deck 3.5 "Operators"
# Page ch03/04 syncs function_vector, difference_stencils, box_grid_states, grid_operators, hermitian_dial
# and order_matters (the first three build the matrix picture step by step before any numpy).

# ------------------------------------------------------------ sample a function at N points: it becomes a vector (still)
@register
def function_vector():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    xs = np.linspace(0, 1, 400)
    f = lambda x: np.sin(np.pi * x) + 0.45 * np.sin(2 * np.pi * x)
    N, h = 7, 1 / 8
    xj = h * np.arange(1, N + 1); fj = f(xj)
    fig = plt.figure(figsize=(9, 3.7))
    gs = fig.add_gridspec(1, 3, width_ratios=[2.6, 0.5, 0.9], wspace=0.05)
    ax, axa, axv = (fig.add_subplot(gs[0, j]) for j in range(3))
    ax.plot(xs, f(xs), color=TEAL, lw=2.6, label=r"$\psi(x)$")
    ax.vlines(xj, 0, fj, color=GRAY, lw=1, ls=":")
    ax.plot(xj, fj, "o", color=CARDINAL, ms=8, zorder=5)
    for j, (xv, fv) in enumerate(zip(xj, fj), start=1):
        ax.text(xv, fv + 0.09, rf"$\psi_{j}$", ha="center", fontsize=12, color=CARDINAL)
    ax.plot([0, 0], [0, 1.55], color="k", lw=2.6); ax.plot([1, 1], [0, 1.55], color="k", lw=2.6)
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.annotate("", xy=(xj[3], -0.14), xytext=(xj[2], -0.14), arrowprops=dict(arrowstyle="<->", color="k", lw=1.2))
    ax.text((xj[2] + xj[3]) / 2, -0.2, r"$h$", ha="center", va="top", fontsize=13)
    ax.set_xlim(-0.03, 1.03); ax.set_ylim(-0.42, 1.6)
    ax.set_xticks(list(xj)); ax.set_xticklabels([rf"$x_{j}$" for j in range(1, N + 1)], fontsize=12)
    ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
    ax.tick_params(length=0)
    ax.set_title(r"a function, sampled at $N$ points spaced $h$ apart", loc="left", fontsize=12.5)
    axa.axis("off")
    axa.annotate("", xy=(0.95, 0.5), xytext=(0.05, 0.5), xycoords="axes fraction",
                 arrowprops=dict(arrowstyle="simple,head_length=0.8,head_width=0.8,tail_width=0.3", color=PURPLE, alpha=0.8))
    axv.axis("off"); axv.set_xlim(0, 1); axv.set_ylim(0, N + 1)
    for j, fv in enumerate(fj, start=1):
        y = N + 0.5 - j
        axv.text(0.5, y, f"{fv:.2f}", ha="center", va="center", fontsize=13,
                 bbox=dict(boxstyle="round,pad=0.25", fc="#fbeaec", ec=CARDINAL, lw=1))
        axv.text(0.02, y, rf"$\psi_{j}$", ha="left", va="center", fontsize=11, color=CARDINAL)
    axv.plot([0.27, 0.22, 0.22, 0.27], [N + 0.35, N + 0.35, 0.15, 0.15], color="k", lw=1.4)
    axv.plot([0.73, 0.78, 0.78, 0.73], [N + 0.35, N + 0.35, 0.15, 0.15], color="k", lw=1.4)
    axv.set_title("a vector", fontsize=12.5)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.88, bottom=0.12)
    fig.savefig(f"{OUT}/function_vector.png", dpi=200)
    print("wrote", f"{OUT}/function_vector.png")
    return fig, None


# ------------------------------------------------------------ derivatives from neighbors: the chord and the change of slope (still)
@register
def difference_stencils():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    f = lambda x: 0.75 + 0.42 * np.sin(1.7 * x - 0.6) + 0.06 * x
    df = lambda x: 0.42 * 1.7 * np.cos(1.7 * x - 0.6) + 0.06
    xs = np.linspace(-0.2, 2.6, 300)
    x0, h = 1.15, 0.55
    pts = np.array([x0 - h, x0, x0 + h]); fp = f(pts)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 4.0), gridspec_kw={"wspace": 0.1})
    for ax in (a1, a2):
        ax.plot(xs, f(xs), color=GRAY, lw=2.2, alpha=0.8)
        ax.plot(pts, fp, "o", color=CARDINAL, ms=9, zorder=5)
        ax.set_xticks(pts); ax.set_xticklabels([r"$x_{j-1}$", r"$x_j$", r"$x_{j+1}$"], fontsize=12.5)
        ax.set_yticks([]); ax.spines["left"].set_visible(False)
        ax.set_xlim(-0.2, 2.6); ax.set_ylim(-0.62, 1.42)
    t = np.array([x0 - 0.62, x0 + 0.62])
    a1.plot(t, fp[1] + df(x0) * (t - x0), color="k", lw=1.6, ls="--", label=r"tangent at $x_j$: slope $\psi'(x_j)$")
    sl = (fp[2] - fp[0]) / (2 * h)
    a1.plot(t, fp[1] + sl * (t - x0), color=PURPLE, lw=2.4, label=r"slope of the chord: $(\psi_{j+1} - \psi_{j-1})/2h$")
    a1.plot([pts[0], pts[2]], [fp[0], fp[2]], color=PURPLE, lw=1.4, ls=":")
    a1.legend(loc="lower center", frameon=False, fontsize=11.5)
    a1.set_title("first derivative: the slope of the chord", loc="left", fontsize=12.5)
    a2.plot(pts[:2], fp[:2], color=ORANGE, lw=2.6, label=r"$s_- = (\psi_j - \psi_{j-1})/h$")
    a2.plot(pts[1:], fp[1:], color=TEAL, lw=2.6, label=r"$s_+ = (\psi_{j+1} - \psi_j)/h$")
    a2.legend(loc="lower left", frameon=False, fontsize=11.5, bbox_to_anchor=(0.0, 0.13))
    a2.text(0.01, 0.02, r"$\psi''(x_j) \approx \dfrac{s_+ - s_-}{h} = \dfrac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{h^2}$",
            transform=a2.transAxes, ha="left", va="bottom", fontsize=12.5)
    a2.set_title("second derivative: how much the slope changes", loc="left", fontsize=12.5)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.91, bottom=0.09)
    fig.savefig(f"{OUT}/difference_stencils.png", dpi=200)
    print("wrote", f"{OUT}/difference_stencils.png")
    return fig, None


# ------------------------------------------------------------ the box on a grid: 3 points already give sampled sines; levels converge from below (still)
@register
def box_grid_states():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    xs = np.linspace(0, 1, 300)                                 # hbar = m = L = 1
    fig = plt.figure(figsize=(9.4, 4.0))
    gs = fig.add_gridspec(3, 3, width_ratios=[1.15, 0.42, 1], hspace=0.25, wspace=0.12)
    N, h = 3, 0.25
    xg = np.array([0, 0.25, 0.5, 0.75, 1.0])
    H = (2 * np.eye(N) - np.eye(N, k=1) - np.eye(N, k=-1)) / (2 * h**2)
    Eg, V = np.linalg.eigh(H)
    for r in range(3):
        ax = fig.add_subplot(gs[r, 0])
        n = r + 1
        v = V[:, r] / np.sqrt(h); v = v * np.sign(v[0])          # normalized as a function, first point positive
        ax.plot(xs, np.sqrt(2) * np.sin(n * np.pi * xs), color=GRAY, lw=1.8, alpha=0.7)
        ax.plot(xg, np.concatenate([[0], v, [0]]), "-o", color=CARDINAL, lw=1.6, ms=7)
        ax.axhline(0, color=GRAY, lw=0.6)
        ax.plot([0, 0], [-1.6, 1.6], color="k", lw=2); ax.plot([1, 1], [-1.6, 1.6], color="k", lw=2)
        ax.set_xlim(-0.03, 1.03); ax.set_ylim(-1.75, 1.75); ax.axis("off")
        axt = fig.add_subplot(gs[r, 1]); axt.axis("off")
        axt.text(0.05, 0.5, rf"$n = {n}$: $E = {Eg[r]:.2f}$" + "\n" + rf"exact: ${(n * np.pi)**2 / 2:.2f}$", fontsize=11.5,
                 va="center", transform=axt.transAxes)
        if r == 0:
            ax.set_title("3 grid points: eigenvectors (dots) vs exact states", loc="left", fontsize=12.5)
    axl = fig.add_subplot(gs[:, 2])
    cols = [(3, CARDINAL), (10, PURPLE), (30, TEAL)]
    for k, (Ng, col) in enumerate(cols):
        hh = 1 / (Ng + 1)
        En = (1 - np.cos(np.arange(1, min(Ng, 4) + 1) * np.pi * hh)) / hh**2
        axl.hlines(En, k - 0.32, k + 0.32, color=col, lw=3)
    Ex = (np.arange(1, 5) * np.pi)**2 / 2
    axl.hlines(Ex, 3 - 0.32, 3 + 0.32, color="k", lw=3)
    for e in Ex:
        axl.axhline(e, color=GRAY, lw=0.6, ls=":", zorder=0)
    axl.set_xticks([0, 1, 2, 3]); axl.set_xticklabels([r"$N = 3$", r"$N = 10$", r"$N = 30$", "exact"], fontsize=12)
    axl.yaxis.tick_right(); axl.yaxis.set_label_position("right")
    axl.spines["left"].set_visible(False); axl.spines["right"].set_visible(True)
    axl.set_ylabel(r"energy  ($\hbar^2/mL^2$)", fontsize=12); axl.tick_params(axis="y", labelsize=11)
    axl.set_xlim(-0.6, 3.6); axl.set_ylim(0, 85)
    axl.set_title("more points: closer to exact", loc="left", fontsize=12.5)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.09)
    fig.subplots_adjust(right=0.93)
    fig.savefig(f"{OUT}/box_grid_states.png", dpi=200)
    print("wrote", f"{OUT}/box_grid_states.png")
    return fig, None

# ------------------------------------------------------------ on a grid, x, p and H are matrices (still)
@register
def grid_operators():
    from matplotlib.colors import LinearSegmentedColormap
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    div = LinearSegmentedColormap.from_list("div", [TEAL, "white", CARDINAL])
    N = 8                                                       # hbar = m = 1, V = x^2/2 on 8 points
    x = np.linspace(-2, 2, N); h = x[1] - x[0]
    up, dn = np.eye(N, k=1), np.eye(N, k=-1)
    X = np.diag(x)
    P = -1j * (up - dn) / (2 * h)                               # p = -i d/dx as a centered difference
    H = -0.5 * (up - 2 * np.eye(N) + dn) / h**2 + np.diag(0.5 * x**2)
    panels = [(X, r"$\hat{x}$", "grid positions on the diagonal\nreal, symmetric"),
              (P.imag, r"$\hat{p}$  (imaginary part)", r"$\mp i\hbar/2h$ next to the diagonal" + "\nimaginary, antisymmetric"),
              (H, r"$\hat{H}$", "$V$ on the diagonal, neighbors linked\nreal, symmetric")]
    fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.8))
    for ax, (M, title, note) in zip(axs, panels):
        m = np.abs(M).max()
        ax.imshow(M, cmap=div, vmin=-m, vmax=m)
        ax.set_xticks(np.arange(-0.5, N, 1), minor=True); ax.set_yticks(np.arange(-0.5, N, 1), minor=True)
        ax.grid(which="minor", color="white", lw=1.5)
        ax.tick_params(which="both", length=0, labelbottom=False, labelleft=False)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_title(title, fontsize=14)
        ax.set_xlabel(note, fontsize=11.5, linespacing=1.4)
    fig.suptitle(r"each matrix equals its conjugate transpose: $A^\dagger = A$", fontsize=13, y=0.98)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.83, bottom=0.17, wspace=0.18)
    fig.savefig(f"{OUT}/grid_operators.png", dpi=200)
    print("wrote", f"{OUT}/grid_operators.png")
    return fig, None


# ------------------------------------------------------------ lose Hermiticity: eigenvalues leave the real axis, overlaps appear
@register
def hermitian_dial():
    from matplotlib.colors import LinearSegmentedColormap
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    wt = LinearSegmentedColormap.from_list("wt", ["white", TEAL])
    rng = np.random.default_rng(3)
    N = 8
    A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    Hm, K = (A + A.conj().T) / 2, (A - A.conj().T) / 2           # Hermitian part plus anti-Hermitian part
    ss = np.concatenate([np.zeros(5), np.linspace(0, 1, 30), np.ones(6)])
    vals, ovl = [], []
    for s in ss:
        w, V = np.linalg.eig(Hm + s * K)
        o = np.argsort(w.real)
        V = V[:, o] / np.linalg.norm(V[:, o], axis=0)
        vals.append(w[o]); ovl.append(np.abs(V.conj().T @ V))
    allv = np.concatenate(vals)
    fig, (ax, axo) = plt.subplots(1, 2, figsize=(8, 3.6), gridspec_kw={"width_ratios": [1.55, 1], "wspace": 0.25})
    ax.axhline(0, color=GRAY, lw=1.2)
    ax.text(allv.real.max() + 0.2, 0.15, "real axis", color=GRAY, fontsize=11, ha="right", va="bottom")
    scat = ax.scatter(vals[0].real, vals[0].imag, s=70, color=TEAL, zorder=5)
    ax.set_xlim(allv.real.min() - 0.5, allv.real.max() + 0.5)
    lim = 1.15 * max(0.5, np.abs(allv.imag).max())
    ax.set_ylim(-lim, lim)
    ax.set_xlabel("Re (eigenvalue)", fontsize=12); ax.set_ylabel("Im (eigenvalue)", fontsize=12)
    img = axo.imshow(ovl[0], cmap=wt, vmin=0, vmax=1)
    axo.set_xticks([]); axo.set_yticks([])
    for sp in axo.spines.values():
        sp.set_visible(False)
    axo.set_title(r"overlaps $|\langle v_j | v_k \rangle|$", fontsize=13)
    fig.subplots_adjust(left=0.09, right=0.98, top=0.84, bottom=0.15)

    def update(i):
        w, s = vals[i], ss[i]
        scat.set_offsets(np.column_stack([w.real, w.imag]))
        scat.set_color([TEAL if abs(v.imag) < 1e-6 else CARDINAL for v in w])
        img.set_data(ovl[i])
        off = (ovl[i] - np.diag(np.diag(ovl[i]))).max()
        ax.set_title(rf"$A = H + s\,K$,  $s = {s:.2f}$:  " + ("eigenvalues real" if s == 0 else f"largest |Im| = {np.abs(w.imag).max():.2f}"),
                     loc="left", fontsize=12.5)
        axo.set_xlabel("eigenvectors orthonormal" if s == 0 else f"largest overlap {off:.2f}", fontsize=12)

    ani = FuncAnimation(fig, update, frames=len(ss), interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ x then p, or p then x: the two orders differ by i hbar psi (still)
@register
def order_matters():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4.5, 4.5, 900); h = x[1] - x[0]          # hbar = 1; psi real, so x p psi and p x psi are imaginary
    funcs = [np.exp(-x**2 / 2) * (1 + 0.5 * x),
             np.exp(-x**2 / 5) * np.cos(2.2 * x) + 0.3 * np.exp(-(x - 1.5)**2)]
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.6))
    for k, (ax, psi) in enumerate(zip(axs, funcs)):
        d = np.gradient(psi, h)
        xp, px = -x * d, -(psi + x * d)                         # (x p psi)/(i hbar) and (p x psi)/(i hbar)
        ax.plot(x, xp, color=TEAL, lw=2.2, label=r"$\hat{x}\hat{p}\,\psi\ /\ i\hbar$")
        ax.plot(x, px, color=ORANGE, lw=2.2, ls="--", label=r"$\hat{p}\hat{x}\,\psi\ /\ i\hbar$")
        ax.plot(x, xp - px, color=CARDINAL, lw=6, alpha=0.4, label=r"difference $/\ i\hbar$")
        ax.plot(x, psi, color="k", lw=1.4, ls=":", label=r"$\psi$ itself")
        ax.axhline(0, color=GRAY, lw=0.6)
        ax.set_xlim(-4.5, 4.5); ax.set_xlabel("x", fontsize=12); ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_title(("a lopsided bump" if k == 0 else "a wiggly packet"), loc="left", fontsize=12.5)
    fig.legend(*axs[0].get_legend_handles_labels(), loc="upper center", ncol=4, frameon=False, fontsize=11.5,
               bbox_to_anchor=(0.5, 0.9), handlelength=2.2, columnspacing=1.6)
    fig.suptitle(r"the difference of the two orders is $\psi$ itself:  $[\hat{x},\hat{p}]\,\psi = i\hbar\,\psi$", fontsize=13.5, y=0.99)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.72, bottom=0.14, wspace=0.08)
    fig.savefig(f"{OUT}/order_matters.png", dpi=200)
    print("wrote", f"{OUT}/order_matters.png")
    return fig, None


# ============================================================ deck 3.5b "Hermitian operators and commutators"
# Deck stills for slides/ch03/05b (commutator_steps is also used by deck 05). When the pages are split, page ch03/04
# may sync matrix_arrows and the new Hermitian page flip_swap and commutator_steps (in place of order_matters);
# eigen_directions stays deck-only if the page gets the widget.

# ------------------------------------------------------------ a matrix turns most arrows; eigenvectors only stretch (still)
@register
def matrix_arrows():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    A = np.array([[2.0, 1.0], [1.0, 2.0]])
    arrow = lambda ax, tip, col, lw, z: ax.annotate("", xy=tip, xytext=(0, 0), zorder=z, arrowprops=dict(
        arrowstyle="-|>", color=col, lw=lw, mutation_scale=22, shrinkA=0, shrinkB=0))
    t = np.linspace(0, 2 * np.pi, 300)
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 4.2))
    for ax in axs:
        ax.plot(np.cos(t), np.sin(t), color=GRAY, lw=1, ls=":")
        ax.axhline(0, color=GRAY, lw=0.8); ax.axvline(0, color=GRAY, lw=0.8)
        ax.set_xlim(-1.3, 2.75); ax.set_ylim(-1.15, 2.5); ax.set_aspect("equal"); ax.axis("off")
    a = axs[0]                                                  # a generic arrow: turned and stretched
    v = np.array([1.0, 0.0]); Av = A @ v
    arrow(a, v, TEAL, 3, 3); arrow(a, Av, CARDINAL, 3, 3)
    a.text(1.0, -0.12, r"$\mathbf{v} = (1, 0)$", color=TEAL, fontsize=15, ha="center", va="top")
    a.text(2.0, 1.12, r"$A\mathbf{v} = (2, 1)$", color=CARDINAL, fontsize=15, ha="center", va="bottom")
    a.set_title("a generic arrow turns", fontsize=15)
    b = axs[1]                                                  # the eigenvectors: only stretched
    u1 = np.array([1.0, 1.0]) / np.sqrt(2); u2 = np.array([1.0, -1.0]) / np.sqrt(2)
    b.plot([-1.0, 2.45], [-1.0, 2.45], color=CARDINAL, lw=0.8, ls="--", alpha=0.5, zorder=1)
    b.plot([-0.95, 1.0], [0.95, -1.0], color=CARDINAL, lw=0.8, ls="--", alpha=0.5, zorder=1)
    arrow(b, A @ u1, CARDINAL, 3, 2); arrow(b, u1, TEAL, 3.4, 3)
    arrow(b, A @ u2, CARDINAL, 7, 2); arrow(b, u2, TEAL, 2.6, 3)
    b.text(1.95, 2.12, r"$A\mathbf{u}_1 = 3\,\mathbf{u}_1$", color=CARDINAL, fontsize=15, ha="right", va="center")
    b.text(0.2, 0.68, r"$\mathbf{u}_1$", color=TEAL, fontsize=15, ha="right")
    b.text(0.85, -0.78, r"$A\mathbf{u}_2 = \mathbf{u}_2$", color=CARDINAL, fontsize=15, ha="left", va="center")
    b.set_title("eigenvectors only stretch", fontsize=15)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.02, wspace=0.05)
    fig.savefig(f"{OUT}/matrix_arrows.png", dpi=200)
    print("wrote", f"{OUT}/matrix_arrows.png")
    return fig, None


# ------------------------------------------------------------ eigen-directions: perpendicular, skewed, or none at all (still)
@register
def eigen_directions():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    t = np.linspace(0, 2 * np.pi, 400); circ = np.array([np.cos(t), np.sin(t)])
    arrow = lambda ax, tip, col, lw: ax.annotate("", xy=tip, xytext=(0, 0), arrowprops=dict(
        arrowstyle="-|>", color=col, lw=lw, mutation_scale=16, shrinkA=0, shrinkB=0))
    mats = [(np.array([[2.0, 1.0], [1.0, 2.0]]), r"$\binom{2\ \ 1}{1\ \ 2}$", "symmetric"),
            (np.array([[1.0, 1.0], [0.0, 2.0]]), r"$\binom{1\ \ 1}{0\ \ 2}$", "not symmetric"),
            (np.array([[0.0, 1.0], [-1.0, 0.0]]), r"$\left(\genfrac{}{}{0}{}{\ \ 0\quad 1}{-1\ \ \ 0}\right)$", "a rotation")]   # = the two-point d/dx = FS
    notes = ["eigen-directions at 90°", "eigen-directions at 45°", "every arrow turns 90° clockwise:\nno eigen-direction"]
    fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.9))
    for k, (ax, (M, lab, title)) in enumerate(zip(axs, mats)):
        ax.plot(*circ, color=GRAY, lw=1, ls=":")
        ax.axhline(0, color=GRAY, lw=0.6); ax.axvline(0, color=GRAY, lw=0.6)
        w, V = np.linalg.eig(M)
        if k < 2:
            for j in range(2):
                d = V[:, j].real / np.linalg.norm(V[:, j].real); d = d if d[0] >= 0 else -d
                ax.plot([-2.6 * d[0], 2.6 * d[0]], [-2.6 * d[1], 2.6 * d[1]], color=TEAL, lw=2.4, ls="--")
                ax.text(*(2.75 * d), rf"$\lambda = {w[j].real:.0f}$", color=TEAL, fontsize=13,
                        ha="left", va="bottom" if d[1] >= 0 else "top")
        else:
            for deg in (20, 235):                                # turned clockwise to 290 and 145 degrees, clear of the originals
                vv = 1.6 * np.array([np.cos(np.radians(deg)), np.sin(np.radians(deg))])
                arrow(ax, vv, TEAL, 2.6); arrow(ax, M @ vv, CARDINAL, 2.6)
                arc = np.radians(np.linspace(deg - 8, deg - 80, 30))
                ax.plot(0.75 * np.cos(arc), 0.75 * np.sin(arc), color=CARDINAL, lw=1.3)
                ax.annotate("", xy=(0.75 * np.cos(np.radians(deg - 86)), 0.75 * np.sin(np.radians(deg - 86))),
                            xytext=(0.75 * np.cos(arc[-1]), 0.75 * np.sin(arc[-1])),
                            arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.3, mutation_scale=12))
        ax.set_xlim(-2.9, 3.6); ax.set_ylim(-2.9, 2.9); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=14.5)
        ax.text(0.0, 0.98, lab, transform=ax.transAxes, fontsize=15, va="top")
        ax.text(0.5, -0.02, notes[k], transform=ax.transAxes, fontsize=13, ha="center", va="top",
                color=CARDINAL if k == 2 else "k")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.17, wspace=0.08)
    fig.savefig(f"{OUT}/eigen_directions.png", dpi=200)
    print("wrote", f"{OUT}/eigen_directions.png")
    return fig, None


# ------------------------------------------------------------ flip then swap, or swap then flip: opposite turns (still)
@register
def flip_swap():
    from matplotlib.patches import FancyArrowPatch
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    F = np.array([[1.0, 0.0], [0.0, -1.0]])                    # flip: mirror in the x axis
    S = np.array([[0.0, 1.0], [1.0, 0.0]])                     # swap: mirror in the line y = x
    strokes = [np.array([[0.25, 0.2], [0.25, 1.0]]), np.array([[0.25, 1.0], [0.8, 1.0]]),
               np.array([[0.25, 0.6], [0.65, 0.6]])]          # the letter F, each stroke as rows [x, y]
    draw = lambda ax, M, col, lw, ls, alpha: [ax.plot(*(M @ s.T), color=col, lw=lw, ls=ls, alpha=alpha,
                                                      solid_capstyle="round") for s in strokes]
    fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.7))
    panels = [(None, None, "start", ""),
              (S, F @ S, r"swap, then flip:  $F\,S$", "turned 90° clockwise"),
              (F, S @ F, r"flip, then swap:  $S\,F$", "turned 90° counterclockwise")]
    for ax, (M1, M2, title, note) in zip(axs, panels):
        ax.axhline(0, color=GRAY, lw=0.8); ax.axvline(0, color=GRAY, lw=0.8)
        draw(ax, np.eye(2), TEAL, 7, "-", 1.0 if M1 is None else 0.3)
        if M1 is not None:
            draw(ax, M1, GRAY, 3.5, (0, (1.5, 2.5)), 0.8)      # after the first step
            draw(ax, M2, CARDINAL, 7, "-", 1.0)                 # after both steps
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=14.5)
        ax.text(0.5, -0.02, note, transform=ax.transAxes, fontsize=13, ha="center", va="top", color=CARDINAL)
    for ax, (a0, a1) in ((axs[1], (78, -12)), (axs[2], (72, 162))):   # the net turn, drawn outside the letters
        arc = np.radians(np.linspace(a0, a1, 60))
        ax.plot(1.38 * np.cos(arc), 1.38 * np.sin(arc), color=CARDINAL, lw=1.6)
        ax.add_patch(FancyArrowPatch((1.38 * np.cos(arc[-4]), 1.38 * np.sin(arc[-4])), (1.38 * np.cos(arc[-1]), 1.38 * np.sin(arc[-1])),
                                     arrowstyle="-|>", mutation_scale=18, color=CARDINAL, lw=1.6))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.12, wspace=0.08)
    fig.savefig(f"{OUT}/flip_swap.png", dpi=200)
    print("wrote", f"{OUT}/flip_swap.png")
    return fig, None


# ------------------------------------------------------------ [x, d/dx] in three steps: f, the two orders, their difference (still)
@register
def commutator_steps():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4.5, 4.5, 900); h = x[1] - x[0]
    f = np.exp(-x**2 / 2) * (1 + 0.5 * x)                       # any smooth test function
    fp = np.gradient(f, h)
    xfp, dxf = x * fp, f + x * fp                                # x f'  and  (x f)' = f + x f'
    fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.5), sharey=True)
    for ax in axs:
        ax.axhline(0, color=GRAY, lw=0.7)
        ax.set_xlim(-4, 4); ax.set_ylim(-1.35, 1.45); ax.set_xticks([]); ax.set_yticks([])
        ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
    axs[0].plot(x, f, color="k", lw=2.6)
    axs[0].text(1.3, 1.05, r"$f$", fontsize=16)
    axs[0].set_title("1.  a test function", loc="left", fontsize=14)
    axs[1].plot(x, xfp, color=TEAL, lw=2.6, label=r"$x\,f'$:  differentiate, then multiply by $x$")
    axs[1].plot(x, dxf, color=ORANGE, lw=2.6, ls="--", label=r"$(x f)'$:  multiply by $x$, then differentiate")
    axs[1].set_title("2.  the two orders differ", loc="left", fontsize=14)
    axs[1].legend(loc="lower center", frameon=False, fontsize=11.5, bbox_to_anchor=(0.5, -0.32))
    axs[2].plot(x, xfp - dxf, color=CARDINAL, lw=7, alpha=0.45, label=r"$x f' - (x f)'$")
    axs[2].plot(x, -f, color="k", lw=1.8, ls=":", label=r"$-f$")
    axs[2].set_title(r"3.  their difference is $-f$", loc="left", fontsize=14)
    axs[2].legend(loc="lower center", frameon=False, fontsize=12, ncol=2, bbox_to_anchor=(0.5, -0.24))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.2, wspace=0.08)
    fig.savefig(f"{OUT}/commutator_steps.png", dpi=200)
    print("wrote", f"{OUT}/commutator_steps.png")
    return fig, None


# ============================================================ deck 3.6 "Measurement: eigenvalues and expectation values"
# Page ch03/05 syncs projection, sine_series, collapse, box_momentum and uncertainty_tradeoff. measure_energy is
# deck-only: the page measures with the JS widget widgets/measure_energy.mjs instead (same state, same story).

# ------------------------------------------------------------ a coefficient is a projection: vector onto axes, function onto psi_n (still)
@register
def projection():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 400)
    psi = np.sqrt(30) * x * (1 - x)                             # the state of the worked example, L = 1
    fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.3), gridspec_kw={"width_ratios": [0.85, 1, 1], "wspace": 0.28})
    ax = axs[0]
    for e, lab, ofs in (((1, 0), r"$\hat{e}_1$", (0.5, -0.32)), ((0, 1), r"$\hat{e}_2$", (-0.42, 0.45))):
        ax.annotate("", xy=e, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=2))
        ax.text(*ofs, lab, color=GRAY, fontsize=13)
    ax.annotate("", xy=(3, 2), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2.6, mutation_scale=18))
    ax.text(3.08, 2.08, r"$\mathbf{v}$", color=TEAL, fontsize=15)
    ax.plot([3, 3], [0, 2], color=PURPLE, ls="--", lw=1.4); ax.plot([0, 3], [2, 2], color=PURPLE, ls="--", lw=1.4)
    ax.text(3, -0.22, r"$c_1 = \langle \hat{e}_1|\mathbf{v}\rangle = 3$", color=PURPLE, fontsize=12, ha="center", va="top")
    ax.text(-0.15, 2, r"$c_2 = 2$", color=PURPLE, fontsize=12, ha="right", va="center")
    ax.set_xlim(-1.3, 3.8); ax.set_ylim(-0.95, 2.6); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title("a vector: project onto the axes", loc="left", fontsize=12)
    for ax, n in ((axs[1], 1), (axs[2], 2)):
        phi = np.sqrt(2) * np.sin(n * np.pi * x)
        prod = phi * psi
        c = np.trapezoid(prod, x)
        ax.fill_between(x, prod, where=prod >= 0, color=PURPLE, alpha=0.25, lw=0, interpolate=True)
        ax.fill_between(x, prod, where=prod < 0, color=ORANGE, alpha=0.3, lw=0, interpolate=True)
        ax.plot(x, psi, color=TEAL, lw=2.4, label=r"the state $\psi$")
        ax.plot(x, phi, color=GRAY, lw=1.6, ls="--", label=r"box state $\psi_n$")
        ax.plot(x, prod, color=PURPLE, lw=1.2, label=r"product $\psi_n\psi$")
        ax.axhline(0, color=GRAY, lw=0.6)
        ax.set_xlim(0, 1); ax.set_ylim(-1.75, 2.35); ax.set_yticks([])
        ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"], fontsize=11)
        ax.spines["left"].set_visible(False)
        ax.set_title(rf"$c_{n} = \int \psi_{n}\,\psi\,dx = {abs(c):.3f}$" if n == 1 else r"$c_2 = 0$: the two lobes cancel",
                     loc="left", fontsize=12)
    axs[2].legend(loc="lower left", frameon=False, fontsize=10.5, handlelength=1.6, borderaxespad=0.1)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.1)
    fig.savefig(f"{OUT}/projection.png", dpi=200)
    print("wrote", f"{OUT}/projection.png")
    return fig, None


# ------------------------------------------------------------ a narrow packet needs many box states: partial sums and |c_n|^2
@register
def sine_series():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 600)
    psi = np.exp(-(x - 0.3)**2 / (4 * 0.045**2))               # |psi|^2 has width 0.045 L
    psi = psi / np.sqrt(np.trapezoid(psi**2, x))
    ns = np.arange(1, 31)
    phis = np.sqrt(2) * np.sin(np.outer(ns, np.pi * x))
    c = np.trapezoid(phis * psi, x, axis=1)
    ks = np.concatenate([np.arange(1, 25), np.full(6, 24)])
    fig, (ax, axb) = plt.subplots(2, 1, figsize=(8, 4.4), gridspec_kw={"height_ratios": [1.5, 1], "hspace": 0.55})
    ax.plot(x, psi, color="k", lw=1.4, ls=":", label=r"the state $\psi$")
    (part,) = ax.plot([], [], color=TEAL, lw=2.4, label=r"sum of the first $k$ terms $c_n\psi_n$")
    band = [ax.fill_between(x, 0 * x, color=TEAL, alpha=0.15, lw=0)]
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(0, 1); ax.set_ylim(-1.6, 3.6); ax.set_yticks([])
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"], fontsize=12)
    ax.spines["left"].set_visible(False)
    ax.legend(loc="upper right", frameon=False, fontsize=12)
    bars = axb.bar(ns, c**2, color="#d9dde1", width=0.75)
    axb.set_xlim(0.3, 30.7); axb.set_ylim(0, 1.15 * (c**2).max())
    axb.set_xlabel(r"$n$", fontsize=12); axb.set_ylabel(r"$|c_n|^2$", fontsize=12)
    axb.set_yticks([0, 0.1]); axb.tick_params(labelsize=11)
    fig.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.12)

    def update(i):
        k = ks[i]
        s = c[:k] @ phis[:k]
        part.set_data(x, s)
        band[0].remove(); band[0] = ax.fill_between(x, s, color=TEAL, alpha=0.15, lw=0)
        for j, b in enumerate(bars):
            b.set_color(TEAL if j < k else "#d9dde1")
        ax.set_title(rf"$k = {k}$ box states", loc="left", fontsize=13)
        axb.set_title(f"the first {k} states hold probability {np.sum(c[:k]**2):.3f}", loc="left", fontsize=12.5)

    ani = FuncAnimation(fig, update, frames=len(ks), interval=140, blit=False)
    return fig, ani


# ------------------------------------------------------------ repeated energy readings: histogram -> |c_n|^2, mean -> <E> (deck GIF)
@register
def measure_energy():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    p, E = np.array([0.25, 0.25, 0.5]), np.array([1, 4, 9])    # psi = (psi1 + psi2 + sqrt2 psi3)/2, E in units of E1
    rng = np.random.default_rng(11)
    reads = rng.choice(E, size=3000, p=p)
    counts = np.unique(np.round(np.geomspace(1, 3000, 40)).astype(int))
    run = np.cumsum(reads) / np.arange(1, 3001)
    Eavg = p @ E
    fig, (axh, axm) = plt.subplots(1, 2, figsize=(8, 3.6), gridspec_kw={"width_ratios": [1, 1.25], "wspace": 0.32})
    bars = axh.bar([1, 2, 3], [0, 0, 0], width=0.6, color=TEAL, alpha=0.75, label="fraction of readings")
    axh.plot([1, 2, 3], p, "_", color=CARDINAL, ms=34, mew=3, label=r"$|c_n|^2$")
    axh.set_xticks([1, 2, 3]); axh.set_xticklabels([r"$E_1$", r"$4E_1$", r"$9E_1$"], fontsize=13)
    axh.set_ylim(0, 0.75); axh.set_yticks([0, 0.25, 0.5]); axh.tick_params(labelsize=11)
    axh.legend(loc="upper left", frameon=False, fontsize=11.5)
    (line,) = axm.plot([], [], color=TEAL, lw=2.2, label="mean of the readings")
    axm.axhline(Eavg, color=CARDINAL, lw=1.8, ls="--", label=rf"$\langle E\rangle = \sum p_n E_n = {Eavg:.2f}\,E_1$")
    axm.set_xscale("log"); axm.set_xlim(1, 3000); axm.set_ylim(0, 10)
    axm.set_xlabel("number of readings", fontsize=12); axm.set_ylabel(r"energy $/\,E_1$", fontsize=12)
    axm.tick_params(labelsize=11)
    axm.legend(loc="upper right", frameon=False, fontsize=11.5)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.84, bottom=0.17)

    def update(i):
        N = counts[i]
        f = np.array([(reads[:N] == e).mean() for e in E])
        for b, h in zip(bars, f):
            b.set_height(h)
        line.set_data(np.arange(1, N + 1), run[:N])
        axh.set_title(f"{N} reading" + ("" if N == 1 else "s") + rf": each one is $E_1$, $4E_1$ or $9E_1$",
                      loc="left", fontsize=12.5)

    ani = FuncAnimation(fig, update, frames=len(counts), interval=160, blit=False)
    return fig, ani


# ------------------------------------------------------------ what one measurement does: the state collapses to the eigenstate it reported (still)
@register
def collapse():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 400)
    ph = [np.sqrt(2) * np.sin(n * np.pi * x) for n in (1, 2, 3, 4)]
    before = np.array([0.5, 0.5, np.sqrt(0.5), 0])
    after = np.array([0, 0, 1.0, 0])
    fig = plt.figure(figsize=(8.6, 3.9))
    gs = fig.add_gridspec(2, 3, width_ratios=[1, 0.42, 1], height_ratios=[1.1, 1], hspace=0.35, wspace=0.05)
    for col, cs, title in ((0, before, r"before: $\psi = \frac{1}{2}\psi_1 + \frac{1}{2}\psi_2 + \frac{1}{\sqrt{2}}\psi_3$"),
                           (2, after, r"after: $\psi = \psi_3$")):
        ax, axb = fig.add_subplot(gs[0, col]), fig.add_subplot(gs[1, col])
        w = sum(ci * p for ci, p in zip(cs, ph))
        ax.fill_between(x, w**2, color=CARDINAL, alpha=0.15, lw=0)
        ax.plot(x, w, color=TEAL, lw=2.4); ax.plot(x, w**2, color=CARDINAL, lw=1.6)
        ax.axhline(0, color=GRAY, lw=0.6); ax.set_xlim(0, 1); ax.set_ylim(-2.2, 4.3)
        ax.set_xticks([]); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
        ax.set_title(title, loc="left", fontsize=12)
        axb.bar([1, 2, 3, 4], cs**2, color=TEAL, width=0.6)
        axb.set_xticks([1, 2, 3, 4]); axb.set_xticklabels([r"$E_1$", r"$4E_1$", r"$9E_1$", r"$16E_1$"], fontsize=12)
        axb.set_ylim(0, 1.08); axb.set_yticks([0, 0.5, 1]); axb.tick_params(axis="y", labelsize=10.5)
        if col == 0:
            axb.set_ylabel("probability", fontsize=11)
        else:
            axb.set_yticklabels([])
    axm = fig.add_subplot(gs[:, 1]); axm.axis("off")
    axm.annotate("", xy=(0.95, 0.55), xytext=(0.05, 0.55), xycoords="axes fraction",
                 arrowprops=dict(arrowstyle="simple,head_length=0.9,head_width=0.9,tail_width=0.35", color=PURPLE, alpha=0.8))
    axm.text(0.5, 0.68, "measure $E$", ha="center", fontsize=12.5, color=PURPLE)
    axm.text(0.5, 0.49, "reading: $9E_1$", ha="center", va="top", fontsize=12.5, color=PURPLE)
    fig.text(0.5, 0.01, r"measuring again right away gives $9E_1$ every time; a fresh copy of the old state gives $E_1$, $4E_1$ or $9E_1$",
             ha="center", fontsize=11.5, color=GRAY)
    fig.subplots_adjust(left=0.06, right=0.99, top=0.9, bottom=0.14)
    fig.savefig(f"{OUT}/collapse.png", dpi=200)
    print("wrote", f"{OUT}/collapse.png")
    return fig, None


# ------------------------------------------------------------ momentum of a box state: two humps near +-n pi hbar/L, never one sharp value (still)
@register
def box_momentum():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 2000)                                 # L = hbar = 1: p in units of pi hbar / L
    p = np.linspace(-8, 8, 800)
    kern = np.exp(-1j * np.outer(p * np.pi, x)) / np.sqrt(2 * np.pi)
    fig, axs = plt.subplots(3, 1, figsize=(8, 4.6), sharex=True, gridspec_kw={"hspace": 0.45})
    for ax, n, col in zip(axs, (1, 2, 5), (TEAL, PURPLE, CARDINAL)):
        amp = np.trapezoid(kern * np.sqrt(2) * np.sin(n * np.pi * x), x, axis=1)
        dens = np.abs(amp)**2 * np.pi                           # density per unit of p / (pi hbar / L)
        ax.fill_between(p, dens, color=col, alpha=0.2, lw=0); ax.plot(p, dens, color=col, lw=2.2)
        for s in (-n, n):
            ax.axvline(s, color=GRAY, lw=1, ls="--")
        ax.set_yticks([]); ax.spines["left"].set_visible(False)
        ax.set_ylim(0, 1.15 * dens.max())
        ax.set_title(rf"$n = {n}$:  dashed lines at $p = \pm\sqrt{{2mE_{n}}} = \pm {n}\,\pi\hbar/L$", loc="left", fontsize=12)
    axs[-1].set_xlabel(r"momentum $p$  (units of $\pi\hbar/L$)", fontsize=12)
    axs[-1].tick_params(labelsize=11)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.93, bottom=0.12)
    fig.savefig(f"{OUT}/box_momentum.png", dpi=200)
    print("wrote", f"{OUT}/box_momentum.png")
    return fig, None


# ------------------------------------------------------------ squeeze a Gaussian: x narrows, p widens, the product stays at hbar/2
@register
def uncertainty_tradeoff():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    nf = 40
    sx = np.exp(np.log(1.4) + (np.log(0.3) - np.log(1.4)) * 0.5 * (1 - np.cos(2 * np.pi * np.arange(nf) / nf)))
    x = np.linspace(-4, 4, 500)                                 # hbar = 1
    fig = plt.figure(figsize=(9, 3.4))
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.05], wspace=0.35)
    axx, axp, axu = (fig.add_subplot(gs[0, j]) for j in range(3))
    (lx,) = axx.plot([], [], color=TEAL, lw=2.4); bx = [axx.fill_between(x, 0 * x, color=TEAL, alpha=0.2, lw=0)]
    (lp,) = axp.plot([], [], color=CARDINAL, lw=2.4); bp = [axp.fill_between(x, 0 * x, color=CARDINAL, alpha=0.2, lw=0)]
    for ax, lab in ((axx, r"position $x$"), (axp, r"momentum $p$")):
        ax.set_xlim(-4, 4); ax.set_ylim(0, 1.45); ax.set_yticks([]); ax.spines["left"].set_visible(False)
        ax.set_xlabel(lab, fontsize=12); ax.tick_params(labelsize=10.5)
    dx = np.geomspace(0.08, 3, 200)
    axu.fill_between(dx, 0.04, 0.5 / dx, color=GRAY, alpha=0.25, lw=0)
    axu.plot(dx, 0.5 / dx, color="k", lw=1.6)
    axu.plot(dx, 0.568 / dx, color=PURPLE, lw=1.4, ls="--")
    axu.text(0.1, 0.35, "forbidden:\n" + r"$\Delta x\,\Delta p < \hbar/2$", fontsize=11, color=GRAY, va="bottom")
    (gdot,) = axu.plot([], [], "o", color=TEAL, ms=10, zorder=5, label=r"Gaussian: $\Delta x\Delta p = 0.50\,\hbar$")
    (bdot,) = axu.plot([], [], "s", color=PURPLE, ms=9, zorder=5, label=r"box ground state: $0.57\,\hbar$")
    axu.set_xscale("log"); axu.set_yscale("log"); axu.set_xlim(0.08, 3); axu.set_ylim(0.04, 12)
    axu.set_xlabel(r"$\Delta x$", fontsize=12); axu.set_ylabel(r"$\Delta p$", fontsize=12); axu.tick_params(labelsize=10)
    axu.legend(loc="upper right", frameon=False, fontsize=10.5, handletextpad=0.3, borderaxespad=0.1)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.86, bottom=0.17)

    def update(i):
        s = sx[i]; sp = 0.5 / s
        rx = np.exp(-x**2 / (2 * s**2)) / np.sqrt(2 * np.pi * s**2)
        rp = np.exp(-x**2 / (2 * sp**2)) / np.sqrt(2 * np.pi * sp**2)
        lx.set_data(x, rx); bx[0].remove(); bx[0] = axx.fill_between(x, rx, color=TEAL, alpha=0.2, lw=0)
        lp.set_data(x, rp); bp[0].remove(); bp[0] = axp.fill_between(x, rp, color=CARDINAL, alpha=0.2, lw=0)
        axx.set_title(rf"$|\psi(x)|^2$:  $\Delta x = {s:.2f}$", loc="left", fontsize=12.5)
        axp.set_title(rf"$|\phi(p)|^2$:  $\Delta p = {sp:.2f}$", loc="left", fontsize=12.5)
        gdot.set_data([s], [sp]); bdot.set_data([s], [0.568 / s])
        axu.set_title(rf"$\Delta x\,\Delta p = {s * sp:.2f}\,\hbar$", loc="left", fontsize=12.5)

    ani = FuncAnimation(fig, update, frames=nf, interval=120, blit=False)
    return fig, ani


# ============================================================ deck 3.7 "Time dependence"
# Page ch03/06 syncs evolve_recipe, free_spread, ehrenfest_wells, bohr_spectrum, box_revival and morse_revival.
# Stationary states (phase_clock), the two-state slosh (box_slosh) and ammonia (ammonia_flip) are shown in
# 3.1, 3.2 and 3.4; the page links back to them instead of animating them again.

# ------------------------------------------------------------ the recipe: three clocks of fixed length drive |Psi|^2 and <x>
@register
def evolve_recipe():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 400)                                  # box, L = hbar = 1, E_n = n^2 E1 with E1 = 1
    c = np.array([0.5, 0.5, np.sqrt(0.5)])                      # the state of the Measurement lecture
    ns = np.array([1, 2, 3])
    phis = np.sqrt(2) * np.sin(np.outer(ns, np.pi * x))
    nf = 44
    ts = np.linspace(0, 2 * np.pi, nf, endpoint=False)          # one full period T = 2 pi hbar / E1
    tt = np.linspace(0, 2 * np.pi, 500)
    amp = lambda t: (c * np.exp(-1j * ns**2 * t)) @ phis
    xbar = np.array([np.trapezoid(x * np.abs(amp(t))**2, x) for t in tt])
    th = np.linspace(0, 2 * np.pi, 200)
    fig = plt.figure(figsize=(8.4, 4.4))
    gs = fig.add_gridspec(3, 2, width_ratios=[2.5, 1], height_ratios=[1, 1, 1], hspace=0.55, wspace=0.12)
    ax = fig.add_subplot(gs[0:2, 0]); axx = fig.add_subplot(gs[2, 0])
    (dens,) = ax.plot([], [], color=CARDINAL, lw=2.6)
    band = [ax.fill_between(x, 0 * x, color=CARDINAL, alpha=0.16, lw=0)]
    (mark,) = ax.plot([], [], marker="^", color=PURPLE, ms=13, ls="none", zorder=6)
    ax.plot([0, 0, 1, 1], [5.4, 0, 0, 5.4], color="k", lw=2.6)
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(0, 5.4); ax.set_xticks([]); ax.set_yticks([])
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
    axx.plot(tt / (2 * np.pi), xbar, color=PURPLE, lw=1, alpha=0.25)
    (trace,) = axx.plot([], [], color=PURPLE, lw=2.4); (dot,) = axx.plot([], [], "o", color=PURPLE, ms=7)
    axx.axhline(0.5, color=GRAY, lw=0.8, ls=":")
    axx.set_xlim(0, 1); axx.set_ylim(0.2, 0.8); axx.set_yticks([0.25, 0.5, 0.75]); axx.set_yticklabels(["L/4", "L/2", "3L/4"])
    axx.set_xticks([0, 0.25, 0.5, 0.75, 1]); axx.set_xticklabels(["0", "T/4", "T/2", "3T/4", "T"])
    axx.tick_params(labelsize=11); axx.set_title(r"$\langle x\rangle(t)$", loc="left", fontsize=12.5, color=PURPLE)
    hands = []
    for r, (n, cn, col) in enumerate(zip(ns, c, (TEAL, ORANGE, CARDINAL))):
        axc = fig.add_subplot(gs[r, 1])
        axc.plot(np.cos(th), np.sin(th), color=GRAY, lw=0.8, ls="--")
        (hd,) = axc.plot([], [], color=col, lw=3.2); (tp,) = axc.plot([], [], "o", color=col, ms=6)
        axc.set_aspect("equal"); axc.set_xlim(-1.1, 1.1); axc.set_ylim(-1.1, 1.1); axc.axis("off")
        axc.text(1.25, 0, rf"$n = {n}$" + "\n" + rf"$|c_{n}|^2 = {cn**2:.2f}$" + "\n" + (r"$E_1$" if n == 1 else rf"${n * n}E_1$"),
                 fontsize=11, va="center", color=col)
        hands.append((hd, tp, n, cn / c.max()))
    fig.subplots_adjust(left=0.08, right=0.9, top=0.93, bottom=0.08)

    def update(i):
        t = ts[i]
        d = np.abs(amp(t))**2
        dens.set_data(x, d)
        band[0].remove(); band[0] = ax.fill_between(x, d, color=CARDINAL, alpha=0.16, lw=0)
        xm = np.trapezoid(x * d, x)
        mark.set_data([xm], [0.25])
        k = int(round(t / (2 * np.pi) * (len(tt) - 1)))
        trace.set_data(tt[:k + 1] / (2 * np.pi), xbar[:k + 1]); dot.set_data([t / (2 * np.pi)], [xm])
        for hd, tp, n, ln in hands:
            z = ln * np.exp(-1j * n * n * t)
            hd.set_data([0, z.real], [0, z.imag]); tp.set_data([z.real], [z.imag])
        ax.set_title(rf"$|\Psi(x,t)|^2$ at $t = {t / (2 * np.pi):.2f}\,T$   (" + "\u25b2" + r" marks $\langle x\rangle$)", loc="left", fontsize=12.5)

    ani = FuncAnimation(fig, update, frames=nf, interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ a free packet spreads in x while its momentum distribution never changes
@register
def free_spread():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-25, 45, 2048, endpoint=False); dx = x[1] - x[0]   # hbar = m = 1
    k = 2 * np.pi * np.fft.fftfreq(x.size, d=dx)
    s0, k0 = 0.8, 2.5                                           # |psi|^2 starts with width s0 and moves at speed k0
    psi0 = np.exp(-x**2 / (4 * s0**2) + 1j * k0 * x); psi0 = psi0 / np.sqrt(np.sum(np.abs(psi0)**2) * dx)
    f0 = np.fft.fft(psi0)
    nf = 36
    ts = np.linspace(0, 7, nf)
    p = np.linspace(-0.5, 5.5, 400)
    php = np.exp(-(p - k0)**2 * 2 * s0**2); php = php / np.trapezoid(php, p)
    fig, (ax, axp) = plt.subplots(2, 1, figsize=(8, 4.2), gridspec_kw={"height_ratios": [1.6, 1], "hspace": 0.6})
    (lx,) = ax.plot([], [], color=TEAL, lw=2.4); bx = [ax.fill_between(x, 0 * x, color=TEAL, alpha=0.2, lw=0)]
    (cl,) = ax.plot([], [], "o", color=PURPLE, ms=9, zorder=5, label=r"classical particle, $x = p_0t/m$")
    ax.set_xlim(-6, 22); ax.set_ylim(0, 0.56); ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.set_xlabel(r"position $x$", fontsize=12); ax.tick_params(labelsize=11)
    ax.legend(loc="upper right", frameon=False, fontsize=11.5)
    axp.fill_between(p, php, color=CARDINAL, alpha=0.2, lw=0); axp.plot(p, php, color=CARDINAL, lw=2.4)
    axp.set_xlim(-0.5, 5.5); axp.set_yticks([]); axp.spines["left"].set_visible(False)
    axp.set_xlabel(r"momentum $p$", fontsize=12); axp.tick_params(labelsize=11)
    axp.set_title(r"$|\phi(p)|^2$: the same at every $t$, because $[\hat{p},\hat{H}] = 0$", loc="left", fontsize=12.5)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.9, bottom=0.13)

    def update(i):
        t = ts[i]
        d = np.abs(np.fft.ifft(f0 * np.exp(-0.5j * k**2 * t)))**2
        lx.set_data(x, d); bx[0].remove(); bx[0] = ax.fill_between(x, d, color=TEAL, alpha=0.2, lw=0)
        cl.set_data([k0 * t], [0.02])
        sx = s0 * np.sqrt(1 + (t / (2 * s0**2))**2)
        ax.set_title(rf"$|\Psi(x,t)|^2$ at $t = {t:.1f}$:  $\Delta x = {sx:.2f}$ grows,  $\Delta p = {1 / (2 * s0):.2f}$ stays",
                     loc="left", fontsize=12.5)

    ani = FuncAnimation(fig, update, frames=nf, interval=120, blit=False)
    return fig, ani


# ------------------------------------------------------------ Ehrenfest: harmonic packet tracks the ball exactly, quartic packet does not
@register
def ehrenfest_wells():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-6, 6, 600); h = x[1] - x[0]               # hbar = m = 1, both packets start at rest at x0
    x0 = -2.5
    T = -0.5 * (np.eye(x.size, k=1) - 2 * np.eye(x.size) + np.eye(x.size, k=-1)) / h**2
    psi0 = np.exp(-(x - x0)**2 / 2) / np.pi**0.25
    nf, tmax = 44, 9.4
    ts = np.linspace(0, tmax, nf)
    wells = [(0.5 * x**2, lambda y: y, lambda y: 0.5 * y**2, r"harmonic, $V = \frac{1}{2}x^2$", TEAL),
             (0.1 * x**4, lambda y: 0.4 * y**3, lambda y: 0.1 * y**4, r"quartic, $V = 0.1\,x^4$", ORANGE)]
    data = []
    for V, dV, Vf, title, col in wells:
        E, U = np.linalg.eigh(T + np.diag(V)); U = U / np.sqrt(h)
        c = U.T @ psi0 * h
        dens = np.array([np.abs(U @ (c * np.exp(-1j * E * t)))**2 for t in ts])
        xq = dens @ x * h
        dt = 1e-3; xc = np.empty(int(tmax / dt) + 2); xv, vv = x0, 0.0  # velocity Verlet for the classical ball
        for j in range(xc.size):
            xc[j] = xv; a1 = -dV(xv); xv = xv + vv * dt + 0.5 * a1 * dt**2; vv = vv + 0.5 * (a1 - dV(xv)) * dt
        xcl = np.interp(ts, np.arange(xc.size) * dt, xc)
        data.append((V, Vf, title, col, dens, xq, xcl, np.sum(c**2 * E)))
    fig = plt.figure(figsize=(8.8, 4.6))
    gs = fig.add_gridspec(2, 2, height_ratios=[1.7, 1], hspace=0.45, wspace=0.14)
    arts = []
    for j, (V, Vf, title, col, dens, xq, xcl, Eav) in enumerate(data):
        ax = fig.add_subplot(gs[0, j]); axt = fig.add_subplot(gs[1, j])
        ax.plot(x, V, color=GRAY, lw=1.8)
        (pk,) = ax.plot([], [], color=col, lw=2.4)
        (ball,) = ax.plot([], [], "o", color=PURPLE, ms=11, zorder=6)
        (qm,) = ax.plot([], [], marker="^", color=col, ms=12, ls="none", zorder=6)
        ax.set_xlim(-4, 4); ax.set_ylim(0, 8.6); ax.set_yticks([]); ax.set_xticks([])
        ax.spines["left"].set_visible(False)
        ax.set_title(title, loc="left", fontsize=12.5)
        axt.plot(ts, xcl, color=PURPLE, lw=1.4, ls="--")
        (tq,) = axt.plot([], [], color=col, lw=2.4)
        axt.set_xlim(0, tmax); axt.set_ylim(-2.9, 2.9); axt.set_yticks([-2, 0, 2]); axt.tick_params(labelsize=10.5)
        axt.set_xlabel("time", fontsize=11.5)
        axt.set_title(r"$\langle x\rangle$ (solid) " + ("tracks the ball (dashed) exactly" if j == 0 else "falls away from the ball (dashed)"),
                      loc="left", fontsize=11.5)
        arts.append((pk, ball, qm, tq, dens, xq, xcl, Vf, Eav))
    fig.subplots_adjust(left=0.04, right=0.99, top=0.92, bottom=0.1)

    def update(i):
        for pk, ball, qm, tq, dens, xq, xcl, Vf, Eav in arts:
            pk.set_data(x, Eav + 1.8 * dens[i])
            ball.set_data([xcl[i]], [Vf(xcl[i])])
            qm.set_data([xq[i]], [Eav - 0.25])
            tq.set_data(ts[:i + 1], xq[:i + 1])

    ani = FuncAnimation(fig, update, frames=nf, interval=110, blit=False)
    return fig, ani


# ------------------------------------------------------------ Bohr frequencies: <x>(t) of psi1 + psi2 + psi3 holds w21 and w32, not w31 (still)
@register
def bohr_spectrum():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    c = np.array([0.5, 0.5, np.sqrt(0.5)])                      # L = hbar = E1 = 1, E_n = n^2
    xnm = lambda n, m: 0.5 if n == m else (0.0 if (n + m) % 2 == 0 else -8 * n * m / (np.pi**2 * (n * n - m * m)**2))
    t = np.linspace(0, 2 * np.pi, 800)
    xt = sum(c[n - 1] * c[m - 1] * xnm(n, m) * np.cos((n * n - m * m) * t) for n in (1, 2, 3) for m in (1, 2, 3))
    fig, (ax, axs) = plt.subplots(1, 2, figsize=(9, 3.4), gridspec_kw={"width_ratios": [1.5, 1], "wspace": 0.3})
    ax.plot(t / (2 * np.pi), xt, color=PURPLE, lw=2.2)
    ax.axhline(0.5, color=GRAY, lw=0.8, ls=":")
    ax.set_xlim(0, 1); ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "T/2", "T"])
    ax.set_yticks([0.3, 0.5, 0.7]); ax.set_yticklabels(["0.3 L", "L/2", "0.7 L"]); ax.tick_params(labelsize=11)
    ax.set_title(r"$\langle x\rangle(t)$ for $\frac{1}{2}\psi_1 + \frac{1}{2}\psi_2 + \frac{1}{\sqrt{2}}\psi_3$", loc="left", fontsize=12.5)
    lines = [(3, 2 * c[0] * c[1] * abs(xnm(1, 2)), r"$\omega_{21}$"), (5, 2 * c[1] * c[2] * abs(xnm(2, 3)), r"$\omega_{32}$"),
             (8, 0.0, r"$\omega_{31}$")]
    for w, a, lab in lines:
        if a > 0:
            axs.vlines(w, 0, a, color=PURPLE, lw=5); axs.text(w, a + 0.01, lab, ha="center", fontsize=13, color=PURPLE)
        else:
            axs.plot([w], [0.004], "o", mfc="white", mec=GRAY, ms=10, mew=2)
            axs.text(w, 0.03, lab + "\nmissing:\n" + r"$\langle 1|x|3\rangle = 0$", ha="center", fontsize=11, color=GRAY)
    axs.set_xlim(1, 10); axs.set_ylim(0, 0.17); axs.set_yticks([])
    axs.set_xticks([3, 5, 8]); axs.set_xticklabels([r"$3E_1/\hbar$", r"$5E_1/\hbar$", r"$8E_1/\hbar$"], fontsize=11.5)
    axs.spines["left"].set_visible(False)
    axs.set_title("frequencies in the motion", loc="left", fontsize=12.5)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.88, bottom=0.14)
    fig.savefig(f"{OUT}/bohr_spectrum.png", dpi=200)
    print("wrote", f"{OUT}/bohr_spectrum.png")
    return fig, None


# ------------------------------------------------------------ revival in a box: the packet dissolves, mirrors at T/2 and returns at T (still)
@register
def box_revival():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 500); dx = x[1] - x[0]               # L = 1; time in units of T_rev = 4 m L^2 / (pi hbar)
    ns = np.arange(1, 81)
    phis = np.sqrt(2) * np.sin(np.outer(ns, np.pi * x))
    g = np.exp(-(x - 0.3)**2 / (4 * 0.05**2)); g = g / np.sqrt(np.sum(g**2) * dx)
    c = phis @ g * dx
    psi = lambda tau: (c * np.exp(-2j * np.pi * ns**2 * tau)) @ phis
    snaps = [(0.0, "t = 0"), (0.01, "t = 0.01 T"), (0.25, "T/4: two copies"), (0.5, "T/2: mirror image"), (1.0, "t = T: back")]
    taus = np.linspace(0, 1, 3001)
    ret = np.abs(np.exp(-2j * np.pi * np.outer(taus, ns**2)) @ (c**2))**2
    fig = plt.figure(figsize=(9.4, 4.1))
    gs = fig.add_gridspec(2, len(snaps), height_ratios=[1, 1.15], hspace=0.55, wspace=0.12)
    for j, (tau, lab) in enumerate(snaps):
        ax = fig.add_subplot(gs[0, j])
        d = np.abs(psi(tau))**2
        ax.fill_between(x, d, color=CARDINAL, alpha=0.2, lw=0); ax.plot(x, d, color=CARDINAL, lw=1.8)
        ax.plot([0, 0, 1, 1], [8.5, 0, 0, 8.5], color="k", lw=2)
        ax.set_xlim(-0.03, 1.03); ax.set_ylim(0, 8.5); ax.axis("off")
        ax.set_title(lab, fontsize=11.5)
    axr = fig.add_subplot(gs[1, :])
    axr.plot(taus, ret, color=TEAL, lw=1.3)
    for tau, lab in snaps:
        k = int(round(tau * (taus.size - 1)))
        axr.plot([tau], [ret[k]], "o", color=CARDINAL, ms=7, zorder=5)
    axr.set_xlim(0, 1); axr.set_ylim(0, 1.08)
    axr.set_xticks([0, 0.25, 0.5, 0.75, 1]); axr.set_xticklabels(["0", "T/4", "T/2", "3T/4", "T"], fontsize=11.5)
    axr.set_yticks([0, 0.5, 1]); axr.tick_params(labelsize=11)
    axr.set_ylabel(r"$|\langle\Psi(0)|\Psi(t)\rangle|^2$", fontsize=12)
    axr.set_title("return probability: how much of the starting packet is back", loc="left", fontsize=12.5)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.92, bottom=0.11)
    fig.savefig(f"{OUT}/box_revival.png", dpi=200)
    print("wrote", f"{OUT}/box_revival.png")
    return fig, None


# ------------------------------------------------------------ femtochemistry: a packet in a Morse bond swings, dephases and revives (still)
@register
def morse_revival():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    D = 10.0; a = 1 / np.sqrt(2 * D)                            # hbar = m = 1, harmonic frequency 1 at the bottom
    x = np.linspace(-4, 20, 900); h = x[1] - x[0]
    V = D * (1 - np.exp(-a * x))**2
    T = -0.5 * (np.eye(x.size, k=1) - 2 * np.eye(x.size) + np.eye(x.size, k=-1)) / h**2
    E, U = np.linalg.eigh(T + np.diag(np.minimum(V, 80))); U = U / np.sqrt(h)
    psi0 = np.exp(-(x + 1.2)**2 / 2) / np.pi**0.25              # ground-state-shaped packet on the compressed side
    c = U.T @ psi0 * h
    keep = np.argsort(-c**2)[:30]; cc, UU, EE = c[keep], U[:, keep], E[keep]
    X = UU.T @ (x[:, None] * UU) * h
    tl = np.linspace(0, 2 * np.pi * 44, 6000)
    A = cc * np.exp(-1j * np.outer(tl, EE))
    xm = np.real(np.einsum("ti,ij,tj->t", np.conj(A), X, A))
    snaps = [(0.25, "first swings: a compact packet"), (10.3, "about 10 periods: spread out"), (20.25, "about 20 periods: back together")]
    fig = plt.figure(figsize=(9.4, 4.4))
    gs = fig.add_gridspec(2, 3, height_ratios=[1.1, 1], hspace=0.5, wspace=0.1)
    Eav = np.sum(c**2 * E)
    for j, (per, lab) in enumerate(snaps):
        ax = fig.add_subplot(gs[0, j])
        d = np.abs(UU @ (cc * np.exp(-1j * EE * per * 2 * np.pi)))**2
        ax.plot(x, V, color=GRAY, lw=1.6)
        ax.fill_between(x, Eav, Eav + 4 * d, color=CARDINAL, alpha=0.2, lw=0); ax.plot(x, Eav + 4 * d, color=CARDINAL, lw=1.8)
        ax.set_xlim(-3, 9); ax.set_ylim(0, 6.2); ax.axis("off")
        ax.set_title(lab, fontsize=11.5)
    axm = fig.add_subplot(gs[1, :])
    axm.plot(tl / (2 * np.pi), xm, color=TEAL, lw=0.9)
    for per, lab in snaps:
        axm.axvline(per, color=CARDINAL, lw=1, ls=":")
    axm.set_xlim(0, 44); axm.set_xlabel("time  (vibrational periods)", fontsize=12)
    axm.set_ylabel(r"$\langle x\rangle$, bond length", fontsize=11.5); axm.set_yticks([]); axm.tick_params(labelsize=11)
    axm.set_title("the average bond length swings, fades as the packet dephases, and comes back", loc="left", fontsize=12.5)
    fig.subplots_adjust(left=0.06, right=0.99, top=0.92, bottom=0.12)
    fig.savefig(f"{OUT}/morse_revival.png", dpi=200)
    print("wrote", f"{OUT}/morse_revival.png")
    return fig, None


if __name__ == "__main__":
    names = sys.argv[1:] or list(REGISTRY)
    for name in names:
        fig, ani = REGISTRY[name]()
        if ani is not None:
            path = f"{OUT}/{name}.gif"
            ani.save(path, writer=PillowWriter(fps=15), dpi=GIF_DPI)
            print("wrote", path)
        plt.close(fig)
