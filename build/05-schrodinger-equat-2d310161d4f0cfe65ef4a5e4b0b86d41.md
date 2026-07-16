# HW 5: Schrodinger Equation and Operators

>  "Where did we get that (equation) from? Nowhere! It is not possible to derive it from anything you know. It came out of the mind of Schrödinger.”
> — Richard Feynman



### Q1

- A. **Arrive at Time independent Schrodinger equation.** Start first plugging this standing wave $\psi(x,t) = \psi(x) cos(\omega t)$ into classical wave equation.  Next express wavelength in terms of momentum via De Broglie relation $\lambda=\frac{h}{p}$. Finally  express momenta in terms of the total energy of the system $E=\frac{p^2}{2m}+{V}$
  - *<u>Hint:</u> This is done in the book. But try to practice your hand at doing the steps.*

- B. **Arive at Time dependent Schrodinger equation.** Start by taking  derivatives of a simple traveling periodic wave $\psi(x,t)=e^{i(kx-\omega t)}$  with respect to time and space. <u>*Hint*:</u>

  - Note that by taking one time derivative you get $i\omega$ in front which can be related to Energy E. How? by recalling planck's formula $E=h\nu = \hbar \omega$ This is why we see $\hbar=h/2\pi$ frequently.

  - When taking two derivatives with respect to x you get $-k^2$. This can also be related to energy $E$ by recalling definition of a wave-number $k=\frac{2\pi}{\lambda}$ and planck's formula. 

  - This procedure shows you the reason why in Schordinger equation you have second derivative with respect to space and single derivative with respect to time. 

### Q2

 Evaluate $g=\hat{A}f$ given the following pairs of operator  $\hat{A}$ and function $f$

| $\hat{A}=\sqrt{....}$                                        | $f=x^4$      |
| ------------------------------------------------------------ | ------------ |
| $\hat{A} =\frac{d^3}{dx^3}+x^3$                              | $f=e^{-ax}$  |
| $\hat{A} = \int^{1}_0 dx$                                    | $f=x^3-2x+3$ |
| $\hat{A}=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}+\frac{\partial^2}{\partial z^2}$ | $x^3y^2z^4$  |

### Q3

Determine which of the opeartors are linear. You can do this by tesing to see weather the linearity condition is satisdied: $\hat{L}(c_1 f_1+c_2 f_2)=c_1\hat{L}f_1+c_2\hat{L}f_2$ 

- $\hat{L}f=\sqrt{f}$

- $\hat{L}f=f^{*}$

- $\hat{L}f=0$

- $\hat{L}f=\frac{1}{f}$

- $\hat{L}f=f(0)$

- $\hat{L}f=ln f$

  

### Q4 

- Show that $\psi(x,t)=e^{i(kx-\omega t)}$ is an eigenfunction for  operators $\hat{A_1}=\frac{d^2}{dt^2}$ and $\hat{A_2}=\frac{d^2}{dx^2}$  

- Write down eigenvalues of the two operators. 
- Are the two operators linear?
- Is the sum of the two opearators linear $\hat{A_1}+\hat{A_2}$
- Would linear combination of linear operators be a linear operator itself? 

### Q5

Write out the operator $\hat{A}^2f$ acting on some arbitrary function $f$ for the following cases: 

- $\hat{A}=\frac{d^2}{dx^2}$
- $\hat{A}=\frac{d}{dx}+x$



