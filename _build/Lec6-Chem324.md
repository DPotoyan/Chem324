---
redirect_from:
  - "/lec6-chem324"
title: '3.0 Schrodinger Equation.'
prev_page:
  url: /waves_1d
  title: '2.2 Visualizing and animating waves.'
next_page:
  url: /features/markdown
  title: '3.1 Interpretation of Schrodinger equation.'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Outline for Lecture 3.0: Schordinger Equartion

- By combining classical wave equation with key quantum ideas: discretization of energies and wave-particle duality we will arrive at Schoridnger's equation (SE).
- Schoridnger's equation in its most general form depends on both time and space. However, for stationary states  we can use the technique of separation of variables and  turn the time dependent Schrodinger equation (TD-SE) into the time independentSchrodinger equation  (TI-SE). The later is of special significance for chemical/biological sciences and will be our main focus in the rest of this course. 

 **Time dependent Schrodinger equation (TD-SE) in 1D**

  $$i\hbar \frac{\partial \psi(x,t)}{\partial t} =\Big[-\frac{\hbar^2}{2m}\frac{\partial^2 }{\partial x^2} +U(x)\Big]\psi(x,t)$$


  **Time independent Schrodinger equation (TI-SI) in 1D**

  $$E\psi(x)=\Big[-\frac{\hbar^2}{2m}\frac{\partial^2 }{\partial x^2} +U(x)\Big]\psi(x)$$

- We will learn about the powerful operator notation with the help of which  we can write equations of quantum mechanics in concise form. The operator notation helps with drawing many useful analogies with intuitive notions in classical  mechanics. Furthermore witht he help of operator notation will  frame the problem of solving such equations as a linear algebra problem of finding eigenvalues and eigenvectors.

- Classical equation of motion fails at small scales. Quantum works on all scales!  We will see how Schrodinger's equation predicts classical behaviour under apprporiate conditions where quantum effects are negligible.

  

### Where do fundamnetal laws come from? 

- Schrodinger equation (SE) is a fundamental law of nature. This implies that  SE can only be inferred or guessed from the experiments. It can not be derived. Its correctness is confirmed by the myriad of successful quantitative predictions and explanations of experimental observations. 

- Let us note that there has not been a single instance when quantum mechanics has failed when used properly! The physical world is quantum which is especially pronounced at small scales. Quantum Mechanics works flawlessly. Always. At all sales.  

### Picking up where classical mechanics has failed

Let us recall that classical mechanics failed at describing motion at the atomic and molecular scales and it is only an approximate theory valid at large scales. A new, correct equation of motion is needed that can explain:

- Quantized nature of energy (remember experiments on blackbody radiation, atomic spectra…)

- Wave-particle duality (Electron diffraction, Compton scattering)

- Explain why classical mechanics and classical thinking completely breaks down at small scales but works perfectly for larger objects. 

### The mathematical language of QM: operators

- Let us introduce some jargon and notation which is going to help us make mathematics and analogies more concise.

- Operators make quantum mechanics more compact  transparent. 

- We define operators via a mathematical act of turning function A into function B.  By operators we mean anything that can act on a function including but not limited to differentiation, integration, adding, multiplying etc. 

### Linear operators. 

Linear means that operator acting on sum of function does not change the power of any of functions. 

$$\hat{A}[c_1 f_1(x)+c_2f_2(x)]=  c_1 \hat{A}f_1(x)+c_2 \hat{A}f_2(x)$$

Schrodinger equation is a linear differnetial equation. Hence it can be written as a linear operator acting on a wave function.

-Question: which of the following would be linear operator: $\hat{A}=\frac{d}{dx}$      $\hat{A}=\int dx$       $\hat{A}=\sqrt{}$



### Schrdoinger Equation (time dependent)

- The correct equation of motion that works for microscopic particles and explains all the experiments was originally proposed by Erwin Schrödinger.
- Schrodinger equation is also known as a wave equation because it describes motion of wave functions in space and time. Below we write it down explicitly for 1-D in operator notation. Looks a bit complicated does not it? But worry not as we will get comfortable solving it for wide variety of problems very soon. 



 $$i\hbar \frac{\partial \psi(x,t)}{\partial t} =\Big[-\frac{\hbar^2}{2m}\frac{\partial^2 }{\partial x^2} +U(x)\Big]\psi(x,t)$$

- Left hand side describes change of wae function with time. The presence of an imaginary uni tells us that solutions of this equation are generally complex functions. 
- Right hand side descirbes spatial varation of wave function. We will soon discover that  inside square bracekts we have operators of kinetic and potential energies: an analog of kinetic and potential energies in classical mechancis.  

## From classical to quantum wave equation



- In 1925/1926 Erwin Schrodinger who was an expert on waves attempted to derive new equation of motion that could unify weird quantum facts of  energy quantization and wave-particle duality under one sound theoretical roof! He (correctly) guessed that the equation of motion for quantum mechanics should be a wave equation.

- This was the only wave equation known at that time so Schordinger started his reasoning from here. 

  $$\frac{\partial^2 \Psi(x,t)}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2 \Psi(x,t)}{\partial t^2}$$

- Taking a typical wave function which satisfies a wave equation we will now inject the above mentioned key quantum relationships and will try to figure out which equation governs such solutions. 

  As an example let us take  a freely moving periodic wave which satisfies classical wave equation. Plug it in above equation to verify. 

  $$\Psi(x,t)=Ae^{i(kx-\omega t)}$$

  

  We could have written a sin or cos functions with equation success.  But the complex notation is more general  and convenient  to work with mathematically. 



## An attempt at deriving Sschordinger Equation

Now let us combining the following two cornerstone quantum ideas into a free periodic wave function:

- **De Brogile relation:** **$p=h/\lambda$** Matter has both particle and wave like qualities. 

- **Plank equaton:** $E=h\nu$  Energy levels  are quantized.

$$\Psi(x,t)=Ae^{i(kx-\omega t)}=Ae^{i2\pi(\frac{x}{\lambda}-\nu t)}= Ae^{i\hbar(px-E t)}$$

Where we have plugged in wave vector $k=\frac{2\pi}{\lambda}=\frac{p}{\hbar}$ expressed in terms of momenum via De Brogile relation and angular frequency expressed in terms of energy via Plank equation $\omega=2\pi \nu=\frac{E}{\hbar}$



### Turning a quantum wave function into quantum wave equation. 

- What we have achieved so far is design a wave function which reflects quantum reality by having the right momentum to wave length and energy to frequency relationships. 

- Now the question is which equation is governing such wave functions?  To find out we will have to differentiatiate the wave function with respect to spatial and temporal components. 



Taking a time derivative once 

$ \frac{\partial \Psi(x,t)}{\partial t}=-\frac{i}{\hbar}E \Psi(x,t)$

we get energy as a multiplicative factor. This is interesting! As you know total energy is conserved hene one wants to find out its relationship with the wave function.  

Likewise we can recover total energy by taking  spatial derivatve twice

$$ \frac{\partial \Psi(x,t)}{\partial x}=\frac{i}{\hbar}p\Psi(x,t)$$

$$ \frac{\partial^2 \Psi(x,t)}{\partial x^2}=-\frac{p^2}{\hbar^2}\Psi(x,t)=-\frac{2m(E-V)}{\hbar^2}\Psi(x,t)$$

Where we have made use of total energy conservation for a free wave by expressing kinetic energy to the total energy.  $E=\frac{p^2}{2m}+V$

This last expression we will come to know as the time independent Schrodinger equation (TI-SE):

$$-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi=E\Psi  $$



By connecting spatial and temporal derivatives through total energy we obtain the time-dependent Schrodinger equation (TD-SE):

$$ i\hbar \frac{\partial }{\partial t} \Psi= [-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V]\Psi$$



### Time dependent Schrodinger equation in operator notation.

By witing the equation in operator notation we may begin to recognize certain terms and appreciate that Schrodinger equation, as any proper equation motion, reflects the total energy conservation 

$$i\hbar \frac{\partial }{\partial t} \Psi= [-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V]\Psi=\hat{H}\Psi$$

The operator $\hat{H}$ is called a Hamilton opertor or hamiltonian. And is an analog of classical Hamiltonian $H(x,p)=\frac{p^2}{2m}+V$ which is an expression of total energy. 

$$\hat{H}=\hat{K}+\hat{V}=\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)$$

As we  see the analog of classical kinetic operator is a second order partial differentiation. 

Whereas the  potential energy is has exactly the same appearance of a function of spatial coordinates. 



### From time dependent to time independent Schrodiner equation.

As we have learned earlier wave function PDE where spatial and coordinates are independent of each other allow using separation of variables and decoupling time and space dependence. The resulting wave equation produces standing waves. 

$$\Psi(x,t)=f(t)\psi(x) $$

$$i\hbar \frac{\partial }{\partial t} f(t)\psi(x) =\hat{H}f(t)\psi(x)$$

$$\frac{1}{f(t)}i\hbar \frac{\partial }{\partial t} f(t)=\frac{1}{\psi(x) }\hat{H}\psi(x)=E$$



The separation constatn is total enegy as is evident by recalling that hamiltonain operator is the analog of hamilton function. 

The temporal part is solved instantly:

$$f(t)=e^{-iEt/\hbar} $$

The sptial part is time independent Schroinger equation. THe solution of which would be our main equation for the remainder of this lecture.

$$\hat{H}\psi(x)=E\psi(x)$$



### Time dependent Schrodinger equation in operator notation.

The time independent Schrodinger equation in operator form takes  even more consie form:

$$\hat{H}\psi(x)=E\psi(x)$$