---
kernelspec:
  name: python3
  display_name: Python 3
---

# Operators

:::{note} **What you need to know**

- An operator turns one function into another. Quantum operators are **linear**, so they respect superposition: acting on a sum gives the sum of the results.
- Sample a function on a grid and it becomes a **vector**; every operator becomes a **matrix**. Position is diagonal, derivatives link neighboring points, and solving $\hat{H}\psi = E\psi$ becomes finding the eigenvalues of a matrix: by hand for three points, with five lines of numpy for four hundred.
- Every observable is a **Hermitian** operator, $\hat{A}^\dagger = \hat{A}$. Hermitian operators have **real eigenvalues** and **orthogonal eigenfunctions** that form a **complete basis**: exactly what a measurement needs.
- Operators need not **commute**. The commutator $[\hat{A},\hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ measures the difference between the two orders, and for position and momentum it is never zero: $[\hat{x},\hat{p}] = i\hbar$.
- Operators that commute share their eigenfunctions, so their observables can have sharp values at the same time. Position and momentum cannot.
- **Dirac notation** writes all of this in one form that does not care whether we use integrals or matrices, and it translates line by line into numpy.

:::

### The rules of the game

This lecture and the next two complete the short list of rules, the **postulates**, from which all of quantum mechanics follows. Two of them we have already met.

| | Postulate | Lecture |
| :-- | :-- | :-- |
| 1 | The state of a system is a wavefunction $\psi$, and $\lvert\psi\rvert^2$ is the probability density | [The Schrödinger Equation](01-schrodinger-equation.md) |
| 2 | Every observable is represented by a linear Hermitian operator $\hat{A}$ | this lecture |
| 3 | A measurement of $A$ returns one of the eigenvalues $a_n$ of $\hat{A}$ and leaves the system in its eigenfunction $\phi_n$ | [Measurement](05-eigenvalues-and-expectation.md) |
| 4 | The outcome $a_n$ has probability $\lvert\langle \phi_n \vert \psi\rangle\rvert^2$, so the average is $\langle A\rangle = \langle \psi \vert \hat{A} \vert \psi \rangle$ | [Measurement](05-eigenvalues-and-expectation.md) |
| 5 | The state evolves by $i\hbar\,\partial\Psi/\partial t = \hat{H}\Psi$ | [The Schrödinger Equation](01-schrodinger-equation.md), [Time Dependence](06-time-dependence.md) |

### Operators act on functions

- In [The Schrödinger Equation](01-schrodinger-equation.md) we built operators by a recipe: write the classical expression in $x$ and $p$, then replace $p$ by $-i\hbar\,d/dx$. We also met eigenfunctions, the functions an operator returns unchanged up to a constant, and expectation values.
- The recipe leaves two questions open. Which operators are allowed to stand for something we can measure? And what happens when two operators do not commute? Answering them is the job of this lecture.
- An operator is any rule that turns a function into another function: multiply by $x$, differentiate, integrate, square. Quantum mechanics uses only one kind.

#### Linear operators

:::{important} **Linear operator**

$$
\hat{A}\,\big(c_1\psi_1 + c_2\psi_2\big) = c_1\,\hat{A}\psi_1 + c_2\,\hat{A}\psi_2
$$

for any functions $\psi_1$, $\psi_2$ and any complex numbers $c_1$, $c_2$.

:::

- Linearity is what superposition demands. If $\Psi_1$ and $\Psi_2$ both solve $i\hbar\,\partial\Psi/\partial t = \hat{H}\Psi$, their sum is again a solution only when $\hat{H}$ is linear. Interference, from the double slit to the sloshing particle in a box, shows that sums of states are states, so the operators must be linear.
- Derivatives and multiplication by a function are linear: the derivative of a sum is the sum of the derivatives. Squaring, square roots and logarithms are not.

:::{note} **Example: two tests for linearity**

Is the kinetic energy operator $\hat{K} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$ linear? Is squaring, $\hat{S}f = f^2$?

$$
\hat{K}\big(c_1f_1 + c_2f_2\big) = -\frac{\hbar^2}{2m}\big(c_1f_1'' + c_2f_2''\big) = c_1\hat{K}f_1 + c_2\hat{K}f_2
$$

so $\hat{K}$ is linear. For squaring,

$$
\hat{S}\big(c_1f_1 + c_2f_2\big) = c_1^2f_1^2 + 2c_1c_2f_1f_2 + c_2^2f_2^2 \ne c_1f_1^2 + c_2f_2^2
$$

The squared constants and the cross term $2c_1c_2f_1f_2$ both spoil it. A quick first test: a linear operator must turn $2f$ into $2\hat{A}f$, and squaring turns it into $4f^2$.

:::

### From operators to matrices

A computer cannot store a function, only a list of numbers. Turning functions into lists and operators into tables of numbers is how every quantum chemistry program works, and it makes the abstract properties of operators, Hermitian or commuting, concrete enough to check by eye. We build the dictionary in four steps. [Operators as Matrices](../math/04-operators-and-matrices.md) in Appendix A has more on each.

#### Step 1: a function becomes a vector

- Pick $N$ grid points $x_1, x_2, \dots, x_N$ spaced $h$ apart and record the value of the function at each one, $\psi_j = \psi(x_j)$. The function becomes a column of $N$ numbers.

```{code-cell} python
:tags: [hide-input]
# synced: function_vector
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
xs = np.linspace(0, 1, 400)
f = lambda x: np.sin(np.pi * x) + 0.45 * np.sin(2 * np.pi * x)
N, h = 7, 1 / 8
xj = h * np.arange(1, N + 1); fj = f(xj)
fig = plt.figure(figsize=(9, 3.7))
gs = fig.add_gridspec(1, 3, width_ratios=[2.6, 0.5, 0.9], wspace=0.05)
ax, axa, axv = (fig.add_subplot(gs[0, j]) for j in range(3))
ax.plot(xs, f(xs), color=TEAL, lw=2.6, label=r"$\psi(x)$")
ax.vlines(xj, 0, fj, color=GRAY, lw=1, ls=":")
ax.plot(xj, fj, "o", color=CARDINAL, ms=8, zorder=5)
for j, (xv, fv) in enumerate(zip(xj, fj), start=1):
    ax.text(xv, fv + 0.09, rf"$\psi_{j}$", ha="center", fontsize=12, color=CARDINAL)
ax.plot([0, 0], [0, 1.55], color="k", lw=2.6); ax.plot([1, 1], [0, 1.55], color="k", lw=2.6)
ax.axhline(0, color=GRAY, lw=0.8)
ax.annotate("", xy=(xj[3], -0.14), xytext=(xj[2], -0.14), arrowprops=dict(arrowstyle="<->", color="k", lw=1.2))
ax.text((xj[2] + xj[3]) / 2, -0.2, r"$h$", ha="center", va="top", fontsize=13)
ax.set_xlim(-0.03, 1.03); ax.set_ylim(-0.42, 1.6)
ax.set_xticks(list(xj)); ax.set_xticklabels([rf"$x_{j}$" for j in range(1, N + 1)], fontsize=12)
ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
ax.tick_params(length=0)
ax.set_title(r"a function, sampled at $N$ points spaced $h$ apart", loc="left", fontsize=12.5)
axa.axis("off")
axa.annotate("", xy=(0.95, 0.5), xytext=(0.05, 0.5), xycoords="axes fraction",
             arrowprops=dict(arrowstyle="simple,head_length=0.8,head_width=0.8,tail_width=0.3", color=PURPLE, alpha=0.8))
axv.axis("off"); axv.set_xlim(0, 1); axv.set_ylim(0, N + 1)
for j, fv in enumerate(fj, start=1):
    y = N + 0.5 - j
    axv.text(0.5, y, f"{fv:.2f}", ha="center", va="center", fontsize=13,
             bbox=dict(boxstyle="round,pad=0.25", fc="#fbeaec", ec=CARDINAL, lw=1))
    axv.text(0.02, y, rf"$\psi_{j}$", ha="left", va="center", fontsize=11, color=CARDINAL)
axv.plot([0.27, 0.22, 0.22, 0.27], [N + 0.35, N + 0.35, 0.15, 0.15], color="k", lw=1.4)
axv.plot([0.73, 0.78, 0.78, 0.73], [N + 0.35, N + 0.35, 0.15, 0.15], color="k", lw=1.4)
axv.set_title("a vector", fontsize=12.5)
fig.subplots_adjust(left=0.02, right=0.99, top=0.88, bottom=0.12)
plt.show()
```

Fig. A wavefunction in a box sampled at seven interior points. The walls, where $\psi = 0$, carry no unknowns. The seven samples, stacked in a column, are the vector that stands in for the function.

- Integrals become sums. The inner product of two functions becomes the dot product of their vectors, times the spacing:

$$
\int \phi^*\,\psi\,dx \;\approx\; \sum_{j} \phi_j^*\,\psi_j\,h, \qquad \int \lvert\psi\rvert^2\,dx = 1 \;\longrightarrow\; \sum_j \lvert\psi_j\rvert^2\,h = 1
$$

#### Step 2: multiplying by $x$ is a diagonal matrix

- $\hat{x}$ multiplies the value at each point by that point's own position, $(\hat{x}\psi)_j = x_j\,\psi_j$. As a matrix acting on the vector, every entry off the diagonal is zero:

$$
\hat{x}\,\psi \;\longrightarrow\;
\begin{pmatrix} x_1 & 0 & 0 & 0 \\ 0 & x_2 & 0 & 0 \\ 0 & 0 & x_3 & 0 \\ 0 & 0 & 0 & x_4 \end{pmatrix}
\begin{pmatrix} \psi_1 \\ \psi_2 \\ \psi_3 \\ \psi_4 \end{pmatrix}
=
\begin{pmatrix} x_1\psi_1 \\ x_2\psi_2 \\ x_3\psi_3 \\ x_4\psi_4 \end{pmatrix}
$$

- Any potential works the same way: $\hat{V}$ is the diagonal matrix of $V(x_1), \dots, V(x_N)$. Multiplying by a function never mixes different points.

#### Step 3: derivatives compare neighbors

- A derivative is a slope, and a slope needs two points. The **centered difference** uses the two neighbors of $x_j$. For the second derivative, take the change between the slopes on either side, $s_+ = (\psi_{j+1} - \psi_j)/h$ and $s_- = (\psi_j - \psi_{j-1})/h$, per unit length:

$$
\psi'(x_j) \approx \frac{\psi_{j+1} - \psi_{j-1}}{2h}, \qquad
\psi''(x_j) \approx \frac{s_+ - s_-}{h} = \frac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{h^2}
$$

```{code-cell} python
:tags: [hide-input]
# synced: difference_stencils
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
f = lambda x: 0.75 + 0.42 * np.sin(1.7 * x - 0.6) + 0.06 * x
df = lambda x: 0.42 * 1.7 * np.cos(1.7 * x - 0.6) + 0.06
xs = np.linspace(-0.2, 2.6, 300)
x0, h = 1.15, 0.55
pts = np.array([x0 - h, x0, x0 + h]); fp = f(pts)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.4, 4.0), gridspec_kw={"wspace": 0.1})
for ax in (a1, a2):
    ax.plot(xs, f(xs), color=GRAY, lw=2.2, alpha=0.8)
    ax.plot(pts, fp, "o", color=CARDINAL, ms=9, zorder=5)
    ax.set_xticks(pts); ax.set_xticklabels([r"$x_{j-1}$", r"$x_j$", r"$x_{j+1}$"], fontsize=12.5)
    ax.set_yticks([]); ax.spines["left"].set_visible(False)
    ax.set_xlim(-0.2, 2.6); ax.set_ylim(-0.62, 1.42)
t = np.array([x0 - 0.62, x0 + 0.62])
a1.plot(t, fp[1] + df(x0) * (t - x0), color="k", lw=1.6, ls="--", label=r"tangent at $x_j$: slope $\psi'(x_j)$")
sl = (fp[2] - fp[0]) / (2 * h)
a1.plot(t, fp[1] + sl * (t - x0), color=PURPLE, lw=2.4, label=r"slope of the chord: $(\psi_{j+1} - \psi_{j-1})/2h$")
a1.plot([pts[0], pts[2]], [fp[0], fp[2]], color=PURPLE, lw=1.4, ls=":")
a1.legend(loc="lower center", frameon=False, fontsize=11.5)
a1.set_title(r"first derivative: weights $-1,\ 0,\ +1$ times $1/2h$", loc="left", fontsize=12.5)
a2.plot(pts[:2], fp[:2], color=ORANGE, lw=2.6, label=r"$s_- = (\psi_j - \psi_{j-1})/h$")
a2.plot(pts[1:], fp[1:], color=TEAL, lw=2.6, label=r"$s_+ = (\psi_{j+1} - \psi_j)/h$")
a2.legend(loc="lower left", frameon=False, fontsize=11.5, bbox_to_anchor=(0.0, 0.13))
a2.text(0.01, 0.02, r"$\psi''(x_j) \approx \dfrac{s_+ - s_-}{h} = \dfrac{\psi_{j+1} - 2\psi_j + \psi_{j-1}}{h^2}$",
        transform=a2.transAxes, ha="left", va="bottom", fontsize=12.5)
a2.set_title(r"second derivative: weights $1,\ -2,\ 1$ times $1/h^2$", loc="left", fontsize=12.5)
fig.subplots_adjust(left=0.01, right=0.99, top=0.91, bottom=0.09)
plt.show()
```

Fig. Derivatives from neighboring samples. Left: the chord through the two neighbors of $x_j$ is almost parallel to the tangent at $x_j$, so its slope estimates $\psi'(x_j)$. Right: the slope drops from $s_-$ to $s_+$ across $x_j$; the drop per unit length estimates $\psi''(x_j)$, the curvature.

- Row $j$ of each matrix holds the weights of its stencil, centered on the diagonal. For four points, with $\psi = 0$ beyond the ends:

$$
\frac{d}{dx} \;\longrightarrow\; D_1 = \frac{1}{2h}\begin{pmatrix} 0 & 1 & 0 & 0 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \\ 0 & 0 & -1 & 0 \end{pmatrix},
\qquad
\frac{d^2}{dx^2} \;\longrightarrow\; D_2 = \frac{1}{h^2}\begin{pmatrix} -2 & 1 & 0 & 0 \\ 1 & -2 & 1 & 0 \\ 0 & 1 & -2 & 1 \\ 0 & 0 & 1 & -2 \end{pmatrix}
$$

- Multiply the first row of $D_2$ into the vector: $(-2\psi_1 + \psi_2)/h^2$. That is the stencil formula with $\psi_0 = 0$, the value at the wall, so the boundary condition is built into the matrix.
- Momentum is $\hat{p} = -i\hbar\,D_1$: entries $-i\hbar/2h$ above the diagonal and $+i\hbar/2h$ below.

:::{note} **Example: the grid derivative of a plane wave**

Apply the centered difference to the samples of a plane wave, $\psi_j = e^{ikx_j}$:

$$
\frac{\psi_{j+1} - \psi_{j-1}}{2h} = \frac{e^{ik(x_j + h)} - e^{ik(x_j - h)}}{2h} = \frac{e^{ikh} - e^{-ikh}}{2h}\,e^{ikx_j} = \frac{i\sin kh}{h}\,\psi_j
$$

The sampled plane wave is an **eigenvector** of the derivative matrix, just as $e^{ikx}$ is an eigenfunction of $d/dx$ (away from the ends of the grid). The eigenvalue $i\sin(kh)/h$ approaches the exact $ik$ when the grid is fine, $kh \ll 1$. Multiplied by $-i\hbar$, the momentum matrix returns $\hbar\sin(kh)/h \approx \hbar k$, the de Broglie momentum. The grid works when it has many points per wavelength.

:::

#### Step 4: the Hamiltonian is a matrix

- Put the pieces together: $\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)$ becomes $H = -\frac{\hbar^2}{2m}D_2 + V$. With the shorthand $t = \hbar^2/2mh^2$:

$$
H = \begin{pmatrix} 2t + V_1 & -t & 0 & 0 \\ -t & 2t + V_2 & -t & 0 \\ 0 & -t & 2t + V_3 & -t \\ 0 & 0 & -t & 2t + V_4 \end{pmatrix}, \qquad t = \frac{\hbar^2}{2mh^2}
$$

- Read it as a picture: the potential energy sits on the diagonal, one value per point, and the kinetic energy couples each point to its neighbors through $-t$. This is the same structure as the Hückel matrix that chemists use for $\pi$ electrons hopping between carbon atoms (Problem 7).

:::{important} **The Schrödinger equation on a grid**

$$
\hat{H}\psi = E\,\psi \quad\longrightarrow\quad H\mathbf{v} = E\,\mathbf{v}
$$

The allowed energies are the eigenvalues of the matrix $H$, and the stationary states are its eigenvectors: the wavefunctions sampled on the grid.

:::

:::{note} **Example: a particle in a box with three grid points**

Divide a box of length $L$ into four intervals, $h = L/4$. The wavefunction vanishes at the two walls, which leaves three interior points, $x = L/4$, $L/2$ and $3L/4$. With $V = 0$ inside,

$$
H = t\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}, \qquad t = \frac{\hbar^2}{2mh^2} = \frac{8\hbar^2}{mL^2}
$$

Write $E = \lambda t$ and set $\det(H - E\,I) = 0$. Expanding along the first row,

$$
(2-\lambda)\big[(2-\lambda)^2 - 1\big] - (2-\lambda) = (2-\lambda)\big[(2-\lambda)^2 - 2\big] = 0
\quad\Longrightarrow\quad \lambda = 2 - \sqrt{2},\ \ 2,\ \ 2 + \sqrt{2}
$$

The lowest level is $E_1 = (2 - \sqrt{2})\,t = 4.69\,\hbar^2/mL^2$, within 5 percent of the exact $\pi^2\hbar^2/2mL^2 = 4.93\,\hbar^2/mL^2$. Its eigenvector is

$$
\mathbf{v}_1 = \tfrac{1}{2}\big(1,\ \sqrt{2},\ 1\big) = \big(\sin\tfrac{\pi}{4},\ \sin\tfrac{\pi}{2},\ \sin\tfrac{3\pi}{4}\big)\big/\sqrt{2}
$$

the exact ground state sampled at the three points. Check it: $H\mathbf{v}_1 = \tfrac{t}{2}\big(2 - \sqrt{2},\ 2\sqrt{2} - 2,\ 2 - \sqrt{2}\big) = (2 - \sqrt{2})\,t\,\mathbf{v}_1$.

:::

```{code-cell} python
:tags: [hide-input]
# synced: box_grid_states
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
xs = np.linspace(0, 1, 300)                                 # hbar = m = L = 1
fig = plt.figure(figsize=(9.4, 4.0))
gs = fig.add_gridspec(3, 3, width_ratios=[1.15, 0.42, 1], hspace=0.25, wspace=0.12)
N, h = 3, 0.25
xg = np.array([0, 0.25, 0.5, 0.75, 1.0])
H = (2 * np.eye(N) - np.eye(N, k=1) - np.eye(N, k=-1)) / (2 * h**2)
Eg, V = np.linalg.eigh(H)
for r in range(3):
    ax = fig.add_subplot(gs[r, 0])
    n = r + 1
    v = V[:, r] / np.sqrt(h); v = v * np.sign(v[0])          # normalized as a function, first point positive
    ax.plot(xs, np.sqrt(2) * np.sin(n * np.pi * xs), color=GRAY, lw=1.8, alpha=0.7)
    ax.plot(xg, np.concatenate([[0], v, [0]]), "-o", color=CARDINAL, lw=1.6, ms=7)
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.plot([0, 0], [-1.6, 1.6], color="k", lw=2); ax.plot([1, 1], [-1.6, 1.6], color="k", lw=2)
    ax.set_xlim(-0.03, 1.03); ax.set_ylim(-1.75, 1.75); ax.axis("off")
    axt = fig.add_subplot(gs[r, 1]); axt.axis("off")
    axt.text(0.05, 0.5, rf"$n = {n}$: $E = {Eg[r]:.2f}$" + "\n" + rf"exact: ${(n * np.pi)**2 / 2:.2f}$", fontsize=11.5,
             va="center", transform=axt.transAxes)
    if r == 0:
        ax.set_title("3 grid points: eigenvectors (dots) vs exact states", loc="left", fontsize=12.5)
axl = fig.add_subplot(gs[:, 2])
cols = [(3, CARDINAL), (10, PURPLE), (30, TEAL)]
for k, (Ng, col) in enumerate(cols):
    hh = 1 / (Ng + 1)
    En = (1 - np.cos(np.arange(1, min(Ng, 4) + 1) * np.pi * hh)) / hh**2
    axl.hlines(En, k - 0.32, k + 0.32, color=col, lw=3)
Ex = (np.arange(1, 5) * np.pi)**2 / 2
axl.hlines(Ex, 3 - 0.32, 3 + 0.32, color="k", lw=3)
for e in Ex:
    axl.axhline(e, color=GRAY, lw=0.6, ls=":", zorder=0)
axl.set_xticks([0, 1, 2, 3]); axl.set_xticklabels([r"$N = 3$", r"$N = 10$", r"$N = 30$", "exact"], fontsize=12)
axl.yaxis.tick_right(); axl.yaxis.set_label_position("right")
axl.spines["left"].set_visible(False); axl.spines["right"].set_visible(True)
axl.set_ylabel(r"energy  ($\hbar^2/mL^2$)", fontsize=12); axl.tick_params(axis="y", labelsize=11)
axl.set_xlim(-0.6, 3.6); axl.set_ylim(0, 85)
axl.set_title("more points: closer to exact", loc="left", fontsize=12.5)
fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.09)
fig.subplots_adjust(right=0.93)
plt.show()
```

Fig. Left: the three eigenvectors of the three-point box (dots, joined by straight lines) on top of the exact box states (gray). Each is the exact sine sampled at the grid points. Right: the levels of grids with 3, 10 and 30 points against the exact ones, in units of $\hbar^2/mL^2$. More points give more levels, and each converges to the exact value from below. The top levels of a coarse grid are the least accurate, because their short wavelengths have few points per wavelength.

#### Five lines of numpy

- Here are $\hat{x}$, $\hat{p}$ and $\hat{H}$ for a particle on a spring on an 8-point grid, as color maps. At any size they keep the same pattern:

```{code-cell} python
:tags: [hide-input]
# synced: grid_operators
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
div = LinearSegmentedColormap.from_list("div", [TEAL, "white", CARDINAL])
N = 8                                                       # hbar = m = 1, V = x^2/2 on 8 points
x = np.linspace(-2, 2, N); h = x[1] - x[0]
up, dn = np.eye(N, k=1), np.eye(N, k=-1)
X = np.diag(x)
P = -1j * (up - dn) / (2 * h)                               # p = -i d/dx as a centered difference
H = -0.5 * (up - 2 * np.eye(N) + dn) / h**2 + np.diag(0.5 * x**2)
panels = [(X, r"$\hat{x}$", "grid positions on the diagonal\nreal, symmetric"),
          (P.imag, r"$\hat{p}$  (imaginary part)", r"$\mp i\hbar/2h$ next to the diagonal" + "\nimaginary, antisymmetric"),
          (H, r"$\hat{H}$", "$V$ on the diagonal, neighbors linked\nreal, symmetric")]
fig, axs = plt.subplots(1, 3, figsize=(9.6, 3.8))
for ax, (M, title, note) in zip(axs, panels):
    m = np.abs(M).max()
    ax.imshow(M, cmap=div, vmin=-m, vmax=m)
    ax.set_xticks(np.arange(-0.5, N, 1), minor=True); ax.set_yticks(np.arange(-0.5, N, 1), minor=True)
    ax.grid(which="minor", color="white", lw=1.5)
    ax.tick_params(which="both", length=0, labelbottom=False, labelleft=False)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_title(title, fontsize=14)
    ax.set_xlabel(note, fontsize=11.5, linespacing=1.4)
fig.suptitle(r"each matrix equals its conjugate transpose: $A^\dagger = A$", fontsize=13, y=0.98)
fig.subplots_adjust(left=0.02, right=0.98, top=0.83, bottom=0.17, wspace=0.18)
plt.show()
```

Fig. Position, momentum and energy of a particle on a spring, on a grid of 8 points. Color shows the sign and size of each entry (teal negative, red positive, white zero). Each matrix equals its own conjugate transpose, the defining property of the Hermitian matrices below; momentum manages it with an imaginary, antisymmetric pattern.

- With 400 points instead of 3, the eigenvalue problem is too big for a determinant by hand, and numpy solves it in one call. Here is the particle on a spring whose levels you hunted with the trial-energy slider in [The Schrödinger Equation](01-schrodinger-equation.md), in units with $\hbar = m = \omega = 1$:

```{code-cell} python
import numpy as np

N = 400                                       # grid points
x = np.linspace(-8, 8, N); h = x[1] - x[0]
D2 = (np.eye(N, k=1) - 2 * np.eye(N) + np.eye(N, k=-1)) / h**2    # second derivative
H = -0.5 * D2 + np.diag(0.5 * x**2)           # kinetic + potential energy

E, psi = np.linalg.eigh(H)                    # eigenvalues and eigenvectors of a Hermitian matrix
print(np.round(E[:5], 4))                     # exact: 0.5 1.5 2.5 3.5 4.5
```

- The levels come out $0.5, 1.5, 2.5, \dots$ in units of $\hbar\omega$, to three or four digits. This evenly spaced ladder is the vibrating bond of [Chapter 4](../ch04/02-quantum-harmonic-oscillator.md). The columns of `psi` are the wavefunctions.
- `eigh` is numpy's eigensolver for **Hermitian** matrices. Why the physics hands us only Hermitian matrices is the subject of the section on Hermitian operators below.

### Dirac notation

Integrals and matrices are two ways of writing the same objects. Dirac's notation writes them once:

- A state is a **ket** $\lvert\psi\rangle$. Its partner, the **bra** $\langle\psi\rvert$, carries the complex conjugate.
- A bra next to a ket is an **inner product**, a number: $\langle\phi\vert\psi\rangle = \int \phi^*\,\psi\,dx$.
- An operator acts on a ket, $\hat{A}\lvert\psi\rangle$. Sandwiched between a bra and a ket it gives the **matrix element** $\langle\phi\vert\hat{A}\vert\psi\rangle = \int\phi^*\,\hat{A}\psi\,dx$.

| | integral | Dirac | numpy on a grid |
| :-- | :-- | :-- | :-- |
| inner product | $\int \phi^*\psi\,dx$ | $\langle \phi \vert \psi \rangle$ | `np.vdot(phi, psi) * h` |
| normalization | $\int \lvert\psi\rvert^2 dx = 1$ | $\langle \psi \vert \psi \rangle = 1$ | `np.vdot(psi, psi) * h` |
| operator acts | $\hat{A}\psi(x)$ | $\hat{A}\lvert\psi\rangle$ | `A @ psi` |
| matrix element | $\int \phi^*\hat{A}\psi\,dx$ | $\langle \phi \vert \hat{A} \vert \psi \rangle$ | `np.vdot(phi, A @ psi) * h` |
| eigenvalue problem | $\hat{A}\phi_n = a_n\phi_n$ | $\hat{A}\lvert n\rangle = a_n\lvert n\rangle$ | `a, phi = np.linalg.eigh(A)` |

- `np.vdot` conjugates its first argument, which is exactly what the bra does. The factor `h` turns the sum over grid points into the integral.
- The table grows in the next two lectures: expansion coefficients in [Measurement](05-eigenvalues-and-expectation.md), time evolution in [Time Dependence](06-time-dependence.md).

### Hermitian operators

#### The adjoint

- For a complex number, the conjugate flips the sign of $i$: $(3 + 2i)^* = 3 - 2i$. For a matrix, the analog is the **adjoint** or conjugate transpose: swap rows and columns, then conjugate every entry, $(A^\dagger)_{jk} = A_{kj}^*$.
- For an operator, the adjoint is whatever you get by moving it from the ket to the bra of an inner product. An operator that can move across unchanged is **Hermitian**.

:::{important} **Adjoint and Hermitian operator**

$$
\langle \phi \vert \hat{A}\psi \rangle = \langle \hat{A}^\dagger\phi \vert \psi \rangle
$$

$\hat{A}$ is **Hermitian** (self-adjoint) when $\hat{A}^\dagger = \hat{A}$:

$$
\int \phi^*\,\big(\hat{A}\psi\big)\,dx = \int \big(\hat{A}\phi\big)^*\,\psi\,dx, \qquad \text{for a matrix: } A_{jk} = A_{kj}^*
$$

:::

- The three grid matrices above are Hermitian. Position and energy are real and symmetric. Momentum is imaginary and antisymmetric: transposing flips the sign of every entry and conjugating flips it back.

:::{note} **Example: which matrices are Hermitian?**

$$
A = \begin{pmatrix} 2 & 1-i \\ 1+i & 3 \end{pmatrix}, \quad
B = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad
C = \begin{pmatrix} i & 0 \\ 0 & 1 \end{pmatrix}, \quad
D = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}
$$

Compare each entry with the conjugate of its mirror image across the diagonal.

- $A$: $A_{12} = 1 - i$ and $A_{21}^* = (1+i)^* = 1 - i$, and the diagonal is real. **Hermitian.**
- $B$: $B_{12} = 2$ but $B_{21}^* = 3$. Not Hermitian.
- $C$: a diagonal entry is its own mirror image, so it must equal its own conjugate, but $i \neq -i$. A Hermitian matrix has a **real diagonal**. Not Hermitian.
- $D$: $D_{12} = -i$ and $D_{21}^* = i^* = -i$. **Hermitian**, although every off-diagonal entry is imaginary: the same pattern as $\hat{p}$ on the grid.

:::

#### Why observables must be Hermitian

A measurement needs three things from its operator, and Hermitian operators deliver all three.

1. **Real eigenvalues.** The eigenvalues are the values a measurement can return, and measured values are real numbers.
2. **Orthogonal eigenfunctions.** Eigenfunctions with different eigenvalues satisfy $\langle \phi_m \vert \phi_n \rangle = 0$: distinct outcomes are mutually exclusive.
3. **A complete basis.** Every state can be written as a sum of the eigenfunctions, so every state has a definite probability for each outcome. That is the subject of [Measurement](05-eigenvalues-and-expectation.md).

:::{important} **Eigenvalues and eigenfunctions of a Hermitian operator**

$$
\hat{A}\phi_n = a_n\phi_n \quad\Longrightarrow\quad a_n = a_n^*, \qquad \langle \phi_m \vert \phi_n \rangle = \delta_{mn}, \qquad \psi = \sum_n c_n\,\phi_n
$$

:::

:::{tip} **Proof: the eigenvalues are real**
:class: dropdown

Let $\hat{A}\phi = a\phi$ with $\phi$ normalized. Use the Hermitian property with both functions equal to $\phi$:

$$
\langle \phi \vert \hat{A}\phi \rangle = a\,\langle \phi \vert \phi \rangle = a, \qquad
\langle \hat{A}\phi \vert \phi \rangle = a^*\,\langle \phi \vert \phi \rangle = a^*
$$

The bra conjugates the constant it carries. Hermitian means the two are equal, so $a = a^*$.

:::

:::{tip} **Proof: eigenfunctions with different eigenvalues are orthogonal**
:class: dropdown

Let $\hat{A}\phi_m = a_m\phi_m$ and $\hat{A}\phi_n = a_n\phi_n$ with $a_m \neq a_n$. Both eigenvalues are real. Move $\hat{A}$ across the inner product:

$$
\langle \phi_m \vert \hat{A}\phi_n \rangle = a_n\,\langle \phi_m \vert \phi_n \rangle, \qquad
\langle \hat{A}\phi_m \vert \phi_n \rangle = a_m\,\langle \phi_m \vert \phi_n \rangle
$$

The two are equal, so $(a_n - a_m)\,\langle \phi_m \vert \phi_n \rangle = 0$, and since $a_n \neq a_m$ the overlap vanishes. When several eigenfunctions share one eigenvalue (degeneracy) the argument says nothing, but they can always be combined into orthogonal ones.

:::

- What goes wrong without Hermiticity? Take a Hermitian matrix and add a growing non-Hermitian part:

```{code-cell} python
:tags: [hide-input]
# synced: hermitian_dial
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
wt = LinearSegmentedColormap.from_list("wt", ["white", TEAL])
rng = np.random.default_rng(3)
N = 8
A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
Hm, K = (A + A.conj().T) / 2, (A - A.conj().T) / 2           # Hermitian part plus anti-Hermitian part
ss = np.concatenate([np.zeros(5), np.linspace(0, 1, 30), np.ones(6)])
vals, ovl = [], []
for s in ss:
    w, V = np.linalg.eig(Hm + s * K)
    o = np.argsort(w.real)
    V = V[:, o] / np.linalg.norm(V[:, o], axis=0)
    vals.append(w[o]); ovl.append(np.abs(V.conj().T @ V))
allv = np.concatenate(vals)
fig, (ax, axo) = plt.subplots(1, 2, figsize=(8, 3.6), gridspec_kw={"width_ratios": [1.55, 1], "wspace": 0.25})
ax.axhline(0, color=GRAY, lw=1.2)
ax.text(allv.real.max() + 0.2, 0.15, "real axis", color=GRAY, fontsize=11, ha="right", va="bottom")
scat = ax.scatter(vals[0].real, vals[0].imag, s=70, color=TEAL, zorder=5)
ax.set_xlim(allv.real.min() - 0.5, allv.real.max() + 0.5)
lim = 1.15 * max(0.5, np.abs(allv.imag).max())
ax.set_ylim(-lim, lim)
ax.set_xlabel("Re (eigenvalue)", fontsize=12); ax.set_ylabel("Im (eigenvalue)", fontsize=12)
img = axo.imshow(ovl[0], cmap=wt, vmin=0, vmax=1)
axo.set_xticks([]); axo.set_yticks([])
for sp in axo.spines.values():
    sp.set_visible(False)
axo.set_title(r"overlaps $|\langle v_j | v_k \rangle|$", fontsize=13)
fig.subplots_adjust(left=0.09, right=0.98, top=0.84, bottom=0.15)

def update(i):
    w, s = vals[i], ss[i]
    scat.set_offsets(np.column_stack([w.real, w.imag]))
    scat.set_color([TEAL if abs(v.imag) < 1e-6 else CARDINAL for v in w])
    img.set_data(ovl[i])
    off = (ovl[i] - np.diag(np.diag(ovl[i]))).max()
    ax.set_title(rf"$A = H + s\,K$,  $s = {s:.2f}$:  " + ("eigenvalues real" if s == 0 else f"largest |Im| = {np.abs(w.imag).max():.2f}"),
                 loc="left", fontsize=12.5)
    axo.set_xlabel("eigenvectors orthonormal" if s == 0 else f"largest overlap {off:.2f}", fontsize=12)

ani = FuncAnimation(fig, update, frames=len(ss), interval=110, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. A Hermitian matrix $H$ ($s = 0$) has real eigenvalues (left, all on the real axis) and orthonormal eigenvectors, so their overlaps (right) form the identity. Adding $s$ times a non-Hermitian part $K$, with $K^\dagger = -K$, pushes the eigenvalues into the complex plane, and the eigenvectors start to overlap. Neither could describe a measurement.

- Hermitian is more than "real eigenvalues". The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ has the real eigenvalues 1 and 2, but its eigenvectors overlap (Problem 4). Its outcomes would not be mutually exclusive, so it cannot represent an observable.

:::{note} **Example: is momentum Hermitian?**

Integrate by parts. The boundary term vanishes because physical wavefunctions go to zero at infinity, or at the walls of a box:

$$
\int_{-\infty}^{\infty}\phi^*\left(-i\hbar\frac{d\psi}{dx}\right)dx
= \Big[-i\hbar\,\phi^*\psi\Big]_{-\infty}^{\infty} + i\hbar\int_{-\infty}^{\infty}\frac{d\phi^*}{dx}\,\psi\,dx
= \int_{-\infty}^{\infty}\left(-i\hbar\frac{d\phi}{dx}\right)^{\!*}\psi\,dx
$$

The last step uses $\big(-i\hbar\,\phi'\big)^* = i\hbar\,\phi'^*$. So $\langle \phi \vert \hat{p}\psi \rangle = \langle \hat{p}\phi \vert \psi \rangle$: **momentum is Hermitian**.

Without the $i$ it fails. The same steps give $\int\phi^*\psi'\,dx = -\int(\phi')^*\psi\,dx$, so $d/dx$ is **anti-Hermitian**, $(d/dx)^\dagger = -d/dx$. The factor $-i$ turns the minus sign around, which is why momentum carries an $i$.

:::

The same check on the grid, where the derivative matrix is real and antisymmetric:

```{code-cell} python
import numpy as np

N = 400; x = np.linspace(-8, 8, N); h = x[1] - x[0]
D1 = (np.eye(N, k=1) - np.eye(N, k=-1)) / (2 * h)    # first derivative, centered difference
P = -1j * D1                                         # momentum, hbar = 1

print("d/dx is anti-Hermitian:", np.allclose(D1.conj().T, -D1))
print("p    is Hermitian:     ", np.allclose(P.conj().T, P))
```

### Commutators: the order of operations

- $\hat{A}\hat{B}\psi$ means: apply $\hat{B}$ first, then $\hat{A}$. For numbers the order never matters. For operators, as for matrices, it often does.

:::{important} **Commutator**

$$
\big[\hat{A},\hat{B}\big] = \hat{A}\hat{B} - \hat{B}\hat{A}
$$

If $\big[\hat{A},\hat{B}\big] = 0$ the operators **commute**, and the order does not matter.

:::

:::{note} **Example: $x$ and $d/dx$ do not commute**

Act on an arbitrary function $f$:

$$
x\,\frac{d}{dx}f = xf', \qquad \frac{d}{dx}\big(xf\big) = f + xf'
$$

$$
\left[x,\frac{d}{dx}\right]f = xf' - f - xf' = -f \qquad\Longrightarrow\qquad \left[x,\frac{d}{dx}\right] = -1
$$

The product rule leaves one extra term, and it does not depend on what $f$ is.

:::

- Multiply by $-i\hbar$ and the example becomes the most important commutator in quantum mechanics:

:::{important} **Canonical commutator**

$$
\big[\hat{x},\hat{p}\big] = i\hbar
$$

:::

```{code-cell} python
:tags: [hide-input]
# synced: order_matters
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(-4.5, 4.5, 900); h = x[1] - x[0]          # hbar = 1; psi real, so x p psi and p x psi are imaginary
funcs = [np.exp(-x**2 / 2) * (1 + 0.5 * x),
         np.exp(-x**2 / 5) * np.cos(2.2 * x) + 0.3 * np.exp(-(x - 1.5)**2)]
fig, axs = plt.subplots(1, 2, figsize=(9, 3.6))
for k, (ax, psi) in enumerate(zip(axs, funcs)):
    d = np.gradient(psi, h)
    xp, px = -x * d, -(psi + x * d)                         # (x p psi)/(i hbar) and (p x psi)/(i hbar)
    ax.plot(x, xp, color=TEAL, lw=2.2, label=r"$\hat{x}\hat{p}\,\psi\ /\ i\hbar$")
    ax.plot(x, px, color=ORANGE, lw=2.2, ls="--", label=r"$\hat{p}\hat{x}\,\psi\ /\ i\hbar$")
    ax.plot(x, xp - px, color=CARDINAL, lw=6, alpha=0.4, label=r"difference $/\ i\hbar$")
    ax.plot(x, psi, color="k", lw=1.4, ls=":", label=r"$\psi$ itself")
    ax.axhline(0, color=GRAY, lw=0.6)
    ax.set_xlim(-4.5, 4.5); ax.set_xlabel("x", fontsize=12); ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_title(("a lopsided bump" if k == 0 else "a wiggly packet"), loc="left", fontsize=12.5)
fig.legend(*axs[0].get_legend_handles_labels(), loc="upper center", ncol=4, frameon=False, fontsize=11.5,
           bbox_to_anchor=(0.5, 0.9), handlelength=2.2, columnspacing=1.6)
fig.suptitle(r"the difference of the two orders is $\psi$ itself:  $[\hat{x},\hat{p}]\,\psi = i\hbar\,\psi$", fontsize=13.5, y=0.99)
fig.subplots_adjust(left=0.02, right=0.99, top=0.72, bottom=0.14, wspace=0.08)
plt.show()
```

Fig. Two arbitrary functions acted on by $\hat{x}\hat{p}$ and by $\hat{p}\hat{x}$, both divided by $i\hbar$. The two orders give very different curves, but their difference lands exactly on $\psi$, whatever $\psi$ is: $[\hat{x},\hat{p}]\,\psi = i\hbar\,\psi$.

- The grid matrices pass the same test. Build $C = XP - PX$ and apply it to a smooth function:

```{code-cell} python
import numpy as np

N = 400; x = np.linspace(-8, 8, N); h = x[1] - x[0]
X = np.diag(x)
P = -1j * (np.eye(N, k=1) - np.eye(N, k=-1)) / (2 * h)      # hbar = 1
C = X @ P - P @ X

psi = np.exp(-x**2 / 2) * (1 + 0.3 * x)                     # any smooth function
print(f"largest |C psi - i psi|: {np.abs(C @ psi - 1j * psi)[5:-5].max():.1e}")
print("largest diagonal entry of C:", np.abs(np.diag(C)).max())
```

- $C\psi$ matches $i\psi$ to about $10^{-3}$, the accuracy of the grid, yet the diagonal of $C$ is zero. That is no accident:

:::{tip} **Why no finite matrices can obey $[X, P] = i\hbar$ exactly**
:class: dropdown

You might expect $C = XP - PX$ to be $i\hbar$ times the identity matrix. It cannot be. The trace of a product does not depend on the order, $\operatorname{tr}(XP) = \operatorname{tr}(PX)$, so $\operatorname{tr} C = 0$, while $\operatorname{tr}(i\hbar\,I) = i\hbar N$. No pair of $N \times N$ matrices satisfies the canonical commutator; only operators on infinitely many dimensions can.

On the grid, $C$ has zeros on its diagonal and $i\hbar/2$ just above and below it. Acting on a function, it averages the two neighbors of each point and multiplies by $i\hbar$. For a smooth function that average is the function itself, so $C\psi \approx i\hbar\psi$, and the error shrinks as the grid gets finer.

:::

#### Rules for commutators

- An operator commutes with itself and its powers: $[\hat{A},\hat{A}] = [\hat{A},\hat{A}^n] = 0$. So $[\hat{p},\hat{K}] = [\hat{p}, \hat{p}^2/2m] = 0$.
- Swapping the order flips the sign: $[\hat{A},\hat{B}] = -[\hat{B},\hat{A}]$, so $[\hat{p},\hat{x}] = -i\hbar$.
- Functions of $x$ commute with each other: $[\hat{x}, V(x)] = 0$.
- A product rule: $[\hat{A},\hat{B}\hat{C}] = [\hat{A},\hat{B}]\,\hat{C} + \hat{B}\,[\hat{A},\hat{C}]$ (Problem 5).

### Commuting operators share eigenfunctions

:::{important} **Commuting operators share eigenfunctions**

If $\big[\hat{A},\hat{B}\big] = 0$, there is a set of functions that are eigenfunctions of both:

$$
\hat{A}\phi_n = a_n\,\phi_n, \qquad \hat{B}\phi_n = b_n\,\phi_n
$$

:::

- **Why, in three lines.** Let $\hat{A}\phi = a\phi$, and suppose no other eigenfunction of $\hat{A}$ has the eigenvalue $a$. Because the operators commute,

$$
\hat{A}\big(\hat{B}\phi\big) = \hat{B}\big(\hat{A}\phi\big) = a\,\big(\hat{B}\phi\big)
$$

so $\hat{B}\phi$ is also an eigenfunction of $\hat{A}$ with eigenvalue $a$. The only such function is $\phi$ itself, up to a constant, so $\hat{B}\phi = b\,\phi$.
- If several eigenfunctions share an eigenvalue (degeneracy), $\hat{B}$ can mix them, and the shared eigenfunctions are particular combinations, as in the example below.

:::{tip} **The converse: shared eigenfunctions mean the operators commute**
:class: dropdown

Suppose $\hat{A}$ and $\hat{B}$ share a complete set of eigenfunctions, $\hat{A}\phi_n = a_n\phi_n$ and $\hat{B}\phi_n = b_n\phi_n$. Expand an arbitrary function in that set, $\psi = \sum_n c_n\phi_n$, and use linearity:

$$
\hat{A}\hat{B}\,\psi = \sum_n c_n\,\hat{A}\big(b_n\phi_n\big) = \sum_n c_n\,a_nb_n\,\phi_n, \qquad
\hat{B}\hat{A}\,\psi = \sum_n c_n\,\hat{B}\big(a_n\phi_n\big) = \sum_n c_n\,b_na_n\,\phi_n
$$

The numbers $a_nb_n$ and $b_na_n$ are equal, so $\hat{A}\hat{B}\psi = \hat{B}\hat{A}\psi$ for every $\psi$: the operators commute. The argument needs the set to be complete, because the commutator must vanish on every function, not just on a few.

:::

:::{note} **Example: the free particle**

With $V = 0$, $\hat{H} = \hat{p}^2/2m$ commutes with $\hat{p}$. The plane wave $e^{ikx}$ is an eigenfunction of both:

$$
\hat{p}\,e^{ikx} = \hbar k\,e^{ikx}, \qquad \hat{H}\,e^{ikx} = \frac{\hbar^2k^2}{2m}\,e^{ikx}
$$

The function $\sin kx$ is an eigenfunction of $\hat{H}$ with the same energy but not of $\hat{p}$ (Problem 4 of [The Schrödinger Equation](01-schrodinger-equation.md)). There is no contradiction: $e^{ikx}$ and $e^{-ikx}$ have the same energy, so any mix of them, $\sin kx$ included, is an eigenfunction of $\hat{H}$. The theorem promises that shared eigenfunctions exist, here the two plane waves, not that every eigenfunction of $\hat{H}$ is one of them.

:::

- Commuting observables can have **sharp values at the same time**: a state of definite momentum also has a definite kinetic energy. Position and momentum do not commute, and no state has sharp values of both. [Measurement](05-eigenvalues-and-expectation.md) turns this into the uncertainty principle.
- The labels of chemistry are shared eigenvalues. The quantum numbers $n$, $l$, $m$ of a hydrogen orbital label simultaneous eigenfunctions of three commuting operators, $\hat{H}$, $\hat{L}^2$ and $\hat{L}_z$ ([Chapter 5](../ch05/01-hydrogenlike-atoms.md)).

### Problems

#### Problem 1: Linear or not?

Decide which of these operators are linear: (a) $\hat{A}f = f + x$, (b) $\hat{B}f = x^2\,\dfrac{d^2f}{dx^2}$, (c) $\hat{C}f = \displaystyle\int_0^x f(y)\,dy$, (d) $\hat{D}f = e^{f}$.

:::{admonition} **Solution**
:class: dropdown solution

- (a) **Not linear.** $\hat{A}(2f) = 2f + x$, but $2\hat{A}f = 2f + 2x$. Adding something that does not depend on $f$ always breaks linearity.
- (b) **Linear.** The second derivative of a sum is the sum of the second derivatives, and multiplying by $x^2$ keeps constants and sums intact.
- (c) **Linear.** The integral of $c_1f_1 + c_2f_2$ is $c_1\int f_1 + c_2\int f_2$.
- (d) **Not linear.** $e^{f_1 + f_2} = e^{f_1}e^{f_2}$, a product rather than a sum.

:::

#### Problem 2: The parity operator

The parity operator reflects a function through the origin, $\hat{\Pi}f(x) = f(-x)$. Show that $\hat{\Pi}$ is Hermitian, and find its eigenvalues and eigenfunctions. Which states of the finite square well of [Tunneling and the Finite Square Well](03-tunneling-and-finite-square-well.md) are eigenfunctions of $\hat{\Pi}$?

:::{admonition} **Solution**
:class: dropdown solution

**Hermitian.** Substitute $y = -x$, which maps the interval $(-\infty, \infty)$ onto itself:

$$
\int_{-\infty}^{\infty}\phi^*(x)\,\psi(-x)\,dx = \int_{-\infty}^{\infty}\phi^*(-y)\,\psi(y)\,dy = \int_{-\infty}^{\infty}\big(\hat{\Pi}\phi\big)^*\,\psi\,dy
$$

**Eigenvalues.** Reflecting twice gives back the function, $\hat{\Pi}^2 f = f$. If $\hat{\Pi}f = \lambda f$ then $\hat{\Pi}^2f = \lambda^2 f = f$, so $\lambda^2 = 1$ and $\lambda = \pm 1$, real as promised. The eigenfunctions with $\lambda = +1$ are the **even** functions, $f(-x) = f(x)$, and those with $\lambda = -1$ the **odd** ones.

**The well.** The bound states of the finite well came out even (cosines inside) or odd (sines inside), so each is an eigenfunction of $\hat{\Pi}$. That is the shared-eigenfunction theorem at work: when $V(-x) = V(x)$, $\hat{\Pi}$ commutes with $\hat{H}$, and the stationary states can be chosen to have definite parity.

:::

#### Problem 3: Momentum on a four-point grid

Build the $4\times4$ momentum matrix on a periodic grid of four points with spacing $h$, using the centered difference and $\hbar = 1$ (on a periodic grid the neighbors of point 1 are points 4 and 2). Show that it is Hermitian and find its eigenvalues.

:::{admonition} **Solution**
:class: dropdown solution

Row $j$ of the derivative matrix holds $+1/2h$ for the right neighbor and $-1/2h$ for the left one, wrapping around at the ends. Multiplying by $-i$:

$$
P = \frac{-i}{2h}\begin{pmatrix} 0 & 1 & 0 & -1 \\ -1 & 0 & 1 & 0 \\ 0 & -1 & 0 & 1 \\ 1 & 0 & -1 & 0 \end{pmatrix}
$$

The real matrix in parentheses is antisymmetric ($d/dx$ is anti-Hermitian). For $P$, compare $P_{12} = -i/2h$ with $P_{21}^* = (+i/2h)^* = -i/2h$: equal, and likewise for every pair, with zeros on the diagonal. $P$ is **Hermitian**.

```python
import numpy as np
h = 1.0
M = np.array([[0, 1, 0, -1], [-1, 0, 1, 0], [0, -1, 0, 1], [1, 0, -1, 0]])
P = -1j * M / (2 * h)
print(np.allclose(P, P.conj().T))           # True
print(np.round(np.linalg.eigvalsh(P), 6))   # [-1.  0.  0.  1.]
```

The eigenvalues $-1/h, 0, 0, +1/h$ are real, and the eigenvectors are discrete plane waves $e^{ikx_j}$: the grid version of the momentum eigenfunctions.

:::

#### Problem 4: Real eigenvalues are not enough

Find the eigenvalues and normalized eigenvectors of $M = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ and the overlap between the eigenvectors. Could $M$ represent an observable?

:::{admonition} **Solution**
:class: dropdown solution

$M$ is triangular, so its eigenvalues are the diagonal entries, $1$ and $2$: both real. The eigenvectors are

$$
\lambda = 1:\ \mathbf{v}_1 = \begin{pmatrix}1\\0\end{pmatrix}, \qquad \lambda = 2:\ \mathbf{v}_2 = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}, \qquad \langle \mathbf{v}_1 \vert \mathbf{v}_2 \rangle = \frac{1}{\sqrt{2}} \neq 0
$$

$M$ is not Hermitian ($M_{12} = 1$ but $M_{21} = 0$), and the price is overlapping eigenvectors. A system in state $\mathbf{v}_2$ would have a nonzero overlap with the outcome "1", although it is supposed to give "2" with certainty. The outcomes are not mutually exclusive, so $M$ cannot represent an observable.

:::

#### Problem 5: Commutator algebra

Prove the product rule $[\hat{A},\hat{B}\hat{C}] = [\hat{A},\hat{B}]\,\hat{C} + \hat{B}\,[\hat{A},\hat{C}]$ by expanding both sides. Use it, with $[\hat{x},\hat{p}] = i\hbar$, to find $[\hat{x},\hat{p}^3]$ and $[\hat{x}^2,\hat{p}]$.

#### Problem 6: Momentum and force

Show that $[\hat{p}, V(x)] = -i\hbar\,\dfrac{dV}{dx}$ by acting on a test function. Evaluate it for a particle on a spring, $V = \tfrac{1}{2}kx^2$, and for a uniform field, $V = mgx$. For which potentials does $\hat{p}$ commute with $\hat{H}$?

#### Problem 7: Butadiene as a matrix

In Hückel theory ([Chapter 8](../ch08/05-huckel-theory.md)) the $\pi$ electrons of butadiene are described by the matrix

$$
H = \begin{pmatrix} \alpha & \beta & 0 & 0 \\ \beta & \alpha & \beta & 0 \\ 0 & \beta & \alpha & \beta \\ 0 & 0 & \beta & \alpha \end{pmatrix}
$$

where $\alpha$ is the energy of an electron on one carbon and $\beta < 0$ couples neighbors. Set $\alpha = 0$, $\beta = -1$ and use `np.linalg.eigh` to find the eigenvalues and eigenvectors. Check that the eigenvalues are real (you should find $\pm 1.618$ and $\pm 0.618$) and that the eigenvectors are orthonormal. Draw each eigenvector as four bars, one per carbon, and count the sign changes. Compare with the particle-in-a-box states of butadiene in [Particle in a Box](02-particle-in-a-box.md).

#### Problem 8: Building a shared eigenfunction

For a free particle, show that $\cos kx$ is an eigenfunction of $\hat{H}$ but not of $\hat{p}$. Which combinations $a\cos kx + b\sin kx$ are eigenfunctions of both, and what are their momenta?
