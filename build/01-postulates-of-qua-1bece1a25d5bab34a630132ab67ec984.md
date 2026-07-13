# Postulates of Quantum Mechanics

:::{note} **What you will learn**

- **Quantum mechanics rests on a few postulates** that were distilled from comparing theory with experiment.
- **The postulates are mathematical requirements** that guarantee physically meaningful solutions to the Schrödinger equation and connect abstract operators to experimental observables.
- **Once we accept these postulates**, quantum mechanics becomes a self-contained theory capable of explaining and computing all there is to know about atoms, molecules, and their interactions with radiation.
:::

### Postulate 1: Wave function

:::{important} **Wave function**

- **The square of the wave function $|\psi(x, t)|^2$ is a probability distribution** for finding the quantum object at location $x$ in space at time $t$.

$$P(x,t) = |\psi(x,t)|^2$$

$$\int |\psi(x,t)|^2 \, dx = 1$$

- In order to describe physically meaningful states of quantum objects as a probability distribution, the wave function (and its square) must be **continuous, single-valued, differentiable, and finite.** Functions that do not satisfy these criteria are discarded as non-physical.
:::

### Postulate 2: Operators

:::{important} **Operators**

- **Operators in QM are linear.** Linearity follows from the nature of the Schrödinger equation, which is a linear differential equation.

$$\hat{L}(c_1\psi_1 + c_2\psi_2 + ... + c_n\psi_n) = c_1\hat{L}\psi_1 + c_2\hat{L}\psi_2 + ... + c_n\hat{L}\psi_n$$

- **Operators in QM are Hermitian.** The Hermitian property of operators guarantees that eigenvalues are strictly real.

$$\int \psi^* (\hat{H}\phi) \, dx = \int \phi (\hat{H}\psi)^* \, dx = \int \phi \hat{H}^* \psi^* \, dx$$

$$\langle \phi |\hat{H} | \psi \rangle = \langle \psi |\hat{H} | \phi \rangle^{*}$$
:::

### Postulate 3: Eigenvalues

:::{important} **Eigenvalues**

- Eigenvalues $a_n$ of an operator $\hat{A}$ are the only possible values of the corresponding observable that can be measured in experiments.

$$\hat{A}\psi_n = a_n \psi_n$$
:::

### Postulate 4: Expectations

:::{important} **Expectations**

- The expectation, or average value, of observable $A$ in a state described by wave function $\psi$ is given by:

$$\boxed{\langle A \rangle = \int \psi^* \hat{A}\psi \, dx = \langle \psi | A | \psi \rangle}$$

- The expected value predicts the result of performing a large number of experiments that measure the observable and then averaging the outcomes.
:::

### Postulate 5: Time evolution

:::{important} **Time evolution**

- The time evolution of the wave function is governed by the time-dependent Schrödinger equation.

$$\boxed{i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi}$$
:::
