## Outline for Lecture 5.1:  "Schrodinger equation for Hydrogen atom"

- Hydrogen atom is the simplest atom for which Schrodinge equation can be solved exactly. He atom which only has one more electron already proves to be impossible to solve exactly. 
- The solution of the Schrödinger equation for H atom uses the fact that the Coulomb potential produced by the nucleus is isotropic: it is radially symmetric in space and only depends on the distance to the nucleus. This symmetry gives rise to degenercaies in energy levels. 
- Although the resulting energy eigenfunctions (the orbitals) are not necessarily isotropic themselves, their dependence on the angular coordinates follows completely generally from this isotropy of the underlying potential.
- The angular momentum is conserved, therefore, the energy eigenvalues may be classified by two angular momentum quantum numbers, ℓ and m (both are integers) and quantize mangitude and projection of angular momentum. 
- Atomic orbitals are introduced which are used for also describing multi-electron atoms and molecules. 



## Atomic spectra of H

Hydrogen atom spectra was the first real test that Schroidinger equation passed perfectly by predicitng all the lines with an energy expressed expressed in terms of dunemtnal constants. The Schroinger equation thereby opened the door for systmetic treatment of spectra and structures of atoms and moelcuels far more complex than H atom, which alas do not admit an exact solution. This is why we treasure the solution fo H atom so much. It provides a fundmental building block to understand more complex systems.



### Setting  up the H atom porblm



- H atom is a two body problm: one electron and one nucleus

- We can reduce the two body problem to one body problem of electron with reduced mass moving with respect to fixed nucleus. 

- We have a porblem of one particle moving in a symmetric potential field in 3D. Expect to get 3 quantum numbers, anticipate some degenreacies due to this raidal symmetry. 

- Potential energy consists of coulomb term encoding the electrostatic attraction between nucleus and electron.  

  

## Hamitlonain of H atom

- This is the hamitlonain for H atom


$$
\hat{H} = \hat{K}+\hat{V}(r)=-\frac{\hbar^2}{2\mu}\nabla^2 -\frac{e^2}{4\pi \epsilon_0r}
$$



Sperhcial nature of the problem prompts us to adopt spherical coordinates:

$$
\nabla_{r,\theta,\phi}^2 = \frac{1}{r^2} \frac{\partial }{\partial r} \Big(r^2\frac{\partial}{\partial r}\Big)+\frac{1}{r^2 sin \theta} \frac{\partial }{\partial \theta} \Big(sin \theta \frac{\partial}{\partial \theta}\Big)+\frac{1}{r^2 sin^2 \theta}\frac{\partial^2 }{\partial \phi^2} = \\ =\nabla^2_r +\frac{1}{r^2}\nabla_{\theta,\phi}^2
$$



This time the radial part of laplacian operator is non-zero becasue $r$ coordinate which is the distance between electorn and nucleus is no longer a constant. Electron is not not a pointy object moving in consants orbits as was erroneously depicted in early quantum theores of Bohr and others. 

- Having prepared hamitlonian in spherical coordinates we can write Schrodinger euqation in convneient for solving form

  

$$
-\frac{\hbar^2}{2\mu}\Big [\nabla^2_r +\frac{1}{r^2}\nabla_{\theta,\phi}^2 \Big ]\psi(r,\theta,\phi) -V(r)\psi(r,\theta,\phi)=E\psi(r,\theta,\phi)
$$



### Separation of variables

Spherical coordinates allows splitting hamitlonian into radial and spherical parts.


$$
\Big [-\frac{\hbar^2}{2\mu}\nabla^2_r -V(r)-E\Big ]\psi(r,\theta,\phi) -\frac{\hbar^2}{2\mu r^2}\nabla_{\theta,\phi}^2 \psi(r,\theta,\phi) = 0
$$




$$
\psi(r,\theta,\phi) =R(r)Y(\theta,\phi)
$$




$$
Y(\theta,\phi)\Big [-\frac{\hbar^2}{2\mu}\nabla^2_r -V(r)-E\Big ]R(r) - R(r) \frac{\hbar^2}{2\mu r^2}\nabla_{\theta,\phi}^2 Y(\theta,\phi) = 0
$$

- Multiply by $2\mu r^2$ and devide by $R(r)Y(\theta,\phi)$ to cleanly separate radial and spherical variables:

  

$$
-\frac{1}{R(r)}\Big[ \hbar^2 r^2 \nabla^2_r + 2\mu r^2(V(r)+E)  \Big] R(r) - \\ - \frac{\hbar^2}{Y(\theta,\phi)}\nabla_{\theta,\phi}^2 Y(\theta,\phi) =0
$$



### $(\theta,\phi)$ part:  Sperhical harmonics!

- Introducing separation constant $\beta$ we have an eignfunction-eigenvalue problem for PDE in $\theta,\phi$ variables.

$$
-\frac{\hbar^2}{Y(\theta,\phi)}\nabla_{\theta,\phi}^2 Y(\theta,\phi) = \beta
$$


$$
-\hbar^2\nabla_{\theta,\phi}^2 Y(\theta,\phi) = \beta Y(\theta,\phi)
$$

- We recognize the last equation as an eigen-function/value problem for angular momentum operators. We can immeadiately write down eigenvlaues we have obteined from rigid-rotor problem with $beta=\hbar^2 l(l+1)$

  

$$
-\hat{L}^2 Y(\theta,\phi) = \beta Y(\theta,\phi) = \hbar^2 l(l+1)Y(\theta,\phi)
$$



- Quantum number m is associated with $\phi$ variable of spherical harmonics which is an eigenfuction of a z component of angular momentum:

  

  - $\Phi(\phi) = \frac{1}{\sqrt{2\pi}}e^{im\phi}$

    

  - $\hat{L_z}\Phi(\phi)=\hbar m\Phi(\phi)$

    

### R part of eigenfunctions of H


$$
\Big[ \hbar^2 r^2 \nabla^2_r + 2\mu r^2(V(r)+E)  \Big] R(r) =\beta R(r) = \hbar^2 l(l+1)R
$$

This equation is solved via series expansion method which introduces new auantum number n.

- Eigenfunctions are expressed in terms of associated Laguerre polynomials. 

  

$$
R_{nl}(r)= C_{nl} r^l e^{-r/na_0} L^{2l+1}_{n+1}(r)
$$



- Eigenvalues depend only on quantum number n thereby showing degeneracy with respect to other quantumn numbers

$$
E_n = -\frac{\mu e^4}{8 \epsilon_0^2 h^2 n^2}
$$

- $n=1,2,... \infty$
- $l=0,1,2,...n-1$
- $m_l =0,\pm1, \pm2,...\pm l$



## Full eigenfunctions of H atom



### Principlac quantum number n



### Angular quantum number l 



### magnetic quantum number m 





 ## Schrodinger equation for hydrogenlike atoms


Consider one electron and one nucleus with charge $Ze$ where $e$ is the magnitude of the electron charge (1.6021773 $\times$ $10^{-19}$ C) and $Z$ is the atomic number. Examples of such systems are: H, $He^+$, $Li^{2+}$ 

For these simple atomic systems, the Schrodinger equation can be solved analytically.  This can be generalized for systems having nuclei with charges other than $+1$ as follows:

$${-\frac{\hbar^2}{2m_e}\Delta \psi_i(x,y,z) - \frac{Ze^2}{4\pi\epsilon_0\sqrt{x^2 + y^2 + z^2}}\psi_i(x,y,z) = E_i\psi_i(x,y,z)}$$


where $m_e$ is the electron mass, $\epsilon_0$ is the \href{http://en.wikipedia.org/wiki/Vacuum_permittivity}{\uline{vacuum permittivity}}, and subscripts for $\psi$ and $E$ signify the fact that there are multiple ($\psi_i$, $E_i$) combinations that satisfy Eq. (\ref{eq10.2}). Note that we should have used the reduced mass ($\mu$; see Eq. (\ref{eqX.25})) for the nucleus and electron above, but because the nucleus is much heavier then the electron, the reduced mass is very close to the electron mass.


Because of the spherical symmetry of the \href{http://en.wikipedia.org/wiki/Coulomb's_law}{\uline{Coulomb potential}} it is convenient to work in spherical coordinates:





$${\left[ -\frac{\hbar^2}{2m_e}\Delta - \frac{Ze^2}{4\pi\epsilon_0 r}\right]\psi_i(r,\theta,\phi) = E_i\psi(r,\theta,\phi)}$$


where the $\Delta$ is expressed in spherical coordinates:

$${\Delta\equiv\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left( r^2\frac{\partial}{\partial r}\right) + \frac{1}{r^2\textnormal{sin}(\theta)}
\frac{\partial}{\partial\theta}\left(\textnormal{sin}(\theta)\frac{\partial}{\partial\theta}\right) + \frac{1}{r^2\textnormal{sin}^2(\theta)}\frac{\partial^2}{\partial\phi^2}}$$


Note that the Coulomb potential term above depends only on $r$ (and not on $\theta$ or $\phi$). By using Eq. (\ref{eq9.160}) the Laplacian can be written in terms of the angular momentum operator $\hat{L}$:

$${\Delta = \frac{1}{r^2}\frac{\partial}{\partial r}\left( r^2\frac{\partial}{\partial r}\right) - \frac{1}{r^2}\frac{\hat{L}^2}{\hbar^2}
= \frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r} - \frac{1}{r^2}\frac{\hat{L}^2}{\hbar^2}}$$


By substituting this into Eq. (\ref{eq10.4}) and multiplying both sides by $2m_er^2$, we get:

$$\left[-\hbar^2r^2\left(\frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r}\right) - \frac{m_er^2Ze^2}{2\pi\epsilon_0r}+ \hat{L}^2\right]\psi_i(r,\theta,\phi) = (2m_er^2E_i)\psi_i(r,\theta,\phi)$$

Since the operator can be split into $r$ and angle dependent parts, the solution can be written as a product of the radial and angular parts 

#### Separation of variables



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

where $L_{n+l}^{2l+1}(\rho)$ are \href{http://en.wikipedia.org/wiki/Laguerre_polynomials}{\uline{associated Laguerre polynomials}}. Explicit expressions will be given later in the text. The constant $a_0$ is called the \href{http://en.wikipedia.org/wiki/Bohr_radius}{\uline{Bohr radius}}. Some of the first radial wavefunctions are listed on the next page.

Some of the electronic energy levels of hydrogen atom are shown below.

$$
\begin{table}
\begin{tabular}{l@{\extracolsep{1cm}}l@{\extracolsep{1cm}}l@{\extracolsep{1cm}}l}
Orbital & $n$ & $l$ & $R_{nl}$\\
\hline
1s & 1 & 0 & $2\left(\frac{Z}{a_0}\right)^{3/2}e^{-\rho/2}$\\
2s & 2 & 0 & $\frac{1}{2\sqrt{2}}\left(\frac{Z}{a_0}\right)^{3/2}(2 - \rho)e^{-\rho/2}$\\
2p & 2 & 1 & $\frac{1}{2\sqrt{6}}\left(\frac{Z}{a_0}\right)^{3/2}\rho e^{-\rho/2}$\\
3s & 3 & 0 & $\frac{1}{9\sqrt{3}}\left(\frac{Z}{a_0}\right)^{3/2}(6 - 6\rho - \rho^2)e^{-\rho/2}$\\
3p & 3 & 1 & $\frac{1}{9\sqrt{6}}\left(\frac{Z}{a_0}\right)^{3/2}(4 - \rho)\rho e^{-\rho/2}$\\
3d & 3 & 2 & $\frac{1}{9\sqrt{30}}\left(\frac{Z}{a_0}\right)^{3/2}\rho^2 e^{-\rho/2}$\\
\end{tabular}
\end{table}
$$



