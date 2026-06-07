## Postulates 

:::{admonition} **What you need to know**
:class: note

- Quantum Mechanics can be built on top of few postulates which have been learned from comparisons of theory with the experiments.
- Postulates are mathematical requirements which ensure physically meaningul solutions to schrodinger equation and which provide connection between abstract concepts of operators and experimental observables.
- Once we accept thses postulates Quantum Mechanics becomes a self-contained theory capable of explaining and computing all that is to know about atoms and molecules and their interactions with radiation. 
:::

### Postulate 1: Wave function

:::{admonition}  Wave function 
:class: important

- **The square of wave function $|\psi(x, t)|^2$ is a probability distribution of finding the quantum object at an $x$ location in space and at a time $t$** 


$$P(x,t)=|\psi(x,t)|^2 \,\,\,$$   

$$\int |\psi(x,t)|^2 dx=1 $$

- In order to describe physically meaningful states of quantum objects as a probability distribution function, the wave function (and its square) must be **Continuous, single-valued, differentiable and finite.** Functions that do not satisfy these criteria are discarded as non-physical.  


:::

### Postulate 2: Operators


:::{admonition}  Operators
:class: important

- **Operators in QM are Linear**. Linearity follows from the nature of Schrödinger equation which is a linear differenetial equation.  

$$\hat{L} (c_1\psi_1+c_2\psi_2+...+c_n\psi_n)=c_1\hat{L} \psi_1+c_2\hat{L}\psi_2+...+c_n\hat{L}\psi_n $$

- **Operators in QM are Hermtian**. Hermitian property of operators guarantees that eigenvalues are strictly real.

$$\int \psi^* (\hat{H} \phi) dx = \int \phi (\hat{H} \psi)^* dx =\int \phi \hat{H}^* \psi^* dx $$


$$\langle \phi |\hat{H} | \psi \rangle = \langle \psi |\hat{H} | \phi \rangle^{*}$$
:::


### Postulate 3: Eigenvalues

:::{admonition}  Eigenvalues
:class: important

- Eigenvalues $a_n$ of an operator $\hat{A}$ are the only possible values of the corresponding observable that can be measured in the experiments. 

$$\hat{A}\psi_n =a_n \psi_n $$
:::


### Postulate 4: Expectations

:::{admonition}  Expectations
:class: important

- Expectation or the average value of observable A in a state described by wave 
  function $\psi$ is given by expression:

$$\boxed{\langle A \rangle = \int \psi^* \hat{A}\psi dx = \langle \psi | A| \psi \rangle}$$

- Expected value predicts what would result from doing large number of experiments measuring observable and then taking average.  

:::


### Postulate 5: Time evolution


:::{admonition}  Time evolution
:class: important

- Time evolution of wave function is governed by time-dependent Schrödinger equation.

  $$\boxed{i\hbar \frac{\partial \psi}{\partial t}=\hat{H}\psi}$$

:::
  
  
  








