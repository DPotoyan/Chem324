---
kernelspec:
  name: python3
  display_name: Python 3
---

# Atomic Orbitals

:::{note} **What you will learn**

- **A wavefunction for a one-electron system is called an orbital.** For an atomic system such as the hydrogen atom, it is called an [atomic orbital](http://en.wikipedia.org/wiki/Atomic_orbital).
- The orbital plots demonstrate the shapes of the orbitals, but this does not tell us anything about the radial extent (i.e., how far the orbital reaches).
- As the value of $Z$ is increased, the radial extent decreases. This indicates that for higher nuclear charge the electrons reside closer to the nucleus.
- **The radial wavefunctions have $n - l - 1$ nodes** between distances of zero and infinity.
- **The angular part of the wavefunctions has $l$ nodes.**
- **The total number of nodes is $n - 1$.**
:::

:::{important} **Definition of an atomic orbital**

- **Atomic orbital (AO):** a single-electron wavefunction (exact for H-like atoms)

$$
\psi_{n\ell m_\ell}(r,\theta,\phi) = R_{n\ell}(r)\,Y_{\ell m_\ell}(\theta,\phi)
$$

- **Principal quantum number:** $n = 1, 2, 3, \ldots$
- **Orbital angular momentum:** $\ell = 0, 1, 2, \ldots, n-1$
- **Magnetic quantum number:** $m_\ell = -\ell, -\ell + 1, \ldots, \ell$

**Probability distribution (full 3D):**

$$
|\psi|^2 dV = \big|R_{n\ell}(r)\big|^2 \cdot \big|Y_{\ell m_\ell}(\theta,\phi)\big|^2 \cdot r^2\sin\theta \, dr \, d\theta \, d\phi
$$

**Radial probability distribution:**

$$
P_r(r) = r^2\big|R_{n\ell}(r)\big|^2
\quad\text{with}\quad \int_{0}^{\infty} P_r(r) \, dr = 1
$$

**Angular probability density:**

$$
P_\Omega(\theta,\phi) = \big|Y_{\ell m_\ell}(\theta,\phi)\big|^2
\quad\text{with}\quad \int_{0}^{2\pi}\int_{0}^{\pi} P_\Omega \sin \theta \, d\theta \, d\phi = 1
$$

*Notes:*

- $s$ orbitals ($\ell = 0$) are isotropic: $P_\Omega = \tfrac{1}{4\pi}$.
- $p, d, \ldots$ orbitals show angular nodes where $Y_{\ell m_\ell} = 0$, setting the orbital shapes.
:::

### Radial profiles of atomic orbitals

- When visualizing the radial probabilities, it is possible to either directly plot the square of the radial wavefunction ($R_{nl}^2$) or the radial probability density ($P_{nl}$):

$${P_{nl}(r) = r^2 N_{nl}^2 R_{nl}^2(r)}$$

:::{figure} images/AO_0.png
:alt: Radial probability densities of hydrogen orbitals
:width: 80%

Fig.1 Radial probability density $P_{nl}(r) = r^2 |R_{nl}(r)|^2$ for several hydrogen orbitals. The peaks mark the most probable distance of the electron from the nucleus.
:::

- According to this expression, the most probable radius for an electron in the hydrogen-atom $1s$ orbital is $a_0$ (the Bohr radius). The figure above shows examples of $P_{nl}$. Probability densities are useful, for example, in understanding charge distributions in atoms and molecules.

:::{figure} images/AO2.jpg
:alt: Radial wavefunctions and probability densities
:width: 80%

Fig.2 Radial wavefunctions $R_{nl}(r)$ and the associated radial probability densities for the lowest hydrogen orbitals.
:::

- As the principal quantum number $n$ increases, the electron moves out to greater distances from the nucleus. The average distance for an electron in a given orbital (with quantum numbers $n$ and $l$) is given by (this is not the same as the most probable value):

$${\langle r\rangle_{nl} = \int_0^\infty r \cdot P_{nl}(r) \, dr = \frac{n^2 a_0}{Z}\left\{ 1 + \frac{1}{2}\left[ 1 - \frac{l(l+1)}{n^2}\right]\right\}}$$

- Note that the expectation value of $r$ and the most probable value of $r$ are not equal. The expectation value can be thought of like *an average*, and the most probable value like a *maximum* value.

### 3D shapes of orbitals

- For degenerate states with $l > 0$, we have an additional degree of freedom in choosing how to represent the orbitals. In fact, any linear combination of a given set of $2l + 1$ orthogonal eigenfunctions corresponding to a degenerate set with orbital angular momentum $l$ is also a solution to the Schrödinger equation.

:::{figure} images/AO.png
:alt: Shapes of atomic orbitals
:width: 80%

Fig.3 Shapes of the $s$, $p$, and $d$ atomic orbitals shown as isosurfaces of the probability density.
:::

- Two commonly used representations are the Cartesian form, which is real-valued (and, in the case of $l = 1$, denoted $p_x$, $p_y$, and $p_z$), and the eigenfunctions of angular momentum ($\hat{L}^2$ and $\hat{L}_z$), which are complex-valued and denoted $p_{-1}$, $p_0$, and $p_{+1}$. Both polar and Cartesian forms represent the same physical electron density, just in different coordinate frames. The relation between the representations is:

$${p_x = -\frac{1}{\sqrt{2}}\left( p_{+1} - p_{-1}\right) \propto \sin(\theta)\cos(\phi) \propto x}$$
$${p_y = \frac{i}{\sqrt{2}}\left( p_{+1} + p_{-1}\right) \propto \sin(\theta)\sin(\phi) \propto y}$$
$${p_z = p_0}$$

:::{figure} images/Orbital_p1-px_animation.gif
:alt: Combining complex p orbitals into real p orbitals
:width: 50%

Fig.4 Animation showing how the complex orbitals $p_{+1}$ and $p_{-1}$ combine into the familiar real $p_x$ orbital.
:::

- By combining $p_x$, $p_y$, and $p_z$, the lobe of the orbital can be made to point in any direction. For $d$-orbitals, we have five degenerate levels:

:::{figure} images/p-orbitals.png
:alt: Real p orbitals pointing along the axes
:width: 70%

Fig.5 The three real $p$ orbitals ($p_x$, $p_y$, $p_z$) point along the Cartesian axes; their linear combinations can point in any direction.
:::

$${d_{x^2 - y^2} = \frac{1}{\sqrt{2}}\left(d_{+2} + d_{-2}\right), \quad d_{xy} = -\frac{i}{\sqrt{2}}\left( d_{+2} - d_{-2}\right)}$$
$${d_{xz} = -\frac{1}{\sqrt{2}}\left( d_{+1} - d_{-1}\right), \quad d_{yz} = \frac{i}{\sqrt{2}}\left( d_{+1} + d_{-1}\right)}$$
$${d_{z^2} = d_0}$$

### Table of 2D orbitals

:::{figure} images/hydrogen_probability_densities.png
:alt: 2D probability densities of hydrogen orbitals
:width: 90%

Fig.6 Two-dimensional cross sections of the probability densities $|\psi_{nlm}|^2$ for hydrogen orbitals.
:::

### Table of 3D orbitals

:::{figure} images/AO3.png
:alt: 3D shapes of hydrogen orbitals
:width: 90%

Fig.7 Three-dimensional isosurface renderings of hydrogen atomic orbitals.
:::

### Interactive plotter of atomic orbitals

<iframe src="https://al2me6.github.io/evanescence/"
        width="800"
        height="500"
        allowfullscreen>
</iframe>

### Problems

::::{admonition} **Problem 1: Counting states for $n = 3$**
:class: note

- For the hydrogen atom, how many possible quantum states correspond to the principal quantum number $n = 3$?
- What are the energies of these states?
- Consider several values of $n$ and show that the number of orbitals for each $n$ is $n^2$.

:::{admonition} **Solution:**
:class: dropdown solution

If $n = 3$, the allowed values of $l$ are $0$, $1$, and $2$.

- If $l = 0$, then $m = 0$ (1 state).
- If $l = 1$, then $m = -1, 0, 1$ (3 states).
- If $l = 2$, then $m = -2, -1, 0, 1, 2$ (5 states).

In total there are $1 + 3 + 5 = 9$ allowed states. This confirms that the number of orbitals for the H-atom is $n^2$.

Because the total energy depends only on the principal quantum number $n = 3$, the energy of each of these states is:

$$
E_n = -13.6 \cdot \frac{1}{n^2} \, [\text{eV}]
$$
:::
::::

::::{admonition} **Problem 2: Quantum numbers of a $3d$ electron**
:class: note

- The notation $3d$ specifies the quantum numbers for an electron in the hydrogen atom. What are the values of $n$ and $l$?
- What are the values of the energy and the angular momentum?
- What are the possible values of the magnetic quantum number?
- What are the possible orientations of the angular momentum vector?

:::{admonition} **Solution:**
:class: dropdown solution

- The $3d$ orbital corresponds to $n = 3$ and $l = 2$. The energy is $E_3 = -13.6/9 \approx -1.51$ eV and the magnitude of the angular momentum is $L = \hbar\sqrt{l(l+1)} = \hbar\sqrt{6}$.
- The possible values of the magnetic quantum number are $m_l = -2, -1, 0, 1, 2$ (five values).
- The orientation of $L_z$ with respect to $L$ is fixed by $\cos\theta = L_z / L = m_l / \sqrt{l(l+1)}$, giving five allowed orientations of the angular momentum vector.
:::
::::

::::{admonition} **Problem 3: Nodes of the $3p_z$ orbital**
:class: note

Locate the nodes (and nodal surfaces) of the $3p_z$ orbital:

$$
\psi_{3p_z} = \frac{1}{81}\sqrt{\frac{2}{\pi}}\left(\frac{1}{a_0}\right)^{3/2}\left(6\frac{r}{a_0} - \frac{r^2}{a_0^2}\right) e^{-r/3a_0}\cos(\theta)
$$

:::{admonition} **Solution:**
:class: dropdown solution

- $3p_z$ corresponds to $n = 3$, $l = 1$, and $m_l = 0$.
- The radial part is zero at $r = 0$ and $r = 6a_0$. The first is part of the boundary condition and not a node, because the wavefunction does not change sign there. Hence there is 1 radial node.
- The angular part has one nodal surface from $\cos\theta = 0$, which occurs at $\theta = \frac{\pi}{2}$ (the $xy$-plane).
- We thus have 2 nodes for the $3p_z$ orbital. The total number of nodes is $n - 1$, made up of $l$ angular nodes and $n - l - 1$ radial nodes.
:::
::::

::::{admonition} **Problem 4: Averages and probabilities for the ground state**
:class: note

- Calculate the average distance from the nucleus at which to find the electron in the ground state of the H-atom.
- Calculate the probability of finding the electron within the first Bohr radius $a_0$.
- Calculate the most probable value of $r$ at which to find the electron.

:::{admonition} **Solution:**
:class: dropdown solution

The ground state is $1s$:

$$
\psi_{1s}(r) = \frac{1}{\sqrt{\pi}}\frac{1}{a_0^{3/2}}e^{-r/a_0}
$$

**Average distance.** Averages (expectations) of observables are computed as usual via $\langle\psi |A| \psi \rangle$:

$$\langle 1s |r| 1s\rangle = \frac{1}{\pi a_0^3}\int_0^{\infty} e^{-2r/a_0} r \cdot r^2 dr \int_0^{\pi} \sin\theta \, d\theta \int_0^{2\pi} d\phi = \frac{4}{a_0^3}\int_0^{\infty} r^3 e^{-2r/a_0} dr$$

The last integral is evaluated using the table integral $\int_0^{\infty} x^n e^{-Ax}dx = \frac{n!}{A^{n+1}}$:

$$\langle 1s |r| 1s\rangle = \frac{4}{a_0^3} \cdot \frac{3!}{(2/a_0)^4} = \frac{3}{2}a_0$$

**Probability within $a_0$.** The probability of finding the electron at a distance $r$ regardless of angle is found by integrating out the angles:

$$
P(r) = \int |\psi(r, \theta, \phi)|^2 r^2 \sin\theta \, d\theta \, d\phi = \frac{4}{a_0^3} r^2 e^{-2r/a_0}
$$

$$
\text{Prob}(0 \leq r \leq a_0) = \frac{4}{a_0^3} \int_0^{a_0} r^2 e^{-2r/a_0} dr
$$

**Most probable value** is found by maximizing $P(r)$:

$$
\left.\frac{dP(r)}{dr}\right|_{r = r_{\max}} = 0 \quad \Rightarrow \quad r_{\max} = a_0
$$
:::
::::

::::{admonition} **Problem 5: Orthonormality of $|210\rangle$ and $|200\rangle$**
:class: note

Show that $|210\rangle$ is normalized and orthogonal to $|200\rangle$.

:::{admonition} **Hint:**
:class: dropdown solution

This problem is worked out in Chapter 7 of McQuarrie's *Quantum Chemistry*. The key is that $|210\rangle$ ($2p_z$) and $|200\rangle$ ($2s$) share the same radial dependence form but differ in their angular parts ($Y_0^0$ versus $Y_1^0$), so the angular integral $\langle Y_1^0 | Y_0^0 \rangle = 0$ makes them orthogonal.
:::
::::

::::{admonition} **Problem 6: Average potential energy**
:class: note

Calculate the average potential energy of the H-atom in its ground and first excited states.

:::{admonition} **Hint:**
:class: dropdown solution

Use $\langle V \rangle = -\frac{Ze^2}{4\pi\epsilon_0}\langle r^{-1}\rangle$ together with $\langle r^{-1}\rangle_{n,l} = \frac{Z}{a_0 n^2}$, so that $\langle V \rangle_n = -\frac{Z^2 e^2}{4\pi\epsilon_0 a_0 n^2}$. This is a worked example in Chapter 7 of McQuarrie. Notice it gives the virial-theorem result $\langle V \rangle = 2E_n$.
:::
::::
