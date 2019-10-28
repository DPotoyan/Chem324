---
redirect_from:
  - "/lec4-2"
title: '4.2 Oscillators.'
prev_page:
  url: /features/markdown
  title: '4.1 Particle in a Box.'
next_page:
  url: /features/markdown
  title: '4.3 Rotators.'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Outline for Lecture 4.2:  Quantum Oscillators 

In this section we study quantum mechanical version of [harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator). Harmonic oscillators have ubqiutuous presence in everyday world: beads bound by a spring which vibrate around equilibirum positions. Turns out beads on a pring is remarkably common in microsocpic world as nuclie of atoms in solids or molecules are in some sense "quantum beads" vibrating around equilibriu position of "quantum springs". The distinction between quantum vs classical regimes will again be highly illuminating about the role of quantum effects on small scales. The key topics we will learn are:

- **Quantization of vibrational degrees of freedom in molecules.** This has implication for Infrared and raman spectroscopies, molecular mechancis and condensed matter in general.  
- **Existence of zero point energy and tunneling.** We have seen this on PIB example and will see again on the example of harmonic oscillator. 
- **Hermite Polynomials as orthogonal eigenfunctions.** This will be our first foray into the world od special functions. 
- **Raising and lower operators as elegant way of solving problems.** This will be our first introduction to raising and lowering operators which provide highly elegant way of solving problems in quantum mechanics. 
- **Effects of unharmonicity.** We will see the impact on energy levels of harmonic oscillators when one goes beyond harmonic approximation. 



## Bead, spring and a wall. 

The classical **harmonic oscillator** is a system of bead attached to a wall with a spring. When bead is displaced from its equilibrium or resting position $r_0$ to some point $r$, experiences a restoring force $F$ proportional to the displacement $x=r-r_0$:

$$ F=-kx$$

The above expression is also known as **Hooke's law**, where minus sign indicates that the direction of force is always towards restoring equilibrium location. The constant k characterizes stiffness of the spring and is called **spring constant.**

![](/Users/potoyan/Dropbox/LECTURES/QM_chem324/Chem324/content/images/harm-osc1.png)

![](https://askeyphysics.files.wordpress.com/2011/08/solveharmonic.gif)



## Solving harmonic oscillator problem

The classical equation of motion for a one-dimensional simple harmonic oscillator with a particle of mass mm attached to a spring having spring constant kk is

$$m \ddot x=−kx$$

$$m \ddot x+kx = 0 \,\,\,\,\rightarrow \,\,\,\, \ddot{x}+\omega^2 x =0$$

whwhere we have intorduced constant $\omega$ which we will see is the frequency oscillations:

$$\omega=\Big(\frac{k}{m}\Big)^{1/2}$$

The differneital equation is a simple second order, linear ODE  which can be solved by a standard trick of pluggin exponential $x(t)=e^{\alpha t}$ and convertin the problem to algebraic equation. The solution is

$$x(t)= A sin(\omega t+\phi)$$ 

Where the two constnants  are: $A$ the amplitude of oscillations and $\phi$ is constant specifying the initial position of the bead. 

## Conservative system 

In the simple harmonic oscillator problem $F$ is the only force acting on the system.  We way that the system is conservative becasue the kinetic and potential energies keep being interconverted with no amount of total energy being of the system being dissipated into the environment. This will be true in a vaccuum where there is no friction.  For a simple harmonic oscillatorthe oscillations go on forever with position $x(t)$ velocity $v=\dot{x}(t)$ and acceleration $a=\ddot{x(t)}$ with same constant frequency $\omega$ but with different amplitudes.  

<iframe src='https://gfycat.com/ifr/CheapSelfishAlbacoretuna' frameborder='0' scrolling='no' allowfullscreen width='240' height='224'></iframe><p> <a href="https://gfycat.com/cheapselfishalbacoretuna"></a></p>

## Energy of the harmonic oscillator

In classical mechanics the force and the potential energy of a conservative system are related via the formula:

$$F = - \frac{\partial V(x)}{\partial x} $$

THis means the steeper the potential the higher the force and minus sign indicates that force is restoring the equilibrium position. 

The potential energy can be obtained by integrating:

$$ V(x)= - \int F dx = - \int (-kx) dx =\frac{kx^2}{2}+C$$

Thus the potential energy for a simple harmonci oscillator is a parabola. Since potential energy is measured relative to constnat we set $C=0$ that is potential energy of equilibrium state is set to be the zero. 

$$V(x)=\frac{kx^2}{2}$$

Kinetic energy is the familiar expression expressed either via momentum $p=mv$ or velocity $v=\dot{x}$

$$K=\frac{p^2}{2m} = \frac{m \dot{x}^2}{2}$$



## Diatomic molecule and two-body problem

