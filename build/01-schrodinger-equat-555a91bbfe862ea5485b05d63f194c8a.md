---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Schrödinger Equation and the Wavefunction

:::{note} **What you need to know**

- Combining the classical wave equation with the Planck and de Broglie relations produces **Schrödinger's equation**, the fundamental equation of motion of the quantum world.
- **Separation of variables** splits the time-dependent equation into an oscillatory time factor $e^{-iEt/\hbar}$ and the **time-independent Schrödinger equation**, our workhorse for the rest of the course.
- The wavefunction itself is complex and not directly measurable; its absolute square $|\psi(x)|^2$ is the **probability distribution** for finding the particle. Physical wavefunctions must be **normalized**.
- Every measurable quantity corresponds to an **operator**, and predictions come as **expectation values** $\langle A \rangle = \int \psi^{*} \hat{A}\, \psi\, dx$.
- Solving the Schrödinger equation means finding the **eigenfunctions** $\psi_n$ and **eigenvalues** $E_n$ of the Hamiltonian. Boundary conditions make the spectrum discrete, and linearity makes superpositions $\sum_n c_n \psi_n$ solutions too.

:::

## The exciting journey into the microscopic world

- In the next few sections, we will introduce **Schrödinger's Equation (SE)**, one of the fundamental laws of physics. A "fundamental law" means that SE cannot be derived from more basic principles; it can only be inferred or hypothesized based on experimental evidence. Its validity is supported by countless successful quantitative predictions and explanations of experimental observations.

- It's important to emphasize that there has never been an instance where **quantum mechanics** has failed when applied correctly. The physical world is inherently quantum, especially at small scales. **Quantum mechanics works flawlessly** at all scales and in all situations where it has been properly applied.


:::{figure} images/SE_intro.jpeg
:label: fig-schrodinger-equation-1
:alt: SE-intro
:width: 300px

You are now entering the quantum world. Proceed with caution.
:::

### What do we require from the new quantum theory?


- Recall that while **classical mechanics** is valid at large scales, it completely fails to describe motion at the atomic and molecular levels. A new, accurate equation of motion is required to explain phenomena such as:

  - The **quantized nature of energy**, as observed in experiments involving blackbody radiation and atomic and molecular spectra.
  
  - **Wave-particle duality**, demonstrated through electron diffraction, Compton scattering, and double-slit experiments.


:::{figure} images/SE_intro2.gif
:label: fig-schrodinger-equation-2
:alt: SE-intro
:width: 300px

Schrödinger had to accept that electrons are correctly described by wave functions.
:::

### Quantum wave equation

- In 1925/1926 Erwin Schrödinger, an expert on the physics of waves, derived a new equation of motion that predicts quantum phenomena such as energy quantization and wave-particle duality from first principles.

- We can trace Schrödinger's approach by starting with the classical wave equation:

  $$\frac{\partial^2 \Psi(x,t)}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2 \Psi(x,t)}{\partial t^2}$$

- The classical wave equation we have seen can produce traveling or standing waves depending on boundary conditions. Let us pick a general periodic traveling wave, for instance:

$$\Psi(x,t) = Ae^{i(kx-\omega t)}$$

- We are going to plug into a wave function the two key quantum relations discovered empirically and then see what kind of wave equation can produce it:

  - **Plug wave-particle duality via De Broglie relation:** 
  
  $$p=h/\lambda=\hbar k\,\,\,\, where\,\,\,\, k=\frac{2\pi}{\lambda}$$

  - **Plug energy quantization via Planck equation:**  
  
  $$E=h\nu=\hbar\omega\,\,\,\, where\,\,\,\, \omega=2\pi\nu$$

- **Quantum wave function** 

$$\Psi(x,t)=Ae^{\frac{i}{\hbar}(px-E t)}$$

- **What equation can generate such quantum wave functions?** To find out we need to take derivatives with respect to time and space.

### From Quantum Wave Function to Quantum Wave Equation

- **Time Part**: When we take the time derivative of the wave function, we find that the total energy appears as a multiplicative factor. This is significant because, in quantum mechanics, total energy is conserved. The relationship between energy and the time dependence of the wave function is given by:

$$
\frac{\partial \Psi(x,t)}{\partial t} = -\frac{i}{\hbar} E \Psi(x,t)
$$


- **Spatial Part**: To recover the total energy from the spatial part of the wave function, we take two spatial derivatives. 

$$
\frac{\partial \Psi(x,t)}{\partial x} = \frac{i}{\hbar} p \Psi(x,t)
$$


$$
\frac{\partial^2 \Psi(x,t)}{\partial x^2} = -\frac{p^2}{\hbar^2} \Psi(x,t) = -\frac{2m(E - V)}{\hbar^2} \Psi(x,t)
$$
- This equation, in which the time variable is absent, is the **time-independent Schrödinger equation.** We will come back to it shortly. 
- **Joining time and spatial parts** by expressing the kinetic energy as a difference between total and potential energies $K = E-V$ and eliminating $E$ we get:

:::{important} **Time-Dependent Schrödinger Equation**

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} + V(x) \Psi = i \hbar \frac{\partial \Psi}{\partial t}
$$
:::

### Quantum vs Classical Wave equation


:::{figure} images/SE-image.png
:label: fig-schrodinger-equation-3
:alt: SE-intro
:width: 300px

Dissecting the Schrödinger equation, using the 1D version for simplicity.
:::

- The Schrödinger equation describes the evolution of the wave function $\Psi(x,t)$ for a quantum system such as an electron or atom in a potential $V(x)$. 
- Unlike the classical wave equation, there is only a single time derivative. The presence of $i$ generates oscillatory solutions in the complex plane, which is why we call it a quantum wave equation. 
- What is the meaning of $\Psi(x,t)$? It is generally complex and so cannot stand for any real measurable quantity. We will see how to extract information from $\Psi$ later. 
- Note that we are focusing on the 1D case for simplicity. Generalizing to 3D involves adding similar terms that depend on the $y$ and $z$ coordinates of every quantum object. 

### Separation of Variables and the Time-Independent Schrödinger Equation

- By assuming the wave function can be separated into a product of a spatial part and a time part, $\Psi(x,t) = \psi(x) T(t)$, we can solve for each part independently:
- The time part $T(t)=e^{-iEt/\hbar}$ yields an oscillatory solution related to the total energy.
- The spatial part $\psi(x)$ satisfies the **time-independent Schrödinger equation**, which we solve to obtain stationary states.

:::{important} **Quantum Wave function**

$$\Psi(x,t) = \psi(x)\cdot e^{-iEt/\hbar}$$

- The hard part is finding $\psi(x)$, which depends on the system, e.g. the form of the potential energy function $V$.

:::

- This method is crucial for solving quantum systems, particularly in cases where the potential $V(x)$ does not depend on time.
- Plugging in $\psi(x) T(t)$ and cancelling the time part, we are back to the time-independent equation we obtained earlier.  

:::{important} **Time-Independent Schrödinger Equation**

$$
-\frac{\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2} + V(x) \psi = E \psi
$$
:::

## From the equation to its meaning

We now have the equation and a strategy for solving it. What we do not yet have is the meaning of the object the equation keeps handing us. This half of the lecture answers that question and turns $\psi$ into numbers an experiment can check.

### What is the meaning of a wave-function $\psi$ ? 

- In the classical wave equation, the wave function has a clear mechanical interpretation: it represents the degree of disturbance in the wave. For example, it can describe the elevation of a guitar string from its resting position.

- In contrast, the quantum wave function is less intuitive. The wave function itself does not have direct physical meaning, as it is generally a complex function. To connect it to measurable quantities, we need to extract real values from it that correspond to physical observables.

- The key insight is that the absolute square of the wave function gives the probability distribution:

:::{important} **Probabilistic meaning of quantum wave function (square)**

  $$p(x) = \psi^{*}(x) \cdot \psi(x) = |\psi(x)|^2$$
  
:::

- $p(x)$ is a **probability distribution function**. It describes the likelihood of finding a quantum object at a position $x$.
- $p(x)\,dx$ gives the probability of finding the particle in a tiny part of space inside the interval $[x, x+dx]$.

- In three-dimensional space, the analogous expression is:

  $$p(x, y, z) = \psi(x, y, z)^{*} \cdot \psi(x, y, z)$$

### Probability Refresher

- Before introducing quantum mechanics and wavefunctions, let's recall some core ideas from probability.

#### Random Variables

- A **random variable** assigns numbers to the outcomes of an experiment. For example, how many squirrels you see each day is a random variable.
- **Discrete examples**: dice rolls, coin flips.  
- **Continuous examples**: particle position, measurement noise.  

#### Probability Distributions

- A continuous random variable is fully described by a distribution over all possible values. We call this object a probability distribution $p(x)$, which must integrate (or sum, in the discrete case) to one, showing that we cover all possibilities and that each possibility is assigned a fraction of 1.

:::{important} **Rules of Probabilities**

- **Non-negative**: 

$$p(x) \geq 0$$


- **Normalized**: 

$$\int_{-\infty}^{\infty} p(x)\,dx = 1$$  

- **Mean (expectation)**:  

  $$
  \mu = \langle x \rangle = \int_{-\infty}^{\infty} x\,p(x)\,dx
  $$

- **Variance**:  

  $$
  \sigma^2 = \langle x^2 \rangle - \langle x \rangle^2
  $$

:::

#### Further Exploration
- [Video overview](https://www.youtube.com/watch?v=QxqxdQ_g2uw)  
- [Interactive probability explorer](https://idiot.computer/probs/)  

:::{note} **Worked Examples of Probability distributions**
:class: dropdown

**1. Fair coin Flip**

- Random variable $X \in \{0,1\}$ with

$$
P(X=0) = 0.5, \quad P(X=1) = 0.5
$$

**Normalization**

$$
P(0)+P(1) = 0.5+0.5 = 1
$$

**Mean**

$$
\langle X \rangle = \sum_x xP(x) = 0\cdot 0.5 + 1\cdot 0.5 = 0.5
$$

**Variance**

$$
\langle X^2 \rangle = 0^2\cdot 0.5 + 1^2\cdot 0.5 = 0.5
$$

$$
\sigma^2 = \langle X^2 \rangle - \langle X \rangle^2 = 0.5 - (0.5)^2 = 0.25
$$



**2. Uniform Distribution on [0,1]**

- PDF:
$$
p(x) = 
\begin{cases}
1, & 0 \leq x \leq 1 \\
0, & \text{otherwise}
\end{cases}
$$

**Normalization**

$$
\int_0^1 1 \, dx = 1
$$

**Mean**

$$
\langle x \rangle = \int_0^1 x \, dx = \left.\frac{x^2}{2}\right|_0^1 = \frac{1}{2}
$$

**Variance**

$$
\langle x^2 \rangle = \int_0^1 x^2 \, dx = \left.\frac{x^3}{3}\right|_0^1 = \frac{1}{3}
$$

$$
\sigma^2 = \frac{1}{3} - \left(\frac{1}{2}\right)^2 = \frac{1}{12}
$$




**Gaussian Distribution $\mathcal{N}(0,1)$**

- PDF:
$$
p(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
$$

**Normalization**

$$
\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 1
$$

(This is the famous Gaussian integral.)

**Mean**

$$
\langle x \rangle = \int_{-\infty}^\infty x\,p(x)\,dx = 0 \quad \text{(odd function)}
$$

**Variance**

$$
\langle x^2 \rangle = \int_{-\infty}^\infty x^2 \frac{1}{\sqrt{2\pi}} e^{-x^2/2}\,dx = 1
$$

$$
\sigma^2 = 1 - 0^2 = 1
$$

:::

```{code-cell} python
:tags: [hide-input]
import matplotlib.pyplot as plt
import numpy as np

# Discrete probabilities (fair dice)
outcomes = np.arange(1, 7)
probs = np.ones_like(outcomes) / 6

plt.bar(outcomes, probs)
plt.xlabel("Dice outcome")
plt.ylabel("Probability")
plt.title("PMF of a Fair Die")
plt.show()
```

```{code-cell} python
:tags: [hide-input]
# -----------------------------
# Correct sampling for H-atom 1s
# -----------------------------
N = 6000
a0 = 1.0

# For 1s: if x = 2r/a0, then x ~ Gamma(k=3, theta=1)
x = np.random.gamma(shape=3.0, scale=1.0, size=N)
r = 0.5 * a0 * x

# Isotropic angles
u = np.random.rand(N)
theta = np.arccos(1 - 2*u)
phi = 2*np.pi*np.random.rand(N)

# Convert to Cartesian and take a 2D projection
x3 = r * np.sin(theta) * np.cos(phi)
y3 = r * np.sin(theta) * np.sin(phi)

# Histogram for the shell probability density P(r) (per unit r)
bins = np.linspace(0, 6*a0, 80)
hist, edges = np.histogram(r, bins=bins, density=True)
centers = 0.5*(edges[1:] + edges[:-1])

# Analytical radial distribution P(r) = 4 r^2 |psi|^2 = 4 r^2 / (a0^3*pi) * exp(-2r/a0) * pi
# Simplifies to: P(r) = (4/a0^3) r^2 exp(-2r/a0), which integrates to 1
rr = np.linspace(0, bins[-1], 400)
P_r = (4.0/(a0**3)) * rr**2 * np.exp(-2*rr/a0)

# Side-by-side subplots: dot cloud and radial distribution

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Left: simulated dot cloud
axs[0].scatter(x3, y3, s=1, alpha=0.5)
axs[0].set_title("Hydrogen 1s: position observations (2D projection)")
axs[0].set_xlabel("x [$a_0$]")
axs[0].set_ylabel("y [$a_0$]")
axs[0].set_aspect('equal')

# Right: radial distribution histogram + analytical curve
axs[1].plot(centers, hist, lw=2, label="Monte Carlo (histogram)")
axs[1].plot(rr, P_r, lw=2, linestyle="--", label="Analytical 1s")
axs[1].set_title("Radial probability distribution")
axs[1].set_xlabel("r [$a_0$]")
axs[1].set_ylabel("$P(r)$")
axs[1].legend()

plt.tight_layout()
plt.show()
```

### Normalization of wavefunction

- For the wave function to represent a proper probability distribution, it must be normalizable. If it is not normalizable, the wave function is only proportional to a probability distribution and not equal to it.

- **Normalization** of $\psi^2$ ensures that there is absolute certainty that the quantum object exists somewhere in space. In an experiment, when searching for a quantum particle across the entire space, normalization guarantees that you will find it somewhere.

- **Normalization in 1D**:

  $$\int^{+\infty}_{-\infty} |\psi(x)|^2 dx = \int^{+\infty}_{-\infty} p(x) dx = 1$$

- To normalize a wave function $\psi'$, multiply it by a constant: $\psi = N\psi'$. The constant $N$ is determined by plugging this expression into the normalization condition. In other words, normalization determines the multiplicative factor in front of the wave function.

- **Normalization in 3D**:

  $$\int^{+\infty}_{-\infty} \int^{+\infty}_{-\infty} \int^{+\infty}_{-\infty} |\psi(x, y, z)|^2 dx \, dy \, dz = 1$$


:::{admonition} **Normalization example**
:class: info, dropdown

- Given the wave function $\psi(x)=x$ on the range $[0,1]$, normalize it so that it becomes a proper probability distribution function.

We require

$$
\int_0^1 |\psi(x)|^2 \, dx = 1.
$$

Substitute $\psi(x)=C\,x$:

$$
\int_0^1 (C\,x)^2 \, dx = 1,
$$

$$
C^2 \int_0^1 x^2 \, dx = 1,
$$

$$
C^2 \cdot \frac{1}{3} = 1.
$$


$$
C^2 = 3 \quad \Rightarrow \quad C = \sqrt{3}.
$$

Therefore the normalized wave function is

$$
\psi(x) = \sqrt{3}\,x, \quad 0 \leq x \leq 1.
$$

:::

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

# Define x values
x = np.linspace(0, 1, 500)

# Unnormalized psi
psi_unnorm = x
psi2_unnorm = psi_unnorm**2

# Normalized psi (C = sqrt(3))
psi_norm = np.sqrt(3) * x
psi2_norm = psi_norm**2

# Compute integrals for annotation
area_unnorm = np.trapezoid(psi2_unnorm, x)
area_norm = np.trapezoid(psi2_norm, x)

# Create the figure and axes
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Plot 1: Unnormalized psi² ---
axes[0].fill_between(x, psi2_unnorm, alpha=0.4, color="blue")
axes[0].set_title("Unnormalized $|\psi(x)|^2$")
axes[0].set_xlabel("x")
axes[0].set_ylabel(r"$|\psi(x)|^2$")
axes[0].grid(True)
axes[0].text(0.5, 0.2, rf"Area = {area_unnorm:.2f}", 
             transform=axes[0].transAxes, fontsize=12, color="blue")

# --- Plot 2: Normalized psi² ---
axes[1].fill_between(x, psi2_norm, alpha=0.4, color="green")
axes[1].set_title("Normalized $|\psi(x)|^2$")
axes[1].set_xlabel("x")
axes[1].set_ylabel(r"$|\psi(x)|^2$")
axes[1].grid(True)
axes[1].text(0.5, 0.2, rf"Area = {area_norm:.2f}", 
             transform=axes[1].transAxes, fontsize=12, color="green")

plt.tight_layout()
plt.show()
```


### What can we do with probability distribution functions (PDF)? 

- By definition, the probability distribution function $p(x)$ lets us quantify the probability that a quantum "particle" is located in an infinitesimal slice $[x, x+dx]$ around the point $x$. This then enables us to find the probability in any finite region $[a,b]$ simply by integrating:

  $$p(a<x<b)=\int_a^b |\psi(x)|^2dx$$

- In higher dimensions, e.g. 3D, we can locate the particle within a volume element $dx\,dy\,dz$, or any finite volume, via a similar integration:

  $$p(a_x<x<b_x,a_y<y<b_y, a_z<z<b_z )=\int^{b_x}_{a_x}  \int^{b_y}_{a_y}  \int^{b_z}_{a_z} |\psi(x,y,z)|^2dx dy dz$$


### The Mathematical Language of Quantum Mechanics: Operators

- To streamline our discussion and draw analogies with classical intuition, we need to introduce some essential **notation and terminology**.

- In quantum mechanics, we define **operators** as mathematical entities that transform one function into another. An operator can perform various actions on a function, such as differentiation, integration, addition, multiplication, and more. In this way, operators serve as tools to manipulate wave functions and extract physical information.


:::{figure} images/SE_intro3.jpg
:label: fig-schrodinger-equation-4
:alt: SE-intro
:width: 300px

Analogy of operators with ordinary functions.
:::

:::{admonition} **Example of operators**
:class: dropdown

- Let us take the function $e^{2x}$ as an example and see how operator notation works:

$$\frac{d^2}{dx^2} e^{2x} = 4e^{2x}$$

$$\hat{A} f =4f$$

-  Here we say that the operator $\hat{A}$ acts on the function $e^{2x}$ to produce another function, which in this case is the same function multiplied by 4.

- In general, operators can be anything placed in front of a function $f(x)$. Here are a few more examples of operators:

  - $\hat{A}f = x$ multiplies function by x, e.g $\hat{A}e^{2x} = xe^{2x}$
  - $\hat{A} = -i$ multiplies function by $-i$, e.g $\hat{A}e^{2x} = -ie^{2x}$
  - $\hat{A} = \sqrt{}$, takes square root, e.g $\hat{A}e^{2x} = e^{x}$
  - $\hat{A} = (d/dx +x^2)$, takes derivative then adds $x^2$ multiplication $\hat{A}e^{2x} = 4e^{2x}+x^2e^{2x} = (4+x^2)e^{2x}$

:::


### Linear operators

- Linear means that an operator acting on a sum of functions does not change the power of any of the functions. 

$$\hat{A}[c_1 f_1(x)+c_2f_2(x)]=  c_1 \hat{A}f_1(x)+c_2 \hat{A}f_2(x)$$

- The Schrödinger equation is a linear differential equation. Hence it can be written as a linear operator acting on a wave function.

:::{admonition} **Example of linear operators**
:class: dropdown

- Which of the following would be linear operator? $\hat{A}=\frac{d}{dx}$,      $\hat{B}=\int dx$       $\hat{C}=\sqrt{}$.


- Using the rules of calculus, we know that the derivative and integral act on each term in the sum:

$$\frac{d}{dx}(c_1f_1+c_2f_2) = c_1\frac{df_1}{dx}+c_2\frac{df_2}{dx}$$

$$\int(c_1f_1+c_2f_2)dx = c_1\int f_1dx+c_2\int f_2dx$$

- For the square root, the linearity property does not hold!

$$\sqrt{(c_1f_1+c_2f_2)} \neq c_1\sqrt{f_1} +c_2\sqrt{f_2}$$

:::





### Schrödinger equation in operator notation

- By expressing the equation in operator notation, we can start to recognize various terms and see that the Schrödinger equation, like any proper equation of motion, embodies the principle of total energy conservation:
- Let us take the Schrödinger equation and denote the differentials as operators acting on the wave function. For example, let us look at the two sides of the time-dependent Schrödinger equation: $
\left[ -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} + V(x) \right] \Psi
$ and $i\hbar \frac{\partial }{\partial t} \Psi$
- The operator of the position part is called the **Hamiltonian operator**, and it has a deep connection to energy conservation and the Hamiltonian function of classical mechanics.

:::{important} **Classical Hamiltonian:**

$$
H(x,p) = K + V = \frac{p^2}{2m} + V(x)
$$

-  The classical Hamiltonian represents the total energy, showing us how kinetic and potential energy change as a function of momentum and position. 

:::

:::{important} **Quantum Hamiltonian:**

$$
\hat{H} = \hat{K} + \hat{V} = -\frac{\hbar^2}{2m} \frac{\partial^2}{\partial x^2} + V(x)
$$

- The operator $\hat{H}$, known as the Hamiltonian operator, is the quantum mechanical analog of the classical Hamiltonian, which represents the total energy:
:::


:::{important} **Schrödinger Equation in operator form**

$$
\hat{H} \psi = E \psi
$$

$$
\hat{H} \psi = i\hbar \frac{\partial \psi}{\partial t}
$$

- **Hamiltonian Operator**: $\hat{H}$ can stand for 1D, 2D, or 3D systems and describe any quantum object, from a single electron to a collection of molecules.
- **Energy**: Describes the possible energy states of the quantum system.
- **Energy Operator**: $i\hbar \frac{\partial}{\partial t}$
:::

- Note how the potential energy term appears in the same form across different systems: it is always a function of spatial coordinates. Some examples of potentials:
  - $V(x) = 0$ represents a free particle, 
  - $V(x) = kx^2$ describes a particle trapped in a harmonic potential, 
  - $V(x) = \cos(x)$ corresponds to a particle in a periodic potential.


### The correspondence principle of Quantum Mechanics

- Thanks to the universality of the energy conservation law, for every observable in classical mechanics there is a corresponding operator in quantum mechanics! Let us list them here:

|               Observables               |                   Classical                    |                           Quantum                            |
| :-------------------------------------: | :--------------------------------------------: | :----------------------------------------------------------: |
|                Position                 |                      $x$                       |                         $\hat{x}=x$                          |
|                Momentum                 |                     $p=mv$                     |        $\hat{p}=-i\hbar \frac{\partial}{\partial x}$         |
|            Potential Energy             |                     $V(X)$                     |                        $\hat{V}=V(x)$                        |
|             Kinetic Energy              |               $K=\frac{p^2}{2m}$               |                $\hat{K}=\frac{\hat{p}^2}{2m}$                |
|              Total Energy               |          $H(x,p)=\frac{p^2}{2m}+V(x)$          |                  $\hat{H}=\hat{K}+\hat{V}$                   |
|           Equation of motion            | Newton's law $F=ma$ <br>or Hamiltons equations | $\hat{H}\psi=E\psi$ Or <br>$i\hbar\frac{\partial \psi}{\partial t}=\hat{H}\psi$ |
| Quantization and wave-particle duality? |                      N/A                       | Energy quantization and duality are<br> naturally described by $E_n$ and $\psi_n$. |


### What about quantities which correspond to operators?

- Recall that the mean value of $x$ is computed by weighting its values by their probabilities. For example, think of the average mass of a box of candies: we multiply the probability (or fraction) of each candy type by its mass and sum.

$$\langle x \rangle = x_1 p_2+x_2 p_2 + ...$$

$$\langle x \rangle  = \int x\cdot p(x)  dx$$

- Likewise, you can compute the average of any function of $x$, say $x^2$ or $\sin(x)$.

$$\langle f \rangle  = \int f(x)  \cdot  p(x) dx$$

- For quantities like momentum or total energy, which are no longer simple functions as in classical mechanics but operators, $\hat{p}$ and $\hat{H}$, we simply use the operators in the definition of the moments:

$$\langle A \rangle  = \int \hat{A} p(x) \cdot  dx = \int \psi^{*}(x) \cdot \hat{A} \psi(x) \cdot  dx $$


|                       Average quantity                       |               Corresponding operator               |
| :----------------------------------------------------------: | :------------------------------------------------: |
|   $\langle E \rangle=\int \psi^{*}(x) \hat{H} \psi(x)  dx$   | $\hat{H}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x)$ |
|  $\langle K \rangle=\int \psi^{*}(x) \hat{K}\psi(x)  dx  $   |   $\hat{K}=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$    |
|   $\langle p \rangle=\int \psi^{*}(x) \hat{p} \psi(x)  dx$   |           $\hat{p}=-i\hbar\frac{d}{dx}$            |
| $\langle p^2 \rangle=\int \psi^{*}(x) \hat{p}^2 \psi(x)  dx$ |        $\hat{p}^2=-\hbar^2\frac{d^2}{dx^2}$        |

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
from math import erf, sqrt

# ----- Parameters -----
sigma = 1.0  # width of the Gaussian (harmonic oscillator ground state)
x0, x1 = -1.0, 1.0  # interval to integrate over

# ----- Define |psi(x)|^2 for a normalized Gaussian -----
def prob_density(x, sigma):
    # |psi(x)|^2 = (1/(sqrt(2*pi)*sigma)) * exp(-x^2/(2*sigma^2))
    return (1.0/(np.sqrt(2*np.pi)*sigma)) * np.exp(-x**2/(2*sigma**2))

# Probability via the error function (analytic CDF of a normal distribution)
def interval_probability(a, b, sigma):
    return 0.5*(erf(b/(sqrt(2)*sigma)) - erf(a/(sqrt(2)*sigma)))

P = interval_probability(x0, x1, sigma)

# ----- Plot -----
xs = np.linspace(-4*sigma, 4*sigma, 800)
ys = prob_density(xs, sigma)

fig = plt.figure(figsize=(10, 5))

# Title with the integral expression
plt.title(r"$P_{x_0<x<x_1}=\int_{x_0}^{x_1}|\psi(x)|^2\,dx$" + 
          f"\nSelected interval: [{x0:.2f}, {x1:.2f}]",
          loc="left")

# Curve
plt.plot(xs, ys, linewidth=3)

# Shade between x0 and x1 under the curve
mask = (xs >= x0) & (xs <= x1)
plt.fill_between(xs[mask], ys[mask], 0, alpha=0.25)

# Mark the boundaries with vertical dashed lines
plt.axvline(x0, linestyle="--", linewidth=2)
plt.axvline(x1, linestyle="--", linewidth=2)

# Tick marks and labels
plt.xlabel("x")
plt.ylabel(r"$|\psi(x)|^2$")

# Annotate the probability
plt.text(0.02, 0.90, rf"$P_{{{x0:.2f}<x<{x1:.2f}}} = {P:.3f}$",
         transform=plt.gca().transAxes, fontsize=16)

plt.xlim(xs.min(), xs.max())
plt.ylim(bottom=0)
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
```

### Linearity and the Principle of Superposition

- As we recall from solving the classical wave equation, whenever boundary conditions are imposed on the spatial domain of our PDE we can end up with an infinite number of solutions $u_n(x)$ discretized by integers $n=1,2,...$ for each spatial coordinate. 

- The general solution was written as a linear combination of normal modes. Likewise, boundary conditions produce an infinite number of solutions to the quantum wave equation discretized by integers $n$: $\hat{H} \psi_n(x)=E_n \psi_n(x)$

- **The general solution** is again written as a linear combination of quantum wave functions, **thanks to the linearity of the Schrödinger equation**:

$$\psi(x,t) = \sum_n c_n \psi_n(x) f_n(t)$$


### Eigenvalues and Eigenfunctions

- In both the classical wave equation and the time-independent Schrödinger equation, we can use operator notation to frame the problem as one of finding special functions and their corresponding multiplicative factors that satisfy specific operators.

:::{figure} images/SE_intro6.jpg
:label: fig-schrodinger-equation-5
:alt: eigval-func
:width: 300px

Eigenvalue/Eigenfunction problem
:::

- In general, the action of an operator can change a function, but in quantum mechanics, we are particularly interested in operators that preserve the form of the function, producing only a constant multiplicative factor.

- The time-independent Schrödinger equation can be viewed as an **eigenfunction-eigenvalue problem.**

:::{important} **Schrödinger Equation as an Eigenfunction/Eigenvalue problem**

$$
\boxed{\hat{H} \psi_n = E_n \psi_n}
$$

- $\psi_n$, the wave functions, are the eigenfunctions of the Hamiltonian operator. 
- $E_n$, the energies, are the eigenvalues of the Hamiltonian operator.

:::


### Examples of using probabilistic calculations in QM

#### Example 1: Probability in a region (1D)

Take the normalized wavefunction on $[0,1]$: $\psi(x)=\sqrt{3}\,x$. Then $p(x)=|\psi(x)|^2=3x^2$.

* Probability that the particle lies in $[a,b]\subset[0,1]$:

$$
P(a<x<b)=\int_a^b 3x^2\,dx= \left[x^3\right]_a^b=b^3-a^3.
$$

* Concrete numbers, say $[0.3,0.6]$:

$$
P(0.3<x<0.6)=0.6^3-0.3^3=0.216-0.027=0.189.
$$



#### Example 2: 3D slice probability (separable state)

Let $\psi(x,y,z)=\sqrt{27}\,xyz$ on the unit cube $[0,1]^3$ (this is normalized since $|\psi|^2=27x^2y^2z^2$ and $\int_0^1 x^2dx=\tfrac13$, so $27(\tfrac13)^3=1$).

* Probability the particle is inside the rectangular box $[a_x,b_x]\times[a_y,b_y]\times[a_z,b_z]$:

$$
P=\int_{a_x}^{b_x}\!\!\int_{a_y}^{b_y}\!\!\int_{a_z}^{b_z}27x^2y^2z^2\,dz\,dy\,dx
= \big(b_x^3-a_x^3\big)\big(b_y^3-a_y^3\big)\big(b_z^3-a_z^3\big).
$$



#### Example 3: Averages and variance from a PDF

For $\psi(x)=\sqrt{3}\,x$ on $[0,1]$ (so $p(x)=3x^2$):

* Mean position:

$$
\langle x\rangle=\int_0^1 x\,3x^2\,dx=3\int_0^1 x^3dx=\tfrac34.
$$

* Mean square position:

$$
\langle x^2\rangle=\int_0^1 x^2\,3x^2\,dx=3\int_0^1 x^4dx=\tfrac35.
$$

* Variance and standard deviation:

$$
\mathrm{Var}(x)=\langle x^2\rangle-\langle x\rangle^2=\tfrac35-\Big(\tfrac34\Big)^2=\tfrac{3}{80},\qquad
\sigma_x=\sqrt{\tfrac{3}{80}}\approx 0.1937.
$$


#### Example 4: Operator expectations (momentum/energy in a box)

Operator rules:

* $ \hat{p}=-i\hbar\,\dfrac{d}{dx}$,
* $ \hat{H}=-\dfrac{\hbar^2}{2m}\dfrac{d^2}{dx^2}+V(x)$.

Use the infinite square well on $[0,1]$ with $V(x)=0$ inside and $\psi_n(x)=\sqrt{2}\sin(n\pi x)$, which is normalized.

* Momentum expectation:

$$
\langle p\rangle=\int_0^1\psi_n^*(-i\hbar)\psi_n'\,dx=0
$$

(the integrand is odd over a full sine half-wave, or integrate by parts with vanishing boundary terms).

* Momentum squared:

$$
\langle p^2\rangle=\int_0^1\psi_n^*(-\hbar^2)\psi_n''\,dx
=(n\pi\hbar)^2.
$$

* Energy (since $\hat{H}=\hat{p}^2/2m$ inside the well):

$$
\langle E\rangle=\frac{\langle p^2\rangle}{2m}=\frac{(n\pi\hbar)^2}{2m}.
$$


### Problems

#### Problem 1

Confirm that the following wavefunctions are eigenfunctions of linear momentum and kinetic energy (or neither or both):

- $C sin(ax)$

- $N e^{-ix/\hbar}$

:::{admonition} **Solution**
:class: dropdown solution

Start by applying the linear momentum operator to the first function:

$$-i \hbar \dfrac{\partial}{\partial x} A \sin(ax) = -i \hbar Aa \cos(ax) \nonumber$$

- We see that the action of the operator changed the $\sin$ function, hence the $\sin$ function cannot be an eigenfunction of linear momentum. 

Next we apply the kinetic energy operator:

$$
\begin{align*} -\dfrac{\hbar^2}{2m} \dfrac{\partial^2}{\partial x^2} A \sin(ax) &= -\dfrac{\hbar^2}{2m} \dfrac{\partial}{\partial x} Aa \cos(ax) \\[4pt] &= +\dfrac{\hbar^2}{2m} Aa^2 \sin(ax) \end{align*}  \nonumber
$$

- The kinetic energy operator did not modify the function, hence the $\sin$ function is an eigenfunction of the kinetic energy operator.
:::


#### Problem 2: Taking the Square of an Operator

Consider the operator $ \hat{A} = x \frac{d}{dx} $. Find $ \hat{A}^2 $, i.e., $ \hat{A}(\hat{A}f(x)) $, and apply it to an arbitrary function $ f(x) $.

:::{admonition} **Solution**
:class: dropdown solution

First, apply $ \hat{A} f(x) = x \frac{d}{dx} f(x) $:

$$
\hat{A} f(x) = x \frac{df}{dx}
$$

Now, apply $ \hat{A} $ again to the result:

$$
\hat{A}(\hat{A} f(x)) = \hat{A} \left( x \frac{df}{dx} \right) = x \frac{d}{dx} \left( x \frac{df}{dx} \right)
$$

Using the product rule:

$$
\frac{d}{dx} \left( x \frac{df}{dx} \right) = \frac{df}{dx} + x \frac{d^2 f}{dx^2}
$$

Thus:

$$
\hat{A}^2 f(x) = x \left( \frac{df}{dx} + x \frac{d^2 f}{dx^2} \right) = x \frac{df}{dx} + x^2 \frac{d^2 f}{dx^2}
$$

:::

#### Problem 3: Verifying Eigenfunction and Eigenvalue

Consider the operator $ \hat{B} = -i\hbar \frac{d}{dx} $ (momentum operator). Verify that $ f(x) = e^{ikx} $ is an eigenfunction of $ \hat{B} $, and find the corresponding eigenvalue.

:::{admonition} **Solution**
:class: dropdown solution

Apply $ \hat{B} $ to $ f(x) = e^{ikx} $:

$$
\hat{B} f(x) = -i\hbar \frac{d}{dx} e^{ikx}
$$

The derivative of $ e^{ikx} $ is:

$$
\frac{d}{dx} e^{ikx} = ik e^{ikx}
$$

Thus:

$$
\hat{B} f(x) = -i\hbar \cdot ik e^{ikx} = \hbar k e^{ikx}
$$

Since $ \hat{B} f(x) = \hbar k f(x) $, $ f(x) = e^{ikx} $ is an eigenfunction of $ \hat{B} $ with eigenvalue $ \hbar k $.

:::

#### Problem 4: Testing for an Eigenfunction and Eigenvalue

Given the operator $ \hat{C} = \frac{d^2}{dx^2} $ (second derivative operator), check if $ f(x) = e^{-\alpha x^2} $ is an eigenfunction of $ \hat{C} $, and find the eigenvalue if it is.

:::{admonition} **Solution**
:class: dropdown solution

Apply $\hat{C} = \frac{d^2}{dx^2} $ to $ f(x) = e^{-\alpha x^2} $:

$$
\frac{d}{dx} e^{-\alpha x^2} = -2\alpha x e^{-\alpha x^2}
$$

Taking the second derivative:

$$
\frac{d^2}{dx^2} e^{-\alpha x^2} = \frac{d}{dx} \left( -2\alpha x e^{-\alpha x^2} \right) = -2\alpha e^{-\alpha x^2} + 4\alpha^2 x^2 e^{-\alpha x^2}
$$

Thus:

$$
\hat{C} f(x) = \left( -2\alpha + 4\alpha^2 x^2 \right) e^{-\alpha x^2}
$$

Since this is not proportional to $ f(x) = e^{-\alpha x^2} $, $ f(x) $ is **not** an eigenfunction of $ \hat{C} $.

:::

#### Problem 5: Linearity and Eigenfunction Testing

Consider the operator $ \hat{D} = x^2 \frac{d}{dx} $. Show whether this operator is linear and check if $ f(x) = x^n $ is an eigenfunction of $ \hat{D} $.

:::{admonition} **Solution**
:class: dropdown solution

First, test linearity by applying $ \hat{D} $ to $ \alpha f(x) + \beta g(x) $:

$$
\hat{D}(\alpha f(x) + \beta g(x)) = x^2 \frac{d}{dx} (\alpha f(x) + \beta g(x)) = \alpha x^2 \frac{df}{dx} + \beta x^2 \frac{dg}{dx}
$$

This is $ \alpha \hat{D} f(x) + \beta \hat{D} g(x) $, so $ \hat{D} $ is linear.

Now, apply $ \hat{D} $ to $ f(x) = x^n $:

$$
\hat{D} f(x) = x^2 \frac{d}{dx} x^n = x^2 \cdot n x^{n-1} = n x^n
$$

Since the result is proportional to $ f(x) = x^n $, $ f(x) = x^n $ is an eigenfunction of $ \hat{D} $ with eigenvalue $ n $.

:::

#### Problem 6: Normalize and locate

Normalize $\psi(x) = \cos(\pi x / 2)$ on the interval $[-1, 1]$, then compute the probability of finding the particle in $[0, \tfrac{1}{2}]$.

#### Problem 7: Symmetry does the integrals

For the particle-in-a-box state $\psi_2(x) = \sqrt{2}\sin(2\pi x)$ on $[0, 1]$, evaluate $\langle x \rangle$ and $\langle p \rangle$, and explain both results using symmetry alone.
