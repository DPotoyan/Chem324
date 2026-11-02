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

:::

### A rotating molecule is a particle on a sphere

[Lecture 4.4](04-angular-momentum.md) reduced a rigid dumbbell to one particle of reduced mass $\mu$ on a circle. Let the dumbbell point in any direction and the particle moves on a sphere of radius $R_e$, the bond length. The potential energy does not change as the molecule turns, so all of its energy is the kinetic energy of rotation, $L^2/2I$:

$$
\hat{H} = \frac{\hat{L}^2}{2I}, \qquad I = \mu R_e^2
$$

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

Light pushes on the dipole moment $M$ of a molecule ([Lecture 4.3](03-molecular-vibrations.md)). A polar diatomic such as HCl or CO carries a permanent dipole $M_e$ along its axis. As the molecule turns, the dipole turns with it: seen along any fixed direction it oscillates at the rotation frequency, and it can exchange energy with light at that frequency. A nonpolar molecule (H$_2$, N$_2$, O$_2$, CO$_2$, CH$_4$) has no permanent dipole, so its rotation is invisible in absorption. (Raman spectroscopy still sees it, through the polarizability.)

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

:::{note} **Example: reading the HCl band**

The HCl band has its lines nearest the gap at R(0) = 2906.25 and P(1) = 2865.10 cm$^{-1}$. Find the band origin and $\tilde{B}$, treating HCl as a rigid rotor.

The two lines sit symmetrically about the gap, $\tilde{\nu}_0 \pm 2\tilde{B}$:

$$
\tilde{\nu}_0 = \frac{2906.25 + 2865.10}{2} = 2885.68\ \text{cm}^{-1}, \qquad \tilde{B} = \frac{2906.25 - 2865.10}{4} = 10.29\ \text{cm}^{-1}
$$

The band origin is 2885.98 cm$^{-1}$, and the microwave value of $\tilde{B}$ is 10.44 cm$^{-1}$. The small differences come from the bond being slightly longer in $v = 1$ (next section).
:::

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

#### Bigger molecules

- Linear molecules (OCS, HCN, CO$_2$) rotate like diatomics, with one moment of inertia and the same $J(J+1)$ ladder. CO$_2$ has no dipole, so it has no microwave spectrum.
- Nonlinear molecules turn about three axes ([Lecture 4.1](01-molecular-degrees-of-freedom.md)), with three moments of inertia. In symmetric tops such as NH$_3$ two of them are equal, and the levels need a second quantum number. Water, with three different moments, has a famously irregular spectrum. These are beyond this course.

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
