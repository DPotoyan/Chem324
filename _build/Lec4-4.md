---
redirect_from:
  - "/lec4-4"
title: '4.4 Angular momentum in QM'
prev_page:
  url: /Lec4-3
  title: '4.3 Rotators.'
next_page:
  url: /HarmOsc_visualize
  title: '4.5 Visualziing Harmonic Oscillator Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Outline for Lecture 4.4:  

- The rigid rotator system is introduced as a prototype for the quantization of rotational degrees of freedom in molecules. The spherical coordinate system is introduced out of the necessity of taking advantage of the spherical symmetry of the problem, which leads to a reduction of dimensionality.
- Solving the Schrodinger equation in spherical coordinates results in eigenfunctions in the form of spherical harmonics. Energy eigenvalues are found to be degenerate for one of the quantum numbers. 
- Connection with microwave spectroscopy is shown where spectral lines are predicted to occur in equal intervals. 
- The selection rule is established via the recursion relation of spherical harmonics.
- Coupling of vibrational degrees leads to rovibronic transitions and necessitates the inclusion of vibrational quantum numbers for a more accurate account of transitions. 





## Classical picture: Rotating dumbbell

The rigid rotor is a model of a rotating dumbbell: two unequal masses held together via a rigid stick.  The system is not acted upon by any external potential; hence the only energy is the kinetic energy of rotation: 

$$
K=\frac{m_1 v_1^2}{2}+\frac{m_2 v_2^2}{2}=\frac{m_1 r_1^2+m_2 r^2_2}{2}\omega^2
$$

Where we have plugged in $v_1=\omega r_1$ and $v_2=\omega_2 r$ velocities of rotation of two masses rotating with frequency $\omega$. The classical mechanical problem of two masses is once again reducible to a single reduced mass $\mu$ rotating around constant radius $r=r_1+r_2$ rotating around center of mass $m_1 r_1=m_2 r_2$.



$$
K=\frac{I \omega^2}{2}=\frac{L^2}{2I}
$$
Where $L=I \omega$ is the angular momentum and $I=\mu r^2$ moment of inertia. 



## Quantum rigid rotor and angular momentum operator 

The hamiltonian for the rigid rotor model is the kinetic energy operator of an effective mass $\mu$ wchih rotates around sphere of radius $r=const$. To incorporate constraint $r=const$ it is more convenient to adopt spherical coordinates $(x,y,z)\rightarrow (r,\theta,\phi)$. To the full laplacian in spherical coordinates is:
$$
\nabla_{r,\theta,\phi}^2 = \frac{1}{r^2} \frac{\partial }{\partial r} \Big(r^2\frac{\partial}{\partial r}\Big)+\frac{1}{r^2 sin \theta} \frac{\partial }{\partial \theta} \Big(sin \theta \frac{\partial}{\partial \theta}\Big)+\frac{1}{r^2 sin^2 \theta}\frac{\partial^2 }{\partial \phi^2}
$$

In rigid rotor approximation laplacian is reduced to an operator acting on two variables $\theta$ and $\phi$

$$
\nabla^2_{\theta,\phi} =\frac{1}{r^2}\Big[\frac{1}{sin \theta} \frac{\partial }{\partial \theta} \Big(sin \theta \frac{\partial}{\partial \theta}\Big)+\frac{1}{sin^2 \theta}\frac{\partial^2 }{\partial \phi^2} \Big ]
$$

In spherical coordinates Hamitlonian is more conveniently expressed in terms of angular momentum operator as opposed to linear momentum operator:
$$
\hat{H}=-\frac{\hbar^2}{2\mu}\nabla_{x,y,z}^2 = -\frac{\hbar^2}{2\mu r^2}\nabla_{\theta,\phi}^2=\frac{\hat{L}^2}{2I}
$$

Where $I=\mu r^2$ is the moment of inertia and where identified  the angular momentum operator as:
$$
\hat{L}= -i\hbar \nabla_{\theta,\phi}
$$



### Quantum numbers $(J,m)$ for quantizing $(\theta,\phi)$ coordiante pair. 

Having written down hamitlonain we now solve it anticipating two quantum numbers for two coordinates. The eigenfunctions turn out to be well known special functions called spherical harmonics $Y(\theta,\phi)$:
$$
\hat{H}Y(\theta, \phi)=E_{J,m}Y(\theta,\phi)
$$
We are once again able to separet two angular variables and solve thr esulting ODE exactly:
$$
\frac{sin \theta}{\theta}\frac{d}{d\theta} \Big(sin \theta\frac{d\Theta(\theta)}{d\theta}\Big)+\beta sin^2 \theta = m^2
$$

$$
\frac{d^2 \Phi(\phi)}{d \phi^2}=-m^2\Phi(\phi)
$$

- The constant $\beta = \frac{2IE}{\hbar^2}=J(J+1)$ with $J=0,1,2,..$ a quantum number which emerges from solution of $\theta$ part.

-  The $m=0,\pm1,\pm2,...J$ is the quantum number which emerged from  the solution of $\phi $ part. 

## Spherical harmonics

The eigenfunctions of the rigid rotor, $Y_{J,m}(\theta,\phi)$ are spherical harmonics that frequently occur in problems with spherical symmetry as the convenient basis of expansion. Spherical harmonics are important in many theoretical and practical applications, e.g., the representation of multipole electrostatic and electromagnetic fields, computation of [atomic orbital](https://en.wikipedia.org/wiki/Atomic_orbital) [electron configurations](https://en.wikipedia.org/wiki/Electron_configuration), representation of gravitational fields,  MRI imaging for streamline tractography, and the magnetic fields of planetary bodies and stars.

![](./images/sphhar.gif)

Spherical harmonics consist of associated Legendre polynomials ($\theta$ part) and complex exponential ($\phi part$)



### Visualization of spherical harmonics

In and physical science, [spherical harmonics](https://en.wikipedia.org/wiki/Spherical_harmonics) are defined on the surface of a sphere. The spherical harmonics are a complete set of on the sphere, and thus may be used to represent functions defined on the surface of a sphere, just as circular functions (sines and cosines) are used to represent functions on a circle via [Fourier series](https://en.wikipedia.org/wiki/Fourier_series). Like the sines and cosines in the Fourier series, the spherical harmonics may be organized by (spatial) angular frequency, as seen in the rows of functions in the illustration on the right. 

![](https://upload.wikimedia.org/wikipedia/commons/1/12/Rotating_spherical_harmonics.gif)

### Visual account of orthogonality of spherical harmonics 

Mathematically, the spherical harmonics contain alternating odd and even pairs of Legendre polynomials similar to Hermite polynomials. Visually, the spherical harmonics clearly show nodal lines with increasing quantum numbers, a pattern that we have seen on the examples of a particle in a box and harmonic oscillator. Using the symmetry argument, one can already tell that the product of any two different spherical harmonics integrated over the sphere will be zero!

$$
\int^{2\pi}_0 d \theta \int^{\pi}_0 d\phi Y^{*}_{J,m_J} \cdot Y^{*}_{J',m'_J} =\delta_{J,J'} \delta_{m_J, m'_J}
$$

<img src="./images/sphhar2.png" style="zoom:80%;" />





### Rotational states of molecules are quantized

Solving a rigid rotor problem, we find that eigenvalues depend only on the quantum number $J$. This makes each energy level degenerate with respect to $2J+1$ values assumed by $m_J$ quantum number. 


$$
E_J = \frac{\hbar^2}{2I}J(J+1)=BJ(J+1) \,\,\, with\,\,\, g_j=2J+1 \,\,\, degeneracy
$$


Where we have defined $B=\frac{h^2}{8\pi^2 I}$ rotational constant with units of energy. 





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



## Rotational-virbational transitions

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

