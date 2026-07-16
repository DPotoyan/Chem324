# Time Dependence

:::{admonition} **What you need to know**

- The **time-dependent Schrödinger equation** governs the evolution of the quantum wavefunction over time, $\psi(x,t)$. 
- **Stationary states** are eigenfunctions of the Hamiltonian $\hat{H}$ containing a spatial part and a time-dependent phase factor:  $\psi(x,t) = \psi(x) e^{-i E t / \hbar}$  
- The stationary states have definite energy and their probability distributions are **time-independent**.
- In more general situations, the wavefunction can be expressed as a **linear superposition of energy eigenstates**, with time evolution given by the phase factors of the eigenstates:  $\psi(x,t) = \sum_n c_n \psi_n(x) e^{-i E_n t / \hbar}$ 

- This superposition leads to **time-dependent probabilities** as different eigenstates interfere.
- The time-dependence of quantum states is key to understanding **quantum dynamics**, such as oscillations between states in **two-level systems** or time evolution of **quantum superpositions**.

:::



### Time Dependence of a Pure Eigenfunction

- Until now, we have largely ignored the time dependence of quantum systems. This is because we have primarily focused on pure eigenfunction states, $\psi_n(x,t)$, which exhibit no time-dependent behavior for observable quantities. The reason for this is straightforward.

$$\psi_n(x,t) = \psi_n(x) e^{-\frac{i}{\hbar}E_n t}$$

- In any probabilistic calculation, the time dependence vanishes because the expressions involve the square of the wavefunction. The absolute value of the complex time-dependent phase factor equals unity:

$$\mid \psi_n(x,t) \mid^2 = \psi_n^*(x)\psi_n(x) e^{-\frac{i}{\hbar}E_n t} e^{+\frac{i}{\hbar}E_n t} = \mid \psi_n(x) \mid^2$$

- Similarly, for the expectation value of an operator $\hat{A}$, the time-dependent phases cancel out, leaving only the spatial part:

$$\langle A \rangle = \int \psi_n^*(x) e^{+\frac{i}{\hbar}E_n t} \hat{A} \psi_n(x) e^{-\frac{i}{\hbar}E_n t} dx = \int \psi_n^*(x) \hat{A} \psi_n(x) dx$$

- Will we always have this fortunate cancellation of time dependence? The answer is no. When the system is described as a **linear superposition** of eigenstates, time dependence reappears in a significant way.


### Time Dependence of a Superposition of Eigenfunctions

- Let us start with a superposition state of two energy eigenfunctions at time $t=0$:

$$\mid \psi(0) \rangle =c_1\mid 1 \rangle + c_2 \mid 2 \rangle$$

- What would the state be after some time $t$? By virtue of separation of variables, we add the time dependence as a multiplicative factor for each eigenfunction:

$$\mid \psi(t) \rangle =c_1 e^{-\frac{i}{\hbar}E_1 t}\mid 1 \rangle + c_2 e^{-\frac{i}{\hbar}E_2 t}\mid 2 \rangle= c_1(t)\mid 1\rangle+c_2(t) \mid 2 \rangle$$

- Thus we see that the coefficients change over time. This means our state vector moves in the functional space spanned by the fixed orthogonal eigenfunctions! We can verify that this expression satisfies the time-dependent Schrödinger equation by plugging it in.

:::{admonition} **Proof that the superposition obeys the time-dependent Schrödinger equation**
:class: dropdown

$$  i\hbar\frac{\partial}{\partial t}\mid \psi \rangle =\hat{H}\psi(t)\rangle $$

*Left hand side :*

$$i\hbar \Big( -\frac{i}{\hbar}E_1 c_1 e^{-\frac{i}{\hbar}E_1 t}\mid 1\rangle-\frac{i}{\hbar}E_2 c_2 e^{-\frac{i}{\hbar}E_2 t}\mid 2\rangle \Big) = E_1 c_1(t)\mid 1 \rangle +E_2 c_2(t)\mid 2 \rangle$$

*Right hand side:*

$$c_1 e^{-\frac{i}{\hbar}E_1 t}\hat{H}\mid 1 \rangle + c_2 e^{-\frac{i}{\hbar}E_2 t}\hat{H} \mid 2 \rangle = E_1 c_1(t)\mid 1 \rangle +E_2 c_2(t)\mid 2 \rangle $$

:::



```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
```

```{marimo} python
def psi_n(x, n):
    """Time-independent wavefunction for a particle in a box."""
    L = 1 # set box length

    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)

def T_n(t, n):
    """Time dependence factor for the wavefunction."""
    L = 1 # set box length
    m, hbar = 1, 1 # set atomic units
    En = n**2 * np.pi**2 * hbar**2 / (2 * m * L**2)

    return np.exp(-1j * En * t / hbar)

def psi_combined(x, t, c1=1, c2=1, n1=1, n2=2):
    """Time-dependent wavefunction for a normalized superposition of two PIB states."""

    norm = np.sqrt(c1**2 + c2**2)

    return (c1 * psi_n(x, n1) * T_n(t, n1) + c2 * psi_n(x, n2) * T_n(t, n2)) / norm
```

```{marimo} python
def plot_wavefunction(t=0, c1=1, c2=1, n1=1, n2=2):

    L = 1.0
    x = np.linspace(0, L, 1000)

    psi_squared_x = np.abs(psi_combined(x, t, c1=c1, c2=c2, n1=n1, n2=n2))**2

    plt.plot(x, psi_squared_x, color="#3d81f6", lw=2)
    plt.fill_between(x, psi_squared_x, alpha=0.2, color="#3d81f6")

    plt.title(f"$|\\Psi(x,t)|^2$ for states n={n1} and n={n2} at t={t:.2f}")
    plt.xlabel('x')
    plt.ylabel(r'$|\Psi(x, t)|^2$')
    plt.grid(True, alpha=0.4)
    plt.ylim([0, 4.5])
    plt.gcf()
```

```{marimo} python
:hide-code: true

t_qw = mo.ui.slider(0, 10.0, step=0.1, value=0.0, show_value=True, label="time t")
n2_qw = mo.ui.slider(2, 6, step=1, value=2, show_value=True, label="second state n2")
mo.hstack([t_qw, n2_qw], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

plot_wavefunction(t=t_qw.value, c1=1, c2=1, n1=1, n2=n2_qw.value)
plt.gcf()
```

- Drag the **time slider** and watch the probability sloshing between the two walls: the interference term beats at the frequency $(E_{n_2} - E_1)/\hbar$. Raising $n_2$ makes the pattern richer and the beat faster. A single eigenstate would sit perfectly still; motion in quantum mechanics lives in superpositions.
### Normalization is time independent!

- Certain quantities remain invariant under time evolution. For instance, it is natural to expect that normalization does not change over time: the particle must always be located somewhere within the box at any given moment.

$$\mid \psi(t)\rangle = \sum_n c_n e^{-\frac{i}{\hbar}E_n t} \mid n\rangle$$

- The normalization condition is expressed as:

$$\langle \psi(t) \mid \psi(t)\rangle = \sum_n \sum_k \langle n \mid c^*_n e^{\frac{i}{\hbar}E_n t} \cdot c_k e^{-\frac{i}{\hbar}E_k t} \mid k\rangle = \sum_n \sum_k c^*_n c_k e^{-\frac{i}{\hbar}(E_k - E_n)t} \delta_{kn} = \sum_n \mid c_n \mid^2 = 1$$

- In the final step, we use the fact that the eigenfunctions are orthogonal, meaning $\langle n \mid k \rangle = 0$ for $n \neq k$, so the cross terms vanish and only the diagonal terms, where $n = k$, survive.


### Constants of Motion

- Quantities that remain conserved over time are called **constants of motion**. In quantum mechanics, we typically deal with expectations or averages rather than sharply defined values.

- However, the principle of energy conservation dictates that the **average total energy** must be a conserved quantity. To determine whether a particular quantity depends on time, we take the time derivative of the expectation value:

  $$\langle A \rangle = \langle \psi \mid \hat{A} \mid \psi \rangle$$

  The time derivative of this expectation value is:

  $$
  \frac{\partial}{\partial t}\langle A \rangle = \langle \frac{\partial \psi}{\partial t} \mid \hat{A} \mid \psi \rangle + \langle \psi \mid \hat{A} \mid \frac{\partial \psi}{\partial t} \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle
  $$

- Now, using the time-dependent Schrödinger equation,  

  $$
  i\hbar \frac{\partial}{\partial t} \mid \psi \rangle = \hat{H} \mid \psi \rangle
  $$  

  we can express the time derivatives of the bras and kets as:

  $$\langle \frac{\partial \psi}{\partial t} \mid = -\frac{1}{i\hbar} \langle \psi \mid \hat{H},$$
  $$\mid \frac{\partial \psi}{\partial t} \rangle = \frac{1}{i\hbar} \hat{H} \mid \psi \rangle.$$

- Substituting these into the time derivative of the expectation value, we obtain:

  $$\frac{\partial}{\partial t}\langle A \rangle = \frac{1}{i\hbar} \langle \psi \mid \hat{A}\hat{H} \mid \psi \rangle - \frac{1}{i\hbar} \langle \psi \mid \hat{H}\hat{A} \mid \psi \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle$$
  
:::{important} **Time dependence of expectation**

  $$
  \frac{\partial}{\partial t}\langle A \rangle = \frac{1}{i\hbar} \langle \psi \mid [\hat{A}, \hat{H}] \mid \psi \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle.
  $$

:::

- This important relationship shows that if the operator $\hat{A}$ does not explicitly depend on time, i.e., $\frac{\partial \hat{A}}{\partial t} = 0$, then quantities that **commute with the Hamiltonian** $[\hat{A}, \hat{H}] = 0$ will be constants of motion. Those that do not commute, $[\hat{A}, \hat{H}] \neq 0$, will evolve over time.

- Since the Hamiltonian commutes with itself and does not depend on time, the **energy** is conserved.

  $$
  \frac{\partial}{\partial t}\langle E \rangle = 0
  $$  
 

### Quantum Dynamics

:::{figure} ./images/gaussian_potential.gif
:label: fig-time-dependence-1
:alt: pib1
:width: 300px

Wavefunction dynamics in a Gaussian potential, showing the probability density along with the real and imaginary parts.
:::

:::{figure} ./images/barrier_potential.gif
:label: fig-time-dependence-2
:alt: pib1
:width: 300px

Wavefunction dynamics in a barrier potential, showing the probability density along with the real and imaginary parts.
:::

:::{seealso} Chapter demos
Computational lab for this chapter: [Numerical Schrödinger solver](../demos/07-demo-numerical-schrodinger.md)
:::
