# Time-Dependent Perturbation Theory and Selection Rules



### Setup: Stationary States and a Time-Dependent Perturbation


We consider a Hamiltonian split into an exactly solvable part and a weak, time-dependent perturbation:

$$
\hat{H}(t) = \hat{H}_0 + \hat{V}(t)
$$

The unperturbed Hamiltonian $\hat{H}_0$ has known eigenstates and eigenvalues:

$$
\hat{H}_0 |n\rangle = E_n |n\rangle
$$

We expand the full time-dependent state in the stationary basis:

$$
|\Psi(t)\rangle = \sum_n c_n(t), e^{-iE_n t/\hbar} |n\rangle
$$

The time-dependent coefficients $c_n(t)$ encode transitions between stationary states caused by $\hat{V}(t)$.




### Deriving the First-Order Transition Amplitude


Insert the expansion into the time-dependent Schrödinger equation

$$
i\hbar \frac{\partial}{\partial t}|\Psi(t)\rangle = \hat{H}(t)|\Psi(t)\rangle
$$

After some algebra and using orthonormality $\langle m|n\rangle = \delta_{mn}$, you obtain the equation of motion for the coefficients:

$$
i\hbar, \dot{c}*m(t) = \sum_n c_n(t) V*{mn}(t), e^{i\omega_{mn} t}
$$

where

$$
V_{mn}(t) = \langle m|\hat V(t)|n\rangle, \qquad \omega_{mn} = \frac{E_m - E_n}{\hbar}
$$

Assume the system starts in state $|i\rangle$ at $t=0$:

$$
c_n(0) = \delta_{ni}, \quad c_i(0) = 1, \quad c_{f\neq i}(0) = 0
$$

In **first-order perturbation theory**, we approximate $c_n(t) \approx \delta_{ni}$ on the right-hand side (the perturbation is weak, so population remains mostly in the initial state). Then the equation for $c_f(t)$ becomes

$$
\dot{c}*f^{(1)}(t) = -\frac{i}{\hbar} V*{fi}(t), e^{i\omega_{fi} t}
$$

Integrating from $0$ to $t$:

$$
c_f^{(1)}(t) = -\frac{i}{\hbar} \int_0^t V_{fi}(t'), e^{i\omega_{fi} t'} dt'
$$

This is the **first-order transition amplitude** from state $|i\rangle$ to $|f\rangle$.

### Coupling to Light: Dipole Approximation


For an atom or molecule in a classical electromagnetic field, in the **electric dipole approximation** the perturbation is

$$
\hat{V}(t) = -\hat{\boldsymbol{\mu}}\cdot \mathbf{E}(t)
$$

For a monochromatic linearly polarized field

$$
\mathbf{E}(t) = \mathbf{E}_0 \cos(\omega t)
$$

the matrix element is

$$
V_{fi}(t) = \langle f|\hat{V}(t)|i\rangle = -\langle f|\hat{\boldsymbol{\mu}}\cdot \mathbf{E}_0|i\rangle \cos(\omega t)
$$

Define the (possibly complex) dipole matrix element

$$
\mu_{fi} = \langle f|\hat{\boldsymbol{\mu}}\cdot \hat{\mathbf{e}}|i\rangle
$$

where $\hat{\mathbf{e}}$ is the polarization direction of the field, and let $E_0 = |\mathbf{E}_0|$. Then

$$
V_{fi}(t) = -\mu_{fi} E_0 \cos(\omega t)
$$

Plugging into the transition amplitude:

$$
c_f^{(1)}(t) = \frac{i E_0}{\hbar} \mu_{fi} \int_0^t \cos(\omega t'), e^{i\omega_{fi} t'} dt'
$$


### Resonance Condition and Energy Conservation


Use the exponential form of the cosine:

$$
\cos(\omega t') = \frac{1}{2}\left(e^{i\omega t'} + e^{-i\omega t'}\right)
$$

Then the integral in $c_f^{(1)}(t)$ contains terms of the form

$$
\int_0^t e^{i(\omega_{fi} \pm \omega)t'} dt'
$$

If $\omega_{fi} \pm \omega$ is large, the exponential oscillates rapidly and the integral averages out to a small value. A **large transition amplitude** occurs when the exponent is nearly stationary:

$$
\omega_{fi} - \omega \approx 0 \quad \Rightarrow \quad \omega_{fi} \approx \omega
$$

This gives the familiar **energy conservation condition** for absorption:

$$
E_f - E_i = \hbar\omega
$$

Similarly, for stimulated emission one finds $E_f - E_i = -\hbar\omega$.




### From Transition Amplitudes to Selection Rules

:::{admonition} **Selection Rules**
:class: important

The **transition probability** (to first order) is

$$
P_{i\to f}(t) \approx |c_f^{(1)}(t)|^2 \propto |\mu_{fi}|^2
$$

- A transition $|i\rangle \to |f\rangle$ is only allowed (electric-dipole allowed) if the dipole matrix element

$$
\mu_{fi} = \langle f|\hat{\boldsymbol{\mu}}\cdot \hat{\mathbf{e}}|i\rangle \neq 0
$$


:::


If the matrix element is **exactly zero** due to symmetry, the transition is **dipole-forbidden** (in first order).

Selection rules therefore come from:

* the symmetry properties (angular, parity, etc.) of the **wavefunctions** $|i\rangle$ and $|f\rangle$
* the transformation properties of the **operator** $\hat{\boldsymbol{\mu}} \sim \mathbf{r}$ (a vector operator)




### Electric Dipole Selection Rules (Hydrogen-like Orbitals)


For an electron in a central potential (e.g., hydrogenic atom), stationary states are labeled by $|n, l, m_l\rangle$.

The position operator $\mathbf{r}$ transforms like an angular momentum 1 object (similar to the spherical harmonics $Y_{1m}$). From angular momentum coupling rules one obtains:

**Orbital angular momentum selection rule**

$$
\Delta l = l_f - l_i = \pm 1
$$

**Magnetic quantum number selection rule**

$$
\Delta m_l = m_{l,f} - m_{l,i} = 0, \pm 1
$$



:::{admonition} **Summary**
:class: tip

* Start from the time-dependent Schrödinger equation with $\hat{H}(t) = \hat{H}_0 + \hat{V}(t)$.
* Expand the state in the eigenbasis of $\hat{H}_0$ to obtain equations for $c_n(t)$.
* First-order perturbation theory gives a transition amplitude
  $$
  c_f^{(1)}(t) = -\frac{i}{\hbar} \int_0^t \langle f|\hat{V}(t')|i\rangle e^{i\omega_{fi} t'} dt'
  $$
* For an oscillating field, the integral is large only when $E_f - E_i = \pm \hbar\omega$ (energy conservation).
* The transition probability is proportional to $|\langle f|\hat{\boldsymbol{\mu}}|i\rangle|^2$.
* If the dipole matrix element is zero by symmetry, the transition is forbidden.
* For electric dipole transitions in atoms: $\Delta l = \pm 1$, $\Delta m_l = 0, \pm 1$, and parity changes.
  :::

.
