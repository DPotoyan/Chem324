---
kernelspec:
  name: python3
  display_name: Python 3
---

# Operators as Matrices

:::{note} **What you will learn**

- **Functions are vectors and operators are matrices.** This is the central structural fact of quantum mechanics: under the calculus, it is all linear algebra. Wavefunctions are vectors, operators are matrices, and $\hat H\psi = E\psi$ is an eigenvalue problem.
- **The grid and the stencil.** Sampling a function on a grid turns a derivative into a banded matrix. We visualize this in 1D, then in 2D where the Laplacian becomes a sparse matrix.
- **Matrices are linear operators.** Acting with a matrix and acting with an operator are the same kind of thing, and operator order matters.
- **The two special matrices of quantum mechanics.** Hermitian matrices have real eigenvalues and orthogonal eigenvectors; unitary matrices preserve length. These are exactly the matrices that represent observables and time evolution.
:::

Under the calculus of quantum mechanics lies a simpler and more powerful truth: **it is all linear algebra**. Wavefunctions are vectors, operators are matrices, and the Schrodinger equation is the eigenvalue problem $A\mathbf{v} = \lambda\mathbf{v}$ in disguise. This appendix makes that correspondence concrete and visual. It does not re-derive the differential equations of the course: separation of variables, the wave equation, and their oscillating and decaying solutions are developed in detail in [Chapter 2 on waves](../ch02/02-the-wave-equation.md). Here we stay on the linear-algebra side and show how operators become matrices you can build, picture, and diagonalize.

## Functions are vectors, operators are matrices

### A function is a vector with one component per point

Take any function and evaluate it at $N$ points $x = (x_1, x_2, \ldots, x_N)$. The list of values is a vector with $N$ components. For example $f(x) = x^2$ sampled at $x = (0,1,2,3,4)$ becomes the vector $(0,1,4,9,16)$.

Now let the grid get finer, $N\to\infty$ with spacing $h\to 0$. The vector gains a component for **every** point $x$, and in that limit the function *is* an infinite-dimensional vector. The value $\psi(x)$ plays the role of "the component at $x$," exactly as $v_i$ is the component of $\mathbf{v}$ along basis direction $i$. The left panel below shows a smooth function and the vector of samples that stands in for it on a grid.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))

# Panel a: sampling a function on a grid
xf = np.linspace(0, 2 * np.pi, 300)
xg = np.linspace(0, 2 * np.pi, 13)
axes[0].plot(xf, np.sin(xf), 'k', lw=1.5, label=r'$f(x)=\sin x$')
axes[0].vlines(xg, 0, np.sin(xg), color='#d1495b', lw=0.8)
axes[0].plot(xg, np.sin(xg), 'o', color='#d1495b', ms=6, label='samples = vector components')
axes[0].axhline(0, color='gray', lw=0.6)
axes[0].set_xlabel('x')
axes[0].legend(fontsize=8, loc='upper right')
axes[0].set_title('Fig.1a A function becomes a vector of samples')

# Panel b: the three-point second-derivative stencil
pts = np.arange(7)
axes[1].plot(pts, np.zeros_like(pts), 'o', color='0.8', ms=13)
for p, w, c in [(2, '+1', '#d1495b'), (3, '-2', '#2e4057'), (4, '+1', '#d1495b')]:
    axes[1].plot(p, 0, 'o', color=c, ms=15)
    axes[1].text(p, 0.18, w, ha='center', color=c, fontsize=12, fontweight='bold')
axes[1].annotate('point j', xy=(3, 0), xytext=(3, -0.35), ha='center',
                 color='#2e4057', fontsize=10)
axes[1].set_ylim(-0.6, 0.6)
axes[1].set_xlim(-0.5, 6.5)
axes[1].axis('off')
axes[1].set_title(r'Fig.1b The stencil $(1,-2,1)$ for $d^2/dx^2$ at point j')

plt.tight_layout()
plt.show()
```

### The inner product becomes an integral

This is the link that makes the analogy precise. The dot product of two vectors sums the products of matching components. For function-vectors, that sum over grid points, weighted by the spacing $h$, is a Riemann sum, and in the fine-grid limit it becomes an **integral**:

$$
\langle f \mid g \rangle = \sum_i f^*(x_i)\,g(x_i)\,h
\;\xrightarrow[h\to 0]{}\;
\int f^*(x)\,g(x)\,dx.
$$

So the quantum-mechanical inner product $\langle\psi\mid\phi\rangle = \int\psi^*\phi\,dx$ is nothing more than the dot product from the [previous page](03-vectors-and-linear-algebra.md), carried to infinite dimensions. Everything built on the dot product carries over verbatim: **normalization** $\int|\psi|^2\,dx = 1$ is just $|\psi| = 1$, and **orthogonal wavefunctions** ($\int\psi_m^*\psi_n\,dx = 0$) are just perpendicular vectors.

### An operator is a matrix

A **linear operator** takes a function and returns a function, that is, it takes a vector and returns a vector. Any linear map on vectors is a matrix, so every quantum operator is a matrix acting on the function-vector. This gives the full dictionary between the linear algebra you already know and the quantum mechanics ahead:

| Linear algebra (finite dimensions) | Quantum mechanics (functions) |
|---|---|
| vector $\mathbf{v}$ | wavefunction $\psi(x)$ |
| component $v_i$ | value $\psi(x)$ |
| dot product $\langle \mathbf{a}\mid\mathbf{b}\rangle = \sum_i a_i^* b_i$ | inner product $\langle\psi\mid\phi\rangle = \int\psi^*\phi\,dx$ |
| normalized $\lvert\mathbf{v}\rvert = 1$ | normalized $\int\lvert\psi\rvert^2 dx = 1$ |
| orthonormal basis $\mathbf{e}_i$ | orthonormal functions $\phi_n(x)$ |
| matrix $A$ | operator $\hat A$ (such as $\hat x$, $\hat p$, $\hat H$) |
| eigenvector equation $A\mathbf{v} = \lambda\mathbf{v}$ | eigenfunction equation $\hat A\psi = a\psi$ |
| eigenvalue $\lambda$ | measured value $a$ (energy, momentum) |
| Hermitian matrix | Hermitian operator (real eigenvalues) |
| unitary matrix | time evolution, symmetry operations |
| expansion $\mathbf{v} = \sum_i c_i\mathbf{e}_i$ | superposition $\psi = \sum_n c_n\phi_n$ |

:::{important} **The one idea to carry through the whole course**

Under the hood, quantum mechanics is linear algebra in an infinite-dimensional space. A wavefunction is a vector, an operator is a matrix, and the time-independent Schrodinger equation $\hat H\psi = E\psi$ is the eigenvalue problem $A\mathbf{v} = \lambda\mathbf{v}$. The allowed energies are eigenvalues and the stationary states are eigenvectors. The calculus is simply how we do this linear algebra in the **position basis**; the eigenvalue structure is what is really going on.
:::

## The derivative as a matrix: the stencil

The recipe for turning a derivative into a matrix is the **stencil**: a small pattern of weights applied to each grid point and its neighbors. The first derivative uses a **centered difference**, the slope between the neighbor on the left and the neighbor on the right:

$$
\frac{d\psi}{dx}\bigg|_{x_i} \approx \frac{\psi(x_{i+1}) - \psi(x_{i-1})}{2h}.
$$

Written as a matrix acting on the sampled vector (with one-sided formulas at the two boundaries), this is

$$
D_1 = \frac{1}{2h}
\begin{pmatrix}
-3 & 4 & -1 & 0 & 0 \\
-1 & 0 & 1 & 0 & 0 \\
0 & -1 & 0 & 1 & 0 \\
0 & 0 & -1 & 0 & 1 \\
0 & 0 & 1 & -4 & 3
\end{pmatrix}.
$$

```{code-cell} python
import numpy as np

n = 5
x = np.linspace(0, 4, n)
h = x[1] - x[0]
psi = x**2

D1 = (1 / (2 * h)) * np.array([
    [-3, 4, -1, 0, 0],
    [-1, 0, 1, 0, 0],
    [0, -1, 0, 1, 0],
    [0, 0, -1, 0, 1],
    [0, 0, 1, -4, 3],
])

print("finite-difference derivative of x^2:", D1 @ psi)
print("exact derivative 2x               :", 2 * x)
```

The **second derivative** uses the three-point stencil $\psi_{i+1} - 2\psi_i + \psi_{i-1}$ over $h^2$, the $(1,-2,1)$ pattern sketched in Fig.1b. Because each point couples only to its two neighbors, the matrix is **banded** (tridiagonal): almost all entries are zero. The left panel below shows that sparsity pattern; the right panel confirms the matrix works by turning $\sin x$ into $-\sin x$, since $\frac{d^2}{dx^2}\sin x = -\sin x$.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

N = 200
x = np.linspace(0, 2 * np.pi, N)
h = x[1] - x[0]

# Second-derivative matrix, tridiagonal (1, -2, 1) / h^2
D2 = (np.diag(np.ones(N - 1), 1)
      - 2 * np.diag(np.ones(N))
      + np.diag(np.ones(N - 1), -1)) / h**2

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))

# Panel a: sparsity pattern of a small D2 (banded / tridiagonal)
small = (np.diag(np.ones(11), 1) - 2 * np.diag(np.ones(12)) + np.diag(np.ones(11), -1))
axes[0].spy(small, markersize=8, color='#2e4057')
axes[0].set_title('Fig.2a $D_2$ is banded: each point couples to neighbors')
axes[0].set_xlabel('column'); axes[0].set_ylabel('row')

# Panel b: apply D2 to sin x
psi = np.sin(x)
d2psi = D2 @ psi
axes[1].plot(x, psi, 'k', lw=2, label=r'$\psi = \sin x$')
axes[1].plot(x[1:-1], d2psi[1:-1], color='#d1495b', lw=2, label=r'$D_2\,\psi$')
axes[1].plot(x, -np.sin(x), '--', color='#66a182', lw=2, label=r'$-\sin x$ (exact)')
axes[1].axhline(0, color='gray', lw=0.6)
axes[1].set_xlabel('x')
axes[1].legend(fontsize=9, loc='upper right')
axes[1].set_title('Fig.2b The matrix turns sin x into -sin x')

plt.tight_layout()
plt.show()
```

Diagonalizing this second-derivative matrix (plus a potential on the diagonal) is exactly how a computer finds energies and wavefunctions. That is the whole idea behind the [numerical Schrodinger solver](../demos/07-demo-numerical-schrodinger.md).

## From 1D to 2D grids

Nothing about the stencil idea is special to one dimension. On a 2D grid, the natural second-derivative operator is the **Laplacian** $\nabla^2 = \partial_x^2 + \partial_y^2$, whose continuous meaning is explored in [div, grad, curl](05-div-grad-curl.md). Discretized, it becomes the **five-point stencil**: the center point with weight $-4$ and its four nearest neighbors with weight $+1$.

To store a 2D grid of values as a single vector, we flatten it row by row. The Laplacian is then still a matrix, now with a **block-banded** sparsity pattern: the horizontal neighbors sit on the near diagonals, and the vertical neighbors appear as off-diagonal blocks one grid-row away.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

# Panel a: 2D grid with the five-point stencil highlighted
m = 5
for i in range(m):
    for j in range(m):
        axes[0].plot(i, j, 'o', color='0.82', ms=13)
cx, cy = 2, 2
for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    axes[0].annotate('', xy=(cx + dx, cy + dy), xytext=(cx, cy),
                     arrowprops=dict(arrowstyle='->', color='#d1495b', lw=1.5))
    axes[0].plot(cx + dx, cy + dy, 'o', color='#d1495b', ms=15)
    axes[0].text(cx + dx, cy + dy + 0.22, '+1', ha='center', color='#d1495b', fontsize=10)
axes[0].plot(cx, cy, 'o', color='#2e4057', ms=17)
axes[0].text(cx, cy + 0.24, '-4', ha='center', color='white', fontsize=9, fontweight='bold')
axes[0].set_xlim(-0.6, 4.6); axes[0].set_ylim(-0.6, 4.6)
axes[0].set_aspect('equal'); axes[0].axis('off')
axes[0].set_title('Fig.3a The five-point Laplacian stencil')

# Panel b: sparsity of the 2D Laplacian, built by a Kronecker sum
n = 6
lap1d = -2 * np.eye(n) + np.eye(n, k=1) + np.eye(n, k=-1)
eye = np.eye(n)
lap2d = np.kron(lap1d, eye) + np.kron(eye, lap1d)   # (n^2) x (n^2)
axes[1].spy(lap2d, markersize=4, color='#2e4057')
axes[1].set_title(f'Fig.3b 2D Laplacian on a {n}x{n} grid ({n*n}x{n*n} matrix)')
axes[1].set_xlabel('column'); axes[1].set_ylabel('row')

plt.tight_layout()
plt.show()
```

The `np.kron` (Kronecker product) construction is the standard way to assemble multidimensional operators from 1D pieces: $\nabla^2 = D_2 \otimes I + I \otimes D_2$. The same trick builds 3D operators for real atoms and molecules. The matrix grows fast ($N^2 \times N^2$ for an $N\times N$ grid), but it stays overwhelmingly sparse, which is what makes large quantum calculations feasible.

## Matrices are linear operators

Acting with a matrix is a **linear** operation: it respects sums and scalar multiples,

$$
A(\alpha\mathbf{u} + \beta\mathbf{v}) = \alpha A\mathbf{u} + \beta A\mathbf{v}.
$$

This is the same linearity that defines a quantum operator, which is why a matrix and an operator are the same kind of object. One consequence is immediate and important: **order matters**. Matrices generally do not commute, $AB \neq BA$.

```{code-cell} python
import numpy as np

A = np.array([[1, 2], [0, 1]])   # a shear
B = np.array([[0, 1], [1, 0]])   # a swap

print("AB =\n", A @ B)
print("BA =\n", B @ A)
print("\ncommutator AB - BA =\n", A @ B - B @ A)
```

Applying a shear then a swap is not the same as a swap then a shear. In quantum mechanics this non-commutation, packaged as the **commutator** $[\hat A, \hat B] = \hat A\hat B - \hat B\hat A$, is exactly what forbids simultaneous sharp values of position and momentum. It is the algebra behind the uncertainty principle.

## The two special matrices of quantum mechanics

Out of all matrices, quantum mechanics leans on just two families, distinguished by how they relate to their **conjugate transpose** $A^\dagger = (A^*)^{\mathsf T}$ (transpose, then complex-conjugate each entry).

### Hermitian matrices: real eigenvalues

:::{important} **Hermitian (self-adjoint) matrix**

$$
A^\dagger = A.
$$

For real matrices this is just **symmetric**, $A^{\mathsf T} = A$. Hermitian matrices have two properties that quantum mechanics depends on:

- all eigenvalues are **real**,
- eigenvectors for different eigenvalues are **orthogonal**.
:::

Because measured values are real, every observable (energy, position, momentum) is represented by a Hermitian operator. The reality of the eigenvalues is what guarantees a measurement returns a real number, and the orthogonality of eigenvectors is why distinct energy levels give orthogonal stationary states.

```{code-cell} python
import numpy as np

# A Hermitian matrix: A^dagger = A (note the i and -i off the diagonal)
A = np.array([[2.0, 1.0 - 1j],
              [1.0 + 1j, 3.0]])
print("Hermitian? A == A^dagger:", np.allclose(A, A.conj().T))

vals, vecs = np.linalg.eigh(A)
print("eigenvalues (all real):", vals)
# eigenvectors orthonormal: V^dagger V = I
print("eigenvectors orthonormal:", np.allclose(vecs.conj().T @ vecs, np.eye(2)))
```

### Unitary matrices: they preserve length

:::{important} **Unitary matrix**

$$
U^\dagger U = U U^\dagger = I, \qquad\text{so}\qquad U^{-1} = U^\dagger.
$$

A unitary matrix **preserves inner products and norms**: $\langle U\mathbf{x}\mid U\mathbf{y}\rangle = \langle\mathbf{x}\mid\mathbf{y}\rangle$. Its eigenvalues all have magnitude one, so they lie on the **unit circle** in the complex plane. For real matrices, unitary means **orthogonal**, a rotation or reflection.
:::

Because probability is the squared norm of the wavefunction, anything that must conserve probability is unitary: time evolution $e^{-i\hat H t/\hbar}$ and symmetry operations are all unitary. They rotate the state vector without changing its length.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

theta = 0.7
U = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])   # a rotation: real unitary

v = np.array([3.0, 4.0])
print("U preserves length:", np.linalg.norm(U @ v), "vs", np.linalg.norm(v))
print("U^dagger U = I:", np.allclose(U.conj().T @ U, np.eye(2)))

# Eigenvalues lie on the unit circle
eigvals = np.linalg.eigvals(U)
fig, ax = plt.subplots(figsize=(4.2, 4.2))
circle = np.exp(1j * np.linspace(0, 2 * np.pi, 200))
ax.plot(circle.real, circle.imag, 'k', lw=1)
ax.plot(eigvals.real, eigvals.imag, 'o', color='#d1495b', ms=10)
ax.axhline(0, color='gray', lw=0.5); ax.axvline(0, color='gray', lw=0.5)
ax.set_aspect('equal')
ax.set_xlabel('real'); ax.set_ylabel('imaginary')
ax.set_title('Fig.4 Unitary eigenvalues sit on the unit circle')
plt.tight_layout()
plt.show()
```

Hermitian and unitary matrices are two sides of one coin: if $\hat H$ is Hermitian, then $e^{-i\hat H t/\hbar}$ is unitary. Real observables generate probability-conserving evolution. That single sentence is the linear-algebra backbone of the whole theory.

## Problems

### Problem 1: Read off a derivative matrix

Using the first-derivative matrix $D_1$ above with $h=1$, apply it to the constant vector $\psi = (5,5,5,5,5)$. What do you expect, and why?

:::{admonition} **Solution**
:class: dropdown solution

Each interior row computes a difference of equal neighbors, so the derivative is $0$ everywhere. The derivative of a constant is zero, and the boundary rows are built to return zero for a constant as well.
:::

### Problem 2: Build a second-derivative matrix

Modify the code to build $D_2$ on a grid of $N = 100$ points over $[0, \pi]$, apply it to $\cos x$, and check that you recover $-\cos x$.

### Problem 3: A commutator

Compute the commutator $[A, B] = AB - BA$ for $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

:::{admonition} **Solution**
:class: dropdown solution

$AB = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$ and $BA = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, so

$$
[A, B] = \begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix} \neq 0.
$$

These operators do not commute.
:::

### Problem 4: Is it Hermitian?

Decide whether $A = \begin{pmatrix} 1 & 2i \\ -2i & 3 \end{pmatrix}$ is Hermitian, and predict whether its eigenvalues are real.

:::{admonition} **Solution**
:class: dropdown solution

The conjugate transpose swaps the off-diagonal entries and conjugates them: $(2i)^* = -2i$ moves to the lower-left, which already holds $-2i$. So $A^\dagger = A$: the matrix is Hermitian, and its eigenvalues must be real.
:::

### Problem 5: Unitary preserves length

Verify by hand that the rotation matrix $U = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ satisfies $U^{\mathsf T}U = I$, so it preserves the norm of any vector.

### Problem 6: Sparsity counting

An $N\times N$ 2D grid gives a Laplacian matrix of size $N^2 \times N^2$. Using the five-point stencil, roughly how many nonzero entries does each row have, and why does the matrix stay sparse as $N$ grows?

:::{admonition} **Solution**
:class: dropdown solution

Each grid point couples to itself and its four neighbors, so every row has about **five** nonzero entries regardless of $N$. The matrix has $N^2$ rows but only about $5N^2$ nonzeros out of $N^4$ possible, so the fraction filled, about $5/N^2$, shrinks as the grid grows. This sparsity is what makes large numerical quantum calculations possible.
:::

### Problem 7: Hermitian generates unitary

Explain in one or two sentences why, if $\hat H$ is Hermitian, the time-evolution operator $e^{-i\hat H t/\hbar}$ is unitary and therefore conserves probability.
