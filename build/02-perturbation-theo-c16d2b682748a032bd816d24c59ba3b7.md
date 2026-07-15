---
kernelspec:
  name: python3
  display_name: Python 3
---

# Perturbation Theory

:::{note} **What you will learn**

- **The big idea:** Perturbation theory attacks analytically intractable problems by splitting the Hamiltonian into an exactly solvable part $\hat{H}^0$ and a small perturbation $\hat{H}^1$. It is the quantum analog of a Taylor expansion: the key is finding the small parameter to expand in.
- **How it works:** Expand the energies and eigenfunctions as power series in a bookkeeping parameter $\lambda$, then collect terms order by order to get corrections of increasing order. In practice the first- and second-order corrections are usually enough for quantitatively accurate results.
- **The master formula:** Perturbation theory lets us write all corrections entirely in terms of the eigenfunctions and eigenvalues of the exactly solved problem, through matrix elements $H_{nk} = \langle n^0|\hat{H}^1|k^0\rangle$.
- **Where it shows up:** Hydrogen in a magnetic field, spin-orbit coupling, a shifted particle in a box, the anharmonic oscillator, and a perturbative picture of chemical bonding.
:::

## The idea behind perturbation theory

- Perturbation theory attempts to solve analytically intractable problems by identifying an exactly *solvable* part and a *small* perturbation to it.
- The method is similar in spirit to the Taylor expansion of continuous functions familiar from calculus. Just as in a Taylor expansion, the key is identifying the relatively small parameter in the problem to expand in.
- Application of perturbation theory proceeds in two steps. Step one: identify the solvable part and the perturbation. Step two: expand the energy and eigenfunctions as a series of corrections of increasing order. In practice the first- and second-order corrections to the energy are sufficient to get quantitatively accurate results.
- Perturbation theory allows us to write down expressions entirely in terms of the eigenfunctions and eigenvalues of the exactly solved problem.

:::{figure} images/perturb1.png
:alt: perturbation of energy levels
:width: 300px

Fig.1 Perturbation theory quantifies how much the energy levels shift when a small deviation is added to an exactly solvable Hamiltonian. For many problems that are impossible to solve exactly, one can still identify part of the Hamiltonian as exactly solvable, $\hat{H}^0$, with the rest treated as a perturbation.
:::

## Time-independent perturbations

- We start with a Hamiltonian $\hat{H}^0$ for some exactly solvable problem, such as a particle in a box, a harmonic oscillator, and so on:

$$
\hat{H}^0 \mid n^0\rangle=E^0_n \mid n^0\rangle
$$

- The $0$ superscript indicates the exactly solvable Hamiltonian, its eigenfunctions, and its eigenvalues. The state $\mid n^0\rangle$ is the eigenfunction corresponding to the $n$-th eigenvalue $E^0_n$.
- Consider a problem whose Hamiltonian is similar to an exactly solvable one, differing only by a small perturbation $\hat{H}^1$. "Small" means the eigenvalue shifts of the two systems are small relative to the level spacing.
- The parameter $\lambda$ turns the perturbation on ($\lambda=1$) and off ($\lambda=0$):

$$
\hat{H}=\hat{H}^0+\lambda {\hat{H}^1}
$$

- The objective of perturbation theory is to solve the new problem, expressing everything in terms of the eigenvalues and eigenfunctions of the exactly solvable problem:

$$
\hat{H}\mid n\rangle =E_n \mid n\rangle
$$

### It is just like a Taylor expansion

- We assume that the eigenvalues and eigenfunctions can be expanded in a power series in the parameter $\lambda$, which is set to $1$ in the end:

$$
E_n ={\color{green}E^0_n}+{\color{red}\lambda E^1_n}+{\color{blue}\lambda^2 E^2_n}+...
$$

$$
\mid n\rangle = {\color{green}\mid n^0\rangle}+{\color{red} \lambda\mid n^1\rangle}+{\color{blue} \lambda^2\mid n^2\rangle} ...
$$

- Plugging the expansions into $\hat{H}\mid n\rangle =E_n \mid n\rangle$ gives an expression with various powers of $\lambda$. The next step is to expand the brackets and group terms according to $\lambda^0$, $\lambda^1$, and $\lambda^2$:

$$
\Big({\color{green}\hat{H}^0}+{\color{red}\lambda \hat{H}^1} \Big)\Big({\color{green}\mid n^0\rangle}+{\color{red}\lambda\mid n^1\rangle} +{\color{blue}\lambda^2\mid n^2\rangle}\Big)  = \Big({\color{green}E^0_n}+{\color{red}\lambda E^1_n}+{\color{blue}\lambda^2 E^2_n}\Big) \Big({\color{green}\mid n^0\rangle}+{\color{red}\lambda\mid n^1\rangle}+{\color{blue}\lambda^2\mid n^2\rangle}\Big)
$$

### Perturbation equations of order 0, 1, and 2

- Opening the brackets and collecting different orders of $\lambda$, we get the zeroth-, first-, and second-order perturbation equations:

$$
\color{green}{\hat{H}^0\mid n^0\rangle = E^0_n\mid n^0 \rangle}
$$

$$
\color{red}{\hat{H}^0\mid n^1\rangle +\hat{H}^1\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle}
$$

$$
\color{blue}{\hat{H}^0\mid n^2\rangle+\hat{H}^1\mid n^1\rangle = E^0_n\mid n^2 \rangle + E^1_n\mid n^1 \rangle+E^2_n\mid n^0 \rangle}
$$

- Note how **the sum of the superscript indices determines** the order of the perturbation expansion.
- The **zeroth order is just the exact solution.**
- The **Hamiltonian only has a first-order term**, while the eigenfunctions and eigenvalues are expanded to infinitely many terms. Usually going to second order is enough for most problems.

## Computing perturbation corrections to energy levels

:::{important} **Perturbation approximation to energies**

$$
{E_n = \color{green}{E^0_n} + \color{red}{H_{nn}} + \color{blue}{\sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}}}
$$

- $n$ and $k$ are quantum numbers running from ground to excited states, $n=0,1,2,\dots$
- **Matrix elements of the perturbation:**

$$\color{red} H_{nk}=\langle n^0\mid \hat{H}^1\mid k^0\rangle$$

$$\color{blue} H_{nn}=\langle n^0\mid \hat{H}^1\mid n^0\rangle$$
:::

:::{tip} **Example: first- and second-order corrections to the ground state**
:class: dropdown

- The **first-order correction to the ground state** requires computing the **diagonal** matrix element only:

$$E_0^{(1)}  = \langle 0|\hat{H}^1|0\rangle$$

- The **second-order correction to the ground state** requires the **off-diagonal** elements $H_{0k}$, where $n=0$ and $k$ runs over all excited states:

$$E_0^{(2)} = {\sum_{k \neq 0} \frac{\mid H_{0k}\mid^2}{E^0_0-E^0_k}}$$

- The denominator of the second-order term involves the difference between the energy of the given state $E_n$ and all other states $E_k$ (the summation index).
- **Key insight:** if the matrix elements are of comparable magnitude, neighboring energy levels make the larger contributions to the perturbation expression, because their small energy denominators amplify the term.
:::

## Derivations of the first- and second-order corrections

:::{admonition} **Deriving the first-order energy correction $E^1_n$**
:class: dropdown

**Fixing the normalization.** If the zeroth-order eigenfunctions are normalized, the unperturbed eigenfunction is orthogonal to all higher-order corrections:

$$
\langle n^0 \mid n^0 \rangle=1
$$

$$
\langle n^0\mid n\rangle = \langle n^0\mid n^0\rangle + \lambda\langle n^0\mid n^1\rangle=1+0+...
$$

$$
\langle n^0 \mid n^{k} \rangle=0, \quad k=1,2,\dots
$$

**Using the orthogonality.** Start from the first-order perturbation equation:

$$
{\hat{H}^0\mid n^1\rangle +\hat{H}^1\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle}
$$

Multiply by $\langle n^0 \mid$ and use the Hermitian property of the Hamiltonian:

$$
{{\langle n^0} \mid \hat{H}^0\mid n^1\rangle +{\langle n^0} \mid  \hat{H}^1\mid n^0\rangle = E^0_n{\langle n^0} \mid n^1 \rangle+E^1_n {\langle n^0} \mid n^0 \rangle}
$$

The first terms on each side cancel by orthogonality, since $\langle n^0 \mid \hat{H}^0\mid n^1\rangle = E^0_n \langle n^0 \mid n^1\rangle = 0$.

**First-order correction.** We obtain the central result of perturbation theory, the first-order correction to the energy:

$$
\color{red}{E_n^1 = \langle n^0 \mid \hat{H}^1\mid n^0 \rangle}
$$

$$
\boxed{E_n=\color{green}{E^0_n}+\color{red}{E^1_n}=\color{green}{E^0_n}+\color{red}{\langle n^0 \mid \hat{H}^1\mid n^0 \rangle}}
$$

- This expression looks like an expectation value but is different: the eigenfunctions of $\hat{H}^0$ sandwich the perturbation $\hat{H}^1$. The two Hamiltonians in general do not share eigenfunctions.
:::

:::{admonition} **Deriving the first-order correction to the eigenfunction $\mid n^1 \rangle$**
:class: dropdown

We express the unknown first-order eigenfunction $\mid n^1 \rangle$ in terms of the known eigenfunctions $\mid k^0 \rangle$, which form a complete basis set because $\hat{H}^0$ is Hermitian:

$$
\mid n^1 \rangle = \sum_{k \neq n} c_{k} \mid k^0 \rangle
$$

The coefficients are $c_k =\langle k^0 \mid n^1 \rangle$. By orthogonality, the $k=n$ term drops out, since $c_n=\langle n^0 \mid n^1 \rangle=0$; hence the $k\neq n$ condition in the sum.

Insert the expansion into the first-order equation and take the dot product with $\langle k^0 \mid$:

$$
{\hat{H}^0\mid n^1\rangle +\hat{H}^1\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle}
$$

$$
c_k E^0_k + \langle k^0 \mid \hat{H}^1 \mid n^0\rangle  = c_k E^0_n
$$

$$
c_k = \frac{ \langle k^0 \mid \hat{H}^1 \mid n^0\rangle}{E^0_n-E^0_k}=\frac{H_{nk}}{E^0_n-E^0_k}
$$

$$
\boxed{\mid n^1 \rangle = \sum_{k \neq n} c_{k} \mid k^0 \rangle = \sum_{k \neq n} \frac{H_{nk}}{E^0_n-E^0_k} \mid k^0 \rangle}
$$

**Matrix element notation.** We have introduced the convenient notation $H_{nk} = \langle k^0 \mid \hat{H}^1 \mid n^0\rangle$. Note that the Hamiltonian inside the matrix element is always the perturbation part.
:::

:::{admonition} **Deriving the second-order correction $E^2_n$**
:class: dropdown

$$
{\hat{H}^0\mid n^2\rangle+\hat{H}^1\mid n^1\rangle = E_n^0\mid n^2\rangle+ E^1_n\mid n^1 \rangle+E^2_n\mid n^0 \rangle}
$$

Take the dot product with $\langle n^0 \mid$:

$$
{{\langle n^0 \mid }\hat{H}^0 \mid n^2\rangle+{\langle n^0 \mid }\hat{H}^1\mid n^1\rangle = E^0{\langle n^0}\mid n^2\rangle+ E^1_n{\langle n^0 \mid } n^1 \rangle+E^2_n {\langle n^0}\mid n^0 \rangle}
$$

The first term on the left vanishes (Hermitian plus orthogonality), and the first two terms on the right vanish by orthogonality, leaving:

$$
\color{blue}{E^2_n = \langle n^0 \mid \hat{H}^1 \mid n^1 \rangle}
$$

We are not done: the expression still contains $\mid n^1 \rangle$, which we express in terms of the known solutions:

$$
\color{black}{E^2_n = \langle n^0 \mid \hat{H}^1 \mid n^1 \rangle}= \sum_{k \neq n} c_k \langle n^0 \mid \hat{H}^1 \mid k^0 \rangle = \sum_{k \neq n} c_k H_{nk}
$$

$$
\color{blue}{E^2_n = \sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}}
$$

$$
\boxed{E_n = \color{green}{E^0_n} + \color{red}{\langle n^0\mid \hat{H}^1\mid n^0\rangle} + \color{blue}{\sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}}}
$$
:::

## Applications

:::{note} **Example 1: Second-order correction to the ground state**

Write the second-order correction explicitly for the ground state of some exactly solvable Hamiltonian $\hat{H}^0$ perturbed by $\hat{H}^1$:

$$
E_n = E^0_n+ H_{nn} + \sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}
$$

$$
E_0 =E^0_0+ H_{00} + \frac{\mid H_{01}\mid^2}{E^0_0-E^0_1}+\frac{\mid H_{02}\mid^2}{E^0_0-E^0_2}+ \frac{\mid H_{03}\mid^2}{E^0_0-E^0_3}+ ...
$$

Notice that for the ground state the second-order correction is always negative, because $\Delta E_{0k}=E_0-E_k<0$ for every excited state.
:::

:::{note} **Example 2: Magnetic field and spin-orbit coupling**

A hydrogen atom in a magnetic field can be viewed as the H-atom Hamiltonian plus a small perturbation from the interaction with the field:

$$
\hat{H}=\hat{H}_0 + \frac{e}{2m_e} B \hat{L}_z =  \hat{H}_0 + \hat{H}^1
$$

Using the first-order expression, the ground-state energy shift is (with $R_H$ the Rydberg constant and $\beta_B$ the Bohr magneton):

$$
E_0=E^0_0 + \langle 0\mid \hat{H}^1 \mid 0\rangle = -\frac{R_H}{n^2}+m_l \beta_B B
$$

In a similar way, the effect of spin-orbit coupling ($LS$) is:

$$
\hat{H} = \hat{H}_0 + A_{SO}\hat{L}\hat{S}, \qquad E=E_0+ A_{SO} \langle 0 \mid \hat{L} \hat{S}\mid 0 \rangle
$$
:::

:::{note} **Example 3: Perturbing the particle in a box**

Estimate the ground-state and first-excited-state energies, within first-order perturbation theory, of a particle in a box with an added constant potential:

$$
V(x) = V_0, \quad 0 \leq x \leq L
$$

This is a particle in a box perturbed by the constant potential $V_0$. The first-order correction is:

$$
E_n^1 = \langle n \mid V_0 \mid n \rangle = V_0 \cdot \frac{2}{L} \int^L_0 \sin^2 \frac{n\pi x}{L}dx=V_0
$$

Every level is shifted up by the same constant amount:

$$
E_n = E^0_n+E^1_n \approx \frac{n^2 h^2}{8mL^2}+V_0
$$
:::

:::{note} **Example 4: Anharmonic oscillator**

The anharmonic oscillator is a harmonic oscillator plus a cubic perturbation:

$$
\hat{H} = \hat{K}+ \frac{kx^2}{2} +\gamma x^3 = \hat{H}_0+\gamma x^3
$$

The first-order correction vanishes by symmetry, since $x^3$ is odd and $|\psi_n|^2$ is even:

$$
E_n^1 = \langle n\mid \gamma x^3 \mid n\rangle = \langle \text{even/odd} \mid \text{odd} \mid \text{even/odd}\rangle = 0
$$

The energy levels must still change, so we turn to second order. For the ground state:

$$
E^2_0 =  \sum_{k \neq 0} \frac{\mid  \langle 0\mid \gamma x^3 \mid k\rangle \mid^2}{E^0_0-E^0_k} = \frac{\mid  \langle 0\mid \gamma x^3 \mid 1\rangle \mid^2}{E^0_0-E^0_1}+\frac{\mid  \langle 0\mid \gamma x^3 \mid 3\rangle \mid^2}{E^0_0-E^0_3}+ ...
$$

$$
E_0 = \frac{\hbar \omega}{2} + 0 + \frac{H^2_{01}}{\hbar \omega}+\frac{H^2_{03}}{2\hbar \omega}+ ...
$$

Only odd terms in the sum contribute. The matrix elements must be evaluated explicitly using Hermite polynomials.
:::

## Problems

#### Problem 1

::::{admonition} **Problem 1: Linear perturbation of a box**
:class: note

A particle in a box of length $L$ is perturbed by the linear potential $\hat{H}^1 = \varepsilon x$. Compute the first-order energy correction $E_n^{(1)}$ for an arbitrary level $n$.

:::{admonition} **Solution:**
:class: dropdown solution

$$E_n^{(1)} = \langle n|\varepsilon x|n\rangle = \frac{2\varepsilon}{L}\int_0^L x\sin^2\frac{n\pi x}{L}\,dx = \frac{2\varepsilon}{L}\cdot\frac{L^2}{4} = \frac{\varepsilon L}{2}.$$

Every level is shifted by the same amount $\varepsilon L/2$, since the average position $\langle x\rangle = L/2$ is the same for all $n$. The level spacing is unchanged to first order.
:::
::::

#### Problem 2

::::{admonition} **Problem 2: Sign of the ground-state second-order shift**
:class: note

Argue, without evaluating any integrals, that the second-order energy correction to the ground state of any system is always negative or zero.

:::{admonition} **Solution:**
:class: dropdown solution

The second-order correction is $E_0^{(2)} = \sum_{k\neq 0}\frac{|H_{0k}|^2}{E_0^0 - E_k^0}$. The numerator $|H_{0k}|^2 \ge 0$ for every term. Since the ground state is the lowest level, $E_0^0 - E_k^0 < 0$ for all $k \neq 0$. Each term is therefore negative or zero, so the sum is negative or zero. Physically, mixing in excited states always pushes the ground state down.
:::
::::

#### Problem 3

::::{admonition} **Problem 3: First-order correction vanishes for the cubic anharmonic term**
:class: note

Show that the first-order energy correction from a perturbation $\hat{H}^1 = \gamma x^3$ vanishes for every harmonic-oscillator eigenstate $|n\rangle$, and explain why the second-order correction does not.
::::

#### Problem 4

::::{admonition} **Problem 4: Two-level perturbation**
:class: note

A two-level system has unperturbed energies $E_1^0$ and $E_2^0$ and a perturbation with the single off-diagonal element $H_{12} = H_{21} = v$ (and zero diagonal elements). Use second-order perturbation theory to write the corrected energies, then compare to the exact eigenvalues of the $2\times 2$ matrix. Under what condition does perturbation theory work well?
::::

#### Problem 5

::::{admonition} **Problem 5: Charged oscillator in a field**
:class: note

A charged harmonic oscillator $\hat{H}_0 = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2$ is placed in a uniform electric field, adding $\hat{H}^1 = -qEx$. Show that the first-order correction vanishes by symmetry, and that the exact energy shift (found by completing the square) is $-\frac{q^2E^2}{2m\omega^2}$, independent of $n$. This is one of the rare cases where perturbation theory can be checked against an exact result.
::::
