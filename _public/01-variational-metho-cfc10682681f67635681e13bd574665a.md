---
kernelspec:
  name: python3
  display_name: Python 3
---

# Variational Method

:::{note} **What you will learn**

- **Why we need approximations:** The Schrodinger equation can be solved analytically only for a handful of simple systems. The hydrogen atom is the most complex atomic case with a closed-form solution; helium and any multi-electron system are intractable.
- **The variational theorem:** For any trial wavefunction, the computed energy is always greater than or equal to the true ground-state energy. This gives a rigorous upper bound and a way to rank approximations.
- **Trial functions and parameters:** Start from an educated guess for the wavefunction, then tune its parameters to minimize the energy and approach the exact value.
- **Worked examples:** Particle in a box, the hydrogen atom with Gaussian trial functions, and the helium atom with an effective nuclear charge.
- **The linear variational method:** Expanding the trial function in a basis set turns a hard differential-equation problem into a tractable linear algebra problem, where we solve for eigenvalues and eigenvectors of a matrix. This idea underlies electronic-structure methods such as Hartree-Fock.
:::

## Why approximations are needed

- The Schrodinger equation can be solved analytically only for simple systems.
- For atomic systems, the hydrogen atom represents the most complex case with an analytical solution.
- For systems with multiple interacting electrons, such as the helium atom or other multi-electron systems, analytical solutions become intractable.
- Approximation methods are therefore essential for finding solutions to complex quantum systems. These methods let us estimate solutions and evaluate how close the approximate results are to the true values.

The variational method provides a systematic approach for making approximations and a quantitative way to assess the convergence of predictions toward exact values. Its core idea is simple:

- Begin with an educated guess by selecting a trial function to represent the wavefunction of the system.
- Adjust the parameters of the trial function to minimize the energy, bringing the solution closer to the exact value.

## Variational theorem

- The variational method states that for any trial (approximate) function $|\phi\rangle$, the computed energy always comes out greater than or equal to the exact (true) ground-state energy.

:::{important} **Variational Theorem of Quantum Mechanics**

$$
E_{\phi}=\frac{\langle \phi \mid \hat{H}  \mid \phi\rangle}{\langle \phi \mid \phi\rangle} \geq E_0
$$

- $\hat{H}$ is the Hamiltonian of the problem we want to solve.
- $|\phi\rangle$ is a trial wavefunction with unknown parameters we want to determine.
- $E_0$ is the true ground-state energy, which is generally not known to us.
:::

- When the trial wavefunction is not normalized, we divide by $\langle \phi \mid \phi\rangle$. The expression simplifies when the trial function is normalized beforehand, so that $\langle \phi \mid \phi\rangle=1$.
- If the true ground-state wavefunction $\psi_0$ is inserted in place of the trial function, the equality is reached. For all other (trial) wavefunctions the energy expectation value on the left side will always be larger. The ratio is also called the Rayleigh ratio.

### Consequences of the variational theorem

1. **Ground-state energy is the lowest possible energy for the system.**
2. **By minimizing the energy functional we obtain the most accurate prediction for a given trial function.**
3. **More parameters give us more handles to vary, and hence more accurate solutions.**

## Worked examples

:::{note} **Example: Particle in a box**

Consider the one-dimensional particle in a box (boundaries at $0$ and $a$). Use the variational theorem to obtain an upper bound for the ground-state energy using the following normalized trial wavefunction:

$$\psi_t(x) = \frac{\sqrt{30}}{a^{5/2}}x(a - x)$$
:::

:::{admonition} **Solution:**
:class: dropdown solution

Clearly this is not the correct ground-state wavefunction. First we check that it satisfies the boundary conditions: $\psi_t(0) = 0$ and $\psi_t(a) = 0$ (OK). The Hamiltonian for this problem is:

$$\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}, \quad 0\le x\le a$$

Plugging both the Hamiltonian and $\psi_t$ into the energy expression gives:

$$\int_0^a\psi_t^*\hat{H}\psi_t \, d\tau = -\frac{30\hbar^2}{2a^5m}\int_0^a\left( ax - x^2\right)\frac{d^2}{dx^2}\left( ax - x^2\right)dx$$

$$= \frac{30\hbar^2}{a^5m}\int_0^a\left( ax-x^2\right) dx = \frac{5\hbar^2}{a^2m}\ge E_1$$

As indicated, this gives an upper limit for the ground-state energy $E_1$.
:::

:::{note} **Example: Hydrogen atom with a Gaussian trial function**

- The exact solution for the ground state is $\psi(r)=\frac{1}{(\pi a^3_0)^{1/2}}e^{-r/a_0}$ with $E_1 = -0.5 \, h$ (in Hartree atomic units).
- Use a trial function $\phi=e^{-\alpha r^2}$ to predict the ground-state energy.
:::

:::{admonition} **Solution:**
:class: dropdown solution

Plug the trial function into the energy expression, computing the energy as a function of the parameter $\alpha$:

$$
E_{trial} = \frac{\langle \phi \mid \hat{H}  \mid \phi\rangle}{\langle \phi \mid \phi\rangle}
$$

$$
E_{trial}(\alpha) = \frac{4\pi \int^{\infty}_0  e^{-\alpha r^2}\left[-\frac{\hbar^2}{2\mu}\nabla_r^2 -\frac{e^2}{4\pi \epsilon_0 r}\right] e^{-\alpha r^2} \, r^2 dr }{4\pi \int^{\infty}_0 e^{-2\alpha r^2} r^2 dr}
$$

$$
E_{trial}(\alpha)=\frac{3\hbar^2 \alpha}{2m_e}-\frac{e^2 \alpha^{1/2}}{\sqrt{2}\epsilon_0 \pi^{3/2}}
$$

Minimization with respect to the parameter $\alpha$ gives the best value of the energy:

$$
\frac{\partial E_{trial}(\alpha)}{\partial \alpha} = 0
$$

$$
\alpha_{min} = \frac{m_e e^4}{18 \pi^3 \epsilon^2_0 \hbar^4}
$$

Finally, we plug this parameter back into the energy function to obtain the energy minimized with respect to $\alpha$, that is $E(\alpha_{min})$:

$$
E_0 = -0.5 \, h, \qquad E_{trial}(\alpha_{min}) = -0.424
$$

This is about 15% error. Not too bad for a start. Adding more parameters and functions will reduce the error.
:::

## The helium atom is tough

- The Schrodinger equation for the helium atom is already extremely complicated mathematically. No analytic solution to this equation has been found. However, with certain approximations, useful results can be obtained. The Hamiltonian for the He atom can be written as:

$${\hat{H} = \underbrace{-\frac{\hbar^2}{2m_e}\left(\Delta_1 + \Delta_2\right)}_{\textnormal{Kinetic energy}}
\underbrace{- \frac{1}{4\pi\epsilon_0}\left(\frac{Ze^2}{r_1} + \frac{Ze^2}{r_2} \overbrace{- \frac{e^2}{r_{12}}}^{\textnormal{Tough!}}\right)}_{\textnormal{Potential energy}}}$$

- Here $\Delta_1$ is the Laplacian for the coordinates of electron 1 and $\Delta_2$ for electron 2; $r_1$ is the distance of electron 1 from the nucleus, $r_2$ the distance of electron 2 from the nucleus, and $r_{12}$ the distance between electrons 1 and 2. For the He atom $Z = 2$.

### Independent-electron approximation

- Ignore the tough term containing $r_{12}$. In this case the Hamiltonian becomes a sum of two hydrogen-like atoms:

$${\hat{H} = \hat{H}_1 + \hat{H}_2}$$

$${\hat{H}_1 = -\frac{\hbar^2}{2m_e}\Delta_1 - \frac{Ze^2}{4\pi\epsilon_0r_1}}$$

$${\hat{H}_2 = -\frac{\hbar^2}{2m_e}\Delta_2 - \frac{Ze^2}{4\pi\epsilon_0r_2}}$$

- Because the Hamiltonian is a sum of two independent parts, the Schrodinger equation separates into two (each a hydrogen-like atom equation):

$${\hat{H}_1\psi(r_1) = E_1\psi(r_1)}$$
$${\hat{H}_2\psi(r_2) = E_2\psi(r_2)}$$

The total energy is a sum of $E_1$ and $E_2$, and the total wavefunction is a product of $\psi(r_1)$ and $\psi(r_2)$. Based on our previous wavefunction table for hydrogen-like atoms:

$${E = E_1 + E_2 = -RZ^2\left(\frac{1}{n_1^2} + \frac{1}{n_2^2}\right)}$$

$${\psi(r_1)\psi(r_2) = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_1/a_0}\frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_2/a_0}
=\frac{1}{\pi}\left(\frac{Z}{a_0}\right)^3e^{-Z(r_1 + r_2)/a_0}}$$

### Consequences of the independent-electron approximation

- For a ground-state He atom both electrons reside in the lowest-energy orbital, so the total wavefunction is $\psi(r_1,r_2) = \psi(r_1)\psi(r_2) = \psi(1)\psi(2) = 1s(1)1s(2)$. The energy from this approximation is not sufficiently accurate (it misses electron-electron repulsion), but the wavefunction is useful for qualitative analysis. The variational principle gives a systematic way to assess how good our approximation is.
- The exact ground-state energy has been found (by very extensive analytic and numerical calculations) to be $-79.0$ eV. Using the approximate wavefunction, we can calculate the expectation value of the energy. This yields $-74.8$ eV, so the error in energy for this wavefunction is $5.2$ eV. Note that the approximate value is, in accordance with the variational principle, higher than the true energy.

### A better approximation

- We take the wavefunction from the previous step and use the nuclear charge $Z$ as a variational parameter. The variational principle states that minimizing the energy expectation value with respect to $Z$ should approach the true value from above (but will not reach it).
- The obtained value of $Z$ is less than the true $Z$ (= 2). This can be understood in terms of electrons shielding the nucleus from each other, giving a reduced effective nuclear charge.

$${E = \langle\psi |\hat{H}|\psi\rangle = ... = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}}$$

- To minimize this expression we differentiate with respect to $Z$ and set it to zero (the extremum here is clearly a minimum):

$${\frac{dE}{dZ} = \left(2Z - \frac{27}{8}\right)\frac{e^2}{4\pi\epsilon_0a_0} = 0}$$

- This gives $Z = 27/16 \approx 1.7$ and $E \approx -77.5$ eV (compared with $-74.8$ eV before and $-79.0$ eV exact). This result could be improved by adding more terms and variables to the trial wavefunction. For example, higher hydrogen-like orbitals with appropriate variational coefficients would yield a much better result.

## The linear variational method

- How does the variational method scale to harder problems in practice? If we cannot solve for $\psi$ exactly, we can expand the wavefunction in a convenient **basis set** $f_n$ (a set of functions indexed by $n$, like a Fourier series) and tune the expansion to get as close as possible to the true energy and wavefunction.

$$\phi(r) = \sum_n^N c_nf_n(r)$$

- With an infinite number of basis functions we could in principle approximate any function and obtain a nearly exact numerical solution. Computationally this is not feasible, so we truncate the expansion to a finite number $N$ of basis functions and minimize the energy with respect to the coefficients $c_n$.
- Using a linear combination of trial functions transforms a difficult quantum-mechanics problem into a more tractable linear algebra task: instead of solving differential equations for eigenfunctions and eigenvalues, we solve for the eigenvalues and eigenvectors of a matrix.

### A two-function example

- We illustrate the idea and the general matrix construction with a simple example of two basis functions ($N=2$):

$$\phi = c_1f_1 + c_2f_2$$

- There is no need to define these functions explicitly yet, so we leave them as generic functions $f_1$ and $f_2$. The energy is:

$$E_\phi = \frac{\langle\phi|\hat{H}|\phi\rangle}{\langle\phi|\phi\rangle} = \frac{\langle c_1f_1 + c_2f_2|\hat{H}|c_1f_1 + c_2f_2 \rangle}{\langle c_1f_1 + c_2f_2|c_1f_1 + c_2f_2 \rangle}$$

- Expanding the brackets, the numerator and denominator are built from two kinds of matrix elements, the **Hamiltonian matrix** elements $H_{ij}$ and the **overlap matrix** elements $S_{ij}$:

$$H_{ij} = \langle f_i|\hat{H}|f_j\rangle, \qquad S_{ij} = \langle f_i|f_j\rangle$$

so that

$$E_\phi = \frac{c_1^2 H_{11} + 2 c_1 c_2 H_{12} + c_2^2 H_{22}}{c_1^2 S_{11} + 2 c_1 c_2 S_{12} + c_2^2 S_{22}}$$

### Minimization leads to a generalized eigenvalue problem

- Since $E_\phi \geq E_0$ for any trial function $\phi$, we minimize $E_\phi$ by varying the parameters $c_1$ and $c_2$.
- Minimizing with respect to $c_1$ means differentiating $E_\phi$ with respect to $c_1$ and setting the derivative to zero:

$$\frac{\partial E_\phi}{\partial c_1} = 0 = c_1(H_{11} - ES_{11}) + c_2(H_{12} - ES_{12})$$

- Minimizing with respect to $c_2$ gives:

$$\frac{\partial E_\phi}{\partial c_2} = 0 = c_1(H_{12} - ES_{12}) + c_2(H_{22} - ES_{22})$$

- These two coupled linear equations can be written compactly as a matrix equation:

:::{important} **Linear variational (generalized eigenvalue) problem**

$$
\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}
$$

$$
\begin{bmatrix} H_{11} & H_{12} \\ H_{12} & H_{22} \end{bmatrix}
\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}
= E
\begin{bmatrix} S_{11} & S_{12} \\ S_{12} & S_{22} \end{bmatrix}
\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}
$$

- $\mathbf{H}$ is the Hamiltonian matrix with elements $H_{ij} = \langle f_i|\hat{H}|f_j\rangle$.
- $\mathbf{S}$ is the overlap matrix with elements $S_{ij} = \langle f_i|f_j\rangle$.
- The lowest eigenvalue $E$ is the variational estimate of the ground-state energy; the corresponding eigenvector $\mathbf{c}$ gives the best coefficients.
:::

- A nontrivial solution exists only when the secular determinant vanishes, $\det(\mathbf{H} - E\,\mathbf{S}) = 0$. Solving this determinant gives the variational energies. For an orthonormal basis ($\mathbf{S} = \mathbf{I}$) this reduces to the ordinary eigenvalue problem $\mathbf{H}\mathbf{c} = E\mathbf{c}$.

:::{tip} **Worked example: particle in a box by linear variation**
:class: dropdown

Consider a free particle in 1D bound to $0\leq x\leq a$, with Hamiltonian $\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$. Although we can solve this analytically, it is instructive to see the variational solution. We approximate $\psi(x)$ as an expansion in two basis functions $f_1=x(a-x)$ and $f_2=x^2(a-x)^2$:

$$\psi(x) \approx c_1x(a-x) + c_2x^2(a-x)^2$$

Computing the matrix elements (by integrating each $\langle f_i|\hat{H}|f_j\rangle$ and $\langle f_i|f_j\rangle$ over $0\le x\le a$) gives:

$$\mathbf{H} = \frac{\hbar^2a^3}{m} \begin{bmatrix} \frac{1}{6} & \frac{a^2}{30}\\ \frac{a^2}{30} & \frac{a^4}{105} \end{bmatrix}, \qquad
\mathbf{S} = \frac{a^5}{10} \begin{bmatrix} \frac{1}{3} & \frac{a^2}{14}\\ \frac{a^2}{14} & \frac{a^4}{63} \end{bmatrix}$$

Solving the generalized eigenvalue problem (with $a = \hbar = m = 1$) gives a lowest energy of

$$E_\phi = 4.9349 \, \frac{\hbar^2}{m}$$

which is essentially the exact analytic value $E_1 = \frac{\pi^2\hbar^2}{2} \approx 4.9348 \, \frac{\hbar^2}{m}$. The variational solution captures both the energy and the shape of the ground-state wavefunction. See the demo notebooks at the end of this chapter for the full calculation and plots.
:::

## Problems

#### Problem 1

::::{admonition} **Problem 1: Hydrogen atom by variation**
:class: note

Use the variational principle to obtain the lowest-energy solution to the hydrogen atom Schrodinger equation in spherical coordinates using the following trial wavefunctions:

- (a) $\psi_{trial} = e^{-kr}$ with $k$ as a variational parameter.
- (b) $\psi_{trial} = e^{-kr^2}$ with $k$ as a variational parameter.
- (c) Which trial function gives the better (lower) energy?

Both trial functions depend only on $r$, so the angular terms drop out of the Laplacian. You may find the following integrals useful:

$$\int_0^\infty x^ne^{-ax}dx = \frac{n!}{a^{n+1}}, \qquad \int_0^\infty x^me^{-ax^2}dx = \frac{\Gamma[(m + 1)/2]}{2a^{(m + 1) / 2}}$$

$$\Gamma[n + 1] = n!, \qquad \Gamma[n + 1] = n\Gamma[n], \qquad \Gamma\left[\frac{1}{2}\right] = \sqrt{\pi}$$

:::{admonition} **Solution:**
:class: dropdown solution

Use the variational principle and employ spherical coordinates in the integrations:

$$E = \frac{\int\psi^*_{trial}H\psi_{trial}d\tau}{\int\psi^*_{trial}\psi_{trial}d\tau}$$

**(a)** Normalization integral:

$$\int\psi^*_{trial}\psi_{trial}d\tau = \int_0^\infty e^{-2kr}
\underbrace{4\pi r^2dr}_{d\tau} = 4\pi\int_0^\infty r^2e^{-2kr}dr
= \frac{\pi}{k^3}$$

Energy numerator:

$$\int\psi_{trial}^*H\psi_{trial}d\tau = \int\left( e^{-kr}\right)
\left( -\frac{\hbar^2}{2m_e}\Delta - \frac{e^2}{4\pi\epsilon_0r}\right)
\left( e^{-kr}\right)d\tau$$

$$= -\frac{4\pi\hbar^2}{2m_e}\int_0^\infty e^{-2kr}(r^2k^2 - 2kr)dr
- \frac{e^2}{\epsilon_0}\int_0^\infty re^{-2kr}dr$$

$$= -\frac{\pi\hbar^2}{2m_ek} + \frac{\pi\hbar^2}{m_ek}
- \frac{e^2}{4k^2\epsilon_0}$$

Dividing numerator by denominator:

$$E = \frac{\hbar^2k^2}{2m_e} - \frac{e^2k}{4\pi\epsilon_0}$$

Minimize with respect to $k$:

$$\frac{dE}{dk} = \frac{\hbar^2k}{m_e} - \frac{e^2}{4\pi\epsilon_0} = 0
\Rightarrow k = \frac{m_ee^2}{4\pi\epsilon_0\hbar^2} \Rightarrow
E = -\frac{1}{2}\frac{m_ee^4}{(4\epsilon_0)^2\hbar^2} = -hcR$$

where $R$ is the Rydberg constant. This trial function recovers the exact ground-state energy because it has the correct functional form.

**(b)** The logic is identical. The normalization integral is

$$\int\psi^*_{trial}\psi_{trial}d\tau = \frac{4\pi\Gamma[3/2]}{2(2k)^{3/2}}
= \frac{\pi^{3/2}}{(2k)^{3/2}}$$

The Laplacian of the Gaussian is

$$\Delta\psi_{trial} = \left( 4k^2r^2 - 6k\right) e^{-kr^2}$$

Carrying out the integrals gives the energy

$$E = \frac{3\hbar^2k}{2m_e} - \frac{e^2\sqrt{k}}{\sqrt{2}\pi^{3/2}\epsilon_0}$$

Minimizing,

$$\frac{\partial E}{\partial k} = \frac{3\hbar^2}{2m_e} - \frac{e^2}{2\sqrt{2}\pi^{3/2}\epsilon_0\sqrt{k}} = 0
\Rightarrow k = \frac{m_e^2e^4}{18\pi^3\epsilon_0^2\hbar^4}$$

and the total energy at this point is

$$E = -\frac{m_ee^4}{12\pi^3\epsilon_0^2\hbar^2} = -\frac{8}{3\pi}hcR \approx -0.85\,hcR$$

**(c)** The function in (a) gives the lower energy ($-1.0\,hcR$ versus $-0.85\,hcR$) and is therefore the better trial function. The exponential has the correct cusp at the origin, while the Gaussian does not.
:::
::::

#### Problem 2

::::{admonition} **Problem 2: Why is the bound always from above?**
:class: note

Expand an arbitrary normalized trial function in the exact eigenbasis of $\hat{H}$, $|\phi\rangle = \sum_n a_n |\psi_n\rangle$ with $\hat{H}|\psi_n\rangle = E_n|\psi_n\rangle$ and $E_0 \le E_1 \le E_2 \le \dots$. Show that $\langle \phi|\hat{H}|\phi\rangle = \sum_n |a_n|^2 E_n \ge E_0$, and state the condition under which equality holds.

:::{admonition} **Solution:**
:class: dropdown solution

Because the $|\psi_n\rangle$ are orthonormal,

$$\langle \phi|\hat{H}|\phi\rangle = \sum_{n,m} a_m^* a_n \langle \psi_m|\hat{H}|\psi_n\rangle = \sum_{n,m} a_m^* a_n E_n \delta_{mn} = \sum_n |a_n|^2 E_n.$$

Normalization gives $\sum_n |a_n|^2 = 1$. Since every $E_n \ge E_0$,

$$\sum_n |a_n|^2 E_n \ge \sum_n |a_n|^2 E_0 = E_0.$$

Equality holds only when all the weight is on the ground state, $|a_0|^2 = 1$ and $a_{n\neq 0} = 0$, that is when the trial function equals the exact ground-state wavefunction.
:::
::::

#### Problem 3

::::{admonition} **Problem 3: Effective nuclear charge of helium**
:class: note

Using the helium trial energy $E(Z) = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}$, confirm that the optimal effective nuclear charge is $Z = 27/16$ and explain physically why $Z < 2$.

:::{admonition} **Solution:**
:class: dropdown solution

Set the derivative to zero:

$$\frac{dE}{dZ} = \left(2Z - \frac{27}{8}\right)\frac{e^2}{4\pi\epsilon_0a_0} = 0 \Rightarrow Z = \frac{27}{16} \approx 1.69.$$

The effective charge is less than the true $Z = 2$ because each electron partially screens the nucleus from the other. From the viewpoint of one electron, the nuclear charge appears reduced by the average presence of the second electron, so the optimal variational charge is smaller than the bare value.
:::
::::

#### Problem 4

::::{admonition} **Problem 4: Linear variation with an orthonormal basis**
:class: note

In the linear variational method, the trial energy satisfies $\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}$. Show that if the basis functions are orthonormal ($\mathbf{S} = \mathbf{I}$), this reduces to an ordinary eigenvalue problem, and explain what the eigenvalues and eigenvectors represent.
::::

#### Problem 5

::::{admonition} **Problem 5: Secular determinant for two states**
:class: note

For a two-function basis with $H_{11} = \alpha$, $H_{22} = \alpha$, $H_{12} = \beta$, and an orthonormal basis ($S_{11} = S_{22} = 1$, $S_{12} = 0$), solve the secular determinant $\det(\mathbf{H} - E\mathbf{I}) = 0$ and show that the two variational energies are $E_\pm = \alpha \pm \beta$. (This is the bonding and antibonding splitting of two identical atomic orbitals.)
::::
