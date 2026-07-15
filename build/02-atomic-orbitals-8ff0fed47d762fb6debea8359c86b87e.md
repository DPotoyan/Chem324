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
