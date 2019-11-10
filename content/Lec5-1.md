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





## Atomic orbitals



