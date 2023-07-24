## Schrödinger Equation


```{admonition} What you need to know
:class: note
- By combining classical wave equation with key quantum ideas: discretization of energies and wave-particle duality we will arrive at Schrödinger's equation (SE).
- Schrödinger's equation depends on both time and space. However, for stationary states  we can use the technique of separation of variables and  turn the time-dependent Schrödinger equation (TD-SE) into the time-independent Schrödinger equation  (TI-SE). The later is of special significance for chemical/biological sciences and will be our main focus in the rest of this course. 
- We will learn about the powerful operator notation with the help of which  we can write equations of quantum mechanics in concise form. The operator notation helps with drawing many useful analogies with intuitive notions in classical  mechanics. Furthermore with the help of operator notation will  frame the problem of solving such equations as a linear algebra problem of finding eigenvalues and eigenvectors.

- Classical equation of motion fails at small scales. Quantum works on all scales!  We will see how Schrödinger's equation predicts classical behaviour under apprporiate conditions where quantum effects are negligible.
```

  

## The exciting journey into the microscopic world.  

- In the next few sections we are going to arrive at Schrödinger equation (SE) which is a fundamental law of nature. This implies that  SE can only be inferred or guessed from the experiments. It can not be derived. Its correctness is confirmed by the myriad of successful quantitative predictions and explanations of experimental observations. 

- Let us note that there has not been a single instance when quantum mechanics has failed when used properly! The physical world is quantum which is especially pronounced at small scales. Quantum Mechanics works flawlessly. Always. At all sales.  

  <img src="images/SE_intro.jpeg" stylewidth="100px" />

### Picking up where classical mechanics has failed

Let us recall that classical mechanics failed at describing motion at the atomic and molecular scales and it is only an approximate theory valid at large scales. A new, correct equation of motion is needed that can explain:

- Quantized nature of energy (remember experiments on blackbody radiation, atomic spectra…)

- Wave-particle duality (Electron diffraction, Compton scattering)

- Explain why classical mechanics and classical thinking completely breaks down at small scales but works perfectly for larger objects. 

  <img src="images/SE_intro2.gif" width="200px" />




### Schrödinger Equation (time-dependent)

<img src="images/SE_4.jpg" width="0.5" />

- The correct equation of motion that works for microscopic particles and explains all the experiments was originally proposed by Erwin Schrödinger. Below we write the time-dependent Schrödinger equation in 1D. Schrödinger equation, is also known as a wave equation because it describes motion of wave functions in space and time. 

  

   $$i\hbar \frac{\partial \psi(x,t)}{\partial t} =\Big[-\frac{\hbar^2}{2m}\frac{\partial^2 }{\partial x^2} +U(x)\Big]\psi(x,t)$$

- Left hand side describes change of wave function with time. The presence of an imaginary unit tells us that solutions of this equation are generally complex functions. 
- Right hand side describes spatial varation of wave function. We will soon discover that  inside square brackets we have operators of kinetic and potential energies: an analog of kinetic and potential energies in classical mechanics.  

### From classical to quantum wave equation

- In 1925/1926 Erwin Schrödinger, who was an expert on waves, attempted to derive new equation of motion that could unify weird quantum facts of  energy quantization and wave-particle duality under one sound theoretical roof! He (correctly) guessed that the equation of motion for quantum mechanics should be a wave equation.

- This was the only wave equation known at that time so Schrödinger started his reasoning from here. 

  $$\frac{\partial^2 \Psi(x,t)}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2 \Psi(x,t)}{\partial t^2}$$

- Taking a typical wave function which satisfies a wave equation we will now inject the above mentioned key quantum relationships and will try to figure out which equation governs such solutions. 

  As an example let us take  a freely moving periodic wave which satisfies classical wave equation. Plug it in above equation to verify. 

  $$\Psi(x,t)=Ae^{i(kx-\omega t)}$$

  We could have written a sin or cos functions with equation success. But the complex notation is more general and convenient to work with mathematically. 



### An attempt at deriving Schrödinger Equation

Now let us combine the following two cornerstone quantum ideas into a free periodic wave function:

- **De Broglie relation:** **$p=h/\lambda$** Matter has both particle and wave like qualities. 

- **Planck equaton:** $E=h\nu$  Energy levels  are quantized.

$$\Psi(x,t)=Ae^{i(kx-\omega t)}=Ae^{i2\pi(\frac{x}{\lambda}-\nu t)}= Ae^{\frac{i}{\hbar}(px-E t)}$$

Where we have plugged in wave vector $k=\frac{2\pi}{\lambda}=\frac{p}{\hbar}$ expressed in terms of momenum via de Broglie relation and angular frequency expressed in terms of energy via Planck equation $\omega=2\pi \nu=\frac{E}{\hbar}$



### Turning a quantum wave function into quantum wave equation. 

- What we have achieved so far is design a wave function which reflects quantum reality by having the right momentum to wave length and energy to frequency relationships. 

- Now the question is which equation is governing such wave functions?  To find out we will have to differentiatiate the wave function with respect to spatial and temporal components. 

Taking a time derivative once 

$ \frac{\partial \Psi(x,t)}{\partial t}=-\frac{i}{\hbar}E \Psi(x,t)$

we get energy as a multiplicative factor. This is interesting! As you know total energy is conserved hence one wants to find out its relationship with the wave function.  

Likewise we can recover total energy by taking  spatial derivatve twice

$$ \frac{\partial \Psi(x,t)}{\partial x}=\frac{i}{\hbar}p\Psi(x,t)$$

$$ \frac{\partial^2 \Psi(x,t)}{\partial x^2}=-\frac{p^2}{\hbar^2}\Psi(x,t)=-\frac{2m(E-V)}{\hbar^2}\Psi(x,t)$$

Where we have made use of total energy conservation for a free wave by expressing kinetic energy to the total energy.  $E=\frac{p^2}{2m}+V$

This last expression we will come to know as the time-independent Schrödinger equation (TI-SE):

$$-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V\Psi=E\Psi  $$

By connecting spatial and temporal derivatives through total energy we obtain the time-dependent Schrödinger equation (TD-SE):

$$ i\hbar \frac{\partial }{\partial t} \Psi= [-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V]\Psi$$

### The mathematical language of QM: operators

- Let us introduce some jargon and notation which is going to help us make mathematics and analogies more concise.

- Operators make quantum mechanics more compact  transparent. 

- We define operators via a mathematical act of turning function A into function B.  By operators we mean anything that can act on a function including but not limited to differentiation, integration, adding, multiplying etc. 

  <img src="images/SE_intro3.jpg" width="300px" />

### Linear operators. 

Linear means that operator acting on sum of function does not change the power of any of functions. 

$$\hat{A}[c_1 f_1(x)+c_2f_2(x)]=  c_1 \hat{A}f_1(x)+c_2 \hat{A}f_2(x)$$

Schrödinger equation is a linear differential equation. Hence it can be written as a linear operator acting on a wave function.

-Question: which of the following would be linear operator: $\hat{A}=\frac{d}{dx}$      $\hat{A}=\int dx$       $\hat{A}=\sqrt{}$




### Time-dependent Schrödinger equation in operator notation.

By writing the equation in operator notation we may begin to recognize certain terms and appreciate that Schrödinger equation, as any proper equation of motion, reflects the total energy conservation 

$$i\hbar \frac{\partial }{\partial t} \Psi= [-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}+V]\Psi=\hat{H}\Psi$$

The operator $\hat{H}$ is called a Hamilton operator or hamiltonian. And is an analog of classical Hamiltonian $H(x,p)=\frac{p^2}{2m}+V$ which is an expression of total energy. 

$$\hat{H}=\hat{K}+\hat{V}=\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)$$

As we  see the analog of classical kinetic operator is a second order partial differentiation. 

Whereas the  potential energy has exactly the same appearance of a function of spatial coordinates. 



### From time-dependent to time-independent Schrödinger equation.

As we have learned from lectures on classical wave equation when the spatial and temporal coordinates are independent of each other one can use separation of variables and decouple time and space dependence. 

$$\Psi(x,t)=f(t)\psi(x) $$

Plugging this into time-dependent wave equation we get

$$i\hbar \frac{\partial }{\partial t} f(t)\psi(x) =\hat{H}f(t)\psi(x)$$

Now collecting $x$ and $t$ terms we achieve separation of variables. 

$$\frac{1}{f(t)}i\hbar \frac{\partial }{\partial t} f(t)=\frac{1}{\psi(x) }\hat{H}\psi(x)=E$$

Notice that the hamiltonian operator contains $x$ derivatives hence $f(t)$ can be taken out of the oeprator expression. In the expression $\frac{\hat{H}\psi(x)}{\psi(x)}$ however one can not cancel $\psi$ becasue what we have in the numerator is differentiation written with the help of an operator, and not just a simple product! 

The separation constant can be recognized as the total energy as is evident by recalling that the hamiltonain operator is the analog of Hamilton function.  The temporal part is solved instantly:

$$f(t)=e^{-iEt/\hbar} $$

The spatial part is obtained by solving time-independent Schrödinger equation.

$$\hat{H}\psi(x)=E\psi(x)$$

Once we have a solution to both spatial and temproal parts of the wave function we can write down the  

$$\psi(x,t)=\psi(x)f(t)=\psi(x) e^{-\frac{i}{\hbar}Et}$$



### What about the boundary conditions and normal modes?

As we recall from solving classical wave equation whenever there are bounary conditions imposed on the spatial domain of our PDE we can end up having infinite number of solutions $u_n(x)$ discretized by integers $n=1,2,...$ for each spatial coordinate. 

$$\frac{\partial^2 u_n(x)}{\partial x^2}=\beta^2_n u_n(x) $$

In the same analogy we are going to have infinite number of  solutions to quantum wave equation discretized by $n$ where the multiplicative factors are nothing but the discrete energy levels! The wave functions for each $n$ are going to have special signficance as gateways to describing the probability profile of finding electrons in different points in space. 

$$\hat{H} \psi_n(x)=E_n \psi_n(x)$$



### Eigenvalue eigenfunction problems

Using the operator notation we see that both classical wave equation and time-independent Schrödinger equation can be framed as a problem of seeking special functions and multiplicative factors which satisfy a special kind of operators. 

<img src="images/SE_intro6.jpg" style="zoom:80%;" />

E.g while action of operator can in general change the function in quantum mechanics we are interested in operators which preserve the function witht he constant multi0licative factor.  

### Time-independent Schrödinger equation as an eigenvalue-eigenfunction problem.

The time-independent Schrödinger equation can now be seen as an eigenfunction-eigenvalue problem where our eigenfunctions are wave-functions and eigenvalues are energies.

$$\hat{H}\psi(x)=E\psi(x)$$

<img src="images/SE_intro5.jpg" style="zoom:70%;" />



### The correspondence principle of Quantum Mechanics

Thanks to universality of energy conservation law, for every observable in classical mechanics there can be found a corresponding operator in quantum mechanics! Lets list them here:

|               Observables               |                   Classical                    |                           Quantum                            |
| :-------------------------------------: | :--------------------------------------------: | :----------------------------------------------------------: |
|                Position                 |                      $x$                       |                         $\hat{x}=x$                          |
|                Momentum                 |                     $p=mv$                     |        $\hat{p}=-i\hbar \frac{\partial}{\partial x}$         |
|            Potential Energy             |                     $V(X)$                     |                        $\hat{V}=V(x)$                        |
|             Kinetic Energy              |               $K=\frac{p^2}{2m}$               |                $\hat{K}=\frac{\hat{p}^2}{2m}$                |
|              Total Energy               |          $H(x,p)=\frac{p^2}{2m}+V(x)$          |                  $\hat{H}=\hat{K}+\hat{V}$                   |
|           Equation of motion            | Newton's law $F=ma$ <br>or Hamiltons equations | $\hat{H}\psi=E\psi$ Or <br>$i\hbar\frac{\partial \psi}{\partial t}=\hat{H}\psi$ |
| Quantization and wave-particle duality? |                      N/A                       | Energy quantization and duality are<br> naturally described by $E_n$ and $\psi_n$. |

