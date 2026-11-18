# HW 12: Methods of Approximation

### Question-1  

For the following hamiltonians, identify the exactly solvable and the perturbation parts and compute the first order corrections to the ground state energy 

- $\hat{H} = -\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2}+kx^2+\gamma x^3+\eta x^4$

- $\hat{H} =-\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2}+V(x)$
  - Where $V(0 \leq x\leq L/2) = 0$  and $V(L/2 \leq x\leq L)=a$

- $\hat{H} = -\frac{\hbar^2}{2\mu}\nabla^2-\frac{e^2}{4\pi \epsilon_0 r}+e\xi r cos\theta$
- $\hat{H}=-\frac{\hbar^2}{2\mu}\nabla_{\theta,\phi}^2+\mu \xi cos\theta$



### Question-2

*Transitions driven by light*

An electron in a one-dimensional box of length $L = 1.0$ nm is a simple model of a $\pi$ electron in a conjugated dye. Light polarized along the box acts on it through the dipole $\hat{M} = -ex$.

- Which of the transitions $n = 1 \to 4$, $2 \to 3$, $2 \to 4$ and $3 \to 5$ are allowed? Decide each one from the symmetry of the integrand of $\langle f \mid x \mid i\rangle$ about the middle of the box, without computing any integral.

- Compute the transition dipole $\langle 3 \mid -ex \mid 2\rangle$ by integration. Give it in units of $eL$ and in debye.

- At what wavelength does the $2 \to 3$ transition absorb?

- On resonance, the first-order probability of the transition is $P = (\mid M_{fi}\mid \mathcal{E}\, t/2\hbar)^2$. For light with a field amplitude $\mathcal{E} = 1.0\times10^{5}$ V/m, how long does it take for the probability to reach 1%? Why can the same formula not be trusted after ten times that long?

### Question-3

Use a trial function $\phi(x)=e^{-ax^2}$ to calculate the ground state energy for a quartic oscillator:
$$
\hat{H}= -\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2} +cx^4
$$



### Question-4

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








### <span style="background-color:lightyellow">Solution key to Question-4  </span>

- The piecewise function $V(x)$ is symmetric with respect to L/2 on a [0,L] interval. Note the nice analogy when we compare L/2 shifted integration limits $[-L/2, +L/2]$ with harmonic oscillator eigenfunctions on $[-\infty, +\infty]$! We will take advantage of this fact below to set integrals of odd functions to zero!

- $S_{11}=\langle 1 \mid 1\rangle =\frac{2}{L} = \int^{L}_0 sin^2 \Big(\frac{\pi x}{L} \Big)dx=1$ similarly $S_{22} =1$
   $S_{12}=\langle 1 \mid 2\rangle =0$  similarly $S_{21}=0$


   $$H_{12} = \langle 1 \mid \hat{H} \mid 2\rangle=\langle 1 \mid \hat{H}_0+V(x) \mid 2\rangle= \\ = E_2\langle 1 \mid 2\rangle +\langle 1 \mid V(x)\mid 2 \rangle= 0+ \frac{2}{L}\int^L_0 \Big(\frac{\pi x}{L} \Big)V(x)\Big(\frac{2\pi x}{L} \Big)dx=0+0$$
We broke down $H_{12}$ into two integrals first of which is zero because of orthogonality of PIB eigenfunctions and second is zero because we are integrating an overall odd function $\langle even\mid even \mid odd \rangle$ on a symmetric range.

$$
H_{11} =
$$
