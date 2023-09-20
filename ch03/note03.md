## Postulates of Quantum Mechanics

```{admonition} What you need to know
:class: note
- **A set of fundamental postulates** make quantum mechanics a self contained fool-proof logical theory. Armed with such a theory all of chemistry and biology “in theory” reduces to mere application of Schrödinger equation. In practice theory is not so easy to apply. 
```

### Postulate 1: Wave function

```{admonition}  Wave function 
:class: important

- The state of a system is completely specified by a wave function which contains all the dynamical information. The square of wave function is a probability distribution of finding the object in space.

$$P(x,t)=|\psi(x,t)|^2 \,\,\,   \,\,\, \int |\psi(x,t)|^2 dx=1 $$

- Wave function that describes real physical objects should be well behaved in order to correspond to probability distribution.
- Continuous, single-valued, differentiable and finite over finite range. 
- Functions that do not satisfy these criteria are discarded as non-physical.  
```

### Postulate 2: Operators


```{admonition}  Operators
:class: important

- For every observable quantity there is a corresponding linear and Hermitian operator in quantum mechanics.

$$\hat{A} (c_1 \psi_i+c_2 \psi_2) =  c_1 \hat{A}\psi_i+c_2 \hat{A}\psi_2$$

$$\int \psi^* (\hat{A}\phi) dx = \int \phi (\hat{A} \psi)^* dx$$

- Linearity of opeartors follows from the nature of Schrödinger equation which is a linear differenetial equation. Linearity implies a distirbutive property of opeartors when applied to any linear combination of functions. 

$$\hat{L} (c_1\psi_1+c_2\psi_2+...+c_n\psi_n)=c_1\hat{L} \psi_1+c_2\hat{L}\psi_2+...+c_n\hat{L}\psi_n $$

- Beside being linear operators of observables in quantum mechanics are Hermitian. Hermtian property guarantees that eigenvalues are strictly real. And since eigenvalues are the only values observed in experimental measurements it is sensible to expect that one would not be getting mixed complex and real numbers in the experiments. An Hermitian property is defined by the following equality where an  operator can go into complex conjugate mode and act on complex conjugate pair of the function. 

$$\int \psi^* (\hat{H} \phi) dx = \int \phi (\hat{H} \psi)^* dx =\int \phi \hat{H}^* \psi^* dx $$
```


### Postulate 3: Eigenvalues


```{admonition}  Eigenvalues
:class: important

- Eigenvalues of an operator are the only possible values of the corresponding observable that can be measured in the experiments. 

$$\hat{A}\psi_n =a_n \psi_n $$

Eigenvalues of an operator $\hat{A}$ exhaust the posisble values one can get in the experiments. Put another way eiganvalues are the only kind fo values to be measured. As a result of boundary conditions one often has discrete eigenvalues for observables which are indexed by integer numbers known as quantum numbers. 

$$\hat{A}\psi_n = a_n\psi_n $$

```



### Postulate 4: Expectations


```{admonition}  Expectations
:class: important

- Expectation or the average value of observable A in a state described by wave 
  function $\psi$ is given by expression:

$$\langle A \rangle = \int \psi^* \hat{A}\psi dx $$

  What is the expected value of an abservable obtained  on average as a result of large number of experiments? The answer is given by plugging operator $\hat{A}$ corresponding to observable $A$ into an expression of average with wave function square acting as probabilty distribution function.  

$$\langle A \rangle =\int \psi^* \hat{A}\psi dx $$

```


### Postulate 5: Time evolution


```{admonition}  Time evolution
:class: important

- Time evolution of wave function is governed by time-dependent Schrödinger equation.

  $$i\hbar \frac{\partial \psi}{\partial t}=\hat{H}\psi $$

- State of quantum mechanical system evolves in time according to Schrödinger equation.

$$i\hbar \frac{\partial \psi}{\partial t}=\hat{H}\psi $$

- We are often interested in stationary states described by pure eigenfunctions where time dependnce does not figure explicitely. In mixed states described by superposition of eigenfunctions, however, leads to time dependece of observable quantities.  
```
  
  
  








