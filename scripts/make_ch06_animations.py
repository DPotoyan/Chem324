"""Chapter 6 animations and deck stills, authored ONCE here (same pipeline as chapters 2 to 5).

Each registered function builds one figure (and, for animations, a FuncAnimation) and is
self-contained: it uses only numpy, matplotlib.pyplot, FuncAnimation and the colour
constants below (plus local matplotlib / scipy imports). Running this script bakes the GIFs /
PNG stills for the slide decks into ch06/images/. `scripts/sync_ch06_cells.py` copies the SAME
function bodies into the `{code-cell}` blocks of the lecture pages (marker line
`# synced: <name>`), where animations play in the matplotlib JS player.

Run from the repo root:
    .venv/bin/python scripts/make_ch06_animations.py                 # bake everything
    .venv/bin/python scripts/make_ch06_animations.py box_trials      # a subset
    .venv/bin/python scripts/sync_ch06_cells.py                      # refresh page cells

Page weight: the JS player embeds every frame as a PNG, so keep animations to 24-48 frames.
Sync strips every line starting with `return`, so inner helpers must not use it (write a
lambda, or fill an array in place) and `update` must not return artists (use blit=False).

Lecture 6.1 (page ch06/01, deck slides/ch06/01) uses the figures in the "lecture 6.1" section; Lecture 6.2
(page ch06/02, deck slides/ch06/02) those in "lecture 6.2"; Lecture 6.3 (page ch06/03, deck slides/ch06/03) those
in "lecture 6.3".
Colours, kept the same in every figure of the chapter: the exact answer GRAY (curves) or black (levels), a trial
function TEAL, the best value CARDINAL, kinetic energy ORANGE and potential energy TEAL where an energy is split
(as in 4.2 and 5.1). Perturbation theory follows the matrix colours of Lecture 3.5: first order (a diagonal
element) PURPLE, second order (off-diagonal elements) ORANGE, the unperturbed problem GRAY, exact black. In 6.3
the initial state is TEAL, the final state ORANGE and the light PURPLE.
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = "ch06/images"
GIF_DPI = 200    # 2x: an 8 in figure bakes 1600 px wide, crisp full screen
TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"

REGISTRY = {}


def register(fn):
    REGISTRY[fn.__name__] = fn
    return fn


# ============================================================ lecture 6.1: the variational method

# ------------------------------------------------------------ the plan of the chapter: exact models, two ways to go beyond them, where they lead (still)
@register
def approx_roadmap():
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
            ax.text(x, y + 0.31 * dy, line, ha="center", va="center", fontsize=sizes[0] if k == 0 else sizes[1],
                    color=col if k == 0 else "k", weight="bold" if k == 0 else None, zorder=3)

    arrow = lambda p, q, col=GRAY: ax.annotate("", xy=q, xytext=p, zorder=1, arrowprops=dict(
        arrowstyle="-|>", color=col, lw=1.5, mutation_scale=15, shrinkA=2, shrinkB=2))
    x1, x2, x3, x4 = 1.15, 3.45, 6.15, 8.9
    yt, yb, ym = 3.1, 1.0, 2.05
    box(x1, ym, 1.9, 1.3, ["solved exactly", "box, spring, rotor", "hydrogen atom"], GRAY)
    box(x2, ym, 2.0, 1.3, ["everything else", "helium, atoms,", "molecules"], "k")
    box(x3, yt, 2.75, 1.25, ["variational method", r"guess $\phi$, minimize $\langle E\rangle$",
                             r"$\langle E\rangle \geq E_0$: Lecture 6.1"], TEAL)
    box(x3, yb, 2.75, 1.25, ["perturbation theory", r"$\hat{H} = \hat{H}^{(0)} + \hat{H}^{(1)}$",
                             "correct in steps: 6.2, 6.3"], PURPLE)
    box(x4, ym, 2.0, 1.3, ["chemistry", "orbitals, bonds, spectra", "Chapters 7 and 8"], ORANGE)
    arrow((x1 + 0.95, ym), (x2 - 1.0, ym))
    arrow((x2 + 1.0, ym + 0.25), (x3 - 1.38, yt - 0.1), TEAL)
    arrow((x2 + 1.0, ym - 0.25), (x3 - 1.38, yb + 0.1), PURPLE)
    arrow((x3 + 1.38, yt - 0.1), (x4 - 1.0, ym + 0.25), TEAL)
    arrow((x3 + 1.38, yb + 0.1), (x4 - 1.0, ym - 0.25), PURPLE)
    fig.savefig(f"{OUT}/approx_roadmap.png", dpi=200)
    print("wrote", f"{OUT}/approx_roadmap.png")
    return fig, None


# ------------------------------------------------------------ any state is a mixture of the exact levels, so its average energy lies above the lowest one (still)
@register
def weights_ladder():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 2001)
    phi = x**3 * (1 - x)                                            # a trial state in the box, pushed to the right
    phi = phi / np.sqrt(np.trapezoid(phi**2, x))
    psi = lambda n: np.sqrt(2) * np.sin(n * np.pi * x)
    c2 = np.array([np.trapezoid(phi * psi(n), x) ** 2 for n in range(1, 5)])
    Eavg = 0.5 * np.trapezoid(np.gradient(phi, x) ** 2, x) / (np.pi**2 / 2)   # average energy in units of E_1
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.2), gridspec_kw={"width_ratios": [1, 1.15], "wspace": 0.32})
    ax.plot([0, 0], [0, 2.5], color="k", lw=2.4); ax.plot([1, 1], [0, 2.5], color="k", lw=2.4)
    ax.plot([0, 1], [0, 0], color="k", lw=2.4)
    ax.plot(x, psi(1), color=GRAY, lw=2.2, ls=(0, (4, 3)))
    ax.fill_between(x, 0, phi, color=TEAL, alpha=0.25, lw=0)
    ax.plot(x, phi, color=TEAL, lw=2.6)
    ax.text(0.28, 1.36, r"$\psi_1$", color=GRAY, fontsize=14, ha="center")
    ax.text(0.9, 2.05, r"$\phi$", color=TEAL, fontsize=15, ha="center")
    ax.set_xlim(-0.06, 1.06); ax.set_ylim(-0.05, 2.5)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "$L$"]); ax.set_yticks([])
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False); ax.tick_params(labelsize=12, length=0)
    for n in range(1, 5):
        E = n * n
        bx.hlines(E, 0, 1.0, color="#ced4da", lw=1.2, zorder=1)
        bx.plot([0, c2[n - 1]], [E, E], color=PURPLE, lw=9, solid_capstyle="butt", zorder=3)
        bx.text(c2[n - 1] + 0.025, E, f"{c2[n - 1]:.2f}" if c2[n - 1] > 0.006 else f"{c2[n - 1]:.3f}", va="center",
                fontsize=12, color=PURPLE)
    bx.axhline(Eavg, color=CARDINAL, lw=1.8, ls=(0, (5, 3)), zorder=2)
    bx.text(1.0, Eavg + 0.35, rf"$\langle E\rangle = {Eavg:.2f}\,E_1$", color=CARDINAL, fontsize=13, ha="right", va="bottom")
    bx.set_xlim(0, 1.0); bx.set_ylim(0, 17.5)
    bx.set_yticks([1, 4, 9, 16]); bx.set_yticklabels(["$E_1$", "$E_2$", "$E_3$", "$E_4$"], fontsize=13)
    bx.set_xticks([0, 0.5, 1]); bx.tick_params(axis="x", labelsize=11)
    bx.set_xlabel(r"weight $|c_n|^2$", fontsize=12.5)
    fig.subplots_adjust(left=0.04, right=0.97, top=0.96, bottom=0.14)
    fig.savefig(f"{OUT}/weights_ladder.png", dpi=200)
    print("wrote", f"{OUT}/weights_ladder.png")
    return fig, None


# ------------------------------------------------------------ three guesses for the ground state of the box, ranked by their energy (still)
@register
def box_trials():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 1001)
    exact = np.sqrt(2) * np.sin(np.pi * x)
    unit = lambda f: f / np.sqrt(np.trapezoid(f**2, x))
    trials = [("(a) tent", unit(np.minimum(x, 1 - x)), 12 / np.pi**2),
              ("(b) parabola", unit(x * (1 - x)), 10 / np.pi**2),
              ("(c) two terms", unit(x * (1 - x) + 1.13314 * x**2 * (1 - x) ** 2), 4.93487481 / (np.pi**2 / 2))]
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.5), gridspec_kw={"wspace": 0.12})
    for ax, (name, f, E) in zip(axes, trials):
        ax.plot([0, 0], [0, 1.95], color="k", lw=2.2); ax.plot([1, 1], [0, 1.95], color="k", lw=2.2)
        ax.plot([0, 1], [0, 0], color="k", lw=2.2)
        ax.fill_between(x, exact, f, color=CARDINAL, alpha=0.35, lw=0)
        ax.plot(x, exact, color=GRAY, lw=4.5, alpha=0.55)
        ax.plot(x, f, color=TEAL, lw=2.2)
        ax.set_title(name, fontsize=13.5, color=TEAL, weight="bold")
        err = 100 * (E - 1)
        ax.text(0.5, 0.42, rf"$\langle E\rangle = {E:.3f}\,E_1$" if err > 0.05 else rf"$\langle E\rangle = {E:.5f}\,E_1$",
                ha="center", fontsize=13)
        ax.text(0.5, 0.14, f"{err:.1f}% high" if err > 0.05 else f"{err:.4f}% high", ha="center", fontsize=12, color=CARDINAL)
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.04, 1.95)
        ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "$L$"]); ax.set_yticks([])
        ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False); ax.tick_params(labelsize=12, length=0)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.09)
    fig.savefig(f"{OUT}/box_trials.png", dpi=200)
    print("wrote", f"{OUT}/box_trials.png")
    return fig, None


# ------------------------------------------------------------ hydrogen with one Gaussian: the energy of every exponent, and the best Gaussian against the exact 1s (still)
@register
def gaussian_hydrogen():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.2), gridspec_kw={"width_ratios": [1.15, 1], "wspace": 0.3})
    a = np.linspace(0.01, 1.0, 400)
    T, V = 1.5 * a, -2 * np.sqrt(2 * a / np.pi)                     # hartree, for the trial state exp(-alpha r^2)
    ax.axhline(0, color=GRAY, lw=0.8, ls=":")
    ax.plot(a, T, color=ORANGE, lw=2.4); ax.plot(a, V, color=TEAL, lw=2.4); ax.plot(a, T + V, color="k", lw=2.8)
    ax.axhline(-0.5, color=GRAY, lw=1.6, ls=(0, (5, 3)))
    a0 = 8 / (9 * np.pi)
    ax.plot([a0], [-4 / (3 * np.pi)], "o", color=CARDINAL, ms=9, zorder=5)
    ax.text(a0, -0.36, r"$-0.424$", color=CARDINAL, fontsize=13, ha="center", va="bottom")
    ax.text(0.99, -0.56, r"exact $-\frac{1}{2}$", color=GRAY, fontsize=13, ha="right", va="top")
    ax.text(0.72, 1.16, "kinetic", color=ORANGE, fontsize=13, ha="right")
    ax.text(0.3, -1.3, "potential", color=TEAL, fontsize=13, ha="left", va="top")
    ax.text(0.98, 0.0, "total", color="k", fontsize=13, ha="right", va="bottom")
    ax.set_xlim(0, 1.0); ax.set_ylim(-1.7, 1.6)
    ax.set_xlabel(r"exponent $\alpha$ ($a_0^{-2}$)", fontsize=12.5); ax.set_ylabel(r"average energy ($E_h$)", fontsize=12.5)
    ax.set_yticks([-1.5, -1, -0.5, 0, 0.5, 1, 1.5]); ax.tick_params(labelsize=10.5)
    r = np.linspace(0, 5, 500)
    bx.plot(r, np.exp(-r) / np.sqrt(np.pi), color=GRAY, lw=4.5, alpha=0.55)
    bx.plot(r, (2 * a0 / np.pi) ** 0.75 * np.exp(-a0 * r**2), color=TEAL, lw=2.4)
    bx.text(0.42, 0.47, r"exact $e^{-r/a_0}$", color=GRAY, fontsize=13)
    bx.text(1.75, 0.16, r"best Gaussian", color=TEAL, fontsize=13)
    bx.set_xlim(0, 5); bx.set_ylim(0, 0.6)
    bx.set_xlabel(r"$r$ ($a_0$)", fontsize=12.5); bx.set_ylabel(r"$\psi(r)$", fontsize=12.5); bx.tick_params(labelsize=10.5)
    fig.subplots_adjust(left=0.085, right=0.98, top=0.96, bottom=0.14)
    fig.savefig(f"{OUT}/gaussian_hydrogen.png", dpi=200)
    print("wrote", f"{OUT}/gaussian_hydrogen.png")
    return fig, None


# ------------------------------------------------------------ helium with a screened charge: the energy of every zeta, the bare charge and the best one (still)
@register
def helium_screening():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    Eh = 27.2114
    z = np.linspace(1.15, 2.35, 300)
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    ax.plot(z, (z**2 - 27 * z / 8) * Eh, color="k", lw=2.8)
    ax.axhline(-79.01, color=GRAY, lw=1.6, ls=(0, (5, 3)))
    ax.text(2.34, -79.25, "exact $-79.0$ eV", color=GRAY, fontsize=13, ha="right", va="top")
    ax.plot([2], [-2.75 * Eh], "o", color=GRAY, ms=9, zorder=5)
    ax.text(2.03, -2.75 * Eh - 0.1, r"$\zeta = 2$:  $-74.8$ eV", color=GRAY, fontsize=13, ha="left", va="top")
    zb = 27 / 16
    ax.plot([zb], [-zb**2 * Eh], "o", color=CARDINAL, ms=9, zorder=5)
    ax.text(zb, -zb**2 * Eh + 0.45, r"$\zeta = \frac{27}{16}$:  $-77.5$ eV", color=CARDINAL, fontsize=13, ha="center", va="bottom")
    ax.set_xlim(1.15, 2.35); ax.set_ylim(-80.6, -68)
    ax.set_xlabel(r"effective nuclear charge $\zeta$", fontsize=12.5); ax.set_ylabel(r"average energy (eV)", fontsize=12.5)
    ax.tick_params(labelsize=10.5)
    fig.subplots_adjust(left=0.11, right=0.97, top=0.96, bottom=0.14)
    fig.savefig(f"{OUT}/helium_screening.png", dpi=200)
    print("wrote", f"{OUT}/helium_screening.png")
    return fig, None


# ------------------------------------------------------------ the two-level problem: levels E1, E2 before and E-, E+ after mixing, and the energy of every mixture (still)
@register
def mixing_angle():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    H11, H22, H12 = 0.0, 1.0, -0.6
    mean, half = 0.5 * (H11 + H22), np.sqrt(0.25 * (H11 - H22) ** 2 + H12**2)
    Em, Ep = mean - half, mean + half
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.2), gridspec_kw={"width_ratios": [1, 1.5], "wspace": 0.12})
    # left: the two diagonal elements, and the two roots they turn into
    for y, lab in ((H11, "$E_1$"), (H22, "$E_2$")):
        ax.hlines(y, 0.0, 0.9, color=GRAY, lw=3.2)
        ax.text(-0.08, y, lab, ha="right", va="center", fontsize=14, color=GRAY)
    for y, lab, col in ((Em, "$E_-$", TEAL), (Ep, "$E_+$", ORANGE)):
        ax.hlines(y, 1.9, 2.8, color=col, lw=3.2)
        ax.text(2.88, y, lab, ha="left", va="center", fontsize=14, color=col)
    for y0, y1 in ((H11, Em), (H22, Ep)):
        ax.plot([0.9, 1.9], [y0, y1], color=GRAY, lw=1, ls=":")
    ax.set_xlim(-0.75, 3.5); ax.set_ylim(-0.55, 1.55); ax.axis("off")
    # right: the energy of cos(theta) f1 + sin(theta) f2
    th = np.linspace(-90, 90, 721); t = np.radians(th)
    E = H11 * np.cos(t) ** 2 + H22 * np.sin(t) ** 2 + H12 * np.sin(2 * t)
    for y, col in ((H11, GRAY), (H22, GRAY), (Em, TEAL), (Ep, ORANGE)):
        bx.axhline(y, color=col, lw=1, ls=":")
    bx.plot(th, E, color="k", lw=2.8)
    tp = np.degrees(0.5 * np.arctan2(2 * H12, H11 - H22))            # the angle of the highest mixture
    tm = tp + 90 if tp < 0 else tp - 90                              # the lowest one is perpendicular to it
    bx.plot([tm], [Em], "o", color=TEAL, ms=10, zorder=5); bx.plot([tp], [Ep], "o", color=ORANGE, ms=10, zorder=5)
    bx.plot([0], [H11], "o", color=GRAY, ms=8, zorder=5); bx.plot([-90, 90], [H22, H22], "o", color=GRAY, ms=8, zorder=5, clip_on=False)
    bx.text(tm, Em - 0.09, r"lowest", color=TEAL, fontsize=13, ha="center", va="top")
    bx.text(tp, Ep + 0.07, r"highest", color=ORANGE, fontsize=13, ha="center", va="bottom")
    bx.text(5, H11 + 0.05, r"$f_1$ alone", color=GRAY, fontsize=12.5, ha="left", va="bottom")
    bx.text(86, H22 + 0.06, r"$f_2$ alone", color=GRAY, fontsize=12.5, ha="right", va="bottom")
    bx.set_xlim(-90, 90); bx.set_ylim(-0.55, 1.55)
    bx.set_xticks([-90, -45, 0, 45, 90]); bx.set_xticklabels(["-90°", "-45°", "0°", "45°", "90°"])
    bx.set_yticks([]); bx.spines["left"].set_visible(False); bx.tick_params(labelsize=11.5)
    bx.set_xlabel(r"mixing angle $\theta$ in $\phi = \cos\theta\,f_1 + \sin\theta\,f_2$", fontsize=12.5)
    fig.subplots_adjust(left=0.02, right=0.97, top=0.96, bottom=0.15)
    fig.savefig(f"{OUT}/mixing_angle.png", dpi=200)
    print("wrote", f"{OUT}/mixing_angle.png")
    return fig, None


# ------------------------------------------------------------ hydrogen from one to five Gaussians: the energy steps down toward the exact one, and the sum grows a cusp (still)
@register
def gaussian_basis():
    from scipy.linalg import eigh
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    sets = {1: [0.28294], 2: [0.20153, 1.3325], 3: [0.15137, 0.68128, 4.5004],     # best exponents for N Gaussians
            4: [0.12195, 0.44454, 1.9623, 13.011], 5: [0.10307, 0.32723, 1.1647, 5.1236, 34.061]}
    r = np.linspace(0, 3.2, 600)
    Es, curves = {}, {}
    for N, al in sets.items():
        a, b = np.meshgrid(al, al)
        S = (np.pi / (a + b)) ** 1.5                                # overlap of exp(-a r^2) and exp(-b r^2)
        H = 3 * a * b / (a + b) * S - 2 * np.pi / (a + b)           # kinetic plus Coulomb, hartree
        E, C = eigh(H, S)
        Es[N] = E[0]
        curves[N] = abs(sum(c * np.exp(-e * r**2) for c, e in zip(C[:, 0], al)))
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.2), gridspec_kw={"width_ratios": [1, 1.05], "wspace": 0.3})
    ax.axhline(-0.5, color=GRAY, lw=1.6, ls=(0, (5, 3)))
    ax.text(5.45, -0.5035, r"exact $-\frac{1}{2}$", color=GRAY, fontsize=13, ha="right", va="top")
    for N, E in Es.items():
        ax.hlines(E, N - 0.32, N + 0.32, color=TEAL, lw=3.4)
        ax.text(N, E + 0.004, rf"${E:.4f}$", ha="center", va="bottom", fontsize=11.5, color=TEAL)
    ax.set_xlim(0.45, 5.55); ax.set_ylim(-0.512, -0.41)
    ax.set_xticks([1, 2, 3, 4, 5]); ax.set_yticks([-0.5, -0.48, -0.46, -0.44, -0.42]); ax.tick_params(labelsize=10.5)
    ax.set_xlabel("number of Gaussians", fontsize=12.5); ax.set_ylabel(r"lowest root ($E_h$)", fontsize=12.5)
    bx.plot(r, np.exp(-r) / np.sqrt(np.pi), color=GRAY, lw=4.5, alpha=0.55)
    for N, ls in ((1, (0, (1, 1.5))), (2, (0, (4, 2))), (3, "-")):
        bx.plot(r, curves[N], color=TEAL, lw=2.2, ls=ls)
    bx.text(0.2, 0.55, "exact", color=GRAY, fontsize=13, ha="left")
    for N, (xx, yy) in ((1, (0.05, 0.245)), (2, (0.05, 0.385)), (3, (0.3, 0.475))):
        bx.text(xx, yy, f"{N}", color=TEAL, fontsize=13, ha="left", va="center")
    bx.set_xlim(0, 3.2); bx.set_ylim(0, 0.6)
    bx.set_xlabel(r"$r$ ($a_0$)", fontsize=12.5); bx.set_ylabel(r"$\psi(r)$", fontsize=12.5); bx.tick_params(labelsize=10.5)
    fig.subplots_adjust(left=0.105, right=0.98, top=0.96, bottom=0.14)
    fig.savefig(f"{OUT}/gaussian_basis.png", dpi=200)
    print("wrote", f"{OUT}/gaussian_basis.png")
    return fig, None


# ============================================================ lecture 6.2: perturbation theory
# Model system of the lecture: a box of length L with a bump of height V_0 = 2 E_1 on its middle fifth
# (0.4 L to 0.6 L). Energies in units of the box ground-state energy E_1.

# ------------------------------------------------------------ a solved problem plus a small change: box + bump = box with a bump (still)
@register
def perturbation_split():
    N = 400; dx = 1 / N; x = np.arange(1, N) * dx
    V0 = 2.0                                                        # bump height, units of E_1
    bump = ((x > 0.4) & (x < 0.6)) * V0
    off = -0.5 / dx**2 * np.ones(N - 2)
    E1 = np.pi**2 / 2
    levels = np.linalg.eigvalsh(np.diag(1 / dx**2 + bump * E1) + np.diag(off, 1) + np.diag(off, -1))[:3] / E1
    fig = plt.figure(figsize=(9.6, 3.6))
    axes = [fig.add_axes([0.03 + 0.33 * j, 0.14, 0.27, 0.8]) for j in range(3)]
    for j, ax in enumerate(axes):
        ax.set_xlim(-0.08, 1.42); ax.set_ylim(-0.3, 10.6); ax.axis("off")
        if j != 1:
            ax.plot([0, 0], [0, 10.4], color="k", lw=2.4); ax.plot([1, 1], [0, 10.4], color="k", lw=2.4)
            ax.plot([0, 1], [0, 0], color="k", lw=2.4)
        else:
            ax.plot([0, 1], [0, 0], color=GRAY, lw=1, ls=":")
        if j > 0:
            ax.fill_between([0.4, 0.6], 0, V0, color=ORANGE, alpha=0.85, lw=0, zorder=3)
    for n in (1, 2, 3):
        axes[0].hlines(n * n, 0, 1, color=GRAY, lw=2.6)
        axes[0].text(1.07, n * n, rf"$E_{n}^{{(0)}}$", ha="left", va="center", fontsize=13.5, color=GRAY)
        axes[2].hlines(n * n, 0, 1, color=GRAY, lw=1.2, ls=(0, (3, 3)))
        axes[2].hlines(levels[n - 1], 0, 1, color="k", lw=2.6)
        axes[2].text(1.07, levels[n - 1], rf"$E_{n}$", ha="left", va="center", fontsize=13.5)
    axes[1].annotate("", xy=(0.72, V0), xytext=(0.72, 0), arrowprops=dict(arrowstyle="<->", color="k", lw=1.2, shrinkA=0, shrinkB=0))
    axes[1].text(0.77, V0 / 2, "$V_0$", ha="left", va="center", fontsize=14)
    for j, lab in enumerate((r"$\hat{H}^{(0)}$", r"$\hat{H}^{(1)}$", r"$\hat{H}$")):
        fig.text(0.134 + 0.33 * j, 0.03, lab, ha="center", va="bottom", fontsize=15)
    fig.text(0.335, 0.5, "+", ha="center", va="center", fontsize=30)
    fig.text(0.665, 0.5, "=", ha="center", va="center", fontsize=30)
    fig.savefig(f"{OUT}/perturbation_split.png", dpi=200)
    print("wrote", f"{OUT}/perturbation_split.png")
    return fig, None


# ------------------------------------------------------------ two levels and a coupling v: the exact levels, and the series cut off after second order (still)
@register
def two_level_series():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    v = np.linspace(0, 1.2, 300)                                     # coupling in units of the gap
    root = np.sqrt(1 + 4 * v**2)
    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    ax.axvspan(0.5, 1.2, color="#f1f3f5", lw=0, zorder=0)
    for y in (0, 1):
        ax.axhline(y, color=GRAY, lw=1.2, ls=":")
    ax.plot(v, -v**2, color=ORANGE, lw=2.4, ls=(0, (5, 2))); ax.plot(v, 1 + v**2, color=ORANGE, lw=2.4, ls=(0, (5, 2)))
    ax.plot(v, 0.5 * (1 - root), color="k", lw=2.8); ax.plot(v, 0.5 * (1 + root), color="k", lw=2.8)
    ax.text(1.19, 0.5 * (1 + root[-1]) - 0.2, "exact", fontsize=13, ha="right", va="top")
    ax.text(1.0, 2.12, "second order", fontsize=13, color=ORANGE, ha="right", va="bottom")
    ax.text(1.19, 0.5 * (1 - root[-1]) + 0.2, "exact", fontsize=13, ha="right", va="bottom")
    ax.text(1.0, -1.12, "second order", fontsize=13, color=ORANGE, ha="right", va="top")
    ax.set_xlim(0, 1.2); ax.set_ylim(-1.5, 2.5)
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", r"$\Delta/2$", r"$\Delta$"])
    ax.set_yticks([0, 1]); ax.set_yticklabels([r"$E_1^{(0)}$", r"$E_2^{(0)}$"]); ax.tick_params(labelsize=13)
    ax.set_xlabel(r"coupling $|v|$", fontsize=13)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.96, bottom=0.15)
    fig.savefig(f"{OUT}/two_level_series.png", dpi=200)
    print("wrote", f"{OUT}/two_level_series.png")
    return fig, None


# ------------------------------------------------------------ first order: the shift is the bump times the chance of finding the particle on it (still)
@register
def first_order_density():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 1001)
    V0 = 2.0
    inside = (x >= 0.4) & (x <= 0.6)
    fig = plt.figure(figsize=(9.6, 3.9))
    P = []
    for j, n in enumerate((1, 2, 3)):
        ax = fig.add_axes([0.02 + 0.235 * j, 0.1, 0.2, 0.78])
        rho = 2 * np.sin(n * np.pi * x) ** 2
        P.append(np.trapezoid(rho[inside], x[inside]))
        ax.axvspan(0.4, 0.6, color=ORANGE, alpha=0.18, lw=0)
        ax.fill_between(x, 0, rho, color=TEAL, alpha=0.22, lw=0)
        ax.fill_between(x[inside], 0, rho[inside], color=PURPLE, alpha=0.85, lw=0)
        ax.plot(x, rho, color=TEAL, lw=2.2)
        ax.plot([0, 0], [0, 2.75], color="k", lw=2.2); ax.plot([1, 1], [0, 2.75], color="k", lw=2.2); ax.plot([0, 1], [0, 0], color="k", lw=2.2)
        ax.text(0.5, 2.3, f"{P[-1]:.2f}", ha="center", va="bottom", fontsize=14, color=PURPLE)
        ax.set_title(rf"$n = {n}$", fontsize=14)
        ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.05, 2.75)
        ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "$L$"]); ax.set_yticks([])
        ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False); ax.tick_params(labelsize=12, length=0)
    bx = fig.add_axes([0.79, 0.1, 0.19, 0.78])
    for n in (1, 2, 3):
        E0, E1 = n * n, n * n + V0 * P[n - 1]
        bx.hlines(E0, 0, 1, color=GRAY, lw=2.6); bx.hlines(E1, 1.6, 2.6, color=PURPLE, lw=2.6)
        bx.plot([1, 1.6], [E0, E1], color=GRAY, lw=1, ls=":")
        bx.text(-0.12, E0, rf"$E_{n}^{{(0)}}$", ha="right", va="center", fontsize=12.5, color=GRAY)
        bx.text(2.1, E1 + 0.25, rf"$+{V0 * P[n - 1]:.2f}$", ha="center", va="bottom", fontsize=12.5, color=PURPLE)
    bx.set_xlim(-1.0, 2.7); bx.set_ylim(0, 10.6); bx.axis("off")
    fig.savefig(f"{OUT}/first_order_density.png", dpi=200)
    print("wrote", f"{OUT}/first_order_density.png")
    return fig, None


# ------------------------------------------------------------ the two lowest levels against the height of the bump: exact, first order, second order (still)
@register
def orders_vs_strength():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    N = 300; dx = 1 / N; x = np.arange(1, N) * dx
    E1 = np.pi**2 / 2
    shape = ((x > 0.4) & (x < 0.6)).astype(float)
    off = -0.5 / dx**2 * np.ones(N - 2)
    K0 = np.diag(1 / dx**2 * np.ones(N - 1)) + np.diag(off, 1) + np.diag(off, -1)
    V0 = np.linspace(0, 10, 41)
    exact = np.array([np.linalg.eigvalsh(K0 + np.diag(v * E1 * shape))[:2] / E1 for v in V0])
    K = 40                                                           # box states kept in the second-order sum
    psi = np.array([np.sqrt(2) * np.sin(k * np.pi * x) for k in range(1, K + 1)])
    H1 = psi @ (shape * psi).T * dx                                   # <k|H1|n> for a bump of unit height
    E0 = np.arange(1, K + 1) ** 2.0
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    ax.axvspan(3, 10, color="#f1f3f5", lw=0, zorder=0)
    for n in (1, 2):
        e1 = H1[n - 1, n - 1]
        e2 = sum(H1[k, n - 1] ** 2 / (E0[n - 1] - E0[k]) for k in range(K) if k != n - 1)
        ax.plot(V0, n * n + e1 * V0, color=PURPLE, lw=2.2, ls=(0, (5, 2)), label="first order" if n == 1 else None)
        ax.plot(V0, n * n + e1 * V0 + e2 * V0**2, color=ORANGE, lw=2.2, ls=(0, (1, 1.2)), label="second order" if n == 1 else None)
        ax.plot(V0, exact[:, n - 1], color="k", lw=2.8, label="exact" if n == 1 else None)
        ax.text(0.25, n * n + (0.3 if n == 2 else -0.22), rf"$n = {n}$", ha="left", va="center", fontsize=13)
    ax.set_xlim(0, 10); ax.set_ylim(0.6, 5.4)
    ax.set_xticks([0, 2, 4, 6, 8, 10]); ax.set_yticks([1, 2, 3, 4, 5]); ax.tick_params(labelsize=11)
    ax.set_xlabel(r"bump height $V_0$ (units of $E_1^{(0)}$)", fontsize=12.5)
    ax.set_ylabel(r"energy (units of $E_1^{(0)}$)", fontsize=12.5)
    ax.legend(loc="lower right", frameon=False, fontsize=12.5, handlelength=2.6)
    fig.subplots_adjust(left=0.09, right=0.97, top=0.97, bottom=0.14)
    fig.savefig(f"{OUT}/orders_vs_strength.png", dpi=200)
    print("wrote", f"{OUT}/orders_vs_strength.png")
    return fig, None


# ------------------------------------------------------------ a box in a field: the ground state borrows a little of the next state and leans downhill (still)
@register
def tilt_mixing():
    N = 400; dx = 1 / N; x = np.arange(1, N) * dx
    E1 = np.pi**2 / 2
    F = 3.0                                                          # H1 = F (x - L/2), F in units of E_1 / L
    off = -0.5 / dx**2 * np.ones(N - 2)
    w, vec = np.linalg.eigh(np.diag(1 / dx**2 + F * E1 * (x - 0.5)) + np.diag(off, 1) + np.diag(off, -1))
    exact = vec[:, 0] / np.sqrt(dx) * np.sign(vec[N // 2, 0])
    p1, p2 = np.sqrt(2) * np.sin(np.pi * x), np.sqrt(2) * np.sin(2 * np.pi * x)
    c2 = F * np.trapezoid(p2 * (x - 0.5) * p1, x) / (1 - 4)          # <2|H1|1> / (E_1 - E_2)
    first = p1 + c2 * p2
    fig = plt.figure(figsize=(9.6, 3.4))
    axes = [fig.add_axes([0.03 + 0.365 * j, 0.13, 0.21, 0.8]) for j in range(3)]
    for j, ax in enumerate(axes):
        ax.set_xlim(-0.08, 1.08); ax.set_ylim(-2.6, 1.95); ax.axis("off")
        tilt = 0.4 if j == 2 else 0.0                                # the floor: flat, or sloping up to the right
        ax.plot([0, 0], [-2.1 - tilt, 1.9], color="k", lw=2.4); ax.plot([1, 1], [-2.1 + tilt, 1.9], color="k", lw=2.4)
        ax.plot([0, 1], [-2.1 - tilt, -2.1 + tilt], color="k", lw=2.4)
        ax.plot([0, 1], [0, 0], color=GRAY, lw=0.9, ls=":")
    axes[0].fill_between(x, 0, p1, color=GRAY, alpha=0.2, lw=0); axes[0].plot(x, p1, color=GRAY, lw=2.6)
    axes[1].fill_between(x, 0, p2, color=ORANGE, alpha=0.2, lw=0); axes[1].plot(x, p2, color=ORANGE, lw=2.6)
    axes[2].plot(x, p1, color=GRAY, lw=1.4, ls=(0, (3, 3)))
    axes[2].plot(x, exact, color="k", lw=5, alpha=0.3)
    axes[2].plot(x, first, color=PURPLE, lw=2.2)
    for j, lab in enumerate((r"$\psi_1^{(0)}$", r"$\psi_2^{(0)}$", r"$\psi_1$")):
        fig.text(0.135 + 0.365 * j, 0.02, lab, ha="center", va="bottom", fontsize=15,
                 color=(GRAY, ORANGE, PURPLE)[j])
    fig.text(0.318, 0.6, rf"$+\ {c2:.2f}\,\times$", ha="center", va="center", fontsize=19)
    fig.text(0.683, 0.6, r"$\approx$", ha="center", va="center", fontsize=30)
    fig.savefig(f"{OUT}/tilt_mixing.png", dpi=200)
    print("wrote", f"{OUT}/tilt_mixing.png")
    return fig, None


# ------------------------------------------------------------ second order: every other level pushes this one away, the nearest the hardest (still)
@register
def level_repulsion():
    from matplotlib.patches import FancyArrowPatch
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 4.2), gridspec_kw={"wspace": 0.1})
    E = [0.0, 1.5, 2.6, 3.4]                                         # unperturbed levels, any units
    for ax, n in zip(axes, (0, 1)):
        shift = 0.0
        for k, Ek in enumerate(E):
            col = "k" if k == n else GRAY
            ax.hlines(Ek, 0, 2.6, color=col, lw=3 if k == n else 2.2)
            ax.text(-0.12, Ek, rf"$E_{k + 1}^{{(0)}}$", ha="right", va="center", fontsize=13.5, color=col)
            if k == n:
                continue
            push = 0.42 / abs(Ek - E[n])                             # the size of this level's push, as 1 / gap
            sgn = -1 if Ek > E[n] else 1                             # levels above push down, levels below push up
            shift += sgn * push
            xk = 0.55 + 0.6 * (k if k < n else k - 1)
            ax.add_patch(FancyArrowPatch((xk, Ek - 0.1 * sgn * -1), (xk, E[n] - 0.06 * sgn), arrowstyle="simple",
                                         mutation_scale=14 + 26 * push, color=ORANGE, alpha=0.85, lw=0, zorder=3))
        ax.hlines(E[n] + shift, 2.95, 4.1, color=ORANGE, lw=3)
        ax.plot([2.6, 2.95], [E[n], E[n] + shift], color=GRAY, lw=1, ls=":")
        ax.hlines(E[n], 2.95, 4.1, color=GRAY, lw=1.2, ls=(0, (3, 3)))
        ax.text(3.52, E[n] + shift - 0.16, rf"$E_{n + 1}^{{(2)}} < 0$" if n == 0 else rf"$E_{n + 1}^{{(2)}}$",
                ha="center", va="top", fontsize=13.5, color=ORANGE)
        ax.set_xlim(-0.9, 4.3); ax.set_ylim(-0.95, 3.75); ax.axis("off")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    fig.savefig(f"{OUT}/level_repulsion.png", dpi=200)
    print("wrote", f"{OUT}/level_repulsion.png")
    return fig, None


# ------------------------------------------------------------ a charged oscillator in a field: the same parabola, moved over and down (still)
@register
def field_oscillator():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4.2, 5.4, 600)
    f = 1.3                                                          # q E in units where hbar = mu = omega = 1 (k = 1)
    x0, drop = f, -0.5 * f**2
    fig, ax = plt.subplots(figsize=(8.0, 4.6))
    ax.plot(x, 0.5 * x**2, color=GRAY, lw=2.2, ls=(0, (5, 3)))
    ax.plot(x, 0.5 * x**2 - f * x, color="k", lw=2.8)
    for v in range(3):
        E = v + 0.5
        xt = np.sqrt(2 * E)
        ax.hlines(E, -xt, xt, color=GRAY, lw=1.6, ls=(0, (5, 3)))
        ax.hlines(E + drop, x0 - xt, x0 + xt, color="k", lw=2.4)
        ax.text(x0 + max(xt, 2.1) + 0.15, E + drop, rf"$v = {v}$", fontsize=12.5, va="center", ha="left")
    xg = np.linspace(-2.1, 2.1, 200)                                 # the ground state, drawn near its own well
    g = 0.55 * np.exp(-0.5 * xg**2)
    ax.fill_between(xg, 0.5, 0.5 + g, color=GRAY, alpha=0.18, lw=0)
    ax.fill_between(xg + x0, 0.5 + drop, 0.5 + drop + g, color=TEAL, alpha=0.3, lw=0)
    ax.plot(xg + x0, 0.5 + drop + g, color=TEAL, lw=2.2)
    ax.annotate("", xy=(x0, -1.25), xytext=(0, -1.25), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.6, shrinkA=0, shrinkB=0))
    ax.text(x0 / 2, -1.32, r"$q\mathcal{E}/k$", ha="center", va="top", fontsize=13.5, color=ORANGE)
    ax.plot([0, 0], [0, -1.25], color=GRAY, lw=0.8, ls=":"); ax.plot([x0, x0], [drop, -1.25], color=GRAY, lw=0.8, ls=":")
    ax.annotate("", xy=(-2.6, drop), xytext=(-2.6, 0), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.6, shrinkA=0, shrinkB=0))
    ax.plot([-2.6, 0], [0, 0], color=GRAY, lw=0.8, ls=":"); ax.plot([-2.6, x0], [drop, drop], color=GRAY, lw=0.8, ls=":")
    ax.text(-2.72, drop / 2, r"$q^2\mathcal{E}^2/2k$", ha="right", va="center", fontsize=13.5, color=ORANGE)
    ax.set_xlim(-4.6, 5.4); ax.set_ylim(-1.75, 3.6)
    ax.set_xticks([0]); ax.set_xticklabels(["0"]); ax.set_yticks([]); ax.tick_params(labelsize=12)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("$x$", fontsize=13)
    fig.subplots_adjust(left=0.03, right=0.98, top=0.98, bottom=0.12)
    fig.savefig(f"{OUT}/field_oscillator.png", dpi=200)
    print("wrote", f"{OUT}/field_oscillator.png")
    return fig, None


# ------------------------------------------------------------ helium, order by order: the repulsion as a perturbation of two hydrogenlike electrons (still)
@register
def helium_orders():
    Eh = 27.2114
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.3), gridspec_kw={"width_ratios": [1, 1.5], "wspace": 0.28})
    for a_ in (ax, bx):
        for sp in ("top", "right", "bottom"):
            a_.spines[sp].set_visible(False)
        a_.set_xticks([]); a_.tick_params(labelsize=11)
    e0, e1 = -4 * Eh, -2.75 * Eh
    ax.hlines(e0, 0, 1, color=GRAY, lw=3.2); ax.hlines(e1, 1.6, 2.6, color=PURPLE, lw=3.2)
    ax.text(0.5, e0 - 1.2, "zeroth", ha="center", va="top", fontsize=13, color=GRAY)
    ax.text(2.1, e1 + 1.2, "first", ha="center", va="bottom", fontsize=13, color=PURPLE)
    ax.annotate("", xy=(1.3, e1), xytext=(1.3, e0), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.8, mutation_scale=16, shrinkA=0, shrinkB=0))
    ax.text(1.2, 0.5 * (e0 + e1), r"$+34.0$", ha="right", va="center", fontsize=13, color=PURPLE)
    ax.axhline(-79.01, color="k", lw=1.2, ls=(0, (5, 3)))
    ax.set_xlim(-0.2, 2.8); ax.set_ylim(-114, -68); ax.set_yticks([-110, -100, -90, -80, -70])
    ax.set_ylabel("energy of helium (eV)", fontsize=12.5)
    cols = [("first", e1, PURPLE), ("second", (-2.75 - 0.157666) * Eh, ORANGE), ("variational", -(27 / 16) ** 2 * Eh, TEAL)]
    bx.axhline(-79.01, color="k", lw=1.2, ls=(0, (5, 3)))
    bx.text(3.45, -79.12, r"exact $-79.01$", ha="right", va="top", fontsize=13)
    for j, (name, E, col) in enumerate(cols):
        bx.hlines(E, j + 0.1, j + 0.9, color=col, lw=3.2)
        bx.text(j + 0.5, E + 0.18, rf"${E:.2f}$", ha="center", va="bottom", fontsize=13, color=col)
        bx.text(j + 0.5, -73.3, name, ha="center", va="bottom", fontsize=13, color=col)
    bx.set_xlim(-0.1, 3.5); bx.set_ylim(-80.4, -72.5); bx.set_yticks([-80, -78, -76, -74])
    fig.subplots_adjust(left=0.09, right=0.98, top=0.97, bottom=0.05)
    fig.savefig(f"{OUT}/helium_orders.png", dpi=200)
    print("wrote", f"{OUT}/helium_orders.png")
    return fig, None


# ============================================================ lecture 6.3: time-dependent perturbations and selection rules
# Colours: the initial state TEAL, the final state ORANGE, the light PURPLE, first order PURPLE dashed.

# ------------------------------------------------------------ the plan: light on a stationary state, two conditions, a rate (still)
@register
def transition_map():
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
            ax.text(x, y + 0.33 * dy, line, ha="center", va="center", fontsize=sizes[0] if k == 0 else sizes[1],
                    color=col if k == 0 else "k", weight="bold" if k == 0 else None, zorder=3)

    arrow = lambda p, q, col=GRAY: ax.annotate("", xy=q, xytext=p, zorder=1, arrowprops=dict(
        arrowstyle="-|>", color=col, lw=1.5, mutation_scale=15, shrinkA=2, shrinkB=2))
    x1, x2, x3, x4 = 1.05, 3.5, 6.25, 8.95
    yt, yb, ym = 3.1, 1.0, 2.05
    box(x1, ym, 1.75, 1.3, ["state $i$", "stationary:", "nothing moves"], TEAL)
    box(x2, ym, 2.45, 1.3, ["light on", r"$\hat{V}(t) = -\hat{M}\,\mathcal{E}\cos\omega t$", r"the $c_n(t)$ start to move"], PURPLE)
    box(x3, yt, 2.35, 1.2, ["resonance", r"$\hbar\omega = E_f - E_i$"], "k", sizes=(13, 12.5))
    box(x3, yb, 2.35, 1.2, ["selection rule", r"$\langle f|\hat{M}|i\rangle \neq 0$"], "k", sizes=(13, 12.5))
    box(x4, ym, 2.0, 1.3, ["state $f$", r"rate $\propto |\langle f|\hat{M}|i\rangle|^2$", r"$\times$ intensity"], ORANGE)
    arrow((x1 + 0.88, ym), (x2 - 1.23, ym))
    arrow((x2 + 1.23, ym + 0.25), (x3 - 1.18, yt - 0.1))
    arrow((x2 + 1.23, ym - 0.25), (x3 - 1.18, yb + 0.1))
    arrow((x3 + 1.18, yt - 0.1), (x4 - 1.0, ym + 0.25))
    arrow((x3 + 1.18, yb + 0.1), (x4 - 1.0, ym - 0.25))
    fig.savefig(f"{OUT}/transition_map.png", dpi=200)
    print("wrote", f"{OUT}/transition_map.png")
    return fig, None


# ------------------------------------------------------------ the wave is a thousand times longer than the molecule: across it the field is uniform (still)
@register
def dipole_approximation():
    from matplotlib.patches import Circle, Rectangle
    fig = plt.figure(figsize=(9.6, 3.8))
    ax = fig.add_axes([0.02, 0.05, 0.56, 0.9]); bx = fig.add_axes([0.66, 0.17, 0.32, 0.7])
    x = np.linspace(0, 1000, 600)
    ax.plot([0, 1000], [0, 0], color=GRAY, lw=0.9)
    ax.plot(x, np.sin(2 * np.pi * x / 500), color=PURPLE, lw=2.4)
    for xa in np.arange(31.25, 1000, 62.5):
        ya = np.sin(2 * np.pi * xa / 500)
        ax.annotate("", xy=(xa, ya), xytext=(xa, 0), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.3, mutation_scale=10,
                                                                    shrinkA=0, shrinkB=0, alpha=0.75))
    ax.annotate("", xy=(625, -1.4), xytext=(125, -1.4), arrowprops=dict(arrowstyle="<->", color="k", lw=1.2, shrinkA=0, shrinkB=0))
    ax.text(375, -1.5, r"$\lambda = 500$ nm", ha="center", va="top", fontsize=13.5)
    xm = 125.0                                                       # the molecule sits at a crest
    ax.add_patch(Rectangle((xm - 16, 0.7), 32, 0.5, fc="none", ec="k", lw=1.4, zorder=5))
    ax.plot([xm], [0.95], "o", color="k", ms=3.5, zorder=6)
    ax.set_xlim(-20, 1020); ax.set_ylim(-2.0, 1.6); ax.axis("off")
    # the zoom: two atoms, a dipole, and the same field everywhere
    for xa in np.linspace(0.08, 0.92, 7):
        bx.annotate("", xy=(xa, 0.93), xytext=(xa, 0.07), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.6, mutation_scale=13,
                                                                          shrinkA=0, shrinkB=0, alpha=0.45))
    bx.plot([0.36, 0.64], [0.4, 0.6], color="k", lw=3, zorder=3)
    bx.add_patch(Circle((0.36, 0.4), 0.085, fc=TEAL, ec="k", lw=1.2, zorder=4))
    bx.add_patch(Circle((0.64, 0.6), 0.055, fc="#dee2e6", ec="k", lw=1.2, zorder=4))
    bx.annotate("", xy=(0.69, 0.42), xytext=(0.41, 0.22), arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=2.2, mutation_scale=16,
                                                                          shrinkA=0, shrinkB=0), zorder=5)
    bx.text(0.6, 0.25, r"$M$", color=CARDINAL, fontsize=15, ha="left", va="center")
    bx.text(0.5, 1.03, r"$\mathcal{E}(t)$", color=PURPLE, fontsize=15, ha="center", va="bottom")
    bx.annotate("", xy=(0.74, -0.06), xytext=(0.26, -0.06), annotation_clip=False,
                arrowprops=dict(arrowstyle="<->", color="k", lw=1.2, shrinkA=0, shrinkB=0))
    bx.text(0.5, -0.1, "0.3 nm", ha="center", va="top", fontsize=13.5)
    bx.set_xlim(0, 1); bx.set_ylim(0, 1); bx.set_xticks([]); bx.set_yticks([]); bx.set_aspect("equal")
    for sp in bx.spines.values():
        sp.set_visible(True); sp.set_linewidth(1.4)
    # zoom lines from the small box on the wave to the panel
    from matplotlib.patches import ConnectionPatch
    for ya, yb_ in ((1.2, 1.0), (0.7, 0.0)):
        fig.add_artist(ConnectionPatch(xyA=(xm + 16, ya), coordsA=ax.transData, xyB=(0, yb_), coordsB=bx.transData,
                                       color=GRAY, lw=0.9, ls=":"))
    fig.savefig(f"{OUT}/dipole_approximation.png", dpi=200)
    print("wrote", f"{OUT}/dipole_approximation.png")
    return fig, None


# ------------------------------------------------------------ light at resonance carries a particle in a box from state 1 to state 2: density, populations, dipole (animation, 36 frames)
@register
def drive_two_level():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(0, 1, 300)
    p1, p2 = np.sqrt(2) * np.sin(np.pi * x), np.sqrt(2) * np.sin(2 * np.pi * x)
    frames, swings = 36, 4                                           # one pi pulse; the dipole swings four times during it
    s = np.linspace(0, 1, 400)                                       # time in units of the pulse length pi / Omega
    x12 = -16 / (9 * np.pi**2)
    dip = lambda u: x12 * np.sin(np.pi * u) * np.sin(2 * np.pi * swings * u)   # <x> - L/2 during the pulse
    fig = plt.figure(figsize=(8.6, 4.0))
    ax = fig.add_axes([0.05, 0.13, 0.4, 0.8])
    bx = fig.add_axes([0.58, 0.6, 0.39, 0.33]); cx = fig.add_axes([0.58, 0.13, 0.39, 0.33])
    ax.plot([0, 0], [0, 4.2], color="k", lw=2.4); ax.plot([1, 1], [0, 4.2], color="k", lw=2.4); ax.plot([0, 1], [0, 0], color="k", lw=2.4)
    line, = ax.plot(x, p1**2, color=TEAL, lw=2.4)
    fill = [ax.fill_between(x, 0, p1**2, color=TEAL, alpha=0.3, lw=0)]
    ax.set_xlim(-0.05, 1.05); ax.set_ylim(-0.05, 4.2); ax.set_xticks([0, 1]); ax.set_xticklabels(["0", "$L$"]); ax.set_yticks([])
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False); ax.tick_params(labelsize=12, length=0)
    ax.set_ylabel(r"$|\Psi(x, t)|^2$", fontsize=13)
    bx.plot(s, np.cos(np.pi * s / 2) ** 2, color=TEAL, lw=2.2); bx.plot(s, np.sin(np.pi * s / 2) ** 2, color=ORANGE, lw=2.2)
    bx.text(0.03, 0.8, r"$|c_1|^2$", color=TEAL, fontsize=12.5, va="center"); bx.text(0.97, 0.8, r"$|c_2|^2$", color=ORANGE, fontsize=12.5, va="center", ha="right")
    d1, = bx.plot([0], [1], "o", color=TEAL, ms=8, clip_on=False); d2, = bx.plot([0], [0], "o", color=ORANGE, ms=8, clip_on=False)
    bx.set_xlim(0, 1); bx.set_ylim(-0.05, 1.08); bx.set_xticks([]); bx.set_yticks([0, 1]); bx.tick_params(labelsize=10.5)
    cx.axhline(0, color=GRAY, lw=0.8)
    cx.plot(s, dip(s), color="#ced4da", lw=1.4)
    trace, = cx.plot([], [], color="k", lw=2.0)
    d3, = cx.plot([0], [0], "o", color="k", ms=7, clip_on=False)
    cx.set_xlim(0, 1); cx.set_ylim(-0.22, 0.22); cx.set_xticks([0, 1]); cx.set_xticklabels(["0", r"$\pi/\Omega$"]); cx.set_yticks([])
    cx.spines["left"].set_visible(False); cx.tick_params(labelsize=12)
    cx.set_xlabel("time", fontsize=12.5); cx.set_ylabel(r"$\langle x\rangle - L/2$", fontsize=12.5)

    def update(k):
        u = k / (frames - 1)
        c1, c2 = np.cos(np.pi * u / 2), np.sin(np.pi * u / 2)
        rho = c1**2 * p1**2 + c2**2 * p2**2 + 2 * c1 * c2 * np.sin(2 * np.pi * swings * u) * p1 * p2
        line.set_ydata(rho)
        fill[0].remove()
        fill[0] = ax.fill_between(x, 0, rho, color=TEAL, alpha=0.3, lw=0)
        d1.set_data([u], [c1**2]); d2.set_data([u], [c2**2])
        m = s <= u
        trace.set_data(s[m], dip(s[m])); d3.set_data([u], [dip(u)])

    ani = FuncAnimation(fig, update, frames=frames, interval=110, blit=False)
    return fig, ani


drive_two_level.fps = 9


# ------------------------------------------------------------ first order: the probability against time for three detunings, and against frequency at two times (still)
@register
def resonance_curves():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.1), gridspec_kw={"wspace": 0.22})
    t = np.linspace(0, 4, 500)
    ax.plot(t, t**2, color=ORANGE, lw=2.8, label="on resonance")
    ax.plot(t, np.sin(t) ** 2, color=ORANGE, lw=2.2, ls=(0, (5, 2)), label="off resonance")
    ax.plot(t, np.sin(2 * t) ** 2 / 4, color=ORANGE, lw=2.2, ls=(0, (1, 1.2)), label="farther off")
    ax.legend(loc="upper right", frameon=False, fontsize=12.5, handlelength=2.6)
    ax.set_xlim(0, 4); ax.set_ylim(0, 2.4); ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("time $t$ the light has been on", fontsize=12.5); ax.set_ylabel(r"probability of state $f$", fontsize=12.5)
    w = np.linspace(-3.2 * np.pi, 3.2 * np.pi, 900)
    line = lambda T: T**2 * np.sinc(w * T / (2 * np.pi)) ** 2          # sin^2(w T / 2) / (w / 2)^2
    for T, a in ((2.0, 0.22), (1.0, 0.45)):
        bx.fill_between(w, 0, line(T), color=ORANGE, alpha=a, lw=0)
        bx.plot(w, line(T), color=ORANGE, lw=2.2)
    bx.text(0.9, 3.75, "$2t$", color=ORANGE, fontsize=14, ha="left"); bx.text(3.2, 0.62, "$t$", color=ORANGE, fontsize=14, ha="left")
    bx.set_xlim(-3.2 * np.pi, 3.2 * np.pi); bx.set_ylim(0, 4.3); bx.set_yticks([])
    bx.set_xticks([-2 * np.pi, 0, 2 * np.pi])
    bx.set_xticklabels([r"$\omega_{fi} - 2\pi/t$", r"$\omega_{fi}$", r"$\omega_{fi} + 2\pi/t$"], fontsize=13)
    bx.set_xlabel(r"frequency $\omega$ of the light", fontsize=12.5)
    fig.subplots_adjust(left=0.05, right=0.98, top=0.97, bottom=0.17)
    fig.savefig(f"{OUT}/resonance_curves.png", dpi=200)
    print("wrote", f"{OUT}/resonance_curves.png")
    return fig, None


# ------------------------------------------------------------ two levels driven exactly: complete transfer on resonance, partial and faster off it; first order for comparison (still)
@register
def rabi_flop():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    wt = np.linspace(0, 4 * np.pi, 800)                              # Omega t
    fig, ax = plt.subplots(figsize=(8.4, 4.3))
    ax.axvline(np.pi, color=GRAY, lw=0.9, ls=":")
    for d, ls, lab, pos in ((0, "-", r"$\delta = 0$", (1.5 * np.pi, 0.9)), (1, (0, (5, 2)), r"$\delta = \Omega$", (5.9, 0.52))):
        W = np.sqrt(1 + d * d)
        ax.plot(wt, np.sin(W * wt / 2) ** 2 / W**2, color=ORANGE, lw=2.8 if d == 0 else 2.2, ls=ls)
        ax.text(*pos, lab, color=ORANGE, fontsize=13, ha="left", va="bottom")
    m = wt <= 2.05
    ax.plot(wt[m], (wt[m] / 2) ** 2, color=PURPLE, lw=2.2, ls=(0, (5, 2)))
    ax.text(0.15, 1.06, "first order", color=PURPLE, fontsize=13, ha="left", va="center")
    ax.plot([np.pi], [1], "o", color=CARDINAL, ms=9, zorder=5); ax.plot([np.pi / 2], [0.5], "o", color=CARDINAL, ms=9, zorder=5)
    ax.text(np.pi + 0.15, 1.03, r"$\pi$ pulse", color=CARDINAL, fontsize=13, ha="left", va="bottom")
    ax.text(np.pi / 2 - 0.22, 0.52, r"$\pi/2$", color=CARDINAL, fontsize=13, ha="right", va="center")
    ax.set_xlim(0, 4 * np.pi); ax.set_ylim(0, 1.16)
    ax.set_xticks(np.pi * np.arange(5)); ax.set_xticklabels(["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
    ax.set_yticks([0, 0.5, 1]); ax.tick_params(labelsize=12)
    ax.set_xlabel(r"$\Omega t$", fontsize=13); ax.set_ylabel(r"probability of state $f$", fontsize=12.5)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.97, bottom=0.15)
    fig.savefig(f"{OUT}/rabi_flop.png", dpi=200)
    print("wrote", f"{OUT}/rabi_flop.png")
    return fig, None


# ------------------------------------------------------------ every selection rule of the course on one page: allowed arrows, forbidden arrows (still)
@register
def selection_ladders():
    fig, axes = plt.subplots(1, 4, figsize=(9.6, 4.2), gridspec_kw={"wspace": 0.08})
    # (title, colour, levels as (label, x0, x1, y), allowed (from, to), forbidden (from, to), rule)
    panels = [("box", GRAY, [("$n = 1$", 0, 1, 0.3), ("$n = 2$", 0, 1, 1.5), ("$n = 3$", 0, 1, 3.5)], (0, 1), (0, 2), r"$\Delta n$ odd"),
              ("oscillator", TEAL, [("$v = 0$", 0, 1, 0.5), ("$v = 1$", 0, 1, 2.0), ("$v = 2$", 0, 1, 3.5)], (0, 1), (0, 2), r"$\Delta v = \pm1$"),
              ("rotor", PURPLE, [("$J = 0$", 0, 1, 0.3), ("$J = 1$", 0, 1, 1.37), ("$J = 2$", 0, 1, 3.5)], (0, 1), (0, 2), r"$\Delta J = \pm1$"),
              ("hydrogen", ORANGE, [("1s", 0, 0.45, 0.3), ("2s", 0, 0.45, 3.0), ("2p", 0.55, 1.0, 3.0)], (0, 2), (0, 1), r"$\Delta l = \pm1$")]
    for ax, (title, col, levels, ok, no, rule) in zip(axes, panels):
        for lab, x0, x1, y in levels:
            ax.hlines(y, x0, x1, color=col, lw=3.2)
            if title == "hydrogen":
                ax.text(0.5 * (x0 + x1), y + (0.14 if y > 1 else -0.14), lab, ha="center", va="bottom" if y > 1 else "top", fontsize=12.5)
            else:
                ax.text(1.05, y, lab, ha="left", va="center", fontsize=12.5)
        xa, xf = (0.72, 0.28) if title != "hydrogen" else (0.775, 0.225)
        xs = 0.72 if title != "hydrogen" else 0.3                     # where the allowed arrow starts on the lower level
        y0 = levels[ok[0]][3]
        ax.annotate("", xy=(xa, levels[ok[1]][3] - 0.05), xytext=(xs, y0 + 0.05),
                    arrowprops=dict(arrowstyle="-|>", color="k", lw=2.2, mutation_scale=17, shrinkA=0, shrinkB=0))
        xn = 0.28 if title != "hydrogen" else 0.15
        yn = levels[no[1]][3]
        ax.annotate("", xy=(xn, yn - 0.05), xytext=(xn, y0 + 0.05),
                    arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.8, mutation_scale=15, shrinkA=0, shrinkB=0, ls=(0, (4, 3))))
        ym = 0.5 * (y0 + yn) + (0.55 if title not in ("hydrogen",) else 0)
        ax.plot([xn], [ym], marker="x", color=CARDINAL, ms=13, mew=2.6, zorder=6)
        ax.set_title(title, fontsize=14, color=col, weight="bold")
        ax.text(0.5, -0.55, rule, ha="center", va="top", fontsize=14)
        ax.set_xlim(-0.12, 1.5 if title != "hydrogen" else 1.12); ax.set_ylim(-1.15, 3.95); ax.axis("off")
    fig.subplots_adjust(left=0.02, right=0.99, top=0.9, bottom=0.02)
    fig.savefig(f"{OUT}/selection_ladders.png", dpi=200)
    print("wrote", f"{OUT}/selection_ladders.png")
    return fig, None


# ------------------------------------------------------------ a state that lives a short time emits a short wave train, and a short wave train has a broad line (still)
@register
def lifetime_linewidth():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.0), gridspec_kw={"wspace": 0.12})
    t = np.linspace(0, 12, 1500)
    cases = [("long-lived", 4.0, TEAL, 1.25), ("short-lived", 1.0, ORANGE, -1.25)]
    for name, tau, col, y0 in cases:
        ax.plot(t, y0 + np.exp(-t / (2 * tau)) * np.cos(9 * t), color=col, lw=1.6)
        ax.plot(t, y0 + np.exp(-t / (2 * tau)), color=col, lw=1, ls=":"); ax.plot(t, y0 - np.exp(-t / (2 * tau)), color=col, lw=1, ls=":")
        ax.text(11.9, y0 + 0.62, name, color=col, fontsize=13.5, ha="right", va="bottom")
    ax.set_xlim(0, 12); ax.set_ylim(-2.5, 2.5); ax.set_xticks([]); ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("time", fontsize=13)
    f = np.linspace(-0.7, 0.7, 900)
    for name, tau, col, y0 in cases:
        g = 1 / (2 * np.pi * tau)                                    # full width at half maximum
        L = (g / 2) / (f**2 + (g / 2) ** 2) / np.pi
        bx.fill_between(f, 0, L, color=col, alpha=0.25, lw=0); bx.plot(f, L, color=col, lw=2.2)
    g = 1 / (2 * np.pi)
    half = 1 / (np.pi * g)                                           # half the peak height of the broad line
    bx.annotate("", xy=(g / 2, half), xytext=(-g / 2, half), arrowprops=dict(arrowstyle="<->", color="k", lw=1.2, shrinkA=0, shrinkB=0))
    bx.text(g / 2 + 0.05, half, r"$1/2\pi\tau$", fontsize=13.5, ha="left", va="center")
    bx.set_xlim(-0.7, 0.7); bx.set_ylim(0, 16.8); bx.set_yticks([]); bx.set_xticks([0]); bx.set_xticklabels([r"$\nu_0$"], fontsize=13.5)
    bx.spines["left"].set_visible(False)
    bx.set_xlabel("frequency", fontsize=13)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.97, bottom=0.14)
    fig.savefig(f"{OUT}/lifetime_linewidth.png", dpi=200)
    print("wrote", f"{OUT}/lifetime_linewidth.png")
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
