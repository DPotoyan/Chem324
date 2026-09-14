"""Chapter 2 animations and deck stills, authored ONCE here.

Each registered function builds one figure (and, for animations, a FuncAnimation) and is
self-contained: it uses only numpy, matplotlib.pyplot, FuncAnimation and the colour
constants below. Running this script bakes the GIFs / PNG stills for the slide decks into
ch02/images/. `scripts/sync_ch02_cells.py` copies the SAME function bodies into the
`{code-cell}` blocks of the lecture pages (marker line `# synced: <name>`), where they are
shown with the matplotlib JS player (house rule: JS player on pages, GIF in decks).

Run from the repo root:
    .venv/bin/python scripts/make_ch02_animations.py                 # bake everything
    .venv/bin/python scripts/make_ch02_animations.py beats light_clock   # a subset
    .venv/bin/python scripts/sync_ch02_cells.py                       # refresh page cells

Page weight: the JS player embeds every frame as a PNG, so keep animations to 24-44 frames.
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = "ch02/images"
TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"

REGISTRY = {}


def register(fn):
    REGISTRY[fn.__name__] = fn
    return fn


# ------------------------------------------------------------ transverse vs longitudinal
@register
def transverse_longitudinal():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    N, A, k, w = 48, 0.35, 2 * np.pi / 4.0, 2 * np.pi / 2.0   # beads, amplitude, lambda = 4, T = 2
    x0 = np.linspace(0, 12, N)
    xs = np.linspace(0, 12, 600)
    ts = np.linspace(0, 2 * np.pi / w, 40, endpoint=False)
    pick = 18                                                 # the bead we follow

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.6))
    for ax in (ax1, ax2):
        ax.set_xlim(-0.5, 12.5); ax.set_ylim(-1.3, 1.45)
        ax.set_yticks([]); ax.spines["left"].set_visible(False)
        ax.annotate("", xy=(12.3, 1.1), xytext=(10.3, 1.1), arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.6))
        ax.text(11.3, 1.22, "wave moves", color=GRAY, fontsize=10, ha="center")
        ax.axvline(x0[pick], color=CARDINAL, lw=1, ls=":")
    ax1.set_title("transverse: each bead moves up and down, perpendicular to the wave", loc="left", fontsize=11.5)
    ax2.set_title("longitudinal: each bead moves back and forth, along the wave", loc="left", fontsize=11.5)
    ax2.set_xlabel("x")
    (string,) = ax1.plot([], [], color=TEAL, lw=1.2, alpha=0.6)
    (beads1,) = ax1.plot([], [], "o", color=TEAL, ms=5)
    (red1,) = ax1.plot([], [], "o", color=CARDINAL, ms=9, mec="white", mew=1.2, zorder=5)
    (beads2,) = ax2.plot([], [], "o", color=TEAL, ms=6)
    (red2,) = ax2.plot([], [], "o", color=CARDINAL, ms=9, mec="white", mew=1.2, zorder=5)
    fig.tight_layout()

    def update(i):
        t = ts[i]
        string.set_data(xs, 0.8 * np.sin(k * xs - w * t))
        beads1.set_data(x0, 0.8 * np.sin(k * x0 - w * t))
        red1.set_data([x0[pick]], [0.8 * np.sin(k * x0[pick] - w * t)])
        xl = x0 + A * np.sin(k * x0 - w * t)
        beads2.set_data(xl, np.zeros(N))
        red2.set_data([xl[pick]], [0])
        return string, beads1, red1, beads2, red2

    ani = FuncAnimation(fig, update, frames=len(ts), interval=75, blit=False)
    return fig, ani


# ------------------------------------------------------------ a shape that moves: f(x -/+ vt)
@register
def traveling_pulse():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    f = lambda s: np.exp(-s**2)
    v = 1.0
    x = np.linspace(-10, 10, 800)
    ts = np.linspace(0, 6.5, 44)

    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    (right,) = ax.plot([], [], color=TEAL, lw=2.6, label=r"$f(x-vt)$  moves right")
    (left,) = ax.plot([], [], color=ORANGE, lw=2.2, ls="--", label=r"$f(x+vt)$  moves left")
    peak = ax.axvline(0, color=TEAL, lw=1, ls=":")
    label = ax.text(0, 1.08, "", color=TEAL, fontsize=11, ha="center")
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(-10, 10); ax.set_ylim(-0.1, 1.25)
    ax.set_xlabel("x"); ax.set_ylabel("u(x, t)")
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    ax.set_title(r"a shape that keeps its form while it moves:  $u(x,t) = f(x \mp vt)$", fontsize=12, loc="left")
    fig.tight_layout()

    def update(i):
        t = ts[i]
        right.set_data(x, f(x - v * t)); left.set_data(x, f(x + v * t))
        peak.set_xdata([v * t, v * t])
        label.set_position((v * t, 1.08)); label.set_text(f"peak at x = vt = {v*t:.1f}")
        return right, left, peak, label

    ani = FuncAnimation(fig, update, frames=len(ts), interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ wavelength (space) and period (time)
@register
def wavelength_period():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    lam, T = 4.0, 2.0
    k, w = 2 * np.pi / lam, 2 * np.pi / T
    x = np.linspace(0, 12, 800); x0 = 5.0
    tt = np.linspace(0, 2 * T, 800)
    ts = np.linspace(0, 2 * T, 40, endpoint=False)

    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.5, 3.9), gridspec_kw={"width_ratios": [1.4, 1]})
    (wave,) = ax.plot([], [], color=TEAL, lw=2.4)
    (dot,) = ax.plot([], [], "o", color=CARDINAL, ms=9, mec="white", mew=1.2, zorder=5)
    (lam_bar,) = ax.plot([], [], color=GRAY, lw=1.4, marker="|", ms=9)
    lam_txt = ax.text(0, 1.22, r"wavelength $\lambda$: crest to crest", color=GRAY, ha="center", fontsize=10.5)
    ax.axvline(x0, color=CARDINAL, lw=1, ls=":")
    ax.text(x0, -1.32, r"watch the point $x_0$", color=CARDINAL, ha="center", fontsize=10.5)
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(0, 12); ax.set_ylim(-1.5, 1.5); ax.set_xlabel("x"); ax.set_ylabel("u")
    ax.set_title(r"snapshot in space:  $u = A\sin(kx-\omega t)$", loc="left", fontsize=11.5)

    bx.plot(tt, np.sin(k * x0 - w * tt), color=GRAY, lw=1.2, alpha=0.5)
    (trace,) = bx.plot([], [], color=CARDINAL, lw=2.4)
    (dot2,) = bx.plot([], [], "o", color=CARDINAL, ms=9, mec="white", mew=1.2, zorder=5)
    bx.plot([0, T], [1.15, 1.15], color=GRAY, lw=1.4, marker="|", ms=9)
    bx.text(T / 2, 1.22, "period T: crest to crest", color=GRAY, ha="center", fontsize=10.5)
    bx.axhline(0, color=GRAY, lw=0.6)
    bx.set_xlim(0, 2 * T); bx.set_ylim(-1.5, 1.5); bx.set_xlabel("t"); bx.set_yticks([])
    bx.set_title(r"history of the point $x_0$", loc="left", fontsize=11.5)
    fig.tight_layout()

    def update(i):
        t = ts[i]
        wave.set_data(x, np.sin(k * x - w * t)); dot.set_data([x0], [np.sin(k * x0 - w * t)])
        xc = ((np.pi / 2 + w * t) / k) % lam            # a crest that stays inside the window
        lam_bar.set_data([xc, xc + lam], [1.15, 1.15]); lam_txt.set_position((xc + lam / 2, 1.24))
        mask = tt <= t
        trace.set_data(tt[mask], np.sin(k * x0 - w * tt[mask])); dot2.set_data([t], [np.sin(k * x0 - w * t)])
        return wave, dot, lam_bar, lam_txt, trace, dot2

    ani = FuncAnimation(fig, update, frames=len(ts), interval=100, blit=False)
    return fig, ani


# ------------------------------------------------------------ complex wave and its phasor
@register
def phasor_wave():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    k, w = 2 * np.pi / 5.0, 2 * np.pi / 3.0     # lambda = 5, T = 3
    x = np.linspace(-10, 10, 800); x0 = 0.0
    ts = np.linspace(0, 2 * np.pi / w, 36, endpoint=False)

    fig, (ax_w, ax_p) = plt.subplots(1, 2, figsize=(9.5, 4), gridspec_kw={"width_ratios": [1.7, 1]})
    (re,) = ax_w.plot([], [], color=TEAL, lw=2.4, label=r"Re $e^{i(kx-\omega t)} = \cos(kx-\omega t)$")
    (im,) = ax_w.plot([], [], color=ORANGE, lw=2.0, ls="--", label=r"Im $e^{i(kx-\omega t)} = \sin(kx-\omega t)$")
    (dot_re,) = ax_w.plot([], [], "o", color=TEAL, ms=8, mec="white", mew=1.2)
    (dot_im,) = ax_w.plot([], [], "o", color=ORANGE, ms=8, mec="white", mew=1.2)
    ax_w.axvline(x0, color=GRAY, lw=1, ls=":"); ax_w.axhline(0, color=GRAY, lw=0.6)
    ax_w.set_xlim(-10, 10); ax_w.set_ylim(-1.35, 1.5)
    ax_w.set_xlabel("x"); ax_w.set_ylabel("u")
    ax_w.legend(loc="upper right", frameon=False, fontsize=9.5)
    ax_w.set_title("the wave along x at time t", loc="left", fontsize=11.5)

    th = np.linspace(0, 2 * np.pi, 400)
    ax_p.plot(np.cos(th), np.sin(th), color=GRAY, lw=1, ls="--")
    ax_p.axhline(0, color=GRAY, lw=0.6); ax_p.axvline(0, color=GRAY, lw=0.6)
    (arrow,) = ax_p.plot([], [], color=PURPLE, lw=2.6)
    (tip,) = ax_p.plot([], [], "o", color=PURPLE, ms=8)
    (proj_re,) = ax_p.plot([], [], color=TEAL, lw=2, ls=":")
    (proj_im,) = ax_p.plot([], [], color=ORANGE, lw=2, ls=":")
    ax_p.set_aspect("equal"); ax_p.set_xlim(-1.3, 1.3); ax_p.set_ylim(-1.3, 1.3)
    ax_p.set_xlabel("Re"); ax_p.set_ylabel("Im")
    ax_p.set_title(r"the phasor $e^{i(kx_0-\omega t)}$ at $x_0 = 0$", loc="left", fontsize=11.5)
    fig.tight_layout()

    def update(i):
        t = ts[i]
        ph = k * x - w * t
        re.set_data(x, np.cos(ph)); im.set_data(x, np.sin(ph))
        z = np.exp(1j * (k * x0 - w * t))
        dot_re.set_data([x0], [z.real]); dot_im.set_data([x0], [z.imag])
        arrow.set_data([0, z.real], [0, z.imag]); tip.set_data([z.real], [z.imag])
        proj_re.set_data([z.real, z.real], [0, z.imag]); proj_im.set_data([0, z.real], [z.imag, z.imag])
        return re, im, dot_re, dot_im, arrow, tip, proj_re, proj_im

    ani = FuncAnimation(fig, update, frames=len(ts), interval=85, blit=False)
    return fig, ani


# ------------------------------------------------------------ interference of two waves vs phase
@register
def interference_phase():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 4 * np.pi, 800)
    phis = np.linspace(0, 2 * np.pi, 40, endpoint=False)

    fig, (ax_w, ax_p) = plt.subplots(1, 2, figsize=(9.5, 4), gridspec_kw={"width_ratios": [1.9, 1]})
    (w1,) = ax_w.plot([], [], color=TEAL, lw=1.6, label=r"$\sin(kx)$")
    (w2,) = ax_w.plot([], [], color=ORANGE, lw=1.6, label=r"$\sin(kx+\phi)$")
    (ws,) = ax_w.plot([], [], color=CARDINAL, lw=2.8, label="sum")
    env_hi = ax_w.axhline(2, color=GRAY, lw=1, ls="--"); env_lo = ax_w.axhline(-2, color=GRAY, lw=1, ls="--")
    ax_w.axhline(0, color=GRAY, lw=0.6)
    ax_w.set_xlim(0, 4 * np.pi); ax_w.set_ylim(-2.5, 2.9)
    ax_w.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi])
    ax_w.set_xticklabels(["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
    ax_w.set_xlabel("kx"); ax_w.set_ylabel("u")
    ax_w.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=3)
    title = ax_w.set_title(r"phase difference $\phi$ = 0.00$\pi$,   sum amplitude $2|\cos(\phi/2)|$ = 2.00", loc="left", fontsize=11.5)

    th = np.linspace(0, 2 * np.pi, 400)
    ax_p.plot(np.cos(th), np.sin(th), color=GRAY, lw=0.8, ls="--")
    ax_p.axhline(0, color=GRAY, lw=0.6); ax_p.axvline(0, color=GRAY, lw=0.6)
    (a1,) = ax_p.plot([], [], color=TEAL, lw=2.4)
    (a2,) = ax_p.plot([], [], color=ORANGE, lw=2.4)
    (asum,) = ax_p.plot([], [], color=CARDINAL, lw=3)
    (t1,) = ax_p.plot([], [], "o", color=TEAL, ms=6)
    (tsum,) = ax_p.plot([], [], "o", color=CARDINAL, ms=7)
    ax_p.set_aspect("equal"); ax_p.set_xlim(-2.3, 2.3); ax_p.set_ylim(-2.3, 2.3)
    ax_p.set_xlabel("Re"); ax_p.set_ylabel("Im")
    ax_p.set_title(r"phasors: $1 + e^{i\phi}$ tip to tail", loc="left", fontsize=11.5)
    fig.tight_layout()

    def update(i):
        phi = phis[i]
        w1.set_data(x, np.sin(x)); w2.set_data(x, np.sin(x + phi)); ws.set_data(x, np.sin(x) + np.sin(x + phi))
        amp = 2 * abs(np.cos(phi / 2))
        env_hi.set_ydata([amp, amp]); env_lo.set_ydata([-amp, -amp])
        z1, zs = 1 + 0j, 1 + np.exp(1j * phi)
        a1.set_data([0, z1.real], [0, z1.imag]); a2.set_data([z1.real, zs.real], [z1.imag, zs.imag])
        asum.set_data([0, zs.real], [0, zs.imag]); t1.set_data([z1.real], [z1.imag]); tsum.set_data([zs.real], [zs.imag])
        title.set_text(rf"phase difference $\phi$ = {phi/np.pi:.2f}$\pi$,   sum amplitude $2|\cos(\phi/2)|$ = {amp:.2f}")
        return w1, w2, ws, env_hi, env_lo, a1, a2, asum, t1, tsum, title

    ani = FuncAnimation(fig, update, frames=len(phis), interval=100, blit=False)
    return fig, ani


# ------------------------------------------------------------ two point sources: fringes in 2D
@register
def two_source_interference():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    lam = 1.0; k, w = 2 * np.pi / lam, 2 * np.pi; d = 3 * lam
    xs = np.linspace(-6, 6, 220); ys = np.linspace(0, 12, 220)
    X, Y = np.meshgrid(xs, ys)
    r1, r2 = np.hypot(X + d / 2, Y), np.hypot(X - d / 2, Y)
    damp = lambda r: 1 / np.sqrt(1 + r)                     # gentle 2D spreading
    ts = np.linspace(0, 2 * np.pi / w, 30, endpoint=False)
    r1f, r2f = np.hypot(xs + d / 2, 12), np.hypot(xs - d / 2, 12)
    I_far = np.abs(damp(r1f) * np.exp(1j * k * r1f) + damp(r2f) * np.exp(1j * k * r2f))**2

    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9, 4.4), gridspec_kw={"width_ratios": [1.15, 1]})
    levels = np.linspace(-1.2, 1.2, 13)
    ax.set_xlim(-6, 6); ax.set_ylim(0, 12); ax.set_aspect("equal")
    ax.plot([-d / 2, d / 2], [0, 0], "o", color=CARDINAL, ms=8, mec="white", mew=1.2, clip_on=False, zorder=5)
    ax.set_xlabel("x"); ax.set_ylabel("y")
    ax.set_title(r"two in-phase point sources,  $d = 3\lambda$", loc="left", fontsize=11.5)
    bx.plot(xs, I_far / I_far.max(), color=CARDINAL, lw=2.4)
    bx.fill_between(xs, I_far / I_far.max(), color=CARDINAL, alpha=0.12)
    bx.set_xlim(-6, 6); bx.set_ylim(0, 1.1)
    bx.set_xlabel("x along the far edge  (y = 12)"); bx.set_ylabel("time-averaged intensity")
    bx.set_title("bright and dark fringes", loc="left", fontsize=11.5)
    fig.tight_layout()
    art = []

    def update(i):
        t = ts[i]
        for c in art:
            c.remove()
        art.clear()
        u = damp(r1) * np.cos(k * r1 - w * t) + damp(r2) * np.cos(k * r2 - w * t)
        art.append(ax.contourf(X, Y, u, levels=levels, cmap="RdBu_r", extend="both"))
        return art

    ani = FuncAnimation(fig, update, frames=len(ts), interval=100, blit=False)
    return fig, ani


# ------------------------------------------------------------ standing wave = two traveling waves
@register
def traveling_standing():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    k, w = 1.0, 1.0                        # v = w/k = 1
    x = np.linspace(0, 4 * np.pi, 800)     # two wavelengths
    ts = np.linspace(0, 2 * np.pi / w, 36, endpoint=False)
    nodes = np.arange(0, 4 * np.pi + 1e-9, np.pi / k)

    fig, axes = plt.subplots(3, 1, figsize=(7.5, 5.6), sharex=True)
    titles = [r"travels right:  $\sin(kx-\omega t)$", r"travels left:  $\sin(kx+\omega t)$",
              r"their sum:  $2\sin(kx)\cos(\omega t)$,  a standing wave"]
    lines, dots = [], []
    for ax, ttl, col in zip(axes, titles, [TEAL, ORANGE, CARDINAL]):
        (ln,) = ax.plot([], [], color=col, lw=2.4)
        (dt,) = ax.plot([], [], "o", color=col, ms=8, mec="white", mew=1.2)
        lines.append(ln); dots.append(dt)
        ax.axhline(0, color=GRAY, lw=0.6)
        ax.set_title(ttl, fontsize=11.5, loc="left", pad=4); ax.set_yticks([])
    axes[0].set_ylim(-1.3, 1.3); axes[1].set_ylim(-1.3, 1.3); axes[2].set_ylim(-2.5, 2.5)
    axes[2].plot(x, 2 * np.sin(k * x), color=GRAY, lw=1, ls="--")
    axes[2].plot(x, -2 * np.sin(k * x), color=GRAY, lw=1, ls="--")
    axes[2].plot(nodes, np.zeros_like(nodes), "o", color=GRAY, ms=7, zorder=5)
    axes[2].text(nodes[1], -2.2, "nodes never move", color=GRAY, fontsize=10, ha="center")
    axes[2].set_xlabel("x"); axes[2].set_xlim(0, 4 * np.pi)
    axes[2].set_xticks(nodes)
    axes[2].set_xticklabels(["0", r"$\lambda/2$", r"$\lambda$", r"$3\lambda/2$", r"$2\lambda$"])
    fig.tight_layout()

    def update(i):
        t = ts[i]
        lines[0].set_data(x, np.sin(k * x - w * t))
        lines[1].set_data(x, np.sin(k * x + w * t))
        lines[2].set_data(x, 2 * np.sin(k * x) * np.cos(w * t))
        dots[0].set_data([(np.pi / 2 + w * t) / k], [1.0])                 # a crest moving right
        dots[1].set_data([(np.pi / 2 + 2 * np.pi - w * t) / k], [1.0])     # a crest moving left
        dots[2].set_data([np.pi / (2 * k)], [2 * np.cos(w * t)])           # an antinode: up and down only
        return (*lines, *dots)

    ani = FuncAnimation(fig, update, frames=len(ts), interval=85, blit=False)
    return fig, ani


# ------------------------------------------------------------ beats
@register
def beats():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    v = 1.0
    k1, k2 = 4.0, 5.0
    w1, w2 = v * k1, v * k2
    x = np.linspace(0, 20, 1600)
    ts = np.linspace(0, 2 * np.pi, 40, endpoint=False)     # common period of both waves

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4.8), sharex=True)
    (l1,) = ax1.plot([], [], color=TEAL, lw=1.5, label=r"$\cos(k_1x-\omega_1t)$")
    (l2,) = ax1.plot([], [], color=ORANGE, lw=1.5, label=r"$\cos(k_2x-\omega_2t)$")
    ax1.set_ylim(-1.5, 1.7); ax1.set_yticks([])
    ax1.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=2)
    ax1.set_title("two waves with slightly different wavelengths", loc="left", fontsize=11.5)
    (ls,) = ax2.plot([], [], color=CARDINAL, lw=2.0, label="sum")
    (e1,) = ax2.plot([], [], color=GRAY, lw=1.4, ls="--",
                     label=r"envelope $\pm 2\cos\left(\frac{\Delta k}{2}x - \frac{\Delta\omega}{2}t\right)$")
    (e2,) = ax2.plot([], [], color=GRAY, lw=1.4, ls="--")
    ax2.set_ylim(-2.7, 3.1); ax2.set_yticks([]); ax2.set_xlim(0, 20); ax2.set_xlabel("x")
    ax2.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=2)
    ax2.set_title("their sum: a fast carrier inside a slow envelope (beats)", loc="left", fontsize=11.5)
    for ax in (ax1, ax2):
        ax.axhline(0, color=GRAY, lw=0.6)
    fig.tight_layout()

    def update(i):
        t = ts[i]
        y1, y2 = np.cos(k1 * x - w1 * t), np.cos(k2 * x - w2 * t)
        l1.set_data(x, y1); l2.set_data(x, y2); ls.set_data(x, y1 + y2)
        env = 2 * np.cos(0.5 * (k2 - k1) * x - 0.5 * (w2 - w1) * t)
        e1.set_data(x, env); e2.set_data(x, -env)
        return l1, l2, ls, e1, e2

    ani = FuncAnimation(fig, update, frames=len(ts), interval=75, blit=False)
    return fig, ani


# ------------------------------------------------------------ light clock: moving clocks run slow
@register
def light_clock():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    c, v, d = 1.0, 0.6, 1.0                          # light speed, clock speed, mirror gap
    gamma = 1 / np.sqrt(1 - v**2 / c**2)             # 1.25
    T0 = 2 * d / c                                   # one tick of the clock at rest
    ts = np.linspace(0, 3 * T0, 48, endpoint=False)  # three ticks of the rest clock
    bounce = lambda tau: d * (1 - np.abs(2 * (tau % 1.0) - 1))   # 0 -> d -> 0 once per unit tau

    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.5, 4.2), gridspec_kw={"width_ratios": [1, 2.4]})
    for a_, xlim in ((ax, (-0.8, 0.8)), (bx, (-0.8, 4.4))):
        a_.set_xlim(*xlim); a_.set_ylim(-0.35, 1.45); a_.set_yticks([]); a_.set_xticks([])
        for s in ("left", "bottom"):
            a_.spines[s].set_visible(False)
    (mir_a0,) = ax.plot([-0.5, 0.5], [0, 0], color="#333333", lw=5, solid_capstyle="butt")
    (mir_a1,) = ax.plot([-0.5, 0.5], [d, d], color="#333333", lw=5, solid_capstyle="butt")
    (ph_a,) = ax.plot([], [], "o", color=ORANGE, ms=13, mec="#ffd27f", mew=2.5, zorder=6)
    (path_a,) = ax.plot([], [], color=ORANGE, lw=1.2, ls=":", alpha=0.8)
    tick_a = ax.text(0, -0.25, "", ha="center", fontsize=12, color=TEAL, fontweight="bold")
    ax.set_title(r"clock at rest:  tick $= 2d/c$", loc="left", fontsize=11.5)
    ax.text(0.62, d / 2, "d", fontsize=12, color=GRAY, va="center")
    ax.plot([0.58, 0.58], [0, d], color=GRAY, lw=1, marker="_", ms=8)

    (mir_b0,) = bx.plot([], [], color="#333333", lw=5, solid_capstyle="butt")
    (mir_b1,) = bx.plot([], [], color="#333333", lw=5, solid_capstyle="butt")
    (ph_b,) = bx.plot([], [], "o", color=ORANGE, ms=13, mec="#ffd27f", mew=2.5, zorder=6)
    (path_b,) = bx.plot([], [], color=ORANGE, lw=1.2, ls=":", alpha=0.8)
    tick_b = bx.text(0, -0.25, "", ha="center", fontsize=12, color=CARDINAL, fontweight="bold")
    bx.annotate("", xy=(4.2, 1.32), xytext=(2.9, 1.32), arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.6))
    bx.text(3.55, 1.37, "v = 0.6 c", color=GRAY, fontsize=10.5, ha="center")
    bx.set_title(rf"moving at $v = 0.6c$:  longer path at the same $c$, tick $= \gamma\, 2d/c$,  $\gamma$ = {gamma:.2f}",
                 loc="left", fontsize=11.5)
    fig.suptitle("light moves at c for every observer, so the moving clock ticks slower", fontsize=12.5, y=0.99)
    fig.tight_layout(rect=(0, 0, 1, 0.94))

    def update(i):
        t = ts[i]
        tt = np.linspace(0, t, 300)
        ph_a.set_data([0], [bounce(t / T0)])
        path_a.set_data(np.zeros_like(tt), bounce(tt / T0))
        tick_a.set_text(f"ticks: {int(t // T0)}")
        xc = v * t
        mir_b0.set_data([xc - 0.5, xc + 0.5], [0, 0]); mir_b1.set_data([xc - 0.5, xc + 0.5], [d, d])
        ph_b.set_data([xc], [bounce(t / (gamma * T0))])
        path_b.set_data(v * tt, bounce(tt / (gamma * T0)))
        tick_b.set_position((xc, -0.25)); tick_b.set_text(f"ticks: {int(t // (gamma * T0))}")
        return mir_b0, mir_b1, ph_a, path_a, tick_a, ph_b, path_b, tick_b

    ani = FuncAnimation(fig, update, frames=len(ts), interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ acceleration follows curvature (still)
@register
def curvature_pulls():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-3.2, 3.6, 1200)
    u = 1.1 * np.exp(-x**2 / 0.9) - 0.7 * np.exp(-(x - 2.3)**2 / 0.35)      # a crest and a trough
    d2 = np.gradient(np.gradient(u, x), x)                                 # curvature u_xx
    xb = np.array([-2.6, -1.9, -1.35, -0.7, 0.0, 0.7, 1.35, 1.75, 2.3, 2.85, 3.4])
    ub, ab = np.interp(xb, x, u), 0.32 * np.interp(xb, x, d2)

    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.plot(x, u, color=TEAL, lw=2.8)
    ax.plot(xb, ub, "o", color=TEAL, ms=7, mec="white", mew=1.2, zorder=5)
    for xi, ui, ai in zip(xb, ub, ab):
        if abs(ai) > 0.1:
            ax.annotate("", xy=(xi, ui + ai), xytext=(xi, ui),
                        arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=2.2, mutation_scale=16))
    ax.text(0, 1.55, "curves down: pulled down", color=CARDINAL, ha="center", fontsize=10.5)
    ax.text(2.3, -1.1, "curves up: pulled up", color=CARDINAL, ha="center", fontsize=10.5)
    ax.annotate("straight here:\nno net pull", xy=(-0.7, 0.64), xytext=(-1.9, 1.15), color=GRAY, ha="center",
                fontsize=10, arrowprops=dict(arrowstyle="-", color=GRAY, lw=1))
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(-3.2, 3.6); ax.set_ylim(-1.3, 1.8); ax.set_yticks([]); ax.set_xlabel("x")
    ax.set_title(r"acceleration follows curvature:  $\partial^2 u/\partial t^2 = v^2\,\partial^2 u/\partial x^2$",
                 loc="left", fontsize=12)
    fig.tight_layout()
    fig.savefig(f"{OUT}/curvature_pulls.png", dpi=200)
    print("wrote", f"{OUT}/curvature_pulls.png")
    return fig, None


# ------------------------------------------------------------ d'Alembert: a bump released from rest
@register
def dalembert_split():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    f = lambda s: np.exp(-s**2 / 0.5)
    v = 1.0
    x = np.linspace(-8, 8, 1000)
    ts = np.linspace(0, 5.5, 40)

    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.plot(x, f(x), color=GRAY, lw=1.2, ls=":", label="initial shape f(x), released from rest")
    (hr,) = ax.plot([], [], color=TEAL, lw=1.6, ls="--", label=r"$\frac{1}{2}f(x-vt)$")
    (hl,) = ax.plot([], [], color=ORANGE, lw=1.6, ls="--", label=r"$\frac{1}{2}f(x+vt)$")
    (u,) = ax.plot([], [], color=CARDINAL, lw=2.8, label="u(x, t)")
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(-8, 8); ax.set_ylim(-0.1, 1.3); ax.set_xlabel("x"); ax.set_ylabel("u")
    ax.legend(loc="upper right", frameon=False, fontsize=9.5)
    ax.set_title(r"the wave equation splits a bump in two:  $u = \frac{1}{2}[f(x-vt) + f(x+vt)]$",
                 loc="left", fontsize=11.5)
    fig.tight_layout()

    def update(i):
        t = ts[i]
        hr.set_data(x, 0.5 * f(x - v * t)); hl.set_data(x, 0.5 * f(x + v * t))
        u.set_data(x, 0.5 * (f(x - v * t) + f(x + v * t)))
        return hr, hl, u

    ani = FuncAnimation(fig, update, frames=len(ts), interval=100, blit=False)
    return fig, ani


# ------------------------------------------------------------ normal modes of a string (still)
@register
def string_modes():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    L = 1.0
    x = np.linspace(0, L, 600)
    lam = [r"$\lambda_1 = 2L$", r"$\lambda_2 = L$", r"$\lambda_3 = 2L/3$", r"$\lambda_4 = L/2$"]

    fig, axes = plt.subplots(4, 1, figsize=(6.6, 5.6), sharex=True)
    for ax, n in zip(axes, range(1, 5)):
        y = np.sin(n * np.pi * x / L)
        ax.plot(x, y, color=TEAL, lw=2.4); ax.plot(x, -y, color=TEAL, lw=1.4, alpha=0.45)
        ax.fill_between(x, y, -y, color=TEAL, alpha=0.08)
        nodes = np.arange(0, n + 1) * L / n
        ax.plot(nodes, np.zeros_like(nodes), "o", color=CARDINAL, ms=7, zorder=5)
        ax.axhline(0, color=GRAY, lw=0.6)
        ax.set_ylim(-1.3, 1.3); ax.set_yticks([]); ax.spines["left"].set_visible(False)
        plural = "s" if n - 1 != 1 else ""
        ax.text(1.03, 0, f"n = {n}\n{n-1} interior node{plural}\n" + lam[n - 1],
                transform=ax.get_yaxis_transform(), va="center", fontsize=10.5)
    for ax in axes[:-1]:
        ax.spines["bottom"].set_visible(False); ax.tick_params(axis="x", which="both", bottom=False)
    axes[-1].set_xlim(0, L); axes[-1].set_xticks([0, L]); axes[-1].set_xticklabels(["0", "L"]); axes[-1].set_xlabel("x")
    fig.suptitle(r"normal modes $X_n(x) = \sin(n\pi x/L)$ of a string fixed at both ends", fontsize=12.5)
    fig.tight_layout(rect=(0, 0, 0.8, 0.96))
    fig.savefig(f"{OUT}/string_modes.png", dpi=200)
    print("wrote", f"{OUT}/string_modes.png")
    return fig, None


# ------------------------------------------------------------ single modes vs sums of modes
@register
def mode_superposition():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    L, v = 1.0, 1.0
    x = np.linspace(0, L, 600)
    ts = np.linspace(0, 2 * L / v, 40, endpoint=False)     # one period of the fundamental
    X = lambda n: np.sin(n * np.pi * x / L)
    Tt = lambda n, t: np.cos(n * np.pi * v * t / L)
    combos = [[1], [3], [1, 2], [1, 2, 3]]
    titles = ["n = 1", "n = 3", "n = 1 + 2", "n = 1 + 2 + 3"]

    fig, axes = plt.subplots(2, 2, figsize=(8, 5.6))
    axes = axes.ravel()
    lines = []
    for ax, ttl in zip(axes, titles):
        (ln,) = ax.plot([], [], color=CARDINAL, lw=2.4); lines.append(ln)
        ax.plot([0, L], [0, 0], "o", color=GRAY, ms=6); ax.axhline(0, color=GRAY, lw=0.6)
        ax.set_xlim(0, L); ax.set_ylim(-2.6, 2.6); ax.set_yticks([])
        ax.set_title(ttl, fontsize=11.5, loc="left")
        ax.set_xticks([0, L]); ax.set_xticklabels(["0", "L"])
    fig.suptitle("single modes are standing waves; sums of modes are not", fontsize=12.5)
    fig.tight_layout()

    def update(i):
        t = ts[i]
        for ln, combo in zip(lines, combos):
            ln.set_data(x, sum(X(n) * Tt(n, t) for n in combo))
        return lines

    ani = FuncAnimation(fig, update, frames=len(ts), interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ plucked string from its modes
@register
def plucked_string():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    L, v, h, a = 1.0, 1.0, 1.0, 0.3            # length, speed, pluck height, pluck position
    N = 40                                      # modes kept
    n = np.arange(1, N + 1)
    A = 2 * h * L**2 * np.sin(n * np.pi * a / L) / (np.pi**2 * n**2 * a * (L - a))
    x = np.linspace(0, L, 600)
    modes = np.sin(np.outer(n, np.pi * x / L))
    omega = n * np.pi * v / L
    ts = np.linspace(0, 2 * L / v, 40, endpoint=False)
    f0 = np.where(x < a, h * x / a, h * (L - x) / (L - a))

    fig, (ax, bx) = plt.subplots(2, 1, figsize=(7.5, 5.8), gridspec_kw={"height_ratios": [1.5, 1]})
    ax.plot(x, f0, color=GRAY, lw=1.2, ls=":", label="initial pluck")
    (u,) = ax.plot([], [], color=CARDINAL, lw=2.8, label=r"$u(x,t)=\sum_n A_n \sin\frac{n\pi x}{L}\cos\omega_n t$")
    (m1,) = ax.plot([], [], color=TEAL, lw=1.4, ls="--", label="n = 1 term")
    (m2,) = ax.plot([], [], color=ORANGE, lw=1.4, ls="--", label="n = 2 term")
    ax.plot([0, L], [0, 0], "o", color=GRAY, ms=7); ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(-0.02, L + 0.02); ax.set_ylim(-1.15, 1.45); ax.set_yticks([]); ax.set_xlabel("x")
    ax.legend(loc="upper right", frameon=False, fontsize=9.5, ncol=2)
    ax.set_title("a string plucked at x = 0.3 L, rebuilt from its normal modes", loc="left", fontsize=11.5)
    bx.bar(n[:12], A[:12], color=[TEAL if c >= 0 else ORANGE for c in A[:12]], width=0.7)
    bx.axhline(0, color=GRAY, lw=0.6)
    bx.set_xticks(n[:12]); bx.set_xlabel("mode n"); bx.set_ylabel(r"$A_n$")
    bx.set_title(r"the pluck sets the recipe:  $A_n = \frac{2hL^2}{\pi^2 n^2 a(L-a)}\sin\frac{n\pi a}{L}$",
                 loc="left", fontsize=11.5)
    fig.tight_layout()

    def update(i):
        Tn = np.cos(omega * ts[i])
        u.set_data(x, (A * Tn) @ modes)
        m1.set_data(x, A[0] * Tn[0] * modes[0]); m2.set_data(x, A[1] * Tn[1] * modes[1])
        return u, m1, m2

    ani = FuncAnimation(fig, update, frames=len(ts), interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ square membrane modes (degeneracy)
@register
def membrane_modes():
    a = b = 1.0
    g = np.linspace(0, 1, 41)
    X, Y = np.meshgrid(g, g)
    pairs = [(1, 1), (2, 1), (1, 2), (2, 2)]
    shapes = [np.sin(n * np.pi * X / a) * np.sin(m * np.pi * Y / b) for n, m in pairs]
    ts = np.linspace(0, 1, 24, endpoint=False)             # one common period

    fig = plt.figure(figsize=(8.4, 6.4))
    axes = [fig.add_subplot(2, 2, i + 1, projection="3d") for i in range(4)]
    for ax, (n, m) in zip(axes, pairs):
        ratio = np.sqrt((n / a)**2 + (m / b)**2) / np.sqrt(2)
        ax.set_title(rf"(n, m) = ({n}, {m}),   $\omega_{{nm}}/\omega_{{11}}$ = {ratio:.2f}", fontsize=11, pad=0)
        ax.set_zlim(-1, 1); ax.view_init(elev=32, azim=-55); ax.set_box_aspect((1, 1, 0.5), zoom=1.35); ax.set_axis_off()
    fig.suptitle("normal modes of a square membrane; (2,1) and (1,2) share one frequency", fontsize=12.5, y=0.98)
    fig.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=0.9, wspace=0.0, hspace=0.05)
    surfs = []

    def update(i):
        for s in surfs:
            s.remove()
        surfs.clear()
        c = np.cos(2 * np.pi * ts[i])
        for ax, Z in zip(axes, shapes):
            surfs.append(ax.plot_surface(X, Y, c * Z, cmap="RdBu_r", vmin=-1, vmax=1,
                                         rstride=1, cstride=1, linewidth=0, antialiased=True))
        return surfs

    ani = FuncAnimation(fig, update, frames=len(ts), interval=110, blit=False)
    return fig, ani


if __name__ == "__main__":
    names = sys.argv[1:] or list(REGISTRY)
    for name in names:
        fig, ani = REGISTRY[name]()
        if ani is not None:
            path = f"{OUT}/{name}.gif"
            ani.save(path, writer=PillowWriter(fps=15), dpi=100)
            print("wrote", path)
        plt.close(fig)
