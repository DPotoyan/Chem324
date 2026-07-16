# HW 12: Methods of Approximation

### Question-1  

For the following hamiltonians, identify the exactly solvable and the perturbation parts and compute the first order corrections to the ground state energy 

- $\hat{H} = -\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2}+kx^2+\gamma x^3+\eta x^4$

- $\hat{H} =-\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2}+V(x)$
  - Where $V(0 \leq x\leq L/2) = 0$  and $V(L/2 \leq x\leq L)=a$

- $\hat{H} = -\frac{\hbar^2}{2\mu}\nabla^2-\frac{e^2}{4\pi \epsilon_0 r}+e\xi r cos\theta$
- $\hat{H}=-\frac{\hbar^2}{2\mu}\nabla_{\theta,\phi}^2+\mu \xi cos\theta$



### Question-2

Complete the proof of perturbation theory following **8-43 Problem in the book**

### Question-3

Use a trial function $\phi(x)=e^{-ax^2}$ to calculate the ground state energy for a quartic oscillator:
$$
\hat{H}= -\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2} +cx^4
$$



### Question-4

- Prove variational theorem following the hints from **Problem 8-1 in the  book**. 
- Complete the derivation of secular determinant outlined in the **Problem 8-22 from the book**



### Question-5

*Application of variational method: Linear combinations of trial functions*

In this problem we make use of the variational method to calcuate the ground state of the particle confined in a box of size $L$ which is subject to the following piecewise potential.
$$
V(0 \leq x \leq L/2) = V_0 x \\
V(L/2 \leq x \leq L) = V_0 (L-x)
$$
As a trial function we will use a linear combination of first two eigenfunctions of particle in a box without potentials() e.g the classical exactly solved PIB model)  
$$
\mid \phi \rangle =c_1 \mid 1 \rangle+c_2 \mid 2 \rangle
$$
*Here is a step by step guide to solving this problem:*

- Draw the shape of the potential $V(x)$ to see how it is different from classical PIB.

- Write down matrix elements $H_{11}$, $H_{12}=H_{21}$ $S_{11}$, $S_{12}$ etc.

- Evaluate matrix elements by taking advatnage of symetry arguments when possible.  

- Plug matirx elements into the determinant and solve the quadratic euqation which gives the determines the energies.








### <span style="background-color:lightyellow">Solution key to Question-5  </span>

- The piecewise function $V(x)$ is symmetric with respect to L/2 on a [0,L] interval. Note the nice analogy when we compare L/2 shifted integration limits $[-L/2, +L/2]$ with harmonic oscillator eigenfunctions on $[-\infty, +\infty]$! We will take advantage of this fact below to set integrals of odd functions to zero!

- $S_{11}=\langle 1 \mid 1\rangle =\frac{2}{L} = \int^{L}_0 sin^2 \Big(\frac{\pi x}{L} \Big)dx=1$ similarly $S_{22} =1$
   $S_{12}=\langle 1 \mid 2\rangle =0$  similarly $S_{21}=0$


   $$H_{12} = \langle 1 \mid \hat{H} \mid 2\rangle=\langle 1 \mid \hat{H}_0+V(x) \mid 2\rangle= \\ = E_2\langle 1 \mid 2\rangle +\langle 1 \mid V(x)\mid 2 \rangle= 0+ \frac{2}{L}\int^L_0 \Big(\frac{\pi x}{L} \Big)V(x)\Big(\frac{2\pi x}{L} \Big)dx=0+0$$
We broke down $H_{12}$ into two integrals first of which is zero because of orthogonality of PIB eigenfunctions and second is zero because we are integrating an overall odd function $\langle even\mid even \mid odd \rangle$ on a symmetric range.

$$
H_{11} =
$$
