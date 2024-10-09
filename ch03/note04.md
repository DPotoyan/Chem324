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

### Operators: A reminder

Operators are denoted by a hat symbol which implies that they encode a mathematical operations that can be carried out on functions. For example, the quantum mechanical momentum operator is:

$${\hat{p}_x = -i\hbar\frac{d}{dx}}$$

- When this operates on a function, it does the following: differentiate the function with respect to $x$ and then  multiply the result from by $-i\hbar$. 

- The quantum mechanical momentum operator of position is:

$$\hat{x} = x$$

- When this operates on a function, it does the following: multiply function by x.


### Linearity of operators: A reminder

Operators in quantum mechanics are *linear*, which means that they fulfill the following rules:

$${\hat{A}\left(\psi_1 + \psi_2\right) = \hat{A}\psi_1 + \hat{A}\psi_2}$$

$${\hat{A}\left(c\psi\right) = c\hat{A}\psi}$$


### Exepctation expression: A reminder

- **Expectation of an bservable** Operators are used to compute average quantities called expectations for the corresponding quantity. E.g average energy, momentum, position. 

$$
{\left < {A}\right> = \int\psi^*\hat{A}\psi d\tau}
$$

- **Special case when wavefunction $\psi$  is an eigenfunction of an operator $\hat{A}$**

$$
{\hat{A}\psi = a\psi \Rightarrow \left<{A}\right>=\int\psi^*\underbrace{\hat{A}\psi}_{a\psi} d\tau = a\underbrace{\int\psi^*\psi d\tau}_{=1} = a}
$$


### Commutations of operators

- From linear algebra we know that order of matrix multiplicaiton matters and that $AB\neq BA$ for two matrices $A$ and B$

- Thus we also ecpect  $\hat{A}\hat{B} \neq \hat{B}\hat{A}$ for two operators acting on some function:

$$
{\hat{A}\hat{B}f = \hat{A}\left(\hat{B}f\right)}
$$

- **The commutator of two operators $[\hat{A}, \hat{B}]$** is defined as:

:::{admonition} **Commutator of operators $\hat{A}$ and $\hat{B}$**
:class: important

$${\left[\hat{A},\hat{B}\right]f = \left(\hat{A}\hat{B} - \hat{B}\hat{A}\right)f}$$
:::

- If the commutator of $\hat{A}$ and $\hat{B}$ is zero, it means that their order in multiplication (or the operation order, in other words) may be changed. If the commutator is non-zero, the order may not be changed. 


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
:class: doprdown

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

### Eigenvalues of hermitian operators are real  

- Note that operators and eigenfunctions may be complex valued; however, **eigenvalues** of quantum mechanical operators **must be real** because they correspond to real values obtained from measurements. 
- By allowing wavefunctions to be complex, it is merely possible to store more information in it (i.e., both the real and imaginary parts or ``density and velocity'')
- When computing experimental quantities complex conjugate pair of wavefunctions must be combined to yield real values. 
- The symmetry of Hermitian operators forces eigenvalues to be real: Let $\psi$ be an eigenfunction of $\hat{A}$ with eigenvalue $a$. Choose $\psi_j = \psi_k = \psi$. Then we can write the result of the left and right hand side of hermitian condition:

$$\int\psi^*\hat{A}\psi d\tau = a$$ 

$$\int\psi\left(\hat{A}\psi\right)^*d\tau = a^*$$ 

Hence $a = a^*$, which means that $a$ must be real!

:::{admonition} **Example** 
:class: note

Prove that the momentum operator (in one dimension) is Hermitian.
:::

:::{admonition} **Solution**
:class: dropdown

${\int\limits_{-\infty}^{\infty}\psi_j^*(x)\left(-i\hbar\frac{d\psi_k(x)}{dx}\right)dx} = -i\hbar\int\limits_{-\infty}^{\infty}\psi_j^*(x)\frac{d\psi_k(x)}{dx}dx = \\ \overbrace{\int\limits_{-\infty}^{\infty}\psi_k(x)\left(i\hbar\frac{d\psi_j^*(x)}{dx}\right)dx}^{{integration\, by\, parts}}$
$ = {\int\limits_{-\infty}^{\infty}\psi_k(x)\left(-i\hbar\frac{d\psi_j(x)}{dx}\right)^*dx} \Rightarrow \hat{p}_x\textnormal{ is Hermitian}$.

Note that the wavefunctions approach zero at infinity and thus the boundary term in the integration by parts does not contribute. In 3-D, one would have to use the [Green identities](http://en.wikipedia.org/wiki/Green's_identities).
:::


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


