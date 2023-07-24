## Operators


We have already seen examples of operators. For short, they consist of mathematical operations that can be carried out on functions. For example, the quantum mechanical momentum operator is:

$${\hat{p}_x = -i\hbar\frac{d}{dx}}$$

- When this operates on a function, it does the following: (1) differentiate the function with respect to $x$ and then (2) multiply the result from (1) by $-i\hbar$. 

- Another example of an operator is the position operator given just by coordinate $x$. This would operate on a given wavefunction just by multiplying it by $x$. We denote operators with \^{} sign (``hat'') above them.

### Linearity of operators
Operators in quantum mechanics are *linear*, which means that they fulfill the following rules:

$${\hat{A}\left(\psi_1 + \psi_2\right) = \hat{A}\psi_1 + \hat{A}\psi_2}$$

$${\hat{A}\left(c\psi\right) = c\hat{A}\psi\textnormal{ where \textit{c} is a constant}}$$

and $\hat{A}$ is a [linear operator](http://en.wikipedia.org/wiki/Operator\#Linear_operators). Operator algebra defines how operators are added, multiplied, etc. For example, adding two operators is equivalent to $\hat{A}_1 + \hat{A}_2$. Multiplication corresponds to them operating one after another.


**Example** Apply the following operators on the given functions:

1. Operator $\hat{A} = d/dx$ and function $x^2$.\\
2. Operator $\hat{A} = d^2/dx^2$ and function $4x^2$.\\
3. Operator $\hat{A} = \left(\partial / \partial y\right)_x$ and function $xy^2$.
4. Operator $\hat{A} = -i\hbar d/dx$ and function $\exp(-ikx)$.
5. Operator $\hat{A} = -\hbar^2 d^2/dx^2$ and function $\exp(-ikx)$.

**Solution**
-  $\hat{A}\left(x^2\right) = \frac{d}{dx}x^2 = 2x$.
- $\hat{A}\left(4x^2\right) = \frac{d^2}{dx^2}\left(4x^2\right) = 8$.
- $\hat{A}\left(xy^2\right) = \left(\frac{\partial}{\partial y}\left(xy^2\right)\right)_x = 2xy$. Note that $x$ is a constant.
-  $\hat{A}\left(e^{-ikx}\right) = -i\hbar\frac{d}{dx}\left(e^{-ikx}\right) = -\hbar ke^{-ikx}$.
- $\hat{A}\left(e^{-ikx}\right) = -\hbar^2\frac{d^2}{dx^2}e^{-ikx} = i\hbar^2k\frac{d}{dx}e^{-ikx} = \hbar^2k^2e^{-ikx}$.

### Eigenvalue problem

$${\hat{H}\psi_i(x,y,z) = E_i\psi_i(x,y,z)}$$

- This is an eigenvalue problem where one needs to determine the eigenfunctions $\psi_i$ and the eigenvalues $E_i$. If $\psi_i$ is an eigenfunction of $\hat{H}$, operating with $\hat{H}$ on it must yield a constant times $\psi_i$.

**Example** What are the eigenfunctions and eigenvalues of operator $d/dx$?

**Solution** Start with the eigenvalue equation:



$${\frac{d}{dx}f(x) = kf(x) \Rightarrow \frac{df(x)}{f(x)} = kdx \textnormal{ (integrate both sides)}}
{\Rightarrow \ln(f(x)) = kx + c\textnormal{ (\textit{k} and \textit{c} are constants)}}
{\Rightarrow f_k(x) = e^ce^{kx} = c'e^{kx}\textnormal{ (\textit{c}' is another constant)}}$$

### Exepctation

The eigenfunctions are $f_k(x)$ with the corresponding eigenvalue given by $k$. In general, for operator $\hat{A}$, the expectation value (quantum mechanical average) is defined as:

$${\left<\hat{A}\right> = \int\psi^*\hat{A}\psi d\tau = \left<\psi\left|\hat{A}\right|\psi\right>}$$

The last ``Bra - Ket'' form is called the [dirac notation](http://en.wikipedia.org/wiki/Dirac_notation). Note that the Bra part always contains the complex conjugation.


If $\psi$ is an eigenfunction of $\hat{A}$ then the expectation value is equal to the corresponding eigenvalue ($a$):

$${\hat{A}\psi = a\psi \Rightarrow \left<\hat{A}\right>=\int\psi^*\underbrace{\hat{A}\psi}_{a\psi} d\tau = a\underbrace{\int\psi^*\psi d\tau}_{=1} = a}$$

Note that operators and eigenfunctions may be complex valued; however, eigenvalues of quantum mechanical operators must be real because they correspond to values obtained from measurements. By allowing wavefunctions to be complex, it is merely possible to store more information in it (i.e., both the real and imaginary parts or ``density and velocity'').

### Hermitian property

Operators that yield real eigenvalues are called [hermitian](http://en.wikipedia.org/wiki/Hermitian_operator) . Operator $\hat{A}$ is Hermitian if it fulfills the following condition for *all* well-behaved functions $\psi_j$ and $\psi_k$:

$${\int\psi^*_j\hat{A}\psi_k d\tau = \int\psi_k\left(\hat{A}\psi_j\right)^*d\tau}$$

Note that this implies that the eigenvalues are real: Let $\psi$ be an eigenfunction of $\hat{A}$ with eigenvalue $a$. Since Eq. (\ref{eq9.38}) applies to all functions, choose $\psi_j = \psi_k = \psi$. Then $\int\psi^*\hat{A}\psi d\tau = a$ and $\int\psi\left(\hat{A}\psi\right)^*d\tau = a^*$. Now Eq. (\ref{eq9.38}) implies that $a = a^*$, which means that $a$ must be real.


**Example** Prove that the momentum operator (in one dimension) is Hermitian.

**Solution**

${\int\limits_{-\infty}^{\infty}\psi_j^*(x)\left(-i\hbar\frac{d\psi_k(x)}{dx}\right)dx}^{\textnormal{}} = -i\hbar\int\limits_{-\infty}^{\infty}\psi_j^*(x)\frac{d\psi_k(x)}{dx}dx = \overbrace{\int\limits_{-\infty}^{\infty}\psi_k(x)\left(i\hbar\frac{d\psi_j^*(x)}{dx}\right)dx}^{\textnormal{integration by parts}}$
$ = {\int\limits_{-\infty}^{\infty}\psi_k(x)\left(-i\hbar\frac{d\psi_j(x)}{dx}\right)^*dx}_{\textnormal{}} \Rightarrow \hat{p}_x\textnormal{ is Hermitian}$.

Note that the wavefunctions approach zero at infinity and thus the boundary term in the integration by parts does not contribute. In 3-D, one would have to use the [Green identities](http://en.wikipedia.org/wiki/Green's_identities).


The Hermitian property can also be used to show that the eigenfunctions ($\psi_j$ and $\psi_k$), which have different eigenvalues (i.e., $a_j$ and $a_k$ with $a_j \ne a_k$; ``non-degenerate''), are orthogonal to each other:

$${\textnormal{LHS: }\int\psi_j^*\hat{A}\psi_kd\tau = \int\psi_j^*a_k\psi_kd\tau = a_k\int\psi_j^*\psi_kd\tau}$$

$${\textnormal{RHS: }\int\psi_k\left(\hat{A}\psi_j\right)^*d\tau = \int\psi_k\left(a_j\psi_j\right)^*d\tau = a_j\int\psi_j^*\psi_kd\tau}$$


Here Hermiticity requires LHS = RHS. If $a_j \ne a_k$, the only way fulfill Eq. (\ref{eq9.38}) is to have:

$${{\left(a_k - a_j\right)}{\ne 0}\int\psi^*_j\psi_kd\tau = 0}$$

Note that if $a_j = a_k$, meaning that the values are [degenerate](http://en.wikipedia.org/wiki/Degenerate_energy_level), this result does not hold.


The product $\hat{A}\hat{B}$ of two operators $\hat{A}$ and $\hat{B}$ are defined as follows:

$${\hat{A}\hat{B}f = \hat{A}\left(\hat{B}f\right)\textnormal{ (\textit{f} is a function)}}$$

In practice, this means that we first operate with $\hat{B}$ and then with $\hat{A}$. Note that the order of multiplication is important because they may not commute ($\hat{A}\hat{B} \ne \hat{B}\hat{A}$; just like for matrices). The commutator of two operators $\hat{A}$ and $\hat{B}$ is defined as:

$${\left[\hat{A},\hat{B}\right]f = \left(\hat{A}\hat{B} - \hat{B}\hat{A}\right)f}$$

If the commutator of $\hat{A}$ and $\hat{B}$ is zero, it means that their order in multiplication (or the operation order, in other words) may be changed. If the commutator is non-zero, the order may not be changed. Operator multiplication is [associative](http://en.wikipedia.org/wiki/Associativity):

$${\hat{A}\hat{B}\hat{C} = \left(\hat{A}\hat{B}\right)\hat{C} = \hat{A}\left(\hat{B}\hat{C}\right)}$$


**Example** Prove that operators $\hat{A} = x$ and $\hat{B} = d/dx$ do not commute (i.e., $\left[\hat{A}, \hat{B}\right] \ne 0$).

**Solution** Let $f$ be an arbitrary well-behaved function. We need to calculate both $\hat{A}\hat{B}f$ and $\hat{B}\hat{A}f$:

$$\hat{A}\hat{B}f = xf'(x)\textnormal{ and } \hat{B}\hat{A}f = \frac{d}{dx}\left(xf(x)\right) = f(x) + xf'(x)$$
$$\left[\hat{A},\hat{B}\right]f = \hat{A}\hat{B}f - \hat{B}\hat{A}f = -f\textnormal{ (remove \textit{f})}$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = -1\textnormal{ (this is non-zero and the operators do not commute)}$$

### Simple rules for commutators


$${\left[A,A\right] = \left[A,A^n\right] = \left[A^n,A\right] = 0}$$

$${\left[A,B\right] = -\left[B,A\right]}$$

$${\left[B+C+...,A\right] = \left[B,A\right] + \left[C,A\right] + ...}$$

$${\left[A,B+C+...\right] = \left[A,B\right] + \left[A,C\right] + ...}$$

$${\left[A+B,C+D\right] = \left[A,C\right] + \left[A,D\right] + \left[B,C\right] + \left[B,D\right]}$$

$${\left[A,B^2\right] = \left[A,B\right]B + B\left[A,B\right]}$$


