

## Wave equation

:::{admonition} What you need to know
:class: note

- **Wave Equation Overview:** The wave equation, a partial differential equation (PDE), fully describes the spatial and temporal evolution of waves.

- **Linearity of the Wave Equation:** The wave equation is linear, meaning that any linear combination of solutions is also a solution. This allows the most general solution to be expressed as a linear combination of all possible solutions.

- **Boundary and Initial Conditions:** To solve the wave equation for a specific physical system, boundary conditions must be specified. These include the values the wave function takes at the physical boundaries (e.g., $x = 0$ and $x = L$). Initial conditions with respect to time (e.g., at $t = 0$) may also be required.

- **Solution Method for 1D Guitar String:** For a 1D guitar string, the wave equation is solved by separating variables, solving the resulting ordinary differential equations, and then applying boundary conditions at the two ends of the string.

- **Periodic Solutions:** The solution for a 1D guitar string results in an infinite number of periodic solutions, which are parameterized by an integer $n$. 

:::

### Classical Wave equation

- **Wave equation** is an example of a second order PDE (partial differential equation). This PDE governs behavior of displacement $u(x,t)$ in time and space.

$$\frac{\partial^2 u(x,t)}{\partial x^2 }= \frac{1}{v^2}\frac{\partial^2 u(x,t)}{\partial t^2}$$ 


:::{figure-md} markdown-fig

<img src="./images/1D-Wave.gif" alt="applied photoelectric" class="bg-primary mb-1" width="50%">

Classical wave equation can describe any complicated wave in space and time given the intitial conditions.
:::

- **Applications of the Classical Wave Equation:** To illustrate the applications of the classical wave equation, we will solve it for a 1D guitar string. This provides a comprehensive mathematical description of the string's behavior.

- **Predicting Evolution:** By specifying arbitrary initial conditions, the wave equation allows us to precisely predict the evolution of the string over time and space.


:::{figure-md} markdown-fig

<img src="./images/lec5_guitar.jpg" alt="applied photoelectric" class="bg-primary mb-1" width="50%">

Classical wave equation can describe any complicated wave in space and time given the intitial conditions.
:::


### Solving Wave Equation: The big picture 

- **Boundary Conditions:** To solve the wave equation for a specific physical situation, such as a guitar string fixed at both ends, we need to specify two boundary conditions. Mathematically, these are:

$$
u(0, t) = 0 \quad \text{and} \quad u(L, t) = 0
$$

where $u(x, t)$ represents the displacement of the string at position $x$ and time $t$.

- **Separation of Variables:** A common method to solve such equations is the technique of separation of variables. This technique assumes that $x$ and $t$ vary independently of each other, allowing us to express $u(x, t)$ as a product of two functions, each depending on only one variable. This allows us to decompose PDE into Ordinary Differnetial Equations ODEs. 

$$
u(x, t) = X(x) \cdot T(t)
$$

- **Principle of superposition:** The wave equation is linear which you can see by  $u$ terms appearing with first order on both side. Linearity means that linear combination of two solutions $c_1 u_1+c_2u_2$ is also a solution. If you have $n$ particular solutions than you write general solution as linear combination of n terms. 

### Step 1: Plug the Product of Univariate Functions into the Wave Equation

- Start with the 1D wave equation that can describe 1D guitar string:

$$
\frac{1}{v^2}\frac{\partial^2 u(x,t)}{\partial t^2} = \frac{\partial^2 u(x,t)}{\partial x^2}
$$

- Substitute $u(x, t) = X(x)T(t)$ into the wave equation:

$$
\frac{1}{v^2}\frac{\partial^2 X(x)T(t)}{\partial t^2} = \frac{\partial^2 X(x)T(t)}{\partial x^2}
$$

- After rearranging, we get:

$$
\frac{X(x)}{v^2}\frac{\partial^2 T(t)}{\partial t^2} = T(t)\frac{\partial^2 X(x)}{\partial x^2}
$$

- Thus, we obtain two separate ordinary differential equations (ODEs) from the original partial differential equation (PDE):

$$
\frac{1}{T(t)v^2}\frac{\partial^2 T(t)}{\partial t^2} = \frac{1}{X(x)}\frac{\partial^2 X(x)}{\partial x^2} = K
$$

- where $K$ is a constant.


### Step 2: Solving Each Ordinary Differential Equation

After decomposing the PDE into ODEs, we solve each ODE separately:

$$
\frac{\partial^2 T(t)}{\partial t^2} - K T(t) v^2 = 0
$$

$$
\frac{\partial^2 X(x)}{\partial x^2} - K X(x) = 0
$$

:::{admonition} **Solving the spatial part: when $K > 0$**
:class: tip, dropdown

- If $K > 0$, we specify $K = \beta^2$, where $\beta$ is a constant. The general solution for $X(x)$ is represented as linar combination of particular solutions (principle of superposition):

  $$
  X(x) = c_1 e^{\beta x} + c_2 e^{-\beta x}
  $$

  Applying the boundary conditions $X(0) = X(L) = 0$ leads to $c_1 = c_2 = 0$. Since a non-trivial linear combination of two exponential functions cannot be zero everywhere, this results in the trivial solution:

  $$
  X(x) = 0
  $$

  This implies that the string does not move—no music!

:::

:::{admonition} **Solving the spatial part: when $K < 0$**
:class: tip, dropdown

- If $K < 0$, we specify $K = -\beta^2$, where $\beta$ is a constant. The general solution for $X(x)$ is:

  $$
  X(x) = c_1 e^{i \beta x} + c_2 e^{-i \beta x}
  $$

  Using Euler's formula, this can be rewritten as:

  $$
  X(x) = c_1 (\cos(\beta x) + i \sin(\beta x)) + c_2 (\cos(\beta x) - i \sin(\beta x))
  $$

  Simplifying further:

  $$
  X(x) = (c_1 + i c_2) \cos(\beta x) + (c_1 - i c_2) \sin(\beta x)
  $$

  Let $A = c_1 + i c_2$ and $B = c_1 - i c_2$:

  $$
  X(x) = A \cos(\beta x) + B \sin(\beta x)
  $$

  Applying the boundary conditions $X(0) = 0$ and $X(L) = 0$:

  - At $x = 0$: $A \cdot 1 + B \cdot 0 = 0$, so $A = 0$.
  - At $x = L$: $X(L) = B \sin(\beta L) = 0$.

  For a non-trivial solution, $\sin(\beta L) = 0$, which implies:

  $$
  \beta L = n \pi \quad \text{where} \quad n = 1, 2, 3, \ldots
  $$

  Hence:

  $$
  \beta = \frac{n \pi}{L}
  $$

  Thus:

  $$
  X(x) = B \sin \left(\frac{n \pi}{L} x \right)
  $$

:::


:::{admonition} **Solving temporal part**
:class: tip, dropdown


- Having identified $K<0$ conditions through solution of spatial part we can now solve for $T(t)$:

$$
\frac{\partial^2 T(t)}{\partial t^2} - K v^2 T(t) = 0 \quad \text{with} \quad K = \beta^2
$$

- Substitute $K = \beta^2$:

$$
\frac{\partial^2 T(t)}{\partial t^2} - \beta^2 v^2 T(t) = 0
$$

- The solution is:

$$
T(t) = D_n \cos(\omega_n t) + E_n \sin(\omega_n t)
$$

- where $\omega_n = \beta v = \frac{n \pi v}{L}$.
:::


- For spatial part we find solution in the form of sine wave. Where n takes on integer values.

$$
X(x) = B \sin \left(\frac{n \pi}{L} x \right)
$$

:::{figure-md} markdown-fig

<img src="./images/modes-x.png" alt="applied photoelectric" class="bg-primary mb-1" width="30%">

The first seven solutions of spatial part of the wave equation on a length $L$ with two amplitudes (one positive and one negative).
:::


- For temporal part since we do not have boundary conditions we find solution in the form of linear combination of sine and cosine functions with $\omega_n = \beta v = \frac{n \pi v}{L}$ and $n = 1, 2, 3, \ldots$ represents the normal modes.

$$
T(t) = D_n \cos(\omega_n t) + E_n \sin(\omega_n t)
$$

### Step 3: Combine the Solutions of All ODEs to Obtain the Solution of the Original PDE

- After solving ODEs for spatial adn tempoeral parts we now combine them to obtain the full solution:

$$
u(x, t) = X(x) T(t) = [D_n \cos(\omega_n t) + E_n \sin(\omega_n t)] \cdot B \sin \left(\frac{n \pi}{L} x \right)
$$

- Using trig identities, we express the general solution as:

$$
u(x, t) = A \sin \left(\frac{n \pi}{L} x \right) \cos (\omega_n t + \phi_n)
$$

- where $A$ and $\phi_n$ are constants which one specifies as part of inititial conditions.

- **The general solution to wave equation is a linear combination of all normal modes**:

$$
u(x, t) = \sum_n A_n \sin \left(\frac{n \pi}{L} x \right) \cdot \cos (\omega_n t + \phi_n)
$$

- This general solution describes the time evolution of any 1D guitar string given initital position and velocity encoded by $A$ and $\phi_n$ constants



### Interpretation of Solution to the Wave Equation

:::{figure-md} markdown-fig

<img src="./images/Standing_waves_on_a_string.gif" alt="applied photoelectric" class="bg-primary mb-1" width="50%">

Presented are first six solutions from $n=0,1,2,3,4,5$
:::


- The complete description of any vibrational motion of the guitar string is given by the sum of the normal modes, $X_n(x)$. While the terms involving time, $T_n(t)$, depend on how and where the string is plucked, the normal modes $X_n(x)$ remain the same for a given string.

  $$
  \nu_n = \frac{\omega_n}{2 \pi} = \frac{n \nu}{2L}
  $$

  where $\nu_n$ is the frequency of the $n$-th mode, $\omega_n$ is the angular frequency, $n$ is the mode number, $\nu$ is the wave speed, and $L$ is the length of the string.

- **For $n = 1$**: There are 0 nodes (excluding the endpoints). This is called the fundamental frequency or first harmonic.

- **For $n = 2$**: There is 1 node. This is known as the first overtone or second harmonic.

- **For $n = 3$**: There are 2 nodes. This is called the second overtone or third harmonic.


### 2D membrane vibrations.

:::{figure-md} markdown-fig

<img src="http://giphygifs.s3.amazonaws.com/media/10qqg7K1HIv2OQ/giphy.gif" alt="applied photoelectric" class="bg-primary mb-1" width="50%">

Vibrations of 2D membrane. 
:::


- Wave function of 2D membrane with fixed edges has two independent variables x and y. Applying the technique of separation of variables we will get three ordinary differential equations.

$$u(x,y,t) =X(x)Y(y)T(t)$$

- This time there will be two boundary conditions fo X and Y
- Boundary on the $X$ edge: $X(0)=X(L)=0$.
- Boundary on the $Y$ edge: $Y(0)=Y(L)=0$.

- Going through exactly the same steps as in 1D case we get full solution expressed as a linear combination of normal modes. 
- The 2D solution is essentially a product of two 1D solutions for each coordinate. Each coordinate has its own independent wave number $k_x$ and $k_y$. 

$$ u(x,y,t) = A_{nm} cos(\omega_{nm}t+\phi_{nm}) sin \frac{n\pi x}{a} sin \frac{m\pi y}{b} $$

- The angular frequency depends on the geometry of the domain and on two integer numbers $n$ and $m$. 

$$\omega_{nm} = v\pi \Big(\frac{n^2}{a^2}+ \frac{m^2}{b^2}\Big)^{1/2} $$

- Can you guess what the solution would be fore the 3D case?


### The sound of music.

 - Music produced by musical instruments is a combination of sound waves with frequencies corresponding to a superposition of normal modes (in music they call harmonics, overtones) of those musical instruments. 
- Learn more from [this series](https://www.youtube.com/watch?v=jveKIYyafaQ).

:::{figure-md} markdown-fig

<img src="./images/lec4_music.jpg" class="bg-primary mb-1" width="40%">

The size of the musical instrument reflects the range of frequencies over which the instrument is designed to function. Smaller size implies higher frequencies, larger size implies lower frequencies.
:::


### Example Problems 

#### Problem 1: Simple Harmonic Oscillator

**Problem:**

Solve the ODE:

$$
\frac{d^2 y}{dt^2} + \omega^2 y = 0
$$

where $\omega$ is a constant.

:::{admonition} **Solution:**
:class: dropdown

The characteristic equation is:

$$
r^2 + \omega^2 = 0
$$

Solving for $r$:

$$
r = \pm i \omega
$$

Thus, the general solution is:

$$
y(t) = C_1 \cos(\omega t) + C_2 \sin(\omega t)
$$

where $C_1$ and $C_2$ are constants determined by initial conditions.

:::

#### Problem 2: Damped Oscillator

Solve the ODE:

$$
\frac{d^2 y}{dt^2} + 2 \beta \frac{dy}{dt} + \omega^2 y = 0
$$

where $\beta$ and $\omega$ are constants. Consider cases of $\beta^2 < \omega^2$, $\beta^2 > \omega^2$ and $\beta^2 = \omega^2$

:::{admonittion} **Solution:**
:class: dropdown

The characteristic equation is:

$$
r^2 + 2 \beta r + \omega^2 = 0
$$

Solving for $r$ using the quadratic formula:

$$
r = \frac{-2 \beta \pm \sqrt{(2 \beta)^2 - 4 \omega^2}}{2}
$$

$$
r = -\beta \pm \sqrt{\beta^2 - \omega^2}
$$

Depending on the discriminant $\beta^2 - \omega^2$, we have three cases:

1. **Underdamping ($\beta^2 < \omega^2$):**

   $$ 
   y(t) = e^{-\beta t} [C_1 \cos(\omega_d t) + C_2 \sin(\omega_d t)]
   $$

   where $\omega_d = \sqrt{\omega^2 - \beta^2}$.

2. **Critical Damping ($\beta^2 = \omega^2$):**

   $$
   y(t) = (C_1 + C_2 t) e^{-\beta t}
   $$

3. **Overdamping ($\beta^2 > \omega^2$):**

   $$
   y(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}
   $$

   where $r_1$ and $r_2$ are the distinct real roots found from the quadratic formula.
:::


### Problem 3: ODE with Constant Coefficients


Solve the ODE:

$$
\frac{d^2 y}{dt^2} - 4 y = 0
$$

:::{admonition} **Solution:**
:class: dropdown

The characteristic equation for this ODE is:

$$
r^2 - 4 = 0
$$

Solving for $r$:

$$
r^2 = 4
$$

$$
r = \pm 2
$$

Thus, the general solution is:

$$
y(t) = C_1 e^{2t} + C_2 e^{-2t}
$$

where $C_1$ and $C_2$ are constants determined by initial conditions.

:::

### Problem 4: Simple 2nd order ODE

Solve the ODE:

$$
\frac{d^2 y}{dt^2} + 9 y = 0
$$

:::{admonition} **Solution:**
:class: dropdown

The characteristic equation for this ODE is:

$$
r^2 + 9 = 0
$$

Solving for $r$:

$$
r^2 = -9
$$

$$
r = \pm 3i
$$

Thus, the general solution is:

$$
y(t) = C_1 \cos(3t) + C_2 \sin(3t)
$$

where $C_1$ and $C_2$ are constants determined by initial conditions.

:::


### Problem 5: Homogeneous Linear ODE 

Solve the ODE:

$$
\frac{d^2 y}{dt^2} - 6 \frac{dy}{dt} + 9 y = 0
$$

:::{admonition} **Solution:**
:class: dropdown

The characteristic equation for this ODE is:

$$
r^2 - 6r + 9 = 0
$$

Factoring:

$$
(r - 3)^2 = 0
$$

Thus:

$$
r = 3 \text{ (repeated root)}
$$

The general solution for repeated roots is:

$$
y(t) = (C_1 + C_2 t) e^{3t}
$$

where $C_1$ and $C_2$ are constants determined by initial conditions.
:::
