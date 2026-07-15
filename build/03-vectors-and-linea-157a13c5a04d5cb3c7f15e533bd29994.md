---
kernelspec:
  name: python3
  display_name: Python 3
---

# Vectors and Linear Algebra

:::{note} **What you will learn**

- **Vectors as arrays of numbers.** A vector is an ordered list of components that describes the state of a system, and any vector is a linear combination of basis vectors.
- **Inner products, norms, and orthogonality.** The dot product measures shared direction; orthonormal vectors are normalized and mutually perpendicular.
- **Linear systems as matrix equations.** A system $A\mathbf{x} = \mathbf{b}$ is solved compactly by matrix inversion.
- **Eigenvalues and eigenvectors.** Special vectors that a matrix only rescales. In quantum mechanics eigenvalues are the measurable observables and eigenvectors the states with definite outcomes.
- **The geometric action of matrices.** Matrices stretch, rotate, shear, and scale vectors, and each effect can be pictured.
:::

Linear algebra is the backbone of quantum mechanics. States are vectors, observables are matrices, and measurement outcomes are eigenvalues. Everything that follows in the course is, at bottom, an eigenvalue problem in a vector space. This page builds that vocabulary from the 2D picture up.

## Vectors

### What is a vector?

A **vector** is an ordered collection of numbers describing the state or configuration of a system:

- $a = (-2, 8)$, a 2D vector,
- $e_1 = (1, 0)$ and $e_2 = (0, 1)$, unit vectors along the axes,
- $b = (1.34, 4.23, 5.98)$, a 3D vector,
- $c = (1, -2, 4i, 3 + 2i)$, a 4D vector with complex components,
- $f = (1, 2, 3, 4, 5, \ldots)$, an infinite-dimensional vector (a sequence).

Vectors may live in **real** or **complex** vector spaces depending on their components. In quantum mechanics the components are generally complex.

:::{tip} **Vectors as linear combinations of a basis**

Any vector in an $N$-dimensional space can be written as a linear combination of $N$ linearly independent **basis vectors**. In 2D, the perpendicular unit vectors $e_1$ and $e_2$ form a convenient basis:

$$
\vec{a} = a_1 e_1 + a_2 e_2 = \begin{pmatrix} a_1 \\ a_2 \end{pmatrix}.
$$

Choosing a rotated basis changes the *components*, but the vector itself is the same arrow in space.
:::

The plot shows a vector built as $\mathbf{v} = 2e_1 + 3e_2$, decomposed along the two basis directions.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

e1 = np.array([1, 0])
e2 = np.array([0, 1])
v = 2 * e1 + 3 * e2

fig, ax = plt.subplots(figsize=(6, 5))
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 3.5)
ax.set_aspect('equal')

ax.arrow(0, 0, *e1, head_width=0.1, color='gray', length_includes_head=True)
ax.arrow(0, 0, *e2, head_width=0.1, color='gray', length_includes_head=True)
ax.text(1.05, -0.25, r'$e_1$', fontsize=13)
ax.text(-0.28, 1.05, r'$e_2$', fontsize=13)

ax.arrow(0, 0, *v, head_width=0.15, color='#2e4057', length_includes_head=True)
ax.plot([0, v[0]], [v[1], v[1]], '--', color='gray')
ax.plot([v[0], v[0]], [0, v[1]], '--', color='gray')
ax.text(v[0] + 0.1, v[1] + 0.1, r'$\mathbf{v} = 2e_1 + 3e_2$', color='#2e4057', fontsize=13)

ax.axhline(0, color='black', lw=0.8)
ax.axvline(0, color='black', lw=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Fig.1 A vector as a linear combination of basis vectors')
plt.tight_layout()
plt.show()
```

### Inner products, norms, and orthogonality

The **inner product** (dot product) $\langle a \mid b \rangle$ measures how much two vectors share a direction:

:::{important} **Dot product, geometric form**

$$
\langle a \mid b \rangle = |a|\,|b|\cos\theta
$$
:::

where $\theta$ is the angle between them. When two vectors are perpendicular the dot product is zero and we call them **orthogonal**. Vectors that are both orthogonal and normalized are **orthonormal**, compactly written with the Kronecker delta:

$$
\langle e_i \mid e_j \rangle = \delta_{ij} =
\begin{cases} 1 & i = j \\ 0 & i \neq j \end{cases}.
$$

The **norm** is the square root of a vector's inner product with itself, giving its length:

$$
\langle a \mid a \rangle = a_1^2 + a_2^2, \qquad |a| = \sqrt{a_1^2 + a_2^2}.
$$

A vector with $|a| = 1$ is **normalized**. Orthonormal bases and this norm are the finite-dimensional shadow of wavefunction normalization and orthogonality.

## Matrices

### Linear systems as matrix equations

A system of linear equations is a matrix acting on a vector. The system

$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 &= b_1 \\
a_{21}x_1 + a_{22}x_2 &= b_2
\end{aligned}
$$

packs into a single matrix-vector product:

:::{important} **A linear system as a matrix equation**

$$
A\mathbf{x} = \mathbf{b}
$$

where $A$ holds the coefficients, $\mathbf{x}$ is the vector of unknowns, and $\mathbf{b}$ the right-hand side.
:::

Matrix times vector is the dot product of each row of $A$ with $\mathbf{x}$:

$$
A\mathbf{x} = \begin{pmatrix} a_{11}x_1 + a_{12}x_2 \\ a_{21}x_1 + a_{22}x_2 \end{pmatrix}.
$$

If $A$ is invertible, the solution is $\mathbf{x} = A^{-1}\mathbf{b}$.

```{code-cell} python
import numpy as np

A = np.array([[2, 3],
              [1, -2]])
b = np.array([7, 1])

# Solve by inversion, and with the recommended solver
x_inv = np.linalg.inv(A) @ b
x_solve = np.linalg.solve(A, b)

print("solution via inverse:", x_inv)
print("solution via solve  :", x_solve)
```

:::{tip} **Prefer `solve` over `inv`**
:class: dropdown

`np.linalg.solve(A, b)` is both faster and more numerically accurate than forming `np.linalg.inv(A) @ b`. Inverting a matrix explicitly is almost never necessary and should be avoided in real calculations; we show the inverse here only because it makes the algebra transparent.
:::

### Eigenvalues and eigenvectors

When a matrix acts on a vector it usually changes both its length and direction. Certain special vectors keep their direction and are only **rescaled**. These are **eigenvectors**, and the scaling factors are **eigenvalues**.

:::{important} **The eigenvalue problem**

A nonzero vector $\mathbf{v}$ is an eigenvector of $A$ if

$$
A\mathbf{v} = \lambda\mathbf{v},
$$

where the scalar $\lambda$ is its eigenvalue.
:::

Rearranging to $(A - \lambda I)\mathbf{v} = 0$, a nonzero solution exists only when the **characteristic equation** holds:

$$
\det(A - \lambda I) = 0.
$$

The sign and size of $\lambda$ say what happens to the eigenvector: $\lambda > 1$ stretches it, $0 < \lambda < 1$ compresses it, $\lambda < 0$ flips it, and $\lambda = 0$ collapses it. In quantum mechanics this exact structure reappears for **operators acting on wavefunctions**: eigenvalues are the measurable observables (energies, momenta) and eigenvectors are the states with definite outcomes. The [next page](04-operators-and-differential-equations.md) makes that leap explicit, showing that a function is just a vector with infinitely many components and the Schrodinger equation $\hat H\psi = E\psi$ is this same eigenvalue problem $A\mathbf{v}=\lambda\mathbf{v}$.

```{code-cell} python
import numpy as np

A = np.array([[2, 1],
              [1, 2]])
vals, vecs = np.linalg.eig(A)

print("eigenvalues :", vals)
print("eigenvectors (columns):\n", vecs)

# Verify A v = lambda v for the first eigenpair
print("\nA @ v0        :", A @ vecs[:, 0])
print("lambda0 * v0  :", vals[0] * vecs[:, 0])
```

### The geometric action of a matrix

Different kinds of matrices deform a shape in characteristic ways:

| Matrix type | Example | Effect |
|---|---|---|
| Diagonal, unequal entries | `[[1.8, 0], [0, 0.8]]` | **Stretch**, different scaling per axis |
| Diagonal, equal entries | `[[0.7, 0], [0, 0.7]]` | **Uniform scaling** |
| Rotation (orthogonal) | `[[cosθ, -sinθ], [sinθ, cosθ]]` | **Rotation**, preserves lengths and angles |
| Off-diagonal term | `[[1, k], [0, 1]]` | **Shear**, slants without changing area |

We apply each matrix to the same small polygon to see how it transforms.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

coords = np.array([[0, 0], [0.5, 0.5], [0.5, 1.5], [0, 1], [0, 0]]).T

stretch = np.array([[1.8, 0], [0, 0.8]])
rotation = np.array([[np.cos(np.pi / 6), -np.sin(np.pi / 6)],
                     [np.sin(np.pi / 6),  np.cos(np.pi / 6)]])
shear = np.array([[1, 0.8], [0, 1]])
scaling = np.array([[0.7, 0], [0, 0.7]])

transforms = {
    "Stretch (non-uniform)": stretch,
    "Rotation (30 deg)": rotation,
    "Shear": shear,
    "Scaling (uniform)": scaling,
}

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
for ax, (name, M) in zip(axes.flat, transforms.items()):
    ax.plot(coords[0], coords[1], 'r--', label='original')
    new_coords = M @ coords
    ax.plot(new_coords[0], new_coords[1], 'b-', label='transformed')
    ax.set_title(name, fontsize=11)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 2)
    ax.grid(True, ls=':')
    ax.legend(fontsize=8, loc='upper left')

plt.suptitle('Fig.2 How different matrices deform the same shape', fontsize=13)
plt.tight_layout()
plt.show()
```

## Problems

### Problem 1: Dot product and angle

Find $\langle a \mid b \rangle$ and the angle between $a = (1, 2)$ and $b = (3, -1)$.

:::{admonition} **Solution**
:class: dropdown solution

$$
\langle a \mid b \rangle = (1)(3) + (2)(-1) = 1.
$$

With $|a| = \sqrt{5}$ and $|b| = \sqrt{10}$,

$$
\cos\theta = \frac{1}{\sqrt{5}\sqrt{10}} = \frac{1}{\sqrt{50}} \approx 0.141,
\qquad \theta \approx 81.9^\circ.
$$
:::

### Problem 2: Normalize a vector

Normalize $v = (3, 4)$.

:::{admonition} **Solution**
:class: dropdown solution

$|v| = \sqrt{9 + 16} = 5$, so the normalized vector is $\hat{v} = (3/5,\ 4/5)$, which has length $1$.
:::

### Problem 3: Check orthogonality

Are $(1, 1)$ and $(1, -1)$ orthogonal? Are they orthonormal?

:::{admonition} **Solution**
:class: dropdown solution

Their dot product is $(1)(1) + (1)(-1) = 0$, so they are orthogonal. Each has length $\sqrt{2}$, not $1$, so they are orthogonal but **not** orthonormal. Dividing each by $\sqrt{2}$ makes them orthonormal.
:::

### Problem 4: Eigenvalues by hand

Find the eigenvalues of $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.

:::{admonition} **Solution**
:class: dropdown solution

$$
\det(A - \lambda I) = (2 - \lambda)^2 - 1 = 0 \;\Rightarrow\; (2-\lambda) = \pm 1,
$$

so $\lambda = 3$ and $\lambda = 1$, matching the numerical output above.
:::

### Problem 5: Solve a linear system

Solve $\begin{pmatrix} 2 & 3 \\ 1 & -2 \end{pmatrix}\mathbf{x} = \begin{pmatrix} 7 \\ 1 \end{pmatrix}$ by hand and check against the code.

### Problem 6: Rotation preserves length

Show that the rotation matrix $R = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ leaves the norm of any vector unchanged.

### Problem 7: Eigenvector direction

Verify that $(1, 1)$ is an eigenvector of $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ and identify its eigenvalue.

### Problem 8: Complex inner product

For complex vectors the inner product conjugates the first entry: $\langle a \mid b \rangle = \sum_i a_i^* b_i$. Compute $\langle a \mid a \rangle$ for $a = (1,\ i)$ and confirm it is real and positive.
