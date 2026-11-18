---
kernelspec:
  name: python3
  display_name: Python 3
---

# DEMO: Linear Variational Method

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/appendix-demo-linear-variational.ipynb)

```{code-cell} python
:tags: [hide-input]

import numpy as np
from scipy.linalg import eigh, eigh_tridiagonal
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
```

:::{note} **What this lab does**

- [Lecture 6.1](../ch06/01-variational-method.md) showed that a trial function built from fixed basis functions, $\phi = \sum_n c_nf_n$, has its best energies at the roots of $\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}$, with $H_{ij} = \langle f_i|\hat{H}|f_j\rangle$ and $S_{ij} = \langle f_i|f_j\rangle$.
- Here that equation becomes one short function that works for **any one-dimensional well and any basis**: the matrix elements are computed by numerical integration on a grid.
- **Experiment 1**: a spring, with Gaussians of the wrong widths. The lowest root steps down toward the exact energy and never passes it.
- **Experiment 2**: a double well, with one Gaussian in each well. This is the two-level problem of Lecture 6.1 and a first look at the chemical bond.
- **Your turn**: five short tasks at the end.

:::

## The method as one function

Units: $\hbar = m = 1$. The matrix elements are integrals over the grid `x`. The kinetic energy uses the slopes, $\langle f_i|\hat{T}|f_j\rangle = \frac{1}{2}\int f_i'f_j'\,dx$, as in Lecture 6.1.

```{code-cell} python
x = np.linspace(-12, 12, 4001)                    # the grid for every integral

def variational(basis, V):
    """Best energies and coefficients for a list of basis functions in the well V(x)."""
    f = np.array(basis)                           # one basis function per row
    df = np.gradient(f, x, axis=1)                # their slopes
    # every pair (i, j) at once: overlaps, kinetic energy, potential energy
    S = np.trapezoid(f[:, None, :] * f[None, :, :], x)
    T = 0.5 * np.trapezoid(df[:, None, :] * df[None, :, :], x)
    U = np.trapezoid(f[:, None, :] * V(x) * f[None, :, :], x)
    return eigh(T + U, S)                         # solves H c = E S c
```

`eigh(H, S)` returns the roots in ascending order and the coefficients as columns: `C[:, 0]` belongs to the lowest root.

## Experiment 1: a spring, with the wrong Gaussians

For $V = \frac{1}{2}x^2$ the exact ground state is $e^{-x^2/2}$ with $E_0 = \frac{1}{2}$. Pretend not to know it, and build the trial function from Gaussians $e^{-ax^2}$ whose exponents all miss the right value, $a = \frac{1}{2}$:

```{code-cell} python
spring = lambda x: 0.5 * x**2
exponents = [0.1, 0.2, 0.4, 0.8, 1.6]

for N in range(1, 6):
    basis = [np.exp(-a * x**2) for a in exponents[:N]]
    E, C = variational(basis, spring)
    print(f"{N} Gaussians: lowest root {E[0]:.5f}    (exact 0.50000)")
```

```{code-cell} python
fig, ax = plt.subplots(figsize=(6, 3.4))
exact = np.pi**-0.25 * np.exp(-0.5 * x**2)
ax.plot(x, exact, color="gray", lw=5, alpha=0.5, label="exact")
for N, style in ((1, ":"), (2, "--"), (5, "-")):
    basis = np.array([np.exp(-a * x**2) for a in exponents[:N]])
    E, C = variational(basis, spring)
    phi = C[:, 0] @ basis                         # the best mixture
    phi = phi / np.sqrt(np.trapezoid(phi**2, x)) * np.sign(phi[len(x) // 2])
    ax.plot(x, phi, style, color="teal", label=f"{N} Gaussian" + ("s" if N > 1 else ""))
ax.set_xlim(-5, 5); ax.set_xlabel("x"); ax.set_ylabel("trial function"); ax.legend(frameon=False)
plt.show()
```

- **Every added function lowers the root**, and no root is below $\frac{1}{2}$: the variational theorem at work.
- **One poor Gaussian gives 1.3; five give 0.50003.** None of the five has the right width. Their mixture does.
- **The higher roots are bounds too.** All these basis functions are even, so the second root approaches the next even level, $E_2 = 2.5$.

## Experiment 2: a double well and the two-level problem

Put two parabolas side by side, with minima at $x = \pm a$ and a barrier between them:

$$
V(x) = \tfrac{1}{2}\left(|x| - a\right)^2
$$

Each well alone would hold the state $e^{-(x \mp a)^2/2}$ with energy $\frac{1}{2}$. Use those two functions as the basis: one "orbital" on each "atom".

```{code-cell} python
a = 1.5
double = lambda x: 0.5 * (np.abs(x) - a)**2       # two wells at -a and +a, barrier a^2/2
left = np.exp(-0.5 * (x + a)**2)                  # the ground state of the left well alone
right = np.exp(-0.5 * (x - a)**2)                 # and of the right well

E, C = variational([left, right], double)
print("roots:", np.round(E, 4))
print("mixtures (columns):")
print(np.round(C / C[0], 3))                      # each column scaled so its first entry is 1
```

The two basis functions have the same energy, so they mix half and half: the lower root belongs to `left + right` and the upper one to `left - right`. Compare with the levels of this well solved on a grid, as in [the numerical Schrödinger lab](07-demo-numerical-schrodinger.md):

```{code-cell} python
dx = x[1] - x[0]
grid = eigh_tridiagonal(1 / dx**2 + double(x), -np.ones(len(x) - 1) / (2 * dx**2),
                        select="i", select_range=(0, 1))[0]
print("two Gaussians :", np.round(E, 4))
print("grid, exact   :", np.round(grid, 4))
```

```{code-cell} python
fig, ax = plt.subplots(figsize=(6, 3.6))
ax.plot(x, double(x), color="k", lw=2)
for k, color in ((0, "teal"), (1, "darkorange")):
    phi = C[:, k] @ np.array([left, right])
    phi = phi / np.sqrt(np.trapezoid(phi**2, x))
    ax.axhline(E[k], color=color, lw=0.8, ls=":")
    phi = phi * np.sign(phi[np.argmax(np.abs(phi) * (x < 0))])   # left lobe drawn upward
    ax.plot(x, E[k] + 0.35 * phi, color=color, label=f"root {k + 1}: E = {E[k]:.3f}")
ax.set_xlim(-5, 5); ax.set_ylim(0, 1.4); ax.set_xlabel("x"); ax.set_ylabel("energy")
ax.legend(frameon=False)
plt.show()
```

- **Two equal levels split in two.** Alone, each well has the energy 0.5. Together they give one level below and one above: the two-level problem of Lecture 6.1 with $\Delta = 0$.
- **The lower state has no node between the wells**; the upper one changes sign there. Replace the wells by two protons and the Gaussians by 1s orbitals, and these are the bonding and antibonding orbitals of H$_2^+$ ([Chapter 8](../ch08/02-hydrogen-molecule-ion.md)).
- **Two functions already come close** to the exact levels. More functions close the rest of the gap:

```{code-cell} python
centers, widths = (-a, -a / 2, 0, a / 2, a), (0.25, 1.0)
extra = [np.exp(-w * (x - c)**2) for c in centers for w in widths]
E12, C12 = variational([left, right] + extra, double)
print(" 2 functions:", np.round(E, 4))
print("12 functions:", np.round(E12[:2], 4))
print("grid, exact :", np.round(grid, 4))
```

## Your turn

1. In Experiment 1, replace the list of exponents by `[0.5]`. What root do you get with a single function, and why?
2. Change the well of Experiment 1 to the V-shaped well, `lambda x: np.abs(x)`. One Gaussian can do no better than 0.813 (Lecture 6.1, Problem 4), and the exact energy is 0.809. How many Gaussians do you need to reach 0.809?
3. In Experiment 2, raise the barrier by setting `a = 2.0` and then `a = 2.5`. What happens to the gap between the two roots? Relate it to tunneling ([Lecture 3.4](../ch03/03-tunneling-and-finite-square-well.md)) and to the overlap of the two basis functions.
4. Read $\alpha = H_{11}/S_{11}$, $\beta = H_{12}/S_{11}$ and $S = S_{12}/S_{11}$ off the matrices of Experiment 2 (print them inside `variational`), and check the roots against $(\alpha \pm \beta)/(1 \pm S)$ from Problem 5 of Lecture 6.1.
5. Make the two wells unequal by adding a slope, `lambda x: 0.5 * (np.abs(x) - a)**2 + 0.1 * x`. Do the two basis functions still mix half and half? Which well does the lower state prefer, and why?
