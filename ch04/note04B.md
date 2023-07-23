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


### Spectroscopic applications of Rigid rotor model

The energy spacing between rotational levels assume simple expression predicting integer multiples (J+1) of spectral lines for $J=0,1,2,...$

$$
\Delta E_{J+1,J} = E_{J+1}-E_{J} = B[(J+1)(J+2)-J(J+1)]=2B(J+1)
$$

Often in spectroscopy application wavenumbers are adopted which we indicate by placing tilde on energy:

$$
\tilde{\nu}_{J+1,J} =\frac{1}{\lambda} = \frac{\Delta E}{hc} = 2\tilde{B}(J+1)
$$

Where rotational constant has units of inverse wavelength [cm^{-1}]  $\tilde{B}=\frac{h^2}{8\pi^2 I c}$



### Spectral lines are predicted to be equidistant!

Rigid rotor model makes a very specifci prediction about spectral lines: they are to be equally spaced. In other words difference between adjacent frequency of tranisitons is a constnat number:

$$
\tilde{\nu}_{J+2,J+1}-\tilde{\nu}_{J+1,J}=2\tilde{B}
$$

Thus be measuring this spectral line difference, we can extract structural information about the molecule, e.g. compute the moment of inertia!



### Rotational-virbational transitions

Rotational transitions often accompany the transitions in vibrational levels. The simplest  model for joint vibrational and rotational transitions is a combination of a harmonic oscillator with rigid rotor models:

$$
E_{v,J} = h\nu(n+1/2)+BJ(J+1)
$$

The selection rules for harmonic oscillator and rigid rotor are $\Delta v =\pm 1$ and $\Delta J \pm 1$, respectively. 

![](./images/rovib1.png)



### Ro-vibrational spectra, R, P and Q branches

Often times we are interested in transitions among rotational levels that accompany excitation from ground vibrational state $v=0\rightarrow v=1 $. The transitions with $\Delta J=+1$ and $\Delta J=-1$ appear as two branches in the spectrum known as R and P   branch, respectively. The Q-branch $\Delta J =0$ is predicted to be absent because it is forbidden by the selection rule of the rigid rotor model. 

$$
\tilde{\nu}_{\Delta J=+/-1} = E_{v+1,J\pm1} - E_{v,J} = \tilde{\omega} \pm 2\tilde{B}(J+1)
$$

![](./images/branch.jpg)



### Correction #1 rovibrational coupling

One correction one can make to the rotational-vibrational model is to include the effect of coupling between rotational and vibrational degrees of freedom. When exciting molecules to higher vibrational states, it is reasonable to expect that rotational parameters will be impacted as a result of changes in the average intra-nuclear distance, among other things. This can be accounted for by making rotational constant dependent on vibrational level v. $B\rightarrow B_v$. The v dependence is captured via the following expression showing that rotational constant is a linearly decreasing function of v!

$$
B_v = B_e-\alpha_e(v+1/2)
$$

The expression of energy with these correction would then be:

$$
E_{v,J} = h\nu(v+1/2)+B_vJ(J+1)
$$

$$
\tilde{\nu}_{\Delta J=+1} = \tilde{\omega} + 2\tilde{B_1}+(3\tilde{B_1}-\tilde{B}_0)J+(\tilde{B_1}-\tilde{B}_0)J^2
$$

$$
\tilde{\nu}_{\Delta J=-1} = \tilde{\omega} - (\tilde{B_1}+\tilde{B}_0)J+(\tilde{B_1}-\tilde{B}_0)J^2
$$



### Correction #2 the unharmonicity/unrigdity term

Similiar to the first order correction we introduced for harmonic oscillator in the form of unharmonicity term  we can now also improve rigid rotor model by accounting for the fact that chemical bonds are not trully rigid: 

$$
\tilde{E}_{v,J} =\Big[\omega_e (v+1/2)- x_e\omega_e(v+1/2)^2\Big] + \Big[ BJ(J+1)-DJ^2 (J+1)^2 \Big ]
$$

Where constant D is called the **centrifugal distortion constant.** and is typically a small number $D<<1$

