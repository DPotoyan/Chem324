## Wave function  

```{admonition} What you need to know
:class: note
- **We explore the meaning of a wave function which is a gateway into probabilsitc quantum-mechanical world of small systems. We learn that psi squared  is a probability distribution function.**
- **We illustrate several key quantum mechanical principles on the example of a Particle in Box. A simple toy system useful for understanding behaviour of bound states of electrons in atoms or molecules such as** 
  - **Energetic quantization**. 
  - **Probabilistic nature of quantum particle.** Having non uniform distirbutions of position when occupying different energy levels. 
  - **Uncertainy relation.** Inverse relationship between spread in position and momentum values. 
  - **Existence of zero point energy.** A minimal non-zero kinetic energy. This implies we can never freeze all motion of small particles. 
  - **Quantum-classical correspondence.** Smooth transition to classical behavior when going larger scales.   
  - **Degeneracy in energy levels.** How symmetries lead to different wave functions correpsonding to the same energy levels. 
```


### What is the meaning of a wave-function $\psi$ ? 

- In classical wave equation, wave function has a simple mechanical  interpretation: it's just the degree of distrurbance of the wave. E.g. elevation of guitar string from a rest position.  
- In contrast the the quantum wave function is not so intuitive. First wave function by itself is without direct physical meaning as it is generally a complex function. One needs to decide how to extract real quantities which are then connected to observables measurable in the experiments. 
- As It turns out, the square value of wave function that is $p(x)=\psi(x) \cdot \psi^{*}(x)$ is a probability distribution function describing likelihood of quantum objects being at different points $x$  in 1D space. For 3D space the analogous expression is $p(x,y,z)=\psi(x,y,z) \cdot \psi^{*}(x,y,z)$ and so on. 

### The importance of normalization

To be a proper probability distirbution, wave-function squared must be normalizable. Otherwise it is only proportional to probability distirbution and not equal. Normalization of $\psi^2$  means that that there is absolute certainty that quantum object exisits somehwere in space. Hence in an experiment when you search for quantum particule in an entire space you are going to find it somehwere.

Tne normalization In 1D is:

$$\int^{+\infty}_{-\infty} |\psi(x)|^2 dx= \int^{+\infty}_{-\infty} p(x)dx=1$$ 

Normalization of a wave function $\psi'$ is done by multiplying it by a constant  $\psi=N\psi'$ and plugging in the above condition to find the value of $N$. In another words normalization allows determining the constant multiplicative factor in front of wave functions.

Normalization In 3D is:

$$ \int^{+\infty}_{-\infty}  \int^{+\infty}_{-\infty}  \int^{+\infty}_{-\infty} |\psi(x,y,z)|^2dx dy dz=1$$

### What can we do with probability distribution functions (PDF)? 

- By defnitition probability distribution function $p(x) $ allows quantifying various probabilities that a quantum "particle" is located in an infinitesimal slice $[x, x+dx]$ around point $x$.  This then enables us to  find probabilities in any finite region $[a,b]$ simply by integrating:

  $$p(a<x<b)=\int_a^b |\psi(x)|^2dx$$

- In higher dimensions, e.g. 3D, we can locate particle around volume $dxdydz$ or any finite volume via a similar integration:

  $$p(a_x<x<b_x,a_y<y<b_y, a_z<z<b_z )=\int^{b_x}_{a_x}  \int^{b_y}_{a_y}  \int^{b_z}_{a_z} |\psi(x,y,z)|^2dx dy dz$$

### Computing moments of probability distirbution function

Probability distribution function contains lot of information. E.g probability of observing every posisble value of $x$.  

- But often we are interested in more reduced descriptions in terms of moments such quantifying average value (first moment) or spread in the distribution (second moment). Below we re-list the definitions of various quantities one can extract from a PDF.

|                      DEFINITION                      | NAME of moment  |
| :--------------------------------------------------: | :-------------: |
|         $$\langle x \rangle=\int p(x) x dx$$         | **1-st moment** |
|       $$\langle x^2 \rangle=\int p(x)x^2 dx$$        | **2-nd moment** |
|       $$\langle x^n \rangle=\int p(x)x^n dx$$        | **N-th moment** |
| $\sigma^2=\langle x^2 \rangle-\langle x \rangle^2  $ | **Dispersion**  |



### What about quantities which correspond to operators?

**For quantities like momentum or total energy which are no longer simple functions as in classical mechanics but operators, $\hat{p}$ and $\hat{H}$, we simply have to use operators in the defintion of moments!**

|                       Average quantity                       |               Corresponding operator               |
| :----------------------------------------------------------: | :------------------------------------------------: |
|   $\langle E \rangle=\int \psi^{*}(x) \hat{H} \psi(x)  dx$   | $\hat{H}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x)$ |
|  $\langle K \rangle=\int \psi^{*}(x) \hat{K}\psi(x)  dx  $   |   $\hat{K}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$    |
|   $\langle p \rangle=\int \psi^{*}(x) \hat{p} \psi(x)  dx$   |           $\hat{p}=-i\hbar\frac{d}{dx}$            |
| $\langle p^2 \rangle=\int \psi^{*}(x) \hat{p}^2 \psi(x)  dx$ |        $\hat{p}^2=-\hbar^2\frac{d^2}{dx^2}$        |



### Particle in a Box (PIB):

- Particle in a box is a toy model of electron/atom/molecule trapped in some region of space $[0,L]$. The positional information of a quantum "particle" is described by a quantum wave function $\psi(x)$ which is obtained by solving Schrödinger equation a simple PDE/ODE or an eigenfunction-eigenvalue problem. 
-  Wave functions are standing waves just like in a guitar on a string problem. With one major difference! Quantum-wave function has a probabilistic meaning and hence has a completely different meaning from a classical notion of a "wave".



### Classical vs Quantum particle in a box

![](https://upload.wikimedia.org/wikipedia/commons/8/8f/InfiniteSquareWellAnimation.gif)

The particle in a box (PIB) is a convenient system for illustrating the differences between classical (A) and quantum systems (B-F). The horizontal axis is position, and the vertical axis is the real part (blue) and imaginary part (red) of the wavefunction  $\psi_n(x)$. The states (B,C,D) are the eigenfunctions of Hamiltonian $n=1,2,3$.  While E and F are not. 

### What are some new ideas that we learn from PIB

1. In classical systems  a particle trapped inside a large box can move at any speed within the box and it is no more likely to be found at one position than another. However, when the well becomes very narrow (on the scale of a few nanometers), quantum effects become important. The particle may only occupy certain positive **energy levels**.

2. "Particle"  can never have **zero energy**, meaning that the particle can never "sit still". 

3. "Particle" is more likely to be found at certain positions than at others, depending on its energy level. The particle may never be detected at certain positions, known as **spatial nodes.**

   

### Solving Schrödinger quation for Particle in a Box (PIB):

The Schrödinger equation for PIB, as for any system is defined by a Hamiltonian operator which consists of potential energy with inifinitely high values at boundaries of the box and zero inside the box. This form of potential energy ensures that  the "particle" stays inside the box where it has acess only to the kinetic energy term.

![](https://upload.wikimedia.org/wikipedia/commons/1/13/Infinite_potential_well-en.svg)

Mathematically, the potential energy is: 

$$V(x=0)=V(x=L)=\infty \,\,\,\,V(0<x<L)=0 $$

The boundary conditions are:

$$\psi(x=0)=\psi(x=L)=0$$

Hamiltonian operator accounting for kinetic energy is:

$$\hat{H}= \hat{K}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$$

We have all the necessary ingeredients to solve Schrödinger equation for 1D PIB $\hat{H}\psi(x)=E\psi(x)$: 

$$-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}\psi(x)=E\psi(x),\,\,\,\,or\,\,\, \psi''(x)=-k^2 \psi(x)$$

Where we have defined $k^2=\frac{2mE}{\hbar^2}$  as a positive real number

### 1D PIB looks just like 1D guitar string problem. 

Mathematically the form of 1D PIB is the same kind fo ODE as the 1D guitar string problem. The differences are in the constant coefficients and the interpretation of wave function!

$$\psi''(x)=-k^2 \psi(x)$$

$$\psi(x)=c_1e^{ikx}+c_2e^{-ikx}=A\cos(kx)+B\sin(kx)$$

- Applying boundary condition $\psi(0)=0$ we get $A=0$ and $\psi(x)=B\sin(kx)$
- Applying boundary condition $\psi(L)=B\sin(kL)=0$ we get $kL=n\pi$ 

$$k=\frac{n\pi}{L}\,\,\, \rightarrow\,\,\, \psi(x)=B \sin(\frac{n\pi}{L}x)$$

$$k^2 = \frac{n^2\pi^2}{L^2}=\frac{2mE}{\hbar^2} \,\,\, \rightarrow\,\,\, E=\frac{n^2 h^2}{8mL^2} $$

Quantization results from trapping a wave function in space! This is why bound states have quantized energy.  Atoms, molecules, solids  all have discrete energy levels for very similar reasons.

### Normalizing wave function determines the constant multiplicative factor 

$$\int^L_0 \psi(x)^2 dx=1 $$

$$B^2 \int^L_0 \sin^2 \left(\frac{n\pi}{L}x\right)=\frac{B^2}{2} \int^L_0 \left[ 1-\cos\left(\frac{2n\pi}{L}x\right) \right]=\frac{B^2}{2}=1$$

$$B=\Big (\frac{2}{L}\Big)^{\frac{1}{2}} $$

Where we made use of $\sin^2(x)=\frac{1}{2}(1-\cos(2x))$ trig relation. 


