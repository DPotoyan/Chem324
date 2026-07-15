# The Schrödinger Equation


:::{note} **What you need to know**

- By combining the classical wave equation with quantum principles, we derive a new equation that describes quantum wave functions: **Schrödinger's Equation (SE)**.
  
- Schrödinger's Equation, like the classical wave equation, depends on both time and space.
  
- We can apply the method of **separation of variables** to transform the time-dependent Schrödinger equation (TD-SE) into the time-independent Schrödinger equation (TI-SE). The time-independent form is especially important in the chemical and biological sciences, and it will be our primary focus for the remainder of the course.
  
- We will introduce the **operator notation**, a powerful mathematical framework that allows us to express the equations of quantum mechanics in a concise and elegant form.
  
- In quantum mechanics, every physical quantity that can be measured experimentally (such as energy, momentum, or position) has a corresponding **operator**.
  
- We will reformulate the process of solving Schrödinger's equation into finding the **eigenfunctions** and **eigenvalues** associated with these operators, which represent measurable quantities in quantum systems.

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