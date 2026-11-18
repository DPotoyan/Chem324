---
kernelspec:
  name: python3
  display_name: Python 3
---

# Time-Dependent Perturbations and Selection Rules

:::{note} **What you need to know**

- A stationary state never changes. A perturbation that **depends on time**, such as the oscillating electric field of light, $\hat{V}(t) = -\hat{M}\mathcal{E}\cos\omega t$, makes the coefficients of the stationary states change: $\Psi = \sum_n c_n(t)\,e^{-iE_nt/\hbar}\psi_n$. A changing $|c_n|^2$ is a **transition** between levels.
- **To first order**, a system that starts in state $i$ reaches state $f$ with the amplitude $c_f(t) = -(i/\hbar)\int_0^t V_{fi}(t')\,e^{i\omega_{fi}t'}dt'$, where $V_{fi} = \langle f|\hat{V}|i\rangle$ and $\omega_{fi} = (E_f - E_i)/\hbar$.
- **Resonance.** The amplitude builds up only if the light stays in step with the Bohr frequency: $\hbar\omega = E_f - E_i$. Bohr's frequency condition is a result, and the line it gives has a width of about $1/t$ for light that acts for a time $t$.
- **Strength.** The probability of the transition is proportional to the intensity of the light and to $|\langle f|\hat{M}|i\rangle|^2$, the square of the **transition dipole**.
- **Selection rules.** If the transition dipole is zero the transition is **forbidden**. Every selection rule of the course says when this one integral vanishes: $\Delta v = \pm1$, $\Delta J = \pm1$, $\Delta l = \pm1$.

:::

### What the earlier lectures left open

Spectroscopy has run through the course since Chapter 1, and three earlier lectures stopped just short of explaining it.

- **[Lecture 3.7](../ch03/07-time-dependence.md)**: a stationary state has a density that never moves. A superposition of two levels moves at the Bohr frequency $\omega_{fi} = (E_f - E_i)/\hbar$.
- **[Lecture 4.3](../ch04/03-molecular-vibrations.md)**: a molecule in such a superposition has a swinging dipole, with amplitude $\langle f|\hat{M}|i\rangle$. The lecture stated that the rate of absorption is proportional to the square of that integral, and promised the reason here.
- **Lectures [4.5](../ch04/05-rigid-rotor.md) and [5.3](../ch05/03-spin.md)**: the same integral gave the selection rules of the rotor and of the hydrogen atom.

Three questions remain. How does light take a molecule out of a stationary state at all? Why only when $h\nu$ matches a gap? And why is the rate set by $|\langle f|\hat{M}|i\rangle|^2$?

```{code-cell} python
:tags: [hide-input]
# synced: transition_map
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
plt.show()
```

Fig. The plan. Light adds a time-dependent term to the Hamiltonian, and the coefficients of the stationary states begin to change. Population reaches state $f$ only if the light is at resonance and the transition dipole is not zero. The rate is then proportional to the square of the transition dipole and to the intensity.

### A Hamiltonian that changes in time

#### Light as a perturbation

A dipole $M$ in an electric field $\mathcal{E}$ has the energy $-M\mathcal{E}$ ([Lecture 4.3](../ch04/03-molecular-vibrations.md)). In a light wave the field oscillates, so the molecule's Hamiltonian gains a term that depends on time:

$$
\hat{H}(t) = \hat{H}^{(0)} + \hat{V}(t), \qquad \hat{V}(t) = -\hat{M}\,\mathcal{E}\cos\omega t
$$

- $\hat{H}^{(0)}$ is the molecule alone, with known levels $E_n$ and states $\psi_n$
- $\mathcal{E}$ is the amplitude of the field and $\omega = 2\pi\nu$ its angular frequency
- $\hat{M}$ is the component of the dipole moment along the field: $-ex$ for an electron, $M(x)$ for a vibrating bond, $M_e\cos\theta$ for a rotating molecule

```{code-cell} python
:tags: [hide-input]
# synced: dipole_approximation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Left: the electric field of green light, wavelength 500 nm. Right: a molecule, a thousand times smaller. Across it the field has the same strength and direction everywhere; it only changes in time.

- **The electric dipole approximation.** Because the wavelength is so much longer than the molecule, the field is uniform over it, and its whole effect is the energy $-M\mathcal{E}(t)$. The approximation is excellent from radio waves to the ultraviolet.

#### The coefficients move

Lecture 3.7 gave the recipe for time evolution when the Hamiltonian is fixed: expand in stationary states, and each term keeps its coefficient and turns its own phase,

$$
\Psi(t) = \sum_n c_n\,e^{-iE_nt/\hbar}\,\psi_n \qquad (c_n\ \text{constant})
$$

With $\hat{V}(t)$ switched on, the same expansion still works, since the $\psi_n$ are a complete set, but the coefficients now depend on time. $|c_n(t)|^2$ is the probability of finding the system in level $n$ at time $t$. Three steps give their equation of motion.

1. **Insert the expansion into the time-dependent Schrödinger equation**, $i\hbar\,\partial\Psi/\partial t = (\hat{H}^{(0)} + \hat{V})\Psi$. The time derivative acts on both $c_n(t)$ and the phase:

$$
\sum_n\left(i\hbar\,\dot{c}_n + E_nc_n\right)e^{-iE_nt/\hbar}\,\psi_n = \sum_n c_n\left(E_n + \hat{V}\right)e^{-iE_nt/\hbar}\,\psi_n
$$

2. **Cancel.** The terms with $E_n$ are the same on both sides: they are the evolution that happens anyway. What is left is driven by $\hat{V}$ alone:

$$
\sum_n i\hbar\,\dot{c}_n\,e^{-iE_nt/\hbar}\,\psi_n = \sum_n c_n\,e^{-iE_nt/\hbar}\,\hat{V}\psi_n
$$

3. **Project onto one state.** Multiply by $\psi_m^*$ and integrate. Orthonormality leaves a single term on the left:

$$
i\hbar\,\frac{dc_m}{dt} = \sum_n V_{mn}(t)\,e^{i\omega_{mn}t}\,c_n
$$

with $V_{mn}(t) = \langle m|\hat{V}(t)|n\rangle$ and $\omega_{mn} = (E_m - E_n)/\hbar$.


- **Nothing has been approximated yet.** With $\hat{V} = 0$ every $c_m$ is constant, which is Lecture 3.7.
- **A matrix element opens each channel.** Population flows from state $n$ to state $m$ only through $V_{mn}$, the matrix element of the perturbation between them, the same kind of integral that [Lecture 6.2](02-perturbation-theory.md) used.
- **Each channel carries a Bohr frequency.** The factor $e^{i\omega_{mn}t}$ is the difference between the phases of the two stationary states.

### First order: a weak perturbation

Let the system start in one stationary state, $i$: $c_i(0) = 1$ and every other coefficient zero. If the perturbation is weak, the coefficients change slowly, and on the right-hand side they can be replaced by their starting values. Only the term $n = i$ survives:

$$
i\hbar\,\frac{dc_f}{dt} = V_{fi}(t)\,e^{i\omega_{fi}t}
$$

Integrating from the moment the perturbation is switched on:

:::{important} **First-order transition amplitude**

$$
c_f(t) = -\frac{i}{\hbar}\int_0^t V_{fi}(t')\,e^{i\omega_{fi}t'}\,dt', \qquad P_{i \to f}(t) = |c_f(t)|^2
$$

- $i$ is the initial state and $f$ the final one; $V_{fi} = \langle f|\hat{V}|i\rangle$ and $\omega_{fi} = (E_f - E_i)/\hbar$
- Valid while $P_{i \to f}$ stays small
:::

- **Two conditions are already visible.** The matrix element $V_{fi}$ must not vanish, and the integral must not average to zero.
- **The integral is a sum of pushes.** $e^{i\omega_{fi}t'}$ turns steadily, like a child on a swing. If $V_{fi}(t')$ is constant, the pushes point in every direction in turn and cancel. They add up only if $V_{fi}(t')$ itself oscillates at the frequency $\omega_{fi}$.

### Light at frequency $\omega$: resonance

#### The integral

For light, $V_{fi}(t) = -M_{fi}\,\mathcal{E}\cos\omega t$, where $M_{fi} = \langle f|\hat{M}|i\rangle$ is the **transition dipole**. Write the cosine as two exponentials, $\cos\omega t = \frac{1}{2}(e^{i\omega t} + e^{-i\omega t})$:

$$
c_f(t) = \frac{iM_{fi}\,\mathcal{E}}{2\hbar}\int_0^t\left[e^{i(\omega_{fi} + \omega)t'} + e^{i(\omega_{fi} - \omega)t'}\right]dt'
$$

Take absorption, $E_f > E_i$, with the light tuned near the gap, $\omega \approx \omega_{fi}$. The first exponential turns at about $2\omega$, some $10^{15}$ times a second for visible light, and its integral never grows. The second turns at the slow rate

$$
\delta = \omega_{fi} - \omega
$$

the **detuning** of the light from the transition. Keeping that term, $\int_0^t e^{i\delta t'}dt' = (e^{i\delta t} - 1)/i\delta$, and with $|e^{i\delta t} - 1|^2 = 4\sin^2(\delta t/2)$:

:::{important} **Absorption of light, to first order**

$$
P_{i \to f}(t) = \frac{|M_{fi}|^2\,\mathcal{E}^2}{\hbar^2}\;\frac{\sin^2\!\left[(\omega_{fi} - \omega)\,t/2\right]}{(\omega_{fi} - \omega)^2}, \qquad M_{fi} = \langle f|\hat{M}|i\rangle
$$

- $\mathcal{E}$ and $\omega$ are the amplitude and frequency of the light, on for a time $t$
- On resonance, $\omega = \omega_{fi}$, it becomes $P_{i \to f} = \left(|M_{fi}|\,\mathcal{E}\,t/2\hbar\right)^2$
:::

```{code-cell} python
:tags: [hide-input]
# synced: resonance_curves
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The first-order probability of reaching state $f$. Left: against time. On resonance it grows as $t^2$; off resonance it rises, falls back to zero and never builds up. Right: against the frequency of the light, after a time $t$ and after $2t$. The peak at $\omega_{fi}$ becomes four times taller and half as wide.

#### Reading the result

- **Bohr's frequency condition, derived.** The transition happens when $\hbar\omega = E_f - E_i$. Lecture 1.5 took this as a postulate and Lecture 3.7 saw it in the motion of a superposition. Here it is the condition for the pushes of the light to stay in step with the system.
- **The line has a width.** The peak reaches zero at $\omega_{fi} \pm 2\pi/t$. Light that acts for a time $t$ does not have a frequency defined better than about $1/t$: $\delta\nu\cdot t \approx 1$. A laser pulse 10 fs long is some 3000 cm$^{-1}$ wide, covers many vibrational levels at once, and launches the vibrating wave packets of Lecture 3.7.
- **Strength.** The probability is proportional to $\mathcal{E}^2$, which is the intensity of the light, and to $|M_{fi}|^2$, the square of the transition dipole. This is the statement Lecture 4.3 borrowed.
- **Emission is the same process run backward.** If the system starts in the upper level, the other exponential is the resonant one and the result is identical. Light at resonance drives a molecule down as readily as up: **stimulated emission**, the process a laser runs on.
- **Ordinary light gives a steady rate.** No light source has a single frequency. Added over a band of frequencies, the peak of the figure contributes its area, which grows in proportion to $t$: the height goes as $t^2$ and the width as $1/t$. A probability proportional to time is a constant rate of absorption, proportional to $|M_{fi}|^2$ and to the intensity of the light at $\omega_{fi}$. Summed over the molecules in a beam's path, this is the Beer-Lambert law.

:::{tip} **Going further: the rate of absorption (Fermi's golden rule)**
:class: dropdown

For light arriving from all directions with an energy density $u(\omega)$ per unit of angular frequency, the rate is

$$
W_{i \to f} = \frac{\pi}{3\varepsilon_0\hbar^2}\,|M_{fi}|^2\,u(\omega_{fi})
$$

a form of **Fermi's golden rule**: rate $=$ (coupling)$^2$ $\times$ (how much there is to couple to). Three steps lead from the first-order probability, written as $P = (|M_{fi}|^2\mathcal{E}^2/4\hbar^2)\,\sin^2(\delta t/2)/(\delta/2)^2$, to this rate.

1. A wave of amplitude $\mathcal{E}$ has the energy density $\frac{1}{2}\varepsilon_0\mathcal{E}^2$. For a band of frequencies replace $\mathcal{E}^2$ by $2u(\omega)\,d\omega/\varepsilon_0$ and integrate over $\omega$.
2. The peak is narrow, so $u(\omega)$ can be taken at $\omega_{fi}$ and moved outside. What remains is $\int\sin^2(\delta t/2)/(\delta/2)^2\,d\delta = 2\pi t$.
3. The field points in a random direction relative to the dipole. The average of $\cos^2$ of the angle between them, over all directions, is $\frac{1}{3}$.

$$
P = \frac{|M_{fi}|^2}{4\hbar^2}\cdot\frac{2u(\omega_{fi})}{\varepsilon_0}\cdot2\pi t\cdot\frac{1}{3} = \frac{\pi|M_{fi}|^2\,u(\omega_{fi})}{3\varepsilon_0\hbar^2}\;t
$$

Here $|M_{fi}|^2$ is the sum of the squares of the three components of the transition dipole. The same rate applies downward, for stimulated emission.
:::

### Watching a transition

First order holds only while the probability is small. Followed all the way, light exactly at resonance moves the whole population to the upper level. The figure follows that process for a particle in a box, driven from $\psi_1$ to $\psi_2$:

```{code-cell} python
:tags: [hide-input]
# synced: drive_two_level
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Light at resonance acting on a particle in a box. Left: the density, which starts as $|\psi_1|^2$ and ends as $|\psi_2|^2$. Right, top: the two populations. Right, bottom: the average position, which is the dipole. Press play.

- **In between, the density sloshes.** The state is a superposition of $\psi_1$ and $\psi_2$, and its density swings from side to side at the Bohr frequency, as in [Lecture 3.2](../ch03/02-particle-in-a-box.md).
- **The dipole swings only during the transition.** $\langle x\rangle$ is still at the start and at the end, when the system is in one stationary state, and swings most at the midpoint, when the populations are equal. A molecule exchanges energy with light through this swinging dipole, as [Lecture 4.3](../ch04/03-molecular-vibrations.md) said.

Drive the two levels yourself. On resonance the population goes all the way up and comes back; move the detuning away from zero and the transfer collapses. The dashed curve is first order, good only at the start.

```{anywidget} ../widgets/rabi_drive.mjs
{}
```

::::{tip} **Going further: strong light and Rabi oscillations**
:class: dropdown

For two levels the equations of motion can be solved without assuming that the coefficients stay near their starting values. Keeping the resonant term, they read

$$
\frac{dc_f}{dt} = \frac{i\Omega}{2}\,e^{i\delta t}\,c_i, \qquad \frac{dc_i}{dt} = \frac{i\Omega}{2}\,e^{-i\delta t}\,c_f
$$

$$
\Omega = \frac{|M_{fi}|\,\mathcal{E}}{\hbar}
$$

$\Omega$ is the **Rabi frequency**: the transition dipole times the field, in units of $\hbar$. On resonance ($\delta = 0$), differentiating the first equation and inserting the second gives $\ddot{c}_f = -(\Omega/2)^2c_f$, the equation of a harmonic oscillator, so $c_f = i\sin(\Omega t/2)$ and $c_i = \cos(\Omega t/2)$. In general,

$$
P_{i \to f}(t) = \frac{\Omega^2}{\Omega^2 + \delta^2}\,\sin^2\!\left(\tfrac{1}{2}\sqrt{\Omega^2 + \delta^2}\;t\right)
$$

:::{figure} ./images/rabi_flop.png
:alt: Probability of the upper state against time for two detunings, with the first-order result
:width: 85%

The probability of the upper state for two levels driven by light. On resonance the population moves completely to the upper level at $\Omega t = \pi$ and back at $2\pi$. Detuned by $\delta = \Omega$, half of it arrives at most. Dashed purple: first order.
:::

- **This is the two-level problem of Lecture 6.1 once more**, with the coupling $\frac{1}{2}\hbar\Omega$ and the gap $\hbar\delta$: the square root $\sqrt{\Omega^2 + \delta^2}$ is the same one that gave $E_\pm$.
- **A $\pi$ pulse inverts the population.** Light at resonance, left on for $t = \pi/\Omega$, moves every molecule from $i$ to $f$. Left on longer, it brings them back down by stimulated emission.
- **A $\pi/2$ pulse makes the equal superposition**, the state whose dipole swings with the largest amplitude. NMR works with exactly these pulses, applied to the two spin levels of [Lecture 5.3](../ch05/03-spin.md) with the magnetic field of a radio wave in place of $\mathcal{E}$ (Problem 3).
- **For short times** $\sin^2x \approx x^2$ returns the first-order result.
- **Why an ordinary spectrometer shows no oscillation.** Its light is weak and has many frequencies, and collisions interrupt each molecule long before $\Omega t$ reaches 1. Every molecule stays in the first-order regime, and the result is a steady rate.
::::

### Selection rules

#### Allowed and forbidden

Every result of this lecture carries the factor $|M_{fi}|^2$. If the transition dipole is zero, light of any intensity and any frequency leaves the transition untouched.

:::{important} **The selection rule for electric dipole transitions**

$$
\text{allowed only if}\qquad M_{fi} = \langle f|\hat{M}|i\rangle = \int\psi_f^*\,\hat{M}\,\psi_i\,d\tau \;\neq\; 0
$$

- The integral depends on the two states and on the dipole operator, not on the light
- A rule on quantum numbers (such as $\Delta v = \pm1$) is a statement of when this integral vanishes
:::

```{code-cell} python
:tags: [hide-input]
# synced: selection_ladders
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The selection rules of the course on one page. Solid arrows: allowed transitions. Dashed and crossed: forbidden ones, for which the transition dipole vanishes.

| system | dipole operator | rule | reason | lecture |
| :-- | :-- | :-- | :-- | :-: |
| particle in a box | $-ex$ | $\Delta n$ odd | $x - L/2$ is odd about the middle: the parity must change | [3.7](../ch03/07-time-dependence.md) |
| harmonic oscillator | $M'x$ | $\Delta v = \pm1$, and $M' \neq 0$ | $x$ connects only neighboring levels | [4.2](../ch04/02-quantum-harmonic-oscillator.md), [4.3](../ch04/03-molecular-vibrations.md) |
| rigid rotor | $M_e\cos\theta$ | $\Delta J = \pm1$, and $M_e \neq 0$ | $\cos\theta\,Y_J^M$ contains only $J \pm 1$ | [4.5](../ch04/05-rigid-rotor.md) |
| hydrogen atom | $-e\vec{r}$ | $\Delta l = \pm1$, $\ \Delta m_l = 0, \pm1$, $\ \Delta m_s = 0$ | the same angular integral; the field does not act on spin | [5.3](../ch05/03-spin.md) |
| spin in a magnetic field | magnetic moment | $\Delta m_s = \pm1$ | driven by the magnetic field of the wave | [5.3](../ch05/03-spin.md) |

Two general arguments settle most cases without an integral.

- **Parity.** The dipole operator is odd: it changes sign when every coordinate does. The integrand $\psi_f^*\hat{M}\psi_i$ is then odd, and the integral zero, unless the two states have opposite parity. This is the sandwich rule of Lecture 4.2, and in atoms it is called the Laporte rule: s to p and p to d are allowed, s to s and d to d are not.
- **Angular momentum.** A photon carries one unit of angular momentum, $\hbar$. Absorbing or emitting one changes the angular momentum of the molecule by one unit: $\Delta J = \pm1$, $\Delta l = \pm1$.

:::{note} **Example: an electron in a box**

For an electron in a box of length $L$, find the transition dipoles from $n = 1$ to $n = 2$ and to $n = 3$.

With $\hat{M} = -ex$ and the matrix elements of Lecture 3.7,

$$
M_{21} = -e\,\langle 2|x|1\rangle = \frac{16}{9\pi^2}\,eL = 0.18\,eL
$$

$$
M_{31} = -e\,\langle 3|x|1\rangle = 0
$$

$1 \to 2$ is allowed: the two states have opposite parity about the middle of the box. $1 \to 3$ is forbidden: both are even, $x - L/2$ is odd, and the integrand is odd. For $L = 1$ nm, $M_{21} = 8.7$ D, a large transition dipole, which is why conjugated dyes absorb so strongly.
:::

#### Forbidden does not mean never

A forbidden transition has a zero **electric dipole** matrix element. Weaker mechanisms remain: the magnetic field of the light, the variation of the field across the molecule, two photons at once, or a small mixing of states that breaks the rule. They show up as lines thousands or millions of times weaker, and as excited states that take a long time to emit their photon:

| excited state | why it decays slowly or fast | lifetime |
| :-- | :-- | :-: |
| H 2p | allowed, $\Delta l = -1$ | 1.6 ns |
| H 2s | $\Delta l = 0$: forbidden, decays by two photons | 0.12 s |
| triplet state of an organic dye (phosphorescence) | $\Delta S \neq 0$: the field does not act on spin | ms to s |
| upper hyperfine level of H (the 21 cm line) | magnetic dipole, and a very low frequency | $10^7$ years |

::::{tip} **Going further: spontaneous emission, lifetimes and linewidths**
:class: dropdown

Stimulated emission needs light already present. An excited atom in complete darkness still emits: **spontaneous emission**. The oscillating field of this lecture is a classical wave and cannot explain it; that takes the quantum theory of the electromagnetic field itself. Einstein found the rate in 1917 by requiring absorption, stimulated emission and spontaneous emission to keep matter and blackbody radiation in equilibrium:

$$
A_{f \to i} = \frac{\omega_{fi}^3\,|M_{fi}|^2}{3\pi\varepsilon_0\hbar c^3}, \qquad \tau = \frac{1}{A}
$$

$A$ is the probability per unit time that the excited state emits a photon, and $\tau$ is its lifetime.

- **The same transition dipole as absorption**, so a forbidden line is weak in absorption and slow in emission.
- **The $\omega^3$ decides where spontaneous emission matters.** In the ultraviolet and visible it empties excited states in nanoseconds. In the infrared it takes milliseconds, and collisions usually win. At radio frequencies it takes years: the spins of an NMR experiment never relax by emitting photons.
- **Hydrogen's 2p state.** With $E_f - E_i = 10.2$ eV, so $\omega_{fi} = 1.55\times10^{16}$ s$^{-1}$, and $|M_{fi}| = 0.745\,ea_0 = 6.32\times10^{-30}$ C m (Problem 5), the formula gives $A = 6.3\times10^8$ s$^{-1}$ and $\tau = 1.6$ ns, the measured lifetime.

:::{figure} ./images/lifetime_linewidth.png
:alt: Decaying wave trains of a long-lived and a short-lived state and their spectral lines
:width: 90%

Left: the light emitted by a long-lived and a short-lived excited state, a wave that dies away with the population. Right: the spectra of the two. The line has the full width at half maximum $1/2\pi\tau$.
:::

- **Natural linewidth.** A state that lasts a time $\tau$ emits a wave train about that long, and a wave of limited duration has a spread of frequencies, as in the resonance section: $\delta\nu = 1/2\pi\tau$. For the 2p state of hydrogen that is 100 MHz.
- **Anything that shortens the life broadens the line.** Collisions in a gas or a liquid interrupt the excited state and add to the width, which is one reason spectra of liquids are broad and spectra of dilute gases sharp.
::::

### The chapter in one table

| | variational method | perturbation theory | time-dependent perturbation theory |
| :-- | :-- | :-- | :-- |
| lecture | [6.1](01-variational-method.md) | [6.2](02-perturbation-theory.md) | this one |
| put in | a trial function | a solved problem and a small constant term | a solved problem and a term that depends on time |
| get out | an upper bound to $E_0$ | shifted levels and mixed states | transitions between the levels |
| key integral | $\langle\phi\vert\hat{H}\vert\phi\rangle$ | $\langle k\vert\hat{H}^{(1)}\vert n\rangle$ | $\langle f\vert\hat{M}\vert i\rangle$ |
| condition | lower is better | coupling small compared with the gap | resonance, $\hbar\omega = E_f - E_i$ |
| two-level problem | exact roots $E_\pm$ | the roots as a series in $v/\Delta$ | the two levels driven by light |

With these three tools the course leaves the systems that can be solved exactly. [Chapter 7](../ch07/01-multi-electron-atoms.md) applies the first two to atoms with more than one electron, and [Chapter 8](../ch08/01-born-oppenheimer-approximation.md) to molecules.

### Problems

#### Problem 1: A perturbation that is switched on and left on

A constant perturbation $\hat{V}$ is switched on at $t = 0$ and left on. (a) Use the first-order amplitude to find the probability of state $f$ at time $t$. (b) What is its largest value, and its average over time? (c) Compare with the first-order mixing coefficient of Lecture 6.2. Does a constant perturbation cause lasting transitions?

:::{admonition} **Solution**
:class: dropdown solution

(a) With $V_{fi}$ constant,

$$
c_f(t) = -\frac{iV_{fi}}{\hbar}\int_0^t e^{i\omega_{fi}t'}dt' = -\frac{V_{fi}}{\hbar\omega_{fi}}\left(e^{i\omega_{fi}t} - 1\right)
$$

$$
P_{i \to f}(t) = \frac{4|V_{fi}|^2}{(E_f - E_i)^2}\,\sin^2\frac{\omega_{fi}t}{2}
$$

(b) The probability oscillates between zero and $4|V_{fi}|^2/(E_f - E_i)^2$, with the average $2|V_{fi}|^2/(E_f - E_i)^2$. It never grows.

(c) Lecture 6.2 found that a constant perturbation changes state $i$ into $\psi_i^{(0)} + \sum_k c_k\psi_k^{(0)}$ with $|c_f|^2 = |V_{fi}|^2/(E_f - E_i)^2$: the same combination of coupling over gap. The system has not made a transition; it has been pushed from an eigenstate of the old Hamiltonian into a mixture of eigenstates of the new one, and the oscillation is that mixture beating. The amplitude is twice the static value because the perturbation was switched on suddenly. A lasting, growing transfer needs a perturbation that oscillates at $\omega_{fi}$.
:::

#### Problem 2: How short a pulse makes a wave packet?

A laser pulse lasts 10 fs. (a) Estimate the spread of its frequencies from $\delta\nu \approx 1/t$, in Hz and in cm$^{-1}$. (b) The vibrational levels of I$_2$ in its excited state are about 100 cm$^{-1}$ apart, and those of HCl are 2886 cm$^{-1}$ apart. For which molecule does the pulse cover several levels at once? (c) What does the molecule do after such a pulse? Connect your answer to the Morse packet of Lecture 3.7. (d) How long must a pulse be to excite a single vibrational level of I$_2$?

#### Problem 3: A 90° pulse in NMR

*This problem uses the Going further box on Rabi oscillations.* In NMR the two levels are the spin states of a proton in a field $B_0$, and the perturbation is a magnetic field $B_1$ rotating at the radio frequency. Its Rabi frequency is $\Omega = \gamma B_1$, with $\gamma = 2.675\times10^8$ rad s$^{-1}$ T$^{-1}$ for the proton. (a) What $B_1$ gives a $\pi/2$ pulse in 10 μs? (b) The pulse lasts 10 μs. How wide a band of frequencies does it excite? Compare with the range of proton resonances in a 400 MHz spectrometer, about 10 ppm.

:::{admonition} **Solution**
:class: dropdown solution

(a) A $\pi/2$ pulse has $\Omega t = \pi/2$:

$$
B_1 = \frac{\pi/2}{\gamma t} = \frac{1.571}{(2.675\times10^8)(1.0\times10^{-5})}\ \text{T} = 5.9\times10^{-4}\ \text{T}
$$

about 0.6 mT, some 16 000 times weaker than the 9.4 T field $B_0$ that sets the resonance frequency. It works because it is at resonance.

(b) A pulse of length $t$ has a width of about $1/t = 10^5$ Hz. Ten parts per million of 400 MHz is 4000 Hz. The pulse is 25 times broader than the whole spectrum, so it excites every proton in the sample equally, whatever its chemical shift. After the pulse each spin is in an equal superposition and its magnetic moment swings at its own frequency; the spectrometer records the sum of all those oscillations and separates the frequencies by a Fourier transform ([Appendix A.6](../math/06-fourier-transforms.md)). This is why a modern NMR experiment takes seconds and not the hours needed to sweep the frequency slowly.
:::

#### Problem 4: Allowed or forbidden?

Decide whether each transition is allowed for electric dipole radiation, and name the rule you used: (a) a particle in a box, $n = 2 \to 4$; (b) the same, $n = 2 \to 3$; (c) a harmonic oscillator, $v = 0 \to 2$; (d) HCl, $J = 1 \to 2$; (e) N$_2$, $J = 1 \to 2$; (f) hydrogen, $3\text{d} \to 2\text{p}$; (g) hydrogen, $3\text{d} \to 1\text{s}$; (h) hydrogen, $3\text{s} \to 1\text{s}$; (i) a triplet state of a molecule to its singlet ground state.

#### Problem 5: The transition dipole of Lyman α

Compute the transition dipole $\langle 2\text{p}_z|{-ez}|1\text{s}\rangle$ of hydrogen, using $z = r\cos\theta$, $R_{10} = 2e^{-r}$, $R_{21} = re^{-r/2}/2\sqrt{6}$ (atomic units), $Y_0^0 = 1/\sqrt{4\pi}$ and $Y_1^0 = \sqrt{3/4\pi}\cos\theta$. Then show that $\langle 2\text{s}|z|1\text{s}\rangle = 0$.

:::{admonition} **Solution**
:class: dropdown solution

The integral separates into a radial and an angular part:

$$
\langle 2\text{p}_z|z|1\text{s}\rangle = \int_0^\infty R_{21}\,r\,R_{10}\,r^2\,dr\;\times\int Y_1^0\cos\theta\;Y_0^0\,d\Omega
$$

Radial part, with $\int_0^\infty r^ne^{-ar}dr = n!/a^{n+1}$:

$$
\frac{1}{\sqrt{6}}\int_0^\infty r^4e^{-3r/2}\,dr = \frac{1}{\sqrt{6}}\cdot\frac{4!}{(3/2)^5} = \frac{768}{243\sqrt{6}} = 1.290\ a_0
$$

Angular part: $\cos\theta\,Y_0^0 = Y_1^0/\sqrt{3}$, so the integral is $\frac{1}{\sqrt{3}}\int|Y_1^0|^2d\Omega = 1/\sqrt{3}$. Together,

$$
\langle 2\text{p}_z|z|1\text{s}\rangle = \frac{1.290}{\sqrt{3}}\,a_0 = \frac{128\sqrt{2}}{243}\,a_0 = 0.745\,a_0
$$

$$
|M_{fi}| = 0.745\,ea_0 = 1.9\ \text{D}
$$

For $2\text{s} \to 1\text{s}$ the angular part is $\int Y_0^0\cos\theta\,Y_0^0\,d\Omega = \frac{1}{4\pi}\int\cos\theta\,d\Omega = 0$: the average of $\cos\theta$ over a sphere vanishes. Whatever the radial integral, the transition dipole is zero. This is $\Delta l = 0$, forbidden, and the reason the 2s state is metastable.
:::

#### Problem 6: The sodium D line

*This problem uses the Going further box on spontaneous emission.* The 3p state of sodium lives 16.2 ns and decays to 3s by emitting the yellow D line at 589 nm. (a) Find the natural width of the line in MHz. The two D lines are 17.2 cm$^{-1}$ apart (Lecture 5.3): is the doublet resolved in spite of the natural width? (b) Invert the formula for $A$ to find the transition dipole, in units of $ea_0$ and in debye. Is your answer a reasonable size for an atom? (c) The 3p state of sodium and the 2p state of hydrogen are both allowed. Why does sodium's live ten times longer?

#### Problem 7: Why steady light cannot empty the lower level

$N_i$ molecules are in the lower of two levels and $N_f$ in the upper. Light at resonance drives both absorption and stimulated emission at the same rate $W$ per molecule. Ignore spontaneous emission. (a) Write $dN_f/dt$. (b) What is the net rate at which energy is absorbed from the light? (c) What happens to the populations if the light is left on, and what happens to the absorption? (d) Apply your answer to NMR, where Lecture 5.3 found a population difference of 32 per million.

:::{admonition} **Solution**
:class: dropdown solution

(a) Each lower molecule goes up at the rate $W$ and each upper one comes down at the same rate:

$$
\frac{dN_f}{dt} = W N_i - W N_f = W\,(N_i - N_f)
$$

(b) Each upward step removes a photon of energy $\hbar\omega$ and each downward step adds one, so the net power absorbed is $\hbar\omega\,W\,(N_i - N_f)$. Absorption is proportional to the **difference** of the populations, not to the number of molecules.

(c) With $N = N_i + N_f$ fixed, $N_i - N_f$ obeys $d(N_i - N_f)/dt = -2W(N_i - N_f)$ and decays to zero. The populations become equal, and the net absorption stops: the transition is **saturated**. Steady light can never put more molecules in the upper level than in the lower. A laser, which needs more molecules up than down, must reach its upper level by a detour through a third level.

(d) In NMR the two levels are so close that at room temperature only 32 spins per million more are in the lower one. The signal comes from that small excess alone, which is why NMR is an insensitive method and why stronger magnets, which widen the gap and the population difference, are worth their cost. Too much radio-frequency power saturates the transition and the signal disappears.
:::

#### Problem 8: Exact against first order

*This problem uses the Going further box on Rabi oscillations.* (a) Show that for short times the exact two-level probability reduces to the first-order result, both on resonance and off. (b) On resonance, at what value of $\Omega t$ is first order 10% too high? (c) How far must the light be detuned, in units of $\Omega$, for the largest transfer to be 50%? 10%? Check both with the widget. (d) Doubling the field strength doubles $\Omega$. At a fixed detuning, what does that do to the largest transfer, and to the range of frequencies over which a transition responds?
