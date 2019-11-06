---
redirect_from:
  - "/lec4-3"
title: '4.3 Rotators.'
prev_page:
  url: /Lec4-2
  title: '4.2 Oscillators.'
next_page:
  url: /HarmOsc_visualize
  title: '4.4 Visualziing Harmonic OScillator Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Outline for Lecture 4.0:  

- Rigid body system is introduced as a prototype for quantization of rotational degrees of freedom in molecules.
- Spherica coordinate system is introduced out of necessity of taking advantage of spherical symmetry of the problem which leads to reduction of dimensionality.
- Solving Schrodinger equation in spherical coordinates results in eigenfunctions in the form of spherical harmonics. Energy eigenvalues are found to be degenerate with respect to one of the quantum numbers. 
- Connection with microwave spectroscopy is shown where spectral lines are predicted to be occur in equal intervals. 
- Selection rule is established via recursion relation of spherical harmonics.
- Coupling of virbational degrees leads to rovibronic transitions and neccessitates inclsuion of virbational quantum numbers for more accurate account of transitions. 





### Classical picture: Rotating dumbell

Rigid rotor is a model of a rotating dumbbell: two unequal masses held together via a rigid stick.  The system is not acted upon by any external potential hence the only energy is the kinetic energy of rotation: 

$$
K=\frac{m_1 v_1^2}{2}+\frac{m_2 v_2^2}{2}=\frac{m_1 r_1^2+m_2 r^2_2}{2}\omega^2
$$

Where we have plugged in $v_1=\omega r_1$ and $v_2=\omega_2 r$ velocoities of rotation of two masses rotating with frequency $\omega$. The classical mechanical problem of two masses is once again reducible to a single reduced mass $\mu$ rotating around constant radius $r=r_1+r_2$ rotating around center of mass $m_1 r_1=m_2 r_2$.



$$
K=\frac{I \omega^2}{2}=\frac{L^2}{2I}
$$
Where $L=I \omega$ is the angular momentum and $I=\mu r^2$ moment of inertia. 



### Quantum rigid rotor and angular momentum operator 

We can write down the hamiltonain for rigid rotor model which corresponds to operator of kinetic energy and which can also be written in terms of angular momentum operator to make correspondence with classical rigid rotor. 

$$
\hat{H}=-\frac{\hbar^2}{2\mu}\nabla^2=\frac{\hat{L}^2}{2I}
$$

Since internuclear distance is fixed in rigid rotor approximation $r=const$ it is convenient to use spherical coordinates which eliminates raidal coordinate from the problem. The laplacian in spherical coordinates is:

$$
\nabla^2 = \frac{1}{r^2} \frac{\partial }{\partial r} \Big(r^2\frac{\partial}{\partial r}\Big)+\frac{1}{r^2 sin \theta} \frac{\partial }{\partial \theta} \Big(sin \theta \frac{\partial}{\partial \theta}\Big)+\frac{1}{r^2 sin^2 \theta}\frac{\partial^2 }{\partial \phi^2}
$$

And in rigid rotor approximation it simplifies to an oeprator acting on two variables $\theta$ and $\phi$

$$
\nabla^2_{\theta,\phi} =\frac{1}{r^2}\Big[\frac{1}{sin \theta} \frac{\partial }{\partial \theta} \Big(sin \theta \frac{\partial}{\partial \theta}\Big)+\frac{1}{sin^2 \theta}\frac{\partial^2 }{\partial \phi^2} \Big ]
$$

$$
\hat{H} = -\frac{\hbar^2}{2\mu r^2}\nabla^2_{\theta,\phi}=-\frac{\hbar^2 \nabla_{\theta,\phi}^2}{2I}=\frac{\hat{L}^2}{2I}
$$

The angular momentum part of the hamiltonian expressed in sperhical coordinates can now be clearly recognized as: 
$$
\hat{L}=i\hbar \nabla_{\theta,\phi}
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






























