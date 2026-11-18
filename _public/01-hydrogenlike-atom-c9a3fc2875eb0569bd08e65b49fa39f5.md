---
kernelspec:
  name: python3
  display_name: Python 3
---

# Hydrogenlike Atoms

:::{note} **What you need to know**

- A **hydrogenlike atom** is one electron bound to a nucleus of charge $Ze$: H, He$^+$, Li$^{2+}$. It is the third model well of the course, after the box and the spring, and the last one the Schrödinger equation solves exactly. The Coulomb attraction $-Ze^2/4\pi\varepsilon_0 r$ has no walls and no bottom; its levels crowd toward $E = 0$, above which the electron is free.
- The force is **central**: $V$ depends on $r$ alone, so angular momentum is conserved and the angular part of every stationary state is a spherical harmonic $Y_l^m$ of [Lecture 4.4](../ch04/04-angular-momentum.md). Only the **radial function** is new, $\psi = R_{nl}(r)\,Y_l^m(\theta, \phi)$, and it solves a one-dimensional Schrödinger equation in an **effective potential**: the Coulomb attraction plus the centrifugal term $l(l+1)\hbar^2/2\mu r^2$.
- The constants $\hbar$, $\mu$ and $e^2/4\pi\varepsilon_0$ build **one length and one energy**: the Bohr radius $a_0 = 52.9$ pm and the hartree $E_h = 27.2$ eV. Squeezing the electron into a size $a$ costs kinetic energy $\hbar^2/2\mu a^2$ while the attraction pays $-e^2/4\pi\varepsilon_0 a$; the balance at $a = a_0$ gives $-E_h/2 = -13.6$ eV. That is why the atom does not collapse.
- The radial function must die at large $r$, and that quantizes the energy: $E_n = -Z^2E_h/2n^2$ with $n = 1, 2, 3, \dots$, $l = 0, \dots, n-1$ and $m = -l, \dots, l$. The energy depends on $n$ alone, so level $n$ holds $n^2$ states ($2n^2$ with spin), a degeneracy special to the $1/r$ potential. $R_{nl}$ is a polynomial times $e^{-Zr/na_0}$, with $n - l - 1$ radial nodes.
- The level differences give **Rydberg's formula** with $R_\infty = E_h/2hc = 109\,737$ cm$^{-1}$ built from constants, no longer a fit. The reduced mass lowers it slightly for each isotope: deuterium's lines sit 0.18 nm from hydrogen's at H$\alpha$.

:::

### A third model well

Chapter 4 solved two model systems: a particle between walls and a particle on a spring. The third is an electron attracted to a nucleus. Its potential energy is the Coulomb law, $-Ze^2/4\pi\varepsilon_0 r$, which has no walls and no spring: it falls without limit as the electron approaches the nucleus and fades to zero far away. The three wells give three patterns of levels:

```{code-cell} python
:tags: [hide-input]
# synced: three_wells
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The three model wells and their ladders. Box: $E_n \propto n^2$, gaps that grow. Spring: equal gaps $\hbar\omega$. Coulomb: $E_n \propto -1/n^2$, gaps that shrink toward $E = 0$. Above zero (shaded) the electron is free and any energy is allowed. Each level is drawn across its classically allowed region.

- **The gaps shrink.** Each step up the Coulomb ladder is smaller than the last, and the levels pile up against $E = 0$, the ionization limit. Lecture 1.5 saw this in the hydrogen spectrum: each series of lines converges on a limit, beyond which a continuum begins.
- **Above zero the electron is free.** With $E > 0$ it escapes to infinity, like the free particle of Lecture 3.1: no quantization, any energy. The bound states, $E < 0$, are the atom.
- **No bottom, but a ground state.** The potential falls to $-\infty$ at the nucleus, yet the lowest level is finite, $-13.6$ eV. The uncertainty principle sets it, as it set the zero-point energy of the spring ([Lecture 4.2](../ch04/02-quantum-harmonic-oscillator.md)); the section on scales shows how.

### One electron and one nucleus

#### Two bodies, one reduced mass

A hydrogenlike atom has two particles, an electron of mass $m_e$ and charge $-e$ and a nucleus of mass $m_N$ and charge $+Ze$. As for the vibrating diatomic of [Lecture 4.1](../ch04/01-molecular-degrees-of-freedom.md), their motion separates into the free flight of the center of mass, which carries no chemistry, and the relative motion of one particle of reduced mass

$$
\mu = \frac{m_em_N}{m_e + m_N}
$$

at the distance $\vec{r}$ of the electron from the nucleus. The nucleus is at least 1836 times heavier than the electron, so $\mu$ differs from $m_e$ by less than 0.06%: $\mu = 0.99946\,m_e$ for hydrogen. This lecture writes $\mu$, and sets $\mu = m_e$ wherever that precision does not matter. The deuterium example at the end shows where it does.

#### The Hamiltonian

The kinetic energy is that of one particle in three dimensions, as for the box of Lecture 3.2, and the potential energy is the Coulomb attraction:

:::{important} **The hydrogenlike atom**

$$
\hat{H} = -\frac{\hbar^2}{2\mu}\nabla^2 - \frac{Ze^2}{4\pi\varepsilon_0 r}, \qquad \hat{H}\,\psi(r, \theta, \phi) = E\,\psi(r, \theta, \phi)
$$

- $Z = 1$ for H, 2 for He$^+$, 3 for Li$^{2+}$: one electron and one nucleus. $\varepsilon_0$ is the vacuum permittivity and $e = 1.602\times10^{-19}$ C
- Helium, with two electrons, adds a repulsion $e^2/4\pi\varepsilon_0 r_{12}$ between them, and the equation can no longer be solved exactly ([Chapter 7](../ch07/01-helium-atom.md))
:::

### A central force

#### Angular momentum is conserved

The potential depends on the distance $r$ alone, not on the direction. Turn the atom about the nucleus and nothing changes, so by Noether's theorem ([Lecture 4.4](../ch04/04-angular-momentum.md)) its angular momentum is conserved. In quantum mechanics the same statement is that the Hamiltonian commutes with the angular momentum operators:

$$
[\hat{H}, \hat{L}^2] = 0, \qquad [\hat{H}, \hat{L}_z] = 0
$$

The kinetic energy commutes with $\hat{L}$ because a turn does not change $\nabla^2$, and $V(r)$ commutes with it because $\hat{L}$ differentiates only with respect to the angles and $V(r)$ has none. By [Operators 2](../ch03/05-hermitian-operators-and-commutators.md), commuting operators share eigenfunctions: the stationary states of the atom can be chosen with sharp $L^2 = \hbar^2l(l+1)$ and $L_z = m\hbar$. The quantum numbers $l$ and $m$ of Lecture 4.4 label the atom's states before any new equation is solved.

#### Separate the angles from the radius

Lecture 4.4 split the Laplacian into a radial part and the angular momentum:

$$
\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) - \frac{\hat{L}^2}{\hbar^2r^2}
\quad\Longrightarrow\quad
\hat{H} = -\frac{\hbar^2}{2\mu}\,\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) + \frac{\hat{L}^2}{2\mu r^2} - \frac{Ze^2}{4\pi\varepsilon_0 r}
$$

The middle term is the rotational kinetic energy $L^2/2I$ of a particle at distance $r$, with $I = \mu r^2$: the rigid rotor of Lecture 4.5, now with a radius that can change. Since $\hat{L}^2$ acts on the angles alone and everything else on $r$ alone, the equation separates:

```{code-cell} python
:tags: [hide-input]
# synced: hatom_roadmap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The plan. A central potential commutes with $\hat{L}^2$ and $\hat{L}_z$, so $\psi$ separates into an angular factor, the spherical harmonics already solved in Lecture 4.4, and a radial factor, which is the only new equation. Multiplying the two gives the atom.

Write $\psi(r, \theta, \phi) = R(r)\,Y_l^m(\theta, \phi)$ and use $\hat{L}^2Y_l^m = \hbar^2l(l+1)\,Y_l^m$. Every term then carries the same factor $Y_l^m$, which divides out, leaving an equation in $r$ alone:

$$
-\frac{\hbar^2}{2\mu}\,\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) + \left[\frac{\hbar^2l(l+1)}{2\mu r^2} - \frac{Ze^2}{4\pi\varepsilon_0 r}\right]R = E\,R
$$

One more substitution turns it into an equation this course has solved many times. Put $R(r) = u(r)/r$. Then $r^2R' = ru' - u$, its derivative is $ru''$, and the radial kinetic term becomes $-(\hbar^2/2\mu)\,u''/r$. Multiplying through by $r$:

:::{important} **The radial equation**

$$
-\frac{\hbar^2}{2\mu}\,\frac{d^2u}{dr^2} + V_{\mathrm{eff}}(r)\,u = E\,u, \qquad V_{\mathrm{eff}}(r) = -\frac{Ze^2}{4\pi\varepsilon_0 r} + \frac{\hbar^2l(l+1)}{2\mu r^2}, \qquad u(r) = r\,R(r), \quad u(0) = 0
$$

- The one-dimensional Schrödinger equation of [Lecture 3.1](../ch03/01-schrodinger-equation.md) on the half line $r > 0$, with a wall at the nucleus: $u(0) = 0$ keeps $R = u/r$ finite there
- $|u|^2\,dr = r^2|R|^2\,dr$ is the probability of finding the electron between $r$ and $r + dr$, at any angle ([Atomic Orbitals](02-atomic-orbitals.md))
:::

#### The effective potential

The electron moves in the Coulomb attraction plus a repulsive **centrifugal term**, the rotational kinetic energy $L^2/2\mu r^2$ with $L^2 = \hbar^2l(l+1)$:

```{code-cell} python
:tags: [hide-input]
# synced: effective_potential
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The effective radial potential for $l = 0$, 1 and 2, in units of $E_h$ and $a_0$ (defined below). For $l = 0$ it is the bare Coulomb well. For $l > 0$ the centrifugal term wins at small $r$ and turns the well into a bowl with a bottom at $r = l(l+1)\,a_0$. Dashed: the levels $E_1$, $E_2$, $E_3$ found below.

- **$l = 0$: no barrier.** The electron can reach the nucleus. Only s states have density at $r = 0$, which is why they feel the nucleus most strongly (Chapter 7).
- **$l > 0$: a barrier.** The $1/r^2$ term beats the $1/r$ attraction at small $r$ and keeps the electron away from the nucleus. The larger $l$, the farther out the bowl, so a p electron stays farther from the nucleus than an s electron of the same energy.
- **The level $E_1$ lies below the bowl for $l = 1$.** The $l = 1$ well bottoms out at $-E_h/4$, above $E_1 = -E_h/2$, so no $l = 1$ state can have the ground-state energy. The lowest level that fits every $l$ is read off below: $n = l + 1$.

### One length and one energy

$\hat{H}$ contains only $\hbar$, $\mu$ and the Coulomb strength $e^2/4\pi\varepsilon_0$. As for the oscillator in [Lecture 4.2](../ch04/02-quantum-harmonic-oscillator.md), they build one length and one energy, and the whole solution is written in those units.

**Length.** Confine the electron within a distance $a$ of the nucleus. The uncertainty principle makes its momentum at least about $\hbar/a$, so confinement costs a kinetic energy of order $\hbar^2/\mu a^2$, while the attraction pays $e^2/4\pi\varepsilon_0 a$. The two balance where

$$
\frac{\hbar^2}{\mu a^2} = \frac{e^2}{4\pi\varepsilon_0 a} \quad\Longrightarrow\quad a_0 = \frac{4\pi\varepsilon_0\hbar^2}{\mu e^2} = 52.9\ \text{pm}
$$

the **Bohr radius**. Lecture 1.5 found the same length from a circular orbit; here no orbit is assumed, only a size.

**Energy.** The Coulomb energy at that distance,

$$
E_h = \frac{e^2}{4\pi\varepsilon_0 a_0} = \frac{\hbar^2}{\mu a_0^2} = 4.360\times10^{-18}\ \text{J} = 27.21\ \text{eV}
$$

is the **hartree**. Half of it, 13.6 eV, is the binding energy of the ground state, the Rydberg energy of Lecture 1.5.

| scale | value | what it sets |
| :-- | :-- | :-- |
| $a_0 = 4\pi\varepsilon_0\hbar^2/\mu e^2$ | 52.92 pm | the size of the ground state; every $R_{nl}$ is a function of $r/a_0$ |
| $E_h = e^2/4\pi\varepsilon_0a_0$ | 27.21 eV | the unit of energy; the levels are $-E_h/2n^2$ |
| $E_h/2$ | 13.61 eV | the ionization energy of hydrogen, $109\,737$ cm$^{-1}$ |
| $a_0/Z$, $Z^2E_h$ | | the same scales for a nucleus of charge $Ze$: smaller and more tightly bound |

- **Atomic units.** Setting $\hbar = \mu = e = 4\pi\varepsilon_0 = 1$ measures lengths in $a_0$ and energies in $E_h$. The radial equation then reads $-\frac{1}{2}u'' + \left[-Z/r + l(l+1)/2r^2\right]u = Eu$, and the numpy cell below uses it.

#### Why the atom does not collapse

Classically the electron would spiral into the nucleus, radiating as it falls, and the potential offers no floor. Quantum mechanically a state of size $a$ has a kinetic energy that grows as the state shrinks. Estimate both parts for a family of trial states $\psi = e^{-r/a}$ of every size:

1. **Kinetic energy from the spread.** A state of size $a$ has a momentum spread of order $\hbar/a$, so $\langle T\rangle = \hbar^2/2\mu a^2$ (exact for this family).
2. **Potential energy from the size.** The electron sits at distance about $a$, so $\langle V\rangle = -e^2/4\pi\varepsilon_0 a$ (also exact for $e^{-r/a}$).
3. **Balance.** $\langle E\rangle = \hbar^2/2\mu a^2 - e^2/4\pi\varepsilon_0 a$ is lowest where $d\langle E\rangle/da = 0$: at $a = a_0$, with $\langle E\rangle = -E_h/2$.

```{code-cell} python
:tags: [hide-input]
# synced: coulomb_tradeoff
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Top: the radial density $r^2|\psi|^2$ of three trial states $e^{-r/a}$, (a) squeezed, (b) $a = a_0$, (c) spread out, with their kinetic and potential energies in hartree. Bottom: the average energy of every size. Squeezing raises the kinetic energy faster than the attraction can pay for it; spreading out gives the attraction away. The lowest total is $-E_h/2 = -13.6$ eV at $a = a_0$.

- The trial state (a) has a positive total energy: squeezed to a third of $a_0$ it would not even be bound.
- The minimum, $-13.6$ eV, is the exact ground-state energy, because $e^{-r/a_0}$ turns out to be the exact ground state (checked below). For any other well this trick gives an upper bound, and [Chapter 6](../ch06/01-variational-method.md) turns it into a method.

### Solving the radial equation

#### The tail must die

Far from the nucleus $V_{\mathrm{eff}} \to 0$ and the radial equation becomes $u'' = \kappa^2u$ with $\kappa = \sqrt{-2\mu E}/\hbar$ for a bound state, $E < 0$. Its solutions are $e^{-\kappa r}$ and $e^{+\kappa r}$. Near the nucleus the centrifugal term rules and $u \propto r^{l+1}$. Start at $u(0) = 0$, integrate outward with a trial $E$, and watch the tail: for almost every $E$ the growing piece $e^{+\kappa r}$ survives and $u$ blows up. Only at special energies does it die, exactly as for the box and the spring. Try it:

```{anywidget} ../widgets/radial_shooting.mjs
{}
```

- Move the slider slowly upward with $l = 0$. The tail flips from one side to the other each time $E$ crosses a level, and the levels appear at $-\tfrac{1}{2}$, $-\tfrac{1}{8}$, $-\tfrac{1}{18}$, $-\tfrac{1}{32}$ hartree: $-1/2n^2$.
- Switch to $l = 1$. The ladder is the same, but its first rung is missing: the lowest $l = 1$ state sits at $-1/8$, the $n = 2$ level. With $l = 2$ the first two are missing. The centrifugal barrier removes the lowest $l$ rungs, and $n$ starts at $l + 1$.
- Count the nodes of a bound state: $n - l - 1$. Each extra node costs one step up the ladder, as always.

#### The solution

The special energies are found by writing $u = r^{l+1}e^{-\kappa r}f(r)$ and expanding $f$ in powers of $r$. The recursion between the coefficients makes the series grow like $e^{+2\kappa r}$, which would undo the decaying factor, unless the series stops after a finite number of terms, exactly as for the oscillator in Lecture 4.2. It stops only when $\kappa a_0 = Z/n$ for a whole number $n > l$, and that fixes the energy:

:::{important} **Eigenfunctions and energies of the hydrogenlike atom**

$$
\hat{H}\,\psi_{nlm} = E_n\,\psi_{nlm}, \qquad E_n = -\frac{Z^2}{n^2}\,\frac{E_h}{2} = -\frac{Z^2}{n^2}\,\frac{\mu e^4}{32\pi^2\varepsilon_0^2\hbar^2} = -13.6\ \text{eV}\,\frac{Z^2}{n^2}
$$

$$
\psi_{nlm}(r, \theta, \phi) = R_{nl}(r)\,Y_l^m(\theta, \phi)
$$

$$
n = 1, 2, 3, \dots \qquad l = 0, 1, \dots, n - 1 \qquad m = -l, \dots, l
$$

- $n$, the **principal quantum number**, sets the energy and the size, $n^2a_0/Z$. The energy depends on neither $l$ nor $m$
- $l$ and $m$ are the angular momentum quantum numbers of Lecture 4.4: $L^2 = \hbar^2l(l+1)$, $L_z = m\hbar$. Chemists name $l = 0, 1, 2, 3$ by the letters s, p, d, f and write $m_l$ for $m$
:::

:::{note} **Example: check the ground state**

Show that $u = re^{-r/a}$ solves the radial equation with $l = 0$, and find $a$ and $E$.

Differentiate twice: $u' = (1 - r/a)\,e^{-r/a}$ and $u'' = (r/a^2 - 2/a)\,e^{-r/a}$. Insert into $-\frac{\hbar^2}{2\mu}u'' - \frac{Ze^2}{4\pi\varepsilon_0 r}u = Eu$ and divide by $e^{-r/a}$:

$$
-\frac{\hbar^2}{2\mu}\left(\frac{r}{a^2} - \frac{2}{a}\right) - \frac{Ze^2}{4\pi\varepsilon_0} = E\,r
$$

This must hold for every $r$. The terms without $r$ cancel only if

$$
\frac{\hbar^2}{\mu a} = \frac{Ze^2}{4\pi\varepsilon_0} \quad\Longrightarrow\quad a = \frac{4\pi\varepsilon_0\hbar^2}{\mu Ze^2} = \frac{a_0}{Z}
$$

and the terms with $r$ then give $E = -\hbar^2/2\mu a^2 = -Z^2\hbar^2/2\mu a_0^2 = -Z^2E_h/2$. So $R_{10} \propto e^{-Zr/a_0}$ with $E_1 = -13.6\,Z^2$ eV: the state of size $a_0$ that the trade-off above singled out. No node, and $l = 0$: the ground state of hydrogen has no angular momentum at all.
:::

#### The radial functions

Each $R_{nl}$ is a polynomial of degree $n - 1$ in $r$ times the exponential $e^{-Zr/na_0}$, written here with $\rho = Zr/a_0$:

| orbital | $n$ | $l$ | $R_{nl}(r)$ | radial nodes |
| :-: | :-: | :-: | :-- | :-: |
| 1s | 1 | 0 | $2\left(\dfrac{Z}{a_0}\right)^{3/2}e^{-\rho}$ | 0 |
| 2s | 2 | 0 | $\dfrac{1}{2\sqrt{2}}\left(\dfrac{Z}{a_0}\right)^{3/2}(2 - \rho)\,e^{-\rho/2}$ | 1 |
| 2p | 2 | 1 | $\dfrac{1}{2\sqrt{6}}\left(\dfrac{Z}{a_0}\right)^{3/2}\rho\,e^{-\rho/2}$ | 0 |
| 3s | 3 | 0 | $\dfrac{2}{81\sqrt{3}}\left(\dfrac{Z}{a_0}\right)^{3/2}(27 - 18\rho + 2\rho^2)\,e^{-\rho/3}$ | 2 |
| 3p | 3 | 1 | $\dfrac{4}{81\sqrt{6}}\left(\dfrac{Z}{a_0}\right)^{3/2}(6 - \rho)\,\rho\,e^{-\rho/3}$ | 1 |
| 3d | 3 | 2 | $\dfrac{4}{81\sqrt{30}}\left(\dfrac{Z}{a_0}\right)^{3/2}\rho^2\,e^{-\rho/3}$ | 0 |

```{code-cell} python
:tags: [hide-input]
# synced: radial_functions
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The radial functions for $n \leq 3$ and $Z = 1$, with their nodes in red ($R$ in units of $a_0^{-3/2}$). Rows share one scale of $r$: the $n = 3$ functions reach about four times as far as $n = 1$. Each starts as $r^l$ at the nucleus (only s functions are nonzero there) and ends as $e^{-r/na_0}$. For a nucleus $Ze$ the same curves are squeezed by $1/Z$.

- **$n - l - 1$ radial nodes.** The polynomial of degree $n - l - 1$ in front of $\rho^l$ has that many positive roots. With the $l$ angular nodes of $Y_l^m$, every $\psi_{nlm}$ has $n - 1$ nodes in all, as the box state $n$ has $n - 1$ ([Atomic Orbitals](02-atomic-orbitals.md) draws them).
- **$r^l$ at the nucleus.** The centrifugal barrier pushes states with larger $l$ out: $R_{21}$ starts linearly, $R_{32}$ quadratically. Only s states have $R(0) \neq 0$.
- **The tail $e^{-Zr/na_0}$ sets the size.** It decays on the length $na_0/Z$, and the polynomial pushes the outermost lobe to about $n^2a_0/Z$: the $n = 3$ functions reach out past $10\,a_0$. A larger $Z$ pulls everything in by the factor $1/Z$.
- Normalization is on the half line with the volume factor $r^2$: $\int_0^\infty R_{nl}^2\,r^2\,dr = 1$, and the $Y_l^m$ carry the angles. States of different $n$ and the same $l$ are orthogonal through the radial integral, states of different $l$ or $m$ through the angular one.

Pick a state. The left panel is $R_{nl}(r)$ with its nodes; the right panel is the radial distribution $r^2R_{nl}^2$, the probability per unit length of finding the electron at distance $r$, which [Atomic Orbitals](02-atomic-orbitals.md) takes up. Raise $Z$ and watch every state contract.

```{anywidget} ../widgets/radial_explorer.mjs
{}
```

In three dimensions an s orbital is a ball: $Y_0^0$ is the same in every direction, so $|\psi|^2$ depends on $r$ alone and the radial nodes are spheres. [Lecture 3.1](../ch03/01-schrodinger-equation.md) drew the 1s state as a cloud of position measurements; here are 1s, 2s and 3s the same way, each point one position drawn from $|\psi|^2$ and coloured by the sign of $\psi$. Cut the cloud open to see the shells.

```{anywidget} ../widgets/orbital_cloud.mjs
{"height": 480}
```

:::{tip} **Going further: the general formula, and the complete wavefunctions for $n \leq 3$**
:class: dropdown

Every radial function has the form

$$
R_{nl}(r) = N_{nl}\,\rho^l\,L_{n-l-1}^{2l+1}\!\left(\frac{2\rho}{n}\right)e^{-\rho/n}, \qquad \rho = \frac{Zr}{a_0}, \qquad N_{nl} = \sqrt{\left(\frac{2Z}{na_0}\right)^3\frac{(n-l-1)!}{2n\,(n+l)!}}\left(\frac{2}{n}\right)^l
$$

where $L_k^{\alpha}$ is an associated Laguerre polynomial of degree $k = n - l - 1$: the polynomial that the series method produces when it stops. scipy has it as `scipy.special.genlaguerre(k, alpha)`.

Multiplying $R_{nl}$ by the real combinations of the $Y_l^m$ (the $p_x$, $p_y$, $d_{xy}$, ... of [Atomic Orbitals](02-atomic-orbitals.md)) gives the familiar orbitals, written with $\sigma = Zr/a_0$:

| $n$ | $l$ | $m$ | wavefunction |
| :-: | :-: | :-: | :-- |
| 1 | 0 | 0 | $\psi_{1s} = \dfrac{1}{\sqrt{\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}e^{-\sigma}$ |
| 2 | 0 | 0 | $\psi_{2s} = \dfrac{1}{4\sqrt{2\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}(2 - \sigma)\,e^{-\sigma/2}$ |
| 2 | 1 | 0 | $\psi_{2p_z} = \dfrac{1}{4\sqrt{2\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}\sigma\,e^{-\sigma/2}\cos\theta$ |
| 2 | 1 | $\pm1$ | $\psi_{2p_x} = \dfrac{1}{4\sqrt{2\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}\sigma\,e^{-\sigma/2}\sin\theta\cos\phi, \qquad \psi_{2p_y} = \dfrac{1}{4\sqrt{2\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}\sigma\,e^{-\sigma/2}\sin\theta\sin\phi$ |
| 3 | 0 | 0 | $\psi_{3s} = \dfrac{1}{81\sqrt{3\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}(27 - 18\sigma + 2\sigma^2)\,e^{-\sigma/3}$ |
| 3 | 1 | 0 | $\psi_{3p_z} = \dfrac{\sqrt{2}}{81\sqrt{\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}(6 - \sigma)\,\sigma\,e^{-\sigma/3}\cos\theta$ |
| 3 | 1 | $\pm1$ | $\psi_{3p_x}, \psi_{3p_y}$: the same with $\sin\theta\cos\phi$, $\sin\theta\sin\phi$ in place of $\cos\theta$ |
| 3 | 2 | 0 | $\psi_{3d_{z^2}} = \dfrac{1}{81\sqrt{6\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}\sigma^2\,e^{-\sigma/3}\,(3\cos^2\theta - 1)$ |
| 3 | 2 | $\pm1$ | $\psi_{3d_{xz}} = \dfrac{\sqrt{2}}{81\sqrt{\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}\sigma^2\,e^{-\sigma/3}\sin\theta\cos\theta\cos\phi, \qquad \psi_{3d_{yz}}: \sin\phi$ in place of $\cos\phi$ |
| 3 | 2 | $\pm2$ | $\psi_{3d_{x^2-y^2}} = \dfrac{1}{81\sqrt{2\pi}}\left(\dfrac{Z}{a_0}\right)^{3/2}\sigma^2\,e^{-\sigma/3}\sin^2\theta\cos2\phi, \qquad \psi_{3d_{xy}}: \sin2\phi$ in place of $\cos2\phi$ |

:::

#### The same equation on a grid

The radial equation is the one-dimensional equation that [Lecture 3.5](../ch03/04-operators.md) turned into a matrix: sample $u$ on a grid of spacing $\Delta r$, write $-\frac{1}{2}u''$ with the three-point formula, add $V_{\mathrm{eff}}$ on the diagonal, and diagonalize. The wall at the nucleus is $u(0) = 0$, so the grid starts just past $r = 0$. In atomic units, for $Z = 1$:

```{code-cell} python
import numpy as np
from scipy.linalg import eigh_tridiagonal

dr = 0.01                                        # grid spacing, units of a0
r = np.arange(dr, 80, dr)                        # r > 0: the wall u(0) = 0 sits at the nucleus
for l in (0, 1, 2):
    V = -1 / r + l * (l + 1) / (2 * r**2)        # V_eff in hartree, Z = 1
    diag, off = 1 / dr**2 + V, -np.ones(len(r) - 1) / (2 * dr**2)
    E = eigh_tridiagonal(diag, off, select="i", select_range=(0, 2))[0]
    print(f"l = {l}:", np.round(E, 4))
```

- Each row of the matrix holds three numbers (the point and its two neighbors), so `eigh_tridiagonal` does what `eigh` did in Lecture 3.5, only faster on 8000 points.
- The $l = 0$ column reads $-\tfrac{1}{2}, -\tfrac{1}{8}, -\tfrac{1}{18}$: the levels $n = 1, 2, 3$. The $l = 1$ column starts at $-\tfrac{1}{8}$ and $l = 2$ at $-\tfrac{1}{18}$: the first level of each $l$ is $n = l + 1$.
- The same energies appear in every column where they are allowed. The grid knows nothing about the formula $-1/2n^2$; the degeneracy in $l$ comes out of the Coulomb potential by itself.

### Energy levels and degeneracy

```{code-cell} python
:tags: [hide-input]
# synced: hydrogen_ladder
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The levels of hydrogen up to $n = 4$, one bar for each state $(l, m)$. All states of a given $n$ share one energy, so level $n$ holds $1 + 3 + 5 + \dots = n^2$ states. Above zero (shaded) the electron is free.

- **$n^2$ states per level.** For each $l$ from 0 to $n - 1$ there are $2l + 1$ values of $m$, and $\sum_{l=0}^{n-1}(2l+1) = n^2$. The electron's spin ([Lecture 5.3](03-spin.md)) doubles it: $2n^2$, the lengths of the rows of the periodic table, 2, 8, 18, 32.
- **The $m$ degeneracy is rotational symmetry.** States that differ only in $m$ are the same state pointed in different directions, as for the rigid rotor. A magnetic field, which picks out a direction, splits them (Lecture 5.3).
- **The $l$ degeneracy is special to $1/r$.** Nothing about rotational symmetry requires 2s and 2p to share an energy; they do in hydrogen because of a further symmetry of the Coulomb potential alone, the same one that keeps planetary orbits from precessing. In atoms with more than one electron the inner electrons screen the nucleus, the potential is no longer $1/r$, and 2s drops below 2p, 3s below 3p below 3d ([Chapter 7](../ch07/02-multi-electron-atoms.md)). The effective potential shows why: s electrons penetrate to the nucleus, where the screening is weakest.

:::{note} **Example: the states with $n = 3$**

List the states of hydrogen with $n = 3$ and what a measurement of $E$, $L^2$ and $L_z$ gives in each.

- $l = 0$: 3s, one state ($m = 0$). $l = 1$: 3p, three states ($m = -1, 0, 1$). $l = 2$: 3d, five states ($m = -2, \dots, 2$). Nine in all, $3^2$, and 18 with spin.
- Every one has $E_3 = -13.6/9 = -1.51$ eV. $L^2$ is $0$, $2\hbar^2$ or $6\hbar^2$ for s, p, d, and $L_z = m\hbar$.
- Each has $n - 1 = 2$ nodes: 3s has two radial nodes, 3p one radial and one angular, 3d two angular.
:::

#### Hydrogenlike ions

Everything scales with the nuclear charge. The length $a_0/Z$ and the energy $Z^2E_h$ come straight out of the ground-state check above: a larger nucleus pulls the electron in by $1/Z$ and binds it $Z^2$ times more tightly.

:::{note} **Example: He$^+$ and Li$^{2+}$**

Find the ionization energy, the size of the ground state and the wavelength of the $2 \to 1$ line for He$^+$ and Li$^{2+}$.

- Ionization energy, $-E_1 = 13.6\,Z^2$ eV: 54.4 eV for He$^+$ and 122.4 eV for Li$^{2+}$ (hydrogen: 13.6 eV).
- Size, $a_0/Z$: 26.5 pm and 17.6 pm.
- The $2 \to 1$ photon carries $\frac{3}{4}\cdot13.6\,Z^2$ eV: 40.8 eV, $\lambda = 30.4$ nm for He$^+$ and 91.8 eV, 13.5 nm for Li$^{2+}$, against 121.6 nm for hydrogen. All in the extreme ultraviolet; the stripped ions exist in stellar atmospheres and plasmas.
:::

### The spectrum

An atom absorbs or emits a photon when it jumps between two levels, $h\nu = E_{n_2} - E_{n_1}$. In wavenumbers, $\tilde{\nu} = \Delta E/hc$:

:::{important} **Spectral lines of a hydrogenlike atom**

$$
\tilde{\nu} = R\,Z^2\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right), \qquad R_\infty = \frac{E_h}{2hc} = \frac{m_ee^4}{8\varepsilon_0^2h^3c} = 109\,737\ \text{cm}^{-1}
$$

$$
R_M = \frac{R_\infty}{1 + m_e/m_N} \qquad\text{for a nucleus of mass } m_N: \quad R_H = 109\,678\ \text{cm}^{-1}
$$

- Rydberg's formula of Lecture 1.5, with the constant now built from $m_e$, $e$, $\varepsilon_0$, $h$ and $c$. $R_\infty$ is the value for an infinitely heavy nucleus; the reduced mass $\mu = m_e/(1 + m_e/m_N)$ lowers it for a real one
- $n_1 = 1$: the Lyman series (ultraviolet); $n_1 = 2$: Balmer (visible); $n_1 = 3$: Paschen (infrared). Each series ends at its limit $RZ^2/n_1^2$, beyond which the electron is free and the spectrum is continuous
:::

```{code-cell} python
:tags: [hide-input]
# synced: balmer_lines
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Top: the Balmer series of hydrogen as a spectroscope shows it, lines from $n = 3, 4, 5, \dots$ down to $n = 2$ crowding toward the series limit at 364.7 nm. Bottom: the red H$\alpha$ line at high resolution. Deuterium's line lies 0.18 nm to the blue of hydrogen's, because its heavier nucleus gives a slightly larger reduced mass.

Lecture 1.5 reached the same levels with Bohr's orbits. The Schrödinger equation keeps the levels and discards the orbit: the ground state has $l = 0$, no angular momentum at all, and the electron is a standing wave $e^{-r/a_0}$ that is densest at the nucleus. Where Bohr's model stops, at helium, intensities and fine structure, the wave equation continues.

:::{note} **Example: deuterium**

Hydrogen's H$\alpha$ line ($3 \to 2$) is at 656.47 nm in vacuum (656.28 nm in air). Where is deuterium's? ($m_p = 1836.15\,m_e$, $m_d = 3670.48\,m_e$.)

The two atoms have the same $Z$ and the same formula; only the reduced mass differs, and $\tilde{\nu} \propto R_M \propto \mu$:

$$
\frac{\mu_H}{m_e} = \frac{1}{1 + 1/1836.15} = 0.999456, \qquad \frac{\mu_D}{m_e} = \frac{1}{1 + 1/3670.48} = 0.999728
$$

$$
\lambda_D = \lambda_H\,\frac{\mu_H}{\mu_D} = 656.47\ \text{nm}\times\frac{0.999456}{0.999728} = 656.29\ \text{nm}
$$

The shift, 0.18 nm, is how Urey found deuterium in 1931 (Nobel Prize 1934): a faint satellite on the blue side of every Balmer line. The lines of ordinary hydrogen sit at $R_H = 109\,678$ cm$^{-1}$, not $R_\infty = 109\,737$: the nucleus moves too.
:::

:::{tip} **Going further: radial averages**
:class: dropdown

Averages of powers of $r$ in the state $\psi_{nlm}$, $\langle r^k\rangle = \int_0^\infty r^k\,R_{nl}^2\,r^2\,dr$, come out in closed form:

$$
\langle r\rangle = \frac{a_0n^2}{Z}\left[1 + \frac{1}{2}\left(1 - \frac{l(l+1)}{n^2}\right)\right], \qquad
\langle r^2\rangle = \frac{a_0^2n^4}{Z^2}\left[1 + \frac{3}{2}\left(1 - \frac{l(l+1) - 1/3}{n^2}\right)\right]
$$

$$
\left\langle\frac{1}{r}\right\rangle = \frac{Z}{a_0n^2}, \qquad
\left\langle\frac{1}{r^2}\right\rangle = \frac{Z^2}{a_0^2n^3(l + 1/2)}, \qquad
\left\langle\frac{1}{r^3}\right\rangle = \frac{Z^3}{a_0^3n^3\,l\,(l + 1/2)(l + 1)}
$$

- $\langle r\rangle$ grows as $n^2$: the size of the state. $\langle 1/r\rangle$ gives the average potential energy, $\langle V\rangle = -Z^2E_h/n^2 = 2E_n$, so the average kinetic energy is $-E_n$: the virial theorem of the Coulomb problem
- $\langle 1/r^3\rangle$ enters the spin-orbit coupling of [Lecture 5.3](03-spin.md)
:::

### What the solution gives, and what it leaves

The hydrogen atom is solved: every level, every state. Three lectures build on it.

- **Shapes and sizes.** $|\psi_{nlm}|^2$ and the radial distribution $r^2R_{nl}^2$, the real orbitals $p_x$, $p_y$, $d_{xy}$, most probable and average distances: [Atomic Orbitals](02-atomic-orbitals.md).
- **Spin.** The electron carries its own angular momentum, $s = \frac{1}{2}$, which the Schrödinger equation does not contain. It doubles every level, couples to the orbital motion (fine structure, a $10^{-4}$ eV splitting of the levels) and responds to magnetic fields: [Lecture 5.3](03-spin.md).
- **More electrons.** Helium's two electrons repel each other and the exact solution is gone, but the hydrogen orbitals remain the language: [Chapter 7](../ch07/01-helium-atom.md) builds atoms from them, with the $l$ degeneracy lifted by screening, and [Chapter 8](../ch08/01-born-oppenheimer-approximation.md) builds molecules.

### Problems

#### Problem 1: Positronium

An electron and a positron (its antiparticle: the same mass, the opposite charge) can bind into positronium, which lives about $10^{-7}$ s before annihilating. Find its reduced mass, its ground-state energy, the size of its ground state, and the wavelength of its $2 \to 1$ line.

:::{admonition} **Solution**
:class: dropdown solution

With two equal masses, $\mu = m_em_e/(m_e + m_e) = m_e/2$. Every energy of a hydrogenlike system is proportional to $\mu$ and every length inversely proportional to it ($a_0 \propto 1/\mu$, $E_h \propto \mu$), with $Z = 1$:

- $E_1 = -13.6\ \text{eV}\times\tfrac{1}{2} = -6.80$ eV; the levels are $-6.80/n^2$ eV.
- Size: $2a_0 = 106$ pm, twice hydrogen's.
- The $2 \to 1$ photon: $\tfrac{3}{4}\times6.80 = 5.10$ eV, $\lambda = 1240\ \text{eV nm}/5.10\ \text{eV} = 243$ nm, twice the Lyman $\alpha$ wavelength of hydrogen (121.6 nm). Measured: 243.0 nm.

Positronium is the cleanest test of the reduced mass: nothing in it is heavy.
:::

#### Problem 2: Muonic hydrogen

A muon is a heavy electron, $m_\mu = 206.8\,m_e$, and a proton can capture one. Find the reduced mass of muonic hydrogen, the size of its ground state, its ground-state energy in keV, and the energy of its $2 \to 1$ photon. The proton has a radius of 0.84 fm; compare it with the size of the state, and explain why the levels of muonic hydrogen are used to measure the size of the proton.

#### Problem 3: Check the 2p state

Show that $u(r) = r^2e^{-r/2a}$ solves the radial equation with $l = 1$, using atomic units ($\hbar = \mu = e = 4\pi\varepsilon_0 = 1$, $Z = 1$), and find $a$ and $E$.

:::{admonition} **Solution**
:class: dropdown solution

With $l = 1$ the centrifugal term is $l(l+1)/2r^2 = 1/r^2$, and the equation is $-\frac{1}{2}u'' + \left(-\frac{1}{r} + \frac{1}{r^2}\right)u = Eu$. Differentiate:

$$
u' = \left(2r - \frac{r^2}{2a}\right)e^{-r/2a}, \qquad u'' = \left(2 - \frac{2r}{a} + \frac{r^2}{4a^2}\right)e^{-r/2a}
$$

Insert and divide by $e^{-r/2a}$:

$$
-1 + \frac{r}{a} - \frac{r^2}{8a^2} - r + 1 = E\,r^2
$$

The constants cancel on their own ($-\frac{1}{2}\cdot2$ against $\frac{1}{r^2}\cdot r^2$). The terms linear in $r$ cancel only if $a = 1$, that is $a = a_0$, and what remains is $-r^2/8 = Er^2$: $E = -\frac{1}{8}$ hartree $= -3.40$ eV, the $n = 2$ level. So $R_{21} \propto re^{-r/2a_0}$, as in the table, with no radial node, and the $l = 1$ ladder starts at $n = 2$.
:::

#### Problem 4: The $n = 4$ shell

List every state of hydrogen with $n = 4$ by its letters and $m$ values, and check that they number $n^2$. For each $l$, give the number of radial nodes, the number of angular nodes, and whether the state has any density at the nucleus. Which of these states would you expect to lie lowest in a sodium atom, where the inner electrons screen the nucleus, and why?

#### Problem 5: A Rydberg atom

Hydrogen can be prepared in the level $n = 100$. Estimate the size of this state, and find the frequency and wavelength of the photon emitted in the transition $100 \to 99$. Compare it with the approximation $\Delta E \approx 2\cdot\frac{E_h}{2}/n^3$ obtained by differentiating $E_n$.

:::{admonition} **Solution**
:class: dropdown solution

- Size: $n^2a_0 = 10^4\times52.9\ \text{pm} = 0.53\ \mu\text{m}$, larger than a small virus. Such Rydberg atoms are so big and so loosely bound ($E_{100} = -1.36$ meV) that a stray electric field tears them apart.
- The photon: $\Delta E = 13.606\ \text{eV}\left(\frac{1}{99^2} - \frac{1}{100^2}\right) = 13.606\ \text{eV}\times2.030\times10^{-6} = 2.762\times10^{-5}$ eV, so $\nu = \Delta E/h = 6.68$ GHz and $\lambda = 4.49$ cm: a radio wave.
- The derivative estimate, $dE_n/dn = E_h/n^3 = 27.2\ \text{eV}/10^6 = 2.72\times10^{-5}$ eV, is 1.5% low, because the gap is not quite the slope at $n = 100$.

Radio astronomers observe these lines from hydrogen between the stars ($n = 110 \to 109$ at 5.0 GHz, for instance), and the frequency $E_h/hn^3$ is the classical orbital frequency of Bohr's model at that radius: at large $n$ the quantum atom radiates at the frequency a classical orbit would, the correspondence principle again.
:::

#### Problem 6: Ionizing hydrogen with light

A hydrogen atom in its ground state absorbs a photon of 15.0 eV. What happens, and how fast does the electron leave? What happens instead if the photon carries 10.0 eV?

:::{admonition} **Solution**
:class: dropdown solution

- 15.0 eV exceeds the ionization energy, 13.6 eV, so the electron is freed with the remainder: $\frac{1}{2}m_ev^2 = 1.4$ eV, $v = \sqrt{2\times1.4\ \text{eV}/m_e} = 7.0\times10^5$ m/s. Above the series limit any photon energy works, because the free electron can take any energy: the photoelectric effect of Lecture 1.3, with the atom as the metal.
- 10.0 eV matches no level difference from $n = 1$ (the smallest is $E_2 - E_1 = 10.2$ eV), and it cannot ionize. The atom is transparent to it. Below the ionization limit the atom absorbs only at its lines; above it, everywhere.
:::

#### Problem 7: Screening on the grid

Modify the numpy cell above. (a) Set $Z = 2$ (replace $-1/r$ by $-2/r$) and verify that every energy scales by $Z^2$. (b) Replace $-1/r$ by a screened potential, $-\left(1 + e^{-2r}\right)/r$: a nucleus of charge 2 surrounded by one electron in a 1s cloud, which cancels one unit of charge at large $r$ but not at small $r$. Compare the lowest $l = 0$ and $l = 1$ energies. Which lies lower, 2s or 2p, and how does the effective potential explain it? This is the beginning of [Chapter 7](../ch07/02-multi-electron-atoms.md).

#### Problem 8: Bohr's orbit and the real ground state

Bohr's ground state (Lecture 1.5) is a circular orbit of radius $a_0$ with angular momentum $L = \hbar$. The Schrödinger ground state has $l = 0$, no angular momentum, and the same energy. (a) Is there any state of hydrogen with energy $E_1$ and $L = \hbar$? Use the effective potential for $l = 1$ to answer. (b) Bohr's orbits have $L = n\hbar$. What values of $L$ does the quantum atom actually allow in the level $n$? (c) In what sense does $a_0$ still describe the quantum ground state, if the electron is not on a circle? (The next lecture computes the most probable distance of the 1s electron from the nucleus.)
