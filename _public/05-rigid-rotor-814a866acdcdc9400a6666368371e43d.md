---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Rigid Rotor

:::{note} **What you need to know**

- A diatomic molecule turning with a fixed bond length $R_e$ is the particle on a sphere of [Lecture 4.4](04-angular-momentum.md), with its reduced mass $\mu$ and $I = \mu R_e^2$. Its Hamiltonian is $\hat{L}^2/2I$, so its states are the spherical harmonics $Y_J^{M_J}$ and its energies are $E_J = \hbar^2J(J+1)/2I$, each $(2J+1)$-fold degenerate. There is no zero-point rotation.
- Spectroscopists write the levels in wavenumbers, $F(J) = \tilde{B}J(J+1)$, with the rotational constant $\tilde{B} = h/8\pi^2cI$. Light molecules have large $\tilde{B}$ (HCl 10.6 cm$^{-1}$), heavy ones small (CO 1.9 cm$^{-1}$). Either way $\tilde{B} \ll k_BT$, so many rotational levels are populated at room temperature.
- A molecule absorbs microwaves only if it has a permanent dipole, and only one rung at a time, $\Delta J = \pm 1$: the dipole points along the molecular axis, and the photon carries one unit of angular momentum. The lines fall at $2\tilde{B}(J+1)$, evenly spaced by $2\tilde{B}$, and the spacing gives the bond length.
- Line intensities follow the populations $(2J+1)\,e^{-hcF(J)/k_BT}$, which rise with the degeneracy and then fall with the Boltzmann factor.
- In the infrared, rotation rides on vibration. $\Delta v = +1$ with $\Delta J = \pm 1$ gives an R branch above and a P branch below the band origin $\tilde{\nu}_0$, with a gap where $\Delta J = 0$ would be. Real molecules add two small corrections: $\tilde{B}$ shrinks in higher vibrational levels, and fast rotation stretches the bond.
- A measured spectrum shows all of this, and more: every HCl line is a pair from chlorine's two isotopes, the lines drift from even spacing, and an instrument's resolution decides whether lines or only humps appear.

:::

### A rotating molecule is a particle on a sphere

[Lecture 4.4](04-angular-momentum.md) reduced a rigid dumbbell to one particle of reduced mass $\mu$ on a circle. Let the dumbbell point in any direction and the particle moves on a sphere of radius $R_e$, the bond length. The potential energy does not change as the molecule turns, so all of its energy is the kinetic energy of rotation, $L^2/2I$:

$$
\hat{H} = \frac{\hat{L}^2}{2I}, \qquad I = \mu R_e^2
$$

```{code-cell} python
:tags: [hide-input]
# synced: rotor_sphere
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle, FancyArrowPatch
from matplotlib.colors import to_rgb
mC, mO, R = 12.0, 16.0, 1.9
rC, rO = mO / (mC + mO) * R, mC / (mC + mO) * R            # distances from the center of mass, m_C r_C = m_O r_O
fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.9))
for a_ in (ax, bx):
    a_.set_xlim(-2.4, 2.4); a_.set_ylim(-2.0, 2.0); a_.set_aspect("equal"); a_.axis("off")
ax.plot([-rC, rO], [0, 0], color="#adb5bd", lw=6, solid_capstyle="round", zorder=2)
ax.add_patch(Circle((-rC, 0), 0.27, fc="#495057", ec="k", lw=1, zorder=3))
ax.add_patch(Circle((rO, 0), 0.31, fc=CARDINAL, ec="k", lw=1, zorder=3))
ax.text(-rC, 0, "C", color="white", ha="center", va="center", fontsize=13, weight="bold", zorder=4)
ax.text(rO, 0, "O", color="white", ha="center", va="center", fontsize=13, weight="bold", zorder=4)
ax.plot([0], [0], "+", color="k", ms=13, mew=2.2, zorder=5)
ax.annotate("", xy=(-rC, -0.62), xytext=(rO, -0.62), arrowprops=dict(arrowstyle="<->", color="k", lw=1.4,
                                                                  shrinkA=0, shrinkB=0))
ax.text(0.5 * (rO - rC), -0.78, "$R_e$", ha="center", va="top", fontsize=18)
ax.add_patch(FancyArrowPatch((1.55 * np.cos(np.radians(15)), 1.55 * np.sin(np.radians(15))),
                             (1.55 * np.cos(np.radians(65)), 1.55 * np.sin(np.radians(65))),
                             connectionstyle="arc3,rad=0.25", arrowstyle="-|>", mutation_scale=16, color=PURPLE, lw=1.8))
S = 301                                                     # the sphere: shaded pale purple, lit from the upper left
u = np.linspace(-1, 1, S)
U, V = np.meshgrid(u, u[::-1])
W = np.sqrt(np.clip(1 - U ** 2 - V ** 2, 0, None))
lit = np.clip(-0.45 * U + 0.55 * V + 0.7 * W, 0, None) / np.linalg.norm([-0.45, 0.55, 0.7])
rgb = 1 - (0.06 + 0.16 * (1 - lit))[..., None] * (1 - np.array(to_rgb(PURPLE)))
bx.imshow(np.dstack([rgb, (U ** 2 + V ** 2 < 1).astype(float)]), extent=(-R, R, -R, R), interpolation="bilinear",
          zorder=1)
bx.add_patch(Circle((0, 0), R, fill=False, ec=PURPLE, lw=1.3, zorder=2))
el = np.radians(20)                                         # the view looks 20 degrees down on the equator
ps = np.linspace(-np.pi / 2, np.pi / 2, 200)
bx.plot(R * np.sin(ps), -R * np.sin(el) * np.cos(ps), color=PURPLE, lw=1.1, alpha=0.8, zorder=2)          # front
bx.plot(-R * np.sin(ps), R * np.sin(el) * np.cos(ps), color=PURPLE, lw=1.0, ls=(0, (3, 3)), alpha=0.55, zorder=2)
th, ps0 = np.radians(50), np.radians(50)                    # where the bead sits on the near side
bead = (R * np.sin(th) * np.sin(ps0), R * (-np.sin(el) * np.sin(th) * np.cos(ps0) + np.cos(el) * np.cos(th)))
bx.plot([0, bead[0]], [0, bead[1]], color="k", lw=1.6, zorder=3)
bx.add_patch(Circle(bead, 0.27, fc=PURPLE, ec="k", lw=1, zorder=4))
bx.text(bead[0], bead[1], r"$\mu$", color="white", ha="center", va="center", fontsize=15, zorder=5)
bx.plot([0], [0], "+", color="k", ms=13, mew=2.2, zorder=5)
ang = np.arctan2(bead[1], bead[0])
bx.text(0.55 * bead[0] + 0.27 * np.sin(ang), 0.55 * bead[1] - 0.27 * np.cos(ang), "$R_e$", fontsize=18,
        ha="center", va="center", zorder=5)
fig.text(0.5, 0.5, "=", ha="center", va="center", fontsize=30, color=GRAY)
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01, wspace=0.1)
plt.show()
```

Fig. Two atoms a bond length $R_e$ apart, turning about their center of mass (+), move like one particle of reduced mass $\mu$ on a sphere of radius $R_e$.

Lecture 4.4 already found the eigenfunctions of $\hat{L}^2$, the spherical harmonics, so the problem is solved. For rotating molecules, spectroscopists write $J$ and $M_J$ in place of $l$ and $m$:

:::{important} **The rigid rotor**

$$
\hat{H}\,Y_J^{M_J} = E_J\,Y_J^{M_J}, \qquad E_J = \frac{\hbar^2}{2I}\,J(J+1), \qquad J = 0, 1, 2, \dots \qquad M_J = -J, \dots, J
$$

- Each level is $(2J+1)$-fold degenerate: the energy does not depend on $M_J$, the orientation of the rotation in space
- $I = \mu R_e^2$, with $\mu$ the reduced mass and $R_e$ the bond length
:::

```{code-cell} python
:tags: [hide-input]
# synced: rotor_levels
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The levels of a rigid rotor, in units of the rotational constant $\tilde{B}$ (defined below). Level $J$ holds $2J + 1$ states, one bar for each value of $M_J$.

- **The gaps grow.** $E_{J+1} - E_J = (\hbar^2/I)(J + 1)$: two, four, six, ... times $\hbar^2/2I$. Each step up in rotation costs more than the last.
- **No zero-point energy.** $J = 0$ has $E = 0$. $Y_0^0$ is the same in every direction: the bond axis points anywhere with equal probability, and nothing rotates. As on the ring of Lecture 4.4, no wall and no potential squeezes the wavefunction. A vibrating bond, by contrast, always keeps $\frac{1}{2}\hbar\omega$ ([Lecture 4.2](02-quantum-harmonic-oscillator.md)).
- **What a state describes.** $\lvert Y_J^{M_J}(\theta, \phi)\rvert^2$ is the probability density for the bond axis to point in the direction $(\theta, \phi)$.

#### Spectroscopists count in wavenumbers

As for vibrations in [Lecture 4.3](03-molecular-vibrations.md), divide each energy by $hc$:

:::{important} **Rotational term values**

$$
F(J) = \frac{E_J}{hc} = \tilde{B}\,J(J+1), \qquad \tilde{B} = \frac{h}{8\pi^2cI}
$$

- $\tilde{B}$, the **rotational constant**, is in cm$^{-1}$. A large moment of inertia means a small $\tilde{B}$ and closely spaced levels
:::

:::{note} **Example: the rotational constant of HCl**

H$^{35}$Cl has $R_e = 127.5$ pm. Find its moment of inertia, $\tilde{B}$, and the energy of the level $J = 1$. What are $L$ and $L_z$ there?

- Reduced mass: $\mu = \dfrac{(1.00783)(34.96885)}{35.97668}$ u $= 0.97959$ u $= 1.6266\times10^{-27}$ kg.
- Moment of inertia: $I = \mu R_e^2 = (1.6266\times10^{-27}\ \text{kg})(127.5\times10^{-12}\ \text{m})^2 = 2.644\times10^{-47}$ kg m$^2$.
- Rotational constant, with $c$ in cm/s:

$$
\tilde{B} = \frac{6.626\times10^{-34}\ \text{J s}}{8\pi^2\,(2.998\times10^{10}\ \text{cm/s})(2.644\times10^{-47}\ \text{kg m}^2)} = 10.59\ \text{cm}^{-1}
$$

- The level $J = 1$: $F(1) = 2\tilde{B} = 21.2$ cm$^{-1}$. Its angular momentum is $L = \sqrt{2}\,\hbar = 1.49\times10^{-34}$ J s, with $L_z = -\hbar$, $0$ or $+\hbar$.
:::

#### Rotation is cheap

| molecule | $\tilde{B}$ (cm$^{-1}$) | vibration $\tilde{\nu}$ (cm$^{-1}$) | $k_BT/hc\tilde{B}$ at 300 K |
| :-- | --: | --: | --: |
| H$_2$ | 60.9 | 4161 | 3.4 |
| HCl | 10.6 | 2886 | 20 |
| CO | 1.93 | 2143 | 108 |
| I$_2$ | 0.037 | 213 | 5600 |

- Rotational steps are a hundred to ten thousand times smaller than vibrational ones. At room temperature $k_BT = 208$ cm$^{-1}$ is far above $\tilde{B}$, so many $J$ levels are occupied (below), while nearly every molecule sits in $v = 0$ ([Lecture 4.1](01-molecular-degrees-of-freedom.md)).
- The light hydrides have the largest $\tilde{B}$: the moment of inertia depends on the reduced mass, which a hydrogen atom keeps small.

### Which transitions light can drive

#### A rotating dipole is an antenna

Light pushes on the dipole moment $M$ of a molecule ([Lecture 4.3](03-molecular-vibrations.md)). A polar diatomic such as HCl or CO carries a **permanent dipole** $M_e$: its dipole at the bond length $R_e$, the first term of Lecture 4.3's $M(x) = M_e + M'x + \dots$ It points along the molecular axis, and it is about 1.1 D for HCl and 0.11 D for CO. As the molecule turns, the dipole turns with it. Seen along a fixed direction $z$, its component $M_z = M_e\cos\theta$ oscillates at the rotation frequency, so it can exchange energy with light at that frequency.

```{code-cell} python
:tags: [hide-input]
# synced: rotor_antenna
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle, FancyArrowPatch
nf = 40
ts = np.arange(nf) / nf                                     # one loop of the animation = two turns
GREEN, BLUE = "#2f9e44", "#1c7ed6"
T0, T1 = 1.65, 5.25                                         # where the trace starts and ends (time 0 to 1)
tt = np.linspace(0, 1, 300)
ring = np.linspace(0, 2 * np.pi, 200)
# per row: atom labels, colours, radii, distances of the two atoms from the center of mass, polar?
rows = [(("H", "Cl"), ("white", GREEN), (0.15, 0.27), (0.62, 0.62 / 35), True),
        (("N", "N"), (BLUE, BLUE), (0.22, 0.22), (0.37, 0.37), False)]
fig, axes = plt.subplots(2, 1, figsize=(7.2, 5.3))
parts = []
for ax, (labels, cols, rads, (p1, p2), polar) in zip(axes, rows):
    ax.set_xlim(-1.3, T1 + 1.1); ax.set_ylim(-1.32, 1.4); ax.set_aspect("equal"); ax.axis("off")
    ax.plot([0, 0], [-1.22, 1.22], color=GRAY, lw=1, ls=(0, (4, 3)), zorder=1)        # the field direction z
    ax.text(0.1, 1.26, "$z$", fontsize=19, color=GRAY, va="center")
    ax.plot([T0, T0], [-1.15, 1.15], color=GRAY, lw=0.9)
    ax.annotate("", xy=(T1 + 0.35, 0), xytext=(T0, 0), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=0.9,
                                                                     mutation_scale=12, shrinkA=0, shrinkB=0))
    ax.text(T1 + 0.42, -0.1, "$t$", fontsize=19, color=GRAY, va="top")
    ax.text(T0, 1.28, "$M_z$", fontsize=19, ha="center", va="center", color=ORANGE)
    if polar:
        ax.plot(np.cos(ring), np.sin(ring), color=ORANGE, lw=0.9, ls=":", alpha=0.7, zorder=1)  # where the tip runs
        for yv, lab in ((1, "$+M_e$"), (-1, "$-M_e$")):
            ax.plot([T0, T1], [yv, yv], color=GRAY, lw=0.9, ls=":")
            ax.text(T1 + 0.08, yv, lab, fontsize=18, color=GRAY, va="center")
        ax.plot(T0 + (T1 - T0) * tt, np.cos(4 * np.pi * tt), color="#dee2e6", lw=1.8, zorder=1)
    else:
        ax.text(-1.25, -1.1, "$M_e = 0$", fontsize=19, color=ORANGE, va="center")
    (bond,) = ax.plot([], [], color="#adb5bd", lw=6, solid_capstyle="round", zorder=3)
    c1 = Circle((0, 0), rads[0], fc=cols[0], ec="k", lw=1, zorder=4); ax.add_patch(c1)
    c2 = Circle((0, 0), rads[1], fc=cols[1], ec="k", lw=1, zorder=4); ax.add_patch(c2)
    l1 = ax.text(0, 0, labels[0], ha="center", va="center", fontsize=11, weight="bold", zorder=5,
                 color="k" if cols[0] == "white" else "white")
    l2 = ax.text(0, 0, labels[1], ha="center", va="center", fontsize=11, weight="bold", zorder=5, color="white")
    arrow = FancyArrowPatch((0, 0), (0, 1), arrowstyle="-|>", mutation_scale=19, color=ORANGE, lw=3.0,
                            shrinkA=0, shrinkB=0, zorder=3.5)                 # over the bond, under the atoms
    if polar:
        ax.add_patch(arrow)
    (arc,) = ax.plot([], [], color="k", lw=1.2, zorder=6)
    th_lab = ax.text(0, 0, r"$\theta$", fontsize=19, ha="center", va="center", zorder=6)
    (link,) = ax.plot([], [], color=ORANGE, lw=1.1, ls=":", zorder=2)
    (trace,) = ax.plot([], [], color=ORANGE, lw=2.4, zorder=3)
    (dot,) = ax.plot([], [], "o", color=ORANGE, ms=7, zorder=4)
    parts.append((p1, p2, polar, bond, c1, c2, l1, l2, arrow, arc, th_lab, link, trace, dot))
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01, hspace=0.06)

def update(i):
    a = 4 * np.pi * ts[i]                                   # the angle turned so far
    d = np.array([-np.sin(a), np.cos(a)])                   # unit vector along the bond, toward H: the dipole
    th = np.arccos(np.clip(d[1], -1, 1))                    # the polar angle from z, 0 to pi
    side = 1.0 if d[0] <= 0 else -1.0                       # the arc runs from z toward the dipole, the short way
    arcs = np.pi / 2 + side * np.linspace(0, th, 40)
    x_now = T0 + (T1 - T0) * ts[i]
    sel = tt <= ts[i] + 1e-9
    for p1, p2, polar, bond, c1, c2, l1, l2, arrow, arc, th_lab, link, trace, dot in parts:
        P1, P2 = p1 * d, -p2 * d
        bond.set_data([P2[0], P1[0]], [P2[1], P1[1]])
        c1.center, c2.center = (P1[0], P1[1]), (P2[0], P2[1])
        l1.set_position((P1[0], P1[1])); l2.set_position((P2[0], P2[1]))
        if polar:
            arrow.set_positions((0, 0), (d[0], d[1]))
            arc.set_data(0.37 * np.cos(arcs), 0.37 * np.sin(arcs))
            mid = np.pi / 2 + side * th / 2
            th_lab.set_position((0.58 * np.cos(mid), 0.58 * np.sin(mid)))
            th_lab.set_visible(th > np.radians(40))
            link.set_data([d[0], x_now], [d[1], d[1]])
            trace.set_data(T0 + (T1 - T0) * tt[sel], np.cos(4 * np.pi * tt[sel]))
            dot.set_data([x_now], [d[1]])
        else:
            th_lab.set_visible(False)
            trace.set_data(T0 + (T1 - T0) * tt[sel], 0 * tt[sel])
            dot.set_data([x_now], [0])

ani = FuncAnimation(fig, update, frames=nf, interval=85, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. HCl (top) and N$_2$ (bottom) turning. HCl's dipole (orange arrow, pointing from the negative Cl end to the positive H end) turns with the bond. Its height along $z$, $M_z = M_e\cos\theta$, is traced at the right: it swings between $+M_e$ and $-M_e$ at the rotation frequency. N$_2$ has no dipole, so its trace stays at zero.

A nonpolar molecule (H$_2$, N$_2$, O$_2$, CO$_2$, CH$_4$) has no permanent dipole, so its rotation is invisible in absorption. (Raman spectroscopy still sees it, through the polarizability.)

#### One rung at a time: $\Delta J = \pm 1$

A field along $z$ pushes on the $z$ component of the dipole, $M_e\cos\theta$, where $\theta$ is the angle between the bond axis and $z$. The transition dipole of [Lecture 4.3](03-molecular-vibrations.md) becomes an integral over orientations:

$$
\langle J'M_J'|\hat{M}_z|JM_J\rangle = M_e\int Y_{J'}^{M_J'*}\,\cos\theta\;Y_J^{M_J}\,\sin\theta\,d\theta\,d\phi
$$

- **From $J = 0$**: $\cos\theta\,Y_0^0 = Y_1^0/\sqrt{3}$ exactly. The function the field produces is a $J = 1$ state, so $J = 1$ is the only level it reaches.
- **In general**, $\cos\theta\,Y_J^{M_J}$ is a mixture of $Y_{J+1}^{M_J}$ and $Y_{J-1}^{M_J}$ (a recursion of the spherical harmonics), so $J$ changes by one and $M_J$ stays. Light polarized in the $xy$ plane couples through $\sin\theta\,e^{\pm i\phi}$ and changes $M_J$ by one as well.
- **Physically**, a photon carries one unit $\hbar$ of angular momentum. Absorbing it changes the molecule's angular momentum by exactly one unit.

```{code-cell} python
:tags: [hide-input]
# synced: rotor_selection
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Why $J$ changes by one. Top: the state $Y_0^0$ (gray dashed), the factor $\cos\theta$ from the dipole along the bond axis (red), and a final state (teal), against the angle $\theta$ between the axis and the field. Bottom: their product times $\sin\theta$ from the surface element; its area is the transition dipole over $M_e$. It is $1/\sqrt{3} = 0.58$ for $J = 0 \to 1$ and zero for $J = 0 \to 2$, whose lobes cancel.

:::{important} **Selection rules for rotational absorption**

$$
M_e \neq 0, \qquad \Delta J = \pm 1, \qquad \Delta M_J = 0, \pm 1
$$

- The molecule must have a permanent dipole moment, and $J$ changes by one: absorption from $J$ to $J + 1$, emission from $J$ to $J - 1$
:::

### The microwave spectrum

Absorption from $J$ to $J + 1$ takes a photon of wavenumber

$$
\tilde{\nu}_J = F(J+1) - F(J) = \tilde{B}\,\big[(J+1)(J+2) - J(J+1)\big] = 2\tilde{B}\,(J+1)
$$

:::{important} **Microwave lines of a rigid rotor**

$$
\tilde{\nu}_J = 2\tilde{B}\,(J+1), \qquad J = 0, 1, 2, \dots \qquad\qquad \tilde{\nu}_{J+1} - \tilde{\nu}_J = 2\tilde{B}
$$
:::

```{code-cell} python
:tags: [hide-input]
# synced: microwave_lines
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Left: absorptions climb one rung at a time, with gaps $2\tilde{B}$, $4\tilde{B}$, $6\tilde{B}$, .... Right: the lines they make, evenly spaced by $2\tilde{B}$.

- The gaps grow by the same amount each step, so the lines are evenly spaced: the fingerprint of a rotating molecule. Measure the spacing and you have $\tilde{B}$, then $I$, then the bond length.
- Lines between 1 and 100 cm$^{-1}$ have frequencies $\nu = c\tilde{\nu}$ from 30 GHz to 3 THz: microwaves and the far infrared.

:::{note} **Example: the bond length of CO**

Carbon monoxide absorbs at 3.845, 7.690 and 11.535 cm$^{-1}$ (115.27, 230.54 and 345.81 GHz). Find its bond length.

- The lines are $2\tilde{B} = 3.845$ cm$^{-1}$ apart, so $\tilde{B} = 1.9225$ cm$^{-1}$.
- Moment of inertia:

$$
I = \frac{h}{8\pi^2c\tilde{B}} = \frac{6.626\times10^{-34}\ \text{J s}}{8\pi^2\,(2.998\times10^{10}\ \text{cm/s})(1.9225\ \text{cm}^{-1})} = 1.456\times10^{-46}\ \text{kg m}^2
$$

- Reduced mass: $\mu = \dfrac{(12.000)(15.995)}{27.995}$ u $= 6.856$ u $= 1.1385\times10^{-26}$ kg.
- Bond length: $R = \sqrt{I/\mu} = \sqrt{1.456\times10^{-46}/1.1385\times10^{-26}}$ m $= 1.131\times10^{-10}$ m $= 113.1$ pm.

Line frequencies are measured to many digits, so microwave spectroscopy gives bond lengths to better than 0.01 pm.
:::

- Swapping $^{12}$C for $^{13}$C leaves the bond length alone but raises $\mu$, so every line moves (Problem 1). Radio astronomers map the cold gas between the stars through CO's 115 GHz line.

#### Line intensities follow the populations

How strong a line is depends first on how many molecules start in level $J$. The Boltzmann factor with the degeneracy $2J + 1$ gives:

:::{important} **Populations of rotational levels**

$$
\frac{N_J}{N_0} = (2J+1)\,e^{-hc\tilde{B}J(J+1)/k_BT}
$$
:::

```{code-cell} python
:tags: [hide-input]
# synced: rotor_populations
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The fraction of molecules in each rotational level at 300 K, for HCl ($\tilde{B} = 10.44$ cm$^{-1}$) and CO ($\tilde{B} = 1.92$ cm$^{-1}$). The most populated level is darker.

- The degeneracy $2J + 1$ rises and the Boltzmann factor falls, so the populations peak: at $J = 3$ for HCl and $J = 7$ for CO at room temperature (Problem 3 finds the peak). The heavier molecule spreads over more levels.
- Each absorption line inherits the population of its starting level. (For microwave lines the photon energy adds a factor that pushes the strongest line a few $J$ higher.)

numpy checks the HCl populations:

```{code-cell} python
import numpy as np

B, T = 10.44, 300.0                       # HCl: rotational constant (cm^-1) and temperature (K)
hc_k = 1.4388                             # hc/k_B in cm K
J = np.arange(0, 40)
N = (2 * J + 1) * np.exp(-hc_k * B * J * (J + 1) / T)
print("N_J / N_0 for J = 0 to 7:", np.round(N[:8] / N[0], 2))
print("most populated J:", N.argmax(), "  fraction of molecules there:", round(N.max() / N.sum(), 3))
```

### Rotation rides on vibration: infrared bands

An infrared photon changes $v$ ([Lecture 4.3](03-molecular-vibrations.md)), but the molecule is also rotating, and a photon must change $J$ by one as well. The energies add ([Lecture 4.1](01-molecular-degrees-of-freedom.md)):

$$
\tilde{E}(v, J) = \tilde{\nu}\left(v + \tfrac{1}{2}\right) + \tilde{B}\,J(J+1)
$$

Starting from $(v = 0, J)$, a photon can reach $(1, J + 1)$ or $(1, J - 1)$:

$$
\begin{aligned}
\Delta J = +1:\quad &\tilde{\nu}_0 + \tilde{B}(J+1)(J+2) - \tilde{B}J(J+1) = \tilde{\nu}_0 + 2\tilde{B}(J+1) \\
\Delta J = -1:\quad &\tilde{\nu}_0 + \tilde{B}(J-1)J - \tilde{B}J(J+1) = \tilde{\nu}_0 - 2\tilde{B}J
\end{aligned}
$$

:::{important} **The P and R branches**

$$
\text{R branch } (\Delta J = +1):\quad \tilde{\nu}_R(J) = \tilde{\nu}_0 + 2\tilde{B}\,(J+1), \qquad J = 0, 1, 2, \dots
$$

$$
\text{P branch } (\Delta J = -1):\quad \tilde{\nu}_P(J) = \tilde{\nu}_0 - 2\tilde{B}\,J, \qquad J = 1, 2, 3, \dots
$$

- $J$ is the level the molecule starts from, in $v = 0$; $\tilde{\nu}_0$ is the band origin, the vibrational wavenumber
- No line at $\tilde{\nu}_0$: $\Delta J = 0$ is forbidden for a diatomic
:::

```{code-cell} python
:tags: [hide-input]
# synced: rovib_branches
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Top: the rotational ladders of $v = 0$ and $v = 1$ (the gap between them is not to scale). R transitions (orange) end one rung higher, P transitions (teal) one rung lower. Bottom: the lines they make, lined up under the arrows, for HCl at 300 K. The two branches have lines $2\tilde{B}$ apart, with a gap at the band origin $\tilde{\nu}_0$.

- **The gap.** R(0) and P(1) are $4\tilde{B}$ apart, twice the usual spacing: the missing line at $\tilde{\nu}_0$ would need $\Delta J = 0$. Molecules with extra angular momentum about the axis, such as NO or the bend of CO$_2$, do show a central Q branch.
- **The envelopes.** The heights follow the populations of the starting levels, so each branch rises and falls like the curve of the last section.

#### A real spectrum

Every spectrum so far has been sticks computed from a formula. Here is what an instrument records: HCl gas at 20 Torr in a 10 cm cell, in a Fourier-transform infrared (FTIR) spectrometer. The vertical axis is the **absorbance**,

$$
A = \log_{10}\frac{I_0}{I}
$$

where $I_0$ is the light entering the cell and $I$ the light leaving it. At $A = 0$ nothing is absorbed, and at $A = 1$ the gas removes 90% of the light.

```{code-cell} python
:tags: [hide-input]
# synced: hcl_measured
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
import os
DATA = "data" if os.path.isdir("data") else "ch04/data"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
nu, A = np.loadtxt(f"{DATA}/hcl_band.csv", delimiter=",", unpack=True)
nu0 = 2885.95
Pl = {1: 2865.10, 2: 2843.62, 3: 2821.56, 4: 2798.94, 5: 2775.76, 6: 2752.03, 7: 2727.77, 8: 2703.00, 9: 2677.74}
Rl = {0: 2906.25, 1: 2925.89, 2: 2944.90, 3: 2963.28, 4: 2980.99, 5: 2998.04, 6: 3014.40, 7: 3030.09, 8: 3045.05}
fig, ax = plt.subplots(figsize=(11, 3.7))
ax.plot(nu[nu < nu0], A[nu < nu0], color=TEAL, lw=1.2)
ax.plot(nu[nu > nu0], A[nu > nu0], color=ORANGE, lw=1.2)
for br, table, col in (("P", Pl, TEAL), ("R", Rl, ORANGE)):
    for J, c in table.items():
        ax.text(c, A[np.abs(nu - c) < 0.4].max() + 0.025, f"{br}({J})", ha="center", va="bottom", fontsize=12.5, color=col)
ax.axvline(nu0, color=GRAY, lw=1, ls=(0, (4, 3)))
ax.text(nu0, 1.03, r"$\tilde{\nu}_0$", ha="center", va="bottom", fontsize=15, color=GRAY)
ax.set_xlim(2640, 3085); ax.set_ylim(0, 1.03)
ax.set_xlabel(r"wavenumber (cm$^{-1}$)", fontsize=14); ax.set_ylabel("absorbance", fontsize=14)
ax.tick_params(labelsize=12.5)
fig.subplots_adjust(left=0.065, right=0.99, top=0.92, bottom=0.17)
plt.show()
```

Fig. The measured infrared band of HCl gas at room temperature. P lines teal, R lines orange, dashed line at the band origin. Each label marks the taller line of its pair. Data: J. Gutow, University of Wisconsin-Oshkosh [@gutow2025hcl].

- **The comb and the gap are there.** Neighboring lines are about 21 cm$^{-1}$ apart, and the gap at the band origin is twice that.
- **The tallest lines are P(3) and R(2).** They start from the most populated levels, near $J = 3$.
- **Every line has a smaller partner.** A rigid rotor does not explain that; the next subsection does.

:::{note} **Example: reading the HCl band**

In the figure above, the lines nearest the gap are R(0) = 2906.25 and P(1) = 2865.10 cm$^{-1}$. Find the band origin and $\tilde{B}$, treating HCl as a rigid rotor.

The two lines sit symmetrically about the gap, $\tilde{\nu}_0 \pm 2\tilde{B}$:

$$
\tilde{\nu}_0 = \frac{2906.25 + 2865.10}{2} = 2885.68\ \text{cm}^{-1}, \qquad \tilde{B} = \frac{2906.25 - 2865.10}{4} = 10.29\ \text{cm}^{-1}
$$

The band origin is 2885.98 cm$^{-1}$, and the microwave value of $\tilde{B}$ is 10.44 cm$^{-1}$. The small differences come from the bond being slightly longer in $v = 1$ (next section).
:::

#### Why every line is double

Natural chlorine is 76% $^{35}$Cl and 24% $^{37}$Cl, so the cell holds two molecules with slightly different reduced masses, and each makes its own band.

```{code-cell} python
:tags: [hide-input]
# synced: hcl_doublet
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
import os
DATA = "data" if os.path.isdir("data") else "ch04/data"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
nu, A = np.loadtxt(f"{DATA}/hcl_zoom.csv", delimiter=",", unpack=True)
LIGHT = "#f0b266"
heavy = (np.abs(nu - 2942.72) < 0.9) | (np.abs(nu - 2961.06) < 0.9)   # the H37Cl peak of each pair
fig, ax = plt.subplots(figsize=(7.4, 4.2))
ax.plot(nu, np.where(heavy, np.nan, A), color=ORANGE, lw=1.8)
ax.plot(nu, np.where(heavy, A, np.nan), color=LIGHT, lw=1.8)
ax.text(2942.72, 0.59, r"H$^{37}$Cl", ha="center", va="bottom", fontsize=15, color="#c98a2e")
ax.text(2944.90, 0.90, r"H$^{35}$Cl", ha="center", va="bottom", fontsize=15, color=ORANGE)
ax.text(2961.06, 0.57, r"H$^{37}$Cl", ha="center", va="bottom", fontsize=15, color="#c98a2e")
ax.text(2963.28, 0.87, r"H$^{35}$Cl", ha="center", va="bottom", fontsize=15, color=ORANGE)
ax.text(2943.8, 1.04, "R(2)", ha="center", va="bottom", fontsize=15, color="k")
ax.text(2962.2, 1.04, "R(3)", ha="center", va="bottom", fontsize=15, color="k")
ax.set_xlim(2937, 2969); ax.set_ylim(0, 1.13)
ax.set_xlabel(r"wavenumber (cm$^{-1}$)", fontsize=14); ax.set_ylabel("absorbance", fontsize=14)
ax.tick_params(labelsize=12.5)
fig.subplots_adjust(left=0.11, right=0.98, top=0.98, bottom=0.15)
plt.show()
```

Fig. Two lines of the same spectrum, magnified. The heavier H$^{37}$Cl (light orange) sits just below H$^{35}$Cl (orange) at every line.

:::{note} **Example: the size of the isotope split**

A vibrational wavenumber scales as $1/\sqrt{\mu}$ ([Lecture 4.3](03-molecular-vibrations.md)). With $\mu(\text{H}^{35}\text{Cl}) = 0.97959$ u and $\mu(\text{H}^{37}\text{Cl}) = 0.98108$ u, estimate how far below the H$^{35}$Cl band (2886 cm$^{-1}$) the H$^{37}$Cl band should sit.

$$
\Delta\tilde{\nu} = 2886\left(1 - \sqrt{\frac{0.97959}{0.98108}}\right) = 2.2\ \text{cm}^{-1}
$$

The two measured band origins are 2885.95 and 2883.85 cm$^{-1}$, about 2.1 apart. Scaling $\tilde{\nu}_e$ and $\tilde{\nu}_ex_e$ separately, as in Problem 5, gives 2.11. A 0.15% change in the reduced mass is easy to see.
:::

- **Why the heights are not 3 : 1.** The abundances are 3.1 : 1, but the tallest pairs measure only about 1.5 : 1. Each line is much narrower (roughly 0.01 cm$^{-1}$) than the instrument can resolve, and the gas absorbs nearly all the light at its center. A line that is already black at its center cannot get much deeper with three times the molecules, so tall peaks are squeezed. Weaker lines come closer to the true ratio: about 2 : 1 at the faint ends of this band, and up to 2.8 : 1 in the much weaker overtone.
- **The same squeeze flattens the envelope.** P(3)/P(1) measures 1.3 here, against 1.8 for the sticks. Positions are unaffected, and the widget below shows the true strengths.

Try it: pick a molecule and change the temperature. Heat spreads the molecules over higher $J$, so the branches widen; the "real molecule" setting adds the corrections of the next section.

```{anywidget} ../widgets/rotor_spectrum.mjs
{}
```

### Beyond the rigid rotor

#### The bond is longer in $v = 1$

A real bond stretches more easily than it compresses (the Morse well of [Lecture 4.3](03-molecular-vibrations.md)), so the average bond length grows with $v$, and $\tilde{B}$ shrinks:

$$
\tilde{B}_v = \tilde{B}_e - \alpha_e\left(v + \tfrac{1}{2}\right)
$$

For HCl, $\tilde{B}_0 = 10.44$ and $\tilde{B}_1 = 10.14$ cm$^{-1}$. With $\tilde{B}_1$ in the upper level and $\tilde{B}_0$ in the lower one, the branches are no longer evenly spaced:

$$
\tilde{\nu}_R(J) = \tilde{\nu}_0 + 2\tilde{B}_1 + (3\tilde{B}_1 - \tilde{B}_0)\,J + (\tilde{B}_1 - \tilde{B}_0)\,J^2
$$

$$
\tilde{\nu}_P(J) = \tilde{\nu}_0 - (\tilde{B}_1 + \tilde{B}_0)\,J + (\tilde{B}_1 - \tilde{B}_0)\,J^2
$$

- Since $\tilde{B}_1 < \tilde{B}_0$, the R lines crowd together at high $J$ and the P lines spread apart.
- Pairs of lines that share an upper or a lower level give $\tilde{B}_1$ and $\tilde{B}_0$ separately (combination differences).

The measured band shows the crowding directly:

```{code-cell} python
:tags: [hide-input]
# synced: hcl_gaps
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
m = np.array([-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
nu = np.array([2571.87, 2599.02, 2625.73, 2651.96, 2677.74, 2703.00, 2727.77, 2752.03, 2775.76, 2798.94, 2821.56,
               2843.62, 2865.10, 2906.25, 2925.89, 2944.90, 2963.28, 2980.99, 2998.04, 3014.40, 3030.09, 3045.05,
               3059.32, 3072.85, 3085.64])                  # measured H35Cl lines; m = J + 1 for R(J), m = -J for P(J)
c = np.polyfit(m, nu, 3)
next_ = m[1:] - m[:-1] == 1                                 # neighbors only: R(0) and P(1) straddle the gap
gap, mid, side = (nu[1:] - nu[:-1])[next_], ((nu[1:] + nu[:-1]) / 2)[next_], m[:-1][next_]
ms = np.linspace(-13, 11, 200)
fig, ax = plt.subplots(figsize=(8.2, 4.1))
ax.plot((np.polyval(c, ms) + np.polyval(c, ms + 1)) / 2, np.polyval(c, ms + 1) - np.polyval(c, ms), color=GRAY, lw=1.4, zorder=1)
ax.axhline(2 * 10.29, color=GRAY, lw=1.2, ls=(0, (4, 3)), zorder=1)
ax.scatter(mid[side < 0], gap[side < 0], s=52, color=TEAL, zorder=3)
ax.scatter(mid[side > 0], gap[side > 0], s=52, color=ORANGE, zorder=3)
ax.text(3098, 2 * 10.29 + 0.35, r"rigid rotor, $2\tilde{B}$", ha="right", va="bottom", fontsize=14, color=GRAY)
ax.text(2672, 28.0, "P branch", ha="left", va="center", fontsize=15, color=TEAL)
ax.text(2905, 14.6, "R branch", ha="left", va="center", fontsize=15, color=ORANGE)
ax.set_xlim(2570, 3100); ax.set_ylim(11, 29.5); ax.set_yticks([12, 16, 20, 24, 28])
ax.set_xlabel(r"wavenumber (cm$^{-1}$)", fontsize=14)
ax.set_ylabel(r"gap to the next line (cm$^{-1}$)", fontsize=14)
ax.tick_params(labelsize=12.5)
fig.subplots_adjust(left=0.1, right=0.965, top=0.98, bottom=0.15)
plt.show()
```

Fig. Measured gaps between neighboring H$^{35}$Cl lines of the band above (dots), with a fit through them (gray). A rigid rotor would put every gap on the dashed line, at the $2\tilde{B}$ found in the example above.

#### Fast rotation stretches the bond

A rapidly spinning molecule stretches, like a mass on a spring swung in a circle. Its moment of inertia grows and its levels fall slightly below $\tilde{B}J(J+1)$:

$$
F(J) = \tilde{B}\,J(J+1) - \tilde{D}\,J^2(J+1)^2, \qquad \tilde{\nu}_J = 2\tilde{B}\,(J+1) - 4\tilde{D}\,(J+1)^3
$$

The **centrifugal distortion constant** $\tilde{D}$ is tiny, about $4\tilde{B}^3/\tilde{\nu}^2$: a stiff bond barely stretches (Problem 7).

| effect | origin | grows with | signature |
| :-- | :-- | :-- | :-- |
| $\tilde{B}_v$ depends on $v$ | the bond is longer on average in higher $v$ | vibrational level $v$ | R lines crowd, P lines spread |
| centrifugal distortion | fast rotation stretches the bond | rotational level $J$ | levels and lines fall slightly at high $J$ |

#### Fitting the real band

Both branches are one formula if we count lines with $m$, where $m = J + 1$ for R($J$) and $m = -J$ for P($J$). With the distortion term,

$$
\tilde{\nu}(m) = \tilde{\nu}_0 + (\tilde{B}_1 + \tilde{B}_0)\,m + (\tilde{B}_1 - \tilde{B}_0)\,m^2 - 4\tilde{D}\,m^3
$$

This is a cubic in $m$, so a polynomial fit to the measured H$^{35}$Cl lines returns the constants:

```{code-cell} python
import numpy as np

m = np.array([-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
nu = np.array([2571.87, 2599.02, 2625.73, 2651.96, 2677.74, 2703.00, 2727.77, 2752.03, 2775.76, 2798.94, 2821.56,
               2843.62, 2865.10, 2906.25, 2925.89, 2944.90, 2963.28, 2980.99, 2998.04, 3014.40, 3030.09, 3045.05,
               3059.32, 3072.85, 3085.64])      # measured line positions, cm^-1

c3, c2, c1, c0 = np.polyfit(m, nu, 3)
print(f"band origin = {c0:.2f}")
print(f"B0 = {(c1 - c2) / 2:.3f},  B1 = {(c1 + c2) / 2:.3f}")
print(f"D  = {-c3 / 4:.1e}")
```

These are the constants this lecture has been quoting: 2885.98, 10.44, 10.14 and $5.3\times10^{-4}$ cm$^{-1}$.

#### Bigger molecules

- Linear molecules (OCS, HCN, CO$_2$) rotate like diatomics, with one moment of inertia and the same $J(J+1)$ ladder. CO$_2$ has no dipole, so it has no microwave spectrum.
- Nonlinear molecules turn about three axes ([Lecture 4.1](01-molecular-degrees-of-freedom.md)), with three moments of inertia. In symmetric tops such as NH$_3$ two of them are equal, and the levels need a second quantum number. Water, with three different moments, has a famously irregular spectrum. These are beyond this course.

### What a real instrument shows

#### Resolution: why CO can look like two humps

HCl's lines are about 21 cm$^{-1}$ apart. CO's are only $2\tilde{B} = 3.8$ cm$^{-1}$ apart, because its moment of inertia is so much larger. An instrument's **resolution** is the smallest gap it can separate, so CO asks for a finer instrument than HCl does.

```{code-cell} python
:tags: [hide-input]
# synced: co_resolution
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
import os
DATA = "data" if os.path.isdir("data") else "ch04/data"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x1, y1 = np.loadtxt(f"{DATA}/co_fine.csv", delimiter=",", unpack=True)
x2, y2 = np.loadtxt(f"{DATA}/co_coarse.csv", delimiter=",", unpack=True)
nu0 = 2143.24
y1 = y1 - np.median(y1[x1 > 2262]); y2 = y2 - np.median(y2[x2 > 2262])
xg = np.arange(x1[0], x1[-1], 0.03)                         # blur the fine trace with a Gaussian of 8 cm^-1 FWHM
s = 8 / 2.3548
t = np.arange(-4 * s, 4 * s, 0.03)
k = np.exp(-(t / s) ** 2 / 2)
y3 = np.convolve(np.interp(xg, x1, y1), k / k.sum(), mode="same")
traces = ((x1, y1, 0.7, "0.25 cm$^{-1}$"), (x2, y2, 1.1, "2 cm$^{-1}$"), (xg, y3, 2.2, "blurred to\n8 cm$^{-1}$"))
fig, axes = plt.subplots(3, 1, figsize=(10, 4.2), sharex=True, gridspec_kw={"hspace": 0.1})
for ax, (x, y, w, lab) in zip(axes, traces):
    ax.plot(x[x < nu0], y[x < nu0] / y.max(), color=TEAL, lw=w)
    ax.plot(x[x > nu0], y[x > nu0] / y.max(), color=ORANGE, lw=w)
    ax.axvline(nu0, color=GRAY, lw=1, ls=(0, (4, 3)))
    ax.text(2262, 0.62, lab, ha="right", va="center", fontsize=16, color="k")
    ax.set_ylim(-0.03, 1.05); ax.set_yticks([]); ax.set_xlim(2020, 2265); ax.spines["left"].set_visible(False)
for ax in axes[:-1]:
    ax.spines["bottom"].set_visible(False); ax.tick_params(bottom=False)
axes[0].text(nu0, 1.07, r"$\tilde{\nu}_0$", ha="center", va="bottom", fontsize=15, color=GRAY)
axes[-1].set_xlabel(r"wavenumber (cm$^{-1}$)", fontsize=14); axes[-1].tick_params(labelsize=12.5)
fig.subplots_adjust(left=0.02, right=0.98, top=0.92, bottom=0.16)
plt.show()
```

Fig. The CO band three ways, each scaled to its tallest point. Top: measured at 0.25 cm$^{-1}$ resolution. Middle: measured at 2 cm$^{-1}$. Bottom: the top trace blurred numerically to about 8 cm$^{-1}$, which resembles a real low-resolution scan. Data: POGIL-PCL meeting, UT Austin [@pogil2018co].

- **Two humps.** With the lines blurred away, only the P and R envelopes remain, with a dip at the band origin where the $\Delta J = 0$ line is missing. Routine scans of gases often look like this.
- **What sets the resolution.** An FTIR spectrometer records the interference of two beams as a mirror moves, and a Fourier transform turns that record into a spectrum. The longest path difference $\Delta d$ sets the resolution, about $1/\Delta d$: 8 cm of path for 0.125 cm$^{-1}$, about 1 mm for 8 cm$^{-1}$. This is the Fourier trade-off of [Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md): a longer record makes a sharper spectrum.
- **The tiny lines.** Most of the small peaks between the big ones in the top trace are $^{13}$C$^{16}$O, about 1% of natural carbon monoxide, with its own band origin at 2096 cm$^{-1}$. It is the isotope of Problem 1.
- **Check the axis.** Instruments often plot wavenumber decreasing from left to right, and transmittance $I/I_0$ instead of absorbance, so that lines point down. Whatever the plot, the R branch is always on the high-wavenumber side of the band origin.

#### One gas cell: stiffness, bond length, mass

Zoomed out, the HCl scan holds more: the cell also contains DCl, and the scan reaches the first overtone of HCl. That $v = 0 \to 2$ band is forbidden for a perfect spring and weakly allowed in a real bond ([Lecture 4.3](03-molecular-vibrations.md)), which is why it is drawn five times larger.

```{code-cell} python
:tags: [hide-input]
# synced: hcl_survey
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
import os
DATA = "data" if os.path.isdir("data") else "ch04/data"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
nu, A = np.loadtxt(f"{DATA}/hcl_survey.csv", delimiter=",", unpack=True)
dcl, hcl, co2, over = (nu > 1880) & (nu < 2260), (nu > 2560) & (nu < 3110), (nu > 2290) & (nu < 2390), (nu > 5400) & (nu < 5900)
rest = ~(dcl | hcl | co2 | over)
fig, ax = plt.subplots(figsize=(11, 3.5))
ax.plot(nu, np.where(rest, A, np.nan), color="#adb5bd", lw=0.7)
ax.plot(nu, np.where(co2, A, np.nan), color=GRAY, lw=0.9)
ax.plot(nu, np.where(dcl, A, np.nan), color=PURPLE, lw=0.9)
ax.plot(nu, np.where(hcl, A, np.nan), color=TEAL, lw=0.9)
ax.plot(nu, np.where(over, 5 * A, np.nan), color=ORANGE, lw=0.9)
ax.text(2070, 0.34, "DCl\n" + r"$v = 0\to 1$", ha="center", va="bottom", fontsize=14, color=PURPLE)
ax.text(3160, 0.70, "HCl\n" + r"$v = 0\to 1$", ha="left", va="center", fontsize=14, color=TEAL)
ax.text(5650, 0.60, "HCl\n" + r"$v = 0\to 2$ ($\times 5$)", ha="center", va="bottom", fontsize=14, color=ORANGE)
ax.text(2360, -0.135, r"CO$_2$", ha="left", va="center", fontsize=13, color=GRAY)
ax.text(3750, -0.11, r"H$_2$O", ha="center", va="center", fontsize=13, color=GRAY)
ax.axhline(0, color="#dee2e6", lw=0.8, zorder=0)
ax.set_xlim(1850, 6050); ax.set_ylim(-0.2, 1.0)
ax.set_xlabel(r"wavenumber (cm$^{-1}$)", fontsize=14); ax.set_ylabel("absorbance", fontsize=14)
ax.tick_params(labelsize=12.5)
fig.subplots_adjust(left=0.08, right=0.99, top=0.97, bottom=0.18)
plt.show()
```

Fig. The whole measured scan. DCl $v = 0 \to 1$ (purple), HCl $v = 0 \to 1$ (teal), and HCl $v = 0 \to 2$ drawn five times larger (orange). The small downward features (gray) are CO$_2$ and water in the room air: the reference scan happened to see a little more of them than the sample scan did.

Fitting each band as above gives:

| from this one scan | what it gives | |
| :-- | :-- | :-- |
| HCl band origins 2885.95 ($v = 0 \to 1$) and 5667.96 ($v = 0 \to 2$) | $\tilde{\nu}_e = 2989.9$ and $\tilde{\nu}_ex_e = 51.97$ cm$^{-1}$, so $k = 516$ N/m | [Lecture 4.3](03-molecular-vibrations.md) |
| $\tilde{B}_0, \tilde{B}_1, \tilde{B}_2 = 10.440, 10.137, 9.834$ cm$^{-1}$ | evenly spaced, so $\alpha_e = 0.303$, $\tilde{B}_e = 10.59$ cm$^{-1}$ and $R_e = 127.5$ pm | this lecture |
| DCl band origin 2091.05, $\tilde{B}_0 = 5.392$ cm$^{-1}$ | the same bond with a heavier mass (Problem 5) | [Lecture 4.3](03-molecular-vibrations.md), this lecture |
| line pairs about 2.1 cm$^{-1}$ apart | chlorine's two isotopes | this lecture |

One gas cell and one scan measure a bond length to a part in a thousand, the stiffness of the bond and how far it departs from a parabola.

### Problems

#### Problem 1: Carbon-13

The $J = 0 \to 1$ line of $^{12}$C$^{16}$O is at 115.271 GHz. Predict the line of $^{13}$C$^{16}$O, assuming the same bond length, and compare with the measured 110.201 GHz. Why are such isotope lines useful to astronomers?

:::{admonition} **Solution**
:class: dropdown solution

The bond length, and so $R_e$, does not change; only $\mu$ does, and $\tilde{B} \propto 1/I \propto 1/\mu$:

$$
\mu(^{12}\text{C}^{16}\text{O}) = \frac{(12.000)(15.995)}{27.995} = 6.856\ \text{u}, \qquad \mu(^{13}\text{C}^{16}\text{O}) = \frac{(13.003)(15.995)}{28.998} = 7.172\ \text{u}
$$

$$
\nu(^{13}\text{CO}) = 115.271\ \text{GHz}\times\frac{6.856}{7.172} = 110.19\ \text{GHz}
$$

The measured line is at 110.201 GHz, within 0.01%; the small difference comes from vibrational averaging, which also differs slightly between the isotopes. Each isotopologue has its own lines, so astronomers can count $^{13}$CO separately from $^{12}$CO. The main CO line is often so strong that it saturates, while the rarer $^{13}$CO line still reports how much gas there is.
:::

#### Problem 2: Which molecules have microwave spectra?

Which of these have a pure rotational spectrum: HBr, Cl$_2$, CO$_2$, OCS, H$_2$O, CH$_4$, N$_2$O, CH$_3$Cl? Explain each answer in one line.

#### Problem 3: The most populated level

Treating $J$ as continuous, show that $(2J+1)\,e^{-hc\tilde{B}J(J+1)/k_BT}$ is largest at

$$
J_{\max} = \sqrt{\frac{k_BT}{2hc\tilde{B}}} - \frac{1}{2}
$$

Evaluate it for HCl ($\tilde{B} = 10.44$ cm$^{-1}$) and CO ($\tilde{B} = 1.92$ cm$^{-1}$) at 300 K, and for HCl at 1000 K.

:::{admonition} **Solution**
:class: dropdown solution

Write $a = hc\tilde{B}/k_BT$ and differentiate:

$$
\frac{d}{dJ}\left[(2J+1)\,e^{-aJ(J+1)}\right] = \left[2 - a\,(2J+1)^2\right]e^{-aJ(J+1)} = 0 \quad\Longrightarrow\quad 2J + 1 = \sqrt{\frac{2}{a}}
$$

which gives $J_{\max} = \sqrt{k_BT/2hc\tilde{B}} - \frac{1}{2}$. With $k_BT/hc = 208.5$ cm$^{-1}$ at 300 K:

- HCl, 300 K: $\sqrt{208.5/20.88} - 0.5 = 3.16 - 0.5 = 2.7$, so the most populated level is $J = 3$.
- CO, 300 K: $\sqrt{208.5/3.84} - 0.5 = 7.4 - 0.5 = 6.9$, so $J = 7$.
- HCl, 1000 K: $k_BT/hc = 695$ cm$^{-1}$, $\sqrt{695/20.88} - 0.5 = 5.8 - 0.5 = 5.3$, so $J = 5$.

Heating or a smaller $\tilde{B}$ moves the peak up, but only as a square root.
:::

#### Problem 4: A thermometer in space

In a cold interstellar cloud, CO is at 10 K. Find $N_1/N_0$ and $N_2/N_0$. Why can the ratio of the $1 \to 2$ and $0 \to 1$ line strengths serve as a thermometer, and why would a hydride like HCl be a poor one at this temperature?

#### Problem 5: Deuterium chloride

From the HCl constants of [Lecture 4.3](03-molecular-vibrations.md) (band origin 2886 cm$^{-1}$, $\tilde{\nu}_e = 2990$ and $\tilde{\nu}_ex_e = 52$ cm$^{-1}$) and $\tilde{B}_e = 10.59$ cm$^{-1}$, predict $\tilde{B}_e$ and the band origin of D$^{35}$Cl. The measured values are 5.45 and 2091 cm$^{-1}$.

:::{admonition} **Solution**
:class: dropdown solution

Deuterium leaves the bond (its potential) unchanged and only raises the reduced mass:

$$
\mu(\text{HCl}) = 0.9796\ \text{u}, \qquad \mu(\text{DCl}) = \frac{(2.0141)(34.9689)}{36.9830} = 1.9044\ \text{u}, \qquad \frac{\mu_{\text{HCl}}}{\mu_{\text{DCl}}} = 0.5144
$$

**Rotation.** $\tilde{B} \propto 1/\mu$: $\tilde{B}_e(\text{DCl}) = 10.59\times0.5144 = 5.45$ cm$^{-1}$, as measured.

**Vibration, first try.** Scaling the band origin by $\sqrt{\mu_{\text{HCl}}/\mu_{\text{DCl}}} = 0.7172$ gives $2886\times0.7172 = 2070$ cm$^{-1}$, 1% low.

**Vibration, with anharmonicity.** The band origin is $\tilde{\nu}_e - 2\tilde{\nu}_ex_e$ ([Lecture 4.3](03-molecular-vibrations.md)), and the two terms scale differently: $\tilde{\nu}_e \propto \mu^{-1/2}$ and $\tilde{\nu}_ex_e \propto \mu^{-1}$. So

$$
\tilde{\nu}_e = 2990\times0.7172 = 2144, \qquad \tilde{\nu}_ex_e = 52\times0.5144 = 26.7, \qquad \tilde{\nu}_0 = 2144 - 2(26.7) = 2091\ \text{cm}^{-1}
$$

in agreement with the measurement. The heavier isotope sits lower in the same well, where the well is more nearly parabolic.
:::

#### Problem 6: The microwave oven

A microwave oven runs at 2.45 GHz. Convert this to cm$^{-1}$ and compare with the lowest rotational absorption of water vapor, near 557 GHz. Does the oven drive a rotational transition of water? What do you think heats the food?

#### Problem 7: Centrifugal distortion in HCl

Estimate $\tilde{D} \approx 4\tilde{B}^3/\tilde{\nu}^2$ for HCl ($\tilde{B} = 10.59$, $\tilde{\nu}_e = 2990$ cm$^{-1}$). How much does it lower the level $J = 20$, and the line $J = 20 \to 21$, compared with the rigid rotor?

:::{admonition} **Solution**
:class: dropdown solution

$$
\tilde{D} \approx \frac{4\,(10.59)^3}{(2990)^2} = \frac{4750}{8.94\times10^{6}} = 5.3\times10^{-4}\ \text{cm}^{-1}
$$

(the measured value is $5.3\times10^{-4}$ cm$^{-1}$). For $J = 20$:

$$
\tilde{B}J(J+1) = 10.59\times420 = 4448\ \text{cm}^{-1}, \qquad \tilde{D}J^2(J+1)^2 = 5.3\times10^{-4}\times420^2 = 94\ \text{cm}^{-1}
$$

so the level sits 2% below the rigid rotor. The line $20 \to 21$ moves by $4\tilde{D}(J+1)^3 = 4\times5.3\times10^{-4}\times21^3 = 19.6$ cm$^{-1}$, out of $2\tilde{B}(J+1) = 445$ cm$^{-1}$, so it is 4.4% low. The correction grows as $J^4$ in the levels and $J^3$ in the lines: negligible for the strong low-$J$ lines, important for hot gases.
:::

#### Problem 8: How fast does a molecule spin?

Treat HCl in the level $J = 10$ classically, with $L = \sqrt{J(J+1)}\,\hbar$ and $L = I\omega$. How many turns per second does it make? Compare with its vibrational frequency, $8.65\times10^{13}$ Hz. Does the bond have time to vibrate during one turn?
