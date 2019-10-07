## Outline for Lecture 3.1: Probabilistic meaning of wave function and toy systems of quantum mechanics.  

- **We explore the meaning of a wave function which is a gateway into probabilsitc quantum-mechanical world of small systems. We learn that psi squared  is a probability distribution function.**
- **We illustrate several key quantum mechanical principles on the example of a Particle in Box. A simple toy system useful for understanding behaviour of bound states of electrons in atoms or molecules such as: ** 
  - **Energetic quantization**. 
  - **Probabilistic nature of quantum particle.** Having non uniform distirbutions of position when occupying different energy levels. 
  - **Uncertainy relation.** Inverse relationship between spread in position and momentum values. 
  - **Existence of zero point energy.** A minimal non-zero kinetic energy. This implies we can never freeze all motion of small particles. 
  - **Quantum-classical correspondence. ** Smooth transition to classical behavior when going larger scales.   
  - **Degeneracy in energy levels.** How symmetries lead to different wave functions correpsonding to the same energy levels. 



## What is a meaning of a wave-function $\psi$ ? 

- In classical wave equation, wave function has a simple mechanical  interpretation: its just the degree of distrurbance of the wave. E.g elevation of guitar string from a  position of rest.  
- In contrast the the quantum wave function is not so intutive. First wave function by itself is without direct physical meaning as it is generally a complex function. One needs to decide how to extract real quantities which are then connected to observables measurable in the experiments. 
- As It turns out, the square value of wave function that is $$p(x)=\psi(x) \cdot \psi^{*}(x)$$ is a probability distribution function describing likeliehood of quantum onbjects being at different points x  in 1D space. For 3D space the analogus expression is $$p(x,y,z)=\psi(x,y,z) \cdot \psi^{*}(x,y,z)$$ and so on. 



### The Importance of normalization

To be a proper probability distirbution, wave-function squared must be normalizable. Otherwise it is only proportional to probability distirbution and not equal. Normalization of $|\psi|^2$  means that that there is absolute certainty that quantum object exisits somehwere in space. Hence in an experiment when you search for quantum particule in an entire space you are going to find it somehwere.

Tne normalization In 1D is:

$$\int^{+\infty}_{-\infty} |\psi(x)|^2 dx= \int^{+\infty}_{-\infty} p(x)dx=1$$  

Normalization of a wave function $\psi'$ is done by multiply it by a constant  $\psi=N\psi'$ and plugging in the above condition to find the value of N. In another words normalizationa allows determining the constant multiplicative factors in front of wave functions

Normalization In 3D is:

$$ \int^{+\infty}_{-\infty}  \int^{+\infty}_{-\infty}  \int^{+\infty}_{-\infty} |\psi(x,y,z)|^2dx dy dz=1$$



### What can we do with probability distirbution functions (pdf)? 

- By defnitition probability distirbution function $p(x) $ allows quantifying various probabilities that a quantum "particle" is located in an infetisemal slice $[x, x+dx]$ around point $x$.  This then enables us to  find probabilities in any finite region [a,b] simply by integrating:

  

  $$p(a<x<b)=\int^{b}_a |\psi(x)|^2dx$$

  

- In higher dimensions, in 3D we can locate particle around volume $dxdydz$ or any finite volume by a a similiar integration:

  

  $$p(a_x<x<b_x,a_y<y<b_y, a_z<z<b_z )=\int^{b_x}_{a_x}  \int^{b_y}_{a_y}  \int^{b_z}_{a_z} |\psi(x,y,z)|^2dx dy dz$$



### Computing moments of probability distirbution function

Probability distribution function contains lot of information. E.g probability of observing every posisble value of **x.**  

- But often we are interested in more reduced descriptions in terms of moments such quantifying average value (first moment) or spread in the distribution (second moment). Below we re-list the definitions of various quantities one can extract from a pdf.

|                      DEFINITION                      | NAME of moment  |
| :--------------------------------------------------: | :-------------: |
|        $$\langle x \rangle = \int p(x) x dx$$        | **1-st moment** |
|      $$\langle x^2 \rangle = \int p(x)x^2 dx$$       | **2-nd moment** |
|      $$\langle x^n \rangle = \int p(x)x^n dx$$       | **N-th moment** |
| $\sigma^2=\langle x^2 \rangle-\langle x \rangle^2  $ | **Dispersion**  |



### What about quantities which correspond to operators?

**For quantities like momentum or total energy which are no longer simple functions as in classical mechancis but operators, $\hat{p}$ and $\hat{H}$, we simply have to use operators in the defintion of moments!**

|                       Average quantity                       |                 Corresponding operator                 |
| :----------------------------------------------------------: | :----------------------------------------------------: |
| $$\langle E \rangle = \int \psi^{*}(x) \hat{H} \psi(x)  dx$$ | $$\hat{H}= -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x) $$ |
| $$\langle K \rangle = \int \psi^{*}(x) \hat{K}\psi(x)  dx  $$ |    $$\hat{K}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$$     |
| $$\langle p \rangle = \int \psi^{*}(x) \hat{p} \psi(x)  dx$$ |            $$\hat{p}=-i\hbar\frac{d}{dx}$$             |
| $$\langle p^2 \rangle = \int \psi^{*}(x) \hat{p}^2 \psi(x)  dx$$ |        $$\hat{p}^2=-\hbar^2\frac{d^2}{dx^2} $$         |

