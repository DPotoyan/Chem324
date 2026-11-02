"""Chapter 4 animations and deck stills, authored ONCE here (same pipeline as chapters 2 and 3).

Each registered function builds one figure (and, for animations, a FuncAnimation) and is
self-contained: it uses only numpy, matplotlib.pyplot, FuncAnimation and the colour
constants below (plus local matplotlib.patches imports). Running this script bakes the GIFs /
PNG stills for the slide decks into ch04/images/. `scripts/sync_ch04_cells.py` copies the SAME
function bodies into the `{code-cell}` blocks of the lecture pages (marker line
`# synced: <name>`), where animations play in the matplotlib JS player.

Run from the repo root:
    .venv/bin/python scripts/make_ch04_animations.py                 # bake everything
    .venv/bin/python scripts/make_ch04_animations.py dof_motions     # a subset
    .venv/bin/python scripts/sync_ch04_cells.py                      # refresh page cells

Page weight: the JS player embeds every frame as a PNG, so keep animations to 24-48 frames.
Sync strips every line starting with `return`, so inner helpers must not use it (write a
lambda, or fill an array in place) and `update` must not return artists (use blit=False).

Lecture 4.1 (page ch04/01, deck slides/ch04/01) uses every figure in the "lecture 4.1" section.
Colours of the motions, kept the same in every figure: translation GRAY, rotation PURPLE,
vibration TEAL, electrons ORANGE.
"""
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = "ch04/images"
GIF_DPI = 200    # 2x: an 8 in figure bakes 1600 px wide, crisp full screen
TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"

REGISTRY = {}


def register(fn):
    REGISTRY[fn.__name__] = fn
    return fn


# ============================================================ lecture 4.1: molecular degrees of freedom

# ------------------------------------------------------------ CO flies, tumbles and vibrates; the real motion is the sum
@register
def dof_motions():
    from matplotlib.patches import Circle
    nf = 40
    ts = np.arange(nf) / nf                                     # one loop of the GIF = 1
    mC, mO, re = 12.0, 16.0, 0.95                               # carbon monoxide, bond in drawing units
    fC, fO = mO / (mC + mO), mC / (mC + mO)                     # distance of each atom from the center of mass, per unit bond
    heads = [("translation", "the center of mass moves", GRAY), ("rotation", "the orientation turns", PURPLE),
             ("vibration", "the bond length changes", TEAL), ("all three at once", "the real motion is the sum", "k")]
    # center of mass (x, y), angle and bond length of each panel at loop time s
    wrap = lambda s: -2.4 + 4.8 * ((s + 0.5) % 1)              # cross the panel once per loop; frame 0 in the middle
    paths = [lambda s: (wrap(s), 0.0, np.radians(25), re),
             lambda s: (0.0, 0.0, 2 * np.pi * s, re),
             lambda s: (0.0, 0.0, 0.0, re * (1 + 0.24 * np.sin(6 * np.pi * s))),
             lambda s: (wrap(s), 0.0, 2 * np.pi * s + 0.4, re * (1 + 0.24 * np.sin(6 * np.pi * s)))]
    fig, axes = plt.subplots(1, 4, figsize=(9.6, 2.85))
    parts = []
    for ax, (t1, t2, col) in zip(axes, heads):
        ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.3, 1.3); ax.set_aspect("equal")
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color("#ced4da")
        ax.set_title(t1, color=col, fontsize=13.5, weight="bold")
        ax.set_xlabel(t2, fontsize=11.5, color=GRAY)
        (bond,) = ax.plot([], [], color="#adb5bd", lw=6, solid_capstyle="round", zorder=2)
        cC = Circle((0, 0), 0.25, fc="#495057", ec="k", lw=1, zorder=3); ax.add_patch(cC)
        cO = Circle((0, 0), 0.29, fc=CARDINAL, ec="k", lw=1, zorder=3); ax.add_patch(cO)
        tC = ax.text(0, 0, "C", color="white", ha="center", va="center", fontsize=10, weight="bold", zorder=4)
        tO = ax.text(0, 0, "O", color="white", ha="center", va="center", fontsize=10, weight="bold", zorder=4)
        (com,) = ax.plot([], [], "+", color="k", ms=10, mew=2.2, zorder=5)
        parts.append((bond, cC, cO, tC, tO, com))
    axes[0].axhline(0, color=GRAY, lw=1, ls=":", zorder=1)
    axes[3].axhline(0, color=GRAY, lw=1, ls=":", zorder=1)
    th = np.linspace(0, 2 * np.pi, 200)
    axes[1].plot(fO * re * np.cos(th), fO * re * np.sin(th), color=PURPLE, lw=1, ls=":", zorder=1)
    axes[1].plot(fC * re * np.cos(th), fC * re * np.sin(th), color=PURPLE, lw=1, ls=":", zorder=1)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.86, bottom=0.12, wspace=0.08)

    def update(i):
        for path, (bond, cC, cO, tC, tO, com) in zip(paths, parts):
            X, Y, a, r = path(ts[i])
            u = np.array([np.cos(a), np.sin(a)])
            pC, pO = np.array([X, Y]) - fC * r * u, np.array([X, Y]) + fO * r * u
            bond.set_data([pC[0], pO[0]], [pC[1], pO[1]])
            cC.center, cO.center = tuple(pC), tuple(pO)
            tC.set_position(pC); tO.set_position(pO)
            com.set_data([X], [Y])

    ani = FuncAnimation(fig, update, frames=nf, interval=85, blit=False)
    return fig, ani


dof_motions.fps = 12


# ------------------------------------------------------------ the ladders of HCl, each one the bottom rung of the last, magnified (still)
@register
def level_zoom():
    from matplotlib.patches import ConnectionPatch, Rectangle
    kT = 208.5                                                  # k_B T at 300 K in cm^-1
    E1 = 4.57e-16                                               # HCl in a 1 cm box: h^2/8mL^2 in cm^-1
    panels = [("electronic", ORANGE, [0, 65000], 80000, r"gap $\approx$ 65 000 cm$^{-1}$", "ultraviolet"),
              ("vibrational", TEAL, [0, 2886, 5668, 8347, 10923], 12500, r"gap $\approx$ 2 900 cm$^{-1}$", "infrared"),
              ("rotational", PURPLE, [10.59 * J * (J + 1) for J in range(9)], 800, r"gaps $\approx$ 20 cm$^{-1}$", "microwave"),
              ("translational", GRAY, [(n * n - 1) * E1 for n in range(1, 15)], 9.0e-14, r"gaps $\approx 10^{-15}$ cm$^{-1}$",
               "none: a continuum")]
    fig, axes = plt.subplots(1, 4, figsize=(9.6, 4.3))
    for k, (ax, (name, col, lev, top, gap, spec)) in enumerate(zip(axes, panels)):
        ax.axhspan(0, min(kT, top), color="#fcc419", alpha=0.32, lw=0, zorder=0)
        ax.hlines(lev, 0.12, 0.88, color=col, lw=2.2, zorder=2)
        ax.set_xlim(0, 1); ax.set_ylim(-0.03 * top, top)
        ax.set_xticks([])
        for sp in ("top", "right", "bottom"):
            ax.spines[sp].set_visible(False)
        ax.set_title(name + "\n", color=col, fontsize=13, weight="bold", pad=2)
        ax.text(0.5, 1.015, gap, transform=ax.transAxes, ha="center", va="bottom", fontsize=10.5, color="k")
        ax.set_xlabel(spec, fontsize=11.5, color=col, labelpad=6)
        ax.tick_params(labelsize=9.5)
    axes[0].set_yticks([0, 40000, 80000]); axes[0].set_yticklabels(["0", "40 000", "80 000"])
    axes[1].set_yticks([0, 5000, 10000]); axes[1].set_yticklabels(["0", "5 000", "10 000"])
    axes[2].set_yticks([0, 400, 800])
    axes[3].set_yticks([0, 8e-14]); axes[3].set_yticklabels(["0", r"$8{\times}10^{-14}$"])
    axes[0].set_ylabel(r"energy above the lowest level (cm$^{-1}$)", fontsize=11)
    axes[0].text(0.5, 15500, "$k_BT$ at 300 K:\ntoo thin to see", ha="center", va="bottom", fontsize=9.5, color="#a07800")
    axes[1].text(0.5, 1150, r"$k_BT$ = 208 cm$^{-1}$", ha="center", va="bottom", fontsize=9.5, color="#a07800")
    axes[2].text(0.5, kT + 14, "$k_BT$: several\nrungs are warm", ha="center", va="bottom", fontsize=9.5, color="#a07800",
                 bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))
    axes[3].text(0.5, 0.5 * 9e-14, "all of it lies\nbelow $k_BT$", ha="center", va="center", fontsize=10, color="#a07800",
                 bbox=dict(fc="white", ec="none", alpha=0.8, pad=2))
    for k, mag in zip(range(3), [r"$\times 6$", r"$\times 16$", r"$\times 10^{16}$"]):
        a, b = axes[k], axes[k + 1]
        top_a = panels[k][3]
        h = max(panels[k + 1][3], 0.012 * top_a)                # the next panel's range, drawn at least 1.2% tall
        a.add_patch(Rectangle((0.08, -0.012 * top_a), 0.84, h + 0.012 * top_a, fill=False, ec="k", lw=1.2, zorder=4))
        for ya, yb in ((h, 1.0), (-0.012 * top_a, 0.0)):
            fig.add_artist(ConnectionPatch(xyA=(0.92, ya), coordsA=a.transData, xyB=(0.0, yb), coordsB=b.transAxes,
                                           color=GRAY, lw=0.9, ls="--"))
        a.text(0.97, h + 0.02 * top_a, mag, ha="left", va="bottom", fontsize=10.5, color=GRAY, clip_on=False)
    fig.subplots_adjust(left=0.09, right=0.985, top=0.83, bottom=0.11, wspace=0.62)
    fig.savefig(f"{OUT}/level_zoom.png", dpi=200)
    print("wrote", f"{OUT}/level_zoom.png")
    return fig, None


# ------------------------------------------------------------ water turns about three axes; CO2 about only two (still)
@register
def linear_rotations():
    from matplotlib.patches import Circle
    el, az = np.radians(16), np.radians(-32)                    # orthographic camera
    Ry = np.array([[np.cos(az), 0, np.sin(az)], [0, 1, 0], [-np.sin(az), 0, np.cos(az)]])
    Rx = np.array([[1, 0, 0], [0, np.cos(el), -np.sin(el)], [0, np.sin(el), np.cos(el)]])
    view = Rx @ Ry
    mols = [("H$_2$O, bent: 3 rotations",
             np.array([[0, 0.066, 0], [0.757, -0.520, 0], [-0.757, -0.520, 0]]),
             [0.27, 0.17, 0.17], [CARDINAL, "white", "white"], [(0, 1), (0, 2)]),
            ("CO$_2$, linear: 2 rotations",
             np.array([[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]]),
             [0.25, 0.27, 0.27], ["#495057", CARDINAL, CARDINAL], [(0, 1), (0, 2)])]
    axis_names = ["x", "y", "z"]
    fig, axes = plt.subplots(2, 3, figsize=(9.0, 5.6))
    phi = np.linspace(0, 2 * np.pi, 200)
    for row, (label, P, rad, cols, bonds) in enumerate(mols):
        for c in range(3):
            ax = axes[row, c]
            ax.set_xlim(-1.75, 1.75); ax.set_ylim(-1.45, 1.45); ax.set_aspect("equal"); ax.axis("off")
            e = np.eye(3)[c]
            Q = (view @ P.T).T
            dist = np.linalg.norm(P - np.outer(P @ e, e), axis=1)
            still = dist.max() < 0.02
            acol = CARDINAL if still else TEAL
            ends = view @ np.array([-1.3 * e, 1.3 * e]).T
            ax.plot(ends[0], ends[1], color=acol, lw=1.6, ls="--", zorder=1)
            lab = view @ ((1.72 if c == 0 else 1.45) * e)       # the x label clears the CO2 oxygen
            ax.text(lab[0], lab[1], axis_names[c], color=acol, fontsize=12.5, style="italic", ha="center", va="center")
            for p, d in zip(P, dist):
                if d > 0.02:
                    perp = p - (p @ e) * e
                    orbit = np.outer(p @ e, e) + np.outer(np.cos(phi), perp) + np.outer(np.sin(phi), np.cross(e, perp))
                    o2 = (view @ orbit.T)
                    ax.plot(o2[0], o2[1], color=TEAL, lw=1.3, alpha=0.75, zorder=1)
                    j = 60
                    ax.annotate("", xy=(o2[0, j + 6], o2[1, j + 6]), xytext=(o2[0, j], o2[1, j]),
                                arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.3, mutation_scale=12))
            for a, b in bonds:
                ax.plot([Q[a, 0], Q[b, 0]], [Q[a, 1], Q[b, 1]], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
            for j in np.argsort(Q[:, 2]):
                ax.add_patch(Circle((Q[j, 0], Q[j, 1]), rad[j], fc=cols[j], ec="k", lw=1, zorder=3 + Q[j, 2]))
            if still:
                ax.text(0, -0.95, "every atom sits on the axis:\nnothing moves, nothing to count",
                        ha="center", va="center", fontsize=11, color=CARDINAL)
            ax.set_title(f"turn about {axis_names[c]}", fontsize=12, color=acol)
        axes[row, 0].text(-1.75, 1.75, label, fontsize=13.5, weight="bold", ha="left", va="bottom")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.01, hspace=0.42, wspace=0.04)
    fig.savefig(f"{OUT}/linear_rotations.png", dpi=200)
    print("wrote", f"{OUT}/linear_rotations.png")
    return fig, None


# ------------------------------------------------------------ the three vibrations of water (normal modes of a valence force field)
@register
def water_modes():
    from matplotlib.patches import Circle
    m = np.array([16.0, 16.0, 1.0, 1.0, 1.0, 1.0])              # O (x, y), H1 (x, y), H2 (x, y) in u
    re, th0 = 0.958, np.radians(104.5)                          # angstrom, equilibrium angle
    kr, kt = 8.45, 0.76                                         # stretch (mdyn/A) and bend (mdyn A/rad^2) force constants
    q0 = np.array([0, 0, re * np.sin(th0 / 2), -re * np.cos(th0 / 2), -re * np.sin(th0 / 2), -re * np.cos(th0 / 2)])
    bl = lambda q, j: np.hypot(q[j] - q[0], q[j + 1] - q[1])
    ang = lambda q: np.arccos(((q[2] - q[0]) * (q[4] - q[0]) + (q[3] - q[1]) * (q[5] - q[1])) / (bl(q, 2) * bl(q, 4)))
    V = lambda q: 0.5 * kr * ((bl(q, 2) - re)**2 + (bl(q, 4) - re)**2) + 0.5 * kt * (ang(q) - th0)**2
    Hs, e, I6 = np.zeros((6, 6)), 1e-4, np.eye(6)
    for i in range(6):                                          # Hessian by central differences
        for j in range(6):
            Hs[i, j] = (V(q0 + e * I6[i] + e * I6[j]) - V(q0 + e * I6[i] - e * I6[j])
                        - V(q0 - e * I6[i] + e * I6[j]) + V(q0 - e * I6[i] - e * I6[j])) / (4 * e * e)
    w2, vec = np.linalg.eigh(Hs / np.sqrt(np.outer(m, m)))      # mass-weighted: three zeros (2 shifts, 1 turn), then 3 modes
    d = vec[:, 3:] / np.sqrt(m)[:, None]
    bend, s1, s2 = 0, 1, 2
    asym = s1 if abs(d[0, s1]) > abs(d[0, s2]) else s2          # only the antisymmetric stretch moves O sideways
    sym = s2 if asym == s1 else s1
    order = [(sym, "symmetric stretch", 3657, 2), (bend, "bend", 1595, 1), (asym, "antisymmetric stretch", 3756, 2)]
    nf = 36
    ts = np.arange(nf) / nf
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.3))
    parts = []
    for ax, (k, name, wn, cyc) in zip(axes, order):
        dk = d[:, k] / np.abs(d[2:, k]).max() * 0.2             # the H atoms swing 0.2 A (exaggerated)
        dk = dk * (np.sign(dk[2] * q0[2] + dk[3] * q0[3]) or 1)  # start with H1 moving out along its bond
        ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.2, 0.55); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(name, fontsize=13, color=TEAL, weight="bold")
        ax.text(0, -1.17, rf"{wn} cm$^{{-1}}$", ha="center", va="bottom", fontsize=12)
        for j in range(3):                                      # equilibrium ghost and the direction of motion
            ax.add_patch(Circle((q0[2 * j], q0[2 * j + 1]), 0.27 if j == 0 else 0.17, fc="none", ec="#ced4da", lw=1, ls="--"))
            if np.hypot(dk[2 * j], dk[2 * j + 1]) > 0.02:
                ax.annotate("", xy=(q0[2 * j] + 2.2 * dk[2 * j], q0[2 * j + 1] + 2.2 * dk[2 * j + 1]),
                            xytext=(q0[2 * j] + 1.25 * dk[2 * j], q0[2 * j + 1] + 1.25 * dk[2 * j + 1]),
                            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.6, mutation_scale=13), zorder=1)
        (b1,) = ax.plot([], [], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
        (b2,) = ax.plot([], [], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
        cO = Circle((0, 0), 0.27, fc=CARDINAL, ec="k", lw=1, zorder=3); ax.add_patch(cO)
        cH1 = Circle((0, 0), 0.17, fc="white", ec="k", lw=1, zorder=3); ax.add_patch(cH1)
        cH2 = Circle((0, 0), 0.17, fc="white", ec="k", lw=1, zorder=3); ax.add_patch(cH2)
        parts.append((dk, cyc, b1, b2, cO, cH1, cH2))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.02, wspace=0.05)

    def update(i):
        for dk, cyc, b1, b2, cO, cH1, cH2 in parts:
            q = q0 + np.sin(2 * np.pi * cyc * ts[i]) * dk
            cO.center, cH1.center, cH2.center = (q[0], q[1]), (q[2], q[3]), (q[4], q[5])
            b1.set_data([q[0], q[2]], [q[1], q[3]]); b2.set_data([q[0], q[4]], [q[1], q[5]])

    ani = FuncAnimation(fig, update, frames=nf, interval=75, blit=False)
    return fig, ani


# ------------------------------------------------------------ the map of the chapter: each motion, its model, its ladder, its spectroscopy (still)
@register
def model_map():
    from matplotlib.patches import FancyBboxPatch
    W, Ht = 10.1, 4.75
    fig = plt.figure(figsize=(W, Ht))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, Ht); ax.axis("off")
    tint = {GRAY: "#f1f3f5", PURPLE: "#f1ecf7", TEAL: "#e3f1f5", ORANGE: "#fdf0e0", "k": "#f8f9fa"}
    xm, xo, xd, xl, xs = 0.9, 3.45, 6.0, 7.55, 8.2              # columns: molecule, motion, model, ladder, spectroscopy
    rows = [(3.65, ORANGE, "electrons", "make the potential E(R)", "atoms and orbitals", "Chapters 5 to 8",
             [1 - 1 / n**2 for n in range(1, 5)], "UV-visible", r"$10^4$ to $10^5$ cm$^{-1}$"),
            (2.6, GRAY, "translation", "center of mass: 3", "particle in a box", "Lecture 3.2",
             [(n * n - 1) / 15 for n in range(1, 5)], "none: a continuum", r"$10^{-15}$ cm$^{-1}$"),
            (1.55, PURPLE, "rotation", "orientation: 3 (linear: 2)", "rigid rotor", "Lectures 4.4, 4.5",
             [J * (J + 1) / 12 for J in range(4)], "microwave", r"1 to 20 cm$^{-1}$"),
            (0.5, TEAL, "vibration", r"shape: $3N-6$ (or $3N-5$)", "harmonic oscillator", "Lectures 4.2, 4.3",
             [v / 3 for v in range(4)], "infrared", r"$10^3$ cm$^{-1}$")]

    def box(x, y, w, h, title, line, col):
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.1",
                                    fc=tint[col], ec=col, lw=1.6, zorder=2))
        ax.text(x, y + 0.13, title, ha="center", va="center", fontsize=12.5, color=col, weight="bold", zorder=3)
        ax.text(x, y - 0.17, line, ha="center", va="center", fontsize=11.5, zorder=3)

    for x, head in ((xo, "motion"), (xd, "model system"), (xl + 0.25, "levels"), (xs + 0.6, "spectroscopy")):
        ax.text(x, 4.42, head, ha="center", fontsize=11.5, color=GRAY, style="italic")
    ax.add_patch(FancyBboxPatch((xm - 0.72, 1.45), 1.44, 1.3, boxstyle="round,pad=0,rounding_size=0.1",
                                fc="#f8f9fa", ec="k", lw=1.6, zorder=2))
    ax.text(xm, 2.38, "a molecule", ha="center", va="center", fontsize=12.5, weight="bold")
    ax.text(xm, 2.0, "N nuclei", ha="center", va="center", fontsize=11.5)
    ax.text(xm, 1.7, "n electrons", ha="center", va="center", fontsize=11.5)
    for y, col, motion, mline, model, mlect, lev, spec, gap in rows:
        ax.annotate("", xy=(xo - 1.1, y), xytext=(xm + 0.74, 2.1), zorder=1,
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=1.5, mutation_scale=15, shrinkA=0, shrinkB=2))
        box(xo, y, 2.2, 0.72, motion, mline, col)
        ax.annotate("", xy=(xd - 1.08, y), xytext=(xo + 1.1, y), zorder=1,
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4, mutation_scale=14, shrinkA=2, shrinkB=2))
        box(xd, y, 2.12, 0.72, model, mlect, col)
        ax.hlines([y - 0.3 + 0.6 * v for v in lev], xl, xl + 0.5, color=col, lw=2)
        ax.text(xs, y + 0.13, spec, ha="left", va="center", fontsize=12, color=col, weight="bold")
        ax.text(xs, y - 0.17, gap, ha="left", va="center", fontsize=11)
    ax.text(1.4, 3.3, "Born-\nOppenheimer", ha="center", va="center", fontsize=10.5, color=GRAY, style="italic")
    ax.text(1.4, 0.85, "nuclei move\non E(R)", ha="center", va="center", fontsize=10.5, color=GRAY, style="italic")
    fig.savefig(f"{OUT}/model_map.png", dpi=200)
    print("wrote", f"{OUT}/model_map.png")
    return fig, None


# ------------------------------------------------------------ the HCl bond: Morse well, its levels, and the parabola that fits the bottom (still)
@register
def bond_parabola():
    from matplotlib.patches import Rectangle, ConnectionPatch
    D, a, re = 4.62, 1.87, 1.275                                # HCl: well depth (eV), Morse range (1/A), bond length (A)
    hw = 0.3708                                                 # hbar omega = 2991 cm^-1, from k = 2 D a^2 = 518 N/m
    xe = hw**2 / (4 * D)                                        # Morse anharmonicity (eV)
    r = np.linspace(0.75, 4.2, 800)
    U = D * (1 - np.exp(-a * (r - re)))**2
    k = 2 * D * a * a                                           # curvature at the bottom, eV/A^2
    P = 0.5 * k * (r - re)**2
    G = lambda v: hw * (v + 0.5) - xe * (v + 0.5)**2
    turn = lambda E: (re - np.log(1 + np.sqrt(E / D)) / a, re - np.log(1 - np.sqrt(E / D)) / a)
    fig, (ax, az) = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"width_ratios": [1.5, 1], "wspace": 0.25})
    for v in range(24):
        E = G(v)
        if E < D:
            r1, r2 = turn(E)
            ax.hlines(E, r1, r2, color=TEAL if v < 3 else "#adb5bd", lw=1.6 if v < 3 else 0.9, zorder=2)
    ax.plot(r, U, color="k", lw=2.4, zorder=3, label="true potential (Morse fit)")
    ax.plot(r, P, color=ORANGE, lw=2.2, ls="--", zorder=3, label=r"parabola $\frac{1}{2}k(R - R_e)^2$")
    ax.axhline(D, color=GRAY, lw=1, ls=":")
    ax.text(4.15, D + 0.08, r"$D_e$ = 4.6 eV: the atoms come apart", ha="right", va="bottom", fontsize=10.5, color=GRAY)
    ax.set_xlim(0.75, 4.2); ax.set_ylim(-0.15, 5.6)
    ax.set_xlabel(r"bond length $R$ ($\AA$)", fontsize=11.5); ax.set_ylabel("energy (eV)", fontsize=11.5)
    ax.legend(loc="lower right", frameon=False, fontsize=10.5)
    ax.set_title("HCl: the potential the nuclei move on", loc="left", fontsize=12)
    ax.add_patch(Rectangle((1.02, -0.06), 0.56, 1.36, fill=False, ec="k", lw=1.1, zorder=4))
    rz = np.linspace(1.0, 1.6, 300)
    az.plot(rz, D * (1 - np.exp(-a * (rz - re)))**2, color="k", lw=2.4)
    az.plot(rz, 0.5 * k * (rz - re)**2, color=ORANGE, lw=2.2, ls="--")
    for v in range(3):
        r1, r2 = turn(G(v))
        az.hlines(G(v), r1, r2, color=TEAL, lw=2)
        az.text(r1 + 0.012, G(v) + 0.025, rf"$v = {v}$", va="bottom", ha="left", fontsize=11, color=TEAL)
    az.set_xlim(1.0, 1.6); az.set_ylim(-0.04, 1.3)
    az.set_xlabel(r"$R$ ($\AA$)", fontsize=11.5)
    az.set_title("zoom: the bottom is a parabola", loc="left", fontsize=12)
    for ya, yb in ((1.3, 1.0), (-0.06, 0.0)):
        fig.add_artist(ConnectionPatch(xyA=(1.58, ya), coordsA=ax.transData, xyB=(0.0, yb), coordsB=az.transAxes,
                                       color=GRAY, lw=0.9, ls="--"))
    for s in (ax, az):
        s.spines["top"].set_visible(False); s.spines["right"].set_visible(False)
    fig.subplots_adjust(left=0.07, right=0.985, top=0.91, bottom=0.14)
    fig.savefig(f"{OUT}/bond_parabola.png", dpi=200)
    print("wrote", f"{OUT}/bond_parabola.png")
    return fig, None


# ------------------------------------------------------------ same spring, four times the mass: half the frequency
@register
def spring_masses():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    nf, A, wall = 48, 0.9, -2.6
    ts = np.linspace(0, 2, nf, endpoint=False)                  # time in periods T of the light mass
    zig = np.zeros(70); zig[4:-4] = 0.2 * (2 * np.abs((np.arange(62) / 4.0) % 1 - 0.5) * 2 - 1)
    rows = [("mass $m$", TEAL, 1.0, 0.42), (r"mass $4m$, same spring", PURPLE, 0.5, 0.62)]
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 3.9), gridspec_kw={"width_ratios": [1, 1.25], "hspace": 0.55, "wspace": 0.12})
    parts = []
    tt = np.linspace(0, 2, 400)
    for (ax, ax2), (name, col, w, size) in zip(axes, rows):
        ax.axvline(wall, color="k", lw=5)
        ax.axhline(-0.5, color=GRAY, lw=0.8)
        ax.axvline(0, color=GRAY, lw=1, ls=":")
        (spring,) = ax.plot([], [], color=GRAY, lw=1.5)
        (block,) = ax.fill([0, 0, 0, 0], [0, 0, 0, 0], color=col, alpha=0.9)
        ax.set_xlim(wall - 0.1, 1.75); ax.set_ylim(-0.55, 0.85); ax.axis("off")
        ax.set_title(name, loc="left", fontsize=12.5, color=col, weight="bold")
        ax2.plot(tt, A * np.cos(2 * np.pi * w * tt), color="#dee2e6", lw=1.6)
        (trace,) = ax2.plot([], [], color=col, lw=2.4)
        (dot,) = ax2.plot([], [], "o", color=col, ms=8)
        ax2.axhline(0, color=GRAY, lw=0.6)
        ax2.set_xlim(0, 2); ax2.set_ylim(-1.15, 1.15); ax2.set_yticks([-A, 0, A]); ax2.set_yticklabels(["-A", "0", "A"])
        ax2.set_xticks([0, 1, 2]); ax2.set_xticklabels(["0", "T", "2T"])
        ax2.set_ylabel("x(t)", fontsize=11)
        parts.append((w, size, spring, block, trace, dot))
    axes[0, 1].set_title(r"$\omega = \sqrt{k/m}$: period $T$", loc="left", fontsize=12, color=TEAL)
    axes[1, 1].set_title(r"$\omega = \sqrt{k/4m}$: half as fast, period $2T$", loc="left", fontsize=12, color=PURPLE)
    axes[1, 1].set_xlabel("time", fontsize=11)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.13)

    def update(i):
        for w, size, spring, block, trace, dot in parts:
            x = A * np.cos(2 * np.pi * w * ts[i])
            spring.set_data(np.linspace(wall, x - size / 2, 70), zig + 0.05)
            block.set_xy([[x - size / 2, -0.5], [x + size / 2, -0.5], [x + size / 2, -0.5 + size * 1.2], [x - size / 2, -0.5 + size * 1.2]])
            sel = tt <= ts[i] + 1e-9
            trace.set_data(tt[sel], A * np.cos(2 * np.pi * w * tt[sel]))
            dot.set_data([ts[i]], [x])

    ani = FuncAnimation(fig, update, frames=nf, interval=70, blit=False)
    return fig, ani


# ------------------------------------------------------------ energy sloshes between kinetic and potential; the total stays
@register
def energy_slosh():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    nf, E = 36, 0.5                                             # k = m = A = 1: E = 1/2
    ts = np.arange(nf) / nf                                     # one period
    x = np.linspace(-1.35, 1.35, 300)
    fig, (ax, axb) = plt.subplots(1, 2, figsize=(8.4, 3.5), gridspec_kw={"width_ratios": [2.4, 1], "wspace": 0.3})
    ax.plot(x, 0.5 * x**2, color="k", lw=2.2)
    ax.axhline(E, color=CARDINAL, lw=1.6, ls="--")
    ax.text(1.33, E + 0.02, "E", color=CARDINAL, fontsize=13, ha="right", va="bottom")
    ax.text(0, 0.88, r"$V = \frac{1}{2}kx^2$", fontsize=13, ha="center", va="top")
    for s in (-1, 1):
        ax.axvline(s, color=GRAY, lw=0.8, ls=":")
    ax.text(-1, -0.075, "turning\npoint", ha="center", va="top", fontsize=10, color=GRAY)
    ax.text(1, -0.075, "turning\npoint", ha="center", va="top", fontsize=10, color=GRAY)
    (vbar,) = ax.plot([], [], color=TEAL, lw=7, solid_capstyle="butt")
    (kbar,) = ax.plot([], [], color=ORANGE, lw=7, solid_capstyle="butt")
    (ball,) = ax.plot([], [], "o", color="k", ms=13, zorder=5)
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-0.25, 0.92); ax.set_yticks([]); ax.set_xticks([])
    ax.spines["left"].set_visible(False); ax.set_xlabel("position x", fontsize=11.5)
    bv = axb.bar([0], [0], width=0.6, color=TEAL, label=r"potential $V$")[0]
    bk = axb.bar([0], [0], width=0.6, color=ORANGE, label=r"kinetic $K = \frac{p^2}{2m}$")[0]
    axb.axhline(E, color=CARDINAL, lw=1.6, ls="--")
    axb.axhline(0, color="k", lw=0.8)
    axb.set_xlim(-0.6, 0.6); axb.set_ylim(-0.25, 0.92); axb.set_xticks([]); axb.set_yticks([])   # same heights as the left panel
    axb.spines["left"].set_visible(False); axb.spines["bottom"].set_visible(False)
    axb.legend(loc="upper center", frameon=False, fontsize=11, bbox_to_anchor=(0.5, 1.02))
    axb.set_xlabel(r"$E = K + V$", fontsize=12.5)
    fig.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.17)

    def update(i):
        xi = np.cos(2 * np.pi * ts[i])
        V = 0.5 * xi**2
        vbar.set_data([xi, xi], [0, V]); kbar.set_data([xi, xi], [V, E]); ball.set_data([xi], [V])
        bv.set_height(V); bk.set_y(V); bk.set_height(E - V)

    ani = FuncAnimation(fig, update, frames=nf, interval=85, blit=False)
    return fig, ani


# ------------------------------------------------------------ where is a classical spring found? snapshots pile up at the turning points
@register
def spring_histogram():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    rng = np.random.default_rng(2)
    A = 1.0
    xs = A * np.cos(2 * np.pi * rng.random(5000))               # snapshots at random times
    yj = rng.random(5000)
    counts = np.unique(np.round(np.geomspace(1, 5000, 40)).astype(int))
    counts = np.concatenate([counts, np.full(8, counts[-1])])
    edges = np.linspace(-1.25, 1.25, 41); mid = 0.5 * (edges[1:] + edges[:-1]); dx = edges[1] - edges[0]
    xc = np.linspace(-0.999, 0.999, 600)
    fig, (ta, ha) = plt.subplots(2, 1, figsize=(8.0, 3.9), sharex=True, gridspec_kw={"height_ratios": [1, 2.3], "hspace": 0.12})
    for ax in (ta, ha):
        ax.axvspan(-1.25, -A, color=GRAY, alpha=0.1, lw=0); ax.axvspan(A, 1.25, color=GRAY, alpha=0.1, lw=0)
        ax.axvline(-A, color=GRAY, lw=1, ls=":"); ax.axvline(A, color=GRAY, lw=1, ls=":")
    ta.set_ylim(0, 1); ta.set_yticks([]); ta.spines["left"].set_visible(False); ta.tick_params(bottom=False)
    ta.set_title("a mass on a spring; each dot is a snapshot at a random time", loc="left", fontsize=11.5)
    scat = ta.scatter([], [], s=4, color=TEAL, alpha=0.5, lw=0)
    (ball,) = ta.plot([], [], "o", color=ORANGE, ms=13, zorder=5)
    bars = ha.bar(mid, 0 * mid, width=0.9 * dx, color=TEAL, alpha=0.55)
    (pc,) = ha.plot([], [], color=CARDINAL, lw=2.4, label=r"$P(x) = \dfrac{1}{\pi\sqrt{A^2 - x^2}}$")
    ha.set_xlim(-1.25, 1.25); ha.set_yticks([])
    ha.set_xticks([-A, 0, A]); ha.set_xticklabels(["-A", "0", "A"]); ha.set_xlabel("position x", fontsize=11.5)
    ha.set_ylabel("times found here", fontsize=11)
    ha.legend(loc="upper center", frameon=False, fontsize=12)
    ha.text(-1.235, 0.03, "never\nfound", transform=ha.get_xaxis_transform(), fontsize=10, color=GRAY, va="bottom")
    ha.text(1.235, 0.03, "never\nfound", transform=ha.get_xaxis_transform(), fontsize=10, color=GRAY, va="bottom", ha="right")
    fig.subplots_adjust(left=0.05, right=0.99, top=0.85, bottom=0.14)
    sup = fig.suptitle("", fontsize=12, x=0.99, ha="right")

    def update(i):
        N = counts[i]
        scat.set_offsets(np.column_stack([xs[:N], yj[:N]]))
        ball.set_data([A * np.cos(2 * np.pi * i / 13)], [0.5])
        h = np.histogram(xs[:N], bins=edges)[0]
        for b, c in zip(bars, h):
            b.set_height(c)
        pc.set_data(xc, N * dx / (np.pi * np.sqrt(A * A - xc**2)))
        ha.set_ylim(0, 1.25 * max(3.0, h.max(), N * dx * 0.9))
        sup.set_text(f"N = {N} snapshot" + ("" if N == 1 else "s"))

    ani = FuncAnimation(fig, update, frames=len(counts), interval=140, blit=False)
    return fig, ani


# ------------------------------------------------------------ two atoms on a spring = one bead of mass mu on a wall
@register
def two_body():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    nf = 32
    ts = np.arange(nf) / nf                                     # one period
    m1, m2, re, A = 12.0, 16.0, 2.2, 0.55                       # C and O (u), bond and stretch amplitude in drawing units
    M, mu = m1 + m2, m1 * m2 / (m1 + m2)
    zig = np.zeros(70); zig[4:-4] = 0.16 * (2 * np.abs((np.arange(62) / 4.0) % 1 - 0.5) * 2 - 1)
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(8.0, 3.4), gridspec_kw={"hspace": 0.5})
    for a in (ax, bx):
        a.set_xlim(-2.6, 2.6); a.set_ylim(-0.55, 0.65); a.axis("off"); a.axhline(-0.48, color=GRAY, lw=0.8)
    eq1, eq2 = -m2 / M * re, m1 / M * re
    ax.axvline(eq1, color=GRAY, lw=1, ls=":"); ax.axvline(eq2, color=GRAY, lw=1, ls=":")
    ax.plot([0], [-0.43], "^", color="k", ms=11)
    ax.text(0.08, -0.36, "center of mass", fontsize=10, color="k", va="bottom")
    ax.set_title(r"C (12 u) and O (16 u): each atom moves; the lighter one moves farther", loc="left", fontsize=12)
    (s1,) = ax.plot([], [], color=GRAY, lw=1.5)
    (a1,) = ax.plot([], [], "o", color="#495057", ms=26, mec="k")
    (a2,) = ax.plot([], [], "o", color=CARDINAL, ms=29, mec="k")
    wall = -2.1
    bx.axvline(wall, color="k", lw=5)
    bx.axvline(wall + re, color=GRAY, lw=1, ls=":")
    bx.set_title(rf"one bead of reduced mass $\mu$ = {mu:.2f} u on a wall: the same stretch $x(t)$", loc="left", fontsize=12)
    (s2,) = bx.plot([], [], color=GRAY, lw=1.5)
    (bead,) = bx.plot([], [], "o", color=TEAL, ms=24, mec="k")
    (arr,) = bx.plot([], [], color=ORANGE, lw=3)
    (d1,) = ax.plot([], [], color=ORANGE, lw=3)                 # each atom's own displacement
    (d2,) = ax.plot([], [], color=ORANGE, lw=3)
    bx.text(wall + re + 0.75, 0.32, "x", color=ORANGE, fontsize=13, style="italic")
    fig.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.03)

    def update(i):
        x = A * np.sin(2 * np.pi * ts[i])
        p1, p2 = eq1 - m2 / M * x, eq2 + m1 / M * x
        a1.set_data([p1], [0]); a2.set_data([p2], [0])
        s1.set_data(np.linspace(p1, p2, 70), zig)
        bead.set_data([wall + re + x], [0])
        s2.set_data(np.linspace(wall, wall + re + x, 70), zig)
        arr.set_data([wall + re, wall + re + x], [0.3, 0.3])
        d1.set_data([eq1, p1], [0.42, 0.42]); d2.set_data([eq2, p2], [0.42, 0.42])

    ani = FuncAnimation(fig, update, frames=nf, interval=80, blit=False)
    return fig, ani


# ------------------------------------------------------------ preview: box rungs spread as n^2, spring rungs are evenly spaced (still)
@register
def ho_preview():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    N = 600                                                     # the spring on a grid, hbar = m = omega = 1 (Lecture 3.5)
    x = np.linspace(-6, 6, N); dx = x[1] - x[0]
    D2 = (np.eye(N, k=1) - 2 * np.eye(N) + np.eye(N, k=-1)) / dx**2
    E, psi = np.linalg.eigh(-0.5 * D2 + np.diag(0.5 * x**2))
    psi = psi / np.sqrt(dx)
    fig, (ab, ah) = plt.subplots(1, 2, figsize=(9.2, 4.0), sharey=True, gridspec_kw={"wspace": 0.08})
    L, E1 = 3.6, 0.42                                           # a box drawn about as wide as the spring's middle rungs
    xb = np.linspace(0, L, 300)
    ab.plot([0, 0, L, L], [7.2, 0, 0, 7.2], color="k", lw=2.4)
    for n in range(1, 5):
        En = E1 * n * n
        ab.hlines(En, 0, L, color=GRAY, lw=0.9, ls="--")
        ab.plot(xb, En + 0.36 * np.sin(n * np.pi * xb / L), color=TEAL, lw=2.2)
        ab.text(L + 0.12, En, rf"$n = {n}$", va="center", fontsize=11)
    for n in range(1, 4):
        ab.annotate("", xy=(L * 0.5 + 0.9, E1 * (n + 1)**2), xytext=(L * 0.5 + 0.9, E1 * n * n),
                    arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.4, shrinkA=0, shrinkB=0))
    ab.set_xlim(-0.3, L + 0.9); ab.set_ylim(0, 7.2); ab.set_xticks([]); ab.set_yticks([])
    ab.spines["left"].set_visible(False); ab.spines["bottom"].set_visible(False)
    ab.set_title("box: fixed walls, the gaps grow", loc="left", fontsize=12.5)
    xx = np.linspace(-3.9, 3.9, 400)
    ah.plot(xx, 0.5 * xx**2, color="k", lw=2.4)
    for v in range(6):
        xt = np.sqrt(2 * E[v])                                  # turning point
        s = psi[:, v] * np.sign(psi[np.argmin(np.abs(x - 0.9 * xt)), v])   # outermost lobe up
        ah.hlines(E[v], -xt, xt, color=GRAY, lw=0.9, ls="--")
        sel = np.abs(x) < 3.95
        ah.plot(x[sel], E[v] + 0.62 * s[sel], color=TEAL, lw=2.2)
        ah.text(4.15, E[v], rf"$v = {v}$:  {E[v]:.2f}", va="center", fontsize=11)
    for v in range(3):
        ah.annotate("", xy=(-2.9, E[v + 1]), xytext=(-2.9, E[v]),
                    arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.4, shrinkA=0, shrinkB=0))
    ah.text(-3.0, 1.95, r"$\hbar\omega$", color=CARDINAL, fontsize=13, ha="right", va="center")
    ah.annotate("", xy=(0, E[0]), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6, shrinkA=0, shrinkB=0))
    ah.text(1.45, 0.22, r"$\frac{1}{2}\hbar\omega$: zero-point energy", color=ORANGE, fontsize=11.5, va="center")
    ah.set_xlim(-4.4, 6.3); ah.set_xticks([]); ah.spines["left"].set_visible(False); ah.spines["bottom"].set_visible(False)
    ah.set_title(r"spring: the walls widen, equal gaps $\hbar\omega$", loc="left", fontsize=12.5)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.91, bottom=0.03)
    fig.savefig(f"{OUT}/ho_preview.png", dpi=200)
    print("wrote", f"{OUT}/ho_preview.png")
    return fig, None


# ============================================================ lecture 4.2: the quantum harmonic oscillator
# Units hbar = mu = omega = 1, so alpha = mu omega / hbar = 1: lengths in 1/sqrt(alpha), energies in hbar omega.
# The normalized states come from the recursion y psi_v = sqrt((v+1)/2) psi_{v+1} + sqrt(v/2) psi_{v-1},
# filled into an array in place (synced cells cannot use helper functions that `return`).

# ------------------------------------------------------------ zero-point energy: Gaussian trial states of three widths, and the average energy of every width (still)
@register
def zpe_tradeoff():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    xs = np.linspace(-3, 3, 400)
    trials = [("a", 0.3, "squeezed", GRAY), ("b", np.sqrt(0.5), "the ground state", CARDINAL), ("c", 1.4, "spread out", GRAY)]
    fig = plt.figure(figsize=(9.6, 5.6))
    for j, (tag, sig, name, col) in enumerate(trials):
        ax = fig.add_axes([0.07 + 0.31 * j, 0.6, 0.27, 0.33])
        rho = np.exp(-xs**2 / (2 * sig**2)) / (sig * np.sqrt(2 * np.pi))   # |psi|^2 of a Gaussian of width sigma_x
        ax.plot(xs, 0.5 * xs**2, color="k", lw=1.6)
        ax.fill_between(xs, 0, 1.4 * rho, color=TEAL, alpha=0.3, lw=0)
        ax.plot(xs, 1.4 * rho, color=TEAL, lw=2)
        h = 1.4 * rho.max() * np.exp(-0.5)
        ax.annotate("", xy=(sig, h), xytext=(0, h), arrowprops=dict(arrowstyle="<->", color="k", lw=1.2, shrinkA=0, shrinkB=0))
        ax.set_xlim(-3, 3); ax.set_ylim(0, 2.1); ax.axis("off")
        ax.set_title(f"({tag}) {name}: " + rf"$\sigma_x = {sig:.2f}$", fontsize=12, color=col)
        K, V = 1 / (8 * sig**2), 0.5 * sig**2
        ax.text(-2.9, -0.2, f"kinetic {K:.2f}", color=ORANGE, fontsize=11.5, va="top")
        ax.text(0.15, -0.2, f"potential {V:.2f}", color=TEAL, fontsize=11.5, va="top")
    ax = fig.add_axes([0.08, 0.1, 0.9, 0.38])
    s = np.linspace(0.2, 1.75, 400)
    ax.plot(s, 1 / (8 * s**2), color=ORANGE, lw=2.4, label=r"kinetic $\sigma_p^2/2\mu$, with $\sigma_p = \hbar/2\sigma_x$")
    ax.plot(s, 0.5 * s**2, color=TEAL, lw=2.4, label=r"potential $\frac{1}{2}k\sigma_x^2$")
    ax.plot(s, 1 / (8 * s**2) + 0.5 * s**2, color="k", lw=2.8, label=r"total $\langle E\rangle$")
    for tag, sig, name, col in trials:
        E = 1 / (8 * sig**2) + 0.5 * sig**2
        ax.plot([sig], [E], "o", color=col, ms=9, zorder=5)
        ax.text(sig + 0.03, E + 0.1, f"({tag})", fontsize=12, color=col)
    ax.annotate(r"lowest: $\frac{1}{2}\hbar\omega$, the ground state", xy=(np.sqrt(0.5), 0.5), xytext=(0.98, 0.2), fontsize=12,
                color=CARDINAL, arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.2, mutation_scale=12, shrinkB=6))
    ax.set_xlim(0.2, 1.75); ax.set_ylim(0, 2.2)
    ax.set_yticks([0, 0.5, 1, 1.5, 2]); ax.set_yticklabels(["0", r"$\frac{1}{2}$", "1", r"$\frac{3}{2}$", "2"])
    ax.set_xlabel(r"width $\sigma_x$ of the Gaussian (units of $1/\sqrt{\alpha}$)", fontsize=11.5)
    ax.set_ylabel(r"average energy ($\hbar\omega$)", fontsize=11.5)
    ax.legend(loc="upper center", frameon=False, fontsize=11, ncol=3, bbox_to_anchor=(0.5, 1.12))
    fig.savefig(f"{OUT}/zpe_tradeoff.png", dpi=200)
    print("wrote", f"{OUT}/zpe_tradeoff.png")
    return fig, None


# ------------------------------------------------------------ polynomial times Gaussian: the roots of H_v become the nodes of psi_v (still)
@register
def hermite_build():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    y = np.linspace(-4.2, 4.2, 700)
    Hs = [np.ones_like(y), 2 * y, 4 * y**2 - 2, 8 * y**3 - 12 * y]
    names = [r"$H_0 = 1$", r"$H_1 = 2y$", r"$H_2 = 4y^2 - 2$", r"$H_3 = 8y^3 - 12y$"]
    roots = [[], [0.0], [-np.sqrt(0.5), np.sqrt(0.5)], [-np.sqrt(1.5), 0.0, np.sqrt(1.5)]]
    nodes = ["no node", "1 node", "2 nodes", "3 nodes"]
    fig, axes = plt.subplots(2, 4, figsize=(9.6, 4.2), gridspec_kw={"hspace": 0.45, "wspace": 0.1})
    for v in range(4):
        top, bot = axes[0, v], axes[1, v]
        H = Hs[v]
        s = np.abs(H[np.abs(y) <= 1.9]).max()                   # each panel on its own scale, set by the roots
        top.axhline(0, color=GRAY, lw=0.8)
        top.plot(y, H, color="k", lw=2.2)
        top.plot(roots[v], [0] * len(roots[v]), "o", color=CARDINAL, ms=7, zorder=5)
        top.set_ylim(-1.2 * s, 1.2 * s)
        top.set_title(names[v], fontsize=12.5)
        psi = H * np.exp(-y**2 / 2)
        m = np.abs(psi).max()
        bot.axhline(0, color=GRAY, lw=0.8)
        bot.plot(y, psi, color=TEAL, lw=2.4)
        bot.plot(roots[v], [0] * len(roots[v]), "o", color=CARDINAL, ms=7, zorder=5)
        bot.set_ylim(-1.25 * m, 1.25 * m)
        bot.set_title(rf"$\psi_{v}$: " + nodes[v], fontsize=12.5, color=TEAL)
        for ax in (top, bot):
            ax.set_xlim(-4.2, 4.2); ax.set_yticks([]); ax.set_xticks([-3, 0, 3])
            ax.spines["left"].set_visible(False); ax.tick_params(labelsize=10)
    axes[0, 0].set_ylabel("polynomial", fontsize=11.5)
    axes[1, 0].set_ylabel("state", fontsize=11.5, color=TEAL)
    fig.subplots_adjust(left=0.04, right=0.99, top=0.92, bottom=0.07)
    fig.savefig(f"{OUT}/hermite_build.png", dpi=200)
    print("wrote", f"{OUT}/hermite_build.png")
    return fig, None


# ------------------------------------------------------------ the ladder: psi_v and |psi_v|^2 on their levels, tails beyond the turning points in orange (still)
@register
def ho_ladder():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    vmax = 5
    y = np.linspace(-4.6, 4.6, 900)
    phi = np.zeros((vmax + 1, y.size))
    phi[0] = np.pi**-0.25 * np.exp(-y**2 / 2)
    phi[1] = np.sqrt(2) * y * phi[0]
    for v in range(1, vmax):
        phi[v + 1] = np.sqrt(2 / (v + 1)) * y * phi[v] - np.sqrt(v / (v + 1)) * phi[v - 1]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 4.7), sharey=True, gridspec_kw={"wspace": 0.05})
    for ax, sq in ((a1, False), (a2, True)):
        ax.plot(y, 0.5 * y**2, color="k", lw=2.2)
        for v in range(vmax + 1):
            E = v + 0.5
            yt = np.sqrt(2 * E)                                 # classical turning points
            f = 1.25 * phi[v]**2 if sq else 0.5 * phi[v]
            ax.hlines(E, -yt, yt, color=GRAY, lw=0.8, ls="--")
            ax.fill_between(y, E, E + f, where=np.abs(y) >= yt, color=ORANGE, alpha=0.6, lw=0)
            ax.plot(y, E + f, color=TEAL, lw=2)
            ax.plot([-yt, yt], [E, E], "o", color="k", ms=3)
        ax.set_xlim(-4.6, 4.6); ax.set_ylim(0, 6.5); ax.set_xticks([])
        ax.spines["bottom"].set_visible(False)
    for v in range(vmax + 1):
        a2.text(4.7, v + 0.5, rf"$v = {v}$", va="center", fontsize=11.5)
    a1.set_yticks([v + 0.5 for v in range(vmax + 1)])
    a1.set_yticklabels([r"$\frac{1}{2}$", r"$\frac{3}{2}$", r"$\frac{5}{2}$", r"$\frac{7}{2}$", r"$\frac{9}{2}$", r"$\frac{11}{2}$"], fontsize=12.5)
    a1.set_ylabel(r"energy ($\hbar\omega$)", fontsize=12)
    a1.set_title(r"$\psi_v(x)$: $v$ nodes, even and odd in turn", loc="left", fontsize=12.5)
    a2.set_title(r"$|\psi_v(x)|^2$: orange lies beyond the turning points", loc="left", fontsize=12.5)
    a2.spines["left"].set_visible(False); a2.tick_params(left=False)
    fig.subplots_adjust(left=0.07, right=0.93, top=0.92, bottom=0.03)
    fig.savefig(f"{OUT}/ho_ladder.png", dpi=200)
    print("wrote", f"{OUT}/ho_ladder.png")
    return fig, None


# ------------------------------------------------------------ orthogonality: odd products cancel by symmetry, even ones by their lobes (still)
@register
def ho_orthogonality():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    y = np.linspace(-4.5, 4.5, 1201); dy = y[1] - y[0]
    phi = np.zeros((3, y.size))
    phi[0] = np.pi**-0.25 * np.exp(-y**2 / 2)
    phi[1] = np.sqrt(2) * y * phi[0]
    phi[2] = y * phi[1] - np.sqrt(0.5) * phi[0]
    cases = [(0, 1, "odd product:\ncancels by symmetry"), (0, 2, "even product:\nthe lobes cancel"), (1, 1, "a state with itself:\nall positive")]
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.3), sharey=True, gridspec_kw={"wspace": 0.08})
    for ax, (m, n, note) in zip(axes, cases):
        f = phi[m] * phi[n]
        ax.fill_between(y, f, 0, where=f > 0, color=PURPLE, alpha=0.45, lw=0)
        ax.fill_between(y, f, 0, where=f < 0, color=ORANGE, alpha=0.55, lw=0)
        ax.plot(y, f, color="k", lw=1.6)
        ax.axhline(0, color=GRAY, lw=0.8)
        ax.set_title(rf"$\psi_{m}\,\psi_{n}$", fontsize=14)
        area = np.sum(f) * dy
        ax.set_xlabel(note + "\n" + rf"area $= {abs(area):.2f}$", fontsize=11.5)
        ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
        ax.set_ylim(-0.42, 0.62); ax.set_xlim(-4.5, 4.5)
    axes[0].set_yticks([0])
    for ax in axes[1:]:
        ax.spines["left"].set_visible(False); ax.tick_params(left=False)
    fig.subplots_adjust(left=0.04, right=0.99, top=0.89, bottom=0.23)
    fig.savefig(f"{OUT}/ho_orthogonality.png", dpi=200)
    print("wrote", f"{OUT}/ho_orthogonality.png")
    return fig, None


# ------------------------------------------------------------ toward the classical spring: |psi_v|^2 against P(x) as v climbs, x in units of the turning point
@register
def classical_limit():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    vmax = 24
    yg = np.linspace(-12, 12, 6001)
    phi = np.zeros((vmax + 1, yg.size))
    phi[0] = np.pi**-0.25 * np.exp(-yg**2 / 2)
    phi[1] = np.sqrt(2) * yg * phi[0]
    for v in range(1, vmax):
        phi[v + 1] = np.sqrt(2 / (v + 1)) * yg * phi[v] - np.sqrt(v / (v + 1)) * phi[v - 1]
    vs = [0, 0, 0] + list(range(1, vmax + 1)) + [vmax] * 4  # hold the first and last frames
    u = np.linspace(-1.55, 1.55, 900)                           # position in units of the turning point
    uc = np.linspace(-0.995, 0.995, 400)
    fig, ax = plt.subplots(figsize=(8.6, 4.0))
    ax.axvspan(-1.55, -1, color=GRAY, alpha=0.12, lw=0); ax.axvspan(1, 1.55, color=GRAY, alpha=0.12, lw=0)
    ax.axvline(-1, color=GRAY, lw=1, ls=":"); ax.axvline(1, color=GRAY, lw=1, ls=":")
    ax.plot(uc, 1 / (np.pi * np.sqrt(1 - uc**2)), color=CARDINAL, lw=2.4, label="classical spring, same energy")
    fill = [ax.fill_between(u, 0, 0 * u, color=TEAL, alpha=0.3, lw=0)]
    (line,) = ax.plot([], [], color=TEAL, lw=2.2, label=r"quantum $|\psi_v|^2$")
    ax.set_xlim(-1.55, 1.55); ax.set_ylim(0, 1.8)
    ax.set_xticks([-1, 0, 1]); ax.set_xticklabels(["left turning point", "0", "right turning point"], fontsize=11)
    ax.set_yticks([]); ax.set_ylabel("probability density", fontsize=11.5)
    ax.legend(loc="lower center", frameon=False, fontsize=11.5, ncol=2, bbox_to_anchor=(0.5, 1.0))
    ax.text(-1.52, 1.5, "classically\nforbidden", fontsize=10.5, color=GRAY)
    ax.text(1.52, 1.5, "classically\nforbidden", fontsize=10.5, color=GRAY, ha="right")
    lab = ax.text(0, 1.3, "", ha="center", fontsize=13)
    fig.subplots_adjust(left=0.06, right=0.98, top=0.89, bottom=0.11)

    def update(i):
        v = vs[i]
        yt = np.sqrt(2 * v + 1)
        dens = np.interp(u * yt, yg, phi[v]**2) * yt            # density per unit of u = x / x_turn
        line.set_data(u, dens)
        fill[0].remove()
        fill[0] = ax.fill_between(u, 0, dens, color=TEAL, alpha=0.3, lw=0)
        yi = np.linspace(-yt, yt, 4001)
        out = 1 - np.trapezoid(np.interp(yi, yg, phi[v]**2), yi)
        lab.set_text(rf"$v = {v}$:  {100 * out:.1f}% beyond the turning points")

    ani = FuncAnimation(fig, update, frames=len(vs), interval=330, blit=False)
    return fig, ani


classical_limit.fps = 3


# ------------------------------------------------------------ raising and lowering: a-dagger climbs one rung, a steps down, and the ladder has a bottom (still)
@register
def ladder_climb():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    y = np.linspace(-3.6, 3.6, 500)
    phi = np.zeros((3, y.size))
    phi[0] = np.pi**-0.25 * np.exp(-y**2 / 2)
    phi[1] = np.sqrt(2) * y * phi[0]
    phi[2] = y * phi[1] - np.sqrt(0.5) * phi[0]
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.6), gridspec_kw={"width_ratios": [1.15, 1], "wspace": 0.08})
    yy = np.linspace(-3.03, 3.03, 300)
    ax.plot(yy, 0.5 * yy**2, color="k", lw=2.2)
    for v in range(5):
        E = v + 0.5
        ax.hlines(E, -np.sqrt(2 * E), np.sqrt(2 * E), color=TEAL, lw=2.4)
        ax.text(np.sqrt(2 * E) + 0.12, E, rf"$\psi_{v}$", va="center", fontsize=12, color=TEAL)
    for v in range(4):
        ax.annotate("", xy=(-0.55, v + 1.45), xytext=(-0.55, v + 0.55),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2, mutation_scale=16, shrinkA=0, shrinkB=0))
        ax.annotate("", xy=(0.55, v + 0.55), xytext=(0.55, v + 1.45),
                    arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2, mutation_scale=16, shrinkA=0, shrinkB=0))
    ax.text(-3.3, 5.0, r"$\hat{a}^\dagger$: up one rung, $+\hbar\omega$", ha="left", fontsize=12, color=ORANGE)
    ax.text(0.45, 5.0, r"$\hat{a}$: down one rung, $-\hbar\omega$", ha="left", fontsize=12, color=PURPLE)
    ax.annotate("", xy=(0.55, 0.06), xytext=(0.55, 0.45),
                arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.6, ls="--", mutation_scale=13, shrinkA=0, shrinkB=0))
    ax.plot([0.55], [0.22], "x", color=CARDINAL, ms=12, mew=2.6)
    ax.text(0.8, 0.12, r"$\hat{a}\psi_0 = 0$: the ladder has a bottom", fontsize=11.5, color=CARDINAL, va="center")
    ax.set_xlim(-3.4, 3.9); ax.set_ylim(0, 5.4); ax.axis("off")
    ax.set_title(r"rungs $\hbar\omega$ apart, starting at $\frac{1}{2}\hbar\omega$", loc="left", fontsize=12.5)
    names = [r"$\psi_0 \propto e^{-y^2/2}$", r"$\hat{a}^\dagger\psi_0 \propto y\,e^{-y^2/2} \propto \psi_1$",
             r"$\hat{a}^\dagger\psi_1 \propto (2y^2 - 1)\,e^{-y^2/2} \propto \psi_2$"]
    for v in range(3):
        off = 1.9 * v
        bx.axhline(off, color="#dee2e6", lw=0.8)
        bx.plot(y, off + 0.95 * phi[v], color=TEAL, lw=2.2)
        bx.text(-3.6, off + 0.98, names[v], fontsize=12, va="center")
    for v in range(2):
        bx.annotate("", xy=(3.25, 1.9 * v + 1.6), xytext=(3.25, 1.9 * v + 0.35),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2, mutation_scale=16, shrinkA=0, shrinkB=0))
        bx.text(3.4, 1.9 * v + 0.95, r"$\hat{a}^\dagger$", color=ORANGE, fontsize=13, va="center")
    bx.set_xlim(-3.7, 3.9); bx.set_ylim(-0.75, 5.3); bx.axis("off")
    bx.set_title(r"each step up adds one node", loc="left", fontsize=12.5)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.92, bottom=0.02)
    fig.savefig(f"{OUT}/ladder_climb.png", dpi=200)
    print("wrote", f"{OUT}/ladder_climb.png")
    return fig, None


# ------------------------------------------------------------ H and x as matrices in the oscillator's own eigenbasis: diagonal and nearest-neighbour (still)
@register
def x_matrix():
    from matplotlib.patches import Rectangle
    n = 7
    Hm = np.diag(np.arange(n) + 0.5)
    Xm = np.diag(np.sqrt(np.arange(1, n) / 2), 1)
    Xm = Xm + Xm.T                                              # <v'|x|v> in units of 1/sqrt(alpha)
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.5), gridspec_kw={"wspace": 0.16})
    titles = [r"$\langle v'|\hat{H}|v\rangle$ in units of $\hbar\omega$", r"$\langle v'|\hat{x}|v\rangle$ in units of $1/\sqrt{\alpha}$"]
    for ax, M, title in zip(axes, (Hm, Xm), titles):
        for i in range(n):
            for j in range(n):
                val = M[i, j]
                fc, tc = ("white", "#adb5bd") if val == 0 else (("#ebe3f4", PURPLE) if i == j else ("#fde9d2", ORANGE))
                ax.add_patch(Rectangle((j, n - 1 - i), 1, 1, fc=fc, ec="#ced4da", lw=0.8))
                ax.text(j + 0.5, n - 0.5 - i, "0" if val == 0 else f"{val:.2f}", ha="center", va="center",
                        fontsize=10.5, color=tc, weight="normal" if val == 0 else "bold")
        ax.set_xlim(0, n); ax.set_ylim(0, n); ax.set_aspect("equal")
        ax.set_xticks(np.arange(n) + 0.5); ax.set_xticklabels(range(n)); ax.xaxis.tick_top()
        ax.set_yticks(np.arange(n) + 0.5); ax.set_yticklabels(range(n - 1, -1, -1))
        ax.tick_params(length=0, labelsize=11)
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_xlabel(title, fontsize=12.5, labelpad=8)
        ax.text(-0.75, n / 2, r"$v'$", fontsize=13, ha="center", va="center")
        ax.text(n / 2, n + 0.85, r"$v$", fontsize=13, ha="center", va="center")
    fig.subplots_adjust(left=0.05, right=0.99, top=0.88, bottom=0.1)
    fig.savefig(f"{OUT}/x_matrix.png", dpi=200)
    print("wrote", f"{OUT}/x_matrix.png")
    return fig, None


# ============================================================ lecture 4.3: molecular vibrations
# Wavenumbers in cm^-1. HCl uses the Morse well of Lecture 4.1 (D = 4.62 eV, a = 1.87 1/A) for shapes and the
# measured lines (2886, 5668, 8347 cm^-1; nu_e = 2990, nu_e x_e = 52) for positions.
# dipole_area and rung_area are deck-only (deck 4.3 "Light needs a transition dipole" and "Selection rules": the
# transition dipole as the area under psi_v' M psi_0). dipole_slosh is unused since 2026-11-01 (kept); the page shows
# that idea live with widgets/transition_dipole.mjs.
# dipole_kick and dipole_slosh use units hbar = mu = omega = 1, x in units of 1/sqrt(alpha).

# ------------------------------------------------------------ light pushes on a dipole: HCl's dipole swings with the stretch, N2 has none
@register
def dipole_antenna():
    from matplotlib.patches import Circle
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    nf = 32
    ts = np.arange(nf) / nf                                     # one loop of the animation = two vibrations
    GREEN, BLUE = "#2f9e44", "#1c7ed6"
    rows = [(("H", "Cl"), ("white", GREEN), (0.15, 0.29), (1.0, 35.0), True,
             "HCl: the dipole swings with the bond", r"$M(t) = M_e + M'x(t)$: the swing couples to light"),
            (("N", "N"), (BLUE, BLUE), (0.24, 0.24), (14.0, 14.0), False,
             r"N$_2$: symmetric, no dipole at any length", r"$M = 0$ always: light has nothing to push on")]
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 4.6), gridspec_kw={"width_ratios": [1, 1.2], "hspace": 0.65, "wspace": 0.12})
    tt = np.linspace(0, 1, 300)
    parts = []
    for (ax, bx), (labels, cols, rads, masses, polar, t1, t2) in zip(axes, rows):
        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-0.6, 1.0); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(t1, loc="left", fontsize=12)
        (bond,) = ax.plot([], [], color="#adb5bd", lw=6, solid_capstyle="round", zorder=2)
        c1 = Circle((0, 0), rads[0], fc=cols[0], ec="k", lw=1, zorder=3); ax.add_patch(c1)
        c2 = Circle((0, 0), rads[1], fc=cols[1], ec="k", lw=1, zorder=3); ax.add_patch(c2)
        l1 = ax.text(0, 0, labels[0], ha="center", va="center", fontsize=10, weight="bold", zorder=4,
                     color="k" if cols[0] == "white" else "white")
        l2 = ax.text(0, 0, labels[1], ha="center", va="center", fontsize=10, weight="bold", zorder=4, color="white")
        (bar,) = ax.plot([], [], color=ORANGE, lw=6, solid_capstyle="butt")
        if polar:
            ax.text(-0.62, -0.5, r"$\delta+$", ha="center", fontsize=11, color=CARDINAL)
            ax.text(0.62, -0.5, r"$\delta-$", ha="center", fontsize=11, color=BLUE)
            ax.text(-1.45, 0.72, "dipole", fontsize=11, color=ORANGE, va="center")
        else:
            ax.text(-1.45, 0.72, r"dipole: $M = 0$", fontsize=11, color=ORANGE, va="center")
        bx.axhline(0, color=GRAY, lw=0.8)
        if polar:
            bx.axhline(1, color=GRAY, lw=1, ls=":")
            bx.text(1.0, 1.08, r"$M_e$", ha="right", fontsize=11, color=GRAY)
        bx.plot(tt, (1 + 0.45 * np.sin(4 * np.pi * tt)) if polar else 0 * tt, color="#dee2e6", lw=1.8)
        (trace,) = bx.plot([], [], color=ORANGE, lw=2.4)
        (dot,) = bx.plot([], [], "o", color=ORANGE, ms=7)
        bx.set_xlim(0, 1); bx.set_ylim(-0.25, 1.75); bx.set_yticks([]); bx.set_xticks([])
        bx.spines["bottom"].set_visible(False)
        bx.set_xlabel("time", fontsize=11); bx.set_ylabel(r"dipole $M(t)$", fontsize=11.5)
        bx.set_title(t2, loc="left", fontsize=12)
        parts.append((masses, polar, bond, c1, c2, l1, l2, bar, trace, dot))
    fig.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.08)

    def update(i):
        s = 0.2 * np.sin(4 * np.pi * ts[i])                     # the stretch, exaggerated
        for (m1, m2), polar, bond, c1, c2, l1, l2, bar, trace, dot in parts:
            p1, p2 = -0.6 - s * m2 / (m1 + m2), 0.6 + s * m1 / (m1 + m2)
            bond.set_data([p1, p2], [0, 0])
            c1.center, c2.center = (p1, 0), (p2, 0)
            l1.set_position((p1, 0)); l2.set_position((p2, 0))
            mu = 1 + 2.25 * s if polar else 0.0
            bar.set_data([-0.62, -0.62 + 0.9 * mu], [0.72, 0.72])
            sel = tt <= ts[i] + 1e-9
            trace.set_data(tt[sel], (1 + 0.45 * np.sin(4 * np.pi * tt[sel])) if polar else 0 * tt[sel])
            dot.set_data([ts[i]], [mu])

    ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
    return fig, ani


# ------------------------------------------------------------ what each term of the dipole does to psi_0: the kicked function and its components (still)
@register
def dipole_kick():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4.5, 4.5, 1201)                            # units of 1/sqrt(alpha)
    dx = x[1] - x[0]
    nv = 5
    psi = np.zeros((nv, x.size))                                # normalized oscillator states, filled by the recursion
    psi[0] = np.pi ** -0.25 * np.exp(-x ** 2 / 2)
    psi[1] = np.sqrt(2) * x * psi[0]
    for v in range(1, nv - 1):
        psi[v + 1] = np.sqrt(2 / (v + 1)) * x * psi[v] - np.sqrt(v / (v + 1)) * psi[v - 1]
    cols = [(np.ones_like(x), r"constant term $M_e$", r"$1\cdot\psi_0 = \psi_0$", None,
             r"$\langle v'|1|0\rangle$: no transition"),
            (x, r"linear term $M'x$", r"$x\,\psi_0 = \frac{1}{\sqrt{2}}\,\psi_1$", (1, r"$\frac{1}{\sqrt{2}}\psi_1$"),
             r"$\langle v'|x|0\rangle$: only $0 \to 1$"),
            (x ** 2, r"quadratic term $\frac{1}{2}M''x^2$", r"$x^2\psi_0 = \frac{1}{2}\psi_0 + \frac{1}{\sqrt{2}}\,\psi_2$",
             (2, r"$\frac{1}{\sqrt{2}}\psi_2$"), r"$\langle v'|x^2|0\rangle$: $0 \to 2$ too")]
    fig, axes = plt.subplots(2, 3, figsize=(9.6, 4.1), gridspec_kw={"height_ratios": [1.2, 1], "hspace": 0.78, "wspace": 0.2})
    for j, (f, head, ident, part, verdict) in enumerate(cols):
        ax, bx = axes[0, j], axes[1, j]
        kick = f * psi[0]
        comp = psi @ kick * dx                                  # <v'| f |0> for v' = 0..4
        ax.axhline(0, color=GRAY, lw=0.8)
        ax.plot(x, psi[0], color=GRAY, lw=1.6, ls="--")
        ax.plot(x, kick, color=ORANGE, lw=2.6)
        if part is not None:
            ax.plot(x, comp[part[0]] * psi[part[0]], color=TEAL, lw=2.2, ls=(0, (1.5, 1.8)))
            ax.text(1.9, 0.5, part[1], color=TEAL, fontsize=13)
        ax.set_xlim(-4, 4); ax.set_ylim(-0.5, 0.8); ax.set_yticks([]); ax.set_xticks([])
        ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
        ax.set_title(head + "\n" + ident, loc="left", fontsize=13, linespacing=1.6)
        bx.bar(np.arange(nv), comp, width=0.6, color=[PURPLE] + [ORANGE] * (nv - 1))
        for v in range(nv):
            if abs(comp[v]) > 0.005:
                bx.text(v, comp[v] + 0.05, f"{comp[v]:.2f}", ha="center", va="bottom", fontsize=12,
                        color=PURPLE if v == 0 else ORANGE)
        bx.axhline(0, color=GRAY, lw=0.8)
        bx.set_ylim(0, 1.3); bx.set_yticks([]); bx.spines["left"].set_visible(False)
        bx.set_xticks(range(nv)); bx.tick_params(labelsize=12)
        bx.set_xlabel(r"$v'$", fontsize=13, labelpad=0)
        bx.set_title(verdict, loc="left", fontsize=13)
    axes[0, 1].text(-1.9, 0.66, r"$\psi_0$", color=GRAY, fontsize=13)
    axes[0, 0].text(1.35, 0.52, "after the kick", color=ORANGE, fontsize=12.5)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.84, bottom=0.11)
    fig.savefig(f"{OUT}/dipole_kick.png", dpi=200)
    print("wrote", f"{OUT}/dipole_kick.png")
    return fig, None


# ------------------------------------------------------------ the absorbing superposition: psi_0 + psi_1 sloshes at omega, psi_0 + psi_2 breathes at 2 omega
@register
def dipole_slosh():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4.5, 4.5, 901)                             # units of 1/sqrt(alpha); omega = 1
    dx = x[1] - x[0]
    psi0 = np.pi ** -0.25 * np.exp(-x ** 2 / 2)
    psi1 = np.sqrt(2) * x * psi0
    psi2 = (2 * x ** 2 - 1) / np.sqrt(2) * psi0
    nf = 36
    ts = 2 * np.pi * np.arange(nf) / nf                         # one loop = one period of the vibration
    tt = np.linspace(0, 2 * np.pi, 400)
    cases = [(psi1, 1, r"$\psi_0 + \psi_1$: the density sloshes at $\omega$",
              r"$\langle x\rangle$ swings at $\omega$: a dipole $M'x$ follows"),
             (psi2, 2, r"$\psi_0 + \psi_2$: the density breathes at $2\omega$",
              r"$\langle x\rangle$ stays put; the width swings at $2\omega$")]
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 4.6), gridspec_kw={"height_ratios": [1.3, 1], "hspace": 0.55, "wspace": 0.14})
    parts = []
    for (ax, bx), (pv, n, t1, t2) in zip(axes.T, cases):
        dens = lambda t, pv=pv, n=n: 0.5 * (psi0 ** 2 + pv ** 2) + psi0 * pv * np.cos(n * t)
        a1 = np.sum(x * psi0 * pv) * dx                         # <v'|x|0>: amplitude of <x>(t)
        a2 = np.sum(x ** 2 * psi0 * pv) * dx                    # <v'|x^2|0>: amplitude of the width's swing
        ax.plot(x, psi0 ** 2, color=GRAY, lw=1.2, ls=":")
        ax.axhline(0, color=GRAY, lw=0.8)
        (line,) = ax.plot([], [], color=TEAL, lw=2.2)
        (mark,) = ax.plot([], [], color=ORANGE, lw=2.4)
        (dot,) = ax.plot([], [], "o", color=ORANGE, ms=7, clip_on=False)
        ax.set_xlim(-4, 4); ax.set_ylim(0, 0.95); ax.set_yticks([]); ax.set_xticks([])
        ax.spines["left"].set_visible(False)
        ax.set_xlabel(r"stretch $x$", fontsize=11.5)
        ax.set_title(t1, loc="left", fontsize=12.5)
        bx.axhline(0, color=GRAY, lw=0.8)
        bx.plot(tt / (2 * np.pi), a1 * np.cos(n * tt), color="#f3d9b8", lw=1.8)
        bx.plot(tt / (2 * np.pi), a2 * np.cos(n * tt), color="#ddd0ea", lw=1.8, ls="--")
        (tr1,) = bx.plot([], [], color=ORANGE, lw=2.4, label=r"$\langle x\rangle$")
        (tr2,) = bx.plot([], [], color=PURPLE, lw=2.2, ls="--", label=r"$\langle x^2\rangle$ about its mean")
        (d1,) = bx.plot([], [], "o", color=ORANGE, ms=6)
        (d2,) = bx.plot([], [], "o", color=PURPLE, ms=6)
        bx.set_xlim(0, 1); bx.set_ylim(-0.95, 0.95); bx.set_yticks([]); bx.set_xticks([])
        bx.spines["bottom"].set_visible(False)
        bx.set_xlabel("time, one vibration period", fontsize=11.5)
        bx.set_title(t2, loc="left", fontsize=12.5)
        parts.append(dict(ax=ax, dens=dens, n=n, a1=a1, a2=a2, line=line, mark=mark, dot=dot,
                          tr1=tr1, tr2=tr2, d1=d1, d2=d2, poly=None))
    axes[1, 0].legend(loc="upper center", frameon=False, fontsize=10.5, ncol=2)
    axes[0, 0].text(-3.9, 0.6, "ground state", color=GRAY, fontsize=10.5)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.92, bottom=0.08)

    def update(i):
        t = ts[i]
        sel = tt <= t + 1e-9
        for p in parts:
            d = p["dens"](t)
            if p["poly"] is not None:
                p["poly"].remove()
            p["poly"] = p["ax"].fill_between(x, 0, d, color=TEAL, alpha=0.25, lw=0)
            p["line"].set_data(x, d)
            xm = p["a1"] * np.cos(p["n"] * t)                   # <x>(t)
            p["mark"].set_data([xm, xm], [0, 0.85])
            p["dot"].set_data([xm], [0])
            p["tr1"].set_data(tt[sel] / (2 * np.pi), p["a1"] * np.cos(p["n"] * tt[sel]))
            p["tr2"].set_data(tt[sel] / (2 * np.pi), p["a2"] * np.cos(p["n"] * tt[sel]))
            p["d1"].set_data([t / (2 * np.pi)], [xm])
            p["d2"].set_data([t / (2 * np.pi)], [p["a2"] * np.cos(p["n"] * t)])

    ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
    return fig, ani


dipole_slosh.fps = 12


# ------------------------------------------------------------ deck: why the transition dipole must be nonzero; HCl vs N2 as the area under psi_1 M psi_0 (still)
@register
def dipole_area():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4.5, 4.5, 1201)                            # units of 1/sqrt(alpha)
    dx = x[1] - x[0]
    psi0 = np.pi ** -0.25 * np.exp(-x ** 2 / 2)
    psi1 = np.sqrt(2) * x * psi0
    cases = [("HCl: the dipole changes", 1.0 + 0.6 * x, r"$M(x)$", "absorbed"),
             (r"N$_2$: no dipole at all", 0.0 * x, r"$M = 0$", "not absorbed")]
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 4.4), gridspec_kw={"height_ratios": [1, 1.1], "hspace": 0.62, "wspace": 0.12})
    for (ax, bx), (title, M, mlab, verdict) in zip(axes.T, cases):
        sel = np.abs(x) <= 3.2
        ax.axhline(0, color=GRAY, lw=0.8)
        ax.plot(x, psi0, color=GRAY, lw=1.8, ls="--")
        ax.plot(x, psi1, color=TEAL, lw=2.2)
        ax.plot(x[sel], 0.18 * M[sel], color=CARDINAL, lw=2.6)
        ax.text(-2.15, 0.6, r"$\psi_0$", color=GRAY, fontsize=16)
        ax.text(1.65, 0.66, r"$\psi_1$", color=TEAL, fontsize=16)
        ax.text(3.3, 0.18 * M[sel][-1] + (0.04 if M.any() else -0.06), mlab, color=CARDINAL, fontsize=16,
                va="bottom" if M.any() else "top", ha="right")
        ax.set_title(title, loc="left", fontsize=16)
        f = psi1 * M * psi0
        area = np.sum(f) * dx
        bx.fill_between(x, f, 0, where=f > 0, color=PURPLE, alpha=0.45, lw=0)
        bx.fill_between(x, f, 0, where=f < 0, color=ORANGE, alpha=0.55, lw=0)
        bx.plot(x, f, color="k", lw=1.6)
        bx.axhline(0, color=GRAY, lw=0.8)
        bx.set_title(r"multiply: $\psi_1\,M\,\psi_0$", loc="left", fontsize=16)
        bx.set_xlabel(("area = 0" if abs(area) < 1e-3 else f"area = {abs(area):.2f}") + f": {verdict}", fontsize=16,
                      color=PURPLE if abs(area) > 1e-3 else GRAY, weight="bold")
        for a in (ax, bx):
            a.set_xlim(-4, 4); a.set_xticks([]); a.set_yticks([]); a.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.set_ylim(-0.7, 0.85); bx.set_ylim(-0.46, 0.55)
        bx.spines["bottom"].set_visible(False)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.91, bottom=0.12)
    fig.savefig(f"{OUT}/dipole_area.png", dpi=200)
    print("wrote", f"{OUT}/dipole_area.png")
    return fig, None


# ------------------------------------------------------------ deck: one rung at a time; for HCl, 0 -> 1 leaves an area, 0 -> 2 cancels (still)
@register
def rung_area():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    x = np.linspace(-4.5, 4.5, 1201)                            # units of 1/sqrt(alpha)
    dx = x[1] - x[0]
    psi0 = np.pi ** -0.25 * np.exp(-x ** 2 / 2)
    psi1 = np.sqrt(2) * x * psi0
    psi2 = (2 * x ** 2 - 1) / np.sqrt(2) * psi0
    M = 1.0 + 0.6 * x                                           # HCl-like: permanent dipole plus a slope
    cases = [(r"$v = 0 \to 1$: one rung", psi1, 1, "allowed"),
             (r"$v = 0 \to 2$: two rungs", psi2, 2, "lobes cancel, forbidden")]
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 3.7), gridspec_kw={"height_ratios": [0.85, 1], "hspace": 0.68, "wspace": 0.12})
    for (ax, bx), (title, pv, n, verdict) in zip(axes.T, cases):
        sel = np.abs(x) <= 3.2
        ax.axhline(0, color=GRAY, lw=0.8)
        ax.plot(x, psi0, color=GRAY, lw=1.8, ls="--")
        ax.plot(x, pv, color=TEAL, lw=2.2)
        ax.plot(x[sel], 0.18 * M[sel], color=CARDINAL, lw=2.6)
        if n == 1:                                              # the 0 -> 2 panel reuses the same gray dashed psi_0
            ax.text(-2.15, 0.6, r"$\psi_0$", color=GRAY, fontsize=16)
        ax.text(1.65 if n == 1 else -2.95, 0.66 if n == 1 else 0.5, rf"$\psi_{n}$", color=TEAL, fontsize=16)
        ax.text(3.3, 0.18 * M[sel][-1] + 0.04, r"$M(x)$", color=CARDINAL, fontsize=16, va="bottom", ha="right")
        ax.set_title(title, loc="left", fontsize=16)
        f = pv * M * psi0
        area = np.sum(f) * dx
        bx.fill_between(x, f, 0, where=f > 0, color=PURPLE, alpha=0.45, lw=0)
        bx.fill_between(x, f, 0, where=f < 0, color=ORANGE, alpha=0.55, lw=0)
        bx.plot(x, f, color="k", lw=1.6)
        bx.axhline(0, color=GRAY, lw=0.8)
        bx.set_title(rf"multiply: $\psi_{n}\,M\,\psi_0$", loc="left", fontsize=16)
        bx.set_xlabel(("area = 0" if abs(area) < 1e-3 else f"area = {abs(area):.2f}") + f": {verdict}", fontsize=16,
                      color=PURPLE if abs(area) > 1e-3 else GRAY, weight="bold")
        for a in (ax, bx):
            a.set_xlim(-4, 4); a.set_xticks([]); a.set_yticks([]); a.spines["left"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.set_ylim(-0.7, 0.85); bx.set_ylim(-0.46, 0.55)
        bx.spines["bottom"].set_visible(False)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.9, bottom=0.13)
    fig.savefig(f"{OUT}/rung_area.png", dpi=200)
    print("wrote", f"{OUT}/rung_area.png")
    return fig, None


# ------------------------------------------------------------ where diatomic molecules absorb: hydrides high, heavy pairs low; hollow = IR inactive (still)
@register
def diatomic_ruler():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False})
    hyd = [("HF", 4138, 1, 1), ("HCl", 2991, 1, 1), ("HBr", 2649, 1, -1), ("HI", 2309, 1, 1), ("H$_2$", 4401, 0, -1)]
    heavy = [("N$_2$", 2359, 0, 1), ("CO", 2170, 1, -1), ("NO", 1904, 1, 1), ("O$_2$", 1580, 0, -1),
             ("Cl$_2$", 560, 0, 1), ("I$_2$", 215, 0, -1)]
    fig, ax = plt.subplots(figsize=(9.6, 3.7))
    for y, group in ((1.0, hyd), (0.0, heavy)):
        ax.axhline(y, color="#dee2e6", lw=1, zorder=1)
        for name, w, act, side in group:
            ax.plot([w], [y], "o", ms=12, mfc=TEAL if act else "white", mec=TEAL, mew=2.2, zorder=3)
            ax.text(w, y + 0.2 * side, name, ha="center", va="center", fontsize=12.5)
    ax.text(4580, 1.0, "one H atom\n" + r"$\mu \approx 1$ u", ha="right", va="center", fontsize=11, color=GRAY)
    ax.text(4580, 0.0, "two heavy atoms\n" + r"$\mu$ = 7 to 63 u", ha="right", va="center", fontsize=11, color=GRAY)
    ax.annotate("", xy=(2309, 1.42), xytext=(4138, 1.42),
                arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.4, mutation_scale=14))
    ax.text(3220, 1.52, "down the halogen group: weaker bond, lower wavenumber", ha="center", fontsize=11, color=CARDINAL)
    ax.annotate("", xy=(560, -0.45), xytext=(2359, -0.45),
                arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.4, mutation_scale=14))
    ax.text(1460, -0.62, r"N$\equiv$N, O=O, Cl$-$Cl: bond order 3, 2, 1", ha="center", fontsize=11, color=PURPLE)
    ax.plot([], [], "o", ms=10, mfc=TEAL, mec=TEAL, label="IR active: the dipole changes")
    ax.plot([], [], "o", ms=10, mfc="white", mec=TEAL, mew=2, label="IR inactive: no dipole at any length")
    ax.legend(loc="upper right", frameon=False, fontsize=11, bbox_to_anchor=(1.0, 1.18), ncol=2)
    ax.set_xlim(4600, 0); ax.set_ylim(-0.8, 1.7); ax.set_yticks([])
    ax.set_xlabel(r"harmonic wavenumber $\tilde{\nu}$ (cm$^{-1}$)", fontsize=11.5)
    fig.subplots_adjust(left=0.17, right=0.99, top=0.88, bottom=0.16)
    fig.savefig(f"{OUT}/diatomic_ruler.png", dpi=200)
    print("wrote", f"{OUT}/diatomic_ruler.png")
    return fig, None


# ------------------------------------------------------------ harmonic vs Morse ladder for HCl: equal steps forever vs shrinking steps and a last level (still)
@register
def morse_ladder():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    D, a, re, hw = 4.62, 1.87, 1.275, 0.3708                   # HCl: eV, 1/A, A, hbar omega in eV
    xe = hw**2 / (4 * D)                                        # Morse anharmonicity (eV)
    k = 2 * D * a * a
    G = lambda v: hw * (v + 0.5) - xe * (v + 0.5)**2
    turn = lambda E: (re - np.log(1 + np.sqrt(E / D)) / a, re - np.log(1 - np.sqrt(E / D)) / a)
    r = np.linspace(0.8, 3.8, 700)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.5), sharey=True, gridspec_kw={"wspace": 0.06})
    ax1.plot(r, 0.5 * k * (r - re)**2, color=ORANGE, lw=2.4)
    for v in range(15):
        E = hw * (v + 0.5)
        h = np.sqrt(2 * E / k)
        ax1.hlines(E, re - h, re + h, color=TEAL if v < 3 else "#adb5bd", lw=1.6 if v < 3 else 1.0)
    ax1.set_title("harmonic: equal steps forever,\nthe bond never comes apart", loc="left", fontsize=12, color=ORANGE)
    ax2.plot(r, D * (1 - np.exp(-a * (r - re)))**2, color="k", lw=2.4)
    vmax = int(hw / (2 * xe) - 0.5)                         # last level below the dissociation limit
    for v in range(vmax + 1):
        r1, r2 = turn(G(v))
        ax2.hlines(G(v), r1, r2, color=TEAL if v < 3 else "#adb5bd", lw=1.6 if v < 3 else 1.0)
    ax2.axhline(D, color=GRAY, lw=1, ls="--")
    ax2.text(3.75, D + 0.08, "atoms apart", ha="right", va="bottom", fontsize=11, color=GRAY)
    ax2.annotate("", xy=(3.15, D), xytext=(3.15, 0), arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.4, shrinkA=0, shrinkB=0))
    ax2.text(3.2, D / 2, r"$D_e$", fontsize=13, color=CARDINAL, va="center")
    ax2.annotate("", xy=(2.75, D), xytext=(2.75, G(0)), arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.4, shrinkA=0, shrinkB=0))
    ax2.text(2.8, D / 2 + 0.3, r"$D_0$", fontsize=13, color=PURPLE, va="center")
    ax2.set_title("Morse: the steps shrink, a last level,\nthen dissociation", loc="left", fontsize=12)
    for ax in (ax1, ax2):
        ax.set_xlim(0.8, 3.8); ax.set_ylim(0, 5.3)
        ax.set_xlabel(r"bond length $R$ ($\AA$)", fontsize=11.5)
    ax1.set_ylabel("energy (eV)", fontsize=11.5)
    fig.subplots_adjust(left=0.07, right=0.99, top=0.86, bottom=0.13)
    fig.savefig(f"{OUT}/morse_ladder.png", dpi=200)
    print("wrote", f"{OUT}/morse_ladder.png")
    return fig, None


# ------------------------------------------------------------ HCl overtones: arrows on the anharmonic ladder and the lines they make (still)
@register
def hcl_overtones():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    we, wexe = 2990.0, 52.0                                     # cm^-1, from the fundamental and first overtone
    G = lambda v: we * (v + 0.5) - wexe * (v + 0.5)**2
    D, a, re = 37260.0, 1.87, 1.275                             # Morse well in cm^-1 for the drawing
    turn = lambda E: (re - np.log(1 + np.sqrt(E / D)) / a, re - np.log(1 - np.sqrt(E / D)) / a)
    lines = [(1, TEAL, "fundamental"), (2, ORANGE, "first overtone"), (3, PURPLE, "second overtone")]
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.4), gridspec_kw={"width_ratios": [1, 1.25], "wspace": 0.18})
    r = np.linspace(0.95, 2.1, 400)
    ax.plot(r, D * (1 - np.exp(-a * (r - re)))**2, color="k", lw=2.2)
    for v in range(4):
        r1, r2 = turn(G(v))
        ax.hlines(G(v), r1, r2, color=GRAY, lw=1.4)
        ax.text(r2 + 0.03, G(v), rf"$v = {v}$", va="center", fontsize=11)
    for j, (v, col, name) in enumerate(lines):
        x = 1.17 + 0.09 * j
        ax.annotate("", xy=(x, G(v)), xytext=(x, G(0)),
                    arrowprops=dict(arrowstyle="-|>", color=col, lw=2.2, mutation_scale=15, shrinkA=0, shrinkB=0))
    ax.set_xlim(0.95, 2.1); ax.set_ylim(0, 11500); ax.set_xticks([])
    ax.set_ylabel(r"energy (cm$^{-1}$)", fontsize=11.5)
    ax.set_title("absorption from $v = 0$", loc="left", fontsize=12)
    inten = [1.0, 2.5e-2, 6e-4]                                 # schematic: each overtone tens of times weaker
    for (v, col, name), I in zip(lines, inten):
        w = G(v) - G(0)
        bx.vlines(w, 1e-4, I, color=col, lw=3.2)
        bx.text(w, I * 1.6, f"{name}\n{w:.0f} cm$^{{-1}}$", ha="center", va="bottom", fontsize=11, color=col)
    bx.set_yscale("log"); bx.set_ylim(1e-4, 20); bx.set_yticks([]); bx.minorticks_off()
    bx.set_xlim(2000, 9400)
    bx.set_xlabel(r"photon wavenumber (cm$^{-1}$)", fontsize=11.5)
    bx.set_ylabel("absorption (log scale)", fontsize=11.5)
    bx.set_title(r"not equally spaced: $2 \times 2886 = 5772$, not 5668", loc="left", fontsize=12)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.9, bottom=0.13)
    fig.savefig(f"{OUT}/hcl_overtones.png", dpi=200)
    print("wrote", f"{OUT}/hcl_overtones.png")
    return fig, None


# ------------------------------------------------------------ CO2: the symmetric stretch keeps the dipole at zero; the other two modes make it swing
@register
def co2_modes():
    from matplotlib.patches import Circle
    nf = 36
    ts = np.arange(nf) / nf
    re, d = 1.0, 0.13                                           # bond (drawing units) and the oxygen amplitude
    f = 2 * 16.0 / 12.0                                         # carbon moves this much more, to keep the center of mass
    # displacements (x, y) of O1, C, O2 per unit amplitude; charges O -1, C +2
    modes = [("symmetric stretch", 1388, 2, [(-1, 0), (0, 0), (1, 0)], False),
             ("antisymmetric stretch", 2349, 3, [(1, 0), (-f, 0), (1, 0)], True),
             ("bend (two of them)", 667, 1, [(0, -1), (0, f), (0, -1)], True)]
    q = np.array([-1.0, 2.0, -1.0])
    x0 = np.array([[-re, 0.0], [0.0, 0.0], [re, 0.0]])
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.6))
    parts = []
    for ax, (name, wn, cyc, disp, active) in zip(axes, modes):
        ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.0, 1.2); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(f"{name}\n{wn} cm$^{{-1}}$", fontsize=12.5, color=TEAL)
        ax.text(0, -0.98, "dipole swings: IR active" if active else "dipole stays 0: IR inactive",
                ha="center", va="bottom", fontsize=11.5, color=ORANGE if active else GRAY, weight="bold")
        (b1,) = ax.plot([], [], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
        (b2,) = ax.plot([], [], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
        atoms = [Circle((0, 0), r, fc=c, ec="k", lw=1, zorder=3) for r, c in ((0.25, CARDINAL), (0.22, "#495057"), (0.25, CARDINAL))]
        for c in atoms:
            ax.add_patch(c)
        arr = ax.annotate("", xy=(0, 0.62), xytext=(0, 0.62),
                          arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.6, mutation_scale=16, shrinkA=0, shrinkB=0))
        parts.append((np.array(disp, float), cyc, b1, b2, atoms, arr))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.84, bottom=0.02, wspace=0.05)

    def update(i):
        for disp, cyc, b1, b2, atoms, arr in parts:
            pos = x0 + d * np.sin(2 * np.pi * cyc * ts[i]) * disp
            for c, p in zip(atoms, pos):
                c.center = tuple(p)
            b1.set_data(pos[:2, 0], pos[:2, 1]); b2.set_data(pos[1:, 0], pos[1:, 1])
            mu = (q[:, None] * pos).sum(axis=0) * 0.5           # the dipole, scaled for the drawing
            base = np.array([0.0, 0.62])                        # drawn from a point above the carbon
            arr.xy = tuple(base + mu); arr.set_position(tuple(base))

    ani = FuncAnimation(fig, update, frames=nf, interval=80, blit=False)
    return fig, ani


# ------------------------------------------------------------ group frequencies: where common bonds absorb (still)
@register
def group_frequencies():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False})
    bands = [("O-H", 3200, 3600, TEAL), ("N-H", 3300, 3500, TEAL), ("C-H", 2850, 3100, TEAL),
             (r"C$\equiv$N", 2210, 2260, PURPLE), (r"C$\equiv$C", 2100, 2260, PURPLE),
             ("C=O", 1650, 1780, ORANGE), ("C=C", 1620, 1680, ORANGE), ("C-O", 1000, 1300, GRAY)]
    groups = [(0, 2, "stretches of a bond to H:\nthe light H atom", TEAL), (3, 4, "triple bonds:\nthe stiffest", PURPLE),
              (5, 6, "double bonds", ORANGE), (7, 7, "single bonds", GRAY)]
    fig, ax = plt.subplots(figsize=(9.6, 4.2))
    ax.axvspan(1500, 400, color=GRAY, alpha=0.1, lw=0)
    ax.text(950, -0.75, "fingerprint region:\nsingle bonds and bends,\nunique to each molecule", ha="center", va="top",
            fontsize=10.5, color=GRAY)
    n = len(bands)
    for j, (name, lo, hi, col) in enumerate(bands):
        y = n - 1 - j
        ax.barh(y, hi - lo, left=lo, height=0.62, color=col, alpha=0.85)
        ax.text(lo - 40, y, name, va="center", ha="left", fontsize=12, color="k")
    for j0, j1, txt, col in groups:
        ax.text(4520, n - 1 - (j0 + j1) / 2, txt, ha="left", va="center", fontsize=10.5, color=col)
    ax.set_xlim(4550, 400); ax.set_ylim(-2.9, n - 0.4); ax.set_yticks([])
    ax.set_xticks([4000, 3500, 3000, 2500, 2000, 1500, 1000, 500])
    ax.set_xlabel(r"wavenumber (cm$^{-1}$)", fontsize=11.5)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.97, bottom=0.13)
    fig.savefig(f"{OUT}/group_frequencies.png", dpi=200)
    print("wrote", f"{OUT}/group_frequencies.png")
    return fig, None



# ------------------------------------------------------------ coupled atoms, independent modes: CO2 stretches atom by atom vs mode by mode (still)
@register
def co2_decoupling():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    mO, mC, k = 16.0, 12.0, 1.0
    m = np.array([mO, mC, mO])
    K = k * np.array([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])
    w2, u = np.linalg.eigh(K / np.sqrt(np.outer(m, m)))
    w = np.sqrt(np.clip(w2, 0, None))
    u = u * np.sign(u[2])                                        # right oxygen moves +1 in every mode
    x0 = np.array([-0.3, 0.0, 0.0])                             # pull the left oxygen outward and let go
    q0 = np.sqrt(m) * x0
    Q0 = u.T @ q0
    Q0[0] = 0.0                                                 # drop the translation: the center of mass stays put
    t = np.linspace(0, 4, 800)                                  # time in periods of the symmetric stretch
    ph = 2 * np.pi * t * w[None, 1:].T / w[1]                   # phases of the two vibrations
    Q = Q0[1:, None] * np.cos(ph)                               # each normal coordinate: one cosine
    x = (u[:, 1:] @ Q) / np.sqrt(m)[:, None]                    # back to atom displacements
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.6, 4.8), sharex=True, gridspec_kw={"hspace": 0.45})
    for xi, lab, col, ls in ((x[0], "left O", CARDINAL, "-"), (x[1], "C", "#495057", "-"), (x[2], "right O", CARDINAL, "--")):
        ax.plot(t, xi, color=col, lw=2, ls=ls, label=lab)
    ax.set_title("atom by atom: every displacement mixes two frequencies, and energy flows between the atoms",
                 loc="left", fontsize=12)
    ax.legend(loc="upper right", frameon=False, fontsize=11, ncol=3, bbox_to_anchor=(1.0, 1.02))
    ax.set_ylabel("displacement", fontsize=11.5)
    bx.plot(t, Q[0], color=TEAL, lw=2.4, label=r"$Q_{\mathrm{sym}}$: symmetric stretch")
    bx.plot(t, Q[1], color=ORANGE, lw=2.4, label=r"$Q_{\mathrm{anti}}$: antisymmetric stretch")
    bx.set_title(r"mode by mode, $Q_k = \mathbf{u}_k\cdot\mathbf{q}$: each is a single cosine, $\ddot{Q}_k = -\omega_k^2 Q_k$",
                 loc="left", fontsize=12)
    bx.legend(loc="upper right", frameon=False, fontsize=11, ncol=2, bbox_to_anchor=(1.0, 1.02))
    bx.set_ylabel("normal coordinate", fontsize=11.5)
    bx.set_xlabel("time (periods of the symmetric stretch)", fontsize=11.5)
    for a in (ax, bx):
        a.axhline(0, color=GRAY, lw=0.8); a.set_yticks([]); a.set_xlim(0, 4)
        lo, hi = a.get_ylim(); a.set_ylim(lo, hi + 0.35 * (hi - lo))
    fig.subplots_adjust(left=0.06, right=0.99, top=0.93, bottom=0.11)
    fig.savefig(f"{OUT}/co2_decoupling.png", dpi=200)
    print("wrote", f"{OUT}/co2_decoupling.png")
    return fig, None


# ============================================================ lecture 4.4: angular momentum
# Lecture 4.4 (page ch04/04, deck slides/ch04/04) uses every figure in this section. Rotation keeps the chapter's
# PURPLE (angular momentum vectors, ring levels); a wavefunction is TEAL where positive and ORANGE where negative.

# ------------------------------------------------------------ the model system: a rigid dumbbell (CO) turning about its center of mass = one bead mu on a circle (still)
@register
def dumbbell_reduce():
    from matplotlib.patches import Circle, FancyArrowPatch
    mC, mO, R = 12.0, 16.0, 1.9
    rC, rO = mO / (mC + mO) * R, mC / (mC + mO) * R            # distances from the center of mass, m_C r_C = m_O r_O
    t = np.linspace(0, 2 * np.pi, 300)
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.0))
    for a_ in (ax, bx):
        a_.set_xlim(-2.5, 2.5); a_.set_ylim(-2.3, 2.4); a_.set_aspect("equal"); a_.axis("off")
        a_.add_patch(FancyArrowPatch((2.2 * np.cos(np.radians(25)), 2.2 * np.sin(np.radians(25))),
                                     (2.2 * np.cos(np.radians(70)), 2.2 * np.sin(np.radians(70))),
                                     connectionstyle="arc3,rad=0.2", arrowstyle="-|>", mutation_scale=16, color=PURPLE, lw=1.8))
        a_.text(1.9, 1.78, r"$\omega$", fontsize=15, color=PURPLE)
    ax.plot(rC * np.cos(t), rC * np.sin(t), color="#495057", lw=1, ls=":")
    ax.plot(rO * np.cos(t), rO * np.sin(t), color=CARDINAL, lw=1, ls=":")
    ax.plot([-rC, rO], [0, 0], color="#adb5bd", lw=6, solid_capstyle="round", zorder=2)
    ax.add_patch(Circle((-rC, 0), 0.27, fc="#495057", ec="k", lw=1, zorder=3))
    ax.add_patch(Circle((rO, 0), 0.31, fc=CARDINAL, ec="k", lw=1, zorder=3))
    ax.text(-rC, 0, "C", color="white", ha="center", va="center", fontsize=12, weight="bold", zorder=4)
    ax.text(rO, 0, "O", color="white", ha="center", va="center", fontsize=12, weight="bold", zorder=4)
    ax.plot([0], [0], "+", color="k", ms=13, mew=2.2, zorder=5)
    ax.annotate("", xy=(-rC, -0.5), xytext=(0, -0.5), arrowprops=dict(arrowstyle="<->", color="#495057", lw=1.2))
    ax.annotate("", xy=(rO, -0.5), xytext=(0, -0.5), arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.2))
    ax.text(-rC / 2, -0.62, "$r_C$", ha="center", va="top", fontsize=13, color="#495057")
    ax.text(rO / 2, -0.62, "$r_O$", ha="center", va="top", fontsize=13, color=CARDINAL)
    ax.text(0, -2.1, r"$I = m_C r_C^2 + m_O r_O^2$", ha="center", fontsize=14)
    bx.plot(R * np.cos(t), R * np.sin(t), color=PURPLE, lw=1.2, ls=":")
    bx.plot([0, R * np.cos(np.radians(30))], [0, R * np.sin(np.radians(30))], color="k", lw=1.6)
    bx.add_patch(Circle((R * np.cos(np.radians(30)), R * np.sin(np.radians(30))), 0.27, fc=PURPLE, ec="k", lw=1, zorder=3))
    bx.text(R * np.cos(np.radians(30)), R * np.sin(np.radians(30)), r"$\mu$", color="white", ha="center", va="center",
            fontsize=14, zorder=4)
    bx.plot([0], [0], "+", color="k", ms=13, mew=2.2)
    bx.text(0.55 * np.cos(np.radians(30)) - 0.05, 0.55 * np.sin(np.radians(30)) + 0.12, "$r$", fontsize=14,
            ha="right", va="bottom")
    bx.text(0, -2.1, r"$I = \mu r^2$ with $\mu = m_Cm_O/(m_C + m_O)$, $r = r_C + r_O$", ha="center", fontsize=13.5)
    fig.text(0.5, 0.53, "=", ha="center", va="center", fontsize=30, color=GRAY)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.02, wspace=0.1)
    fig.savefig(f"{OUT}/dumbbell_reduce.png", dpi=200)
    print("wrote", f"{OUT}/dumbbell_reduce.png")
    return fig, None


# ------------------------------------------------------------ angular momentum is a vector product: r and p in the plane, L = r x p along the axis (still)
@register
def angular_momentum_vector():
    from matplotlib.patches import Circle, FancyArrowPatch
    fig, ax = plt.subplots(figsize=(6.0, 4.4))
    k = 0.32                                                    # the circle seen from above at an angle: an ellipse
    t = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(t), k * np.sin(t), color=GRAY, lw=1.2, ls=":")
    tp = np.radians(-38)
    P = np.array([np.cos(tp), k * np.sin(tp)])
    d = np.array([-np.sin(tp), k * np.cos(tp)]); d /= np.linalg.norm(d)
    ax.add_patch(FancyArrowPatch((0, 0), P, arrowstyle="-|>", mutation_scale=16, color="k", lw=2, zorder=4))
    ax.text(0.45 * P[0] + 0.02, 0.45 * P[1] - 0.1, r"$\vec{r}$", fontsize=18, va="top")
    ax.add_patch(FancyArrowPatch(P, P + 0.6 * d, arrowstyle="-|>", mutation_scale=18, color=ORANGE, lw=2.6, zorder=4))
    ax.text(*(P + 0.62 * d + np.array([0.04, -0.02])), r"$\vec{p} = \mu\vec{v}$", fontsize=17, color=ORANGE, va="center")
    ax.add_patch(Circle(P, 0.06, fc=PURPLE, ec="k", lw=1, zorder=5))
    ax.add_patch(FancyArrowPatch((0, 0), (0, 1.45), arrowstyle="-|>", mutation_scale=22, color=PURPLE, lw=3.4, zorder=4))
    ax.text(0.09, 1.38, r"$\vec{L} = \vec{r}\times\vec{p}$", fontsize=18, color=PURPLE, va="center")
    u = np.linspace(np.radians(200), np.radians(500), 120)     # the right-hand curl, counterclockwise seen from above
    ax.plot(0.26 * np.cos(u), 0.95 + 0.08 * np.sin(u), color=GRAY, lw=1.5)
    ax.add_patch(FancyArrowPatch((0.26 * np.cos(u[-6]), 0.95 + 0.08 * np.sin(u[-6])), (0.26 * np.cos(u[-1]), 0.95 + 0.08 * np.sin(u[-1])),
                                 arrowstyle="-|>", mutation_scale=12, color=GRAY, lw=1.5))
    ax.text(-0.33, 0.95, "right\nhand", fontsize=12, color=GRAY, ha="right", va="center")
    ax.set_xlim(-1.15, 2.0); ax.set_ylim(-0.48, 1.58); ax.set_aspect("equal"); ax.axis("off")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(f"{OUT}/angular_momentum_vector.png", dpi=200)
    print("wrote", f"{OUT}/angular_momentum_vector.png")
    return fig, None


# ------------------------------------------------------------ the spinning skater: pull the masses in, I drops, omega rises, L = I omega stays
@register
def skater_spin():
    from matplotlib.patches import Circle
    nf = 44
    I0, mm, rout, rin = 0.12, 0.5, 1.0, 0.36                  # the body, each hand weight, arm lengths out and in
    s = 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(nf) / nf)    # 0 -> 1 -> 0: arms out, in, out again
    r = rout + (rin - rout) * s
    I = I0 + 2 * mm * r ** 2
    Lc = I[0] * 0.17                                           # fixed angular momentum; arms out turn 0.17 rad per frame
    w = Lc / I                                                 # rad per frame
    ang = np.cumsum(w) - w[0]
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.2), gridspec_kw={"width_ratios": [1, 1.15], "wspace": 0.1})
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Circle((0, 0), 0.22, fc="#adb5bd", ec="k", lw=1, zorder=3))
    (arms,) = ax.plot([], [], color="#495057", lw=5, solid_capstyle="round", zorder=2)
    hands = [ax.add_patch(Circle((0, 0), 0.11, fc=CARDINAL, ec="k", lw=1, zorder=4)) for _ in range(2)]
    trails = [ax.plot([], [], color=CARDINAL, lw=4, alpha=0.3, solid_capstyle="round")[0] for _ in range(2)]
    names = ["moment of inertia $I$", r"angular velocity $\omega$", r"angular momentum $L = I\omega$"]
    cols = [ORANGE, TEAL, PURPLE]
    vals = [I / I[0], w / w[0], I * w / (I[0] * w[0])]
    bars = bx.barh(range(3)[::-1], [v[0] for v in vals], color=cols, height=0.42)
    texts = [bx.text(0, 2 - j, "", va="center", fontsize=12.5, color=cols[j]) for j in range(3)]
    for j, nm in enumerate(names):
        bx.text(0.02, 2 - j + 0.36, nm, ha="left", va="bottom", fontsize=13, color=cols[j])
    bx.axvline(1, color=GRAY, lw=0.8, ls=":")
    bx.set_xlim(0, 5.6); bx.set_ylim(-0.45, 2.95); bx.set_yticks([]); bx.set_xticks([0, 1, 2, 3, 4, 5])
    for sp in ("top", "right", "left"):
        bx.spines[sp].set_visible(False)
    bx.set_xlabel("relative to the arms-out value", fontsize=11.5)
    fig.subplots_adjust(left=0.01, right=0.98, top=0.98, bottom=0.14)

    def update(i):
        c, sn = np.cos(ang[i]), np.sin(ang[i])
        arms.set_data([-r[i] * c, r[i] * c], [-r[i] * sn, r[i] * sn])
        for k_, sg in enumerate((1, -1)):
            hands[k_].center = (sg * r[i] * c, sg * r[i] * sn)
            sweep = np.linspace(ang[i] - 1.6 * w[i], ang[i], 30)   # the angle swept just before: a streak as long as the speed
            trails[k_].set_data(sg * r[i] * np.cos(sweep), sg * r[i] * np.sin(sweep))
        for j, (bar, v) in enumerate(zip(bars, vals)):
            bar.set_width(v[i])
            texts[j].set_position((v[i] + 0.08, 2 - j)); texts[j].set_text(f"{v[i]:.2f}")

    ani = FuncAnimation(fig, update, frames=nf, interval=110, blit=False)
    return fig, ani


skater_spin.fps = 10


# ------------------------------------------------------------ a wave on a ring must join up: e^{im phi} for whole m, and a misfit (still)
@register
def ring_waves():
    phi = np.linspace(0, 2 * np.pi, 721)
    cases = [(0, "constant"), (1, "one wavelength"), (2, "two wavelengths"), (3, "three wavelengths"),
             (2.5, "the ends miss")]
    fig, axes = plt.subplots(1, 5, figsize=(9.6, 2.35))
    for ax, (m, note) in zip(axes, cases):
        col = TEAL if float(m).is_integer() else CARDINAL
        ax.plot(np.cos(phi), np.sin(phi), color=GRAY, lw=1.2, ls=":")
        r = 1 + 0.3 * np.cos(m * phi)                           # the real part of e^{im phi}, drawn out from the ring
        ax.plot(r * np.cos(phi), r * np.sin(phi), color=col, lw=2.6)
        ax.plot([r[0]], [0], "o", color=col, ms=6.5, zorder=4)  # the start, phi = 0
        if col == CARDINAL:                                     # after one turn the wave is back at phi = 0, but at r = 0.7
            ax.plot([r[-1]], [0], "o", color=CARDINAL, ms=6.5, mfc="white", mew=2, zorder=4)
            ax.annotate("", xy=(r[0] - 0.03, -0.32), xytext=(r[-1] + 0.03, -0.32),
                        arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.4, shrinkA=0, shrinkB=0))
        ax.set_xlim(-1.42, 1.42); ax.set_ylim(-1.42, 1.42); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(rf"$m = {m:g}$", fontsize=14, color=col)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.86, bottom=0.01, wspace=0.06)
    fig.savefig(f"{OUT}/ring_waves.png", dpi=200)
    print("wrote", f"{OUT}/ring_waves.png")
    return fig, None


# ------------------------------------------------------------ glue the ends of a box: a ring of radius R and the box of length 2 pi R (still)
@register
def ring_ladder():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    b0, b1 = 0.6, 2.9                                           # box column
    r0, r1 = 6.3, 9.0                                           # ring column: +m on the left half, -m on the right
    rc = 0.5 * (r0 + r1)
    for n in range(1, 5):                                       # box: E_n = n^2/4 in units of hbar^2/2I
        E, even = n * n / 4, n % 2 == 0
        ax.hlines(E, b0, b1, color=GRAY, lw=2.6 if even else 1.6, ls="-" if even else (0, (4, 3)),
                  alpha=1 if even else 0.65)
        ax.text(b0 - 0.12, E, rf"$n = {n}$", ha="right", va="center", fontsize=12, color=GRAY)
        if even:                                                # the same wavelength fits around the ring
            ax.plot([b1 + 0.1, r0 - 0.1], [E, E], color=PURPLE, lw=1.1, ls=":", alpha=0.7)
    for m in range(3):                                          # ring: E_m = m^2 in units of hbar^2/2I
        E = m * m
        if m == 0:
            ax.hlines(E, r0, r1, color=PURPLE, lw=2.8)
            ax.text(r1 + 0.12, E, r"$m = 0$", va="center", fontsize=12, color=PURPLE)
        else:
            ax.hlines(E, r0, rc - 0.1, color=PURPLE, lw=2.8)
            ax.hlines(E, rc + 0.1, r1, color=PURPLE, lw=2.8)
            ax.text(r1 + 0.12, E, rf"$m = \pm {m}$", va="center", fontsize=12, color=PURPLE)
            ax.text(0.5 * (r0 + rc), E + 0.11, rf"$+{m}$ ↺", ha="center", va="bottom", fontsize=11.5, color=PURPLE)
            ax.text(0.5 * (rc + r1), E + 0.11, rf"$-{m}$ ↻", ha="center", va="bottom", fontsize=11.5, color=PURPLE)
    ax.text(0.5 * (b0 + b1), 4.65, r"box of length $2\pi r$", ha="center", fontsize=13, color=GRAY, weight="bold")
    ax.text(0.5 * (r0 + r1), 4.65, r"ring of radius $r$", ha="center", fontsize=13, color=PURPLE, weight="bold")
    ax.set_xlim(-0.6, 10.4); ax.set_ylim(-0.2, 5.0)
    ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
    ax.set_yticks([0, 0.25, 1, 2.25, 4]); ax.set_yticklabels(["0", "1/4", "1", "9/4", "4"]); ax.tick_params(labelsize=11)
    ax.spines["left"].set_bounds(0, 4.25)
    ax.set_ylabel(r"energy (units of $\hbar^2/2I$)", fontsize=12)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.98, bottom=0.03)
    fig.savefig(f"{OUT}/ring_ladder.png", dpi=200)
    print("wrote", f"{OUT}/ring_ladder.png")
    return fig, None


# ------------------------------------------------------------ sharp L_z runs around the ring with an even density; the +m, -m mix stands still
@register
def ring_flow():
    from matplotlib.patches import FancyArrowPatch, Patch
    from matplotlib.lines import Line2D
    nf = 36
    phi = np.linspace(0, 2 * np.pi, 361)
    cases = [(2, r"$e^{+2i\phi}$"), (-2, r"$e^{-2i\phi}$"), (0, r"$2\cos 2\phi$")]
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.4), gridspec_kw={"wspace": 0.32})
    parts = []
    for ax, (m, title) in zip(axes, cases):
        ax.set_xlim(-1.62, 1.62); ax.set_ylim(-1.62, 1.62); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(title, fontsize=17)
        dens = np.ones_like(phi) if m else 2 * np.cos(2 * phi) ** 2     # |Psi|^2 in units of its average
        band = 0.1 * dens
        ax.fill(np.r_[(1 + band) * np.cos(phi), ((1 - band) * np.cos(phi))[::-1]],
                np.r_[(1 + band) * np.sin(phi), ((1 - band) * np.sin(phi))[::-1]], color=TEAL, alpha=0.25, lw=0)
        ax.plot(np.cos(phi), np.sin(phi), color=GRAY, lw=0.8, ls=":")
        (wave,) = ax.plot([], [], color=TEAL, lw=2.4)
        if m:
            a0, a1 = np.radians(55), np.radians(125)
            if m < 0:
                a0, a1 = a1, a0
            ax.add_patch(FancyArrowPatch((1.45 * np.cos(a0), 1.45 * np.sin(a0)), (1.45 * np.cos(a1), 1.45 * np.sin(a1)),
                                         connectionstyle=f"arc3,rad={0.22 if m > 0 else -0.22}", arrowstyle="-|>",
                                         mutation_scale=18, color=PURPLE, lw=2))
        parts.append((m, wave))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.13)
    fig.legend(handles=[Line2D([0], [0], color=TEAL, lw=2.4, label=r"real part of $\Psi$"),
                        Patch(facecolor=TEAL, alpha=0.25, label=r"probability density $|\Psi|^2$")],
               loc="lower center", ncol=2, frameon=False, fontsize=13, bbox_to_anchor=(0.5, 0.0), columnspacing=3)
    for k, sign in ((0, "+"), (1, "=")):                        # running + running = standing
        x = 0.5 * (axes[k].get_position().x1 + axes[k + 1].get_position().x0)
        fig.text(x, 0.45, sign, ha="center", va="center", fontsize=34, color=GRAY)

    def update(i):
        wt = 2 * np.pi * i / nf                                 # E t / hbar over one period of the phase
        for m, wave in parts:
            if m:                                               # the real part of e^{i(m phi - w t)}
                re, amp = np.cos(m * phi - wt), 0.25
            else:                                               # the sum of the two running waves
                re, amp = np.cos(2 * phi - wt) + np.cos(-2 * phi - wt), 0.25
            r = 1 + amp * re
            wave.set_data(r * np.cos(phi), r * np.sin(phi))

    ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
    return fig, ani


ring_flow.fps = 12


# ------------------------------------------------------------ turns about x and y do not commute: one book, two orders, two different ends
@register
def rotation_order():
    from matplotlib.patches import Polygon
    from matplotlib.colors import to_rgb
    nf = 42
    el, az = np.radians(24), np.radians(35)
    cam = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])     # unit vector toward the viewer
    ex = np.array([-np.sin(az), np.cos(az), 0.0])                                     # screen right
    ey = np.cross(cam, ex)                                                            # screen up
    to2d = lambda p: np.c_[p @ ex, p @ ey]
    Rx = lambda a: np.array([[1, 0, 0], [0, np.cos(a), -np.sin(a)], [0, np.sin(a), np.cos(a)]])
    Ry = lambda a: np.array([[np.cos(a), 0, np.sin(a)], [0, 1, 0], [-np.sin(a), 0, np.cos(a)]])
    a, b, c = 0.5, 0.72, 0.13                                   # half sizes of the book: width, height, thickness
    corners = np.array([[sx * a, sy * b, sz * c] for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)])
    PAGES = "#f3ead8"
    faces = [((0, 0, 1), [1, 5, 7, 3], TEAL), ((0, 0, -1), [0, 2, 6, 4], "#adb5bd"), ((-1, 0, 0), [0, 1, 3, 2], PURPLE),
             ((1, 0, 0), [4, 6, 7, 5], PAGES), ((0, 1, 0), [2, 3, 7, 6], PAGES), ((0, -1, 0), [0, 4, 5, 1], PAGES)]
    arrow = np.array([[-0.07, -0.45], [0.07, -0.45], [0.07, 0.16], [0.2, 0.16], [0, 0.5], [-0.2, 0.16], [-0.07, 0.16]])
    arrow = np.c_[arrow, np.full(len(arrow), c + 0.004)]        # an arrow printed on the cover, pointing to the top edge
    ease = lambda s: np.clip(s, 0, 1) ** 2 * (3 - 2 * np.clip(s, 0, 1))
    s1 = lambda k: ease((k - 3) / 12)                           # first quarter turn over frames 4 to 15
    s2 = lambda k: ease((k - 19) / 12)                          # second quarter turn over frames 20 to 31
    orders = [("x", "y", lambda k: Ry(np.pi / 2 * s2(k)) @ Rx(-np.pi / 2 * s1(k))),
              ("y", "x", lambda k: Rx(-np.pi / 2 * s2(k)) @ Ry(np.pi / 2 * s1(k)))]
    unit = {"x": np.array([1.0, 0, 0]), "y": np.array([0, 1.0, 0]), "z": np.array([0, 0, 1.0])}
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.1))
    parts = []
    for ax, (first, second, R) in zip(axes, orders):
        ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.18, 1.12); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(rf"turn about ${first}$, then about ${second}$", fontsize=14)
        polys = [ax.add_patch(Polygon(np.zeros((4, 2)), closed=True, fc=col, ec="#495057", lw=1.2, zorder=2))
                 for _, _, col in faces]
        mark = ax.add_patch(Polygon(np.zeros((7, 2)), closed=True, fc="white", ec="none", alpha=0.95, zorder=3))
        (axis_line,) = ax.plot([], [], color=CARDINAL, lw=1.8, ls=(0, (5, 3)), zorder=4)
        axis_lab = ax.text(0, 0, "", color=CARDINAL, fontsize=15, weight="bold", ha="center", va="center", zorder=4)
        o = np.array([-1.05, -0.95])                            # a fixed triad of axes in the corner
        triad = {}
        for name, v in unit.items():
            d = 0.28 * to2d(v[None])[0]
            ln = ax.annotate("", xy=o + d, xytext=o, arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.6,
                                                                     mutation_scale=12, shrinkA=0, shrinkB=0))
            tx = ax.text(*(o + 1.38 * d), name, color=GRAY, fontsize=12, ha="center", va="center")
            triad[name] = (ln, tx)
        step = None
        parts.append((first, second, R, polys, mark, axis_line, axis_lab, triad, step))
    fig.subplots_adjust(left=0.01, right=0.99, top=0.91, bottom=0.01, wspace=0.04)

    def update(k):
        for first, second, R, polys, mark, axis_line, axis_lab, triad, step in parts:
            M = R(k)
            pts = corners @ M.T
            for poly, (n, idx, col) in zip(polys, faces):
                nv = M @ np.array(n, float)
                poly.set_visible(nv @ cam > 1e-6)              # a convex box: draw only the faces turned to us
                poly.set_xy(to2d(pts[idx]))
                if poly.get_visible():
                    rgb = np.array(to_rgb(col))
                    poly.set_facecolor(rgb * (0.78 + 0.22 * (nv @ cam)))
            cover = M @ np.array([0, 0, 1.0])
            mark.set_visible(cover @ cam > 1e-6)
            mark.set_xy(to2d(arrow @ M.T))
            now = None if k >= 32 else (first if k < 18 else second)
            for name, (ln, tx) in triad.items():
                on = name == now
                ln.arrow_patch.set_color(CARDINAL if on else GRAY)
                tx.set_color(CARDINAL if on else GRAY); tx.set_fontweight("bold" if on else "normal")
            if now is None:
                axis_line.set_data([], []); axis_lab.set_text("")
            else:
                ends = to2d(np.array([-1.08, 1.08])[:, None] * unit[now])
                axis_line.set_data(ends[:, 0], ends[:, 1])
                axis_lab.set_position(1.12 * ends[1]); axis_lab.set_text(now)

    ani = FuncAnimation(fig, update, frames=nf, interval=85, blit=False)
    return fig, ani


rotation_order.fps = 12


# ------------------------------------------------------------ the vector model: fixed length sqrt(l(l+1)), 2l+1 heights m, the direction around z unknown (still)
@register
def vector_cones():
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.7), gridspec_kw={"width_ratios": [1, 1.32], "wspace": 0.02})
    t = np.linspace(0, 2 * np.pi, 300)
    LIGHT = "#cdb9e3"
    lz = {-2: r"-2\hbar", -1: r"-\hbar", 0: "0", 1: r"+\hbar", 2: r"+2\hbar"}
    for ax, l in zip(axes, (1, 2)):
        R = np.sqrt(l * (l + 1))                                # |L| in units of hbar
        ax.plot(R * np.cos(t), R * np.sin(t), color=GRAY, lw=1, ls=":")
        ax.annotate("", xy=(0, R + 0.62), xytext=(0, -R - 0.35),
                    arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=14, shrinkA=0, shrinkB=0))
        ax.text(0.14, R + 0.55, "$z$", fontsize=14, va="center")
        for m in range(-l, l + 1):
            rm = np.sqrt(R * R - m * m)                         # radius of the cone's rim: the part of L off the z axis
            ax.plot(rm * np.cos(t), m + 0.2 * rm * np.sin(t), color=LIGHT, lw=1.6)
            ax.plot([-rm, 0, rm], [m, 0, m], color=LIGHT, lw=1.2)
            tip = (rm * np.cos(np.radians(-42)), m + 0.2 * rm * np.sin(np.radians(-42)))
            ax.annotate("", xy=tip, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.2,
                                                                  mutation_scale=15, shrinkA=0, shrinkB=0))
            ax.plot([0], [m], "o", color=PURPLE, ms=5, zorder=5)
            ax.plot([0.05, R + 0.25], [m, m], color=GRAY, lw=0.8, ls=(0, (2, 3)))
            ax.text(R + 0.32, m, rf"$m = {m:+d}$: $L_z = {lz[m]}$" if m else r"$m = 0$: $L_z = 0$", va="center",
                    fontsize=12, color=PURPLE)
        root = "2" if l == 1 else "6"
        ax.set_title(rf"$l = {l}$", fontsize=15)
        ax.set_xlim(-R - 0.25, R + 2.75 if l == 2 else R + 2.55); ax.set_ylim(-R - 0.5, R + 0.75)
        ax.set_aspect("equal"); ax.axis("off")
    fig.subplots_adjust(left=0.0, right=0.99, top=0.92, bottom=0.01)
    fig.savefig(f"{OUT}/vector_cones.png", dpi=200)
    print("wrote", f"{OUT}/vector_cones.png")
    return fig, None


# ------------------------------------------------------------ spherical harmonics on the globe: sign of the real part and the l nodal lines (still)
@register
def harmonic_globes():
    from scipy.special import sph_harm_y
    from matplotlib.colors import to_rgb
    S = 261
    u = np.linspace(-1, 1, S)
    U, V = np.meshgrid(u, u[::-1])                              # screen coordinates, V upward
    inside = U ** 2 + V ** 2 < 1
    W = np.sqrt(np.clip(1 - U ** 2 - V ** 2, 0, None))          # toward the viewer
    el, az = np.radians(22), np.radians(-55)                    # the north pole tipped 22 degrees toward us
    cam = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])
    ex = np.array([-np.sin(az), np.cos(az), 0.0])
    ey = np.cross(cam, ex)
    P = U[..., None] * ex + V[..., None] * ey + W[..., None] * cam      # the point of the sphere behind each pixel
    TH, PH = np.arccos(np.clip(P[..., 2], -1, 1)), np.arctan2(P[..., 1], P[..., 0])
    light = np.array([-0.45, 0.55, 0.7]) / np.linalg.norm([-0.45, 0.55, 0.7])
    shade = 0.5 + 0.5 * np.clip(U * light[0] + V * light[1] + W * light[2], 0, 1)
    white, pos, neg = np.ones(3), np.array(to_rgb(TEAL)), np.array(to_rgb(ORANGE))
    th1 = np.linspace(0, np.pi, 721)
    fig, axes = plt.subplots(4, 4, figsize=(9.6, 7.5))
    for l in range(4):
        for m in range(4):
            ax = axes[l, m]
            ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.15, 1.35); ax.set_aspect("equal"); ax.axis("off")
            if m > l:
                continue
            top = np.abs(sph_harm_y(l, m, th1, 0 * th1).real).max()          # the largest |Re Y| on the sphere
            s = sph_harm_y(l, m, TH, PH).real / top                          # -1 .. 1
            rgb = np.where(s[..., None] > 0, white + s[..., None] * (pos - white), white - s[..., None] * (neg - white))
            rgb = np.clip(rgb, 0, 1)
            img = np.dstack([rgb * shade[..., None], inside.astype(float)])
            ax.imshow(img, extent=(-1, 1, -1, 1), interpolation="bilinear", zorder=1)
            if l > 0:
                ax.contour(U, V, np.ma.masked_where(U ** 2 + V ** 2 > 0.985, s), levels=[0], colors="#212529",
                           linewidths=1.4, zorder=2)
            ax.add_patch(plt.Circle((0, 0), 1, fill=False, ec="#868e96", lw=0.8, zorder=3))
            ax.plot([0, 0], [ey[2], ey[2] + 0.3], color="#495057", lw=1.4, zorder=3)     # the z axis leaving the north pole
            ax.text(0.08, ey[2] + 0.28, "$z$", fontsize=10, color="#495057", va="center")
            ax.text(0, -1.12, f"{l - m} + {m} = {l}", ha="center", va="top", fontsize=10.5, color=GRAY)
    for l in range(4):
        axes[l, 0].text(-1.45, 0.1, rf"$l = {l}$", ha="right", va="center", fontsize=14)
    for m in range(4):
        axes[0, m].set_title(rf"$m = {m}$", fontsize=14)
    fig.subplots_adjust(left=0.07, right=0.995, top=0.955, bottom=0.035, wspace=0.0, hspace=0.12)
    fig.savefig(f"{OUT}/harmonic_globes.png", dpi=200)
    print("wrote", f"{OUT}/harmonic_globes.png")
    return fig, None


# ------------------------------------------------------------ every ladder the commutators allow: 2l + 1 rungs; whole l for rotation, half-integer for spin (still)
@register
def m_ladders():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    ladders = [(0, 0.0), (1, 1.5), (2, 3.15), (0.5, 6.7), (1.5, 8.15)]
    names = {0: "0", 1: "1", 2: "2", 0.5: "1/2", 1.5: "3/2"}
    for l, x in ladders:
        whole = float(l).is_integer()
        ms = np.arange(-l, l + 0.01, 1.0)
        ax.hlines(ms, x - 0.42, x + 0.42, color="k" if whole else GRAY, lw=2.8, ls="-" if whole else (0, (3, 2)))
        ax.text(x, -2.75, rf"$l = {names[l]}$", ha="center", va="top", fontsize=13)
        ax.text(x, -3.2, f"{len(ms)} rung" + ("s" if len(ms) > 1 else ""), ha="center", va="top", fontsize=11, color=GRAY)
    x2 = 3.15
    for m in range(-2, 2):
        ax.annotate("", xy=(x2 + 0.6, m + 0.92), xytext=(x2 + 0.6, m + 0.08),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2, mutation_scale=15, shrinkA=0, shrinkB=0))
        ax.annotate("", xy=(x2 + 0.95, m + 0.08), xytext=(x2 + 0.95, m + 0.92),
                    arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2, mutation_scale=15, shrinkA=0, shrinkB=0))
    ax.text(-0.8, 2.45, r"$\hat{L}_+$: up one rung", ha="left", va="center", fontsize=12, color=ORANGE)
    ax.text(-0.8, 1.95, r"$\hat{L}_-$: down one rung", ha="left", va="center", fontsize=12, color=PURPLE)
    ax.plot([x2 + 0.6], [2.38], "x", color=CARDINAL, ms=10, mew=2.4)
    ax.plot([x2 + 0.95], [-2.38], "x", color=CARDINAL, ms=10, mew=2.4)
    ax.text(x2 + 0.8, 2.38, r"$\hat{L}_+Y_2^2 = 0$", ha="left", va="center", fontsize=11.5, color=CARDINAL)
    ax.text(x2 + 1.15, -2.38, r"$\hat{L}_-Y_2^{-2} = 0$", ha="left", va="center", fontsize=11.5, color=CARDINAL)
    ax.axvline(5.55, color=GRAY, lw=1, ls=":")
    ax.text(1.55, 3.15, "whole $l$: rotation in space", ha="center", fontsize=13, color=PURPLE)
    ax.text(7.45, 3.15, "half-integer $l$: spin", ha="center", fontsize=13, color=ORANGE)
    ax.set_xlim(-0.9, 9.0); ax.set_ylim(-3.6, 3.55)
    ax.set_yticks(np.arange(-2, 2.01, 0.5))
    ax.set_yticklabels(["$-2$", "$-3/2$", "$-1$", "$-1/2$", "$0$", "$1/2$", "$1$", "$3/2$", "$2$"])
    ax.tick_params(labelsize=11.5)
    ax.set_ylabel(r"$m$ ($L_z$ in units of $\hbar$)", fontsize=12.5)
    ax.spines["left"].set_bounds(-2, 2)
    ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
    fig.subplots_adjust(left=0.1, right=0.99, top=0.98, bottom=0.02)
    fig.savefig(f"{OUT}/m_ladders.png", dpi=200)
    print("wrote", f"{OUT}/m_ladders.png")
    return fig, None


# ============================================================ lecture 4.5: the rigid rotor
# Lecture 4.5 (page ch04/05, deck slides/ch04/05) uses every figure in this section; deck 4.5 also reuses 4.4's
# dumbbell_reduce. Rotational levels PURPLE (the chapter's rotation colour), transitions ORANGE, P branch TEAL.

# ------------------------------------------------------------ the rigid rotor ladder: levels B J(J+1), each made of 2J+1 states (still)
@register
def rotor_levels():
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    w, g = 0.3, 0.1                                             # width of one state's bar, gap between bars
    for J in range(6):
        E = J * (J + 1)
        n = 2 * J + 1
        x0 = -0.5 * (n * w + (n - 1) * g)
        for k in range(n):
            ax.plot([x0 + k * (w + g), x0 + k * (w + g) + w], [E, E], color=PURPLE, lw=3, solid_capstyle="butt")
        ax.text(-2.6, E, rf"$J = {J}$", ha="right", va="center", fontsize=19)
        ax.text(2.6, E, "0" if J == 0 else rf"${E}\tilde{{B}}$", ha="left", va="center", fontsize=19, color=PURPLE)
    ax.set_xlim(-4.6, 4.3); ax.set_ylim(-1.5, 32); ax.axis("off")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    fig.savefig(f"{OUT}/rotor_levels.png", dpi=200)
    print("wrote", f"{OUT}/rotor_levels.png")
    return fig, None


# ------------------------------------------------------------ why J changes by one: the dipole points along the axis, cos(theta) Y_0 lands only on J = 1 (still)
@register
def rotor_selection():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    th = np.linspace(0, np.pi, 801)
    dth = th[1] - th[0]
    Y0 = np.full_like(th, 1 / np.sqrt(4 * np.pi))
    Y1 = np.sqrt(3 / (4 * np.pi)) * np.cos(th)
    Y2 = np.sqrt(5 / (16 * np.pi)) * (3 * np.cos(th) ** 2 - 1)
    cases = [(r"$J = 0 \to 1$", Y1, 1, "allowed"), (r"$J = 0 \to 2$", Y2, 2, "lobes cancel, forbidden")]
    fig, axes = plt.subplots(2, 2, figsize=(9.6, 3.7), gridspec_kw={"height_ratios": [0.85, 1], "hspace": 0.62, "wspace": 0.12})
    for (ax, bx), (title, Yj, n, verdict) in zip(axes.T, cases):
        ax.axhline(0, color=GRAY, lw=0.8)
        ax.plot(th, Y0, color=GRAY, lw=1.8, ls="--")
        ax.plot(th, Yj, color=TEAL, lw=2.2)
        ax.plot(th, 0.3 * np.cos(th), color=CARDINAL, lw=2.6)
        for xk, lab, col in ((1.0, r"$Y_0^0$", GRAY), (1.55, r"$\cos\theta$", CARDINAL), (2.15, rf"$Y_{n}^0$", TEAL)):
            ax.text(xk, 0.5, lab, color=col, fontsize=15, ha="center", va="center")
        ax.set_title(title, loc="left", fontsize=16)
        f = 2 * np.pi * Yj * np.cos(th) * Y0 * np.sin(th)       # the phi integral gives 2 pi
        area = np.sum(f) * dth
        bx.fill_between(th, f, 0, where=f > 0, color=PURPLE, alpha=0.45, lw=0)
        bx.fill_between(th, f, 0, where=f < 0, color=ORANGE, alpha=0.55, lw=0)
        bx.plot(th, f, color="k", lw=1.6)
        bx.axhline(0, color=GRAY, lw=0.8)
        bx.set_title(rf"multiply: $Y_{n}^0\,\cos\theta\;Y_0^0\,\sin\theta$", loc="left", fontsize=15)
        bx.set_xlabel(("area = 0" if abs(area) < 1e-3 else f"area = {abs(area):.2f}") + f": {verdict}", fontsize=15,
                      color=PURPLE if abs(area) > 1e-3 else GRAY, weight="bold")
        for a in (ax, bx):
            a.set_xlim(0, np.pi); a.set_yticks([]); a.spines["left"].set_visible(False)
        ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
        bx.set_xticks([0, np.pi / 2, np.pi]); bx.set_xticklabels(["0", r"$\pi/2$", r"$\pi$"]); bx.tick_params(labelsize=12)
        ax.set_ylim(-0.62, 0.62); bx.set_ylim(-0.75, 0.75)
    fig.subplots_adjust(left=0.02, right=0.99, top=0.9, bottom=0.16)
    fig.savefig(f"{OUT}/rotor_selection.png", dpi=200)
    print("wrote", f"{OUT}/rotor_selection.png")
    return fig, None


# ------------------------------------------------------------ the microwave spectrum: one rung at a time, gaps 2B, 4B, 6B, ..., lines evenly spaced (still)
@register
def microwave_lines():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.0), gridspec_kw={"width_ratios": [0.85, 1.3], "wspace": 0.22})
    for J in range(6):
        E = J * (J + 1)
        ax.hlines(E, 0, 6.2, color=PURPLE, lw=2.6)
        ax.text(-0.15, E, rf"$J = {J}$", ha="right", va="center", fontsize=12.5)
    for J in range(5):
        x = 0.9 + 1.05 * J
        ax.annotate("", xy=(x, (J + 1) * (J + 2)), xytext=(x, J * (J + 1)),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2, mutation_scale=15, shrinkA=0, shrinkB=0))
        ax.text(x + 0.14, 0.5 * (J * (J + 1) + (J + 1) * (J + 2)), rf"${2 * (J + 1)}\tilde{{B}}$", fontsize=12,
                color=ORANGE, va="center", bbox=dict(fc="white", ec="none", pad=0.5))
    ax.set_xlim(-1.6, 6.4); ax.set_ylim(-1.5, 32); ax.axis("off")
    for J in range(5):
        bx.vlines(2 * (J + 1), 0, 1, color=ORANGE, lw=3)
        bx.text(2 * (J + 1), 1.05, rf"${J}\to{J + 1}$", ha="center", va="bottom", fontsize=12, color=ORANGE)
    bx.annotate("", xy=(6, 0.5), xytext=(4, 0.5), arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.4, shrinkA=2, shrinkB=2))
    bx.text(5, 0.55, r"$2\tilde{B}$", ha="center", va="bottom", fontsize=14, color=GRAY)
    bx.set_xlim(0, 11.5); bx.set_ylim(0, 1.35); bx.set_yticks([])
    bx.spines["left"].set_visible(False)
    bx.set_xticks([0, 2, 4, 6, 8, 10]); bx.set_xticklabels(["0", r"$2\tilde{B}$", r"$4\tilde{B}$", r"$6\tilde{B}$",
                                                            r"$8\tilde{B}$", r"$10\tilde{B}$"])
    bx.tick_params(labelsize=12.5)
    bx.set_xlabel(r"wavenumber $\tilde{\nu}$", fontsize=13)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.95, bottom=0.14)
    fig.savefig(f"{OUT}/microwave_lines.png", dpi=200)
    print("wrote", f"{OUT}/microwave_lines.png")
    return fig, None


# ------------------------------------------------------------ who sits where: rotational populations of HCl and CO at 300 K (still)
@register
def rotor_populations():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    hck, T = 1.438777, 300.0                                   # hc/k_B in cm K
    LIGHT = "#cdb9e3"
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6), gridspec_kw={"width_ratios": [1, 1.6], "wspace": 0.12})
    for ax, (name, B, Jn) in zip(axes, (("HCl", 10.44, 16), ("CO", 1.9225, 31))):
        J = np.arange(Jn)
        allJ = np.arange(400)
        q = np.sum((2 * allJ + 1) * np.exp(-hck * B * allJ * (allJ + 1) / T))
        f = (2 * J + 1) * np.exp(-hck * B * J * (J + 1) / T) / q
        top = int(np.argmax(f))
        ax.bar(J, f, width=0.75, color=[PURPLE if j == top else LIGHT for j in J])
        ax.text(top, f[top] + 0.004, rf"$J = {top}$", ha="center", va="bottom", fontsize=13, color=PURPLE)
        ax.set_title(name, fontsize=15, loc="left")
        ax.set_xlabel("$J$", fontsize=13)
        ax.set_ylim(0, f.max() * 1.22); ax.tick_params(labelsize=11.5)
        ax.set_xlim(-0.8, Jn - 0.2)
    axes[0].set_ylabel("fraction of molecules", fontsize=12.5)
    fig.subplots_adjust(left=0.08, right=0.99, top=0.9, bottom=0.15)
    fig.savefig(f"{OUT}/rotor_populations.png", dpi=200)
    print("wrote", f"{OUT}/rotor_populations.png")
    return fig, None


# ------------------------------------------------------------ rotation rides on vibration: P and R transitions on two ladders, lined up above the band they make (still)
@register
def rovib_branches():
    plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
    B, nu0, hck, T = 10.59, 2886.0, 1.438777, 300.0             # HCl as a rigid rotor and harmonic oscillator
    Jn = 5
    s = 0.5                                                     # drawing units per cm^-1 of rotational energy
    y1 = 185.0                                                  # where the v = 1 ladder starts (energy axis broken)
    lines = [("R", J, nu0 + 2 * B * (J + 1)) for J in range(Jn - 1)] + [("P", J, nu0 - 2 * B * J) for J in range(1, Jn)]
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.6, 5.8), sharex=True, gridspec_kw={"height_ratios": [2.6, 1], "hspace": 0.04})
    x0, x1 = 2780, 2990
    for J in range(Jn):
        E = B * J * (J + 1) * s
        ax.hlines(E, x0, x1, color=PURPLE, lw=1.8)
        ax.hlines(y1 + E, x0, x1, color=PURPLE, lw=1.8)
        ax.text(x1 + 2, E, rf"$J = {J}$", va="center", fontsize=11)
        ax.text(x1 + 2, y1 + E, rf"$J = {J}$", va="center", fontsize=11)
    ax.text(x0 - 3, 0.5 * B * 12 * s, "$v = 0$", ha="right", va="center", fontsize=14, color=TEAL)
    ax.text(x0 - 3, y1 + 0.5 * B * 12 * s, "$v = 1$", ha="right", va="center", fontsize=14, color=TEAL)
    for br, J, nu in lines:
        J2 = J + 1 if br == "R" else J - 1
        ax.annotate("", xy=(nu, y1 + B * J2 * (J2 + 1) * s), xytext=(nu, B * J * (J + 1) * s),
                    arrowprops=dict(arrowstyle="-|>", color=ORANGE if br == "R" else TEAL, lw=1.8, mutation_scale=12,
                                    shrinkA=0, shrinkB=0))
    ax.axvline(nu0, color=GRAY, lw=1, ls=(0, (4, 3)))
    ax.set_xlim(x0 - 40, x1 + 25); ax.set_ylim(-6, y1 + B * 20 * s + 6); ax.axis("off")
    for br, J, nu in lines:
        S = J + 1 if br == "R" else J
        I = S * np.exp(-hck * B * J * (J + 1) / T)
        bx.vlines(nu, 0, I, color=ORANGE if br == "R" else TEAL, lw=3)
        bx.text(nu, I + 0.12, f"{br}({J})", ha="center", va="bottom", fontsize=11.5, color=ORANGE if br == "R" else TEAL)
    bx.axvline(nu0, color=GRAY, lw=1, ls=(0, (4, 3)))
    bx.text(nu0 + 3, 3.2, r"$\tilde{\nu}_0$", ha="left", va="bottom", fontsize=13, color=GRAY)
    bx.set_ylim(0, 4.0); bx.set_yticks([]); bx.spines["left"].set_visible(False)
    bx.tick_params(labelsize=11.5)
    bx.set_xlabel(r"wavenumber (cm$^{-1}$)", fontsize=12.5)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.1)
    fig.savefig(f"{OUT}/rovib_branches.png", dpi=200)
    print("wrote", f"{OUT}/rovib_branches.png")
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
