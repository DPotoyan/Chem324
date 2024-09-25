## Wave function  

:::{admonition} **What you need to know**
:class: note

1. **The Probabilistic Nature of the Quantum World**  
   The quantum realm operates on fundamentally probabilistic principles, where certainty is replaced by probabilities.

2. **Wave Function and Probability Distribution**  
   The absolute square of the wave function, \(|\psi|^2\), represents the probability distribution of finding a quantum particle in space and time.
:::


### What is the meaning of a wave-function $\psi$ ? 

- In the classical wave equation, the wave function has a clear mechanical interpretation: it represents the degree of disturbance in the wave. For example, it can describe the elevation of a guitar string from its resting position.

- In contrast, the quantum wave function is less intuitive. The wave function itself does not have direct physical meaning, as it is generally a complex function. To connect it to measurable quantities, we need to extract real values from it that correspond to physical observables.

- The key insight is that the absolute square of the wave function gives the probability distribution:

:::{admonition} **Probabilistic meaning of quantum wave function (square)**
:class: important

  $$p(x) = \psi^{*}(x) \cdot \psi(x) = |\psi(x)|^2$$
  
:::

- $p(x)$ is a **probability distribution function**. It is describing the likelihood of finding a quantum object at a positions x. 
- $p(x)dx$ gives the probability to find particle in a tiny part of space inside $x, x+dx$ interval.

- In three-dimensional space, the analogous expression is:

  $$p(x, y, z) = \psi(x, y, z)^{*} \cdot \psi(x, y, z)$$


### Probability refresher

- [Watch this video overview](https://www.youtube.com/watch?v=QxqxdQ_g2uw)

- **Always positive** $p(x)>0$ 
- **Must sume to one over its domain** $\int p(x)dx=1$
- **Mean** $\mu = \langle x\cdot \rangle  = \int xp(x)dx$
- **Variance** $\sigma^2 = \langle x^2\rangle - \langle x\rangle^2$
- [Probability distribution explorer](https://idiot.computer/probs/)

### Normalization of wavefunction

- For the wave function to represent a proper probability distribution, it must be normalizable. If it is not normalizable, the wave function is only proportional to a probability distribution and not equal to it.

- **Normalization** of $\psi^2$ ensures that there is absolute certainty that the quantum object exists somewhere in space. In an experiment, when searching for a quantum particle across the entire space, normalization guarantees that you will find it somewhere.

- **Normalization in 1D**:

  $$\int^{+\infty}_{-\infty} |\psi(x)|^2 dx = \int^{+\infty}_{-\infty} p(x) dx = 1$$

- To normalize a wave function $\psi'$, multiply it by a constant: $\psi = N\psi'$. The constant $N$ is determined by plugging this expression into the normalization condition. In other words, normalization helps determine the multiplicative factor in front of wave functions.

- **Normalization in 3D**:

  $$\int^{+\infty}_{-\infty} \int^{+\infty}_{-\infty} \int^{+\infty}_{-\infty} |\psi(x, y, z)|^2 dx \, dy \, dz = 1$$



### What can we do with probability distribution functions (PDF)? 

- By definition probability distribution function $p(x) $ allows quantifying various probabilities that a quantum "particle" is located in an infinitesimal slice $[x, x+dx]$ around point $x$.  This then enables us to  find probabilities in any finite region $[a,b]$ simply by integrating:

  $$p(a<x<b)=\int_a^b |\psi(x)|^2dx$$

- In higher dimensions, e.g. 3D, we can locate particle around volume $dxdydz$ or any finite volume via a similar integration:

  $$p(a_x<x<b_x,a_y<y<b_y, a_z<z<b_z )=\int^{b_x}_{a_x}  \int^{b_y}_{a_y}  \int^{b_z}_{a_z} |\psi(x,y,z)|^2dx dy dz$$


### What about quantities which correspond to operators?

**For quantities like momentum or total energy which are no longer simple functions as in classical mechanics but operators, $\hat{p}$ and $\hat{H}$, we simply have to use operators in the defintion of moments!**

|                       Average quantity                       |               Corresponding operator               |
| :----------------------------------------------------------: | :------------------------------------------------: |
|   $\langle E \rangle=\int \psi^{*}(x) \hat{H} \psi(x)  dx$   | $\hat{H}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x)$ |
|  $\langle K \rangle=\int \psi^{*}(x) \hat{K}\psi(x)  dx  $   |   $\hat{K}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$    |
|   $\langle p \rangle=\int \psi^{*}(x) \hat{p} \psi(x)  dx$   |           $\hat{p}=-i\hbar\frac{d}{dx}$            |
| $\langle p^2 \rangle=\int \psi^{*}(x) \hat{p}^2 \psi(x)  dx$ |        $\hat{p}^2=-\hbar^2\frac{d^2}{dx^2}$        |

