---
redirect_from:
  - "/lec3-2"
title: '3.2 Postulates of QM'
prev_page:
  url: /Lec3-1
  title: '3.1 Probabilistic meaning of wave function.'
next_page:
  url: /Lec3-3
  title: '3.3 Mathematics of QM'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Outline for Lecture 3.2: Postulates of quantum mechanics.  

- **A set of fundamental postulates** make quantum mechanics a self contained fool-proof logical theory. Armed with such a theory all of chemistry and biology “in theory” reduces to mere application of Schrodinger equation. In practice theory is not so easy to apply. 
- **Double slit experiment and quantum weirdness**. Microscopic world has an inherently probabilistic nature where in some sense the very act of observation creates the outcome! Uncertainty relation places rigid bound on the amount of information one can possess about microscopic objects.



## The posutlates

- The state of a system is completely specified by a wave function which contains all the dynamical information. The square of wave function is a probability distribution of finding the object in space.

$$P(x,t)=|\psi(x,t)|^2 \,\,\,   \,\,\, \int |\psi(x,t)|^2 dx=1 $$



- For every observable quantity there is a corresponding linear and Hermitian operator in quantum mechanics.

$$\hat{A} (c_1 \psi_i+c_2 \psi_2) =  c_1 \hat{A}\psi_i+c_2 \hat{A}\psi_2$$

$$\int \psi^* (\hat{A}\phi) dx = \int \phi (\hat{A} \psi)^* dx$$



- Eigenvalues of an operator are the only possible values of the correspnding observable that can be measured in the experiments. 

$$\hat{A}\psi_n =a_n \psi_n $$



- Expectation or the average value of observable A in a state described by wave 
  function $\psi$ is given by expression:

  $$\langle A \rangle = \int \psi^* \hat{A}\psi dx $$
  
  
  
- Time evolution of wave function is governed by time-dependent Schrodinger equation.

  $$i\hbar \frac{\partial \psi}{\partial t}=\hat{H}\psi $$



## Postulate #1 Wave function beahviour

Wave function that describes real physical objects should be well behaved in order to correspond to probability distribution.

- Continuous, single-valued, differentiable and finite over finite range. 
- Functions that do not satisfy these criteria are discarded as non-physical.  





## Postulate #2  Linear and Hermitian operators

- Linearity of opeartors follows from the nature of Schrodinger equation which is a linear differnetiatial equation. Linearity implies a distirbutive property of opeartors when applied to any linear combination of functions. 

$$\hat{L} (c_1\psi_1+c_2\psi_2+...+c_n\psi_n)=c_1\hat{L} \psi_1+c_2\hat{L}\psi_2+...+c_n\hat{L}\psi_n $$



- Beside being linear operators of observables in quantum mechanics are hermitian. Hermtian property guarantees that eigenvalues are strictly real. And since eigenvalues are the only values observed in experimental measruemnts it is sensible to expect that one would not be getting mixed complex and real numbers in the experiments. An hermitian property is defined by the following equality where an  operator can go into complex conjugate mode and act on complex conjugate pair of the function. 

$$\int \psi^* (\hat{H} \phi) dx = \int \phi (\hat{H} \psi)^* dx =\int \phi \hat{H}^* \psi^* dx $$



## Postulate #3 Eigenvalues are the only values seen in the experiments. 

Eigenvalues of an operator $\hat{A}$ exhaust the posisble values one can get in the experiments. Put another way eiganvalues are the only kind fo values to be measured. As a result of boundary conditions one often has discrete eigenvalues for observables which are indexed by integer numbers known as quantum numbers. 

$$\hat{A}\psi_n = a_n\psi_n $$



## Postualate #4 Expectation of an observable

What is the expected value of an abservable obtained  on average as a result of large number of expeirments. The answer is given by plugging operator $\hat{A}$ correpsonding to observable A into an expression of average with wave function square acting as probabilty distirbution function.  

$$\langle A \rangle =\int \psi^* \hat{A}\psi dx $$



## Posutalte #5 Time evoluation of quantum states

 State of quantum mechanical system evolves in time according to Schroinger equation.

$$i\hbar \frac{\partial \psi}{\partial t}=\hat{H}\psi $$

We are often interested in stationary states desribed by pure eigenfunctions where time dependnce does not figure explciitely. In mixed states described by superposiionts of eigenfunctions, however, leads to time depednce of observable quantities.  

 