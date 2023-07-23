## Rigid Rotor  

```{admonition} What you need to know
:class: note
- The rigid rotator system is introduced as a prototype for the quantization of rotational degrees of freedom in molecules. The spherical coordinate system is introduced out of the necessity of taking advantage of the spherical symmetry of the problem, which leads to a reduction of dimensionality.
- Solving the Schrodinger equation in spherical coordinates results in eigenfunctions in the form of spherical harmonics. Energy eigenvalues are found to be degenerate for one of the quantum numbers. 
- Connection with microwave spectroscopy is shown where spectral lines are predicted to occur in equal intervals. 
- The selection rule is established via the recursion relation of spherical harmonics.
- Coupling of vibrational degrees leads to rovibronic transitions and necessitates the inclusion of vibrational quantum numbers for a more accurate account of transitions. 
```


### Classical picture: Rotating dumbbell

The rigid rotor is a model of a rotating dumbbell: two unequal masses held together via a rigid stick.  The system is not acted upon by any external potential; hence the only energy is the kinetic energy of rotation: 

$$
K=\frac{m_1 v_1^2}{2}+\frac{m_2 v_2^2}{2}=\frac{m_1 r_1^2+m_2 r^2_2}{2}\omega^2
$$

Where we have plugged in $v_1=\omega r_1$ and $v_2=\omega_2 r$ velocities of rotation of two masses rotating with frequency $\omega$. The classical mechanical problem of two masses is once again reducible to a single reduced mass $\mu$ rotating around constant radius $r=r_1+r_2$ rotating around center of mass $m_1 r_1=m_2 r_2$.



$$
K=\frac{I \omega^2}{2}=\frac{L^2}{2I}
$$


Where $L=I \omega$ is the angular momentum, the $I=\mu r^2$ is moment of inertia and $\mu=\frac{m_1 m_2}{m_1+m_2}$



### Quantum rigid rotor and angular momentum operator 

- The hamiltonian for the rigid rotor model is the kinetic energy operator of an effective mass $\mu$ wchih rotates around sphere of radius $r=const$. To incorporate constraint $r=const$ it is more convenient to adopt spherical coordinates $(x,y,z)\rightarrow (r,\theta,\phi)$. To the full laplacian in spherical coordinates is:

- In spherical coordinates Hamitlonian is more conveniently expressed in terms of angular momentum operator as opposed to linear momentum operator:


$$
\hat{H}=-\frac{\hbar^2}{2\mu}\nabla_{x,y,z}^2 = -\frac{\hbar^2}{2\mu r^2}\nabla_{\theta,\phi}^2=\frac{\hat{L}^2}{2I}
$$


- Where $I=\mu r^2$ is the moment of inertia and where identified  the angular momentum operator as:
$$
\hat{L}= -i\hbar \nabla_{\theta,\phi}
$$



### Quantum numbers $(J,m)$ for quantizing $(\theta,\phi)$ coordiante pair. 

Having written down hamitlonain we now solve it anticipating two quantum numbers for two coordinates. The eigenfunctions turn out to be well known special functions called spherical harmonics $Y(\theta,\phi)$:


$$
\hat{H}Y(\theta, \phi)=E_{J,m}Y(\theta,\phi)
$$


We are once again able to separet two angular variables and solve the esulting ODE exactly:

- The constant $\beta = \frac{2IE}{\hbar^2}=J(J+1)$ with $J=0,1,2,..$ is a quantum number which emerges from solution of $\theta$ part.
-  The $m=0,\pm1,\pm2,...J$ is the quantum number which emerges from  the solution of $\phi $ part. 


### Rotational states of molecules are quantized

Solving a rigid rotor problem, we find that eigenvalues depend only on the quantum number $J$. This makes each energy level degenerate with respect to $2J+1$ values assumed by $m_J$ quantum number. 


$$
E_J = \frac{\hbar^2}{2I}J(J+1)=BJ(J+1) \,\,\, with\,\,\, g_j=2J+1 \,\,\, degeneracy
$$


Where we have defined $B=\frac{h^2}{8\pi^2 I}$ rotational constant with units of energy. 


**Notes**

- Quantization in this equation arises from the cyclic boundary condition rather than the potential energy, which is identically zero.
- There is no rotational zero-point energy ($J = 0$ is allowed). The ground state rotational wavefunction has equal probability amplitudes for each orientation.
- The energies are independent of $m_J$. $m_J$ introduces the degeneracy of a given $J$ level.
- For non-linear molecules Eq. (\ref{eq9.165}) becomes more complicated.


**Example** What are the reduced mass and moment of inertia of $H^{35}Cl$? The equilibrium internuclear distance $R_e$ is 127.5 pm. What are the values of $L, L_z$ and $E$ for the state with $J = 1$? The atomic masses are: $m_{\textnormal{H}} = 1.673470 \times 10^{-27}$ kg and $m_{\textnormal{Cl}} = 5.806496 \times 10^{-26}$ kg.

**Solution** First we calculate the reduced mass (Eq. (\ref{eqX.25})):

$$\mu = \frac{m_{\textnormal{H}}m_{^{35}\textnormal{Cl}}}{m_{\textnormal{H}} + m_{^{35}\textnormal{Cl}}} = \frac{(1.673470\times 10^{-27}\textnormal{ kg})(5.806496\times 10^{-26}\textnormal{ kg})}{(1.673470\times 10^{-27}\textnormal{ kg}) + (5.806496\times 10^{-26}\textnormal{ kg})}$$
$$= 1.62665\times 10^{-27}\textnormal{ kg}$$


$$I = \mu R_e^2 = (1.626\times 10^{-27}\textnormal{ kg})(127.5\times 10^{-12}\textnormal{ m})^2 = 2.644\times 10^{-47}\textnormal{ kg m}^2$$

$L$ is given by Eq. (\ref{eq9.166}):

$$L = \sqrt{J(J+1)}\hbar = \sqrt{2}\left(1.054\times 10^{-34}\textnormal{ Js}\right) = 1.491\times 10^{-34}\textnormal{ Js}$$

$L_z$ is given by Eq. (\ref{eq9.163}):

$$L_z = -\hbar,0,\hbar\textnormal{ (three possible values)}$$

Energy of the $J = 1$ level is given by 

$$E = \frac{\hbar^2}{2I}J(J+1) = \frac{\hbar^2}{I} = 4.206\times 10^{-22}\textnormal{ J} = 21\textnormal{ cm}^{-1}$$

This rotational spacing can be, for example, observed in gas phase infrared spectrum of HCl.


