---
kernelspec:
  name: python3
  display_name: Python 3
---

# Perturbation Theory

:::{note} **What you need to know**

- Many real problems are a **solved problem plus a small change**: a bond is a spring plus anharmonic terms, an atom in a field is the free atom plus the energy of its dipole, helium is two hydrogenlike electrons plus their repulsion. Write $\hat{H} = \hat{H}^{(0)} + \hat{H}^{(1)}$, with $\hat{H}^{(0)}$ solved, and correct its energies and states step by step.
- **First order.** The first correction to a level is the average of the perturbation in the unperturbed state, $E_n^{(1)} = \langle n|\hat{H}^{(1)}|n\rangle$. A bump in a well raises each level in proportion to the chance of finding the particle on the bump. No new wavefunction is needed.
- **Second order.** The perturbation mixes each state with the others, and the mixing lowers or raises the level: $E_n^{(2)} = \sum_{k\neq n}|\langle k|\hat{H}^{(1)}|n\rangle|^2/(E_n^{(0)} - E_k^{(0)})$. **Levels repel**: every level above pushes down, every level below pushes up, and the nearest push hardest. The ground state always goes down in second order.
- The method works when the coupling $|\langle k|\hat{H}^{(1)}|n\rangle|$ is **small compared with the gap** between the levels it connects. When levels are degenerate or nearly so, the mixing is strong and the matrix must be diagonalized, as in [Lecture 6.1](01-variational-method.md).
- Earlier lectures used perturbation theory without the name: anharmonic levels, centrifugal distortion, the Zeeman effect and fine structure. New here: the polarizability of a molecule, the attraction between two argon atoms, and helium, where first order gives $-74.8$ eV and second order $-79.1$ eV against the exact $-79.0$ eV.

:::

### A solved problem, plus a small change

The variational method starts from a guess. Perturbation theory starts from an answer: a Hamiltonian $\hat{H}^{(0)}$ whose energies and states are already known, to which a small extra term $\hat{H}^{(1)}$, the **perturbation**, is added.

$$
\hat{H} = \hat{H}^{(0)} + \hat{H}^{(1)}, \qquad \hat{H}^{(0)}\psi_n^{(0)} = E_n^{(0)}\psi_n^{(0)} \quad\text{solved}
$$

The model for this lecture is a particle in a box with a small bump on its floor:

```{code-cell} python
:tags: [hide-input]
# synced: perturbation_split
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The model of this lecture. The solved problem is a box of length $L$; the perturbation is a bump of height $V_0$ on the middle fifth of the floor; their sum is a box with a bump, which has no simple solution. Its levels (black) are those of the plain box (dashed), each shifted by a different amount. Here $V_0 = 2E_1^{(0)}$.

The superscripts count orders of correction and are not powers:

| symbol | meaning |
| :-- | :-- |
| $\hat{H}^{(0)}$ | the solved, **unperturbed** Hamiltonian |
| $\hat{H}^{(1)}$ | the perturbation |
| $E_n^{(0)}$, $\psi_n^{(0)}$ | the known levels and states of $\hat{H}^{(0)}$; in a bracket the state is written $\vert n\rangle$ |
| $E_n^{(1)}$, $E_n^{(2)}$ | the first and second corrections to level $n$ |
| $\psi_n^{(1)}$ | the first correction to state $n$ |
| $\langle k\vert\hat{H}^{(1)}\vert n\rangle$ | a matrix element of the perturbation between two unperturbed states |

The goal is to express the levels of $\hat{H}$ entirely in terms of the right-hand column: known energies, known states, and integrals of the perturbation between them.

### Expanding in powers of the perturbation

#### The two-level problem, expanded

Before the general method, take the one problem this chapter has already solved exactly: the [two-level problem](01-variational-method.md) of Lecture 6.1, two levels a gap $\Delta$ apart, coupled by $v$. Read the two levels as the solved problem, $E_1^{(0)}$ and $E_2^{(0)}$, and the coupling as the perturbation, dialed on by a number $\lambda$ between 0 and 1. The exact lower root is then

$$
E_- = \frac{E_1^{(0)} + E_2^{(0)}}{2} - \sqrt{\left(\frac{\Delta}{2}\right)^2 + \lambda^2v^2}, \qquad \Delta = E_2^{(0)} - E_1^{(0)}
$$

For a small coupling the square root can be expanded, using $\sqrt{1 + x} \approx 1 + \frac{1}{2}x - \frac{1}{8}x^2$:

$$
E_- = E_1^{(0)} - \lambda^2\,\frac{v^2}{\Delta} + \lambda^4\,\frac{v^4}{\Delta^3} - \dots
$$

The upper root is the mirror image, $E_+ = E_2^{(0)} + \lambda^2v^2/\Delta - \dots$

```{code-cell} python
:tags: [hide-input]
# synced: two_level_series
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. Two levels coupled by $v$. Black: the exact levels. Dashed orange: the series stopped after the $\lambda^2$ term (with $\lambda = 1$). The two agree while $|v|$ is small compared with the gap $\Delta$. In the shaded region, $|v| > \Delta/2$, the series no longer converges.

- **The exact answer is a power series in $\lambda$.** Each term is a correction of higher order: the unperturbed level, then a term in $\lambda^2$, then $\lambda^4$.
- **The second-order term is the coupling squared over the gap**, $v^2/\Delta$, and it pushes the two levels apart.
- **The series needs a small parameter**, the ratio $|v|/\Delta$ of coupling to gap. That, and not the size of $v$ alone, is what "small perturbation" means.

Perturbation theory produces this series term by term for problems that cannot be solved exactly.

#### The general expansion

1. **Dial the perturbation on.** Write $\hat{H} = \hat{H}^{(0)} + \lambda\hat{H}^{(1)}$, and expand the unknown level and state of $\hat{H}$ in powers of $\lambda$:

$$
E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2E_n^{(2)} + \dots, \qquad \psi_n = \psi_n^{(0)} + \lambda\psi_n^{(1)} + \dots
$$

2. **Insert into $\hat{H}\psi_n = E_n\psi_n$ and sort by powers of $\lambda$.** A polynomial in $\lambda$ that vanishes for every $\lambda$ must vanish power by power, so each power gives its own equation:

$$
\begin{aligned}
\lambda^0:&\qquad \hat{H}^{(0)}\psi_n^{(0)} = E_n^{(0)}\psi_n^{(0)}\\
\lambda^1:&\qquad \hat{H}^{(0)}\psi_n^{(1)} + \hat{H}^{(1)}\psi_n^{(0)} = E_n^{(0)}\psi_n^{(1)} + E_n^{(1)}\psi_n^{(0)}
\end{aligned}
$$

3. **Solve them in order.** The first is the unperturbed problem, already solved. The second contains two unknowns, $E_n^{(1)}$ and $\psi_n^{(1)}$, and the next two sections extract them. At the end set $\lambda = 1$.

### First order: average the perturbation

Project the $\lambda^1$ equation onto the unperturbed state: multiply from the left by $\psi_n^{(0)*}$ and integrate.

$$
\langle n|\hat{H}^{(0)}|\psi_n^{(1)}\rangle + \langle n|\hat{H}^{(1)}|n\rangle = E_n^{(0)}\langle n|\psi_n^{(1)}\rangle + E_n^{(1)}\langle n|n\rangle
$$

$\hat{H}^{(0)}$ is Hermitian, so it can act to the left on $\langle n|$, where it gives $E_n^{(0)}$ ([Operators 2](../ch03/05-hermitian-operators-and-commutators.md)). The first term on the left then equals the first term on the right, and the two cancel. The unknown $\psi_n^{(1)}$ has dropped out, and $\langle n|n\rangle = 1$:

:::{important} **First-order correction to the energy**

$$
E_n^{(1)} = \langle n|\hat{H}^{(1)}|n\rangle = \int\psi_n^{(0)*}\,\hat{H}^{(1)}\,\psi_n^{(0)}\,d\tau
$$

- The average of the perturbation in the **unperturbed** state
- $E_n \approx E_n^{(0)} + E_n^{(1)}$ needs no new wavefunction
:::

- **For a change in the potential, weigh it by the density.** If $\hat{H}^{(1)}$ is a function $V^{(1)}(x)$, then $E_n^{(1)} = \int|\psi_n^{(0)}|^2\,V^{(1)}(x)\,dx$: the perturbation counts where the particle is likely to be.
- **To first order the state has not moved.** The particle is still in $\psi_n^{(0)}$; only its energy has been re-evaluated with the new Hamiltonian. That is also why $E_n^{(0)} + E_n^{(1)} = \langle n|\hat{H}|n\rangle$, the variational energy of the unperturbed state: for a ground state, first order is always an upper bound.

:::{note} **Example: a bump in a box**

A box of length $L$ has a bump of height $V_0$ between $0.4L$ and $0.6L$. Find the first-order shifts of the three lowest levels.

The perturbation is $V_0$ on the bump and zero elsewhere, so the shift is $V_0$ times the probability of finding the particle on the bump:

$$
E_n^{(1)} = V_0\int_{0.4L}^{0.6L}\frac{2}{L}\sin^2\frac{n\pi x}{L}\,dx
$$

$$
= V_0\left[0.2 - \frac{\sin(1.2\,n\pi) - \sin(0.8\,n\pi)}{2n\pi}\right]
$$

$$
E_1^{(1)} = 0.387\,V_0, \qquad E_2^{(1)} = 0.049\,V_0, \qquad E_3^{(1)} = 0.301\,V_0
$$
:::

```{code-cell} python
:tags: [hide-input]
# synced: first_order_density
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The densities of the three lowest box states, with the bump shaded. The dark area is the probability of finding the particle on the bump: 0.39, 0.05 and 0.30. Right: the first-order shifts for $V_0 = 2E_1^{(0)}$, in units of $E_1^{(0)}$.

- **A level is raised in proportion to its density on the bump.** States 1 and 3 have a maximum in the middle of the box and are raised strongly. State 2 has a node there and is barely moved.
- **The spacings change.** With $V_0 = 2E_1^{(0)}$ the three levels rise by 0.77, 0.10 and 0.60 in units of $E_1^{(0)}$. Solving the problem numerically gives 0.71, 0.09 and 0.64: first order is close, and second order will account for most of the rest.
- **Symmetry can make the first-order shift vanish.** If the well is symmetric and the perturbation is odd, the integrand $|\psi_n^{(0)}|^2\,V^{(1)}$ is odd and the integral is zero, the rule of [Lecture 4.2](../ch04/02-quantum-harmonic-oscillator.md) for sandwiches. The energy then first changes in second order.

### Second order: the state borrows from its neighbors

#### The state changes first

To first order in the energy the state was left alone. The perturbation does change it, by mixing in other unperturbed states. Expand the correction in those states, as any function can be ([Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md)):

$$
\psi_n^{(1)} = \sum_{k \neq n} c_k\,\psi_k^{(0)}
$$

To find a coefficient, project the $\lambda^1$ equation onto a different state, $\langle k|$ with $k \neq n$. Orthogonality removes the last term, and $\hat{H}^{(0)}$ acting to the left gives $E_k^{(0)}$:

$$
E_k^{(0)}c_k + \langle k|\hat{H}^{(1)}|n\rangle = E_n^{(0)}c_k \quad\Longrightarrow\quad c_k = \frac{\langle k|\hat{H}^{(1)}|n\rangle}{E_n^{(0)} - E_k^{(0)}}
$$

A state is mixed in strongly if the perturbation connects it to $\psi_n^{(0)}$ and if its energy is close.

```{code-cell} python
:tags: [hide-input]
# synced: tilt_mixing
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. A box whose floor slopes upward to the right, $\hat{H}^{(1)} = F(x - L/2)$ with $F = 3E_1^{(0)}/L$. To first order its ground state is $\psi_1^{(0)}$ plus 0.18 of $\psi_2^{(0)}$ (purple), which is nearly the exact state (thick gray). The thin dashed curve is $\psi_1^{(0)}$ alone. The particle has shifted toward the low side.

- **Mixing moves the particle.** Adding a little of $\psi_2^{(0)}$, positive on the left and negative on the right, piles the wavefunction up on the left, where the potential is lower. For a charged particle in an electric field this shift is an induced dipole moment: the state is **polarized**.
- **One neighbor does almost all the work.** $\psi_3^{(0)}$ is not mixed in at all, since the integrand $\psi_3^{(0)}(x - L/2)\,\psi_1^{(0)}$ is odd about the middle, and $\psi_4^{(0)}$ enters with the coefficient 0.003.

#### The energy to second order

The $\lambda^2$ equation, projected onto $\langle n|$ in the same way, gives the next correction in terms of the state just found (the steps are in the dropdown):

$$
E_n^{(2)} = \langle n|\hat{H}^{(1)}|\psi_n^{(1)}\rangle = \sum_{k \neq n}c_k\,\langle n|\hat{H}^{(1)}|k\rangle
$$

:::{important} **Perturbation theory through second order**

$$
E_n \approx E_n^{(0)} + \langle n|\hat{H}^{(1)}|n\rangle + \sum_{k \neq n}\frac{\left|\langle k|\hat{H}^{(1)}|n\rangle\right|^2}{E_n^{(0)} - E_k^{(0)}}
$$

$$
\psi_n \approx \psi_n^{(0)} + \sum_{k \neq n}\frac{\langle k|\hat{H}^{(1)}|n\rangle}{E_n^{(0)} - E_k^{(0)}}\,\psi_k^{(0)}
$$

- First order uses one **diagonal** matrix element of the perturbation; second order uses the **off-diagonal** ones, each divided by a gap
- Everything on the right belongs to the solved problem
:::

```{code-cell} python
:tags: [hide-input]
# synced: level_repulsion
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The second-order sum, one arrow for each term. Left: the ground state. Every other level lies above it and pushes it down, the nearest hardest, so $E_1^{(2)}$ is negative. Right: a level in the middle is pushed down by the levels above it and up by the level below; the sign of the total depends on which pushes win.

- **Levels repel.** A term with $E_k^{(0)}$ above $E_n^{(0)}$ has a negative denominator and lowers level $n$; a term with $E_k^{(0)}$ below raises it. The two-level example showed the same thing: coupled levels move apart.
- **The ground state always drops in second order.** Every denominator is negative and every numerator is positive or zero.
- **Close levels matter most.** The gap is in the denominator, so a nearby level with a modest coupling can outweigh a distant one with a large coupling.
- **It works only if each coupling is small compared with its gap**, $|\langle k|\hat{H}^{(1)}|n\rangle| \ll |E_n^{(0)} - E_k^{(0)}|$, which is the condition found in the two-level example.
- **Degenerate levels need care.** If two unperturbed states share an energy, a denominator vanishes. The remedy is to choose, within the degenerate level, the combinations that the perturbation does not connect, which means diagonalizing $\hat{H}^{(1)}$ inside that level with the secular determinant of Lecture 6.1. [Lecture 5.3](../ch05/03-spin.md) did this for spin-orbit coupling by switching from the states $m_l, m_s$ to the states $j, m_j$.

:::{tip} **Going further: where the second-order formula comes from**
:class: dropdown

Collecting the terms in $\lambda^2$ gives

$$
\hat{H}^{(0)}\psi_n^{(2)} + \hat{H}^{(1)}\psi_n^{(1)} = E_n^{(0)}\psi_n^{(2)} + E_n^{(1)}\psi_n^{(1)} + E_n^{(2)}\psi_n^{(0)}
$$

Project onto $\langle n|$. As before, $\hat{H}^{(0)}$ acts to the left and the first terms on the two sides cancel. The expansion of $\psi_n^{(1)}$ contains no $\psi_n^{(0)}$, so $\langle n|\psi_n^{(1)}\rangle = 0$ and the term with $E_n^{(1)}$ vanishes too. What is left is

$$
E_n^{(2)} = \langle n|\hat{H}^{(1)}|\psi_n^{(1)}\rangle = \sum_{k \neq n}\frac{\langle k|\hat{H}^{(1)}|n\rangle}{E_n^{(0)} - E_k^{(0)}}\,\langle n|\hat{H}^{(1)}|k\rangle
$$

and since $\hat{H}^{(1)}$ is Hermitian, $\langle n|\hat{H}^{(1)}|k\rangle = \langle k|\hat{H}^{(1)}|n\rangle^*$, which makes the numerator an absolute square.

Why may $\psi_n^{(1)}$ be chosen without any $\psi_n^{(0)}$ in it? Adding a multiple of $\psi_n^{(0)}$ to the correction only changes the length of the total state $\psi_n^{(0)} + \lambda\psi_n^{(1)}$, not its direction, and the length is fixed at the end by normalizing.
:::

#### An exact check: an oscillator in an electric field

:::{note} **Example: a charged oscillator in a uniform field**

A particle of charge $q$ on a spring of force constant $k$ sits in an electric field $\mathcal{E}$, which adds the energy $\hat{H}^{(1)} = -q\mathcal{E}x$. Find the shift of every level to second order.

**First order** vanishes: $x$ is odd and $|\psi_v|^2$ is even, so $\langle v|x|v\rangle = 0$.

**Second order.** [Lecture 4.2](../ch04/02-quantum-harmonic-oscillator.md) showed that $x$ connects only neighboring levels, with

$$
\langle v + 1|x|v\rangle = \sqrt{\frac{(v + 1)\hbar}{2\mu\omega}}, \qquad \langle v - 1|x|v\rangle = \sqrt{\frac{v\hbar}{2\mu\omega}}
$$

so the sum has two terms. The level above is $\hbar\omega$ higher and the level below $\hbar\omega$ lower:

$$
E_v^{(2)} = q^2\mathcal{E}^2\left[\frac{(v + 1)\hbar/2\mu\omega}{-\hbar\omega} + \frac{v\hbar/2\mu\omega}{+\hbar\omega}\right] = -\frac{q^2\mathcal{E}^2}{2\mu\omega^2} = -\frac{q^2\mathcal{E}^2}{2k}
$$

**Exact.** Complete the square in the potential:

$$
\tfrac{1}{2}kx^2 - q\mathcal{E}x = \tfrac{1}{2}k\left(x - \frac{q\mathcal{E}}{k}\right)^2 - \frac{q^2\mathcal{E}^2}{2k}
$$

The same parabola, moved sideways by $q\mathcal{E}/k$ and down by $q^2\mathcal{E}^2/2k$. Second-order perturbation theory gives the exact answer here.
:::

```{code-cell} python
:tags: [hide-input]
# synced: field_oscillator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. A charged oscillator without a field (dashed) and in a field (solid). The well keeps its shape; it moves over by $q\mathcal{E}/k$ and down by $q^2\mathcal{E}^2/2k$, and every level drops by the same amount.

- **Every level drops equally**, so the spacing stays $\hbar\omega$: a uniform field does not change the frequency of a harmonic vibration.
- **Polarizability.** The charge has moved by $q\mathcal{E}/k$, which is an induced dipole $q\cdot q\mathcal{E}/k = \alpha\,\mathcal{E}$ with the **polarizability** $\alpha = q^2/k$. The energy drop is $-\frac{1}{2}\alpha\,\mathcal{E}^2$. Soft springs, meaning loosely held electrons, polarize easily. For any atom or molecule the polarizability is a second-order energy, and it is large when there are excited states close above the ground state.

### How far it can be pushed

numpy carries out both corrections for the box with a bump and compares them with the exact levels of the grid Hamiltonian of [Lecture 3.5](../ch03/04-operators.md). The matrix elements of the perturbation are sandwiches, as in the $x$ matrix of Lecture 4.2:

```{code-cell} python
import numpy as np

N = 1000; dx = 1 / N; x = np.arange(1, N) * dx   # box of length 1, hbar = m = 1
E1 = np.pi**2 / 2                                # ground state of the plain box
# the bump: 1 on the middle fifth, 1/2 at its two edge points, 0 outside
bump = np.clip((0.1 - np.abs(x - 0.5)) / dx + 0.5, 0, 1)
V = 2 * E1 * bump                                # the perturbation, V0 = 2 E1

n = np.arange(1, 41)                             # the first 40 box states
psi = np.sqrt(2) * np.sin(np.outer(n, np.pi * x))   # their states, one per row
E0 = n**2 * E1                                   # unperturbed energies
H1 = psi @ (V * psi).T * dx                      # every <k|H1|n> at once

# the exact levels, from the grid Hamiltonian of Lecture 3.5
off = -np.ones(N - 2) / (2 * dx**2)
H = np.diag(1 / dx**2 + V) + np.diag(off, 1) + np.diag(off, -1)
exact = np.linalg.eigvalsh(H)

for j in range(3):
    first = H1[j, j]                             # the diagonal element
    column = np.delete(H1[:, j], j)              # the rest of that column
    second = np.sum(column**2 / (E0[j] - np.delete(E0, j)))
    e = np.array([E0[j], E0[j] + first, E0[j] + first + second, exact[j]]) / E1
    print(f"n = {j + 1}:  zeroth {e[0]:.3f}   first {e[1]:.3f}"
          f"   second {e[2]:.3f}   exact {e[3]:.3f}")
```

- **First order is the diagonal of `H1`**, second order a sum over one column, off the diagonal.
- **Second order closes most of the gap** that first order leaves. For $n = 1$ the second-order term is negative, as it must be for a ground state; for $n = 3$ it is positive, because the push from $n = 1$ below is the strongest one.

```{code-cell} python
:tags: [hide-input]
# synced: orders_vs_strength
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The two lowest levels of the box against the height of the bump. First order is the tangent to the exact curve at $V_0 = 0$; second order adds its curvature. Shaded: bump heights larger than the gap $E_2^{(0)} - E_1^{(0)} = 3E_1^{(0)}$.

- **Small bump, good answer.** While $V_0$ is well below the gap between the levels, second order is indistinguishable from the exact curve.
- **Large bump, drifting answer.** Once $V_0$ exceeds the gap, first order overshoots badly and second order begins to bend away. A perturbation that large is no longer a correction, and the matrix should be diagonalized instead, which is what the `exact` line of the cell does.

Turn the perturbation on yourself. The bump raises the levels; the slope polarizes the ground state.

```{anywidget} ../widgets/perturbation_dial.mjs
{}
```

### Helium, order by order

:::{note} **Example: the ground state of helium**

Treat the repulsion between the two electrons of helium as the perturbation.

- **Unperturbed.** Without the repulsion each electron is in the 1s state of He$^+$, with energy $-Z^2E_h/2 = -2E_h$. Two of them: $E^{(0)} = -4E_h = -108.8$ eV.
- **First order.** The average of $1/r_{12}$ over the product of two 1s orbitals is $\frac{5}{8}Z\,E_h$ ([Lecture 6.1](01-variational-method.md)). With $Z = 2$: $E^{(1)} = +\frac{5}{4}E_h = +34.0$ eV, and $E^{(0)} + E^{(1)} = -74.8$ eV.
- **Second order.** The sum over excited states gives $E^{(2)} = -0.158\,E_h = -4.3$ eV, for a total of $-79.1$ eV.

The measured energy is $-79.01$ eV.
:::

```{code-cell} python
:tags: [hide-input]
# synced: helium_orders
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
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
plt.show()
```

Fig. The ground-state energy of helium. Left: the repulsion raises the unperturbed energy by 34.0 eV in first order. Right, enlarged: first order, second order and the variational result of Lecture 6.1 against the exact energy (dashed).

- **The perturbation is not small**, 34 eV on a scale of 109 eV, and two orders still land within 0.1 eV. The second-order term is eight times smaller than the first.
- **First order is the $\zeta = 2$ energy of Lecture 6.1.** Both are $\langle\phi|\hat{H}|\phi\rangle$ for the unperturbed product of 1s orbitals, so first order is an upper bound.
- **Second order is below the exact energy.** Perturbation theory is not a bound: its results can fall on either side of the truth. The variational energy, $-77.5$ eV, is less accurate here but is guaranteed to be above.

### Perturbations already met

Several results of earlier lectures were perturbation theory under other names.

| effect | solved problem | perturbation | order | lecture |
| :-- | :-- | :-- | :-: | :-: |
| anharmonic levels, $-\tilde{\nu}_ex_e(v + \frac{1}{2})^2$ | harmonic oscillator | cubic and quartic terms of the bond potential | 1st and 2nd | [4.3](../ch04/03-molecular-vibrations.md) |
| centrifugal distortion, $-DJ^2(J + 1)^2$ | rigid rotor | stretching of the bond by rotation | 2nd | [4.5](../ch04/05-rigid-rotor.md) |
| Zeeman effect, $\mu_BBm_l$ | hydrogen atom | $(\mu_BB/\hbar)\hat{L}_z$ | 1st, exact | [5.3](../ch05/03-spin.md) |
| fine structure | hydrogen atom | spin-orbit coupling | 1st, degenerate | [5.3](../ch05/03-spin.md) |
| polarizability, $-\frac{1}{2}\alpha\mathcal{E}^2$ | atom or molecule | $-\hat{M}\mathcal{E}$, dipole in a field | 2nd | this lecture |
| dispersion forces, $-C_6/R^6$ | two separate atoms | interaction of their dipoles | 2nd | Problem 7 |
| helium | two hydrogenlike electrons | repulsion $1/r_{12}$ | 1st, 2nd | this lecture |

- **The Zeeman shift is exact at first order.** The perturbation $\hat{L}_z$ commutes with the hydrogen Hamiltonian, so the two share eigenfunctions and every off-diagonal element $\langle k|\hat{L}_z|n\rangle$ vanishes. There is nothing left for second order to add (Problem 6).
- **Second-order effects are attractions.** Polarization and dispersion both lower the ground state, as every second-order correction to a ground state must.

The two methods of this chapter meet at the two-level problem: the variational method gives its exact roots, and perturbation theory gives the same roots as a series in the coupling over the gap. A perturbation that changes in time does something neither method has described yet: it moves a system from one level to another. That is how light is absorbed, and it is the subject of [Lecture 6.3](03-time-dependent-perturbation-and-selection-rules.md).

:::{seealso} Computational lab
[Perturbation theory](../demos/10-demo-perturbation-theory.md) computes these corrections for a box in a Colab notebook.
:::

### Problems

#### Problem 1: A sloping floor

The floor of a box of length $L$ slopes, $\hat{H}^{(1)} = \varepsilon x$ for $0 \leq x \leq L$. Find the first-order shift of every level. What does first order say about the spacings between the levels?

:::{admonition} **Solution**
:class: dropdown solution

$$
E_n^{(1)} = \langle n|\varepsilon x|n\rangle = \varepsilon\,\langle x\rangle_n = \frac{\varepsilon L}{2}
$$

for every $n$, because every box state has its density symmetric about the middle, so $\langle x\rangle = L/2$ ([Lecture 3.2](../ch03/02-particle-in-a-box.md)). All levels rise by the same amount, the average height of the floor, and to first order no spacing changes.

The spacings do change, in second order. Writing $\varepsilon x = \varepsilon L/2 + \varepsilon(x - L/2)$ separates a constant, which shifts everything equally, from an odd part, which is the tilted box of the figure above. The odd part has no first-order effect and lowers the ground state in second order.
:::

#### Problem 2: Move the bump

The bump of height $V_0$ now covers the left fifth of the box, from $0$ to $0.2L$. (a) Without calculating, rank the first-order shifts of the levels $n = 1, 2, 3$. (b) Compute them from $E_n^{(1)} = V_0\int_0^{0.2L}(2/L)\sin^2(n\pi x/L)\,dx$. (c) Why does the ranking differ from that of the bump in the middle? (d) For very large $n$, what does the first-order shift become, and why?

#### Problem 3: Why long molecules are easy to polarize

Model a $\pi$ electron of a conjugated chain as a particle of charge $-e$ in a box of length $L$, in a field $\mathcal{E}$ along the chain: $\hat{H}^{(1)} = e\mathcal{E}(x - L/2)$. (a) Find the second-order shift of the ground state, keeping only the nearest level, $n = 2$, with $\langle 2|x|1\rangle = -16L/9\pi^2$. (b) From $E^{(2)} = -\frac{1}{2}\alpha\mathcal{E}^2$ find the polarizability, and evaluate $\alpha/4\pi\varepsilon_0$ in Å$^3$ for $L = 1.0$ nm. (c) How does $\alpha$ grow with $L$?

:::{admonition} **Solution**
:class: dropdown solution

(a) First order vanishes, because the perturbation is odd about the middle of the box. In second order the gap is $E_1^{(0)} - E_2^{(0)} = -3E_1^{(0)}$:

$$
E_1^{(2)} \approx \frac{\left(e\mathcal{E}\cdot16L/9\pi^2\right)^2}{-3E_1^{(0)}} = -\frac{256}{243\pi^4}\,\frac{e^2\mathcal{E}^2L^2}{E_1^{(0)}} = -0.0108\,\frac{e^2\mathcal{E}^2L^2}{E_1^{(0)}}
$$

Summing over all the other levels changes the number only from 0.01082 to 0.01083: the nearest level carries 99.9% of the sum.

(b) $\alpha = 2\times0.0108\,e^2L^2/E_1^{(0)}$. For an electron and $L = 1.0$ nm, $E_1^{(0)} = h^2/8m_eL^2 = 0.376$ eV $= 6.02\times10^{-20}$ J:

$$
\alpha = \frac{0.0216\times(1.602\times10^{-19}\ \text{C})^2\,(10^{-9}\ \text{m})^2}{6.02\times10^{-20}\ \text{J}}
$$

$$
= 9.2\times10^{-39}\ \text{C}^2\,\text{m}^2\,\text{J}^{-1}
$$

$$
\frac{\alpha}{4\pi\varepsilon_0} = \frac{9.2\times10^{-39}}{1.113\times10^{-10}}\ \text{m}^3 = 8.3\times10^{-29}\ \text{m}^3 = 83\ \text{Å}^3
$$

For comparison, a helium atom has 0.2 Å$^3$ and benzene about 10 Å$^3$.

(c) $E_1^{(0)} \propto 1/L^2$, so $\alpha \propto L^2/E_1^{(0)} \propto L^4$. Doubling the length of the chain multiplies the polarizability by 16: the levels move closer together and the transition dipole grows, and both help. Long conjugated molecules are among the most polarizable known, which is why they are used in nonlinear optics.
:::

#### Problem 4: Two-electron ions in first order

For a nucleus of charge $Z$ with two electrons, the helium example generalizes to $E^{(0)} = -Z^2E_h$ and $E^{(1)} = \frac{5}{8}Z\,E_h$. (a) Compute $E^{(0)} + E^{(1)}$ for H$^-$, Li$^+$ and Be$^{2+}$. (b) The exact energies are $-0.5278$, $-7.2799$ and $-13.6556$ hartree. Find the percent error of first order for each, and for helium. (c) Why does the error shrink as $Z$ grows? Compare the size of the perturbation with the size of the unperturbed energy.

#### Problem 5: A slightly stiffer spring

The force constant of an oscillator is raised from $k$ to $k + \delta k$, so that $\hat{H}^{(1)} = \frac{1}{2}\delta k\,x^2$. (a) Find the first-order shift of level $v$, using $\langle x^2\rangle = (v + \frac{1}{2})\hbar/\mu\omega$. (b) The problem can be solved exactly: the new oscillator has $\omega' = \sqrt{(k + \delta k)/\mu}$. Expand the exact levels in powers of $\delta k/k$ and compare.

:::{admonition} **Solution**
:class: dropdown solution

(a) With $k = \mu\omega^2$,

$$
E_v^{(1)} = \tfrac{1}{2}\delta k\,\langle x^2\rangle = \tfrac{1}{2}\delta k\left(v + \tfrac{1}{2}\right)\frac{\hbar}{\mu\omega} = \frac{\delta k}{2k}\left(v + \tfrac{1}{2}\right)\hbar\omega
$$

(b) Exactly, $E_v = (v + \frac{1}{2})\hbar\omega'$ with $\omega' = \omega\sqrt{1 + \delta k/k}$. Using $\sqrt{1 + x} = 1 + \frac{1}{2}x - \frac{1}{8}x^2 + \dots$:

$$
E_v = \left(v + \tfrac{1}{2}\right)\hbar\omega\left[1 + \frac{\delta k}{2k} - \frac{1}{8}\left(\frac{\delta k}{k}\right)^2 + \dots\right]
$$

The first term is the unperturbed level, the second is exactly the first-order result of (a), and the third is what second-order perturbation theory would give, $-\frac{1}{8}(\delta k/k)^2(v + \frac{1}{2})\hbar\omega$. Perturbation theory is the Taylor series of the exact answer in the strength of the perturbation. For $\delta k/k = 0.1$ first order gives a factor 1.0500 against the exact 1.0488.
:::

#### Problem 6: When first order is exact

Suppose the perturbation commutes with the unperturbed Hamiltonian, $[\hat{H}^{(0)}, \hat{H}^{(1)}] = 0$, and the unperturbed states are chosen as eigenfunctions of both. (a) Show that every off-diagonal element $\langle k|\hat{H}^{(1)}|n\rangle$ with $k \neq n$ vanishes. (b) What does that make of the second-order energy and of the first-order correction to the state? (c) Apply this to a hydrogen atom in a magnetic field, $\hat{H}^{(1)} = (\mu_BB/\hbar)\hat{L}_z$, and recover the Zeeman levels of Lecture 5.3. (d) Why does the same argument fail for an electric field, $\hat{H}^{(1)} = e\mathcal{E}z$?

#### Problem 7: Why argon atoms attract

Two neutral atoms with no permanent dipoles still attract each other. Model each atom as a charge $q$ on a spring (mass $\mu$, frequency $\omega$) and place the two a distance $R$ apart along the $x$ axis. Their displacements $x_1$ and $x_2$ are two dipoles $qx_1$ and $qx_2$, which interact with the energy

$$
\hat{H}^{(1)} = -\frac{2q^2}{4\pi\varepsilon_0R^3}\,x_1x_2
$$

(a) Show that the first-order shift of the ground state $|0, 0\rangle$ is zero. (b) Find the second-order shift. (c) Write it in terms of the polarizability volume $\alpha' = q^2/4\pi\varepsilon_0k$ and estimate it for two argon atoms, with $\alpha' = 1.64$ Å$^3$, $\hbar\omega = 15.8$ eV (the ionization energy) and $R = 3.8$ Å.

:::{admonition} **Solution**
:class: dropdown solution

The unperturbed problem is two independent oscillators, with states $|v_1, v_2\rangle$ and energies $(v_1 + v_2 + 1)\hbar\omega$.

(a) $\langle 0, 0|x_1x_2|0, 0\rangle = \langle 0|x_1|0\rangle\langle 0|x_2|0\rangle = 0$: neither atom has an average dipole.

(b) Each $x$ raises its own oscillator by one level, $x|0\rangle = \sqrt{\hbar/2\mu\omega}\,|1\rangle$, so $x_1x_2|0, 0\rangle = (\hbar/2\mu\omega)\,|1, 1\rangle$. The perturbation connects the ground state to one state only, $|1, 1\rangle$, which lies $2\hbar\omega$ higher:

$$
E^{(2)} = \frac{1}{-2\hbar\omega}\left(\frac{2q^2}{4\pi\varepsilon_0R^3}\cdot\frac{\hbar}{2\mu\omega}\right)^2 = -\frac{\hbar\omega}{2}\left(\frac{q^2}{4\pi\varepsilon_0\,\mu\omega^2}\right)^2\frac{1}{R^6}
$$

(c) Since $k = \mu\omega^2$, the bracket is the polarizability volume:

$$
E^{(2)} = -\frac{\hbar\omega}{2}\,\frac{\alpha'^2}{R^6} = -\frac{15.8\ \text{eV}}{2}\times\frac{(1.64)^2}{(3.8)^6}
$$

$$
= -7.1\times10^{-3}\ \text{eV} = -0.7\ \text{kJ/mol}
$$

The measured depth of the argon-argon well is 1.2 kJ/mol; a one-dimensional model gets the size right.

This is the **dispersion** (London) force. Each atom's charge cloud fluctuates, since the ground state has a spread in $x$; the fluctuating dipole of one atom polarizes the other, and the correlated motion lowers the energy. It is attractive because it is a second-order shift of a ground state, it falls off as $1/R^6$ because the dipole-dipole coupling $1/R^3$ enters squared, and it grows with the square of the polarizability, which is why large atoms and molecules have higher boiling points.
:::

#### Problem 8: A bound and not a bound

For helium, $E^{(0)} + E^{(1)} = -74.8$ eV lies above the exact $-79.0$ eV, and $E^{(0)} + E^{(1)} + E^{(2)} = -79.1$ eV lies below it. (a) Use the variational theorem of Lecture 6.1 to show that $E_n^{(0)} + E_n^{(1)}$ is an upper bound for the ground state of any system. (b) Why does the theorem say nothing about the sum through second order? (c) The unperturbed energy alone, $E^{(0)} = -108.8$ eV, is far below the exact value. Does that contradict the variational theorem? Of which Hamiltonian is $-108.8$ eV an average?
