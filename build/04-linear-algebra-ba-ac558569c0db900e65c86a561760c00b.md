---
kernelspec:
  name: python3
  display_name: Python 3
---

# Linear Algebra Basics

:::{note} **What you will learn**

- **Vectors as arrays of numbers.** A vector is an ordered collection of numbers that describes the state or configuration of a system, and any vector can be written as a linear combination of basis vectors.
- **Inner products, norms, and orthogonality.** The dot product measures how much two vectors share a direction; orthonormal vectors are both normalized and mutually perpendicular.
- **Systems of linear equations as matrix operations.** A linear system $A\mathbf{x}=\mathbf{b}$ can be solved compactly by matrix inversion.
- **Eigenvalues and eigenvectors.** Special vectors that a matrix only rescales, not rotates. In quantum mechanics, eigenvalues correspond to measurable observables and eigenvectors to states with definite outcomes.
- **The geometric action of matrices.** Matrices stretch, rotate, shear, and scale vectors, and we can visualize each of these effects.
:::

### Vectors, what are they?

<html>
<iframe width="300" height="300" src="https://www.youtube.com/embed/fNk_zzaMoSs" frameborder="0" allowfullscreen>
</iframe>
</html>

```{code-cell} python
:tags: [hide-input]
# Visualizing geometric vs abstract representations of vectors
import matplotlib.pyplot as plt
import numpy as np

# Basis vectors and sample vector
e1 = np.array([1, 0])
e2 = np.array([0, 1])
v = 2*e1 + 3*e2

fig, ax = plt.subplots(figsize=(7, 5))
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 3.5)
ax.set_aspect('equal')

# Draw basis vectors
ax.arrow(0, 0, *e1, head_width=0.1, color='gray', length_includes_head=True)
ax.arrow(0, 0, *e2, head_width=0.1, color='gray', length_includes_head=True)
ax.text(1.1, -0.2, r'$\mathbf{e_1}$', fontsize=14)
ax.text(-0.2, 1.1, r'$\mathbf{e_2}$', fontsize=14)

# Draw vector v and its components
ax.arrow(0, 0, *v, head_width=0.15, color='royalblue', length_includes_head=True)
ax.plot([0, v[0]], [v[1], v[1]], '--', color='gray')
ax.plot([v[0], v[0]], [0, v[1]], '--', color='gray')
ax.text(v[0]+0.1, v[1]/2, r'$2\mathbf{e_1}$', color='gray', fontsize=12, rotation=0)
ax.text(v[0]/2, v[1]+0.1, r'$3\mathbf{e_2}$', color='gray', fontsize=12, rotation=0)
ax.text(v[0]+0.1, v[1]+0.1, r'$\mathbf{v} = 2\mathbf{e_1} + 3\mathbf{e_2}$', color='royalblue', fontsize=14)

# Axes and labels
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('A vector as a linear combination of basis vectors')
plt.show()
```

### Vectors as arrays of numbers

A **vector** is an ordered collection of numbers that represents the state or configuration of a physical system.

* $a = (-2, 8)$, a 2D vector
* $e_1 = (1,0)$, a unit vector along the x axis, and $e_2 = (0,1)$, a unit vector along the y axis
* $b = (1.34, 4.23, 5.98)$, a 3D vector
* $c = (1, -2, 4i, 3 + 2i)$, a 4D vector with complex components
* $f = (1, 2, 3, 4, 5, 6, \ldots)$, an infinite-dimensional vector (e.g., a sequence)

**Note:** Vectors may belong to *real* or *complex* vector spaces depending on the nature of their components.

:::{tip} **Vector Space**

* Any vector in an $N$-dimensional space can be written as a **linear combination** of $N$ linearly independent basis vectors.
* For instance, in 2D space, we can choose two perpendicular unit vectors $e_1$ and $e_2$ to form a convenient basis:

$$
\vec{a} = a_1 e_1 + a_2 e_2 = \begin{pmatrix}
    a_1\\
    a_2\\
    \end{pmatrix}
$$

$$a= \begin{pmatrix}
    2\\
    3\\
    \end{pmatrix} = 2\begin{pmatrix}
    1\\
    0\\
    \end{pmatrix}+3 \begin{pmatrix}
    0\\
    1\\
    \end{pmatrix}
$$

* If we choose a rotated basis $e'_1$, $e'_2$ (e.g., choose basis vectors with a different orientation), the same vector will have different components, but it remains the same vector.
:::

### Inner products and orthogonality

- **Dot product $\langle a\mid b \rangle$** quantifies the projection of vector $a$ on $b$ and vice versa. That is, how much $a$ and $b$ have in common in terms of direction in space!

:::{important} **Dot product: geometric definition**

$$
\langle a\mid b \rangle = |a| |b| \cos\theta
$$
:::

- The $\theta$ measures the angle between $a$ and $b$. If the vectors are perpendicular, like the unit vectors in the Cartesian system, we call them **orthogonal**.
- **Orthonormal vectors** are both normalized and orthogonal. We denote the orthonormality condition with the convenient Kronecker symbol: $\delta_{ij}=0$ when $i\neq j$ and $1$ when $i=j$.

$$
\langle e_i \mid e_j \rangle =\delta_{ij}
$$

$$
  (1,0)\begin{pmatrix}
    0\\
    1\\
    \end{pmatrix}=1\cdot 0+0\cdot 1=0
$$

- **Norm of a vector $\mid a\mid$** is the projection of the vector onto itself and quantifies the length of the vector. When the norm is $\mid a \mid=1$, we say that the vector is normalized.

$$
\langle a \mid a\rangle= \big(a_1\langle e_1| + a_2 \langle e_2|\big) \cdot \big (a_1 |e_1\rangle + a_2 |e_2 \rangle \big ) = a_1^2+a_2^2
$$

$$
\mid a \mid =\sqrt{a_1^2+a_2^2}
$$

### Systems of linear equations as matrix operations

A system of linear equations can be interpreted as a matrix operating on a vector to produce another vector. For example, consider the system:

$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 &= b_1 \\
a_{21}x_1 + a_{22}x_2 &= b_2
\end{aligned}
$$

This system can be written compactly in matrix form as:

:::{important} **A system of linear equations as a matrix-vector product**

$$
A \mathbf{x} = \mathbf{b}
$$

- $A$ is a matrix containing the coefficients of the system,
- $\mathbf{x}$ is the vector of unknowns, and
- $\mathbf{b}$ is the vector of constants (right-hand side).
:::

For a 2D system, this becomes:

$$
\begin{pmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{pmatrix}
\begin{pmatrix}
x_1 \\
x_2
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\
b_2
\end{pmatrix}
$$

### Matrix-vector multiplication

**Row-by-column product rule**

Matrix multiplication operates by taking the dot product of the rows of the matrix $A$ with the vector $\mathbf{x}$. For the above example:

$$
A \mathbf{x} = \begin{pmatrix}
a_{11}x_1 + a_{12}x_2 \\
a_{21}x_1 + a_{22}x_2
\end{pmatrix}
$$

This shows how the system of equations is equivalent to a single matrix-vector product.

:::{important} **Solving a linear equation via matrix inversion**

$${\bf x} = A^{-1}{\bf b}$$
:::

```{code-cell} python
:tags: [hide-input]
import numpy as np
# Define the coefficients matrix A and the right-hand side vector b
print('Solving Ax=b via matrix inversion')

A = np.array([[2, 3],
              [1, -2]])

b = np.array([7, 1])

print('A', A)
print('b', b)

# Calculate the inverse of matrix A
A_inv = np.linalg.inv(A)

# Solve for the unknown vector x using matrix inversion: x = A_inv * b
x = np.dot(A_inv, b)

print("Solution using matrix inversion:")
print("x =", x)
```

### Eigenvalues and eigenvectors

- When a matrix acts on a vector, it generally **changes both its direction and length**. However, there are special vectors that **preserve their direction**: they are only **scaled** by the transformation. These are called **eigenvectors**, and the corresponding scaling factors are **eigenvalues**.

:::{important} **Definition of the Eigenvalue Problem**

A vector $\mathbf{v}$ is an **eigenvector** of a matrix $A$ if

$$
A \mathbf{v} = \lambda \mathbf{v},
$$

where $\lambda$ is a **scalar** called the **eigenvalue**.
:::

In this equation:

* $A$ is the linear transformation (matrix or operator),
* $\mathbf{v}$ is a non-zero vector whose direction remains unchanged,
* $\lambda$ tells how much $\mathbf{v}$ is stretched, compressed, or flipped.

#### Finding eigenvalues

Rearranging the equation gives:

$$
(A - \lambda I)\mathbf{v} = 0.
$$

For a nontrivial solution ($\mathbf{v} \neq 0$), the determinant must vanish:

$$
\det(A - \lambda I) = 0.
$$

This condition is the **characteristic equation** of the matrix and yields the possible eigenvalues $\lambda$.

#### Geometric meaning

* If $\lambda > 1$: the vector is **stretched**.
* If $0 < \lambda < 1$: the vector is **compressed**.
* If $\lambda < 0$: the vector is **flipped** in direction.
* If $\lambda = 0$: the vector is **collapsed** to the origin.

In quantum mechanics, this idea generalizes to **operators acting on wavefunctions**, where eigenvalues correspond to **measurable quantities** (observables) and eigenvectors to the **states** with definite outcomes.

| Property | Expression | Meaning |
| ----------------------- | ------------------------------------------------ | -------------------------------------------------- |
| Eigenvalue equation | $A\mathbf{v} = \lambda\mathbf{v}$ | Defines scaling along eigenvector |
| Inverse action | $A^{-1}\mathbf{v} = \frac{1}{\lambda}\mathbf{v}$ | Inverse rescales in opposite way |
| Invertibility condition | $\det(A) \neq 0$ or all $\lambda \neq 0$ | Matrix is invertible only if no eigenvalue is zero |

### Visualizing the action of a matrix on a vector

- These transformations illustrate different ways of modifying vectors and geometric shapes through scaling, shearing, and identity operations. We use a 2D vector and matrices as an example.

| Matrix Type | Example | Effect |
| ---------------------------- | ------------------------------- | --------------------------------------------- |
| Diagonal, unequal entries | `[[2, 0], [0, 0.5]]` | **Stretch**, different scaling per axis |
| Diagonal, equal entries | `[[0.7, 0], [0, 0.7]]` | **Uniform scaling**, isotropic compression |
| Orthogonal (rotation matrix) | `[[cosθ, -sinθ], [sinθ, cosθ]]` | **Rotation**, preserves lengths and angles |
| Off-diagonal elements | `[[1, k], [0, 1]]` | **Shear**, slants axes without changing area |

- We pick the following four dummy vectors and act our matrix on all of them to see how the relationship between their distances and angles changes.

$$(0,0), (0.5,0.5), (0.5, 1.5), (0,1), (0,0)$$

- We connect the points defined by these vectors to aid our visualization.

```{code-cell} python
:tags: [hide-input]
import matplotlib.pyplot as plt
import numpy as np

# Define the original shape (unit square)
coords = np.array([
    [0, 0],
    [0.5, 0.5],
    [0.5, 1.5],
    [0, 1],
    [0, 0]
]).T

# Define transformations
stretch = np.array([[1.8, 0],
                    [0, 0.8]])   # non-uniform diagonal: stretch
rotation = np.array([[np.cos(np.pi/6), -np.sin(np.pi/6)],
                     [np.sin(np.pi/6),  np.cos(np.pi/6)]])  # 30 degree rotation
shear = np.array([[1, 0.8],
                  [0, 1]])       # off-diagonal term: shear
scaling = np.array([[0.7, 0],
                    [0, 0.7]])   # uniform diagonal: scaling

# Collect transformations
transforms = {
    "Stretch (non-uniform scaling)": stretch,
    "Rotation": rotation,
    "Shear": shear,
    "Scaling (uniform)": scaling
}

# Set up 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(8, 8))

for ax, (name, M) in zip(axes.flat, transforms.items()):
    # Original shape
    ax.plot(coords[0], coords[1], 'r--', label='original')

    # Transformed shape
    new_coords = M @ coords
    ax.plot(new_coords[0], new_coords[1], 'b-', label='transformed')

    # Style
    ax.set_title(name, fontsize=11)
    ax.set_aspect('equal', 'box')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 2)
    ax.grid(True, ls=':')
    ax.legend(fontsize=8, loc='upper left')

plt.suptitle("Linear Transformations of a Vector Set", fontsize=14)
plt.tight_layout()
plt.show()
```
</content>
