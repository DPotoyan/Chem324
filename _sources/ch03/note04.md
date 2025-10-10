# P2 Operators

:::{admonition} What you need to know
:class: note
- For every experimental **observable** there is a **corresponding operator** in quantum mechanics. 
- **Operators must be linear.** Becasue they are dervied from Schrodinger equation which itself is linear.
- **Operatprs must be Hermitian** becasue only Hermitian operators produce real eigenvalues.
- **Operatprs must produce real eigenvalues.** Becasue eigenvalue are the only possible values that are measured in experiments.
- Operators **commutations** show weather two experimental observables can be **measured simulateneously**. E.g can one simulatenoulsy and precisely determine the values of position and momentum of an electron. 
- Commuting operators share eignefunctions, non-commuiting operators have different eigenfunctions.
:::


### Operators

- In quantum mechanics, **operators** represent physical observables and are denoted by a hat symbol ($\hat{}$), which indicates a mathematical operation on functions.

- For example, the momentum operator is differentiating the function with respect to $x$, then multiplies the result by $-i\hbar$.

  $$
  \hat{p}_x = -i\hbar\frac{d}{dx}
  $$

- When this operates on a function, it 

- The position operator simply multiplies the function by $x$.

  $$
  \hat{x} = x
  $$

- In quantum mechanics we use **a simple recepie to find operators**: Take expressions from classical mechancis and replace positions and momentum by their respective operator expressions. 


### Linearity of Operators

- Operators in quantum mechanics are **linear**, meaning they satisfy:

$$
\hat{A}(\psi_1 + \psi_2) = \hat{A}\psi_1 + \hat{A}\psi_2
$$

$$
\hat{A}(c\psi) = c\hat{A}\psi
$$

- Where $c$ is a constant, and $\psi_1$, $\psi_2$, and $\psi$ are wavefunctions.
- $\hat{x}$, $\hat{p_x}$, $\hat{H}$ all satisfy this property 



### Commutations of operators

:::{admonition} **Commutator $\hat{A}$ and $\hat{B}$**
:class: important

$${\left[\hat{A},\hat{B}\right]f = \left(\hat{A}\hat{B} - \hat{B}\hat{A}\right)f}$$
:::

- From linear algebra we know that order of matrix multiplicaiton matters and that $AB\neq BA$ for two matrices $A$ and $B$
- Thus we also generally ecpect  $\hat{A}\hat{B} \neq \hat{B}\hat{A}$ for any two operators. 

- We can quantify relationship between two operators by computing the **Commutator**
    - If the commutator is zero, it means that order in multiplication of operators or matrices can be changed. 
    - If the commutator is non-zero, the order matters and can not be changed! 


:::{admonition} **Example**
:class: note

Prove that operators $\hat{A} = x$ and $\hat{B} = d/dx$ do not commute (i.e., $\left[\hat{A}, \hat{B}\right] \ne 0$).
:::

:::{admonition} **Solution** 
:class: dropdown

Let $f$ be an arbitrary well-behaved function. We need to calculate both $\hat{A}\hat{B}f$ and $\hat{B}\hat{A}f$:

$$
\hat{A}\hat{B}f = xf'(x)\textnormal{ and } \hat{B}\hat{A}f = \frac{d}{dx}\left(xf(x)\right) = f(x) + xf'(x)$$
$$\left[\hat{A},\hat{B}\right]f = \hat{A}\hat{B}f - \hat{B}\hat{A}f = -f$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = -1\textnormal{ (this is non-zero and the operators do not commute)}
$$
:::

#### Simple rules for commutators

$${\left[A,A\right] = \left[A,A^n\right] = \left[A^n,A\right] = 0}$$

- This shows that operators always commuts with itself and its power. Now lets apply this. Would kinetic operator commute with the momentum operator? 

$${\left[A,B\right] = -\left[B,A\right]}$$

- This shows that in comutator order is important. You swap the oeprators in places the sign changes. 


### Commutators and experimental measurements

We have seen previously that operators may not always commute (i.e., $[A, B] \ne 0$). An example of such operator pair is position $\hat{x}$ and momentum $\hat{p}_x$:

$${\hat{p}_x\hat{x}\psi(x) = \hat{p}_x\left(x\psi(x)\right) = \left(\frac{\hbar}{i}\frac{d}{dx}\right)\left(x\psi(x)\right) = \frac{\hbar x}{i}\frac{d\psi(x)}{dx} + \frac{\hbar}{i}\psi(x)}$$

$${\hat{x}\hat{p}_x\psi(x) = x\left(\frac{\hbar}{i}\frac{d\psi(x)}{dx}\right)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right]\psi(x) = \left(\hat{p}_x\hat{x} - \hat{x}\hat{p}_x\right)\psi(x) = \frac{\hbar}{i}\psi(x)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right] = \frac{\hbar}{i}}$$

In contrast, the kinetic energy operator and the momentum operators commute:

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

-  We find that we can not measure precise values of position or momentum simulatneously. 


### Commuting operators and simultaneous measurments

:::{admonition} **Commuting operators share eigenfunction**
:class: important

$$[\hat{A},\hat{B}]=0$$

$$\hat{A}\phi_k = a_k \phi_k$$

$$\hat{B}\phi_k = b_k \phi_k$$

:::

:::{admonition} **Proof that commutation implie shared eigenfunctions**
:class: dropdown

- We will show that if all eigenfunctions of operators $\hat{A}$ and $\hat{B}$ are identical, $\hat{A}$ and $\hat{B}$ commute with each other. 

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

- If opertors commute that means we can **simultaneously measure corresponding observables in a single experiment**. 

- For instance operatos of kinetic energy and momentum commute. We can measure momentum and kinetic energy. But we can not do the same for momentum and position. 

- If we measure observables $A$ and $B$ desribed by a common eigenfunction $\phi_k$ we find the observables to be the corresponding eigenvalues $a_k$ and $b_k$



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
  
* This form is elegant and general—it applies to all quantum systems, independent of the particular representation (position, momentum, etc.).


### Hermitian Property of Operators

* In classical algebra, we often take the **complex conjugate** of a number.
  For matrices, the analog operation is the **adjoint (or conjugate transpose)**.

* The **adjoint** of a matrix or operator $\hat{A}$, denoted $\hat{A}^\dagger$, is obtained by **transposing** the matrix (swapping rows and columns) and **taking the complex conjugate** of each element.

* When a matrix (or operator) is **equal to its own adjoint**, all its **eigenvalues are real**.
  Such matrices or operators are called **Hermitian** (or *self-adjoint*).

:::{admonition} **Hermitian Matrix**
:class: important

$$A = A^\dagger$$

$$a_{jk} = a^*_{kj}$$

Here, $A^\dagger$ is the **conjugate transpose**: first transpose the matrix, then take the complex conjugate of every element.
:::

* In operator language, the adjoint is defined through the **inner product**:
  
$$
  \langle \phi | \hat{A} \psi \rangle = \langle \hat{A}^\dagger \phi | \psi \rangle
$$
  
This means taking the adjoint is like “moving the operator to the other side” of the inner product and **taking a complex conjugate**.

* In the **matrix element form**,
  
$$
a_{jk} = \langle \psi_j | \hat{A} | \psi_k \rangle
$$
  
taking the adjoint gives

$$
  a^*_{kj} = \langle \psi_k | \hat{A}^\dagger | \psi_j \rangle.
$$

- Thus, when $\hat{A}$ is Hermitian we have 

$$a_{jk} = a^*_{kj}$$





:::{admonition} **Hermitian Operator**
:class: important

$$\hat{A} = \hat{A}^\dagger$$

$$
\int {\color{blue} \psi^*_j}  {\color{green}\hat{A}\psi_k} d\tau = \int { \color{green} \psi_k}  {\color{blue}\hat{A}^\dagger\psi_j^{*} } d\tau= \int { \color{green} \psi_k} { {\color{blue}(\hat{A}\psi_j)}^{*}}  d\tau
$$

**In Dirac Notation**

$$ \langle j| \hat{A}|k\rangle = \langle k| \hat{A} | j \rangle^{*}$$
:::


- On the left, $\hat{A}$ acts on $\psi_k$, and the result is integrated against $\psi_j^*$.
- On the right, $\hat{A}^\dagger$ acts on $\psi_j^*$, and the result is integrated against $\psi_k$. 
- **For Hermitian operators** we have special case when $\hat{A} = \hat{A}^\dagger$ and this equation becomes symmetric.
- In general most matrices/operators in mathematics are not Hermitian. Meaning you get different result when you feed complex conjugate function to the same operator. Some examples are below

:::{admonition} **Example of Hermitian Matrix** 
:class: note

Which of these matricies is Hermitian?

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
:class: dropdown

- For the first matrix we have $a_{12}=2\neq a^{*}_{21}=3$, **non-Hermitian**
- For the second matrix $a_{11}\neq a^{*}_{11}=0$, **non-Hermitian**
- For the third matrix  $a_{12}=-3i =a^{*}_{21} = (3i)^{*}=-3i$, **Hermitian**
- For the fourth matrix  $a_{12}=2i \neq a^{*}_{21} = (2i)^{*} = -2i$, **non-Hermitian**

:::

- To see that Differentiation operators are Hermitian requires a little more work.

- A trick that helps see it is integration by parts where the constant term is zero because wavefunction decays to zero at boundaries (postulate 1, keeping probability finite)!

$$\int \psi_1 d\psi_2 =- \int \psi_2d\psi_1 + \psi_1\psi_2\Big|_{x_{min}}^{x_{max}} =- \int \psi_2d\psi_1$$

:::{admonition} **Example of Hermitian Operator** 
:class: note

Prove that the momentum operator (in one dimension) is Hermitian.
:::

:::{admonition} **Solution**
:class: dropdown

${\int\limits_{-\infty}^{\infty}\psi_j^*(x)\left(-i\hbar\frac{d\psi_k(x)}{dx}\right)dx} = -i\hbar\int\limits_{-\infty}^{\infty}\psi_j^*(x)\frac{d\psi_k(x)}{dx}dx = \\ \overbrace{\int\limits_{-\infty}^{\infty}\psi_k(x)\left(i\hbar\frac{d\psi_j^*(x)}{dx}\right)dx}^{{integration\, by\, parts}}$
$ = {\int\limits_{-\infty}^{\infty}\psi_k(x)\left(-i\hbar\frac{d\psi_j(x)}{dx}\right)^*dx} \Rightarrow \hat{p}_x\textnormal{ is Hermitian}$.
:::



### Two Consequences of Hermitian Property

#### Eigenvalues of Hermitian Operators Are Real

- Operators and eigenfunctions in quantum mechanics may be complex valued; however, **eigenvalues** of quantum mechanical operators **must be real** because they correspond to the real values obtained from measurements.
- By allowing wavefunctions to be complex, it is possible to store more information (i.e., both the real and imaginary parts, or "density and velocity").
- When computing experimental quantities, the complex conjugate pair of wavefunctions must be combined to yield real values.
  
- **Proof**: Let $\psi$ be an eigenfunction of $\hat{A}$ with eigenvalue $a$. Choose $\psi_j = \psi_k = \psi$. Then we can write the result of the left-hand and right-hand sides of the Hermitian condition:

$$
\int \psi^* \hat{A} \psi \, d\tau = a
$$

$$
\int \psi \left(\hat{A} \psi\right)^* \, d\tau = a^*
$$

- Since the operator is Hermitian, this leads to equality ensuring real nature of eigenvalues.

$$
a = a^*
$$





#### Eigenfunctions of Hermitian Operators Are Orthogonal

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


### Problems

#### Problem-1: Is $xd/dx$ operator Hermitian

Check weather the operator $\hat{A} = xd/dx$ is Hermitian. 

- You can test weather the following condition holds:

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( x \frac{d}{dx} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

- Note how complex conjugation applies to an expression with an operator inside! 
- But since our operator contains no imaginary number complex conjugation only applies to the wavefunction


:::{admonition} **Solution** 
:class: note, dropdown


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

#### Problem-2: Is $d^2/dx^2$ operator Hermitian?

- You can test weather the following condition holds

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx
$$

- Note how complec conjugation applies to an expression with operator inside. but since our operator contains no imaginary numbers it will only apply to wavefunction


:::{admonition} **Solution** 
:class: note, dropdown

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


#### Problem-3: Is $id^2/dx^2$ operator Hermitian? 

- You can test weather the following condition holds

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx
$$

:::{admonition} **Solution** 
:class: note, dropdown

Fro the last problem we learned that the following condition holds which makes second derivative operator $d^2/dx^2$ hermitian. 

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1^*(x) \right)  \, dx
$$

- Now if we have $id^2/dx^2$ the complex conjugate part will prduce minus sign which breaks the Hermitian equality

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

:::{admonition} **Solution** 
:class: note, dropdown

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

Show how the momentum operator looks in matrix form using a finite-dimensional example where you evaluate wavefunction onf 4 points which will correspond to $4 \times 4$ matrix. 

:::{admonition} **Solution** 
:class: note, dropdown

- We can represent the momentum operator $\hat{p} = -i \hbar \frac{d}{dx}$ in a discrete basis, such as using a position basis. In this case, the matrix elements of the momentum operator can be approximated using finite differences.

- For simplicity, let's assume we are working in a discrete system, where we approximate the derivative $\frac{d}{dx}$ with finite differences. The finite difference approximation for the derivative at point $x_n$ is:

$$
\frac{d \psi(x)}{dx} \approx \frac{\psi(x_{n+1}) - \psi(x_{n-1})}{2 \Delta x}
$$

- where $\Delta x$ is the spacing between the discrete points.

- The corresponding momentum operator matrix in this finite-dimensional space can be written as a skew-symmetric matrix that captures this finite difference behavior.

- Here is an example of a $4 \times 4$ momentum operator matrix $P$, assuming \$\hbar = 1$ for simplicity:

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