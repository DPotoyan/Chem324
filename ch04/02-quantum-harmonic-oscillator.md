---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Quantum Harmonic Oscillator

:::{note} **What you need to know**

- The vibrating bond of [Lecture 4.1](01-molecular-degrees-of-freedom.md) becomes the operator $\hat{H} = -\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2} + \frac{1}{2}kx^2$. It has one natural energy, $\hbar\omega$ with $\omega = \sqrt{k/\mu}$, and one natural length, $1/\sqrt{\alpha} = \sqrt{\hbar/\mu\omega}$: about 11 pm for HCl, under a tenth of the bond length.
- The ground state is a Gaussian, $\psi_0 \propto e^{-\alpha x^2/2}$, with energy $E_0 = \frac{1}{2}\hbar\omega$. This **zero-point energy** is the price of the uncertainty principle: squeezing the bond raises its kinetic energy, letting it spread raises its potential energy, and the Gaussian is the best compromise.
- The levels are evenly spaced, $E_v = \hbar\omega\left(v + \frac{1}{2}\right)$. Each state is a Hermite polynomial times the Gaussian; $\psi_v$ has $v$ nodes and is even or odd as $v$ is, so $\langle x\rangle = \langle p\rangle = 0$ in every level.
- The quantum oscillator is found beyond its classical turning points (16% of the time in $v = 0$), and at high $v$ its probability density approaches that of a classical spring.
- **Raising and lowering operators** explain the equal steps: $\hat{H} = \hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2}\right)$, $\hat{a}^\dagger$ climbs one rung, $\hat{a}$ steps down one, and the $\frac{1}{2}$ left over is a commutator. Position is $\hat{x} = (\hat{a} + \hat{a}^\dagger)/\sqrt{2\alpha}$, so it connects only neighboring levels: the root of the infrared selection rule $\Delta v = \pm 1$.

:::

### From the classical spring to the quantum one

[Lecture 4.1](01-molecular-degrees-of-freedom.md) ended with a vibrating diatomic as one bead of reduced mass $\mu$ on a spring of force constant $k$, and with five lines of numpy that found its levels: $0.5, 1.5, 2.5, \dots$ in units of $\hbar\omega$. This lecture derives that ladder by hand, finds the wavefunctions, and explains why the steps are exactly equal.

Replace the momentum by $\hat{p} = -i\hbar\,d/dx$ in the classical energy:

$$
\hat{H} = \frac{\hat{p}^2}{2\mu} + \frac{1}{2}kx^2 = -\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2} + \frac{1}{2}kx^2, \qquad \hat{H}\psi_v(x) = E_v\,\psi_v(x)
$$

- $x = R - R_e$ is the stretch of the bond, $\mu$ the reduced mass, and $k$ the force constant, the curvature of the bond potential at its minimum.
- The integer $v = 0, 1, 2, \dots$ that labels the states is the **vibrational quantum number**, the italic letter $v$. Do not confuse it with the frequency $\nu$ (Greek nu). The angular frequency of the classical spring is $\omega = 2\pi\nu = \sqrt{k/\mu}$.

#### One energy and one length

The Hamiltonian contains only $\hbar$, $\mu$ and $k$. From these there is one way to build an energy and one way to build a length:

$$
\hbar\omega = \hbar\sqrt{\frac{k}{\mu}}, \qquad \frac{1}{\sqrt{\alpha}} = \sqrt{\frac{\hbar}{\mu\omega}}, \qquad \text{with} \quad \alpha = \frac{\mu\omega}{\hbar} = \frac{\sqrt{\mu k}}{\hbar}
$$

Every energy of the oscillator is a number times $\hbar\omega$, and every length a number times $1/\sqrt{\alpha}$. For H$^{35}$Cl, with $k = 516$ N/m and $\mu = 1.627\times10^{-27}$ kg ([Lecture 4.1](01-molecular-degrees-of-freedom.md), Problem 2):

| quantity | value for HCl |
|:--|:--|
| $\omega = \sqrt{k/\mu}$ | $5.63\times10^{14}$ s$^{-1}$ |
| $\hbar\omega$ | $5.94\times10^{-20}$ J $= 0.371$ eV, or 2990 cm$^{-1}$ |
| $1/\sqrt{\alpha} = \sqrt{\hbar/\mu\omega}$ | 10.7 pm, against a bond length of 127.5 pm |

- The quantum scale of the motion is about ten picometers, a few percent of the bond. A bond is a well-defined length that quivers slightly, not a smeared cloud.
- In the dimensionless position $y = \sqrt{\alpha}\,x$ the constants drop out. Since $d/dx = \sqrt{\alpha}\,d/dy$, the kinetic term becomes $-\frac{\hbar^2\alpha}{2\mu}\frac{d^2}{dy^2}$ and the potential $\frac{k}{2\alpha}y^2$. Both prefactors equal $\frac{1}{2}\hbar\omega$ (check: $\hbar^2\alpha/\mu = \hbar\omega$ and $k/\alpha = \hbar\omega$), so

$$
\hat{H} = \frac{\hbar\omega}{2}\left(-\frac{d^2}{dy^2} + y^2\right)
$$

- Every harmonic oscillator, an H-Cl bond or an I-I bond, is this one problem; only $\hbar\omega$ and $1/\sqrt{\alpha}$ change. The figures below use the numpy units of Lecture 4.1, $\hbar = \mu = \omega = 1$, in which $\alpha = 1$ and $y = x$.

### The ground state: guess a Gaussian

The trial-energy slider of [Lecture 3.1](../ch03/01-schrodinger-equation.md) and the numpy ladder of Lecture 4.1 both showed a lowest state shaped like a bell: no nodes, largest at the bottom of the well, dying away on both sides. The simplest bell is a Gaussian. Try

$$
\psi(x) = e^{-\alpha x^2/2}
$$

with the width parameter $\alpha$ still unknown. (It will turn out to be the $\alpha$ above, hence the name.)

**Step 1: two derivatives.** By the chain rule,

$$
\psi' = -\alpha x\,e^{-\alpha x^2/2}, \qquad \psi'' = \left(\alpha^2x^2 - \alpha\right)e^{-\alpha x^2/2}
$$

**Step 2: apply $\hat{H}$.**

$$
\hat{H}\psi = -\frac{\hbar^2}{2\mu}\left(\alpha^2x^2 - \alpha\right)\psi + \frac{1}{2}kx^2\psi = \left[\frac{\hbar^2\alpha}{2\mu} + \left(\frac{k}{2} - \frac{\hbar^2\alpha^2}{2\mu}\right)x^2\right]\psi
$$

**Step 3: demand an eigenfunction.** $\hat{H}\psi = E\psi$ requires the bracket to be the same number $E$ at every $x$, so the $x^2$ term must vanish:

$$
\frac{\hbar^2\alpha^2}{2\mu} = \frac{k}{2} \quad\Longrightarrow\quad \alpha = \frac{\sqrt{\mu k}}{\hbar} = \frac{\mu\omega}{\hbar}
$$

What is left is the energy:

$$
E_0 = \frac{\hbar^2\alpha}{2\mu} = \frac{\hbar^2}{2\mu}\cdot\frac{\mu\omega}{\hbar} = \frac{1}{2}\hbar\omega
$$

The kinetic energy (set by the curvature of the bell) and the potential energy (set by the walls) both change from place to place, and only one width makes their sum the same everywhere. The figure tests three widths by plotting $\hat{H}\psi/\psi$, which for an eigenfunction must be a flat line, the eigenfunction test of [Lecture 3.1](../ch03/01-schrodinger-equation.md):

```{code-cell} python
:tags: [hide-input]
# synced: gaussian_width
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(-2.6, 2.6, 400)
cases = [(0.35, "too wide", GRAY, "rises: not an eigenfunction"),
         (1.0, r"just right: $\alpha = \mu\omega/\hbar$", TEAL, r"flat at $\frac{1}{2}\hbar\omega$: an eigenfunction"),
         (2.8, "too narrow", GRAY, "falls: not an eigenfunction")]
fig, axes = plt.subplots(2, 3, figsize=(9.6, 4.9), sharex=True,
                         gridspec_kw={"height_ratios": [1.1, 1], "hspace": 0.22, "wspace": 0.1})
for c, (a, name, col, verdict) in enumerate(cases):
    top, bot = axes[0, c], axes[1, c]
    top.plot(x, 0.5 * x**2, color="k", lw=2)
    top.fill_between(x, 0, 1.5 * np.exp(-a * x**2 / 2), color=col, alpha=0.2, lw=0)
    top.plot(x, 1.5 * np.exp(-a * x**2 / 2), color=col, lw=2.4)
    top.set_ylim(0, 3.3); top.set_yticks([])
    top.set_title(name, color=col, fontsize=12.5, weight="bold")
    el = a / 2 + 0.5 * (1 - a * a) * x**2                   # H psi / psi for psi = exp(-a x^2 / 2)
    bot.axhline(0.5, color=CARDINAL, lw=1, ls="--")
    bot.plot(x, el, color=col, lw=2.6)
    bot.set_ylim(-1.2, 2.4); bot.set_yticks([0, 0.5, 1, 2]); bot.set_yticklabels(["0", r"$\frac{1}{2}$", "1", "2"])
    bot.set_xticks([]); bot.spines["bottom"].set_visible(False)
    bot.set_xlabel(verdict, fontsize=11.5, color=col)
    if c:
        bot.set_yticklabels([])
axes[0, 0].set_ylabel(r"$V(x)$ and trial $\psi$", fontsize=11)
axes[1, 0].set_ylabel(r"$\hat{H}\psi\,/\,\psi$  ($\hbar\omega$)", fontsize=11)
fig.subplots_adjust(left=0.08, right=0.99, top=0.93, bottom=0.08)
plt.show()
```

Fig. Three trial Gaussians in the well $V = \frac{1}{2}kx^2$ (top) and the ratio $\hat{H}\psi/\psi$ for each (bottom), in units with $\hbar = \mu = \omega = 1$. A Gaussian that is too wide curves too little to balance the walls, and the ratio grows with $|x|$; one that is too narrow overshoots. Only $\alpha = \mu\omega/\hbar$ gives the same value, $\frac{1}{2}\hbar\omega$, at every $x$.

- Normalize with the Gaussian integral $\int_{-\infty}^{\infty} e^{-\alpha x^2}dx = \sqrt{\pi/\alpha}$: the prefactor is $(\alpha/\pi)^{1/4}$.
- The bell changes from bending down to bending up at $x = \pm 1/\sqrt{\alpha}$ (its inflection points, [Appendix A.1](../math/01-calculus.md)). These are exactly the classical turning points of the energy $\frac{1}{2}\hbar\omega$, where $\frac{1}{2}kx^2 = \frac{1}{2}\hbar\omega$. It is the curvature rule of [the finite well](../ch03/03-tunneling-and-finite-square-well.md): $\psi$ bends toward the axis where $E > V$ and away from it where $E < V$.

### Zero-point energy

The lowest energy is not at the bottom of the well. Even at absolute zero a bond keeps $\frac{1}{2}\hbar\omega$ of vibrational energy, its **zero-point energy**. A classical spring can sit still at $x = 0$ with $E = 0$. Why can't the quantum one?

- Sitting still at $x = 0$ means a definite position and a definite momentum, zero. The uncertainty principle of [Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md) forbids that: $\sigma_x\sigma_p \geq \hbar/2$.
- Make it quantitative. For a state centered at the bottom, $\langle x\rangle = \langle p\rangle = 0$, so $\langle x^2\rangle = \sigma_x^2$ and $\langle p^2\rangle = \sigma_p^2$. With $\sigma_p \geq \hbar/2\sigma_x$, the average energy is at least

$$
\langle E\rangle = \frac{\sigma_p^2}{2\mu} + \frac{1}{2}k\sigma_x^2 \;\geq\; \frac{\hbar^2}{8\mu\sigma_x^2} + \frac{1}{2}k\sigma_x^2
$$

- Squeezing the state (small $\sigma_x$) raises the first term; letting it spread raises the second.

```{code-cell} python
:tags: [hide-input]
# synced: zpe_tradeoff
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
s = np.linspace(0.16, 1.75, 400)                            # sigma_x of a Gaussian with sigma_x sigma_p = hbar / 2
K, V = 1 / (8 * s**2), 0.5 * s**2
fig = plt.figure(figsize=(9.6, 4.1))
ax = fig.add_axes([0.08, 0.17, 0.6, 0.8])
ax.plot(s, K, color=ORANGE, lw=2.4, label=r"kinetic: $\sigma_p^2/2\mu = \hbar^2/8\mu\sigma_x^2$")
ax.plot(s, V, color=TEAL, lw=2.4, label=r"potential: $\frac{1}{2}k\sigma_x^2$")
ax.plot(s, K + V, color="k", lw=2.8, label="total")
s0 = np.sqrt(0.5)
ax.plot([s0], [0.5], "o", color=CARDINAL, ms=10, zorder=5)
ax.annotate(r"lowest: $E_0 = \frac{1}{2}\hbar\omega$" + "\n" + r"at $\sigma_x = 1/\sqrt{2\alpha}$", xy=(s0, 0.5),
            xytext=(1.0, 0.13), fontsize=12.5, color=CARDINAL,
            arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.4, mutation_scale=14, shrinkB=6))
ax.set_xlim(0.15, 1.75); ax.set_ylim(0, 2.2)
ax.set_xticks([s0, 1, 1.5]); ax.set_xticklabels([r"$\frac{1}{\sqrt{2\alpha}}$", r"$\frac{1}{\sqrt{\alpha}}$", r"$\frac{1.5}{\sqrt{\alpha}}$"], fontsize=12)
ax.set_yticks([0, 0.5, 1, 1.5, 2]); ax.set_yticklabels(["0", r"$\frac{1}{2}$", "1", r"$\frac{3}{2}$", "2"])
ax.set_xlabel(r"width of the state, $\sigma_x$", fontsize=12); ax.set_ylabel(r"average energy ($\hbar\omega$)", fontsize=12)
ax.legend(loc="upper center", frameon=False, fontsize=11.5, bbox_to_anchor=(0.55, 1.0))
xi = np.linspace(-2.8, 2.8, 300)
for y0, sig, txt in ((0.6, 0.3, "squeezed: steep sides,\nhigh kinetic energy"),
                     (0.14, 1.4, "spread out: far up the walls,\nhigh potential energy")):
    ins = fig.add_axes([0.73, y0, 0.25, 0.27])
    ins.plot(xi, 0.5 * xi**2, color="k", lw=1.4)
    ins.fill_between(xi, 0, 2.2 * np.exp(-xi**2 / (4 * sig**2)), color=TEAL, alpha=0.3, lw=0)
    ins.plot(xi, 2.2 * np.exp(-xi**2 / (4 * sig**2)), color=TEAL, lw=1.6)
    ins.set_ylim(0, 3.2); ins.axis("off")
    ins.set_title(txt, fontsize=10.5, color=GRAY)
plt.show()
```

Fig. The smallest average energy a state of width $\sigma_x$ can have, in units of $\hbar\omega$: the kinetic energy forced by the uncertainty principle (orange), the potential energy (teal), and their sum (black). The sum is lowest, $\frac{1}{2}\hbar\omega$, at $\sigma_x = 1/\sqrt{2\alpha}$.

- Find the minimum: the derivative with respect to $\sigma_x$ is $-\frac{\hbar^2}{4\mu\sigma_x^3} + k\sigma_x = 0$, so $\sigma_x^2 = \frac{\hbar}{2\sqrt{\mu k}} = \frac{1}{2\alpha}$. Each term is then $\frac{1}{4}\hbar\omega$, and the sum is $\frac{1}{2}\hbar\omega$.
- No state can do better, and the Gaussian ground state reaches the bound. It is a **minimum-uncertainty state**, $\sigma_x\sigma_p = \hbar/2$ exactly (Problem 1), with its energy split evenly between kinetic and potential.

:::{important} **Zero-point energy**

$$
\psi_0(x) = \left(\frac{\alpha}{\pi}\right)^{1/4}e^{-\alpha x^2/2}, \qquad E_0 = \frac{1}{2}\hbar\omega, \qquad \alpha = \frac{\mu\omega}{\hbar}
$$

The lowest state is a Gaussian of width $\sigma_x = 1/\sqrt{2\alpha}$. Its energy $\frac{1}{2}\hbar\omega$ is the least the uncertainty principle allows, and a bond keeps it even at absolute zero.
:::

:::{note} **Example: the zero-point energy of HCl**

For HCl, $\hbar\omega$ corresponds to 2990 cm$^{-1}$ (0.371 eV).

- **Zero-point energy**: $E_0 = \frac{1}{2}\hbar\omega = 1495$ cm$^{-1}$ $= 0.185$ eV, seven times $k_BT$ at room temperature (208 cm$^{-1}$).
- **Spread of the bond length** in $v = 0$: $\sigma_x = 1/\sqrt{2\alpha} = 10.7/\sqrt{2}$ pm $= 7.6$ pm, 6% of $R_e = 127.5$ pm.
- **Bond energy**: the Morse well of Lecture 4.1 is $D_e = 4.62$ eV deep, but the molecule starts $E_0$ above its bottom, so breaking the bond costs only $D_0 = D_e - E_0 = 4.62 - 0.19 = 4.43$ eV, the measured value. Tables of bond energies list $D_0$: zero-point energy is part of every bond energy and every reaction energy.
:::

- Heavier isotopes sit lower. $E_0 = \frac{1}{2}\hbar\sqrt{k/\mu}$ falls as $\mu$ grows, while $k$, set by the electrons, stays the same. A C-D bond has less zero-point energy than a C-H bond, so it takes more energy to break, and a reaction that breaks it runs slower: the **kinetic isotope effect** (Problem 4).

### The whole ladder

#### The next state: one node

The first excited state should have one node, at the center. Try $x$ times the same Gaussian, $\psi = x\,e^{-\alpha x^2/2}$. The product rule gives

$$
\psi' = \left(1 - \alpha x^2\right)e^{-\alpha x^2/2}, \qquad \psi'' = \left(\alpha^2x^3 - 3\alpha x\right)e^{-\alpha x^2/2} = \left(\alpha^2x^2 - 3\alpha\right)\psi
$$

so, with the same $\alpha$ as before,

$$
\hat{H}\psi = \left[\frac{3\hbar^2\alpha}{2\mu} + \left(\frac{k}{2} - \frac{\hbar^2\alpha^2}{2\mu}\right)x^2\right]\psi = \frac{3}{2}\hbar\omega\,\psi
$$

One more node, one more $\hbar\omega$.

#### The pattern: Hermite polynomials

Every state is a polynomial times the same Gaussian. The polynomials are the **Hermite polynomials** $H_v$, written in the dimensionless position $y = \sqrt{\alpha}\,x$:

| $v$ | $H_v(y)$ | $E_v$ | nodes | symmetry |
|:-:|:--|:-:|:-:|:-:|
| 0 | $1$ | $\frac{1}{2}\hbar\omega$ | 0 | even |
| 1 | $2y$ | $\frac{3}{2}\hbar\omega$ | 1 | odd |
| 2 | $4y^2 - 2$ | $\frac{5}{2}\hbar\omega$ | 2 | even |
| 3 | $8y^3 - 12y$ | $\frac{7}{2}\hbar\omega$ | 3 | odd |
| 4 | $16y^4 - 48y^2 + 12$ | $\frac{9}{2}\hbar\omega$ | 4 | even |

- Each polynomial follows from the two before it by the **recursion** $H_{v+1}(y) = 2y\,H_v(y) - 2v\,H_{v-1}(y)$. Check: $H_2 = 2y(2y) - 2(1)(1) = 4y^2 - 2$.

:::{important} **Energies and wavefunctions of the harmonic oscillator**

$$
E_v = \hbar\omega\left(v + \frac{1}{2}\right), \qquad \psi_v(x) = N_v\,H_v\!\left(\sqrt{\alpha}\,x\right)e^{-\alpha x^2/2}, \qquad v = 0, 1, 2, \dots
$$

- $\omega = \sqrt{k/\mu}$ and $\alpha = \mu\omega/\hbar$
- $H_v$ is the Hermite polynomial of degree $v$, and $N_v = \dfrac{1}{\sqrt{2^v v!}}\left(\dfrac{\alpha}{\pi}\right)^{1/4}$ normalizes $\psi_v$
- The levels are evenly spaced by $\hbar\omega$, and the lowest sits $\frac{1}{2}\hbar\omega$ above the bottom of the well
:::

```{code-cell} python
:tags: [hide-input]
# synced: ho_ladder
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The first six states of the harmonic oscillator, each drawn on its energy level in the well, in units with $\hbar = \mu = \omega = 1$. Left: $\psi_v$, with $v$ nodes. Right: the probability density $\lvert\psi_v\rvert^2$. Black dots mark the classical turning points, where $V = E_v$; orange marks the parts of each state beyond them.

- **Nodes**: $\psi_v$ has $v$ nodes, as in the box. More nodes means more curvature, more kinetic energy, and a higher rung.
- **Equal steps**: in a box the gaps grow as $n^2$. Here the well widens as the energy rises, giving each new node more room, and the two effects balance exactly. The rough argument at the end of Lecture 4.1 got $E \propto n$; the raising operator below gets exactly $\hbar\omega$.
- **One frequency**: every gap is a multiple of $\hbar\omega$, so every Bohr frequency $(E_m - E_n)/\hbar$ of [Lecture 3.7](../ch03/07-time-dependence.md) is a multiple of $\omega$. Any state in the well therefore returns to its starting shape after one classical period $2\pi/\omega$. That is why the packet of Lecture 3.7 swung exactly like a mass on a spring.

The formula and the numpy ladder of Lecture 4.1 agree. In units with $\hbar = \mu = \omega = 1$ (so $\alpha = 1$ and $y = x$):

```{code-cell} python
import numpy as np
from math import factorial

N = 400                                       # the spring on a grid, as in Lecture 4.1
x = np.linspace(-8, 8, N); dx = x[1] - x[0]
D2 = (np.eye(N, k=1) - 2 * np.eye(N) + np.eye(N, k=-1)) / dx**2
E, psi = np.linalg.eigh(-0.5 * D2 + np.diag(0.5 * x**2))
psi = psi / np.sqrt(dx)                       # unit vectors -> normalized functions
psi = psi * np.sign(psi[N - 100])             # sign convention: positive at x = 4

H2 = 4 * x**2 - 2                             # the Hermite polynomial H_2
psi2 = H2 * np.exp(-x**2 / 2) / np.sqrt(2**2 * factorial(2) * np.sqrt(np.pi))
print("energies:", np.round(E[:5], 4))
print("largest difference between the two psi_2:", round(np.abs(psi[:, 2] - psi2).max(), 5))
```

The energies agree with $v + \frac{1}{2}$ to better than 0.1%, and the two versions of $\psi_2$ differ by a few parts in ten thousand, the error of the grid.

### Even and odd states

The well is symmetric, $V(-x) = V(x)$, and the states alternate between even and odd:

$$
\psi_v(-x) = (-1)^v\,\psi_v(x)
$$

The Gaussian is even, and a Hermite polynomial of even degree contains only even powers of $y$, one of odd degree only odd powers. Symmetry settles many integrals without computing them, using three rules:

1. The integral of an odd function over a symmetric range is zero: the left half cancels the right half.
2. Products follow the signs: even times even and odd times odd are even, even times odd is odd.
3. A derivative flips the symmetry: the slope of an even function is odd, and of an odd function even (the slope of $x^2$ is $2x$).

In every state $\psi_v$:

- $\langle x\rangle = \int \psi_v\,x\,\psi_v\,dx = 0$, because $\lvert\psi_v\rvert^2$ is even and $x$ is odd. The oscillator is centered at the bottom of the well.
- $\langle p\rangle = -i\hbar\int\psi_v\,\psi_v'\,dx = 0$, because $\psi_v'$ has the opposite symmetry to $\psi_v$, so the integrand is odd. Moving left and moving right are equally likely.
- $\langle x^2\rangle$ and $\langle p^2\rangle$ are not zero: they are averages of quantities that are never negative. The spreads $\sigma_x$ and $\sigma_p$ carry the zero-point motion.

Eigenfunctions of a Hermitian operator with different eigenvalues are orthogonal ([Operators 2](../ch03/05-hermitian-operators-and-commutators.md)). Symmetry shows half of this at a glance:

```{code-cell} python
:tags: [hide-input]
# synced: ho_orthogonality
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Products of oscillator states, positive area purple and negative area orange. Left: $\psi_0\psi_1$ is odd, and its two halves cancel. Middle: $\psi_0\psi_2$ is even, but its negative middle exactly cancels its positive wings. Right: $\psi_1\psi_1 = \lvert\psi_1\rvert^2$ is never negative and has area 1.

$$
\langle v'|v\rangle = \int_{-\infty}^{\infty}\psi_{v'}(x)\,\psi_v(x)\,dx = \delta_{v'v}
$$

### Beyond the turning points, and back to the classical spring

A classical oscillator of energy $E$ turns around where $\frac{1}{2}kx^2 = E$. For $E_v = \hbar\omega\left(v + \frac{1}{2}\right)$, using $\hbar\omega/k = 1/\alpha$, the turning points are

$$
x = \pm\sqrt{\frac{2v + 1}{\alpha}}
$$

Every state in the ladder figure leaks past them (orange). The oscillator is found where its kinetic energy would be negative, like the particle in [the finite well](../ch03/03-tunneling-and-finite-square-well.md).

:::{note} **Example: how often is the ground state beyond its turning points?**

For $v = 0$ the turning points are at $x = \pm 1/\sqrt{\alpha}$, which is $y = \pm 1$. With $dx = dy/\sqrt{\alpha}$, the density is $\lvert\psi_0\rvert^2dx = \pi^{-1/2}e^{-y^2}dy$, so

$$
P(\text{beyond}) = 1 - \frac{1}{\sqrt{\pi}}\int_{-1}^{1} e^{-y^2}\,dy = 0.157
$$

The integral has no closed form (it is tabulated as the error function), but one line of numpy evaluates it:

```{code-cell} python
y = np.linspace(-1, 1, 20001)                 # between the turning points of v = 0
inside = np.trapezoid(np.exp(-y**2) / np.sqrt(np.pi), y)
print(f"inside: {inside:.4f}   beyond: {1 - inside:.4f}")
```

About one time in six, a bond in its ground state is caught stretched or compressed beyond where a classical spring of the same energy could reach. For HCl the turning points are $\pm 10.7$ pm from $R_e$.
:::

Lecture 4.1 found where a classical spring spends its time: most often near the turning points, where it moves slowest, $P(x) = 1/\pi\sqrt{A^2 - x^2}$. The quantum ground state does the opposite and peaks in the middle. The animation climbs the ladder, with the classical curve of the same energy fixed in place:

```{code-cell} python
:tags: [hide-input]
# synced: classical_limit
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. The probability density of state $v$ (teal) and of a classical spring with the same energy (red), with position measured in units of the turning point so that both share one scale. As $v$ grows the quantum density piles up near the turning points, its wiggles become finer, and the share beyond the turning points shrinks.

- At large $v$ the wiggles are too fine to resolve, and their average follows the classical curve: the **correspondence principle**, as for the particle in a box at large $n$ ([Lecture 3.2](../ch03/02-particle-in-a-box.md)).
- Molecules live at the other end. At room temperature nearly every bond is in $v = 0$ (Lecture 4.1), the most quantum state of all: a Gaussian centered where a classical spring is least likely to be.

### Why the steps are equal: raising and lowering operators

The Hermite polynomials give the states one at a time. An idea of Dirac's gives the whole ladder at once, and shows why the rungs are exactly $\hbar\omega$ apart. Work in the dimensionless position $y = \sqrt{\alpha}\,x$, where

$$
\hat{H} = \frac{\hbar\omega}{2}\left(y^2 - \frac{d^2}{dy^2}\right)
$$

#### Factor the Hamiltonian

For numbers, a sum of two squares factors: $u^2 + w^2 = (u - iw)(u + iw)$. The Hamiltonian is a sum of two squares too, $y^2$ and $\hat{P}^2$ with $\hat{P} = -i\,d/dy$. Since $i\hat{P} = d/dy$, the same factors would be $y \mp d/dy$. Define

$$
\hat{a} = \frac{1}{\sqrt{2}}\left(y + \frac{d}{dy}\right), \qquad \hat{a}^\dagger = \frac{1}{\sqrt{2}}\left(y - \frac{d}{dy}\right)
$$

$\hat{a}^\dagger$ is the adjoint of $\hat{a}$: $y$ is Hermitian, and $d/dy$ changes sign under the adjoint ([Operators 2](../ch03/05-hermitian-operators-and-commutators.md)).

#### The leftover is a commutator

Multiply in the order $\hat{a}^\dagger\hat{a}$ and act on a test function $f(y)$, as in Operators 2:

$$
\hat{a}^\dagger\hat{a}f = \frac{1}{2}\left(y - \frac{d}{dy}\right)\left(yf + f'\right) = \frac{1}{2}\left(y^2f + yf' - f - yf' - f''\right) = \frac{1}{2}\left(y^2f - f''\right) - \frac{1}{2}f
$$

The $-f$ comes from the product rule, $\frac{d}{dy}(yf) = f + yf'$. It is the only thing that keeps the operators from factoring like numbers. Reading off the operator:

$$
\hat{a}^\dagger\hat{a} = \frac{1}{2}\left(y^2 - \frac{d^2}{dy^2}\right) - \frac{1}{2} = \frac{\hat{H}}{\hbar\omega} - \frac{1}{2} \qquad\Longrightarrow\qquad \hat{H} = \hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2}\right)
$$

The other order gives $+\frac{1}{2}$ instead of $-\frac{1}{2}$ (Problem 6), so $[\hat{a}, \hat{a}^\dagger] = \hat{a}\hat{a}^\dagger - \hat{a}^\dagger\hat{a} = 1$.

- The zero-point energy $\frac{1}{2}\hbar\omega$ is exactly the piece left over because $y$ and $d/dy$ do not commute. If they did, the factorization would be exact and the lowest energy would be zero, as for a classical spring.

#### Climbing the ladder

Let $\psi$ be an eigenfunction with energy $E$. Apply $\hat{H}$ to $\hat{a}^\dagger\psi$, using $\hat{a}\hat{a}^\dagger = \hat{a}^\dagger\hat{a} + 1$ in the middle:

$$
\hat{H}\hat{a}^\dagger = \hbar\omega\left(\hat{a}^\dagger\hat{a}\hat{a}^\dagger + \frac{1}{2}\hat{a}^\dagger\right) = \hbar\omega\,\hat{a}^\dagger\left(\hat{a}^\dagger\hat{a} + 1 + \frac{1}{2}\right) = \hat{a}^\dagger\left(\hat{H} + \hbar\omega\right)
$$

so

$$
\hat{H}\left(\hat{a}^\dagger\psi\right) = \hat{a}^\dagger\left(\hat{H} + \hbar\omega\right)\psi = \left(E + \hbar\omega\right)\left(\hat{a}^\dagger\psi\right)
$$

$\hat{a}^\dagger\psi$ is again an eigenfunction, with energy exactly $\hbar\omega$ higher: $\hat{a}^\dagger$ is the **raising operator**. The same steps show that $\hat{a}\psi$ has energy $E - \hbar\omega$ (Problem 6): $\hat{a}$ is the **lowering operator**.

#### The ladder has a bottom

Kinetic and potential energy are never negative, so no state has energy below zero, and stepping down cannot go on forever. It must stop at a state that $\hat{a}$ turns into nothing:

$$
\hat{a}\psi_0 = 0 \quad\Longrightarrow\quad \frac{d\psi_0}{dy} = -y\,\psi_0 \quad\Longrightarrow\quad \psi_0 \propto e^{-y^2/2} = e^{-\alpha x^2/2}
$$

the Gaussian again, this time from a first-order equation. Its energy is $\hat{H}\psi_0 = \hbar\omega\left(\hat{a}^\dagger\hat{a}\psi_0 + \frac{1}{2}\psi_0\right) = \frac{1}{2}\hbar\omega\,\psi_0$. Climbing $v$ rungs from there adds $v\hbar\omega$, which gives $E_v = \hbar\omega\left(v + \frac{1}{2}\right)$. No other energies exist: a state at any other energy could be lowered below zero.

- One step up from the Gaussian, using $\frac{d}{dy}e^{-y^2/2} = -y\,e^{-y^2/2}$: $\hat{a}^\dagger\psi_0 \propto \left(y + y\right)e^{-y^2/2} \propto H_1(y)\,e^{-y^2/2}$, the state $\psi_1$.

```{code-cell} python
:tags: [hide-input]
# synced: ladder_climb
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Left: the raising operator $\hat{a}^\dagger$ moves a state up one rung (orange) and the lowering operator $\hat{a}$ down one (purple); $\hat{a}\psi_0 = 0$ ends the ladder at $\frac{1}{2}\hbar\omega$. Right: raising the Gaussian once gives $\psi_1$, and twice gives $\psi_2$. Each step multiplies by a polynomial one degree higher and adds a node.

:::{important} **Raising and lowering operators**

$$
\hat{a} = \frac{1}{\sqrt{2}}\left(y + \frac{d}{dy}\right), \qquad \hat{a}^\dagger = \frac{1}{\sqrt{2}}\left(y - \frac{d}{dy}\right), \qquad y = \sqrt{\alpha}\,x
$$

$$
\hat{H} = \hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2}\right), \qquad [\hat{a}, \hat{a}^\dagger] = 1
$$

$$
\hat{a}^\dagger\psi_v = \sqrt{v + 1}\,\psi_{v+1}, \qquad \hat{a}\,\psi_v = \sqrt{v}\,\psi_{v-1}, \qquad \hat{a}\,\psi_0 = 0
$$
:::

- The square roots keep the states normalized. The length squared of $\hat{a}^\dagger\psi_v$ is $\langle\psi_v|\hat{a}\hat{a}^\dagger|\psi_v\rangle = \langle\psi_v|\hat{a}^\dagger\hat{a} + 1|\psi_v\rangle = v + 1$.
- $\hat{a}^\dagger\hat{a}\,\psi_v = v\,\psi_v$: the product counts the rungs, and is called the **number operator**.

### Position connects only neighboring levels

Add the two operators: $\hat{a} + \hat{a}^\dagger = \sqrt{2}\,y$. Position is therefore one step down plus one step up:

$$
\hat{x} = \frac{y}{\sqrt{\alpha}} = \frac{\hat{a} + \hat{a}^\dagger}{\sqrt{2\alpha}}, \qquad \hat{x}\,\psi_v = \frac{1}{\sqrt{2\alpha}}\left(\sqrt{v + 1}\,\psi_{v+1} + \sqrt{v}\,\psi_{v-1}\right)
$$

(This is the Hermite recursion $2yH_v = H_{v+1} + 2vH_{v-1}$ in disguise.) Multiply by $\psi_{v'}$ and integrate; orthonormality keeps two terms at most:

$$
\langle v'|\hat{x}|v\rangle = \frac{1}{\sqrt{2\alpha}}\left(\sqrt{v + 1}\;\delta_{v',v+1} + \sqrt{v}\;\delta_{v',v-1}\right)
$$

In the matrix language of [Lecture 3.5](../ch03/04-operators.md): in the oscillator's own eigenbasis $\hat{H}$ is diagonal, and $\hat{x}$ has entries only next to the diagonal.

```{code-cell} python
:tags: [hide-input]
# synced: x_matrix
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The Hamiltonian (left) and position (right) as matrices in the basis of oscillator states $v = 0$ to 6. $\hat{H}$ is diagonal, with the energies $v + \frac{1}{2}$. $\hat{x}$ has a zero diagonal, since $\langle x\rangle = 0$ in every state, and nonzero entries $\sqrt{(v + 1)/2}$ only where $v'$ and $v$ differ by one.

numpy builds the same matrix from the grid states of the earlier cell: sandwich each pair of eigenvectors around the diagonal matrix of positions, as in Lecture 3.5.

```{code-cell} python
V = psi[:, :6] * np.sqrt(dx)                  # the first six eigenvectors, unit length again
X = V.T @ np.diag(x) @ V                      # <v'|x|v>, in units of 1/sqrt(alpha)
print(np.round(X, 3) + 0)                     # + 0 turns -0.0 into 0.0
```

The entries next to the diagonal are $\sqrt{1/2} = 0.707$, $1$, $\sqrt{3/2} = 1.225$, $\sqrt{2} = 1.414$ and $\sqrt{5/2} = 1.581$, up to the grid error; everything else is zero.

:::{important} **Position connects neighboring levels**

$$
\hat{x} = \frac{\hat{a} + \hat{a}^\dagger}{\sqrt{2\alpha}}, \qquad \langle v'|\hat{x}|v\rangle = 0 \quad\text{unless}\quad v' = v \pm 1
$$
:::

- This is the origin of the **infrared selection rule** of [Lecture 4.3](03-molecular-vibrations.md). Light couples to a vibrating molecule through its dipole moment, which to first order changes in proportion to the stretch $x$. Light can drive only the transitions for which $\langle v'|\hat{x}|v\rangle \neq 0$: in a harmonic molecule, one rung at a time, $\Delta v = \pm 1$. Every allowed jump has the same energy $\hbar\omega$, so each vibration gives one strong infrared line.
- Powers of $\hat{x}$ reach further: $\hat{x}^2 \propto (\hat{a} + \hat{a}^\dagger)^2$ moves up to two rungs, and gives $\langle x^2\rangle$ in any state in two lines (Problem 8).
- Real bonds are softer than a parabola at large stretch. Their levels bunch together toward the dissociation limit, and weak overtones with $\Delta v = 2, 3$ appear; [Lecture 4.3](03-molecular-vibrations.md) adds this anharmonicity.

### Problems

#### Problem 1: The minimum-uncertainty state

Compute $\sigma_x$ and $\sigma_p$ for the ground state $\psi_0 = (\alpha/\pi)^{1/4}e^{-\alpha x^2/2}$ and show that $\sigma_x\sigma_p = \hbar/2$. Use $\int_{-\infty}^{\infty}e^{-\alpha x^2}dx = \sqrt{\pi/\alpha}$ and $\int_{-\infty}^{\infty}x^2e^{-\alpha x^2}dx = \frac{1}{2\alpha}\sqrt{\pi/\alpha}$.

:::{admonition} **Solution**
:class: dropdown solution

By symmetry $\langle x\rangle = \langle p\rangle = 0$ ($\lvert\psi_0\rvert^2$ is even, $\psi_0\psi_0'$ is odd), so $\sigma_x^2 = \langle x^2\rangle$ and $\sigma_p^2 = \langle p^2\rangle$.

$$
\langle x^2\rangle = \left(\frac{\alpha}{\pi}\right)^{1/2}\int_{-\infty}^{\infty}x^2e^{-\alpha x^2}dx = \left(\frac{\alpha}{\pi}\right)^{1/2}\frac{1}{2\alpha}\left(\frac{\pi}{\alpha}\right)^{1/2} = \frac{1}{2\alpha}
$$

For $\langle p^2\rangle$ use $\psi_0'' = (\alpha^2x^2 - \alpha)\psi_0$ from the lecture:

$$
\langle p^2\rangle = -\hbar^2\int_{-\infty}^{\infty}\psi_0\,\psi_0''\,dx = -\hbar^2\left(\alpha^2\langle x^2\rangle - \alpha\right) = -\hbar^2\left(\frac{\alpha}{2} - \alpha\right) = \frac{\hbar^2\alpha}{2}
$$

So $\sigma_x = 1/\sqrt{2\alpha}$, $\sigma_p = \hbar\sqrt{\alpha/2}$, and

$$
\sigma_x\sigma_p = \frac{1}{\sqrt{2\alpha}}\cdot\hbar\sqrt{\frac{\alpha}{2}} = \frac{\hbar}{2}
$$

the smallest product the uncertainty principle allows. As a check on the energy: $\langle p^2\rangle/2\mu = \hbar^2\alpha/4\mu = \frac{1}{4}\hbar\omega$ and $\frac{1}{2}k\langle x^2\rangle = k/4\alpha = \frac{1}{4}\hbar\omega$, which add to $E_0 = \frac{1}{2}\hbar\omega$.
:::

#### Problem 2: How sharp is a bond?

Carbon monoxide, $^{12}$C$^{16}$O, vibrates at $\tilde{\nu} = 2170$ cm$^{-1}$ and has a bond length $R_e = 113$ pm. Find the spread $\sigma_x$ of its bond length in the ground vibrational state, and compare it with $R_e$.

:::{admonition} **Solution**
:class: dropdown solution

From Problem 1, $\sigma_x = 1/\sqrt{2\alpha} = \sqrt{\hbar/2\mu\omega}$, with $\omega = 2\pi c\tilde{\nu}$. The reduced mass is

$$
\mu = \frac{(12.000)(15.995)}{27.995}\ \text{u} = 6.856\ \text{u} = 1.139\times10^{-26}\ \text{kg}
$$

and $\omega = 2\pi\,(2.998\times10^{10}\ \text{cm/s})(2170\ \text{cm}^{-1}) = 4.088\times10^{14}$ s$^{-1}$. Then

$$
\sigma_x = \left[\frac{1.055\times10^{-34}\ \text{J s}}{2\,(1.139\times10^{-26}\ \text{kg})(4.088\times10^{14}\ \text{s}^{-1})}\right]^{1/2} = 3.37\ \text{pm}
$$

That is $3.37/113 = 3.0\%$ of the bond length. CO is heavier and stiffer than HCl, whose spread is 6%.
:::

#### Problem 3: The second excited state

Show that $\psi = \left(2\alpha x^2 - 1\right)e^{-\alpha x^2/2}$ is an eigenfunction of $\hat{H}$ and find its energy. Where are its nodes, and how do they compare with the classical turning points of the same energy? Compare $\psi$ with $H_2(y)\,e^{-y^2/2}$.

#### Problem 4: The kinetic isotope effect

A C-H stretch absorbs near 2900 cm$^{-1}$. (a) Predict the wavenumber of the C-D stretch, treating each as a diatomic with the carbon mass 12 u and the same force constant. (b) Find the difference in zero-point energy. (c) Suppose a reaction breaks this bond, and its transition state has lost the stretch, so both isotopes reach the same barrier top. By about what factor does replacing H with D slow the reaction at 300 K ($k_BT = 208$ cm$^{-1}$)?

:::{admonition} **Solution**
:class: dropdown solution

(a) The force constant is set by the electrons and does not change, so $\tilde{\nu} \propto 1/\sqrt{\mu}$:

$$
\mu_{\text{CH}} = \frac{(12)(1.008)}{13.008} = 0.930\ \text{u}, \qquad \mu_{\text{CD}} = \frac{(12)(2.014)}{14.014} = 1.725\ \text{u}
$$

$$
\tilde{\nu}_{\text{CD}} = 2900\ \text{cm}^{-1}\times\sqrt{\frac{0.930}{1.725}} = 2900 \times 0.734 = 2130\ \text{cm}^{-1}
$$

(b) $E_0 = \frac{1}{2}\hbar\omega$, so the zero-point energies are 1450 and 1065 cm$^{-1}$, a difference of 385 cm$^{-1}$. The C-D bond sits 385 cm$^{-1}$ lower in the same well.

(c) Both climb to the same barrier top, so the C-D bond needs 385 cm$^{-1}$ more activation energy. The Boltzmann factor makes the rate ratio

$$
\frac{k_{\text{H}}}{k_{\text{D}}} \approx e^{385/208} = e^{1.85} \approx 6
$$

Measured primary isotope effects are typically 2 to 7. An effect this large is the standard sign that a C-H bond breaks in the slowest step of a reaction, and it is purely a zero-point energy effect.
:::

#### Problem 5: Beyond the turning points, higher up

Adapt the numpy line of the example to find how often the oscillator is found beyond its turning points in $v = 1$ and in $v = 10$, using the grid `x` and states `psi` from the code cell that checks the Hermite formula. (The turning points are at $x = \pm\sqrt{2v + 1}$ in these units.) Why does the fraction fall as $v$ grows?

#### Problem 6: Ladder algebra

(a) Act with $\hat{a}\hat{a}^\dagger$ on a test function $f(y)$ and show that $[\hat{a}, \hat{a}^\dagger] = 1$. (b) Show that if $\hat{H}\psi = E\psi$, then $\hat{H}(\hat{a}\psi) = (E - \hbar\omega)(\hat{a}\psi)$. (c) Apply $\hat{a}^\dagger$ to $y\,e^{-y^2/2}$ and show that the result is proportional to $H_2(y)\,e^{-y^2/2}$.

:::{admonition} **Solution**
:class: dropdown solution

(a) With the product rule, $\frac{d}{dy}(yf) = f + yf'$:

$$
\hat{a}\hat{a}^\dagger f = \frac{1}{2}\left(y + \frac{d}{dy}\right)\left(yf - f'\right) = \frac{1}{2}\left(y^2f - yf' + f + yf' - f''\right) = \frac{1}{2}\left(y^2f - f''\right) + \frac{1}{2}f
$$

The lecture found $\hat{a}^\dagger\hat{a}f = \frac{1}{2}(y^2f - f'') - \frac{1}{2}f$. Subtracting, $[\hat{a}, \hat{a}^\dagger]f = f$ for every $f$, so $[\hat{a}, \hat{a}^\dagger] = 1$.

(b) Use $\hat{a}^\dagger\hat{a} = \hat{a}\hat{a}^\dagger - 1$:

$$
\hat{H}\hat{a} = \hbar\omega\left(\hat{a}^\dagger\hat{a}\,\hat{a} + \frac{1}{2}\hat{a}\right) = \hbar\omega\left(\hat{a}\hat{a}^\dagger\hat{a} - \hat{a} + \frac{1}{2}\hat{a}\right) = \hat{a}\,\hbar\omega\left(\hat{a}^\dagger\hat{a} + \frac{1}{2} - 1\right) = \hat{a}\left(\hat{H} - \hbar\omega\right)
$$

so $\hat{H}(\hat{a}\psi) = \hat{a}(\hat{H} - \hbar\omega)\psi = (E - \hbar\omega)(\hat{a}\psi)$.

(c) $\frac{d}{dy}\left(y\,e^{-y^2/2}\right) = \left(1 - y^2\right)e^{-y^2/2}$, so

$$
\hat{a}^\dagger\left(y\,e^{-y^2/2}\right) = \frac{1}{\sqrt{2}}\left(y^2 - 1 + y^2\right)e^{-y^2/2} = \frac{1}{\sqrt{2}}\left(2y^2 - 1\right)e^{-y^2/2}
$$

and $2y^2 - 1 = \frac{1}{2}H_2(y)$. One raising step turned the one-node state into the two-node state.
:::

#### Problem 7: Half an oscillator

A particle moves in $V = \frac{1}{2}kx^2$ for $x > 0$, with an impenetrable wall at $x = 0$, so $\psi(0) = 0$. Which states of the full oscillator also solve this problem? What are the allowed energies, and how far apart are they?

#### Problem 8: Average energies in any level

Write $\hat{x}^2$ in terms of $\hat{a}$ and $\hat{a}^\dagger$ (keep the order of the factors). Use the ladder relations to show that $\langle v|\hat{x}^2|v\rangle = (v + \frac{1}{2})/\alpha$, and from this that the average potential energy in any level is half the total, $\langle V\rangle = \frac{1}{2}E_v$. What is the average kinetic energy?
