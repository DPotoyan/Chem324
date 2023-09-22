## Wave function  

```{admonition} What you need to know
:class: note
- Quantum world is probabilistic in its nature 
- Absolute value of wave function squared is a probability distribution function to find quantum object in space and time
- A simple toy system, like Particle in a Box is introduced to qualitatively explain behavior of electrons bound inside atom and molecules.
  - On the example of PIB we see **Energetic quantization**. 
  - **Probabilistic nature of quantum particle.** Having non uniform distributions over position with existence of nodal points. 
  - **Uncertainty relation.** Inverse relationship between spread in position and momentum values. 
  - **Existence of zero point energy.** A minimal non-zero kinetic energy. This implies we can never freeze all motion of small particles. 
  - **Quantum-classical correspondence.** Smooth transition to classical behavior when going larger scales.   
  - **Degeneracy in energy levels.** How symmetries lead to different wave functions corresponding to the same energy levels. 
```
### What is the meaning of a wave-function $\psi$ ? 

- In classical wave equation, wave function has a simple mechanical interpretation: it's just the degree of disturbance of the wave. E.g. elevation of guitar string from a rest position.  
- In contrast the the quantum wave function is not so intuitive. First wave function by itself is without direct physical meaning as it is generally a complex function. One needs to decide how to extract real quantities which are then connected to observables measurable in the experiments. 
- It turns out that the absolute value of wave function squared that is 
$$p(x)=\psi(x) \cdot \psi^{*}(x)$$ 

- $p(x)$ is a probability distribution function describing likelihood of quantum objects being at different points $x$. 

- For 3D space the analogous expression is 

$$p(x,y,z)=\psi(x,y,z) \cdot \psi^{*}(x,y,z)$$ 

### The importance of normalization

- To be a proper probability distribution, wave-function squared must be normalizable. Otherwise it is only proportional to probability distribution and not equal. 
- Normalization of $\psi^2$  means that that there is absolute certainty that quantum object exists somehwere in space. Hence in an experiment when you search for quantum particle in an entire space you are going to find it somewhere.

Normalization in 1D:

$$\int^{+\infty}_{-\infty} |\psi(x)|^2 dx= \int^{+\infty}_{-\infty} p(x)dx=1$$ 

Normalization of a wave function $\psi'$ is done by multiplying it by a constant  $\psi=N\psi'$ and plugging in the above condition to find the value of $N$. In another words normalization allows determining the constant multiplicative factor in front of wave functions.

Normalization in 3D:

$$ \int^{+\infty}_{-\infty}  \int^{+\infty}_{-\infty}  \int^{+\infty}_{-\infty} |\psi(x,y,z)|^2dx dy dz=1$$

### What can we do with probability distribution functions (PDF)? 

- By definition probability distribution function $p(x) $ allows quantifying various probabilities that a quantum "particle" is located in an infinitesimal slice $[x, x+dx]$ around point $x$.  This then enables us to  find probabilities in any finite region $[a,b]$ simply by integrating:

  $$p(a<x<b)=\int_a^b |\psi(x)|^2dx$$

- In higher dimensions, e.g. 3D, we can locate particle around volume $dxdydz$ or any finite volume via a similar integration:

  $$p(a_x<x<b_x,a_y<y<b_y, a_z<z<b_z )=\int^{b_x}_{a_x}  \int^{b_y}_{a_y}  \int^{b_z}_{a_z} |\psi(x,y,z)|^2dx dy dz$$

### Computing moments of probability distirbution function

- Probability distribution function contains lot of information. E.g probability of observing every possible value of $x$.  

- But often we are interested in more reduced descriptions in terms of moments such quantifying average value (first moment) or spread in the distribution (second moment). Below we re-list the definitions of various quantities one can extract from a PDF.

|                      DEFINITION                      | NAME of moment  |
| :--------------------------------------------------: | :-------------: |
|         $\langle x \rangle=\int p(x) x dx$         | **1-st moment** |
|       $\langle x^2 \rangle=\int p(x)x^2 dx$        | **2-nd moment** |
|       $\langle x^n \rangle=\int p(x)x^n dx$        | **N-th moment** |
| $\sigma^2=\langle x^2 \rangle-\langle x \rangle^2$   | **Dispersion**  |



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
- Wave functions are standing waves just like in a guitar on a string problem. With one major difference! Quantum-wave function has a probabilistic meaning and hence has a completely different meaning from a classical notion of a "wave".



### Classical vs Quantum particle in a box

:::{figure-md} markdown-fig
<img src="https://upload.wikimedia.org/wikipedia/commons/8/8f/InfiniteSquareWellAnimation.gif" alt="PIB-wiki" class="bg-primary mb-1" width="300px">

The particle in a box (PIB) is a convenient system for illustrating the differences between classical (A) and quantum systems (B-F). The horizontal axis is position, and the vertical axis is the real part (blue) and imaginary part (red) of the wavefunction  $\psi_n(x)$. The states (B,C,D) are the eigenfunctions of Hamiltonian $n=1,2,3$.  While E and F are not. 
:::


### What are some new ideas that we learn from PIB

1. In classical systems  a particle trapped inside a large box can move at any speed within the box and it is no more likely to be found at one position than another. However, when the well becomes very narrow (on the scale of a few nanometers), quantum effects become important. The particle may only occupy certain positive **energy levels**.

2. "Particle"  can never have **zero energy**, meaning that the particle can never "sit still". 

3. "Particle" is more likely to be found at certain positions than at others, depending on its energy level. The particle may never be detected at certain positions, known as **spatial nodes.**

   

### Solving Schrödinger quation for Particle in a Box (PIB):

The Schrödinger equation for PIB, as for any system is defined by a Hamiltonian operator which consists of potential energy with infinitely high values at boundaries of the box and zero inside the box. This form of potential energy ensures that  the "particle" stays inside the box where it has acess only to the kinetic energy term.

:::{figure-md} markdown-fig
<img src="https://upload.wikimedia.org/wikipedia/commons/1/13/Infinite_potential_well-en.svg" alt="pib1" class="bg-primary mb-1" width="300px">

Particle in a box subject to infinitely high potential walls
:::


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

### Wave functions must be normalized

Now we will see how requirement of normalization determines the constant coefficient B. 

$$\int^L_0 \psi_n(x)^2 dx=1 $$


$$\psi_n^*(x) \psi_n(x)  = B_n^*B_n \sin^2\frac{n\pi x}{a}$$

We will make use of $\sin^2(x)=\frac{1}{2}(1-\cos(2x))$ trig relation to evaluate integral

$$B_n^2 \int^L_0 \sin^2 \left(\frac{n\pi}{L}x\right)=\frac{B_n^2}{2} \int^L_0 \left[ 1-\cos\left(\frac{2n\pi}{L}x\right) \right]=\frac{B_n^2}{2}=1$$

$$B_n=\Big (\frac{2}{L}\Big)^{\frac{1}{2}} $$

Not that normalization coefficient turned out to be independent of $n$.

:::{admonition} Example: Compute the probability of observing the particle in a box being in the domain $\frac{a}{3} \leq x \leq \frac{2a}{3}$. 
:class: tip, dropdown

Since the square of the wave function is a probability function, we can determine the probability of observing a particle in a particular domain using the relationship

$$\begin{equation}
\text{Prob}(x_1 \leq x \leq x_2) = \int_{x_1}^{x_2}P(x)dx = \int_{x_1}^{x_2} \psi^*(x)\psi(x)dx
\end{equation}$$

We simply use the above equation and the normalized particle in a box wave function:

$$\begin{align}
\text{Prob}(\frac{a}{3} \leq x \leq \frac{2a}{3}) = \frac{2}{a}\int_{\frac{a}{3}}^{\frac{2a}{3}} \sin^2\frac{n\pi x}{a}dx
\end{align}$$

We will use the definite integral of $\sin^2ax$ from a table:

$$\begin{equation}
\int\sin^2axdx = \frac{x}{2} - \frac{\sin2ax}{4a}
\end{equation}$$

Perform $u = $ substition of the integral above to get into the table form

$$\begin{align}
\text{Prob}(\frac{a}{3} \leq x \leq \frac{2a}{3}) &= \frac{2}{a}\left[ \frac{x}{2} - \frac{\sin\frac{2n\pi x}{a}}{\frac{4n\pi}{a}}\right]_{\frac{a}{3}}^{\frac{2a}{3}} \\
&= \frac{2}{a}\left[ \frac{x}{2} - \frac{a\sin\frac{2n\pi x}{a}}{4n\pi}\right]_{\frac{a}{3}}^{\frac{2a}{3}} \\
&= \frac{2}{a}\left[ \frac{a}{3} - \frac{a\sin\frac{4n\pi}{3}}{4n\pi} - \frac{a}{6} + \frac{a\sin\frac{2n\pi }{3}}{4n\pi}\right] \\
&= 2\left[ \frac{1}{6}  + \frac{\sin\frac{2n\pi }{3} - \sin\frac{4n\pi}{3}}{4n\pi}\right]
\end{align}$$
:::


### Computing Average Properties from a Wave Function

Because of the probabilistic interpretation of the wave function, average properties can be computed from the wave function.  The general formula is

$$\begin{equation}
<A> = \int \psi^*(x)\hat{A}\psi(x)dx
\end{equation}$$

where $\hat{A}$ is any operator.  This could be momentum, kinetic energy, etc.
    
Let's look at a few examples.  
    
1. Compute the average value of $x^2$ for a particle in a box
2. Compute the average energy for a particle in a box
3. Compute the average momentum for a particle in a box

:::{admonition} Example: Compute he average of $x^2$ for a particle in a box
:class: tip, dropdown

To compute the average value of $x^2$ we start by writing the integral expression

$$\begin{equation}
\langle x^2 \rangle = \int \psi^*(x) x^2 \psi(x)dx
\end{equation}$$

For the particle in a box, we can limit the domain, and thus the bounds of integration, to $0\leq x \leq a$.  We can also set $\psi_n(x) = \sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}$.

Thus, for a particle in a 1D box of size $a$ we get

$$\begin{align}
\langle x^2 \rangle &= \int_0^a \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) x^2 \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)dx \\
&= \frac{2}{a} \int_0^a x^2 \sin^2\frac{n\pi x}{a}dx
\end{align}$$

From an integral table we find that

$$\begin{equation}
\int x^2\sin^2\alpha xdx = \frac{x^3}{6} - \left(\frac{x^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha x - \frac{x\cos 2\alpha x}{4\alpha^2} + C
\end{equation}$$

We use this equation with $\alpha = \frac{n\pi}{a}$ and get

$$\begin{align}
\langle x^2 \rangle &= \int_0^a \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) x^2 \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)dx \\
&= \frac{2}{a} \int_0^a x^2 \sin^2\frac{n\pi x}{a}dx \\
&= \frac{2}{a}\left[ \frac{x^3}{6} - \left(\frac{x^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha x - \frac{x\cos 2\alpha x}{4\alpha^2}\right]_0^a \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \left(\frac{a^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha a - \frac{a\cos 2\alpha a}{4\alpha^2} \right] \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \left(\frac{a^2}{4\frac{n\pi}{a}} - \frac{1}{8\left(\frac{n\pi}{a}\right)^3}\right)\sin2\frac{n\pi}{a} a - \frac{a\cos 2\frac{n\pi}{a} a}{4\left(\frac{n\pi}{a}\right)^2} \right] \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \frac{a^3}{\left(2n\pi\right)^2} \right] \\
&=  \frac{a^2}{3} - \frac{a^2}{2\left(n\pi\right)^2} 
\end{align}$$

This result, combined with the result for $\langle x \rangle$, can be used to determine $\sigma_x$, the standard deviation of particle deviation:

$$\begin{equation}
\sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} = \frac{a}{2\pi n}\sqrt{\frac{\pi^2n^2}{3} -2}
\end{equation}$$
:::



:::{admonition} Compute the average Energy of Particle in a Box
:class: tip, dropdown

The average energy of the particle in a box is a special case of computing an average quantity.  We will start by writing out the standard definition of computing and average from a wavefunction

$$\begin{equation}
\langle E \rangle = \int_0^a \psi_n^*(x)\hat{E}\psi_n(x)dx
\end{equation}$$

where $\hat{E}$ is the total energy operator.  We know the total energy operator by another symbol, namely $\hat{E} = \hat{H}$.  We plug this into the above equation to get

$$\begin{equation}
\langle E \rangle = \int_0^a \psi_n^*(x)\hat{H}\psi_n(x)dx.
\end{equation}$$

We now recognize that, for the particle in a box wavefunctions that we are discussion these were derived from the Schrodinger equation

$$\begin{equation}
\hat{H}\psi_n(x)  = E_n\psi_n(x)
\end{equation}$$

where $E_n$ is a scalar.  Thus, for the average energy we get

$$\begin{align}
\langle E \rangle &= \int_0^a \psi_n^*(x)\hat{H}\psi_n(x)dx \\
&=\int_0^a \psi_n^*(x)E_n\psi_n(x)dx \\
&=E_n\int_0^a \psi_n^*(x)\psi_n(x)dx \\
&= E_n
\end{align}$$

The last equality holding because the wave functions are normalized.
:::


:::{admonition} Example: Compute Average momentum
:class: tip, dropdown

To compute the average momentum of a particle in a 1D box we start in the usual way

$$\begin{equation}
\langle p \rangle = \int_0^a \psi_n^*(x)\hat{p}\psi_n(x)dx
\end{equation}$$

Recall that the momentum operator in one dimension is given by

$$\begin{equation}
\hat{p}_x = -i\hbar\frac{d}{dx}
\end{equation}$$

We now substitute this into the  above equation and solve

$$\begin{align}
\langle p \rangle &= \int_0^a \psi_n^*(x)\left(-i\hbar\frac{d}{dx}\right)\psi_n(x)dx \\
&= -\frac{2i\hbar}{a}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\frac{d}{dx}\left(\sin\left(\frac{n\pi x}{a}\right)\right)dx \\
&= -\frac{2i\hbar}{a}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\frac{n\pi}{a}\cos\left(\frac{n\pi x}{a}\right)dx \\
&= -\frac{2in\pi\hbar}{a^2}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\cos\left(\frac{n\pi x}{a}\right)dx \\
&= 0
\end{align}$$

where the last equality can be found in an integral table.

So the average momentum of a particle in a box is zero.  This is because it is equally probable for the particle to be moving forward and backwards.
:::


### Problems

