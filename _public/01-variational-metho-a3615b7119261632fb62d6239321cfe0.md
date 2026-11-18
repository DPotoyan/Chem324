---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Variational Method

:::{note} **What you need to know**

- The Schrödinger equation is solved exactly for the box, the spring, the rotor and the hydrogen atom, and for almost nothing else. Helium already has a term, the repulsion $e^2/4\pi\varepsilon_0 r_{12}$ between its two electrons, that no formula handles. Chemistry runs on two approximation methods: the **variational method** of this lecture and **perturbation theory** of the next two.
- **The variational theorem.** Take any function $\phi$ that obeys the boundary conditions and compute its average energy. The result can never lie below the true ground-state energy: $\langle\phi|\hat{H}|\phi\rangle/\langle\phi|\phi\rangle \geq E_0$. Every guess gives an **upper bound**, so of two guesses the one with the lower energy is the better one.
- **The recipe.** Put adjustable parameters in the guess, compute the energy as a function of them, and minimize. A Gaussian for hydrogen gives $-0.424\,E_h$ against the exact $-0.5$; a screened nuclear charge for helium gives $\zeta = 27/16$ and $-77.5$ eV against $-79.0$ eV.
- **The linear variational method.** Write the guess as a sum of fixed **basis functions**, $\phi = \sum_n c_nf_n$, and vary only the coefficients. Minimizing turns the Schrödinger equation into the matrix problem $\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}$, solved by the **secular determinant** $\det(\mathbf{H} - E\,\mathbf{S}) = 0$ or by one line of numpy. Adding basis functions can only lower the energy.
- Two functions that mix give two levels pushed apart, $E_\pm$: one below both starting energies and one above. This **two-level problem** returns as perturbation theory in Lecture 6.2, as absorption of light in Lecture 6.3 and as the chemical bond in Chapter 8. Every electronic-structure program solves the same equation with thousands of basis functions.

:::

### Where exact solutions stop

Four model systems have carried the course so far, and each was solved exactly:

| system | potential | solved in |
| :-- | :-- | :-- |
| particle in a box | walls | [Lecture 3.2](../ch03/02-particle-in-a-box.md) |
| harmonic oscillator | $\frac{1}{2}kx^2$ | [Lecture 4.2](../ch04/02-quantum-harmonic-oscillator.md) |
| rigid rotor | none, fixed distance | [Lecture 4.5](../ch04/05-rigid-rotor.md) |
| hydrogenlike atom | $-Ze^2/4\pi\varepsilon_0 r$ | [Lecture 5.1](../ch05/01-hydrogenlike-atoms.md) |

The list ends there. Add one electron to hydrogen and the Hamiltonian of helium, written in the atomic units of Lecture 5.1 ($\hbar = m_e = e = 4\pi\varepsilon_0 = 1$), is

$$
\hat{H} = \underbrace{-\tfrac{1}{2}\nabla_1^2 - \frac{2}{r_1}}_{\text{electron 1}}\;\;\underbrace{-\,\tfrac{1}{2}\nabla_2^2 - \frac{2}{r_2}}_{\text{electron 2}}\;+\;\underbrace{\frac{1}{r_{12}}}_{\text{repulsion}}
$$

The first two pieces are hydrogenlike atoms with $Z = 2$, which Lecture 5.1 solved. The last piece, the repulsion between the electrons a distance $r_{12}$ apart, ties the coordinates of one electron to those of the other. The equation no longer separates, and no one has found a formula for its solutions. The same term appears between every pair of electrons in every atom and molecule.

```{code-cell} python
:tags: [hide-input]
# synced: approx_roadmap
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
plt.show()
```

Fig. The plan of the chapter. Beyond the exactly solved models there are two ways forward: guess the wavefunction and improve the guess (the variational method), or start from a solved problem and correct it step by step (perturbation theory). Both lead to the atoms and molecules of Chapters 7 and 8.

- **The variational method** asks for a guess of the wavefunction. It returns an energy that is guaranteed to be too high, so guesses can be ranked and improved.
- **Perturbation theory** asks for a solved problem close to the real one. It returns corrections to the energies and states, order by order ([Lecture 6.2](02-perturbation-theory.md)), and with a perturbation that changes in time it explains how light moves molecules between levels ([Lecture 6.3](03-time-dependent-perturbation-and-selection-rules.md)).

### An idea already used twice

Two earlier lectures found a ground-state energy by trying a family of states and keeping the one of lowest energy.

- **The spring** ([Lecture 4.2](../ch04/02-quantum-harmonic-oscillator.md)). Gaussians of every width $\sigma_x$, centered in the well, have the average energy $\hbar^2/8\mu\sigma_x^2 + \frac{1}{2}k\sigma_x^2$. The lowest value is $\frac{1}{2}\hbar\omega$, the zero-point energy.
- **The hydrogen atom** ([Lecture 5.1](../ch05/01-hydrogenlike-atoms.md)). Exponentials $e^{-r/a}$ of every size $a$ have the average energy $\hbar^2/2\mu a^2 - e^2/4\pi\varepsilon_0 a$. The lowest value is $-\frac{1}{2}E_h = -13.6$ eV, at $a = a_0$.

Both answers were exact, because in each case the family happened to contain the true ground state. This lecture asks what the minimum means when it does not. The answer is the variational theorem: the minimum is then too high, and never too low.

### The variational theorem

#### Any state is a mixture of the exact states

Let $\phi$ be any normalized function that obeys the boundary conditions of the problem: a guess, called a **trial function**. Its average energy is $\langle E\rangle = \langle\phi|\hat{H}|\phi\rangle$. Three steps bound it from below.

1. **Expand the guess in the exact states.** The eigenfunctions of $\hat{H}$ form a complete set ([Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md)), whether or not anyone can write them down:

$$
\phi = \sum_n c_n\,\psi_n, \qquad \hat{H}\psi_n = E_n\psi_n, \qquad E_0 \leq E_1 \leq E_2 \leq \dots
$$

Since $\phi$ is normalized, $\sum_n|c_n|^2 = 1$.


2. **The average energy is a weighted average of the levels.** A measurement of the energy returns $E_n$ with probability $|c_n|^2$ (the Born rule of Lecture 3.6), so

$$
\langle E\rangle = \langle\phi|\hat{H}|\phi\rangle = \sum_n|c_n|^2\,E_n
$$

3. **An average cannot lie below its smallest entry.** Every $E_n$ is at least $E_0$, so

$$
\langle E\rangle = \sum_n|c_n|^2\,E_n \;\geq\; E_0\sum_n|c_n|^2 = E_0
$$

Here $E_0$ stands for the lowest level, whatever its quantum number is called: $n = 1$ for the box and for hydrogen, $v = 0$ for the spring.

```{code-cell} python
:tags: [hide-input]
# synced: weights_ladder
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Left: a trial state $\phi$ in a box (teal), pushed toward the right wall, beside the true ground state $\psi_1$ (dashed). Right: the weights $|c_n|^2$ of $\phi$ on the exact levels. An energy measurement returns $E_1$ in 68% of trials, $E_2$ in 29%, higher levels in the rest. The average, $2.19\,E_1$, lies above $E_1$ because every single reading does.

:::{important} **The variational theorem**

$$
E_\phi = \frac{\langle\phi|\hat{H}|\phi\rangle}{\langle\phi|\phi\rangle} \;\geq\; E_0
$$

- $\phi$ is any trial function that obeys the boundary conditions, and $E_0$ is the true ground-state energy
- The denominator normalizes the guess; it is 1 if $\phi$ is already normalized
- Equality holds only when $\phi$ is the true ground state $\psi_0$
:::

- **Every guess gives an upper bound.** The true energy is never above the computed one. No knowledge of the exact solution is needed to say so.
- **Lower is better.** Of two trial functions, the one with the lower $E_\phi$ is closer to the truth in energy. That turns guessing into a method: change the guess, keep the change if the energy drops.
- **The energy forgives a poor guess.** Let the guess be the true ground state plus a small error, $\phi = \psi_0 + \epsilon\,\chi$, with $\chi$ normalized and orthogonal to $\psi_0$. Then

$$
E_\phi = \frac{E_0 + \epsilon^2\,\langle\chi|\hat{H}|\chi\rangle}{1 + \epsilon^2} \approx E_0 + \epsilon^2\left(\langle\chi|\hat{H}|\chi\rangle - E_0\right)
$$

  An error of size $\epsilon$ in the function costs only $\epsilon^2$ in the energy. A guess that is 10% wrong can give an energy good to about 1%. The reverse also holds: a good energy does not certify the wavefunction, and other properties computed from it are less accurate.
- **The theorem is about the ground state.** For an excited state the same argument works only if the trial function is orthogonal to every state below it. Symmetry can arrange that: an odd trial function in a symmetric well bounds the lowest odd state (Problem 7).

### The recipe: guess, compute, minimize

1. **Guess.** Choose a trial function $\phi$ with the right boundary conditions and a sensible shape: no more nodes than a ground state should have, large where the potential is low. Put adjustable parameters in it.
2. **Compute.** Evaluate $E_\phi = \langle\phi|\hat{H}|\phi\rangle/\langle\phi|\phi\rangle$ as a function of the parameters.
3. **Minimize.** Set the derivative with respect to each parameter to zero. The minimum is the best energy that family of functions can give, and it is still an upper bound.

One formula saves work in step 2. Integrating by parts, with $\phi$ vanishing at the ends of the range,

$$
\langle\phi|\hat{T}|\phi\rangle = -\frac{\hbar^2}{2m}\int\phi\,\phi''\,dx = \frac{\hbar^2}{2m}\int\left(\phi'\right)^2dx
$$

so the kinetic energy needs only the first derivative: it is large wherever the function is steep.

#### No parameter: a parabola in a box

:::{note} **Example: guess the ground state of a box**

A particle in a box of length $L$ has the ground state $\sqrt{2/L}\,\sin(\pi x/L)$ with $E_1 = \pi^2\hbar^2/2mL^2$. Pretend not to know it, and guess the simplest function that vanishes at both walls, $\phi = x(L - x)$. What energy does the guess give?

Inside the box $\hat{H} = -(\hbar^2/2m)\,d^2/dx^2$, and $\phi'' = -2$, so $\hat{H}\phi = \hbar^2/m$, a constant. The two integrals are

$$
\langle\phi|\hat{H}|\phi\rangle = \frac{\hbar^2}{m}\int_0^L x(L - x)\,dx = \frac{\hbar^2L^3}{6m}
$$

$$
\langle\phi|\phi\rangle = \int_0^L x^2(L - x)^2\,dx = \frac{L^5}{30}
$$

$$
E_\phi = \frac{\hbar^2L^3/6m}{L^5/30} = \frac{5\hbar^2}{mL^2} = \frac{10}{\pi^2}\,E_1 = 1.013\,E_1
$$

The guess is 1.3% too high. It is above $E_1$, as the theorem requires, and close to it because a parabola looks like half a sine wave.
:::

```{code-cell} python
:tags: [hide-input]
# synced: box_trials
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Three guesses (teal) for the ground state of a box, drawn over the exact one (gray), with the area between them in red. (a) A tent, with a kink in the middle. (b) The parabola of the example. (c) The parabola plus a second term, built below. Each energy lies above $E_1$, and the closer the shape, the lower the energy.

- **The theorem ranks the guesses.** The tent (Problem 1) is 21.6% high, the parabola 1.3%, the two-term function 0.0015%. No comparison with the exact answer was needed to put them in that order.
- **Shape decides.** The tent overlaps the true state almost as well as the parabola does, but its kink is steep, and steepness is kinetic energy.

#### One parameter: hydrogen with a Gaussian

The ground state of hydrogen is $e^{-r/a_0}$, with $E_1 = -\frac{1}{2}E_h$. Suppose the guess is a Gaussian instead, $\phi = e^{-\alpha r^2}$, with the exponent $\alpha$ free. In atomic units $\hat{H} = -\frac{1}{2}\nabla^2 - 1/r$, and the recipe runs as follows.

1. **Normalize.** $\langle\phi|\phi\rangle = \int_0^\infty e^{-2\alpha r^2}\,4\pi r^2\,dr = (\pi/2\alpha)^{3/2}$.
2. **Compute the two parts of the energy.** The integrals are in the dropdown below; divided by the normalization they give

$$
\langle T\rangle = \frac{3\alpha}{2}, \qquad \langle V\rangle = -2\sqrt{\frac{2\alpha}{\pi}}, \qquad E(\alpha) = \frac{3\alpha}{2} - 2\sqrt{\frac{2\alpha}{\pi}}
$$

3. **Minimize.** A large $\alpha$ is a tight Gaussian: the kinetic energy grows in proportion to $\alpha$, the attraction only as $\sqrt{\alpha}$. Setting $dE/d\alpha = 0$:

$$
\frac{3}{2} - \sqrt{\frac{2}{\pi\alpha}} = 0 \quad\Longrightarrow\quad \alpha = \frac{8}{9\pi} = 0.283\ a_0^{-2}
$$

$$
E = -\frac{4}{3\pi}\,E_h = -0.424\,E_h = -11.5\ \text{eV}
$$

```{code-cell} python
:tags: [hide-input]
# synced: gaussian_hydrogen
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Hydrogen with the trial function $e^{-\alpha r^2}$. Left: the average kinetic, potential and total energy for every exponent $\alpha$. The total has its minimum, $-0.424\,E_h$, at $\alpha = 0.283\,a_0^{-2}$ and stays above the exact $-\frac{1}{2}E_h$ (dashed) everywhere. Right: the best Gaussian against the exact $e^{-r/a_0}$, both normalized.

- **15% too high, and above the exact value for every $\alpha$.** No Gaussian reaches $-\frac{1}{2}E_h$, because no Gaussian is the true state.
- **What the Gaussian gets wrong.** The true function has a cusp at the nucleus and a long tail $e^{-r}$. The Gaussian is flat at the nucleus and its tail $e^{-\alpha r^2}$ dies too fast.
- **Why chemists use Gaussians anyway.** Integrals over products of Gaussians centered on different atoms have simple formulas, and exponentials do not. The cure for the poor shape is to add several Gaussians together, which is the linear method below.

:::{tip} **Going further: the integrals behind $E(\alpha)$**
:class: dropdown

Three standard integrals do all the work, with $b = 2\alpha$:

$$
\int_0^\infty r\,e^{-br^2}dr = \frac{1}{2b}, \qquad \int_0^\infty r^2e^{-br^2}dr = \frac{\sqrt{\pi}}{4b^{3/2}}
$$

$$
\int_0^\infty r^4e^{-br^2}dr = \frac{3\sqrt{\pi}}{8b^{5/2}}
$$

For a function of $r$ alone, $\nabla^2\phi = \phi'' + 2\phi'/r$, which for the Gaussian is $(4\alpha^2r^2 - 6\alpha)\,e^{-\alpha r^2}$. Then

$$
\langle\phi|\hat{T}|\phi\rangle = -\frac{1}{2}\int_0^\infty\left(4\alpha^2r^2 - 6\alpha\right)e^{-2\alpha r^2}\,4\pi r^2\,dr = \frac{3\alpha}{2}\left(\frac{\pi}{2\alpha}\right)^{3/2}
$$

$$
\langle\phi|\hat{V}|\phi\rangle = -\int_0^\infty\frac{1}{r}\,e^{-2\alpha r^2}\,4\pi r^2\,dr = -\frac{\pi}{\alpha}
$$

Dividing each by $\langle\phi|\phi\rangle = (\pi/2\alpha)^{3/2}$ gives $\langle T\rangle = 3\alpha/2$ and $\langle V\rangle = -2\sqrt{2\alpha/\pi}$.
:::

The recipe does not need a formula for the exact answer. Pick a well and tune the width of a Gaussian trial function; the dashed level is the exact ground state, solved numerically for comparison.

```{anywidget} ../widgets/variational_tuner.mjs
{}
```

- In the **spring** the family contains the exact state, and the teal level touches the dashed one at one width: the bound becomes an equality.
- In the **V-shaped well** no Gaussian is exact. The best one stops 0.5% above the dashed level.
- The **Morse well** is lopsided, and a Gaussian centered at the minimum cannot follow it. Move the center as well: a second parameter lowers the bound further.

#### Helium: a charge that is not 2

Helium is where the exact solutions stopped. Drop the repulsion $1/r_{12}$ from its Hamiltonian, and what is left is a sum of two He$^+$ Hamiltonians, one for each electron. A Hamiltonian that is a sum separates: the energies add and the wavefunctions multiply. Both electrons then sit in the 1s orbital of He$^+$, $e^{-2r}$ in atomic units, and the state of the atom is the product

$$
\phi(r_1, r_2) = \psi_{1s}(r_1)\,\psi_{1s}(r_2) \propto e^{-2r_1}\,e^{-2r_2}
$$

This **independent-electron** product is not an eigenfunction of the true Hamiltonian, which still contains the repulsion. It is a guess, and the variational method can improve it.

:::{note} **Example: the effective nuclear charge of helium**

Keep the product of two 1s orbitals, but let the charge in the exponent be a parameter $\zeta$ in place of 2:

$$
\phi(r_1, r_2) = \frac{\zeta^3}{\pi}\,e^{-\zeta r_1}\,e^{-\zeta r_2} \qquad\text{(atomic units)}
$$

The Hamiltonian keeps the true nuclear charge $Z = 2$. The average energy has three parts:

- kinetic energy, $\zeta^2/2$ for each electron: $\zeta^2$ in all
- attraction to the nucleus, $-Z\zeta$ for each electron, since $\langle 1/r\rangle = \zeta$ in this orbital: $-2Z\zeta$ in all
- repulsion between the two clouds, $\langle 1/r_{12}\rangle = \frac{5}{8}\zeta$ (a standard integral; the dropdown below shows where it comes from)

$$
E(\zeta) = \zeta^2 - 2Z\zeta + \tfrac{5}{8}\zeta = \zeta^2 - \tfrac{27}{8}\zeta \quad (Z = 2)
$$

$$
\frac{dE}{d\zeta} = 2\zeta - \tfrac{27}{8} = 0 \quad\Longrightarrow\quad \zeta = \frac{27}{16} = 1.69
$$

$$
E = -\left(\frac{27}{16}\right)^2E_h = -2.848\,E_h = -77.5\ \text{eV}
$$
:::

```{code-cell} python
:tags: [hide-input]
# synced: helium_screening
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The average energy of helium for the trial function $e^{-\zeta(r_1 + r_2)}$. The bare nuclear charge, $\zeta = 2$, gives $-74.8$ eV. The minimum is at $\zeta = 27/16$, with $-77.5$ eV. The exact energy, $-79.0$ eV, lies below both.

| trial function | energy ($E_h$) | energy (eV) | above the exact value |
| :-- | :-: | :-: | :-: |
| $e^{-\zeta(r_1 + r_2)}$ with $\zeta = 2$ | $-2.750$ | $-74.8$ | 4.2 eV |
| the same with $\zeta = 27/16$ | $-2.848$ | $-77.5$ | 1.5 eV |
| Hylleraas, three parameters (1929) | $-2.9024$ | $-78.98$ | 0.04 eV |
| exact | $-2.9037$ | $-79.01$ | |

- **Screening.** The best charge is less than 2. Each electron spends part of its time between the other electron and the nucleus, so each sees a nucleus of charge about 1.69. The **effective nuclear charge** of general chemistry is a variational parameter.
- **More parameters, lower energy.** Hylleraas added terms that depend on $r_{12}$ itself, which lets the electrons avoid each other, and came within 0.04 eV. Every row is above the exact value.
- **Orbitals for many electrons.** A product of one-electron functions with adjusted charges is the **orbital approximation**, the starting point for every atom in [Chapter 7](../ch07/01-multi-electron-atoms.md).

:::{tip} **Going further: where $\frac{5}{8}\zeta$ comes from**
:class: dropdown

Each electron in the orbital $e^{-\zeta r}$ is a round cloud of charge with the density $\rho(r) = (\zeta^3/\pi)\,e^{-2\zeta r}$. Electrostatics gives the potential that such a cloud creates at a distance $r$ from its center:

$$
\varphi(r) = \frac{1}{r} - \left(\zeta + \frac{1}{r}\right)e^{-2\zeta r}
$$

Far away it is $1/r$, the potential of a point charge; inside the cloud it is weaker, and at the center it levels off at $\zeta$. The repulsion energy is the potential of one cloud averaged over the density of the other:

$$
\left\langle\frac{1}{r_{12}}\right\rangle = \int_0^\infty\varphi(r)\,\rho(r)\,4\pi r^2\,dr
$$

$$
= 4\zeta^3\int_0^\infty\left[r\,e^{-2\zeta r} - \left(\zeta r^2 + r\right)e^{-4\zeta r}\right]dr
$$

$$
= 4\zeta^3\left[\frac{1}{4\zeta^2} - \frac{1}{32\zeta^2} - \frac{1}{16\zeta^2}\right] = \frac{5}{8}\,\zeta
$$
:::

### Linear combinations: the method chemists use

#### Mix fixed functions

Nonlinear parameters such as $\alpha$ and $\zeta$ sit inside exponentials, and each new one makes the minimization harder. A second kind of trial function avoids that. Choose a set of fixed functions $f_1, f_2, \dots, f_N$, the **basis functions**, and let only the mixing coefficients vary:

$$
\phi = c_1f_1 + c_2f_2 + \dots + c_Nf_N
$$

Minimizing the energy with respect to the coefficients needs no searching. It leads to a matrix eigenvalue problem, the kind [Lecture 3.5](../ch03/04-operators.md) solved with `eigh`.

#### Two functions, step by step

Take $N = 2$ and real functions and coefficients.

1. **Write the energy.** Insert $\phi = c_1f_1 + c_2f_2$ into $E = \langle\phi|\hat{H}|\phi\rangle/\langle\phi|\phi\rangle$ and multiply out:

$$
E = \frac{c_1^2H_{11} + 2c_1c_2H_{12} + c_2^2H_{22}}{c_1^2S_{11} + 2c_1c_2S_{12} + c_2^2S_{22}}
$$

$$
H_{ij} = \langle f_i|\hat{H}|f_j\rangle, \qquad S_{ij} = \langle f_i|f_j\rangle
$$

  The $H_{ij}$ are the **matrix elements** of the Hamiltonian, the sandwiches of Lecture 3.5. The $S_{ij}$ are **overlaps**: the basis functions need not be orthogonal or normalized. $\hat{H}$ is Hermitian, so $H_{12} = H_{21}$.

2. **Minimize.** Clear the fraction, $E\times(\text{denominator}) = \text{numerator}$, and differentiate both sides with respect to $c_1$. At the minimum $\partial E/\partial c_1 = 0$, which leaves

$$
E\left(2c_1S_{11} + 2c_2S_{12}\right) = 2c_1H_{11} + 2c_2H_{12}
$$

  Collect the terms, and do the same for $c_2$:

$$
\begin{aligned}
c_1\left(H_{11} - ES_{11}\right) + c_2\left(H_{12} - ES_{12}\right) &= 0\\
c_1\left(H_{12} - ES_{12}\right) + c_2\left(H_{22} - ES_{22}\right) &= 0
\end{aligned}
$$

3. **Solve.** These are two linear equations for $c_1$ and $c_2$. They always have the useless solution $c_1 = c_2 = 0$. Another solution exists only if the determinant of the coefficients vanishes, and that condition fixes $E$.

:::{important} **The linear variational method**

$$
\phi = \sum_{n=1}^N c_n f_n \qquad\Longrightarrow\qquad \mathbf{H}\,\mathbf{c} = E\,\mathbf{S}\,\mathbf{c}, \qquad \det\left(\mathbf{H} - E\,\mathbf{S}\right) = 0
$$

$$
H_{ij} = \langle f_i|\hat{H}|f_j\rangle, \qquad S_{ij} = \langle f_i|f_j\rangle
$$

- $N$ basis functions give $N\times N$ matrices and $N$ roots. The lowest root is the best energy this basis can give, an upper bound to $E_0$, and its eigenvector $\mathbf{c}$ holds the best coefficients
- $\det(\mathbf{H} - E\,\mathbf{S}) = 0$ is the **secular determinant**
- For an orthonormal basis $\mathbf{S}$ is the identity, and the problem is the ordinary eigenvalue problem $\mathbf{H}\mathbf{c} = E\mathbf{c}$
:::

- **numpy solves it in one line.** `eigh(H)` handles an orthonormal basis, as in Lecture 3.5, and `scipy.linalg.eigh(H, S)` handles overlaps.
- **Adding a basis function never raises the lowest root.** The old answer is still available, with the new coefficient set to zero, so the new minimum can only be equal or lower.
- **The higher roots are bounds too.** Each is an upper bound to the corresponding excited level, the second root to the second level and so on.

#### The two-level problem

The smallest case, two orthonormal basis functions, is worth solving once and keeping: it returns in every remaining lecture of this chapter. Call the energies of the two functions $E_1 = H_{11}$ and $E_2 = H_{22}$, with $E_1 \leq E_2$, and the matrix element that connects them $v = H_{12}$. The secular determinant is the quadratic equation $(E_1 - E)(E_2 - E) - v^2 = 0$.

:::{important} **The two-level problem**

$$
\mathbf{H} = \begin{pmatrix} E_1 & v\\ v & E_2\end{pmatrix}, \qquad \Delta = E_2 - E_1
$$

$$
E_\pm = \frac{E_1 + E_2}{2} \pm \sqrt{\left(\frac{\Delta}{2}\right)^2 + v^2}
$$

- $E_1$, $E_2$: the energies of the two states before they mix. $\Delta$: the **gap** between them. $v$: the **coupling**
- **Equal levels** ($\Delta = 0$): $E_\pm = E_1 \pm |v|$, and the states mix half and half, $(f_1 \pm f_2)/\sqrt{2}$
- **Distant levels** ($|v| \ll \Delta$): $E_- \approx E_1 - v^2/\Delta$ and $E_+ \approx E_2 + v^2/\Delta$, and the states barely mix
:::

```{code-cell} python
:tags: [hide-input]
# synced: mixing_angle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The two-level problem. Left: the levels $E_1$ and $E_2$ before mixing, and the roots $E_-$ and $E_+$ after. Right: the energy of every normalized mixture $\cos\theta\,f_1 + \sin\theta\,f_2$. Its lowest and highest points are the two roots; $f_1$ alone and $f_2$ alone lie in between.

- **Mixing pushes the levels apart.** $E_-$ lies below both starting levels and $E_+$ above both. The lower state gains exactly what the upper one loses.
- **The roots are the extremes of the energy.** The curve on the right is the variational energy of every possible mixture. Finding its minimum and solving the eigenvalue problem are the same task.
- **Equal levels make the chemical bond.** Two identical atomic orbitals on neighboring atoms have $\Delta = 0$. Chemists write their energy $\alpha$ and their coupling $\beta$, so the two levels are $\alpha \pm \beta$, and the lower mixture is the bond ([Chapter 8](../ch08/02-hydrogen-molecule-ion.md)).
- **Distant levels give perturbation theory.** The small push $v^2/\Delta$, coupling squared over gap, is the second-order shift of [Lecture 6.2](02-perturbation-theory.md). [Lecture 6.3](03-time-dependent-perturbation-and-selection-rules.md) then drives the same two levels with light.

#### The box again, with two polynomials

:::{note} **Example: improve the parabola**

Add a second function to the parabola of the first example: $f_1 = x(L - x)$ and $f_2 = x^2(L - x)^2$. Find the best energy of $\phi = c_1f_1 + c_2f_2$.

With $L = 1$ and energies in units of $\hbar^2/mL^2$, the matrix elements are integrals of polynomials. Using $H_{ij} = \frac{1}{2}\int f_i'f_j'\,dx$:

$$
\mathbf{H} = \begin{pmatrix} \frac{1}{6} & \frac{1}{30}\\[2pt] \frac{1}{30} & \frac{1}{105}\end{pmatrix}, \qquad \mathbf{S} = \begin{pmatrix} \frac{1}{30} & \frac{1}{140}\\[2pt] \frac{1}{140} & \frac{1}{630}\end{pmatrix}
$$

The functions overlap ($S_{12} \neq 0$), so the problem is $\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}$:
:::

```{code-cell} python
import numpy as np
from scipy.linalg import eigh

# f1 = x(1 - x) and f2 = x^2 (1 - x)^2, energies in units of hbar^2 / m L^2
H = np.array([[1/6, 1/30], [1/30, 1/105]])        # <f_i|H|f_j>
S = np.array([[1/30, 1/140], [1/140, 1/630]])     # overlaps <f_i|f_j>
E, C = eigh(H, S)                                 # solves H c = E S c
print("roots        :", np.round(E, 5))
print("exact E1, E3 :", np.round([np.pi**2 / 2, 9 * np.pi**2 / 2], 5))
print("c2 / c1      :", round(C[1, 0] / C[0, 0], 4))
```

- **The lowest root is 4.93487**, against the exact $\pi^2/2 = 4.93480$: 0.0015% too high. One extra function cut the error of the parabola by a factor of about 900. This is panel (c) of the figure above.
- **The second root, 51.07, is an upper bound to $E_3 = 44.41$**, not to $E_2$. Both basis functions are symmetric about the middle of the box, so they can build only symmetric states, and the next symmetric state after $\psi_1$ is $\psi_3$.

#### Hydrogen from several Gaussians

One Gaussian gave hydrogen 85% of its binding energy. A sum of Gaussians with different exponents does better, and the coefficients come from the same matrix equation. For s-type Gaussians $e^{-ar^2}$ and $e^{-br^2}$ the matrix elements are known formulas (atomic units):

$$
S_{ab} = \left(\frac{\pi}{a + b}\right)^{3/2}, \qquad H_{ab} = \frac{3ab}{a + b}\,S_{ab} - \frac{2\pi}{a + b}
$$

```{code-cell} python
alpha = np.array([0.15137, 0.68128, 4.5004])      # three exponents, in 1/a0^2
a, b = np.meshgrid(alpha, alpha)
S = (np.pi / (a + b))**1.5                        # overlaps
# kinetic energy plus Coulomb attraction, in hartree
H = 3 * a * b / (a + b) * S - 2 * np.pi / (a + b)
E, C = eigh(H, S)
print("lowest root:", round(E[0], 5), "hartree   (exact: -0.5)")
```

```{code-cell} python
:tags: [hide-input]
# synced: gaussian_basis
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Hydrogen from one to five Gaussians, each set with its best exponents. Left: the lowest root steps down toward the exact $-\frac{1}{2}E_h$ and never passes it. Right: the sums of one, two and three Gaussians against the exact $e^{-r/a_0}$. Tight Gaussians build up the cusp at the nucleus.

- **Three Gaussians recover 99.4% of the energy**, $-0.4970$ of $-0.5$ hartree, and five recover 99.96%.
- **This is a basis set.** The name STO-3G on a quantum chemistry program's menu means three Gaussians standing in for each exponential orbital, exactly as here.
- **Every electronic-structure program solves $\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}$.** The basis functions are Gaussians on each atom, the matrices have thousands of rows, and the eigenvectors are the molecular orbitals ([Hartree-Fock](../ch07/02-hartree-fock.md), [Chapter 8](../ch08/02-hydrogen-molecule-ion.md)).

The variational method needs a guess and returns a bound, with no estimate of how far above the truth the bound lies. When the problem is a small change to one that is already solved, no guess is needed: [perturbation theory](02-perturbation-theory.md) corrects the known answer directly.

:::{seealso} Computational lab
[Linear variational method](../demos/08-demo-linear-variational.md) builds $\mathbf{H}$ and $\mathbf{S}$ numerically for any well and any basis, in a Colab notebook.
:::

### Problems

#### Problem 1: A tent in a box

Use the tent function, $\phi = x$ for $0 \leq x \leq L/2$ and $\phi = L - x$ for $L/2 \leq x \leq L$, as a trial function for the ground state of a particle in a box. Find $E_\phi$ and compare it with $E_1$ and with the parabola of the first example.

:::{admonition} **Solution**
:class: dropdown solution

The tent has a kink, so $\phi''$ is zero everywhere except at one point. Use the first-derivative form of the kinetic energy, $\langle\phi|\hat{H}|\phi\rangle = (\hbar^2/2m)\int(\phi')^2dx$. The slope is $+1$ on the left half and $-1$ on the right, so $(\phi')^2 = 1$ throughout:

$$
\langle\phi|\hat{H}|\phi\rangle = \frac{\hbar^2}{2m}\,L, \qquad \langle\phi|\phi\rangle = 2\int_0^{L/2}x^2\,dx = \frac{L^3}{12}
$$

$$
E_\phi = \frac{\hbar^2L/2m}{L^3/12} = \frac{6\hbar^2}{mL^2} = \frac{12}{\pi^2}\,E_1 = 1.216\,E_1
$$

The tent is 21.6% too high, against 1.3% for the parabola. Both obey the boundary conditions and both have one maximum in the middle, but the tent stays steep all the way to its peak, and $\int(\phi')^2dx$ counts steepness. The theorem ranks the parabola as the better guess without any reference to the exact solution.
:::

#### Problem 2: A Lorentzian in a spring

Use $\phi = 1/(x^2 + b^2)$, with $b$ as the parameter, as a trial function for the ground state of the harmonic oscillator, $\hat{H} = -(\hbar^2/2\mu)\,d^2/dx^2 + \frac{1}{2}kx^2$. Show that $E(b) = \hbar^2/4\mu b^2 + \frac{1}{2}kb^2$, minimize it, and compare the result with $\frac{1}{2}\hbar\omega$. Why does this trial function do so much worse than a Gaussian? Useful integrals over all $x$:

$$
\int\frac{dx}{(x^2 + b^2)^2} = \frac{\pi}{2b^3}, \qquad \int\frac{x^2\,dx}{(x^2 + b^2)^2} = \frac{\pi}{2b}
$$

$$
\int\frac{x^2\,dx}{(x^2 + b^2)^4} = \frac{\pi}{16b^5}
$$

#### Problem 3: Where the 1.3% comes from

The normalized parabola $\phi = \sqrt{30/L^5}\,x(L - x)$ has the expansion coefficients $c_n = \langle\psi_n|\phi\rangle = 8\sqrt{15}/n^3\pi^3$ for odd $n$ and zero for even $n$ in the states of the box. (a) Find the probabilities of measuring $E_1$, $E_3$ and $E_5$. (b) Compute the average energy from $\sum_n|c_n|^2E_n$ and check it against the example. (c) How large is the error in the wavefunction, and how large is the error in the energy?

:::{admonition} **Solution**
:class: dropdown solution

(a) $|c_n|^2 = 960/n^6\pi^6$ for odd $n$:

$$
|c_1|^2 = \frac{960}{\pi^6} = 0.99856, \qquad |c_3|^2 = \frac{|c_1|^2}{729} = 0.00137
$$

$$
|c_5|^2 = \frac{|c_1|^2}{15625} = 0.00006
$$

The even states are missing because the parabola is symmetric about the middle of the box and they are antisymmetric.

(b) With $E_n = n^2E_1$,

$$
\langle E\rangle = \sum_{n\ \text{odd}}\frac{960}{n^6\pi^6}\,n^2E_1 = \frac{960}{\pi^6}\,E_1\sum_{n\ \text{odd}}\frac{1}{n^4}
$$

$$
= \frac{960}{\pi^6}\cdot\frac{\pi^4}{96}\,E_1 = \frac{10}{\pi^2}\,E_1 = 1.013\,E_1
$$

the value found directly in the example. The first two terms alone give $0.99856 + 9\times0.00137 = 1.0109$.

(c) The guess is 99.86% ground state. The part that is wrong has weight $\epsilon^2 = 0.0014$, an amplitude $\epsilon = 0.038$: the wavefunction is off by about 4%. The energy is off by 1.3%, which is $\epsilon^2$ times the cost of the admixed states, mostly $\psi_3$ at $8E_1$ above the ground state: $0.00137\times8 = 0.011$. The error in the energy is second order in the error of the function.
:::

#### Problem 4: A V-shaped well

A particle moves in the well $V(x) = F|x|$. Use the Gaussian $\phi = e^{-ax^2}$ as a trial function. With $\langle T\rangle = \hbar^2a/2m$ and $\langle|x|\rangle = 1/\sqrt{2\pi a}$ for this function, write $E(a)$, minimize it, and show that the best energy is $\frac{3}{2}\left(\hbar^2F^2/2\pi m\right)^{1/3} = 0.813\,(\hbar^2F^2/m)^{1/3}$. The exact ground-state energy is $0.809\,(\hbar^2F^2/m)^{1/3}$. How close is the bound, and which way is it off? Check your value against the widget above, which uses $\hbar = m = F = 1$.

#### Problem 5: Two orbitals that overlap

Two identical basis functions on neighboring atoms have $H_{11} = H_{22} = \alpha$, $H_{12} = \beta$ and an overlap $S_{12} = S$, with $S_{11} = S_{22} = 1$. Solve the secular determinant and find the two energies and their coefficients. Which level moves farther from $\alpha$?

:::{admonition} **Solution**
:class: dropdown solution

The secular determinant is

$$
\begin{vmatrix}\alpha - E & \beta - ES\\ \beta - ES & \alpha - E\end{vmatrix} = (\alpha - E)^2 - (\beta - ES)^2 = 0
$$

$$
\alpha - E = \pm(\beta - ES)
$$

$$
E_+ = \frac{\alpha + \beta}{1 + S}, \qquad E_- = \frac{\alpha - \beta}{1 - S}
$$

Insert each root into the first equation, $c_1(\alpha - E) + c_2(\beta - ES) = 0$. For $E_+$, $\alpha - E = -(\beta - ES)$ and so $c_1 = c_2$: the mixture $f_1 + f_2$. For $E_-$, $c_1 = -c_2$: the mixture $f_1 - f_2$.

With $S = 0$ the levels are $\alpha \pm \beta$, split evenly. With an overlap, measure both from $\alpha$:

$$
E_+ - \alpha = \frac{\beta - \alpha S}{1 + S}, \qquad E_- - \alpha = -\frac{\beta - \alpha S}{1 - S}
$$

The two shifts have the same numerator and opposite signs, but the second is divided by the smaller number $1 - S$. For a bond, $\beta - \alpha S$ is negative: $f_1 + f_2$ is the bonding orbital, lowered by $|\beta - \alpha S|/(1 + S)$, and $f_1 - f_2$ is the antibonding orbital, raised by the larger amount $|\beta - \alpha S|/(1 - S)$. That asymmetry is why filling both orbitals, as in He$_2$, gives no bond ([Chapter 8](../ch08/03-hydrogen-molecule.md)).
:::

#### Problem 6: Two-electron ions

The helium example gives $E(\zeta) = \zeta^2 - 2Z\zeta + \frac{5}{8}\zeta$ hartree for any nucleus of charge $Z$ with two electrons. (a) Show that the best exponent is $\zeta = Z - \frac{5}{16}$ and the best energy $-(Z - \frac{5}{16})^2$. (b) Evaluate it for H$^-$ ($Z = 1$) and Li$^+$ ($Z = 3$) and compare with the exact energies, $-0.5278$ and $-7.2799$ hartree. (c) A hydrogen atom plus a free electron at rest has the energy $-0.5$ hartree. Does this trial function predict that H$^-$ is stable? It is, in fact. What does that tell you about the difference between a bound and an estimate?

#### Problem 7: A bound for an excited state

The first excited state of the box, $\psi_2$, is antisymmetric about the middle. Use the antisymmetric trial function $\phi = x(L - x)(L/2 - x)$ to bound $E_2$. Why is the result an upper bound to $E_2$ and not merely to $E_1$?

:::{admonition} **Solution**
:class: dropdown solution

Set $L = 1$ and use units of $\hbar^2/mL^2$. Then $\phi \propto x(1 - x)(1 - 2x) = x - 3x^2 + 2x^3$ and $\phi' = 1 - 6x + 6x^2$:

$$
\int_0^1(\phi')^2dx = 1 - 6 + 16 - 18 + \frac{36}{5} = \frac{1}{5}
$$

$$
\int_0^1\phi^2\,dx = \frac{1}{3} - \frac{3}{2} + \frac{13}{5} - 2 + \frac{4}{7} = \frac{1}{210}
$$

$$
E_\phi = \frac{\frac{1}{2}\cdot\frac{1}{5}}{\frac{1}{210}} = 21\,\frac{\hbar^2}{mL^2}, \qquad E_2 = \frac{4\pi^2}{2}\,\frac{\hbar^2}{mL^2} = 19.74\,\frac{\hbar^2}{mL^2}
$$

The bound is 6.4% high. It bounds $E_2$ because $\phi$ is antisymmetric about the middle of the box, and every symmetric state, $\psi_1$ included, is orthogonal to it. In the expansion $\phi = \sum c_n\psi_n$ only the antisymmetric states $n = 2, 4, 6, \dots$ appear, and the lowest of them is $\psi_2$. The proof of the theorem then runs as before, with $E_2$ in the role of the lowest level.
:::

#### Problem 8: One more Gaussian

(a) Explain in two sentences why adding a basis function to a linear variational calculation can never raise the lowest root. (b) Test it. In the three-Gaussian cell above, add a fourth exponent of your choice and rerun; then try several values between 0.05 and 50. Does the energy ever rise above $-0.49698$? (c) Which values of the fourth exponent help most, very small ones, very large ones, or ones between those already present? Relate your answer to the two things a Gaussian gets wrong about the hydrogen atom.
