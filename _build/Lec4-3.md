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

Where we have plugged in $v_1=\omega r_1$ and $v_2=\omega_2 r$ velocoities of rotation of two masses rotating with frequency $\omega$. The classical mechanical problem of two masses is once again reducible to a single reduced mass $\mu$ rotating around constant radius $r=r_1+r_2$ rotating around center of mass $m_1 r_1=m_2 r_2$


$$
K=\frac{I \omega^2}{2}=\frac{L^2}{2I}
$$
Where $L=I \omega$ is the angular momentum and $I=\mu r^2$ moment of inertia. 

### Quantum picture: Angular momentum operator 

Quantum mechanical version of rigid rotor problem is formualted by simply replacing classical quantities with their corresponding quantum mechanical operators:
$$
\hat{H}=\frac{\hat{L}^2}{2I}
$$