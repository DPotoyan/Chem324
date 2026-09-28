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
The "deck 3.2" and "deck 3.3" sections (particle in a box and its applications) are deck-only
for now; page ch03/02 still has its older cells and is not in sync_ch03_cells.PAGES yet.
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = "ch03/images"
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


# ------------------------------------------------------------ only whole half-waves fit: scan the energy
@register
def box_fit():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 400)
    es = np.concatenate([np.linspace(0.25, 1, 8), np.full(5, 1.0), np.linspace(1, 4, 11)[1:], np.full(5, 4.0),
                         np.linspace(4, 9, 13)[1:], np.full(5, 9.0), np.linspace(9, 11, 4)[1:], np.full(3, 11.0)])
    eg = np.linspace(0, 11.2, 600)
    fig, (ax, axe) = plt.subplots(1, 2, figsize=(8, 3.4), gridspec_kw={"width_ratios": [1.15, 1], "wspace": 0.3})
    ax.axvline(0, color="k", lw=3); ax.axvline(1, color="k", lw=3); ax.axhline(0, color=GRAY, lw=0.6)
    (wave,) = ax.plot([], [], lw=2.6)
    (miss,) = ax.plot([], [], color=CARDINAL, lw=4)
    (dot,) = ax.plot([], [], "o", ms=10, zorder=5)
    ax.set_xlim(-0.04, 1.04); ax.set_ylim(-1.3, 1.55); ax.set_yticks([])
    ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "L"]); ax.set_xlabel("x")
    ax.text(0.02, 1.3, r"$\psi = \sin kx$ already obeys $\psi(0) = 0$", fontsize=9.5, color=GRAY)
    axe.plot(eg, np.sin(np.pi * np.sqrt(eg)), color=GRAY, lw=1, alpha=0.3)
    axe.axhline(0, color=GRAY, lw=0.6)
    (trace,) = axe.plot([], [], color=ORANGE, lw=2.2)
    (cur,) = axe.plot([], [], "o", ms=9, zorder=5)
    zeros = []
    for n in (1, 2, 3):
        (mk,) = axe.plot([n * n], [0], "o", color=TEAL, ms=11, mfc="white", mew=2.4, zorder=4)
        lb = axe.text(n * n, -1.27, f"n = {n}", ha="center", va="bottom", fontsize=10.5, color=TEAL)
        zeros.append((n, mk, lb))
    axe.set_xlim(0, 11.2); axe.set_ylim(-1.3, 1.55)
    axe.set_xticks([1, 4, 9]); axe.set_xticklabels([r"$E_1$", r"$4E_1$", r"$9E_1$"])
    axe.set_xlabel("energy E"); axe.set_ylabel(r"$\psi(L)$"); axe.set_yticks([-1, 0, 1])
    axe.set_title("the right wall's verdict", loc="left", fontsize=11)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.88, bottom=0.16)

    def update(i):
        e = es[i]; r = np.sqrt(e)
        fit = abs(r - round(r)) < 1e-9 and e <= 9
        col = TEAL if fit else ORANGE
        end = np.sin(np.pi * r)
        wave.set_data(x, np.sin(np.pi * r * x)); wave.set_color(col)
        miss.set_data([1.018, 1.018], [0, end]); miss.set_visible(not fit)
        dot.set_data([1.018 if not fit else 1], [end]); dot.set_color(TEAL if fit else CARDINAL)
        ax.set_title((f"E = {round(e)}" if e > 1 else "E = ") + r"$E_1$" + f":  {round(r)} half-wave" + ("s fit" if r > 1 else " fits")
                     if fit else f"E = {e:.2f}" + r"$E_1$" + ":  misses the wall", loc="left", fontsize=11, color=col)
        m = eg <= e
        trace.set_data(eg[m], np.sin(np.pi * np.sqrt(eg[m])))
        cur.set_data([e], [end]); cur.set_color(TEAL if fit else CARDINAL)
        for n, mk, lb in zeros:
            mk.set_visible(e >= n * n - 1e-9); lb.set_visible(e >= n * n - 1e-9)

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


# ------------------------------------------------------------ superposition of n = 1 and n = 2: the density sloshes
@register
def box_slosh():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 400)
    p1, p2 = np.sqrt(2) * np.sin(np.pi * x), np.sqrt(2) * np.sin(2 * np.pi * x)
    nf = 60
    ts = np.linspace(0, 2 * np.pi, nf, endpoint=False)          # E1 = 1, E2 = 4, hbar = 1: three sloshes
    tt = np.linspace(0, 2 * np.pi, 400)
    xbar = lambda t: 0.5 - 16 / (9 * np.pi**2) * np.cos(3 * t)  # <x>(t) = L/2 + x12 cos(w21 t)
    th = np.linspace(0, 2 * np.pi, 200)
    fig = plt.figure(figsize=(8, 3.3))
    gs = fig.add_gridspec(2, 2, width_ratios=[2.3, 1], hspace=0.75, wspace=0.22)
    ax, axc, axt = fig.add_subplot(gs[:, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])
    ax.plot(x, 0.5 * p1**2, color=GRAY, lw=1, ls="--")
    ax.plot(x, 0.5 * p2**2, color=GRAY, lw=1, ls=":")
    (dens,) = ax.plot([], [], color=CARDINAL, lw=2.6, label=r"$|\Psi(x,t)|^2$")
    band = [ax.fill_between(x, 0 * x, color=CARDINAL, alpha=0.18, lw=0)]
    (mark,) = ax.plot([], [], marker="^", color=PURPLE, ms=13, clip_on=False, zorder=6, ls="none",
                      label=r"$\langle x\rangle$")
    ax.plot([0, 0, 1, 1], [3.4, 0, 0, 3.4], color="k", lw=2.6)
    ax.set_xlim(-0.02, 1.02); ax.set_ylim(0, 3.4); ax.set_yticks([])
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("x", labelpad=8)
    ax.tick_params(axis="x", pad=10)
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.set_title(r"$\Psi = (\psi_1 e^{-iE_1t/\hbar} + \psi_2 e^{-iE_2t/\hbar})/\sqrt{2}$", loc="left", fontsize=11)
    axc.plot(np.cos(th), np.sin(th), color=GRAY, lw=1, ls="--")
    (h1,) = axc.plot([], [], color=TEAL, lw=2.8, label=r"$E_1$")
    (h2,) = axc.plot([], [], color=ORANGE, lw=2.8, label=r"$E_2 = 4E_1$")
    axc.set_aspect("equal"); axc.set_xlim(-1.25, 1.25); axc.set_ylim(-1.25, 1.25); axc.set_axis_off()
    axc.legend(loc="center left", bbox_to_anchor=(1.0, 0.5), frameon=False, fontsize=9.5, handlelength=1.2)
    axc.set_title("two phase clocks", fontsize=10.5, color=GRAY)
    axt.plot(tt, xbar(tt), color=GRAY, lw=1.2)
    (tdot,) = axt.plot([], [], "o", color=PURPLE, ms=8)
    axt.set_xlim(0, 2 * np.pi); axt.set_ylim(0.25, 0.75); axt.set_xticks([])
    axt.set_yticks([0.5]); axt.set_yticklabels(["L/2"]); axt.set_xlabel("time")
    axt.set_title(r"$\langle x\rangle$ swings at $(E_2-E_1)/\hbar$", fontsize=10.5)
    fig.subplots_adjust(left=0.03, right=0.9, top=0.88, bottom=0.14)

    def update(i):
        t = ts[i]
        psi = (p1 * np.exp(-1j * t) + p2 * np.exp(-4j * t)) / np.sqrt(2)
        rho = np.abs(psi) ** 2
        dens.set_data(x, rho)
        band[0].remove(); band[0] = ax.fill_between(x, rho, color=CARDINAL, alpha=0.18, lw=0)
        mark.set_data([xbar(t)], [-0.12])
        h1.set_data([0, np.cos(-t)], [0, np.sin(-t)]); h2.set_data([0, np.cos(-4 * t)], [0, np.sin(-4 * t)])
        tdot.set_data([t], [xbar(t)])

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


if __name__ == "__main__":
    names = sys.argv[1:] or list(REGISTRY)
    for name in names:
        fig, ani = REGISTRY[name]()
        if ani is not None:
            path = f"{OUT}/{name}.gif"
            ani.save(path, writer=PillowWriter(fps=15), dpi=100)
            print("wrote", path)
        plt.close(fig)
