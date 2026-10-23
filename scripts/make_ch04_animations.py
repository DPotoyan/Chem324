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


if __name__ == "__main__":
    names = sys.argv[1:] or list(REGISTRY)
    for name in names:
        fig, ani = REGISTRY[name]()
        if ani is not None:
            path = f"{OUT}/{name}.gif"
            ani.save(path, writer=PillowWriter(fps=getattr(REGISTRY[name], "fps", 15)), dpi=GIF_DPI)
            print("wrote", path)
        plt.close(fig)
