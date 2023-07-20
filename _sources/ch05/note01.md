## Hydrogenlike atoms

```{admonition} What you need to know
:class: note
- Hydrogen atom is the simplest atom for which Schrodinge equation can be solved exactly. He atom which only has one more electron already proves to be impossible to solve exactly. 
- The solution of the Schrödinger equation for H atom uses the fact that the Coulomb potential produced by the nucleus is isotropic: it is radially symmetric in space and only depends on the distance to the nucleus. This symmetry gives rise to degenercaies in energy levels. 
- Although the resulting energy eigenfunctions (the orbitals) are not necessarily isotropic themselves, their dependence on the angular coordinates follows completely generally from this isotropy of the underlying potential.
- The angular momentum is conserved, therefore, the energy eigenvalues may be classified by two angular momentum quantum numbers, ℓ and m (both are integers) and quantize mangitude and projection of angular momentum. 
- Atomic orbitals are introduced which are used for also describing multi-electron atoms and molecules. 
```

### Atomic spectra of H

Hydrogen atom spectra was the first real test that Schroidinger equation passed perfectly by predicitng all the lines with an energy expressed expressed in terms of dunemtnal constants. The Schroinger equation thereby opened the door for systmetic treatment of spectra and structures of atoms and moelcuels far more complex than H atom, which alas do not admit an exact solution. This is why we treasure the solution fo H atom so much. It provides a fundmental building block to understand more complex systems.


 ### Schrodinger equation for hydrogenlike atoms

 - H atom is a two body problm: one electron and one nucleus

- We can reduce the two body problem to one body problem of electron with reduced mass moving with respect to fixed nucleus. 

- We have a porblem of one particle moving in a symmetric potential field in 3D. Expect to get 3 quantum numbers, anticipate some degenreacies due to this raidal symmetry. 

- Potential energy consists of coulomb term encoding the electrostatic attraction between nucleus and electron. 

- Consider one electron and one nucleus with charge $Ze$ where $e$ is the magnitude of the electron charge (1.6021773 $\times$ $10^{-19}$ C) and $Z$ is the atomic number. Examples of such systems are: H, $He^+$, $Li^{2+}$ 

- For these simple atomic systems, the Schrodinger equation can be solved analytically.  This can be generalized for systems having nuclei with charges other than $+1$ as follows:

$${-\frac{\hbar^2}{2m_e}\Delta \psi_i(x,y,z) - \frac{Ze^2}{4\pi\epsilon_0\sqrt{x^2 + y^2 + z^2}}\psi_i(x,y,z) = E_i\psi_i(x,y,z)}$$


where $m_e$ is the electron mass, $\epsilon_0$ is the [vacuum permitivity](http://en.wikipedia.org/wiki/Vacuum_permittivity) and subscripts for $\psi$ and $E$ signify the fact that there are multiple ($\psi_i$, $E_i$) combinations. 

> Note again that we should have used the reduced mass  for the nucleus and electron above, but because the nucleus is much heavier then the electron, the reduced mass is very close to the electron mass.


- Because of the spherical symmetry of the [Coulomb potential](http://en.wikipedia.org/wiki/Coulomb's_law)it is convenient to work in spherical coordinates:



$${\left[ -\frac{\hbar^2}{2m_e}\Delta - \frac{Ze^2}{4\pi\epsilon_0 r}\right]\psi_i(r,\theta,\phi) = E_i\psi(r,\theta,\phi)}$$


where the $\Delta$ is expressed in spherical coordinates:

$${\Delta\equiv\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left( r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\textnormal{sin}(\theta)}
\frac{\partial}{\partial\theta}\left(\textnormal{sin}(\theta)\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\textnormal{sin}^2(\theta)}\frac{\partial^2}{\partial\phi^2}}$$


Note that the Coulomb potential term above depends only on $r$ (and not on $\theta$ or $\phi$). The Laplacian can be written in terms of the angular momentum operator $\hat{L}$:

$${\Delta = \frac{1}{r^2}\frac{\partial}{\partial r}\left( r^2\frac{\partial}{\partial r}\right) - \frac{1}{r^2}\frac{\hat{L}^2}{\hbar^2}
= \frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r} - \frac{1}{r^2}\frac{\hat{L}^2}{\hbar^2}}$$


By substituting this into Eq. (\ref{eq10.4}) and multiplying both sides by $2m_er^2$, we get:

$$\left[-\hbar^2r^2\left(\frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r}\right) - \frac{m_er^2Ze^2}{2\pi\epsilon_0r}+ \hat{L}^2\right]\psi_i(r,\theta,\phi) = (2m_er^2E_i)\psi_i(r,\theta,\phi)$$

Since the operator can be split into $r$ and angle dependent parts, the solution can be written as a product of the radial and angular parts 

### Separation of variables



$${\psi_i(r,\theta,\phi) = R_{nl}(r)Y_l^m(\theta,\phi)}$$

where $R_{nl}$ is called the radial wavefunction and $Y_l^m$ are eigenfunctions of $\hat{L}^2$ as discussed earlier. Eq. (\ref{eq10.7}) can now be rewritten as:

$${-\hbar^2Y_l^m(\theta,\phi)r^2\left(\frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r}\right) R_{nl}(r) - Y_l^m(\theta,\phi)
\frac{m_er^2Ze^2}{2\pi\epsilon_0r}R_{nl}(r)}
{+ Y_l^m(\theta, \phi)R_{nl}(r)\underbrace{l(l+1)\hbar^2}_{= \hat{L}^2} = (2m_er^2E_{nl})Y_l^m(\theta,\phi)R_{nl}(r)}$$


Next we divide the above equation side by side by $Y_l^m\times (2m_er^2)$:

$${\left[ -\frac{\hbar^2}{2m_e}\left(\frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r}\right) - \frac{Ze^2}{4\pi\epsilon_0r}+ \frac{l(l+1)\hbar^2}{2m_er^2}\right] R_{nl}(r) = E_{nl}R_{nl}(r)}$$

Substituting $R_{nl}(r) = S_{nl}(r) / r$ and multiplying both sides by $r$ gives a slightly simpler form:

$${-\frac{\hbar^2}{2m_e}\frac{\partial^2S_{nl}(r)}{\partial r^2} + \underbrace{\left( -\frac{Ze^2}{4\pi\epsilon_0r} + \overbrace{\frac{l(l+1)\hbar^2}{2m_er^2}}^{\textnormal{``centrifugal potential''}}\right)}_{\equiv V_{eff}(r)} S_{nl}(r) = E_{nl}S_{nl}(r)}$$


with $l = 0, 1, 2, ...$.



The eigenvalues $E_{nl}$ and and the radial eigenfunctions $R_{nl}$ can be written as (derivations are lengthy but standard math):

$${E_{nl} = -\frac{m_ee^4Z^2}{32\pi^2\epsilon_0^2\hbar^2n^2}\textnormal{ with }n = 1,2,3...\textnormal{ (independent of }l,l<n\textnormal{)}}$$

$${R_{nl}(r) = \rho^lL^{2l+1}_{n+l}(\rho)\textnormal{exp}\left(-\frac{\rho}{2}\right)\textnormal{ with }\rho = \frac{2Zr}{na_0}\textnormal{ and }
a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_ee^2}}$$

where $L_{n+l}^{2l+1}(\rho)$ are [Laguerre polynomials](http://en.wikipedia.org/wiki/Laguerre_polynomials). Explicit expressions will be given later in the text. The constant $a_0$ is called the [Bohr radius](http://en.wikipedia.org/wiki/Bohr_radius) Some of the first radial wavefunctions are listed on the next page.

Some of the electronic energy levels of hydrogen atom are shown below.



#### Examples of the radial wavefunctions for hydrogenlike atoms


| Orbital | $n$ | $l$ | $R_{nl}$                                                                             |
|---------|-----|-----|--------------------------------------------------------------------------------------|
| 1s      | 1   | 0   | $2\left(\frac{Z}{a_0}\right)^{3/2}e^{-\rho/2}$                                       |
| 2s      | 2   | 0   | $\frac{1}{2\sqrt{2}}\left(\frac{Z}{a_0}\right)^{3/2}(2 - \rho)e^{-\rho/2}$           |
| 2p      | 2   | 1   | $\frac{1}{2\sqrt{6}}\left(\frac{Z}{a_0}\right)^{3/2}\rho e^{-\rho/2}$                |
| 3s      | 3   | 0   | $\frac{1}{9\sqrt{3}}\left(\frac{Z}{a_0}\right)^{3/2}(6 - 6\rho - \rho^2)e^{-\rho/2}$ |
| 3p      | 3   | 1   | $\frac{1}{9\sqrt{6}}\left(\frac{Z}{a_0}\right)^{3/2}(4 - \rho)\rho e^{-\rho/2}$      |
| 3d      | 3   | 2   | $\frac{1}{9\sqrt{30}}\left(\frac{Z}{a_0}\right)^{3/2}\rho^2 e^{-\rho/2}$             |




