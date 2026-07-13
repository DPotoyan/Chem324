# DEMO: Numerical Schrödinger Solver

:::{note} **What you need to know**

- Only a handful of potentials (particle in a box, harmonic oscillator, hydrogen atom) can be solved with pencil and paper. Every other Schrödinger equation in chemistry is solved **numerically**.
- The **finite-difference method** samples the wavefunction on a grid and replaces derivatives with differences between neighboring points. The Schrödinger equation becomes a **matrix eigenvalue problem**: eigenvalues are the allowed energies, eigenvectors are the wavefunctions.
- Placing a barrier inside a box splits the energy levels into closely spaced **tunneling doublets**, a first look at a phenomenon that returns in ammonia inversion and hydrogen transfer reactions.
- This page is **reactive**: the Python cells below run live in your browser. Move the slider and every plot that depends on it recomputes. No installation is needed.
:::

### From differential equation to matrix problem

We want the bound states of the time-independent Schrödinger equation on $0 \le x \le L$ with hard walls, the same boundary conditions as the [particle in a box](./03-particle-in-a-box.md):

```{math}
:label: eq-tise-grid

-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\,\psi(x) = E\,\psi(x),
\qquad \psi(0) = \psi(L) = 0
```

Instead of guessing a functional form for $\psi(x)$, we store its values $\psi_1, \psi_2, \dots, \psi_N$ at $N$ evenly spaced grid points, as sketched in [](#fig-fd-grid). On the grid, the second derivative at point $j$ is approximated by the classic three-point formula [@press2007]:

```{math}
:label: eq-three-point

\frac{d^2\psi}{dx^2}\bigg|_{x_j} \approx \frac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{\Delta x^2}
```

:::{figure} images/fd-grid.png
:label: fig-fd-grid
:alt: A smooth wavefunction sampled at evenly spaced grid points between two hard walls
:width: 85%

A wavefunction sampled on a uniform grid between hard walls. The curvature at point $j$ is built from the point and its two neighbors (red circles), which turns the differential equation into a matrix problem.
:::

Substituting [](#eq-three-point) into [](#eq-tise-grid) gives one linear equation per grid point. Collecting them produces a matrix eigenvalue problem $\mathbf{H}\,\boldsymbol{\psi} = E\,\boldsymbol{\psi}$ with a **tridiagonal** Hamiltonian: kinetic energy couples each point only to its two neighbors, and the potential sits on the diagonal.

$$
\mathbf{H} =
\frac{\hbar^2}{2m\,\Delta x^2}
\begin{pmatrix}
2 & -1 & & \\
-1 & 2 & -1 & \\
& \ddots & \ddots & \ddots \\
& & -1 & 2
\end{pmatrix}
+
\begin{pmatrix}
V_1 & & & \\
& V_2 & & \\
& & \ddots & \\
& & & V_N
\end{pmatrix}
$$

Diagonalizing $\mathbf{H}$ hands us energies and wavefunctions in one shot. The LAPACK routines that do this are the same machinery running inside every modern quantum chemistry package.

### A box with a barrier inside

As a test system we take the unit box and drop a rectangular barrier of height $V_0$ and width $L/4$ into the middle. With $\hbar = m = L = 1$, the natural energy unit is the ground-state energy of the empty box from the [particle in a box lecture](./03-particle-in-a-box.md):

$$
E_1 = \frac{\pi^2 \hbar^2}{2mL^2} = \frac{h^2}{8mL^2}
$$

For $V_0 = 0$ the solver must reproduce $E_n = n^2 E_1$ exactly, which is a good sanity check. As $V_0$ grows, the box splits into two weakly coupled half-boxes, and pairs of levels squeeze together into **doublets**: a symmetric state with no node at the center and an antisymmetric partner with one. Their tiny energy difference is the **tunneling splitting**, the standard textbook route to double-well physics [@griffiths2018].

### The live solver

```{marimo-config}
---
echo: true
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "scipy",
      "matplotlib",
  ]
---
```

We need only the course's standard scientific stack: NumPy for arrays, SciPy for the tridiagonal eigensolver, and Matplotlib for plots.

```{marimo} python
import time

import marimo as mo
import numpy as np
from scipy.linalg import eigh_tridiagonal
import matplotlib.pyplot as plt
```

The solver builds the two diagonals of $\mathbf{H}$ and asks SciPy for the lowest few eigenpairs. Dividing the eigenvectors by $\sqrt{\Delta x}$ normalizes them so that $\int |\psi|^2\,dx = 1$.

```{marimo} python
E1 = np.pi**2 / 2  # ground-state energy of the empty box (hbar = m = L = 1)


def solve_box(v0, n_grid=1500, n_states=4, width=0.25):
    """Lowest eigenstates of a unit box with a central barrier of height v0."""
    x = np.linspace(0.0, 1.0, n_grid + 2)[1:-1]  # interior points, psi = 0 at walls
    dx = x[1] - x[0]
    v = np.where(np.abs(x - 0.5) < width / 2, v0, 0.0)
    diag = 1.0 / dx**2 + v
    off = np.full(n_grid - 1, -0.5 / dx**2)
    energies, vectors = eigh_tridiagonal(
        diag, off, select="i", select_range=(0, n_states - 1)
    )
    return x, v, energies, vectors / np.sqrt(dx)
```

Drag the slider to raise or lower the barrier. Everything below it reacts.

```{marimo} python
barrier = mo.ui.slider(
    start=0,
    stop=100,
    step=5,
    value=40,
    show_value=True,
    label="Barrier height V0 in units of E1",
)
barrier
```

```{marimo} python
x_now, v_now, e_now, psi_now = solve_box(barrier.value * E1)

fig_psi, ax_psi = plt.subplots(figsize=(7, 4.3))
ax_psi.fill_between(x_now, 0.0, v_now / E1, color="0.88")
for e_i, psi_i in zip(e_now / E1, psi_now.T):
    ax_psi.axhline(e_i, color="0.75", lw=0.7)
    ax_psi.plot(x_now, e_i + 1.6 * psi_i, lw=1.8, label=f"E = {e_i:.2f} E1")
ax_psi.set_xlabel("x / L")
ax_psi.set_ylabel("energy / E1  (wavefunctions offset)")
ax_psi.set_xlim(0, 1)
ax_psi.set_ylim(0, float(np.max(e_now / E1)) * 1.25 + 3)
ax_psi.legend(loc="upper right", fontsize=8, frameon=False)
fig_psi
```

With the barrier at zero you should read off $E/E_1 = 1, 4, 9, 16$, the exact particle in a box ladder. Raise the barrier and watch $n = 1, 2$ collapse onto each other while keeping opposite symmetry about the center.

### Tunneling doublets across all barrier heights

A single click of the slider solves one Hamiltonian. The cell below instead sweeps the full range of barrier heights, a **moderately expensive computation**: 51 diagonalizations of a $2000 \times 2000$ matrix, tracking the six lowest states. Because it does not read the slider, marimo executes it once and reuses the cached result no matter how much you play with the plots.

```{marimo} python
n_sweep = 2000
heights = np.linspace(0.0, 100.0, 51)
t0 = time.perf_counter()
sweep = (
    np.array([solve_box(h * E1, n_grid=n_sweep, n_states=6)[2] for h in heights])
    / E1
)
t_sweep = time.perf_counter() - t0

mo.md(
    f"Diagonalized a {n_sweep} x {n_sweep} Hamiltonian at {len(heights)} "
    f"barrier heights in **{t_sweep:.2f} s**. This cell ignores the slider, "
    "so marimo runs it once and caches `sweep`."
)
```

The correlation diagram replots instantly when you move the slider, because only the cheap plotting cell reruns, not the sweep.

```{marimo} python
fig_corr, ax_corr = plt.subplots(figsize=(7, 4.3))
for n_idx in range(sweep.shape[1]):
    ax_corr.plot(heights, sweep[:, n_idx], lw=1.8, label=f"n = {n_idx + 1}")
ax_corr.axvline(barrier.value, color="crimson", ls="--", lw=1.2)
ax_corr.set_xlabel("barrier height V0 / E1")
ax_corr.set_ylabel("energy / E1")
ax_corr.legend(frameon=False, fontsize=9)
fig_corr
```

:::{attention} **Things to try**

- Find the barrier height where $n = 1$ and $n = 2$ first become indistinguishable on the plot. Compare it with where the $n = 3, 4$ pair merges. Why do the higher states need a taller barrier?
- At $V_0 = 100\,E_1$, zoom into the wavefunction plot: the ground state has no node at the center while its doublet partner has one, yet their energies nearly coincide. This is the quantum mechanics behind the ammonia umbrella inversion.
- Set the barrier to zero and check the solver against the exact ladder $E_n = n^2 E_1$. Estimate the accuracy of the finite-difference approximation from the $n = 4$ level.
:::

:::{tip} How this page works
:class: dropdown

This demo pilots [marimo](https://marimo.io) cells inside the course website. The cells are executed while the site is built, so the page loads with correct static output. The first time you touch the slider, a Python runtime (Pyodide, Python compiled to WebAssembly) downloads in the background along with NumPy, SciPy, and Matplotlib, and from then on all cells rerun locally in your browser. Unlike the ipywidgets demos, nothing needs to run on a server, and unlike static pages, every plot stays live.
:::
