---
kernelspec:
  name: python3
  display_name: Python 3
---

# Electron Spin

:::{note} **What you need to know**

- A charge that circulates is a magnet. An electron with orbital angular momentum $\vec{L}$ has a **magnetic moment** $\vec{\mu} = -(e/2m_e)\,\vec{L}$, so $\mu_z = -\mu_Bm_l$ with the **Bohr magneton** $\mu_B = e\hbar/2m_e = 5.79\times10^{-5}$ eV/T. A magnetic field $B$ along $z$ shifts each state by $\mu_BB\,m_l$ and splits a level into $2l + 1$: the **Zeeman effect**.
- **Stern and Gerlach** sent silver atoms through a non-uniform magnetic field, which sorts atoms by $\mu_z$. Silver's outer electron has $l = 0$, so one undeflected spot was expected. The beam split in **two**.
- The electron carries an angular momentum of its own, **spin**, with $s = \frac{1}{2}$. It has two states, $\alpha$ ($m_s = +\frac{1}{2}$) and $\beta$ ($m_s = -\frac{1}{2}$), with $S_z = \pm\frac{1}{2}\hbar$ and length $\frac{\sqrt{3}}{2}\hbar$. Spin obeys the commutators of $\hat{\vec{L}}$ but is not a motion in space: its states are two-component vectors and its operators $2\times2$ matrices, the smallest quantum system there is.
- The spin magnetic moment is $\mu_z = -g_e\mu_Bm_s$ with $g_e = 2.0023$, twice as magnetic as orbital motion. In a field the two spin states lie $g_e\mu_BB$ apart, the basis of EPR (electrons, GHz) and NMR (nuclei, MHz).
- With spin, a hydrogen state has four quantum numbers, $n$, $l$, $m_l$, $m_s$, and level $n$ holds $2n^2$ states. **Spin-orbit coupling**, $A\,\hat{\vec{L}}\cdot\hat{\vec{S}}/\hbar^2$, ties the two angular momenta together: only the **total** $\hat{\vec{J}} = \hat{\vec{L}} + \hat{\vec{S}}$ stays sharp, with $j = l \pm \frac{1}{2}$, and every level with $l > 0$ splits in two (**fine structure**), named by term symbols such as $^2P_{3/2}$. Sodium's yellow line is a doublet for this reason. Light drives transitions with $\Delta l = \pm1$ and $\Delta m_s = 0$.

:::

### A moving charge is a magnet

The Schrödinger equation of Lectures [5.1](01-hydrogenlike-atoms.md) and [5.2](02-atomic-orbitals.md) treated the electron as a charged point mass. This lecture adds magnetism: first the magnetism of the electron's orbital motion, which that equation already contains, and then a second kind, which it does not.

Three symbols change their meaning for this lecture. $\mu$ is a **magnetic moment** (the reduced mass does not appear; the electron mass $m_e$ stands in for it, a 0.05% difference in hydrogen). $B$ is the strength of a **magnetic field** in tesla. And the quantum number $m$ of Lectures 4.4 to 5.2 is written $m_l$ from here on, because a second $m$ is coming.

#### A loop of current

Take the model system of [Lecture 4.4](../ch04/04-angular-momentum.md): a particle of mass $m$ and charge $q$ moving at speed $v$ on a circle of radius $r$. It passes any point of the circle once per period $T = 2\pi r/v$, so it is an electric current. A loop of current $I$ around an area is a magnet, and the strength of the magnet, its **magnetic moment**, is the current times the area:

$$
\begin{aligned}
I &= \frac{q}{T} = \frac{qv}{2\pi r} && \text{charge passing per unit time}\\[4pt]
\mu &= I\cdot\pi r^2 = \frac{qvr}{2} && \text{current times area}\\[4pt]
&= \frac{q}{2m}\,(mvr) = \frac{q}{2m}\,L && L = mvr \text{ on a circle (Lecture 4.4)}
\end{aligned}
$$

The moment is a vector along the axis of the loop, like $\vec{L}$. For a positive charge the two are parallel. The electron's charge is $q = -e$, so its moment points against its angular momentum:

$$
\vec{\mu} = -\frac{e}{2m_e}\,\vec{L}
$$

```{code-cell} python
:tags: [hide-input]
# synced: current_loop
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. An electron on a circular orbit. Its angular momentum $\vec{L}$ points up. The current $I$ runs against the motion because the charge is negative, so the magnetic moment $\vec{\mu}$ points down. Gray: the magnetic field lines of the loop.

- **The orbit has dropped out.** Neither $r$ nor $v$ survives: $\mu/L = q/2m$ for any orbit. The ratio is called the **magnetogyric ratio** $\gamma$, and for an orbiting electron $\gamma = -e/2m_e$.
- **The loop is a bar magnet.** Its field lines leave one face and return to the other, with the north pole on the side $\vec{\mu}$ points to.
- **Light particles are strong magnets**, since $\gamma \propto 1/m$. A proton with the same angular momentum is 1836 times less magnetic.

#### A magnet in a field

A magnet in a magnetic field $\vec{B}$ has the energy

$$
E = -\vec{\mu}\cdot\vec{B} = -\mu_zB \qquad (\vec{B} \text{ along } z)
$$

lowest when the moment points along the field, as a compass needle does. What the field does to the magnet depends on whether the field is the same everywhere:

```{code-cell} python
:tags: [hide-input]
# synced: gradient_force
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. A small magnet (red arrow: its moment, from the S pole to the N pole) in a field that points up. The field pushes the N pole along $\vec{B}$ and the S pole against it (gray arrows). Left: in a uniform field the two forces cancel. Right: between a sharp edge and a groove the field is stronger at the bottom, the two forces differ, and a net force $\vec{F}$ remains.

- **Uniform field: a twist, no push.** The forces on the two poles are equal and opposite. They turn a tilted magnet but do not move it.
- **Non-uniform field: a net force.** The pole in the stronger field is pushed harder. Since $E = -\mu_zB$ and force is minus the slope of the energy,

$$
F_z = -\frac{\partial E}{\partial z} = \mu_z\,\frac{\partial B}{\partial z}
$$

- **The force sorts magnets by $\mu_z$.** A moment along the field is pulled toward the stronger field, a moment against the field is pushed away from it, and a moment at right angles feels nothing. This is the idea of the Stern-Gerlach experiment below.

### An atom in a magnetic field

#### The orbital magnetic moment is quantized

The classical relation becomes an operator relation, $\hat{\mu}_z = -(e/2m_e)\,\hat{L}_z$, and the hydrogen states are eigenfunctions of $\hat{L}_z$ with eigenvalues $m_l\hbar$ ([Lecture 4.4](../ch04/04-angular-momentum.md)):

:::{important} **The orbital magnetic moment**

$$
\hat{\vec{\mu}} = -\frac{e}{2m_e}\,\hat{\vec{L}}, \qquad \mu_z = -\frac{e\hbar}{2m_e}\,m_l = -\mu_B\,m_l, \qquad m_l = -l, \dots, l
$$

$$
\mu_B = \frac{e\hbar}{2m_e} = 9.274\times10^{-24}\ \text{J/T}
$$

- $\mu_B$ is the **Bohr magneton**, the magnetic moment that goes with one $\hbar$ of orbital angular momentum: the natural unit for the magnetism of electrons
- $\mu_z$ takes $2l + 1$ values. An s electron ($l = 0$) has no orbital moment at all
:::

The Bohr magneton in the units a chemist meets, for a field of one tesla (the Earth's field is $5\times10^{-5}$ T, a refrigerator magnet about $10^{-2}$ T, an NMR magnet 10 to 20 T):

| $\mu_B$ as | value | what it sets |
| :-- | :-- | :-- |
| an energy per tesla | $5.788\times10^{-5}$ eV/T | the shift of a level: 58 $\mu$eV in 1 T, against gaps of several eV between levels |
| a wavenumber per tesla, $\mu_B/hc$ | 0.467 cm$^{-1}$/T | the shift of a spectral line |
| a frequency per tesla, $\mu_B/h$ | 14.0 GHz/T | the frequency of a photon that connects two neighbouring magnetic levels |
| a temperature per tesla, $\mu_B/k_B$ | 0.67 K/T | the temperature below which a 1 T field lines up the moments |

#### The Hamiltonian and its levels

A field along $z$ adds the energy $-\hat{\mu}_zB$ to the hydrogen Hamiltonian $\hat{H}_0$ of Lecture 5.1:

$$
\hat{H} = \hat{H}_0 + \frac{\mu_BB}{\hbar}\,\hat{L}_z
$$

There is no new equation to solve. $\hat{L}_z$ commutes with $\hat{H}_0$, so the states $\psi_{nlm_l}$ are eigenfunctions of both ([Lecture 3.5b](../ch03/05-hermitian-operators-and-commutators.md)), and therefore of their sum:

$$
\hat{H}\,\psi_{nlm_l} = \left(E_n + \mu_BB\,m_l\right)\psi_{nlm_l}
$$

:::{important} **A hydrogenlike atom in a magnetic field (orbital motion only)**

$$
\hat{H} = \hat{H}_0 + \frac{\mu_BB}{\hbar}\,\hat{L}_z, \qquad E_{nm_l} = E_n + \mu_BB\,m_l
$$

- The states do not change. The field shifts each one in proportion to its $m_l$, which is why $m_l$ is called the **magnetic quantum number**
- A level of angular momentum $l$ splits into $2l + 1$ equally spaced levels, $\mu_BB$ apart
- In [Lecture 5.2](02-atomic-orbitals.md) the $z$ axis was our choice, and the atom could not tell. A field along $z$ makes the direction matter: it gives each $m_l$ its own energy, so the states of definite $m_l$ stay stationary, while $p_x$ and $p_y$, which mix $m_l = +1$ and $-1$, no longer are
:::

#### The Zeeman effect

```{code-cell} python
:tags: [hide-input]
# synced: zeeman_orbital
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Left: in a magnetic field the 2p level splits into three levels $\mu_BB$ apart, and 1s does not move. The arrows are the three allowed transitions. Right: one spectral line becomes three.

- **One line becomes three.** The line at $\nu_0$ gains two companions at $\nu_0 \pm \mu_BB/h$. Pieter Zeeman saw spectral lines widen in a magnetic field in 1896, and Hendrik Lorentz explained the triplet.
- **Three, whatever $l$.** Light changes $m_l$ by 0 or $\pm1$ (the selection rules at the end of this lecture), and every level has the same spacing $\mu_BB$. So $3\text{d} \to 2\text{p}$, with five levels above and three below, still gives the same three frequencies. This is the **normal Zeeman effect**.
- **The splitting is small.** At 1 T it is $5.8\times10^{-5}$ eV, against 10.2 eV for the line itself: six parts in a million.
- **Most atoms do not obey.** The triplet is seen only for certain lines. Sodium's yellow line, and hydrogen's own lines in a weak field, split into four, six or more components with unequal spacings. This **anomalous Zeeman effect** had no explanation for a quarter of a century. What was missing is the subject of the rest of this lecture.

:::{note} **Example: how far apart are the Zeeman lines?**

The red line of cadmium at 643.85 nm shows the normal triplet. How far from the center are its outer components in a field of 1.0 T?

Each outer component is shifted by

$$
\Delta\tilde{\nu} = \frac{\mu_BB}{hc} = 0.467\ \text{cm}^{-1}
$$

The line itself is at $\tilde{\nu}_0 = 1/\lambda = 15\,532$ cm$^{-1}$, so the shift is 3 parts in $10^5$. In wavelength, from $\lambda = 1/\tilde{\nu}$,

$$
\lvert\Delta\lambda\rvert = \lambda^2\,\Delta\tilde{\nu} = (643.85\times10^{-7}\ \text{cm})^2\times0.467\ \text{cm}^{-1} = 0.019\ \text{nm}
$$

Separating lines 0.02 nm apart at 644 nm takes a resolving power $\lambda/\Delta\lambda$ of about 30 000, ten times finer than the hydrogen and deuterium pair of Lecture 5.1. Zeeman's first observation was only a broadening of the line.
:::

### The Stern-Gerlach experiment

In 1922 Otto Stern and Walther Gerlach measured the magnetic moment of single atoms with the force of the last section. They evaporated silver in an oven, cut a narrow beam of atoms out of the vapor with slits, sent it between the poles of a magnet shaped to make the field strongly non-uniform (a sharp edge facing a groove), and let the atoms land on a glass plate.

```{code-cell} python
:tags: [hide-input]
# synced: stern_gerlach
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Atoms from the oven fly through a non-uniform magnetic field and land on a plate. Each atom is pushed up or down by a force proportional to its $\mu_z$. The beam splits in two.

- **The apparatus measures $\mu_z$, one atom at a time.** The force $F_z = \mu_z\,\partial B/\partial z$ turns a value of $\mu_z$ into a position on the plate.
- **The atom is neutral.** A magnetic field bends the path of a moving charge, which would swamp the effect. A neutral atom feels only the push on its moment.

What should the plate show?

```{code-cell} python
:tags: [hide-input]
# synced: sg_screens
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. What the plate would show for classical magnets, for atoms with $l = 0$ and for atoms with $l = 1$, and what Stern and Gerlach found for silver.

- **Classical magnets** leave the oven pointing in every direction. $\mu_z$ takes every value from $-\mu$ to $+\mu$, and the beam smears into a band.
- **Orbital angular momentum** gives $\mu_z = -\mu_Bm_l$ with $2l + 1$ values, an **odd** number of spots: one for $l = 0$, three for $l = 1$.
- **Silver** has one electron outside closed shells, in the 5s orbital, and closed shells carry no angular momentum ([Chapter 7](../ch07/01-multi-electron-atoms.md)). So $l = 0$, and the prediction is a single spot in the middle.
- **Observed: two spots, and nothing in the middle.** Two means $2l + 1 = 2$, that is $l = \frac{1}{2}$, which no orbital motion can have: $l$ is a whole number because $e^{im\phi}$ must join up around the circle (Lecture 4.4). The moment that splits the beam is not orbital. Hydrogen atoms in their 1s ground state split in two as well (Phipps and Taylor, 1927).

:::{note} **Example: how far apart are the two spots?**

Silver atoms (mass 107.9 u) leave a 1300 K oven at about 550 m/s and cross a magnet 3.5 cm long in which the field changes by 10 T per centimeter. Each atom carries $\mu_z = \pm\mu_B$ (shown below). How far sideways has it moved at the end of the magnet?

The force is tiny, but so is the mass:

$$
F = \mu_B\,\frac{\partial B}{\partial z} = 9.27\times10^{-24}\ \text{J/T}\times1000\ \text{T/m} = 9.3\times10^{-21}\ \text{N}
$$

$$
a = \frac{F}{m} = \frac{9.3\times10^{-21}\ \text{N}}{1.79\times10^{-25}\ \text{kg}} = 5.2\times10^{4}\ \text{m/s}^2
$$

The atom spends $t = 0.035\ \text{m}/550\ \text{m/s} = 6.4\times10^{-5}$ s in the magnet, and moves

$$
z = \tfrac{1}{2}at^2 = \tfrac{1}{2}\times5.2\times10^{4}\times(6.4\times10^{-5})^2\ \text{m} = 0.10\ \text{mm}
$$

The two beams end up 0.2 mm apart, which is what Stern and Gerlach saw under a microscope.
:::

:::{tip} **Watch: the experiment and what it means**
:class: dropdown

<iframe width="560" height="315" src="https://www.youtube.com/embed/lYl6uLNT9vc?si=gt23V57CrLDIuFVF" title="Electron spin and the Stern-Gerlach experiment" frameborder="0" allowfullscreen>
</iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/cd2Ua9dKEl8?si=cdao304sDoR4_SfZ" title="What is spin?" frameborder="0" allowfullscreen>
</iframe>
:::

### Spin

#### A new angular momentum

Two spots mean a magnetic moment with two values of $\mu_z$. In 1925 George Uhlenbeck and Samuel Goudsmit proposed, to explain doubled lines in atomic spectra, that the electron carries an angular momentum of its own in addition to the orbital one. It is called **spin**. Count its states as for any angular momentum, $2s + 1 = 2$:

$$
s = \tfrac{1}{2}, \qquad m_s = +\tfrac{1}{2} \ \text{ or } \ -\tfrac{1}{2}
$$

The spin operators $\hat{S}_x$, $\hat{S}_y$, $\hat{S}_z$ are defined by obeying the commutation rules of angular momentum,

$$
[\hat{S}_x, \hat{S}_y] = i\hbar\,\hat{S}_z, \qquad [\hat{S}_y, \hat{S}_z] = i\hbar\,\hat{S}_x, \qquad [\hat{S}_z, \hat{S}_x] = i\hbar\,\hat{S}_y
$$

and everything that Lecture 4.4 drew from the commutators alone carries over: $\hat{S}^2 = \hat{S}_x^2 + \hat{S}_y^2 + \hat{S}_z^2$ and one component can be sharp together, with eigenvalues $s(s+1)\hbar^2$ and $m_s\hbar$. The ladder argument of that lecture (its "Going further" box) allowed ladders with half-integer $l$. Orbital motion cannot use them. Spin does.

:::{important} **Electron spin**

$$
\hat{S}^2\alpha = \tfrac{3}{4}\hbar^2\,\alpha, \qquad \hat{S}_z\alpha = +\tfrac{1}{2}\hbar\,\alpha
$$

$$
\hat{S}^2\beta = \tfrac{3}{4}\hbar^2\,\beta, \qquad \hat{S}_z\beta = -\tfrac{1}{2}\hbar\,\beta
$$

$$
\langle\alpha|\alpha\rangle = \langle\beta|\beta\rangle = 1, \qquad \langle\alpha|\beta\rangle = 0
$$

- $s = \frac{1}{2}$ for every electron, so $\hat{S}^2$ always gives $s(s+1)\hbar^2 = \frac{3}{4}\hbar^2$: a spin of length $\frac{\sqrt{3}}{2}\hbar$
- Two states: $\alpha$, "spin up", with $m_s = +\frac{1}{2}$, and $\beta$, "spin down", with $m_s = -\frac{1}{2}$
- They are orthonormal, as eigenstates of a Hermitian operator with different eigenvalues must be
:::

- **Spin is intrinsic.** Every electron has $s = \frac{1}{2}$, as every electron has the charge $-e$ and the mass $m_e$. The orbital quantum number $l$ depends on the state the electron is in; $s$ cannot be changed. Only the orientation $m_s$ can.
- **Spin is not a motion in space.** $\alpha$ and $\beta$ are not functions of $x$, $y$, $z$ or of the angles. There is no $Y_{1/2}^{m}(\theta, \phi)$: a function of $\phi$ with $m = \frac{1}{2}$ would change sign after one full turn. The name is historical.
- **The Schrödinger equation does not contain it.** Our Hamiltonians were built by taking a classical energy and replacing $x$ and $p$ by operators, and spin has no classical energy to start from. It comes out on its own from Dirac's relativistic equation for the electron (1928). Here it is added by hand, as a new degree of freedom with the properties in the box.
- **Other particles have spin too.** Protons and neutrons have $s = \frac{1}{2}$, the photon has $s = 1$, and nuclei have spins $0, \frac{1}{2}, 1, \frac{3}{2}, \dots$ Particles with half-integer spin are **fermions** and those with whole spin are **bosons**. That distinction is behind the Pauli principle and the periodic table ([Chapter 7](../ch07/01-multi-electron-atoms.md)).

#### The vector model

Spin follows the rules that Lecture 4.4 found for $\vec{L}$, with $s$ in place of $l$ and $m_s$ in place of $m_l$. Draw the two side by side:

```{code-cell} python
:tags: [hide-input]
# synced: spin_cones
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The vector model for orbital angular momentum with $l = 1$ (left, three cones) and for spin (right, two cones), drawn on the same scale. Each arrow has a sharp length and a sharp height along $z$.

| | length | height along $z$ | how many states |
| :-- | :-- | :-- | :-: |
| orbital, $l = 1$ | $\sqrt{l(l+1)}\,\hbar = \sqrt{2}\,\hbar$ | $m_l\hbar = +\hbar,\ 0,\ -\hbar$ | $2l + 1 = 3$ |
| spin, $s = \frac{1}{2}$ | $\sqrt{s(s+1)}\,\hbar = \frac{\sqrt{3}}{2}\hbar$ | $m_s\hbar = +\frac{1}{2}\hbar,\ -\frac{1}{2}\hbar$ | $2s + 1 = 2$ |

- **Two things are sharp, as for $\vec{L}$:** the length and one component. Where the arrow sits on its cone is not defined, because $\hat{S}_x$ and $\hat{S}_y$ do not commute with $\hat{S}_z$.
- **"Spin up" is far from straight up.** The angle from the $z$ axis has $\cos\theta = \frac{1}{2}\big/\frac{\sqrt{3}}{2} = 1/\sqrt{3}$, so $\theta = 54.7°$: the magic angle of Problem 6 of Lecture 4.4, and of the nodal cones of $d_{z^2}$ in Lecture 5.2.
- **The rest is in $S_x$ and $S_y$:** $\langle S_x^2\rangle = \langle S_y^2\rangle = \frac{1}{2}\left(\frac{3}{4} - \frac{1}{4}\right)\hbar^2 = \frac{1}{4}\hbar^2$, with $\langle S_x\rangle = \langle S_y\rangle = 0$.

:::{note} **Example: is the electron a spinning ball?**

Suppose the electron were a solid ball of radius $r = 2.8\times10^{-15}$ m (the "classical electron radius") turning about its axis with angular momentum $\frac{1}{2}\hbar$. How fast would its equator move?

A solid sphere has $I = \frac{2}{5}m_er^2$, so $L = I\omega = \frac{2}{5}m_er\,v$ with $v = \omega r$ the speed at the equator:

$$
v = \frac{5L}{2m_er} = \frac{5\hbar}{4m_er} = \frac{5\times1.055\times10^{-34}}{4\times9.11\times10^{-31}\times2.8\times10^{-15}}\ \frac{\text{m}}{\text{s}}
$$

$$
v = 5.2\times10^{10}\ \text{m/s} \approx 170\,c
$$

Faster than light, 170 times over. Scattering experiments show that the electron is smaller than $10^{-18}$ m, which makes it thousands of times worse. Nothing is rotating. Spin is angular momentum, and it adds to $\vec{L}$ in the conservation law (below), but it is not the rotation of anything.
:::

#### Spin states are two-component vectors

How should a spin state be written down? An orbital is a function of $r$, $\theta$, $\phi$, but spin has no coordinate to plot against. Three steps lead to the answer:

1. **Two readings, two eigenstates.** A measurement of $S_z$ has two outcomes, so $\hat{S}_z$ has two eigenstates, $\alpha$ and $\beta$, and they are orthonormal (the box above).
2. **Every spin state is a superposition of the two.** The eigenstates of an observable are a complete set of axes ([Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md)), so any spin state is $\chi = c_\alpha\,\alpha + c_\beta\,\beta$, with $c_\alpha = \langle\alpha|\chi\rangle$ and $c_\beta = \langle\beta|\chi\rangle$.
3. **Two numbers make a column.** In [Lecture 3.5](../ch03/04-operators.md) a wavefunction became a long column of its values on a grid. A spin state needs two entries, $c_\alpha$ on top and $c_\beta$ below. The state $\alpha$ itself has $c_\alpha = 1$ and $c_\beta = 0$:

$$
\chi = c_\alpha\,\alpha + c_\beta\,\beta = \begin{pmatrix}c_\alpha\\ c_\beta\end{pmatrix} \qquad\Longrightarrow\qquad \alpha = \begin{pmatrix}1\\ 0\end{pmatrix}, \qquad \beta = \begin{pmatrix}0\\ 1\end{pmatrix}
$$

$$
\lvert c_\alpha\rvert^2 + \lvert c_\beta\rvert^2 = 1
$$

With only two components, spin is the simplest quantum system there is, and Lectures 3.5 and 3.6 apply to it in full with nothing larger than a $2\times2$ matrix.

- **The bracket is a dot product,** row times column with the bra's components conjugated: $\langle\alpha|\beta\rangle = 1\cdot0 + 0\cdot1 = 0$. There is no integral, because there is no coordinate. (Some books write a formal integral over a "spin variable", and the states as $\psi_{+1/2}$ and $\psi_{-1/2}$. They mean this two-term sum.)
- **The Born rule** of Lecture 3.6: a measurement of $S_z$ gives $+\frac{1}{2}\hbar$ with probability $\lvert c_\alpha\rvert^2$ and $-\frac{1}{2}\hbar$ with probability $\lvert c_\beta\rvert^2$.

#### Spin operators are $2\times2$ matrices

If a state is a column of two numbers, an operator that turns one state into another is a $2\times2$ matrix (Lecture 3.5). The matrix of $\hat{S}_z$ needs no calculation: $\alpha$ and $\beta$ are its eigenvectors, and a matrix written in the basis of its own eigenvectors is diagonal, with the eigenvalues on the diagonal:

$$
\hat{S}_z = \frac{\hbar}{2}\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}
$$

The other two components are not diagonal in this basis. Together the three are $\frac{1}{2}\hbar$ times the **Pauli matrices**:

$$
\hat{S}_x = \frac{\hbar}{2}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}, \qquad \hat{S}_y = \frac{\hbar}{2}\begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}, \qquad \hat{S}_z = \frac{\hbar}{2}\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}
$$

:::{note} **Example: $\hat{S}_z$ and $\hat{S}_x$ acting on $\alpha$ and $\beta$**

Multiply each matrix into the columns, row times column.

$$
\hat{S}_z\,\alpha = \frac{\hbar}{2}\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}1\\ 0\end{pmatrix} = \frac{\hbar}{2}\begin{pmatrix}1\cdot1 + 0\cdot0\\ 0\cdot1 - 1\cdot0\end{pmatrix} = \frac{\hbar}{2}\begin{pmatrix}1\\ 0\end{pmatrix} = +\tfrac{1}{2}\hbar\,\alpha
$$

$$
\hat{S}_z\,\beta = \frac{\hbar}{2}\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}0\\ 1\end{pmatrix} = \frac{\hbar}{2}\begin{pmatrix}0\\ -1\end{pmatrix} = -\tfrac{1}{2}\hbar\,\beta
$$

The matrix gives back the two eigenvalue equations the lecture started from. Now the same with $\hat{S}_x$:

$$
\hat{S}_x\,\alpha = \frac{\hbar}{2}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}\begin{pmatrix}1\\ 0\end{pmatrix} = \frac{\hbar}{2}\begin{pmatrix}0\\ 1\end{pmatrix} = \tfrac{1}{2}\hbar\,\beta
$$

Not a multiple of $\alpha$: $\hat{S}_x$ turns spin up into spin down, so $\alpha$ is not an eigenvector of $\hat{S}_x$.
:::

- **$\hat{S}_z$ is diagonal** because $\alpha$ and $\beta$, its own eigenvectors, are the basis. Its eigenvalues $\pm\frac{1}{2}\hbar$ sit on the diagonal (Lecture 3.5).
- **$\hat{S}_x$ flips the spin.** Row times column gives $\hat{S}_x\alpha = \frac{1}{2}\hbar\,\beta$ and $\hat{S}_x\beta = \frac{1}{2}\hbar\,\alpha$. So $\alpha$ is not an eigenvector of $\hat{S}_x$: when $S_z$ is sharp, $S_x$ is not.
- **Each matrix is Hermitian,** equal to its own conjugate transpose, which is why $\hat{S}_y$ needs its two $i$'s, as momentum did in Lecture 3.5b. Each has the eigenvalues $\pm\frac{1}{2}\hbar$: whatever axis the spin is measured along, the reading is $+\frac{1}{2}\hbar$ or $-\frac{1}{2}\hbar$.
- **The square of each matrix is $\frac{1}{4}\hbar^2$ times the unit matrix,** so $\hat{S}^2 = \frac{3}{4}\hbar^2$ times the unit matrix: every spin state is an eigenstate of $\hat{S}^2$, as the box says.

| operator | acting on $\alpha$ | acting on $\beta$ |
| :-: | :-: | :-: |
| $\hat{S}_z$ | $+\frac{1}{2}\hbar\,\alpha$ | $-\frac{1}{2}\hbar\,\beta$ |
| $\hat{S}_x$ | $\frac{1}{2}\hbar\,\beta$ | $\frac{1}{2}\hbar\,\alpha$ |
| $\hat{S}_y$ | $\frac{i}{2}\hbar\,\beta$ | $-\frac{i}{2}\hbar\,\alpha$ |

The same checks in numpy, in units of $\hbar$:

```{code-cell} python
import numpy as np

# spin matrices in the basis (alpha, beta)
Sx = 0.5 * np.array([[0, 1], [1, 0]])
Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
Sz = 0.5 * np.array([[1, 0], [0, -1]])

print("Sx Sy - Sy Sx = i Sz ?", np.allclose(Sx @ Sy - Sy @ Sx, 1j * Sz))
print("S^2 =\n", (Sx @ Sx + Sy @ Sy + Sz @ Sz).real)

# measure Sx: its possible readings and the states they leave
values, vectors = np.linalg.eigh(Sx)
print("readings of Sx:", values)
print("their states (columns):\n", vectors.round(3))
```

:::{note} **Example: measure $S_x$ on a spin-up electron**

An electron is in the state $\alpha$. What can a measurement of $S_x$ give, and how often?

The readings are the eigenvalues of $\hat{S}_x$. From $\det(\hat{S}_x - \lambda) = \lambda^2 - \frac{1}{4}\hbar^2 = 0$ they are $\lambda = \pm\frac{1}{2}\hbar$, with eigenvectors (check them by row times column)

$$
\chi_{+x} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\end{pmatrix} = \frac{\alpha + \beta}{\sqrt{2}}, \qquad \chi_{-x} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\end{pmatrix} = \frac{\alpha - \beta}{\sqrt{2}}
$$

The probabilities are the squared components of $\alpha$ along them (Lecture 3.6):

$$
P\left(\pm\tfrac{1}{2}\hbar\right) = \lvert\langle\chi_{\pm x}|\alpha\rangle\rvert^2 = \left(\tfrac{1}{\sqrt{2}}\right)^2 = \tfrac{1}{2}
$$

A spin that is certainly up along $z$ is a coin toss along $x$, and $\langle S_x\rangle = 0$ as the vector model said. After the reading $+\frac{1}{2}\hbar$ the electron is in $\chi_{+x}$, which is half $\alpha$ and half $\beta$: the certainty about $S_z$ is gone. (The matrix is the $\sigma_x$ of [Appendix A.3](../math/03-vectors-and-linear-algebra.md).)
:::

#### One magnet after another

A Stern-Gerlach magnet measures one component of the spin, and blocking one of its two beams prepares a state. Put several in a row and the measurement postulates of Lecture 3.6 become things one can see on a plate:

```{code-cell} python
:tags: [hide-input]
# synced: sg_sequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Stern-Gerlach magnets in a row. Each box measures the spin along the axis written in it, and its lower beam is blocked. (a) $z$, then $z$. (b) $z$, then $x$. (c) $z$, then $x$, then $z$ again.

- **(a) Measure twice, same answer.** The first magnet leaves the atoms it passes in $\alpha$. A second measurement of $S_z$ gives $+\frac{1}{2}\hbar$ every time: the collapse of Lecture 3.6, and the reason a measurement can be trusted.
- **(b) A sharp $S_z$ is an undecided $S_x$.** Half of the atoms come out $+x$ and half $-x$, as in the example above. No way of preparing the beam makes both sharp, because $[\hat{S}_z, \hat{S}_x] \neq 0$ ([Lecture 3.5b](../ch03/05-hermitian-operators-and-commutators.md)).
- **(c) Measuring $S_x$ erases the $z$ result.** The atoms leaving the second magnet are in $\chi_{+x} = (\alpha + \beta)/\sqrt{2}$, and the third magnet finds $+z$ and $-z$ half the time each, although every one of these atoms had passed a "$+z$ only" filter. A measurement does not read off a value the atom already had. It leaves the atom in an eigenstate of what was measured.

Send atoms through. Set the second magnet along $z$, $x$ or $-z$, or tilt it by any angle: the fraction found $+$ along a magnet tilted by $\theta$ is $\cos^2(\theta/2)$ (Problem 3). Then add the third magnet.

```{anywidget} ../widgets/stern_gerlach.mjs
{}
```

### The magnetic moment of spin

If spin is an angular momentum, it should come with a magnetic moment, as orbital motion does. It does, with twice the ratio:

:::{important} **The spin magnetic moment**

$$
\hat{\vec{\mu}}_s = -g_e\,\frac{e}{2m_e}\,\hat{\vec{S}}, \qquad \mu_z = -g_e\,\mu_B\,m_s \approx \mp\mu_B, \qquad g_e = 2.0023
$$

$$
E = -\mu_zB = g_e\,\mu_BB\,m_s = \pm\tfrac{1}{2}\,g_e\,\mu_BB
$$

- $g_e$ is the electron's **g factor**. Orbital motion has $g = 1$: for the same angular momentum, spin is twice as magnetic
- $\mu_z \approx \mp\mu_B$: half a unit of angular momentum, a whole Bohr magneton
- In a field along $z$ the state $\beta$, whose moment points along the field, lies below $\alpha$, and the two are $g_e\mu_BB$ apart
:::

- **This is what Stern and Gerlach measured.** Silver's 5s electron has no orbital moment, so the moment of the atom is the spin moment of that one electron: $\mu_z = \pm\mu_B$, two spots.
- **Where the 2 comes from.** Dirac's equation gives $g = 2$ exactly. The extra 0.0023 comes from quantum electrodynamics, and the measured and calculated values of $g_e$ agree to 12 digits, the most precise agreement between theory and experiment in science.

#### Two levels in a field: magnetic resonance

```{code-cell} python
:tags: [hide-input]
# synced: spin_resonance
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The two spin states of an electron (left) and of a proton (right) in a magnetic field. The arrows mark the photon that flips the spin, at 0.34 T for the electron and at 9.4 T for the proton.

- **EPR.** An unpaired electron in a field $B$ absorbs a photon with $h\nu = g_e\mu_BB$, 28 GHz per tesla: microwaves. Electron paramagnetic resonance detects whatever has an unpaired electron: radicals, many transition-metal ions, defects in solids.
- **NMR.** The proton also has spin $\frac{1}{2}$ (written $I$ for a nucleus). Its moment is set by the **nuclear magneton** $\mu_N = e\hbar/2m_p = \mu_B/1836$ and its own g factor, $g_p = 5.586$: $h\nu = g_p\mu_NB$, 42.6 MHz per tesla, radio waves. A "400 MHz" spectrometer is a 9.4 T magnet. The proton's charge is positive, so its moment lies along its spin and $\alpha$ is the lower state.
- **Same physics, 660 times apart in frequency,** because of the mass in $\mu = (q/2m)L$.
- **Why chemists care.** In both, the exact frequency depends slightly on the surroundings of the spin: the electrons around a nucleus shield it from the field by a few parts per million (the chemical shift). That small dependence turns a spin into a reporter of structure.

:::{note} **Example: the microwaves that flip an electron spin**

A free radical sits in a field of 0.34 T. What frequency and wavelength of radiation flips its unpaired spin?

$$
\nu = \frac{g_e\,\mu_BB}{h} = 2.0023\times14.0\ \frac{\text{GHz}}{\text{T}}\times0.34\ \text{T} = 9.5\ \text{GHz}
$$

$$
\lambda = \frac{c}{\nu} = 3.1\ \text{cm}
$$

Centimeter waves, the "X band" of radar, which is why most EPR spectrometers work at this field. The photon energy is $h\nu = 3.9\times10^{-5}$ eV, 650 times smaller than $k_BT$ at room temperature, so the two spin states are almost equally populated (Problem 1).
:::

### The complete states of hydrogen

The spatial wavefunction says where the electron is, and the spin state says how its spin points. As long as the two do not influence each other, a complete state is their product, a **spin orbital**:

$$
\psi_{nlm_lm_s} = R_{nl}(r)\,Y_l^{m_l}(\theta, \phi)\times\begin{cases}\alpha & m_s = +\frac{1}{2}\\[2pt] \beta & m_s = -\frac{1}{2}\end{cases} \qquad \text{or} \qquad |n, l, m_l, m_s\rangle
$$

| operator | eigenvalue | quantum number |
| :-: | :-: | :-- |
| $\hat{H}_0$ | $-Z^2E_h/2n^2$ | $n = 1, 2, 3, \dots$ |
| $\hat{L}^2$ | $l(l+1)\,\hbar^2$ | $l = 0, 1, \dots, n - 1$ |
| $\hat{L}_z$ | $m_l\,\hbar$ | $m_l = -l, \dots, l$ |
| $\hat{S}^2$ | $\frac{3}{4}\hbar^2$ | $s = \frac{1}{2}$, always |
| $\hat{S}_z$ | $m_s\,\hbar$ | $m_s = +\frac{1}{2}, -\frac{1}{2}$ |

- **Four quantum numbers.** The five operators commute with one another (the spin operators act on $\alpha$ and $\beta$ only, the others on $r$, $\theta$, $\phi$ only), so one state carries all five values. Four numbers label it, since $s$ never changes.
- **Orthonormal.** The bracket of two spin orbitals is the integral over space times the dot product of the spin parts. Two states with the same orbital and opposite spins are orthogonal because $\langle\alpha|\beta\rangle = 0$.
- **$2n^2$ states in level $n$:** 2, 8, 18, 32. With the Pauli principle these become the lengths of the rows of the periodic table ([Chapter 7](../ch07/01-multi-electron-atoms.md)).
- **In a magnetic field** both moments contribute: $\hat{H} = \hat{H}_0 + \dfrac{\mu_BB}{\hbar}\left(\hat{L}_z + g_e\hat{S}_z\right)$, with energies $E_n + \mu_BB\,(m_l + g_e m_s)$. This is right as long as the two magnets inside the atom ignore each other. They do not quite.

### Spin-orbit coupling

#### The electron sees a moving nucleus

```{code-cell} python
:tags: [hide-input]
# synced: spin_orbit_frames
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Left: the electron orbits the nucleus, with orbital angular momentum $\vec{L}$. Right: the same motion seen from the electron. The nucleus circles the electron, and this loop of positive current makes a magnetic field $\vec{B}$ at the electron, parallel to $\vec{L}$. The spin moment $\vec{\mu}_s$ has an energy in that field.

Seen from the electron, the nucleus is a loop of current, and a loop of current makes a magnetic field at its center. That field points along $\vec{L}$ and falls off as $Z/r^3$. The spin moment has the energy $-\vec{\mu}_s\cdot\vec{B}$ in it, and with $\vec{\mu}_s \propto -\vec{S}$ and $\vec{B} \propto \vec{L}$ this is

$$
\hat{H}_{\text{so}} = \xi(r)\;\hat{\vec{L}}\cdot\hat{\vec{S}}, \qquad \xi(r) = \frac{Ze^2}{8\pi\varepsilon_0\,m_e^2c^2}\,\frac{1}{r^3}
$$

- **No outside field is involved.** The atom makes the field itself. In hydrogen's 2p state it is about 0.4 T (Problem 5).
- **$\xi > 0$:** the energy is higher when $\vec{S}$ is parallel to $\vec{L}$, because then the moment points against the internal field.
- **An s electron has no orbital motion** ($l = 0$): no internal field, no coupling.
- **The $c^2$ marks a relativistic effect.** It is small in light atoms and grows quickly with the nuclear charge.

In a state with radial function $R_{nl}$, the factor $\xi(r)$ is replaced by its average, and it is convenient to absorb the $\hbar^2$ of $\hat{\vec{L}}\cdot\hat{\vec{S}}$ into one constant with the units of energy, the **spin-orbit coupling constant** $A = \hbar^2\langle\xi\rangle_{nl}$ of the level:

$$
\hat{H}_{\text{so}} = \frac{A}{\hbar^2}\;\hat{\vec{L}}\cdot\hat{\vec{S}}
$$

#### Only the total angular momentum is conserved

Written out, $\hat{\vec{L}}\cdot\hat{\vec{S}} = \hat{L}_x\hat{S}_x + \hat{L}_y\hat{S}_y + \hat{L}_z\hat{S}_z$. The first two terms do not commute with $\hat{L}_z$ or with $\hat{S}_z$: the internal field twists the spin, the spin twists the orbit back, and neither $m_l$ nor $m_s$ stays sharp. But nothing twists the atom as a whole, and by the rule of Lecture 4.4 (no torque, no change) its **total** angular momentum is conserved:

$$
\hat{\vec{J}} = \hat{\vec{L}} + \hat{\vec{S}}, \qquad [\hat{H}, \hat{J}^2] = [\hat{H}, \hat{J}_z] = 0
$$

$\hat{\vec{J}}$ obeys the commutation rules of an angular momentum, so it has quantum numbers of its own: $\hat{J}^2$ gives $j(j+1)\hbar^2$ and $\hat{J}_z$ gives $m_j\hbar$ with $m_j = -j, \dots, j$. Since $\hat{J}_z = \hat{L}_z + \hat{S}_z$, the projections add: $m_j = m_l + m_s$.

The energy follows without solving anything. Square the sum (the cross terms combine because every component of $\hat{\vec{L}}$ commutes with every component of $\hat{\vec{S}}$):

$$
\hat{J}^2 = \hat{L}^2 + \hat{S}^2 + 2\,\hat{\vec{L}}\cdot\hat{\vec{S}} \qquad\Longrightarrow\qquad \hat{\vec{L}}\cdot\hat{\vec{S}} = \tfrac{1}{2}\left(\hat{J}^2 - \hat{L}^2 - \hat{S}^2\right)
$$

In a state with sharp $j$, $l$ and $s$ each operator on the right gives its eigenvalue:

:::{important} **Spin-orbit coupling and the total angular momentum**

$$
\hat{\vec{J}} = \hat{\vec{L}} + \hat{\vec{S}}, \qquad j = l + \tfrac{1}{2} \ \text{ or } \ l - \tfrac{1}{2}, \qquad m_j = -j, \dots, j
$$

$$
E_{\text{so}} = \frac{A}{2}\Big[j(j+1) - l(l+1) - s(s+1)\Big]
$$

$$
E_{\text{so}} = +\tfrac{1}{2}A\,l \ \ \left(j = l + \tfrac{1}{2}\right), \qquad E_{\text{so}} = -\tfrac{1}{2}A\,(l+1) \ \ \left(j = l - \tfrac{1}{2}\right)
$$

- For $l = 0$ there is only $j = \frac{1}{2}$, and no splitting
- $A$ is the spin-orbit coupling constant of the level, an energy
- The states of sharp energy are labelled by $n$, $l$, $j$, $m_j$. Neither $m_l$ nor $m_s$ is sharp in them
- Every level with $l > 0$ splits in two, $\frac{1}{2}A\,(2l+1)$ apart: the **fine structure**
:::

#### Adding $l = 1$ and $s = \frac{1}{2}$: count the states

Why $j = l \pm \frac{1}{2}$ and nothing else? Count, for the six states of a p electron:

```{code-cell} python
:tags: [hide-input]
# synced: adding_momenta
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Left: the six states of a p electron sorted by $m_l$ and $m_s$; each box shows $m_j = m_l + m_s$. Right: the same six values of $m_j$ form a ladder of four ($j = \frac{3}{2}$) and a ladder of two ($j = \frac{1}{2}$).

- **The largest $m_j$ is $\frac{3}{2}$, and it occurs once.** A ladder that reaches $\frac{3}{2}$ has $j = \frac{3}{2}$, and it uses one state at each of $\frac{3}{2}, \frac{1}{2}, -\frac{1}{2}, -\frac{3}{2}$.
- **What is left is one state at $+\frac{1}{2}$ and one at $-\frac{1}{2}$:** a ladder with $j = \frac{1}{2}$.
- **$3\times2 = 6 = 4 + 2$.** The same six states, regrouped: a change of axes within the level, like the step from $Y_1^{\pm1}$ to $p_x$, $p_y$ in Lecture 5.2. In general $2(2l+1) = (2l+2) + 2l$, the two ladders $j = l + \frac{1}{2}$ and $j = l - \frac{1}{2}$.
- **The corner boxes are single products,** for example $Y_1^{+1}\alpha$ for $m_j = +\frac{3}{2}$. **The split boxes are shared:** the state with $j = \frac{3}{2}$, $m_j = \frac{1}{2}$ is $\sqrt{\frac{2}{3}}\;Y_1^{0}\,\alpha + \sqrt{\frac{1}{3}}\;Y_1^{+1}\,\beta$, a superposition in which neither $m_l$ nor $m_s$ is sharp but their sum is.

:::{note} **Example: an f electron**

What values of $j$ can an electron with $l = 3$ have, how many states are in each level, and where do the levels lie?

$j = 3 + \frac{1}{2} = \frac{7}{2}$ or $3 - \frac{1}{2} = \frac{5}{2}$, with $2j + 1 = 8$ and 6 states: $8 + 6 = 14 = 2\times7$, every state accounted for. From the box, $E_{\text{so}} = +\frac{3}{2}A$ for $j = \frac{7}{2}$ and $-2A$ for $j = \frac{5}{2}$, a gap of $\frac{7}{2}A$. The weighted average is $8\times\frac{3}{2}A + 6\times(-2A) = 0$: the coupling splits the level without moving its center.
:::

#### Fine structure and term symbols

The levels are named by a **term symbol**,

$$
^{2s+1}L_j
$$

where $L$ is the capital letter of $l$ (S, P, D, F for $l = 0, 1, 2, 3$), the superscript $2s + 1 = 2$ counts the orientations of the spin (read "doublet"), and the subscript is $j$. Mind the letter S: in $^2S_{1/2}$ it means $l = 0$, not spin.

| electron | $l$ | levels | states, $2j + 1$ | $E_{\text{so}}$ |
| :-: | :-: | :-- | :-: | :-- |
| s | 0 | $^2S_{1/2}$ | 2 | 0 |
| p | 1 | $^2P_{1/2}$, $^2P_{3/2}$ | 2, 4 | $-A$, $+\frac{1}{2}A$ |
| d | 2 | $^2D_{3/2}$, $^2D_{5/2}$ | 4, 6 | $-\frac{3}{2}A$, $+A$ |
| f | 3 | $^2F_{5/2}$, $^2F_{7/2}$ | 6, 8 | $-2A$, $+\frac{3}{2}A$ |

For atoms with several electrons the same symbol is built from the total spin and total orbital angular momentum ([Lecture 7.3](../ch07/03-angular-momentum-and-term-symbols.md)).

```{code-cell} python
:tags: [hide-input]
# synced: fine_structure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Left: spin-orbit coupling splits the six states of a p level into $^2P_{3/2}$ (four states) and $^2P_{1/2}$ (two). Right: the yellow line of sodium is two lines 0.60 nm apart.

- **Sodium's yellow light is $3\text{p} \to 3\text{s}$.** The upper level is split and the lower one is not, so there are two lines: D$_2$ from $^2P_{3/2}$ at 588.995 nm and D$_1$ from $^2P_{1/2}$ at 589.592 nm.
- **In hydrogen the splitting is fine indeed.** The 2p level splits by 0.365 cm$^{-1}$, or $4.5\times10^{-5}$ eV, the "$10^{-4}$ eV" promised in Lecture 5.1. It turns H$\alpha$ into a doublet 0.014 nm wide, ten times closer than the hydrogen and deuterium pair.
- **It grows steeply with the nuclear charge:** as $Z^4$ for hydrogenlike ions, and down a group of the periodic table.

| atom | level | lines (nm) | doublet splitting (cm$^{-1}$) |
| :-: | :-: | :-: | :-: |
| Li | 2p | 670.78, 670.79 | 0.34 |
| Na | 3p | 589.00, 589.59 | 17.2 |
| K | 4p | 766.49, 769.90 | 57.7 |
| Rb | 5p | 780.03, 794.76 | 237.6 |
| Cs | 6p | 852.11, 894.35 | 554.0 |

- **In heavy atoms spin-orbit coupling is chemistry.** It reaches tenths of an eV, lets states of different total spin mix, and with that opens the "spin-forbidden" paths of photochemistry: phosphorescence and intersystem crossing are faster when a heavy atom is near.

:::{note} **Example: the sodium D lines**

From the two wavelengths, find the splitting of sodium's 3p level and its coupling constant.

$$
\tilde{\nu}_2 - \tilde{\nu}_1 = \frac{10^7}{588.995} - \frac{10^7}{589.592} = 16\,978.1 - 16\,960.9 = 17.2\ \text{cm}^{-1}
$$

or 2.1 meV. Both lines end on the same 3s level, so the difference is the gap between $^2P_{3/2}$ and $^2P_{1/2}$, which is $\frac{3}{2}A$:

$$
A = \tfrac{2}{3}\times17.2\ \text{cm}^{-1} = 11.5\ \text{cm}^{-1}
$$

47 times hydrogen's 2p value, although sodium's outer electron sees a nucleus screened by ten inner electrons. The 3p electron dips inside the core, and close to the nucleus, where $1/r^3$ is large, it feels almost the full charge $Z = 11$.
:::

:::{tip} **Going further: hydrogen's fine structure, exactly**
:class: dropdown

For a hydrogenlike atom the average of $1/r^3$ (the radial averages of Lecture 5.1) gives the coupling constant in closed form,

$$
A = \frac{Z^4E_h}{2\,(137.04)^2\;n^3\,l\,(l + \frac{1}{2})(l + 1)}
$$

where $1/137.04$ is the **fine-structure constant** $e^2/4\pi\varepsilon_0\hbar c$, the speed of the electron in hydrogen's ground state as a fraction of the speed of light. For 2p, $A = E_h/(48\times137.04^2) = 3.0\times10^{-5}$ eV, and the splitting is $\frac{3}{2}A = 4.5\times10^{-5}$ eV $= 0.365$ cm$^{-1}$ $= 10.9$ GHz.

Two more relativistic corrections have the same size (the mass of a fast electron grows, and a term that acts only on s states). Added together, the three give a simple result, the one Dirac's equation also gives:

$$
E_{nj} = E_n\left[1 + \frac{Z^2}{(137.04)^2\,n^2}\left(\frac{n}{j + \frac{1}{2}} - \frac{3}{4}\right)\right]
$$

The energy depends on $n$ and $j$, not on $l$: $2\,{}^2S_{1/2}$ and $2\,{}^2P_{1/2}$ coincide, and $2\,{}^2P_{3/2}$ lies 0.365 cm$^{-1}$ above them. In 1947 Willis Lamb and Robert Retherford found that $2\,{}^2S_{1/2}$ in fact lies 1058 MHz (0.035 cm$^{-1}$) above $2\,{}^2P_{1/2}$. This **Lamb shift** was the starting point of quantum electrodynamics. Smaller again is the **hyperfine structure**, the coupling of the electron's moment to the proton's (Problem 7).
:::

### Weak field or strong field

Now put the atom, spin-orbit coupling included, into a magnetic field. Two magnetic energies compete, the internal one of size $A$ and the external one of size $\mu_BB$ (with $g_e$ rounded to 2):

$$
\hat{H} = \hat{H}_0 + \frac{A}{\hbar^2}\,\hat{\vec{L}}\cdot\hat{\vec{S}} + \frac{\mu_BB}{\hbar}\left(\hat{L}_z + 2\hat{S}_z\right)
$$

The two added terms do not commute with each other, so no single set of labels fits every field. For a p level, though, the whole problem is a $6\times6$ matrix, and its eigenvalues can be followed from one limit to the other:

```{code-cell} python
:tags: [hide-input]
# synced: zeeman_crossover
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The six states of a p level in a magnetic field. Energies are in units of the spin-orbit constant $A$, and the field is given as $\mu_BB/A$. Dark: the states that start in $^2P_{3/2}$. Light: those that start in $^2P_{1/2}$.

- **Weak field, $\mu_BB \ll A$.** The internal coupling wins. $\vec{L}$ and $\vec{S}$ stay locked into $\vec{J}$, and the field splits each level into its $2j + 1$ states of different $m_j$: four from $^2P_{3/2}$, two from $^2P_{1/2}$. The states of one level are evenly spaced, but the spacing differs from level to level, so a spectral line breaks into many components with unequal gaps. This is the **anomalous Zeeman effect**. It was anomalous only as long as spin was unknown.
- **Strong field, $\mu_BB \gg A$.** The external field wins. $\vec{L}$ and $\vec{S}$ each line up with it on their own, $m_l$ and $m_s$ are sharp again, and $E = \mu_BB\,(m_l + 2m_s)$: five levels for a p electron. Because light does not flip the spin, the spin part of the shift is the same before and after a transition, and the lines form the normal triplet again.
- **In between** only $m_j$ is sharp. The curves bend, and two states with the same $m_j$ repel each other instead of crossing.
- **Which is which?** $\mu_BB = A$ at 0.5 T for hydrogen's 2p level and at 25 T for sodium's 3p. A 1 T laboratory magnet is a strong field for hydrogen and a weak one for sodium.

:::{tip} **Going further: the Landé factor, and the matrix behind the figure**
:class: dropdown

**Weak field.** The energies are $E = g_j\,\mu_BB\,m_j$ with the **Landé factor**

$$
g_j = 1 + \frac{j(j+1) + s(s+1) - l(l+1)}{2\,j(j+1)}
$$

| level | $^2S_{1/2}$ | $^2P_{1/2}$ | $^2P_{3/2}$ | $^2D_{3/2}$ | $^2D_{5/2}$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| $g_j$ | 2 | $\frac{2}{3}$ | $\frac{4}{3}$ | $\frac{4}{5}$ | $\frac{6}{5}$ |

It lies between the orbital value 1 and the spin value 2. The field couples to $\hat{L}_z + 2\hat{S}_z = \hat{J}_z + \hat{S}_z$; in a state of sharp $j$ the first part gives $m_j\hbar$, and the second gives the part of $\vec{S}$ that lies along $\vec{J}$, which the squaring trick supplies: $\hat{\vec{S}}\cdot\hat{\vec{J}} = \frac{1}{2}(\hat{J}^2 + \hat{S}^2 - \hat{L}^2)$.

**The matrix.** The six product states $(m_l, m_s)$ are the basis. `np.kron(A, B)` builds the matrix of "operator $A$ on the orbit, operator $B$ on the spin", and $\hat{L}_x\hat{S}_x + \hat{L}_y\hat{S}_y = \frac{1}{2}(\hat{L}_+\hat{S}_- + \hat{L}_-\hat{S}_+)$ with the raising and lowering operators of Lecture 4.4:

```python
import numpy as np

# l = 1 in the basis m_l = +1, 0, -1; s = 1/2 in the basis alpha, beta (units of hbar)
Lz = np.diag([1.0, 0, -1])
Lp = np.sqrt(2) * np.diag([1.0, 1.0], 1)        # L+ raises m_l
Sz = np.diag([0.5, -0.5])
Sp = np.diag([1.0], 1)                          # S+ turns beta into alpha

LS = np.kron(Lz, Sz) + 0.5 * (np.kron(Lp, Sp.T) + np.kron(Lp.T, Sp))
field = np.kron(Lz, np.eye(2)) + 2 * np.kron(np.eye(3), Sz)     # Lz + 2 Sz

for b in (0, 0.1, 10):                          # b = mu_B B / A
    print(b, np.linalg.eigvalsh(LS + b * field).round(2))
# 0    [-1.   -1.    0.5   0.5   0.5   0.5 ]
# 0.1  [-1.03 -0.97  0.3   0.43  0.57  0.7 ]
# 10   [-19.5 -10.05 -0.55 -0.45 10.05 20.5]
```

At zero field the eigenvalues are $-1$ twice and $+\frac{1}{2}$ four times, the box above for $l = 1$. In the weak field ($b = 0.1$) the levels are evenly spaced within each group, by $g_jb$: $\frac{2}{3}\times0.1$ and $\frac{4}{3}\times0.1$. In the strong field ($b = 10$) they approach $b\,(m_l + 2m_s) = -20, -10, 0, 0, 10, 20$.
:::

### Which transitions light can drive

The electric field of light acts on the electron's position, as it acted on a bond's dipole in Lectures [4.3](../ch04/03-molecular-vibrations.md) and [4.5](../ch04/05-rigid-rotor.md). A transition between two states is allowed only if the transition dipole $\langle\psi_f|\,\vec{r}\,|\psi_i\rangle$ is not zero ([Lecture 6.3](../ch06/03-time-dependent-perturbation-and-selection-rules.md)), and for the states of a one-electron atom the integral over the angles decides:

:::{important} **Selection rules for a one-electron atom**

$$
\Delta l = \pm1, \qquad \Delta m_l = 0, \pm1, \qquad \Delta m_s = 0, \qquad \Delta n \ \text{anything}
$$

$$
\text{with spin-orbit coupling:} \qquad \Delta j = 0, \pm1, \qquad \Delta m_j = 0, \pm1
$$

- $\Delta l = \pm1$: a photon carries one unit of angular momentum
- $\Delta m_s = 0$: the electric field of light acts on where the electron is, not on its spin
- No rule for $n$: every $n$p state can fall to 1s, which is the whole Lyman series
:::

```{code-cell} python
:tags: [hide-input]
# synced: hydrogen_grotrian
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The levels of hydrogen sorted into columns by $l$. Arrows: allowed lines, each joining neighbouring columns. Dashed and crossed: forbidden, 2s to 1s ($\Delta l = 0$) and 3d to 1s ($\Delta l = 2$).

- **Every line moves one column.** The Lyman lines are $n\text{p} \to 1\text{s}$. The Balmer line H$\alpha$ ($n = 3 \to 2$) is three transitions at once, $3\text{s} \to 2\text{p}$, $3\text{p} \to 2\text{s}$ and $3\text{d} \to 2\text{p}$, which coincide in hydrogen because the energy does not depend on $l$.
- **Why one unit.** $z = r\cos\theta$, and $\cos\theta\;Y_l^{m}$ contains only $Y_{l+1}^{m}$ and $Y_{l-1}^{m}$, the fact that gave $\Delta J = \pm1$ for the rotor in Lecture 4.5. Parity says the same in the manner of Lecture 4.2: $z$ is odd, $Y_l^m$ has parity $(-1)^l$, so $l$ must change by an odd number.
- **The $\Delta m_l$ rule made the Zeeman triplet:** $\Delta m_l = 0$ for light polarized along the field, $\pm1$ for the two circular polarizations.
- **An excited atom can only fall along the arrows.**

:::{note} **Example: why 2s outlives 2p**

The 2s and 2p states of hydrogen have the same energy, 10.2 eV above the ground state. An atom in 2p emits a Lyman $\alpha$ photon within 1.6 ns: $2\text{p} \to 1\text{s}$ has $\Delta l = -1$. For an atom in 2s the only lower state is 1s, and $2\text{s} \to 1\text{s}$ has $\Delta l = 0$. Both states are even, $z$ is odd, the integrand $\psi_{1s}\,z\,\psi_{2s}$ is odd, and the transition dipole vanishes.

The atom is stuck. The 2s state is **metastable**: left alone it lasts 0.12 s, about $10^8$ times longer than 2p, and then decays by a much slower process, the emission of two photons at once. In a real gas a collision usually comes first.
:::

### Orbital and spin angular momentum, side by side

| | orbital | spin |
| :-- | :-- | :-- |
| operators | $\hat{\vec{L}} = \hat{\vec{r}}\times\hat{\vec{p}}$, with $\hat{L}_z = -i\hbar\,\partial/\partial\phi$ | $\hat{\vec{S}}$, three $2\times2$ matrices |
| quantum numbers | $l = 0, 1, \dots, n - 1$ and $m_l = -l, \dots, l$ | $s = \frac{1}{2}$ always, and $m_s = \pm\frac{1}{2}$ |
| states | $Y_l^{m_l}(\theta, \phi)$, functions of direction | $\alpha$ and $\beta$, two-component vectors |
| length | $\sqrt{l(l+1)}\,\hbar$ | $\frac{\sqrt{3}}{2}\hbar$ |
| $z$ component | $m_l\hbar$ | $\pm\frac{1}{2}\hbar$ |
| magnetic moment | $\mu_z = -\mu_Bm_l$ | $\mu_z = -g_e\mu_Bm_s$, $g_e \approx 2$ |
| origin | motion in space; in the Schrödinger equation | intrinsic; from Dirac's equation |
| together | $\hat{\vec{J}} = \hat{\vec{L}} + \hat{\vec{S}}$, $\ j = l \pm \frac{1}{2}$, $\ m_j = m_l + m_s$ | |

- **Spin doubles every orbital** and gives the electron a second magnetic moment. A field separates the $m_l$ and $m_s$ states; inside the atom the two moments couple into $\vec{J}$ and split the levels with $l > 0$.
- **Two electrons** bring something new: their spins combine into singlets and triplets, and the Pauli principle limits which combinations exist. [Chapter 7](../ch07/01-multi-electron-atoms.md) starts there, after [Chapter 6](../ch06/01-variational-method.md) supplies the approximation methods that atoms with more than one electron need.

### Problems

#### Problem 1: Why NMR needs a big magnet

A proton has $g_p = 5.586$, and the nuclear magneton is $\mu_N = 5.051\times10^{-27}$ J/T. (a) Find the frequency that flips a proton spin in a 9.4 T magnet. (b) At 298 K, how many more protons per million are in the lower spin state than in the upper one? (c) Repeat (b) for an electron spin at 0.34 T. (d) Why do NMR spectroscopists pay for ever stronger magnets?

:::{admonition} **Solution**
:class: dropdown solution

(a) The two states are $g_p\mu_NB$ apart:

$$
\nu = \frac{g_p\,\mu_NB}{h} = \frac{5.586\times5.051\times10^{-27}\ \text{J/T}\times9.4\ \text{T}}{6.626\times10^{-34}\ \text{J s}} = 400\ \text{MHz}
$$

(b) $\Delta E = h\nu = 2.65\times10^{-25}$ J and $k_BT = 4.11\times10^{-21}$ J, so $\Delta E/k_BT = 6.4\times10^{-5}$. The Boltzmann ratio is $N_{\text{upper}}/N_{\text{lower}} = e^{-\Delta E/k_BT} \approx 1 - \Delta E/k_BT$, and the excess as a fraction of all spins is

$$
\frac{N_{\text{lower}} - N_{\text{upper}}}{N_{\text{lower}} + N_{\text{upper}}} \approx \frac{\Delta E}{2k_BT} = 3.2\times10^{-5}
$$

32 protons in a million. The rest cancel in pairs: for every spin that absorbs a photon, another emits one.

(c) For the electron $\Delta E = g_e\mu_BB = 6.3\times10^{-24}$ J, $\Delta E/k_BT = 1.5\times10^{-3}$, and the excess is $7.7\times10^{-4}$: 770 per million, 24 times better than NMR although the magnet is 28 times weaker.

(d) The net signal comes from the excess, which grows in proportion to $B$, and each photon carries an energy that also grows with $B$. A stronger magnet also spreads the chemical shifts over more hertz, so crowded spectra come apart. NMR is an insensitive technique because the nuclear magneton is small, and field is the remedy.
:::

#### Problem 2: The magnetic field of a sunspot

In 1908 George Ellery Hale found that spectral lines from sunspots are split, and used the Zeeman effect to measure a magnetic field beyond the Earth for the first time. An iron line at 630.25 nm splits into three components shifted by $0$ and $\pm g\,\mu_BB$, with $g = 2.5$ for this line. In a large sunspot each outer component lies 0.014 nm from the center. (a) Find the field. (b) Compare it with the Earth's field, $5\times10^{-5}$ T. (c) A spectrograph has a resolving power $\lambda/\Delta\lambda = 500\,000$. What is the weakest field whose splitting it can resolve with this line?

#### Problem 3: A spin pointing at an angle

Consider the spin state $\chi = \cos\frac{\theta}{2}\,\alpha + \sin\frac{\theta}{2}\,\beta$. (a) Show that it is normalized. (b) What are the probabilities of the two readings of $S_z$? (c) Find $\langle S_z\rangle$, $\langle S_x\rangle$ and $\langle S_y\rangle$, and say in which direction the spin points on average. (d) Show that $\chi$ is an eigenvector of the spin component along that direction, $\hat{S}_\theta = \hat{S}_z\cos\theta + \hat{S}_x\sin\theta$. (e) A beam prepared in $\alpha$ enters a Stern-Gerlach magnet tilted by $\theta$ from $z$. What fraction comes out $+$? Check 0°, 90°, 180° and 60° against the widget.

:::{admonition} **Solution**
:class: dropdown solution

(a) $\lvert c_\alpha\rvert^2 + \lvert c_\beta\rvert^2 = \cos^2\frac{\theta}{2} + \sin^2\frac{\theta}{2} = 1$.

(b) $P(+\frac{1}{2}\hbar) = \cos^2\frac{\theta}{2}$ and $P(-\frac{1}{2}\hbar) = \sin^2\frac{\theta}{2}$.

(c) With $c = \cos\frac{\theta}{2}$ and $s = \sin\frac{\theta}{2}$:

$$
\langle S_z\rangle = \tfrac{1}{2}\hbar\,(c^2 - s^2) = \tfrac{1}{2}\hbar\cos\theta
$$

$$
\langle S_x\rangle = \frac{\hbar}{2}\begin{pmatrix}c & s\end{pmatrix}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}\begin{pmatrix}c\\ s\end{pmatrix} = \tfrac{1}{2}\hbar\,(2cs) = \tfrac{1}{2}\hbar\sin\theta
$$

and $\langle S_y\rangle = \frac{1}{2}\hbar\,(-i\,cs + i\,sc) = 0$. The averages are the components of an arrow of length $\frac{1}{2}\hbar$ in the $xz$ plane, tilted by $\theta$ from the $z$ axis.

(d) Row times column, then the formulas for the cosine and sine of a difference:

$$
\hat{S}_\theta\,\chi = \frac{\hbar}{2}\begin{pmatrix}\cos\theta & \sin\theta\\ \sin\theta & -\cos\theta\end{pmatrix}\begin{pmatrix}c\\ s\end{pmatrix} = \frac{\hbar}{2}\begin{pmatrix}\cos\theta\cos\frac{\theta}{2} + \sin\theta\sin\frac{\theta}{2}\\[2pt] \sin\theta\cos\frac{\theta}{2} - \cos\theta\sin\frac{\theta}{2}\end{pmatrix}
$$

$$
= \frac{\hbar}{2}\begin{pmatrix}\cos\left(\theta - \frac{\theta}{2}\right)\\[2pt] \sin\left(\theta - \frac{\theta}{2}\right)\end{pmatrix} = \frac{\hbar}{2}\begin{pmatrix}c\\ s\end{pmatrix} = +\frac{\hbar}{2}\,\chi
$$

$\chi$ is "spin up along the tilted axis". For $\theta = 90°$ it is $\chi_{+x} = (\alpha + \beta)/\sqrt{2}$.

(e) The magnet measures $S_\theta$, and the probability of its $+$ reading is the squared component of $\alpha$ along $\chi$: $\lvert\langle\chi|\alpha\rangle\rvert^2 = \cos^2\frac{\theta}{2}$. That gives 1 at 0°, $\frac{1}{2}$ at 90°, 0 at 180° and $\cos^230° = 0.75$ at 60°. The half angle is the mark of spin $\frac{1}{2}$: the state orthogonal to "up" is reached by turning the axis through 180°, not 90°.
:::

#### Problem 4: The third component

(a) Find the eigenvalues and the normalized eigenvectors of $\hat{S}_y$. (b) An electron is in $\alpha$. What are the probabilities of the two readings of $S_y$? (c) The same for an electron in $\chi_{+x} = (\alpha + \beta)/\sqrt{2}$. (d) Multiply the matrices to verify $[\hat{S}_x, \hat{S}_y] = i\hbar\hat{S}_z$ and $\hat{S}_x^2 + \hat{S}_y^2 + \hat{S}_z^2 = \frac{3}{4}\hbar^2$ times the unit matrix. (e) For the state $\alpha$ evaluate both sides of the general uncertainty relation of Lecture 3.6, $\sigma_{S_x}\sigma_{S_y} \geq \frac{1}{2}\lvert\langle[\hat{S}_x, \hat{S}_y]\rangle\rvert$. What is special about the result?

#### Problem 5: How strong is the magnet inside an atom?

The spin-orbit splitting of a p level can be read as the energy needed to turn the spin moment over in an internal magnetic field, $\Delta E \approx 2\mu_BB_{\text{int}}$. (a) Estimate $B_{\text{int}}$ for hydrogen's 2p level, which is split by 0.365 cm$^{-1}$. (b) Do the same for sodium's 3p level (17.2 cm$^{-1}$) and caesium's 6p level (554 cm$^{-1}$). (c) For which of hydrogen and sodium is a 1 T laboratory magnet a "weak" field, and what does each atom's spectrum show in it?

:::{admonition} **Solution**
:class: dropdown solution

(a) With $\mu_B/hc = 0.467$ cm$^{-1}$/T:

$$
B_{\text{int}} = \frac{\Delta\tilde{\nu}}{2\,\mu_B/hc} = \frac{0.365\ \text{cm}^{-1}}{2\times0.467\ \text{cm}^{-1}/\text{T}} = 0.39\ \text{T}
$$

(b) Sodium: $17.2/0.934 = 18$ T. Caesium: $554/0.934 = 590$ T. The strongest steady laboratory magnets reach about 45 T, so the outer electron of a heavy atom lives in a field that no laboratory can supply.

(c) A field is weak when $\mu_BB$ is small compared with the spin-orbit splitting, that is when $B \ll B_{\text{int}}$. For sodium 1 T is weak ($1 \ll 18$): $j$ and $m_j$ label the states, and the D lines show the anomalous Zeeman pattern. For hydrogen 1 T is already larger than the internal 0.4 T: $m_l$ and $m_s$ are nearly sharp, and the lines are close to the normal triplet. The same magnet puts the two atoms at opposite ends of the figure in "Weak field or strong field".
:::

#### Problem 6: The heavier alkali metals

Potassium's $4\text{p} \to 4\text{s}$ doublet lies at 766.49 and 769.90 nm, and caesium's $6\text{p} \to 6\text{s}$ doublet at 852.11 and 894.35 nm. (a) For each atom find the splitting of the p level in cm$^{-1}$ and in meV, and the coupling constant $A$. (b) Which line of each pair starts from $^2P_{3/2}$? (c) Compare with lithium (0.34 cm$^{-1}$) and sodium (17.2 cm$^{-1}$), and explain in a sentence or two why the splitting grows down the group although the outer electron always sees a net charge of about $+1$ from far away. (d) At 300 K, $k_BT = 208$ cm$^{-1}$. For which of these atoms would both levels of the excited p state be populated about equally in a flame?

#### Problem 7: The 21 cm line

The proton has spin $I = \frac{1}{2}$. In the ground state of hydrogen the magnetic moments of the proton and the electron are coupled by a term $A'\,\hat{\vec{I}}\cdot\hat{\vec{S}}/\hbar^2$, the hyperfine interaction, of the same form as spin-orbit coupling. The total angular momentum is $\hat{\vec{F}} = \hat{\vec{I}} + \hat{\vec{S}}$. (a) What values can $F$ take, and how many states does each have? (b) Find the energy of each level in terms of $A'$. (c) The measured gap is 1420.406 MHz. Find the wavelength and the photon energy, and compare the energy with the fine structure of 2p. (d) In an interstellar cloud at 100 K, what fraction of the hydrogen atoms is in the upper level?

:::{admonition} **Solution**
:class: dropdown solution

(a) Two spins $\frac{1}{2}$ add like $l$ and $s$: $F = \frac{1}{2} + \frac{1}{2} = 1$ or $\frac{1}{2} - \frac{1}{2} = 0$. $F = 1$ has three states ($m_F = 1, 0, -1$) and $F = 0$ has one: $3 + 1 = 4 = 2\times2$.

(b) The squaring trick again, $\hat{\vec{I}}\cdot\hat{\vec{S}} = \frac{1}{2}(\hat{F}^2 - \hat{I}^2 - \hat{S}^2)$:

$$
E_F = \frac{A'}{2}\left[F(F+1) - \tfrac{3}{4} - \tfrac{3}{4}\right] = \begin{cases} +\frac{1}{4}A' & F = 1\\[2pt] -\frac{3}{4}A' & F = 0\end{cases}
$$

The gap is $A'$, and the center does not move: $3\times\frac{1}{4} - 1\times\frac{3}{4} = 0$.

(c) $\lambda = c/\nu = 2.998\times10^{8}/1.4204\times10^{9} = 0.211$ m $= 21.1$ cm, and $h\nu = 5.9\times10^{-6}$ eV. The fine structure of 2p is $4.5\times10^{-5}$ eV, eight times larger: the proton's moment is far weaker than the electron's.

(d) $k_BT = 8.6\times10^{-3}$ eV at 100 K, 1500 times the gap, so the Boltzmann factor is 1 and the populations follow the number of states, 3 to 1: three quarters of the atoms are in $F = 1$. An atom in $F = 1$ radiates only about once in $10^{7}$ years, but there is so much hydrogen between the stars that the line, first detected in 1951, maps the spiral arms of the galaxy.
:::

#### Problem 8: Counting lines

(a) List the levels of hydrogen with $n = 3$ by term symbol, with the number of states in each, and check that they add up to $2n^2 = 18$. (b) Which of these transitions are allowed: $3\text{d} \to 2\text{p}$, $3\text{d} \to 2\text{s}$, $3\text{s} \to 1\text{s}$, $4\text{f} \to 3\text{d}$, $3\text{p} \to 2\text{p}$, $4\text{s} \to 3\text{p}$? (c) H$\alpha$ is $n = 3 \to n = 2$. Using $\Delta l = \pm1$ and $\Delta j = 0, \pm1$, list every allowed transition between the fine-structure levels, in the form $3\,{}^2D_{5/2} \to 2\,{}^2P_{3/2}$. How many are there? (d) Which rule forbids $3\,{}^2D_{5/2} \to 2\,{}^2P_{1/2}$?
