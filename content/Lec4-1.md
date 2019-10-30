## Outline for Lecture 4.0:  

## Particle in a Box (PIB):

- Particle in a box is a toy model of electron/atom/molecule trapped in some region of space $[0,L]$. The positional information of a quantum "particle" is described by a quantum wave function $\psi(x)$ which is obtained by solving Schrodinger equation a simple PDE/ODE or an eigenfunction-eigenvalue problem. 
-  Wave functions are standing waves just like in a guitar on a string problem. With one major difference! Quantum-wave function has a probabilistic meaning and hence has a completely different meaning from a classical notion of a "wave"



### Classical vs Quantum particle in a box

![](https://upload.wikimedia.org/wikipedia/commons/8/8f/InfiniteSquareWellAnimation.gif)

The Partile in a box(PIB) is a convenient system for illustrating the differences between classical (A) and quantum systems (B-F). The horizontal axis is position, and the vertical axis is the real part (blue) and imaginary part (red) of the wavefunction  $\psi_n(x)$. The states (B,C,D) are the eigenfunctions of Hamitlonian n=1,2,3.  While E and F are not. 

### Whatare some new ideas that we learn from PIB

1. In classical systems  a particle trapped inside a large box can move at any speed within the box and it is no more likely to be found at one position than another. However, when the well becomes very narrow (on the scale of a few nanometers), quantum effects become important. The particle may only occupy certain positive **energy levels**.

2. "Particle"  can never have **zero energy**, meaning that the particle can never "sit still". 

3. "Particle" is more likely to be found at certain positions than at others, depending on its energy level. The particle may never be detected at certain positions, known as **spatial nodes.**

   

### Solving Schoridnger quation for Particle in a Box (PIB):

The Schrodinger equation for PIB, as for any system is definited by a Hamitlonian operator which consists of potential energy with inifinitely high values at boundaries of the box and zero inside the box. This form of potential energy ensures that  the "particle" stays inside the box where it has acess only the kinetic energy term.

![](https://upload.wikimedia.org/wikipedia/commons/1/13/Infinite_potential_well-en.svg)

Mathematically, the potential energy is: 

$$V(x=0)=V(x=L)=\infty \,\,\,\,V(0<x<L)=0 $$

The boundary conditions are:

$$\psi(x=0)=\psi(x=L)=0$$

Hamilotnian operator accounting for kinetic energy is:

$$\hat{H}= \hat{K}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$$

We have all the necessary ingeredients to solve Schrodinger equation for 1D PIB $\hat{H}\psi(x)=E\psi(x)$: 



$$-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}\psi(x)=E\psi(x),\,\,\,\,or\,\,\, \psi''(x)=-k^2 \psi(x)$$



Where we have defined $k^2=\frac{2mE}{\hbar^2}$  as a positive real number



### 1D PIB looks just like 1D guitar string problem. 

Mathematically the form of 1D PIB is the same kind fo ODE as the 1D guitar string problem. The differences are in the constant coefficients and the interpartation of wave function!

$$\psi''(x)=-k^2 \psi(x)$$

$$\psi(x)=c_1e^{ikx}+c_2e^{-ikx}=Acos(kx)+Bsin(kx)$$

- Applying boundary condition $\psi(0)=0$ we get A=0 and $\psi(x)=Bsin(kx)$
- Applying boundary condition $\psi(L)=Bsin(kL)=0$ we get $kL=n\pi$ 

$$k=\frac{n\pi}{L}\,\,\, \rightarrow\,\,\, \psi(x)=B sin(n\pi \frac{x}{L})$$



$$k^2 = \frac{n^2\pi^2}{L^2}=\frac{2mE}{\hbar^2} \,\,\, \rightarrow\,\,\, E=\frac{n^2 h^2}{8mL^2} $$

Quantization results from trapping a wave function in space! This is why bound states have quantized energies.  Atoms, molecules, solids  all have discrete energy levels for very similar reasons.



### Normalizing wave function determines the constant multiplicative factor 

$$\int^L_0 \psi(x)^2 dx=1 $$

$$B^2 \int^L_0 sin^2 \Big(\frac{n\pi x}{L}\Big)=\frac{B^2}{2} \int^L_0 [1-cos\Big(\frac{2n\pi x}{L}\Big) ]=\frac{B^2}{2}=1$$

$$B=\Big (\frac{2}{L}\Big)^{1/2} $$

Where we made use of $sin^2x=\frac{1}{2}(1-cos(2x))$ trig relation. 