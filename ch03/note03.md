## Postulates 

:::{admonition} What you need to know
:class: note
- Quantum Mechanics can be built on top of few postulates which have been learned from comparisons of theory with the experiments.
- Postulates are mathematical requirements which ensure physically meaningul solutions to schrodinger equation and which provide connection between abstract concepts of operators and experimental observables.
- Once we accept thses postulates Quantum Mechanics becomes a self-contained theory capable of explaining and computing all that is to know about atoms and molecules and their interactions with radiation. 
:::

### Postulate 1: Wave function

```{admonition}  Wave function 
:class: important

- **The square of wave function is a probability distribution of finding the object in space.** 
- It is important to stress that the state of a system is completely specified by a wave function which contains all the information acessible to us through experiments. 

$$P(x,t)=|\psi(x,t)|^2 \,\,\,$$   

- Wave function needs to conform to a number of requirments in order to be probability distribution integral of which should always return 1 meaning that quantum object is to be found somehwere.

$$\int |\psi(x,t)|^2 dx=1 $$

- **Being Continuous, single-valued, differentiable and finite.**  Functions that do not satisfy these criteria are discarded as non-physical.  
```

### Postulate 2: Operators


:::{admonition}  Operators
:class: important

- **Operators in QM are Linear**. Linearity follows from the nature of Schrödinger equation which is a linear differenetial equation. Linearity implies a distirbutive property of opeartors when applied to any linear combination of functions. 

$$\hat{L} (c_1\psi_1+c_2\psi_2+...+c_n\psi_n)=c_1\hat{L} \psi_1+c_2\hat{L}\psi_2+...+c_n\hat{L}\psi_n $$

- **Operators in QM are Hermtian**. Hermitian property of operators guarantees that eigenvalues are strictly real. And since eigenvalues are the only values observed in experimental measurements it is sensible to expect that one would not be getting mixed complex and real numbers in the experiments. Hermitian property is defined by the following equality where the same operator can go into complex conjugate mode and act on complex conjugate pair of the function. 

$$\int \psi^* (\hat{H} \phi) dx = \int \phi (\hat{H} \psi)^* dx =\int \phi \hat{H}^* \psi^* dx $$

- In dirac notation the hermitian condition looks simpler:

$$\langle \phi |\hat{H} | \psi \rangle = \langle \psi |\hat{H} | \phi \rangle^{*}$$
:::


### Postulate 3: Eigenvalues

:::{admonition}  Eigenvalues
:class: important

- Eigenvalues of an operator are the only possible values of the corresponding observable that can be measured in the experiments. No other values are possible.  

$$\hat{A}\psi_n =a_n \psi_n $$
:::


### Postulate 4: Expectations

```{admonition}  Expectations
:class: important

- Expectation or the average value of observable A in a state described by wave 
  function $\psi$ is given by expression:

$$\boxed{\langle A \rangle = \int \psi^* \hat{A}\psi dx = \langle \psi | A| \psi \rangle}$$

- Expected value predicts what would result from doing large number of experiments measuring observable and then taking average.  

```


### Postulate 5: Time evolution


```{admonition}  Time evolution
:class: important

- Time evolution of wave function is governed by time-dependent Schrödinger equation.

  $$\boxed{i\hbar \frac{\partial \psi}{\partial t}=\hat{H}\psi}$$

- We are often interested in stationary states described by pure eigenfunctions where time dependnce does not figure explicitely. In mixed states described by superposition of eigenfunctions, however, leads to time dependece of observable quantities.  
```
  
  
  








