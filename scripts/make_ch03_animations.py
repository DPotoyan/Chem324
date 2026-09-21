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


if __name__ == "__main__":
    names = sys.argv[1:] or list(REGISTRY)
    for name in names:
        fig, ani = REGISTRY[name]()
        if ani is not None:
            path = f"{OUT}/{name}.gif"
            ani.save(path, writer=PillowWriter(fps=15), dpi=100)
            print("wrote", path)
        plt.close(fig)
