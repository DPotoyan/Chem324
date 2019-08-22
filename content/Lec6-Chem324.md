---
title: |
    | Lecture 3.0, Chem-324, Fall2019
	|
    | Solving wave equations. PDEs and ODEs.
author: 'Davit Potoyan'
institute: ' Iowa State University, Ames IA 50011'
toc: false

---


- Arrive at Schrodinger equation by combining classical equation of waves with key pieces of experimental evidence: energy quantization and wave-particle duality.

- Use separation of variables to turn the time dependent Schrodinger equation into time independent form. The latter form is of enormous significance for chemical/biological sciences. 

- Learn operator notation to write equations of quantum mechanics in compact form. Frame the problem of solving such equations as eigenvalue problems.

- Operator notation will allows us to see clearly the direct correspondence between Schrodinger equation and classical equation of motion. Both equations reflect the energy conservation! Classical equation of motion fails at small scales. Quantum works on all scales! 


## Facts about Schrodinger equation

- Schrodinger equation is the fundamental equation which completely describes all aspects of matter both at small and large scales. By matter we mean anything from electrons, atoms, molecules and macroscopic objects.

- Schrodinger equation by being a fundamental law of nature can only be inferred or guessed from the experiments. It can not be derived. Its correctness is confirmed by its successful quantitative explanations of all known experimental observations.

> Some restrictions apply: When some small particles move comparable to speed of light relativistic effects of these particles may become important. Dirac extended Schrodinger equation to account for these. These relativistic effects are usually negligible for most systems of interest. They do however manifest in the spin-orbit coupling, intersystem crossing, and other scalar relativistic effects. These effects can become substantial in some very heavy elements.


## Why we need quantum theory for matter?

Let us recall that classical mechanics has failed at describing motion at the atomic and molecular scales. Put another way classical mechanics is a theory which is valid only at sufficiently large scale. A new, correct equation of motion is needed that can explain:

- Quantized nature of energy (remember experiments on blackbody radiation, atomic spectra…)

- Wave-particle duality (Electron diffraction, Compton scattering)

- Explain why classical mechanics and classical thinking completely breaks down at small scales but works perfectly for larger objects. 

## Mathematical aspects of quantum mechanics

We introduce here some jargon and notation which is going to help us to make sense of the following slides. We define operators as some mathematical constructs which act on function A and turn it into function B. Operator notation will allow us write equations of quantum mechanics in most compact and transparent manner. So lets take some time to get to know them.



## Time dependent Schrodinger equation.

$$i\hbar \frac{\partial \psi(x,t)}{\partial t} =\Big[-\frac{\hbar^2}{2m}\frac{\partial^2 }{\partial x^2} +U(x)\Big]\psi(x,t)$$


## Time independent Schrodinger equation. 

$$\Big[-\frac{\hbar^2}{2m}\frac{\partial^2 }{\partial x^2} +U(x)\Big]\psi(x)=E\psi(x)$$