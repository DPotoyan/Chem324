---
redirect_from:
  - "/lec6-2"
title: '6.2 Variation Method'
prev_page:
  url: /Lec6-1
  title: '6.1 Perturbation Theory'
next_page:
  url: /Lec6-3
  title: '6.3 Linear Algebra and QM'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Outline for Lecture 6.2:  "Variational Method"



- Variational method provides a powerful tool tool to (a) Make systematic  approximations and quantiatively measure convergence of predictions towards true values. 
- In variational method one first makes an "educated" guess by picking trial functions for the hamiltonian. One then minimizes parameters of the trial function to get solutions closer to the truth. 
- Variational method, when applied to linear combination of trial functions can turn hard QM problem into an easier linear algebra task: solution of systems of linear equations. Instead of solving differentiation equations for eignefunctions/eigenvalues we instead are solving for matrix eigevnalues and eigenvectors.


<!-- slide -->
## Variational method

Any trial function $\mid \phi \rangle$ we come up with the energy computed with it will always be greater or equal to exact or true energy. 


$$
E_{\phi}=\frac{\langle \phi \mid \hat{H}  \mid \phi\rangle}{\langle \phi \mid \phi\rangle} \geq E_0
$$


1. Ground state energy is the lowest possible energy for the system. 

2. By minimizing the energy functions we can make most accurate prediction for a given trail function. 

3. More parameters give us more handles to vary and get more acurate solutions. 



### Example: H-atom trial function

- Exact solution for ground state: $\psi(r)=\frac{1}{(\pi a^3_0)^{1/2}}e^{-r/a_0}$ and $E_1 = -0.5 h$

- Let's test a trail function $\phi=e^{-\alpha r^2}$  and predict energy:

  
$$
E_{trial} = \frac{\langle \phi \mid \hat{H}  \mid \phi\rangle}{\langle \phi \mid \phi\rangle}
$$


$$
E_{trial}(\alpha) = \frac{4\pi \int^{\infty}_0 \hat{ e^{-\alpha r^2}[-\frac{\hbar^2}{2\mu}\nabla_r^2}-\frac{e^2}{4\pi \epsilon_0 r}] e^{-\alpha r^2} r^2 dr }{4\pi \int^{\infty}_0 e^{-2\alpha r^2} r^2 dr}
$$


$$
E_{trial}(\alpha)=\frac{3\hbar^2 \alpha}{2m_e}-\frac{e^2 \alpha^{1/2}}{\sqrt{2}\epsilon_0 \pi^{3/2}}
$$



### Minimization gives the best values of paramaters in trial functions

$$
E_{trial}=\frac{3\hbar^2 \alpha}{2m_e}-\frac{e^2 \alpha^{1/2}}{\sqrt{2}\epsilon_0 \pi^{3/2}}
$$

$$
\frac{\partial E_{trial}(\alpha)}{\partial \alpha} = 0
$$

$$
\alpha_{min} = \frac{m_e e^4}{18 \pi^3 \epsilon^2_0 \hbar^4}
$$

- We need to plug this parameters back into energy function to get the  energy minimized with respect to $\alpha$, e.g $E(\alpha_{min})$



### Comparison of optimized vs true values


$$
E_0 = -0.5 h
$$


$$
E_{trial}(\alpha_{min}) = -0.424
$$



- About 15% error. But hey it is not too bad for a start!
- Adding more parameters and functions will reduce the error.


### 

## Variational method as applied to linear combinations of trial functions


$$
\phi = \sum_i c_i f_i
$$

- $c_i$ -Variational coefficients
- $f_i$ Trial functions
- Example: $\phi(x) = c_1 sin (2x)+c_2 sin(2x)$





### It's a linear algebra problem


$$
\begin{vmatrix}
H-ES & x_{0} & x_{0}^{2} & \dots & x_{0}^{n} \newline 
H-ES & x_{1} & x_{1}^{2} & \dots & x_{1}^{n} \newline 
1 & x_{n} & x_{n}^{2} & \dots & x_{n}^{n}
\end{vmatrix} = 0
$$
