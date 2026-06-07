---
kernelspec:
  name: python3
  display_name: Python 3
---

# Operators and Matrices

:::{note} **What you will learn**

- **Functions in quantum mechanics seen as vectors.** Sampling a function at $N$ points turns it into an $N$-dimensional vector.
- **Operators seen as matrices.** Differential operators acting on discretized functions can be represented by finite-difference matrices.
- **Finite-difference derivatives.** Forward and centered differences approximate first and second derivatives, with care needed at the boundaries.
- **Matrix multiplication and its rules.** Matrix products, powers, the identity, and the inverse, plus the crucial fact that matrix multiplication is generally not commutative.
:::

### Functions in QM seen as vectors

- Take any function and evaluate it at $N$ points, e.g., $x=(1,2,3, \ldots N)$.
- We have just turned our function into a vector with $N$ components, or an $N$-dimensional vector.
- Example: $f(x)=x^2$ can be represented as $(1, 4, 8)$, where we evaluated the function at three points.

### Operators in QM seen as matrices

- In quantum mechanics, **functions** that describe quantum states can be treated as vectors in a vector space, and **operators** that act on these functions are represented as matrices.
- For instance, a **differentiation operator** can be represented by a matrix when acting on discretized versions of the wavefunctions. Let us illustrate this with the first and second derivative operators.

#### Example: First derivative as a matrix

- Suppose we discretize a function $\psi(x)$ over a set of points $\{x_1, x_2, \dots, x_n\}$ with spacing $h$. We can approximate the first derivative using the **finite difference**:

$$ \frac{d\psi}{dx} \approx \frac{\psi(x_{i+1}) - \psi(x_i)}{h} $$

- This operation can be represented by a matrix. For $n = 5$ grid points, the first derivative matrix $D_1$ in the finite-difference approximation looks like:

$$
D_1 = \frac{1}{h}
\begin{pmatrix}
-1 & 1 & 0 & 0 & 0 \\
0 & -1 & 1 & 0 & 0 \\
0 & 0 & -1 & 1 & 0 \\
0 & 0 & 0 & -1 & 1 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}
$$

- For a function represented as a vector $\psi = (\psi(x_1), \psi(x_2), \dots, \psi(x_5))$, applying this matrix gives the derivative at each point.

#### Numerical example of applying the derivative matrix for $\psi(x) = x^2$

Let us consider the function $\psi(x) = x^2$ sampled at 5 points $x = (0, 1, 2, 3, 4)$, giving us:

$$ \psi = \begin{pmatrix}
    0 \\
    1 \\
    4 \\
    9 \\
    16
\end{pmatrix}
$$

If the spacing between points is $h = 1$, applying the first derivative matrix $D_1$ gives:

$$
D_1 \cdot \psi = \frac{1}{1}
\begin{pmatrix}
-1 & 1 & 0 & 0 & 0 \\
0 & -1 & 1 & 0 & 0 \\
0 & 0 & -1 & 1 & 0 \\
0 & 0 & 0 & -1 & 1 \\
0 & 0 & 0 & 0 & 0
\end{pmatrix}
\begin{pmatrix}
0 \\
1 \\
4 \\
9 \\
16
\end{pmatrix}
= \begin{pmatrix}
1 \\
3 \\
5 \\
7 \\
0
\end{pmatrix}
$$

This approximates the first derivative of $\psi(x) = x^2$ at each of the sampled points:

- At $x = 1$, the derivative is approximately 1 (exact value: 2).
- At $x = 2$, the derivative is approximately 3 (exact value: 4).
- At $x = 3$, the derivative is approximately 5 (exact value: 6).
- At $x = 4$, the derivative is approximately 7 (exact value: 8).
- The last value is zero due to boundary handling.

This illustrates how the finite-difference method approximates the derivative for the function $\psi(x) = x^2$ at discrete points.

```{code-cell} python
:tags: [hide-input]
import numpy as np

# Define the grid points and function
n = 5
x = np.linspace(0, 4, n)  # Grid points from 0 to 4
h = x[1] - x[0]  # Spacing between points
psi = x**2  # Function psi(x) = x^2

# Define the first derivative matrix D_1
D_1 = (1/h) * np.array([
    [-1, 1, 0, 0, 0],
    [0, -1, 1, 0, 0],
    [0, 0, -1, 1, 0],
    [0, 0, 0, -1, 1],
    [0, 0, 0, 0, 0]
])

# Apply the first derivative matrix to the function vector
derivative_psi = D_1 @ psi

print('derivative of x^2 using finite difference matrix', derivative_psi)

# Exact derivative of psi = x^2 is 2*x
exact_derivative_psi = 2 * x
print('\nExact derivative of x^2:\n', exact_derivative_psi)
```

#### Centered-difference approximation

- A much better approximation is obtained by using a centered difference (the difference between one point to the left and one point to the right of a given point).
- We also take care of the boundary points via a higher-order evaluation of the derivatives.

$$ \frac{d\psi}{dx} \approx \frac{\psi(x_{i+1}) - \psi(x_{i-1})}{2h} $$

- This operation can be represented by a matrix. For $n = 5$ grid points, with improved boundary handling, the first derivative matrix $D_1$ using the centered-difference method looks like:

$$
D_1 = \frac{1}{2h}
\begin{pmatrix}
-3 & 4 & -1 & 0 & 0 \\
-1 & 0 & 1 & 0 & 0 \\
0 & -1 & 0 & 1 & 0 \\
0 & 0 & -1 & 0 & 1 \\
0 & 0 & 1 & -4 & 3
\end{pmatrix}
$$

- The coefficients $-3,4,-1$ come from applying a Taylor-series expansion to derive a higher-order accurate one-sided difference approximation for the derivative at the boundary point.

```{code-cell} python
:tags: [hide-input]
import numpy as np

# Define the grid points and function
n = 5
x = np.linspace(0, 4, n)  # Grid points from 0 to 4
h = x[1] - x[0]  # Spacing between points
psi = x**2  # Function psi(x) = x^2

# Define the centered difference approximation for the first derivative matrix
D_1_centered = (1/(2*h)) * np.array([
    [-3, 4, -1, 0, 0],  # One-sided difference for the first point (improved boundary handling)
    [-1, 0, 1, 0, 0],   # Centered difference for interior points
    [0, -1, 0, 1, 0],
    [0, 0, -1, 0, 1],
    [0, 0, 1, -4, 3]    # One-sided difference for the last point (improved boundary handling)
])

# Apply the centered difference matrix to the function vector
derivative_psi_centered = D_1_centered @ psi

# Print the results
print('First derivative using centered difference approximation:\n', derivative_psi_centered)

# Exact derivative of psi = x^2 is 2*x
exact_derivative_psi = 2 * x
print('\nExact derivative of x^2:\n', exact_derivative_psi)
```

#### Second derivative as a matrix (centered difference)

Similarly, the second derivative can be approximated by a **centered-difference formula** for interior points:

$$ \frac{d^2\psi}{dx^2} \approx \frac{\psi(x_{i+1}) - 2\psi(x_i) + \psi(x_{i-1})}{h^2} $$

At the **boundaries**, we use one-sided difference formulas to maintain accuracy:

- At the first point $x_1$, we approximate using:

  $$ \frac{d^2\psi}{dx^2} \bigg|_{x_1} \approx \frac{\psi(x_1) - 2\psi(x_2) + \psi(x_3)}{h^2} $$

- At the last point $x_n$, we approximate using:

  $$ \frac{d^2\psi}{dx^2} \bigg|_{x_n} \approx \frac{\psi(x_{n-2}) - 2\psi(x_{n-1}) + \psi(x_n)}{h^2} $$

The corresponding second derivative matrix $D_2$ for $n = 5$ grid points, with this improved boundary handling, is:

$$
D_2 = \frac{1}{h^2}
\begin{pmatrix}
1 & -2 & 1 & 0 & 0 \\
1 & -2 & 1 & 0 & 0 \\
0 & 1 & -2 & 1 & 0 \\
0 & 0 & 1 & -2 & 1 \\
0 & 0 & 1 & -2 & 1
\end{pmatrix}
$$

Applying this matrix to the vector $\psi$ gives the second derivative of the function at each point, including the boundary points with improved accuracy.

```{code-cell} python
:tags: [hide-input]
import numpy as np

# Define the grid points and function
n = 5
x = np.linspace(0, 4, n)  # Grid points from 0 to 4
h = x[1] - x[0]  # Spacing between points

psi = x**2  # Function psi(x) = x^2
# Define the centered difference approximation for the second derivative matrix
D_2_centered = (1/h**2) * np.array([
    [1, -2, 1, 0, 0],
    [1, -2, 1, 0, 0],
    [0, 1, -2, 1, 0],
    [0, 0, 1, -2, 1],
    [0, 0, 0, 1, -2]
])

# Calculate the second derivative of x^2 using the centered difference method
second_derivative_centered = D_2_centered @ psi

print('second derivative of x^2 by using centered difference \n', second_derivative_centered)
```

### Matrix multiplication

:::{important} **Matrix multiplication as a row-by-column product**

$$\bf C = AB$$

$$C_{ij} = \sum_k A_{ik} B_{kj}$$
:::

- **Powers of a matrix.** Multiplying the same matrix together yields different powers. For example, the second derivative matrix can be obtained by multiplying two first-order derivative matrices.

$$A \cdot A = A^2$$

- **Identity matrix.** $I$ is a special matrix with ones on the diagonal and zeros everywhere else. Multiplying by $I$ leaves a matrix intact.

$$I\cdot A = A\cdot I = A$$

- **Inverse of a matrix $A$** is a matrix $A^{-1}$, multiplication with which returns the identity matrix:

$$A^{-1}\cdot A = I$$

### Why matrix multiplication order matters

- In linear algebra, matrix multiplication is generally **not commutative**, meaning that for two matrices $A$ and $B$, it is usually the case that:

$$
A B \neq B A
$$

To illustrate why this happens, let us consider an example with 2D matrices.

#### Example: Non-commuting matrices

Let us define two 2D matrices $A$ and $B$:

$$
A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}, \quad B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
$$

We will compute $AB$ and $BA$ to show that they are not equal.

**Compute $AB$**

$$
AB = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix}
(1 \cdot 0 + 2 \cdot 1) & (1 \cdot 1 + 2 \cdot 0) \\
(0 \cdot 0 + 1 \cdot 1) & (0 \cdot 1 + 1 \cdot 0)
\end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix}
$$

**Compute $BA$**

$$
BA = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix}
(0 \cdot 1 + 1 \cdot 0) & (0 \cdot 2 + 1 \cdot 1) \\
(1 \cdot 1 + 0 \cdot 0) & (1 \cdot 2 + 0 \cdot 1)
\end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}
$$

**Compare $AB$ and $BA$**

We now have:

$$
AB = \begin{pmatrix} 2 & 1 \\ 1 & 0 \end{pmatrix}, \quad BA = \begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}
$$

Clearly, $AB \neq BA$.

#### Why do not matrices commute?

- The reason matrix multiplication is generally not commutative lies in how matrix multiplication is performed. Matrix multiplication involves combining rows of the first matrix with columns of the second matrix.
- These operations usually yield different results because the effect of applying transformations in different orders changes the outcome.
- For example, one matrix might represent a shear transformation and another a rotation. Applying the shear first and then the rotation will generally give a different result than applying the rotation first and then the shear.

#### Special cases

There are some special cases where matrices do commute:

- **Diagonal matrices**: if $A$ and $B$ are both diagonal matrices, then $AB = BA$, because each entry on the diagonal simply scales the corresponding entry in the other matrix.
- **Identity matrix**: the identity matrix $I$ commutes with any matrix $A$, i.e., $IA = AI = A$, because multiplying by the identity matrix leaves the original matrix unchanged.
</content>
