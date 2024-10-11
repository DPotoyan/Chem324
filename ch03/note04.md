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


### Operators: A Reminder

In quantum mechanics, **operators** represent physical observables and are denoted by a hat symbol ($\hat{}$), which indicates a mathematical operation on functions.

- For example, the momentum operator is differentiating the function with respect to $x$, then multiplies the result by $-i\hbar$.

  $$
  \hat{p}_x = -i\hbar\frac{d}{dx}
  $$

  When this operates on a function, it 

- The position operator simply multiplies the function by $x$.

  $$
  \hat{x} = x
  $$


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



### Expectation Value: A Reminder

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



### Commutations of operators

- From linear algebra we know that order of matrix multiplicaiton matters and that $AB\neq BA$ for two matrices $A$ and $B$

- Thus we generally ecpect  $\hat{A}\hat{B} \neq \hat{B}\hat{A}$.
- We can quantify relationship between two operators by computing the **Commutator**:

:::{admonition} **Commutator $\hat{A}$ and $\hat{B}$**
:class: important

$${\left[\hat{A},\hat{B}\right]f = \left(\hat{A}\hat{B} - \hat{B}\hat{A}\right)f}$$
:::

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

$${\left[A,B\right] = -\left[B,A\right]}$$

$${\left[A,B^2\right] = \left[A,B\right]B + B\left[A,B\right]}$$

## Commutators and experimental measurements

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


:::{admonition} **Example**  
:class: note

Obtain the position/momentum uncertainty principle 
:::

:::{admonition} **Solution**
:class: dropdown

Denote $\hat{A} = \hat{x}$ and $\hat{B} = \hat{p}_x$. 


$$\frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right| = \frac{1}{2}\left|\left<\left[\hat{x},\hat{p}_x\right]\right>\right| = \frac{1}{2}\left|\left<\frac{\hbar}{i}\right>\right|
= \frac{1}{2}\left|\left<\psi\left|\frac{\hbar}{i}\right|\psi\right>\right| = \frac{1}{2}\left|\frac{\hbar}{i}\underbrace{\left<\psi\left|\psi\right.\right>}_{=1}\right| = \frac{\hbar}{2}$$

$$\Rightarrow \Delta x\Delta p_x \ge \frac{\hbar}{2}$$
:::


### Commuting operators and simultaneous measurments

:::{admonition} **Commuting operators share eigenfunction**
:class: important

$$[\hat{A},\hat{B}]=0$$

$$\hat{A}\phi_k = a_k \phi_k$$

$$\hat{B}\phi_k = b_k \phi_k$$

:::

:::{admonition} **Proof**
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

### Hermitian property of operators 


:::{admonition} **Hermitian Matrix**
:class: important

$$a_{jk} = a^{*}_{kj}$$

:::



:::{admonition} **Hermitian Operator**
:class: important

$$
{\int {\color{blue} \psi^*_j} {\color{green}\hat{A} \psi_k} d\tau = \int { \color{green} \psi_k} {\color{blue} (\hat{A}\psi_j)^{*} } d\tau}
$$

:::


- *Note the symmetry between complex conjugate pair of wavefunctions:* The expression remains the same wether the same operator acts on wavefunction or its complex conjugate pair. 

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

- For the first matrix we have $a_{12}=2\neq a^{*}_{21}=3$, non-Hermitian
- For the second matrix $a_{12}= a^{*}_{21}=0$, Hermitian
- For the third matrix  $a_{12}=-3i =a^{*}_{21} = (3i)^{*}=-3i$, Hermitian
- For the fourth matrix  $a_{12}=2i \neq a^{*}_{21} = (2i)^{*} = -2i$, Hermitian

:::


:::{admonition} **Example of Hermitian Operator** 
:class: note

Prove that the momentum operator (in one dimension) is Hermitian.
:::

:::{admonition} **Solution**
:class: dropdown

${\int\limits_{-\infty}^{\infty}\psi_j^*(x)\left(-i\hbar\frac{d\psi_k(x)}{dx}\right)dx} = -i\hbar\int\limits_{-\infty}^{\infty}\psi_j^*(x)\frac{d\psi_k(x)}{dx}dx = \\ \overbrace{\int\limits_{-\infty}^{\infty}\psi_k(x)\left(i\hbar\frac{d\psi_j^*(x)}{dx}\right)dx}^{{integration\, by\, parts}}$
$ = {\int\limits_{-\infty}^{\infty}\psi_k(x)\left(-i\hbar\frac{d\psi_j(x)}{dx}\right)^*dx} \Rightarrow \hat{p}_x\textnormal{ is Hermitian}$.

Note that the wavefunctions approach zero at infinity and thus the boundary term in the integration by parts does not contribute. In 3-D, one would have to use the [Green identities](http://en.wikipedia.org/wiki/Green's_identities).
:::


### Two conseqeuences of Hermitian property

#### Eigenvalues of Hermitian operator are real  

- Note that operators and eigenfunctions may be complex valued; however, **eigenvalues** of quantum mechanical operators **must be real** because they correspond to real values obtained from measurements. 
- By allowing wavefunctions to be complex, it is merely possible to store more information in it (i.e., both the real and imaginary parts or ``density and velocity'')
- When computing experimental quantities complex conjugate pair of wavefunctions must be combined to yield real values. 
- **Proof** Let $\psi$ be an eigenfunction of $\hat{A}$ with eigenvalue $a$. Choose $\psi_j = \psi_k = \psi$. Then we can write the result of the left and right hand side of hermitian condition:

$$\int\psi^*\hat{A}\psi d\tau = a$$ 

$$\int\psi\left(\hat{A}\psi\right)^*d\tau = a^*$$ 

$$a = a^*$$




#### Eigenfunction of Hermitian operator are orthogonal 

The Hermitian property can also be used to show that the eigenfunctions ($\psi_j$ and $\psi_k$), which have different eigenvalues (i.e., $a_j$ and $a_k$ with $a_j \ne a_k$; ``non-degenerate''), are orthogonal to each other:

$$
{\textnormal{LHS: }\int\psi_j^*\hat{A}\psi_kd\tau = \int\psi_j^*a_k\psi_kd\tau = a_k\int\psi_j^*\psi_kd\tau}
$$

$$
{\textnormal{RHS: }\int\psi_k\left(\hat{A}\psi_j\right)^*d\tau = \int\psi_k\left(a_j\psi_j\right)^*d\tau = a_j\int\psi_j^*\psi_kd\tau}
$$


Here Hermiticity requires LHS = RHS. If $a_j \ne a_k$, then we are dealing with:

$$
{{\left(a_k - a_j\right)}{\ne 0}\int\psi^*_j\psi_kd\tau = 0}
$$

Note that if $a_j = a_k$, meaning that the values are [degenerate](http://en.wikipedia.org/wiki/Degenerate_energy_level), this result does not hold.


