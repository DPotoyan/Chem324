
# Multi-electron atoms

:::{admonition} What you need to know

* We approximate many-electron wavefunctions using **hydrogenic orbitals** as building blocks.
* Unlike the hydrogen atom, **multi-electron problems do not separate** and therefore do not admit exact analytical solutions.
* **Spin and antisymmetry** impose strict constraints on allowed electronic wavefunctions.
:::

## Orbital Approximation

:::{figure-md} markdown-fig <img src="./images/HvsHe.png" alt="H vs He" class="bg-primary mb-1" width="500px">
Difference between the hydrogen and helium Hamiltonians that makes multi-electron atoms analytically unsolvable.
:::

* For multi-electron atoms, the Hamiltonian depends on the coordinates of all electrons. The coordinates **cannot be separated**, so the Schrödinger equation is not analytically solvable.
* A practical approximation is to represent the wavefunction as a product of **single-electron orbitals**:

  * These orbitals are obtained computationally (e.g., variationally).

:::{admonition} Orbital Approximation
:class: important

$$
\Psi(r_1, r_2, \ldots, r_n) \approx \phi_1(r_1)\phi_2(r_2)\cdots\phi_n(r_n)
$$

* $\Psi$ is the multi-electron wavefunction.
* Each $\phi_i(r)$ is an **atomic orbital** occupied by one electron.
  :::

## Helium Wavefunction

For helium, the simplest guess would be

$$
\Psi(r_1, r_2) \approx \phi_1(r_1)\phi_2(r_2).
$$

This form, however, suffers from three fundamental issues:

1. **Indistinguishability**
   Electrons are identical; the wavefunction cannot assign “electron 1” to “orbital 1” and “electron 2” to “orbital 2.”

2. **Missing spin information**
   The spatial wavefunction must combine with a spin function so that the **total wavefunction is antisymmetric**.

3. **Neglect of electron–electron correlation**
   The product form assumes electrons move independently, which leads to quantitative errors in energies.



## Issue 1: Indistinguishability and Antisymmetry

Particles such as electrons are indistinguishable. Therefore the probability density must remain unchanged upon interchange:

$$
|\Psi(r_1,r_2)|^2 = |\Psi(r_2,r_1)|^2,
$$

which implies

$$
\Psi(r_1,r_2) = \pm \Psi(r_2,r_1).
$$

Electrons are **fermions**, and Pauli’s principle dictates that their total wavefunction must be **antisymmetric**:

:::{admonition} Antisymmetry Requirement
:class: important

$$
\Psi(\ldots, r_m, \ldots, r_n, \ldots)
= -\Psi(\ldots, r_n, \ldots, r_m, \ldots).
$$

:::

A simple way to generate symmetric/antisymmetric forms for a two-variable function $f(x,y)$:

* Symmetric:

  $$
  g_+(x,y) = f(x,y) + f(y,x)
  $$

* Antisymmetric:

  $$
  g_-(x,y) = f(x,y) - f(y,x)
  $$

For helium, the antisymmetrized spatial wavefunction is

$$
\Psi(r_1,r_2) \propto \phi_1(r_1)\phi_2(r_2) - \phi_1(r_2)\phi_2(r_1).
$$



## Issue 2: Spin Requirement

Electrons have two spin states, $\alpha$ and $\beta$. The **total wavefunction** (spatial × spin) must be antisymmetric:

* If spatial part is **symmetric**, spin part must be **antisymmetric**.
* If spatial part is **antisymmetric**, spin part must be **symmetric**.

Possible two-electron spin combinations:

* Symmetric:

  $$
  \alpha(1)\alpha(2)
  $$

  $$
  \beta(1)\beta(2)
  $$

  $$
  \frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) + \alpha(2)\beta(1)\right]
  $$

* Antisymmetric:

  $$
  \frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) - \alpha(2)\beta(1)\right]
  $$



### Pauli Exclusion Principle

A key result of antisymmetry is the **Pauli Exclusion Principle**:

> **No two electrons can possess identical sets of quantum numbers.**

For helium’s ground state ($1s^2$), the properly antisymmetrized total wavefunction is

$$
\Psi = \frac{1}{\sqrt{2}}
\left[1s(1)1s(2) + 1s(2)1s(1)\right]
\left[\alpha(1)\beta(2) - \alpha(2)\beta(1)\right].
$$



## Slater Determinants

Slater introduced a compact representation of antisymmetric wavefunctions:

$$
\Psi(r_1,\ldots, r_n)
= \frac{1}{\sqrt{n!}}
\begin{vmatrix}
\chi_1(1) & \chi_2(1) & \cdots \
\chi_1(2) & \chi_2(2) & \cdots \
\vdots & \vdots & \ddots
\end{vmatrix},
$$

where each $\chi_i$ is an **orbital × spin** function. For helium ground state:

$$
\Psi = \frac{1}{\sqrt{2}}
\begin{vmatrix}
1s(1)\alpha(1) & 1s(1)\beta(1) \
1s(2)\alpha(2) & 1s(2)\beta(2)
\end{vmatrix}.
$$






## Singlet and Triplet States of Helium

For an excited configuration (e.g., $1s,2s$), the symmetric and antisymmetric spatial combinations are:

$$
\Psi_{\text{sym}} = \frac{1}{\sqrt{2}}\left[1s(1)2s(2) + 1s(2)2s(1)\right],
$$

$$
\Psi_{\text{antisym}} = \frac{1}{\sqrt{2}}\left[1s(1)2s(2) - 1s(2)2s(1)\right].
$$

Combining with spin symmetries:

* Triplet (symmetric spin)
* Singlet (antisymmetric spin)


![](./images/He_exc1.png)

### Action of Spin Operators

- **Triplet:**

$$
\hat{S}_z|\psi_1\rangle = +\hbar|\psi_1\rangle,
\qquad
\hat{S}_z|\psi_2\rangle = 0,
\qquad
\hat{S}_z|\psi_3\rangle = -\hbar|\psi_3\rangle,
$$

$$
\hat{S}^2|\psi_i\rangle = 2\hbar^2|\psi_i\rangle.
$$

- **Singlet:**

$$
\hat{S}_z|\psi_4\rangle = 0,
\qquad
\hat{S}^2|\psi_4\rangle = 0.
$$



### Energies of Multi-Electron States

The Hamiltonian is

$$
\hat{H} = \hat{H}_1 + \hat{H}_2 + \hat{H}_{12},
$$

with $\hat{H}_{12}$ corresponding to electron–electron repulsion.

### Useful Integrals

:::{admonition} **Single-electron energy**
:class: important

$$
I(a) = \int \phi_a^*(r)
\left[
-\frac{\hbar^2}{2m}\nabla^2
- \frac{Ze^2}{4\pi\epsilon_0 r}
\right]
\phi_a(r)\, d\tau
$$

:::


:::{admonition} **Coulomb Integral**
:class: important

$$
J_{ij} =
\int |\phi_i(r_1)|^2
\frac{e^2}{4\pi\epsilon_0 r_{12}}
|\phi_j(r_2)|^2
, d^3r_1, d^3r_2,
$$

always **positive**.
:::

:::{admonition} **Exchange Integral**
:class: important

$$
K_{ij} =
\int \phi_i^*(r_1)\phi_j^*(r_2)
\frac{e^2}{4\pi\epsilon_0 r_{12}}
\phi_j(r_1)\phi_i(r_2),
d^3r_1, d^3r_2.
$$

Positive, but leads to **energy lowering** for triplet states.
:::



### Energies of $1s2s$ Singlet and Triplet

Triplet (antisymmetric spatial):

$$
E_{\text{triplet}} = I(1s) + I(2s) + J(1s,2s) - K(1s,2s)
$$

Singlet (symmetric spatial):

$$
E_{\text{singlet}} = I(1s) + I(2s) + J(1s,2s) + K(1s,2s)
$$

Thus the triplet state is **lower in energy** due to exchange stabilization.

![](./images/He_exc2.png)


# Hund’s Rule and the Aufbau Principle

:::{figure-md} markdown-fig 

<img src="./images/aufbau.png" alt="Aufbau" class="bg-primary mb-1" width="400px">
Aufbau filling pattern for atomic orbitals.

:::

### Aufbau Principle

Electrons fill orbitals in order of increasing energy.

### Pauli Exclusion Principle

Each orbital holds at most two electrons with opposite spins.

### Hund’s Rule

Electrons occupy **degenerate orbitals singly with parallel spins** before pairing. This reflects exchange stabilization.

:::{figure-md} markdown-fig 

<img src="./images/Hund1.png" alt="Hund" class="bg-primary mb-1" width="400px">

Exchange stabilization in the triplet state underlies Hund’s rule.
:::

