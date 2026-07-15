# Operators

:::{note} What you need to know
- For every experimental **observable** there is a **corresponding operator** in quantum mechanics.
- **Operators must be linear**, because they are derived from the Schrodinger equation, which itself is linear.
- **Operators must be Hermitian**, because only Hermitian operators produce real eigenvalues.
- **Operators must produce real eigenvalues**, because eigenvalues are the only possible values measured in experiments.
- Operator **commutators** show whether two experimental observables can be **measured simultaneously**. For example, can one simultaneously and precisely determine the position and momentum of an electron?
- Commuting operators share eigenfunctions; non-commuting operators have different eigenfunctions.
:::


### Operators

- In quantum mechanics, **operators** represent physical observables and are denoted by a hat symbol ($\hat{}$), which indicates a mathematical operation on functions.

- For example, the momentum operator differentiates the function with respect to $x$, then multiplies the result by $-i\hbar$.

  $$
  \hat{p}_x = -i\hbar\frac{d}{dx}
  $$

- The position operator simply multiplies the function by $x$.

  $$
  \hat{x} = x
  $$

- In quantum mechanics we use **a simple recipe to find operators**: take expressions from classical mechanics and replace position and momentum by their respective operator expressions.


### Linearity of Operators

- Operators in quantum mechanics are **linear**, meaning they satisfy:

$$
\hat{A}(\psi_1 + \psi_2) = \hat{A}\psi_1 + \hat{A}\psi_2
$$

$$
\hat{A}(c\psi) = c\hat{A}\psi
$$

- Here $c$ is a constant, and $\psi_1$, $\psi_2$, and $\psi$ are wavefunctions.
- $\hat{x}$, $\hat{p_x}$, and $\hat{H}$ all satisfy this property.



### Commutations of operators

:::{important} **Commutator $\hat{A}$ and $\hat{B}$**

$${\left[\hat{A},\hat{B}\right]f = \left(\hat{A}\hat{B} - \hat{B}\hat{A}\right)f}$$
:::

- From linear algebra we know that the order of matrix multiplication matters and that $AB\neq BA$ for two matrices $A$ and $B$.
- Thus we also generally expect $\hat{A}\hat{B} \neq \hat{B}\hat{A}$ for any two operators.

- We can quantify the relationship between two operators by computing the **commutator**.
    - If the commutator is zero, the order of multiplication of operators or matrices can be changed.
    - If the commutator is non-zero, the order matters and cannot be changed.


:::{note} **Example**

Prove that operators $\hat{A} = x$ and $\hat{B} = d/dx$ do not commute (i.e., $\left[\hat{A}, \hat{B}\right] \ne 0$).
:::

:::{admonition} **Solution**
:class: dropdown solution

Let $f$ be an arbitrary well-behaved function. We need to calculate both $\hat{A}\hat{B}f$ and $\hat{B}\hat{A}f$:

$$
\hat{A}\hat{B}f = xf'(x)\textnormal{ and } \hat{B}\hat{A}f = \frac{d}{dx}\left(xf(x)\right) = f(x) + xf'(x)$$
$$\left[\hat{A},\hat{B}\right]f = \hat{A}\hat{B}f - \hat{B}\hat{A}f = -f$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = -1\textnormal{ (this is non-zero and the operators do not commute)}
$$
:::

#### Simple rules for commutators

$${\left[A,A\right] = \left[A,A^n\right] = \left[A^n,A\right] = 0}$$

- This shows that an operator always commutes with itself and its powers. Now let's apply this. Would the kinetic energy operator commute with the momentum operator?

$${\left[A,B\right] = -\left[B,A\right]}$$

- This shows that order is important in a commutator. When you swap the operators, the sign changes.


### Commutators and experimental measurements

We have seen previously that operators may not always commute (i.e., $[A, B] \ne 0$). An example of such an operator pair is position $\hat{x}$ and momentum $\hat{p}_x$:

$${\hat{p}_x\hat{x}\psi(x) = \hat{p}_x\left(x\psi(x)\right) = \left(\frac{\hbar}{i}\frac{d}{dx}\right)\left(x\psi(x)\right) = \frac{\hbar x}{i}\frac{d\psi(x)}{dx} + \frac{\hbar}{i}\psi(x)}$$

$${\hat{x}\hat{p}_x\psi(x) = x\left(\frac{\hbar}{i}\frac{d\psi(x)}{dx}\right)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right]\psi(x) = \left(\hat{p}_x\hat{x} - \hat{x}\hat{p}_x\right)\psi(x) = \frac{\hbar}{i}\psi(x)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right] = \frac{\hbar}{i}}$$

In contrast, the kinetic energy operator and the momentum operator commute:

$$
{\left[\hat{T},\hat{p}_x\right] = \left[\frac{\hat{p}_x^2}{2m},\hat{p}_x\right] = \frac{p_x^3}{2m} - \frac{p_x^3}{2m} = 0}
$$

We had the uncertainty principle for the position and momentum operators:

$$
\Delta x\Delta p_x \ge \frac{\hbar}{2}
$$


In general, it turns out that for operators $\hat{A}$ and $\hat{B}$ that do not commute, the [uncertainty principle](http://en.wikipedia.org/wiki/Uncertainty_principle) applies in the following form:

$${\Delta A\Delta B \ge \frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right|}$$


- Let's check this relation on the example of momentum and position operators

- Denote $\hat{A} = \hat{x}$ and $\hat{B} = \hat{p}_x$. 

$$\frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right| = \frac{1}{2}\left|\left<\left[\hat{x},\hat{p}_x\right]\right>\right| = \frac{1}{2}\left|\left<\frac{\hbar}{i}\right>\right|
= \frac{1}{2}\left|\left<\psi\left|\frac{\hbar}{i}\right|\psi\right>\right| = \frac{1}{2}\left|\frac{\hbar}{i}\underbrace{\left<\psi\left|\psi\right.\right>}_{=1}\right| = \frac{\hbar}{2}$$

$$\Rightarrow \Delta x\Delta p_x \ge \frac{\hbar}{2}$$

- We find that we cannot measure precise values of position and momentum simultaneously.


### Commuting operators and simultaneous measurements

:::{important} **Commuting operators share eigenfunction**

$$[\hat{A},\hat{B}]=0$$

$$\hat{A}\phi_k = a_k \phi_k$$

$$\hat{B}\phi_k = b_k \phi_k$$

:::

:::{admonition} **Proof that commutation implies shared eigenfunctions**
:class: dropdown

- We will show that if all eigenfunctions of operators $\hat{A}$ and $\hat{B}$ are identical, then $\hat{A}$ and $\hat{B}$ commute with each other.

Denote the eigenvalues of $\hat{A}$ and $\hat{B}$ by $a_i$ and $b_i$ and the common eigenfunctions by $\psi_i$. For both operators we have then:

$$\hat{A}\psi_i = a_i\psi_i\textnormal{ and }\hat{B}\psi_i = b_i\psi_i$$

By using these two equations and expressing the general wavefunction $\psi$ as a linear combination of the eigenfunctions, the commutator can be evaluated as:

$$\hat{A}\hat{B}\psi = \hat{A}\left(\hat{B}\psi\right) = \hat{A}\overbrace{\left(\hat{B}\sum\limits_{i=1}^{\infty}c_i\psi_i\right)}^{\textnormal{complete basis}}
= \hat{A}\overbrace{\left(\sum\limits_{i=1}^{\infty}c_i\hat{B}\psi_i\right)}^{\hat{B}\textnormal{ linear}} = \hat{A}\overbrace{\left(\sum\limits_{i=1}^{\infty}c_ib_i\psi_i\right)}^{\textnormal{eigenfunction of }\hat{B}}$$
$$= \overbrace{\sum\limits_{i=1}^{\infty}c_ib_i\hat{A}\psi_i}^{\hat{A}\textnormal{ linear}} = \overbrace{\sum\limits_{i=1}^{\infty}c_ib_ia_i\psi_i}^{\textnormal{eigenfunction of }\hat{A}} = \overbrace{\sum\limits_{i=1}^{\infty}c_ia_ib_i\psi_i}^{a_i\textnormal{ and }b_i\textnormal{ are constants}} = \sum\limits_{i=1}^{\infty}c_ia_i\hat{B}\psi_i$$
$$= \hat{B}\sum\limits_{i=1}^{\infty}c_ia_i\psi_i = \hat{B}\sum\limits_{i=1}^{\infty}c_i\hat{A}\psi_i = \hat{B}\hat{A}\sum\limits_{i=1}^{\infty}c_i\psi_i = \hat{B}\hat{A}\psi$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = 0$$

Note that the commutation relation must apply to all well-behaved functions and not just for some given subset of functions!
:::

- If operators commute, that means we can **simultaneously measure the corresponding observables in a single experiment**.

- For instance, the kinetic energy and momentum operators commute, so we can measure momentum and kinetic energy together. But we cannot do the same for momentum and position.

- If we measure observables $A$ and $B$ described by a common eigenfunction $\phi_k$, we find the observables to be the corresponding eigenvalues $a_k$ and $b_k$.



### Expectation expression

- The **expectation value** of an observable $\hat{A}$, which gives the average outcome of measurements, is computed as:

  $$
  \langle A \rangle = \int \psi^* \hat{A} \psi \, d\tau
  $$

- **Special Case**: If the wavefunction $\psi$ is an eigenfunction of the operator $\hat{A}$, with eigenvalue $a$:

  $$
  \hat{A}\psi = a\psi
  $$

  Then the expectation value simplifies to:

  $$
  \langle A \rangle = \int \psi^* a \psi \, d\tau = a \int \psi^*\psi \, d\tau = a
  $$

  Since $\int \psi^*\psi \, d\tau = 1$ (normalization), the expectation value is simply the eigenvalue $a$.



### Dirac Notation

To express quantum states and operators more compactly, we use **Dirac (bra–ket) notation**.

* A **state** is written as a *ket*, $|\psi\rangle$, and its complex conjugate (dual) is the *bra*, $\langle\psi|$.
* The **inner product** between two states corresponds to the integral over space:
  
$$
  \langle \phi | \psi \rangle = \int \phi^*(r), \psi(r), d\tau
$$

* In this notation, the **expectation value** of an operator $\hat{A}$ becomes simply:
  
$$
  \langle A \rangle = \langle \psi | \hat{A} | \psi \rangle
$$
  
* This form is elegant and general: it applies to all quantum systems, independent of the particular representation (position, momentum, etc.).


### Hermitian Property of Operators


- In quantum mechanics, operators often act on **complex-valued functions**, so we need a notion of “complex conjugate” that applies not just to numbers but to operators.
This leads to the concept of the **adjoint operator**.

#### The Adjoint (Conjugate Transpose)

- For complex numbers we take the **complex conjugate**:
$(3 + 2i)^* = 3 - 2i$.

- For matrices or linear operators, the corresponding operation is the **adjoint**, denoted by the dagger symbol $(\dagger)$.

:::{important} **Definition of Adjoint**

* For an **operator**, the adjoint is defined through the **inner product**:

$$
\langle \phi | \hat{A}\psi \rangle = \langle \hat{A}^\dagger \phi | \psi \rangle.
$$

- This means that moving an operator from one side of an inner product to the other requires taking its adjoint (and thus a complex conjugate).

* For a **matrix**, the adjoint is its **conjugate transpose**:

$$
A^\dagger = (A^T)^*
$$

That is, swap rows and columns, then take the complex conjugate of every entry:

$$
(A^\dagger)_{jk} = A_{kj}^*.
$$


:::

In matrix element form, taking the adjoint generates different elements:

$$
a_{jk} = \langle \psi_j | \hat{A} | \psi_k \rangle
\quad \Rightarrow \quad
a^*_{kj} = \langle \psi_k | \hat{A}^\dagger | \psi_j \rangle.
$$



#### Hermitian (Self-Adjoint) Operators

An operator is **Hermitian** if it equals its own adjoint:

$$
\hat{A} = \hat{A}^\dagger.
$$

This means the operator behaves the same way when acting on either side of the inner product.

:::{important} **Hermitian Matrix**

$$
A = A^\dagger, \quad a_{jk} = a_{kj}^*.
$$
:::

:::{important} **Hermitian Operator**

$$
\langle \phi | \hat{A}\psi \rangle = \langle \hat{A}\phi | \psi \rangle,
\qquad \text{or equivalently,} \qquad
\langle j| \hat{A}|k\rangle = \langle k| \hat{A}|j\rangle^*.
$$

In integral form:

$$
\int \psi_j^*(x), [\hat{A}\psi_k(x)],dx
= \int \psi_k(x), [\hat{A}\psi_j(x)]^*,dx.
$$
:::



#### Why Hermitian Operators Matter


1. **Eigenvalues are real**: Observables in quantum mechanics (energy, momentum, position, etc.) are represented by **Hermitian operators**, ensuring all measurement outcomes are real numbers.

  $$
  \hat{A}|\psi\rangle = a|\psi\rangle \implies a \in \mathbb{R}.
  $$

:::{tip} **Proof of real eigenvalues**
:class: dropdown

- Let $\psi$ be an eigenfunction of $\hat{A}$ with eigenvalue $a$. Choose $\psi_j = \psi_k = \psi$. Then we can write the left-hand and right-hand sides of the Hermitian condition:

$$
\int \psi^* \hat{A} \psi \, d\tau = a
$$

$$
\int \psi \left(\hat{A} \psi\right)^* \, d\tau = a^*
$$

- Since the operator is Hermitian, this leads to an equality ensuring the eigenvalues are real.

$$
a = a^*
$$

:::

2. **Eigenfunctions are orthogonal**:

  $$
  \langle \psi_m | \psi_n \rangle = 0 \quad (m \ne n).
  $$

:::{tip} **Proof of orthogonal eigenfunctions**
:class: dropdown

The Hermitian property can also be used to show that eigenfunctions $\psi_j$ and $\psi_k$, corresponding to different eigenvalues $a_j$ and $a_k$ (with $a_j \neq a_k$, i.e., "non-degenerate"), are orthogonal to each other:

$$
\textnormal{LHS: } \int \psi_j^* \hat{A} \psi_k \, d\tau = \int \psi_j^* a_k \psi_k \, d\tau = a_k \int \psi_j^* \psi_k \, d\tau
$$

$$
\textnormal{RHS: } \int \psi_k \left(\hat{A} \psi_j \right)^* \, d\tau = \int \psi_k \left(a_j \psi_j \right)^* \, d\tau = a_j \int \psi_j^* \psi_k \, d\tau
$$

- Since the operator is Hermitian, we require that LHS = RHS. This results in:

$$
\left(a_k - a_j \right) \int \psi_j^* \psi_k \, d\tau = 0
$$

- If $a_j \neq a_k$, then we have:

$$
\int \psi_j^* \psi_k \, d\tau = 0
$$

- This shows that $\psi_j$ and $\psi_k$ are orthogonal.

- **Note**: If $a_j = a_k$, meaning the eigenvalues are degenerate, this result does not hold.

:::

:::{note} **Example of Hermitian Matrix**

Which of these matrices is Hermitian?

$\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}$, $\begin{pmatrix}
i & 0 \\
0 & 1
\end{pmatrix}$, $\begin{pmatrix}
-1 & -3i \\
3i & 8
\end{pmatrix}$, $\begin{pmatrix}
1 & 2i \\
2i & 3
\end{pmatrix}$
:::

:::{admonition} **Solution**
:class: dropdown solution

- For the first matrix we have $a_{12}=2\neq a^{*}_{21}=3$, **non-Hermitian**
- For the second matrix $a_{11}\neq a^{*}_{11}=0$, **non-Hermitian**
- For the third matrix  $a_{12}=-3i =a^{*}_{21} = (3i)^{*}=-3i$, **Hermitian**
- For the fourth matrix  $a_{12}=2i \neq a^{*}_{21} = (2i)^{*} = -2i$, **non-Hermitian**

:::

- Seeing that differentiation operators are Hermitian requires a little more work.

- A trick that helps is integration by parts, where the boundary term is zero because the wavefunction decays to zero at the boundaries (postulate 1, keeping probability finite).

$$\int \psi_1 d\psi_2 =- \int \psi_2d\psi_1 + \psi_1\psi_2\Big|_{x_{min}}^{x_{max}} =- \int \psi_2d\psi_1$$

:::{note} **Example of Hermitian Operator**

Prove that the momentum operator (in one dimension) is Hermitian.
:::

:::{admonition} **Solution**
:class: dropdown solution

${\int\limits_{-\infty}^{\infty}\psi_j^*(x)\left(-i\hbar\frac{d\psi_k(x)}{dx}\right)dx} = -i\hbar\int\limits_{-\infty}^{\infty}\psi_j^*(x)\frac{d\psi_k(x)}{dx}dx = \\ \overbrace{\int\limits_{-\infty}^{\infty}\psi_k(x)\left(i\hbar\frac{d\psi_j^*(x)}{dx}\right)dx}^{{integration\, by\, parts}}$
$ = {\int\limits_{-\infty}^{\infty}\psi_k(x)\left(-i\hbar\frac{d\psi_j(x)}{dx}\right)^*dx} \Rightarrow \hat{p}_x\textnormal{ is Hermitian}$.
:::

**Geometric Intuition** Hermitian operators are the analog of **symmetric matrices** in real vector spaces. They represent linear transformations that **do not rotate vectors into complex directions**: they only stretch or compress them along real axes.


### Problems

#### Problem-1: Is the $xd/dx$ operator Hermitian?

Check whether the operator $\hat{A} = xd/dx$ is Hermitian.

- You can test whether the following condition holds:

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( x \frac{d}{dx} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

- Note how complex conjugation applies to an expression with an operator inside.
- But since our operator contains no imaginary numbers, complex conjugation only applies to the wavefunction.


:::{note} **Solution**
:class: dropdown


**Step 1: Left-hand side**

The left-hand side is:

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx
$$

**Step 2: Integration by parts**

We apply integration by parts to simplify this expression. Using the product rule for differentiation, we get:

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx = \left[ x \psi_1^*(x) \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d}{dx} \left( x \psi_1^*(x) \right) \psi_2(x) \, dx
$$

The boundary term $\left[ x \psi_1^*(x) \psi_2(x) \right]_{a}^{b}$ can be discarded if the wavefunctions vanish at the boundaries (such as in the case of bound states in a box).

Now, for the remaining integral, we apply the derivative to the product $x \psi_1^*(x)$:

$$
\int_{a}^{b} \frac{d}{dx} \left( x \psi_1^*(x) \right) \psi_2(x) \, dx = \int_{a}^{b} \left( \psi_1^*(x) + x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

Thus, the left-hand side becomes:

$$
\int_{a}^{b} \psi_1^*(x) \psi_2(x) \, dx + \int_{a}^{b} x \frac{d}{dx} \psi_1^*(x) \psi_2(x) \, dx
$$

**Step 3: Right-hand side**

The right-hand side is:

$$
\int_{a}^{b} \left( x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

**Step 4: Comparison**

Now, we compare the two expressions. The left-hand side contains the extra term:

$$
\int_{a}^{b} \psi_1^*(x) \psi_2(x) \, dx
$$

which is not present in the right-hand side. This means:

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx \neq \int_{a}^{b} \left( x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

- Since the two sides are not equal, we conclude that the operator $x \frac{d}{dx}$ **is non-Hermitian.**
:::

#### Problem-2: Is the $d^2/dx^2$ operator Hermitian?

- You can test whether the following condition holds:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx
$$

- Note how complex conjugation applies to an expression with an operator inside. But since our operator contains no imaginary numbers, it will only apply to the wavefunction.


:::{note} **Solution**
:class: dropdown

To show that the operator $\hat{A} = \frac{d^2}{dx^2}$ is Hermitian, we need to check whether the following condition holds:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

### Step 1: Left-hand side

The left-hand side is:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx
$$

### Step 2: Integration by parts

We apply integration by parts twice. First, applying integration by parts to the term $\psi_1^*(x) \frac{d^2}{dx^2} \psi_2(x)$, we get:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \left[ \psi_1^*(x) \frac{d}{dx} \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d}{dx} \psi_1^*(x) \frac{d}{dx} \psi_2(x) \, dx
$$

The boundary term $\left[ \psi_1^*(x) \frac{d}{dx} \psi_2(x) \right]_{a}^{b}$ can be discarded if the wavefunctions vanish at the boundaries (as for bound states in a box).

We now apply integration by parts again to the remaining term:

$$
-\int_{a}^{b} \frac{d}{dx} \psi_1^*(x) \frac{d}{dx} \psi_2(x) \, dx = \left[ \frac{d}{dx} \psi_1^*(x) \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d^2}{dx^2} \psi_1^*(x) \psi_2(x) \, dx
$$

Again, the boundary term $\left[ \frac{d}{dx} \psi_1^*(x) \psi_2(x) \right]_{a}^{b} $ vanishes if the wavefunctions vanish at the boundaries. This leaves us with:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

**Step 3: Conclusion**

Since the two sides are equal, we conclude that the operator $\frac{d^2}{dx^2}$ is Hermitian:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

:::


#### Problem-3: Is the $id^2/dx^2$ operator Hermitian?

- You can test whether the following condition holds:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx
$$

:::{note} **Solution**
:class: dropdown

From the last problem we learned that the following condition holds, which makes the second derivative operator $d^2/dx^2$ Hermitian:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1^*(x) \right)  \, dx
$$

- Now if we have $id^2/dx^2$, the complex conjugate part will produce a minus sign, which breaks the Hermitian equality:

$$
\int_{a}^{b} \psi_1^*(x) \left( i\frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( i\frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx = -\int_{a}^{b} \psi_2(x)\left( i\frac{d^2}{dx^2} \psi_1(x)^* \right)
$$

:::

#### Problem-4: Identify Hermitian Matrices

$$
A = \begin{pmatrix}
1 & 2 \\
2 & 3
\end{pmatrix}
$$

$$
B = \begin{pmatrix}
i & 1 \\
-1 & -i
\end{pmatrix}
$$

$$
C = \begin{pmatrix}
2 & i \\
-i & 2
\end{pmatrix}
$$

:::{note} **Solution**
:class: dropdown

**A Matrix**

To check if a matrix is Hermitian, it must satisfy the condition $A = A^\dagger$, where $A^\dagger$ is the conjugate transpose of $A$. Since this matrix has real entries, the conjugate transpose is just the transpose.

The transpose of $A$ is:

$
A^\dagger = \begin{pmatrix}
1 & 2 \\
2 & 3
\end{pmatrix}
$

Since $A = A^\dagger$, matrix $A$ is **Hermitian**.

**B Matrix**
Now, let's compute the conjugate transpose of $B$. We first take the transpose and then take the complex conjugate of each entry:

$$
B^\dagger = \begin{pmatrix}
-i & -1 \\
1 & i
\end{pmatrix}
$$

Clearly, $B \neq B^\dagger$, so matrix $B$ is **not Hermitian**.

**C Matrix**

The conjugate transpose of $C$ is:

$$
C^\dagger = \begin{pmatrix}
2 & -i \\
i & 2
\end{pmatrix}
$$

Since $C = C^\dagger$, matrix $C$ is **Hermitian**.

:::

#### Problem-5 Momentum Matrix

Show how the momentum operator looks in matrix form using a finite-dimensional example where you evaluate the wavefunction on 4 points, which will correspond to a $4 \times 4$ matrix.

:::{note} **Solution**
:class: dropdown

- We can represent the momentum operator $\hat{p} = -i \hbar \frac{d}{dx}$ in a discrete basis, such as using a position basis. In this case, the matrix elements of the momentum operator can be approximated using finite differences.

- For simplicity, let's assume we are working in a discrete system, where we approximate the derivative $\frac{d}{dx}$ with finite differences. The finite difference approximation for the derivative at point $x_n$ is:

$$
\frac{d \psi(x)}{dx} \approx \frac{\psi(x_{n+1}) - \psi(x_{n-1})}{2 \Delta x}
$$

- where $\Delta x$ is the spacing between the discrete points.

- The corresponding momentum operator matrix in this finite-dimensional space can be written as a skew-symmetric matrix that captures this finite difference behavior.

- Here is an example of a $4 \times 4$ momentum operator matrix $P$, assuming $\hbar = 1$ for simplicity:

$$
P = \frac{i}{2 \Delta x} \begin{pmatrix}
0 & -1 & 0 & 1 \\
1 & 0 & -1 & 0 \\
0 & 1 & 0 & -1 \\
-1 & 0 & 1 & 0
\end{pmatrix}
$$

**Explanation:**
- The non-diagonal entries correspond to the finite difference approximation of the derivative.
- The factor of $\frac{i}{2 \Delta x}$ ensures that the momentum operator reflects the correct dimensionality.
- The matrix is anti-Hermitian (i.e., $P^\dagger = -P$), as expected for the momentum operator.

- This $4 \times 4$ matrix represents the momentum operator in a discrete system with 4 grid points. The matrix elements link neighboring points, reflecting the nature of the derivative approximation.
:::