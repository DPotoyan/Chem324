---
kernelspec:
  name: python3
  display_name: Python 3
---

# Wave equation

:::{note} **What you will learn**

- **Wave Equation Overview:** The wave equation, a partial differential equation (PDE), fully describes the spatial and temporal evolution of waves.

- **Linearity of the Wave Equation:** The wave equation is linear, meaning that any linear combination of solutions is also a solution. This allows the most general solution to be expressed as a linear combination of all possible solutions.

- **Boundary and Initial Conditions:** To solve the wave equation for a specific physical system, boundary conditions must be specified. These include the values the wave function takes at the physical boundaries (e.g., $x = 0$ and $x = L$). Initial conditions with respect to time (e.g., at $t = 0$) may also be required.

- **Solution Method for 1D Guitar String:** For a 1D guitar string, the wave equation is solved by separating variables, solving the resulting ordinary differential equations, and then applying boundary conditions at the two ends of the string.

- **Periodic Solutions:** The solution for a 1D guitar string yields an infinite number of periodic solutions, parameterized by an integer $n$. 

:::

### Classical Wave equation

- The **wave equation** is an example of a second-order PDE (partial differential equation). This PDE governs the behavior of the displacement $u(x,t)$ in time and space.

$$
\frac{\partial^2 u(x,t)}{\partial x^2 }= \frac{1}{v^2}\frac{\partial^2 u(x,t)}{\partial t^2}$$ 


:::{figure} ./images/1D-Wave.gif
:label: fig-the-wave-equation-1
:alt: applied photoelectric
:width: 50%

The classical wave equation describes any complicated wave in space and time, given the initial conditions.
:::

- **Applications of the Classical Wave Equation:** To illustrate the applications of the classical wave equation, we will solve it for a 1D guitar string. This provides a comprehensive mathematical description of the string's behavior.

- **Predicting Evolution:** By specifying arbitrary initial conditions, the wave equation allows us to precisely predict the evolution of the string over time and space.


:::{figure} ./images/lec5_guitar.jpg
:label: fig-the-wave-equation-2
:alt: applied photoelectric
:width: 50%

A plucked guitar string is a classic system governed by the 1D wave equation.
:::

### Solving Wave Equation: The big picture 

- **1. Boundary Conditions:** To solve the wave equation for a specific physical situation, such as a guitar string fixed at both ends, we need to specify two boundary conditions. Mathematically, these are:

$$
u(0, t) = 0 \quad \text{and} \quad u(L, t) = 0
$$


- where $u(x, t)$ represents the displacement of the string at position $x$ and time $t$.

- **2. Separation of Variables:** A common method to solve such equations is the technique of separation of variables. This technique assumes that $x$ and $t$ vary independently of each other, allowing us to express $u(x, t)$ as a product of two functions, each depending on only one variable. This lets us decompose the PDE into ordinary differential equations (ODEs). 

$$
u(x, t) = X(x) \cdot T(t)
$$

- **3. Principle of superposition:** The wave equation is linear, which you can see from the $u$ terms appearing to first order on both sides. Linearity means that a linear combination of two solutions $u_1$ and $u_2$ is also a solution. If you have $n$ particular solutions, then you write the general solution as a linear combination of those $n$ terms. 

$$
u = c_1 u_1+c_2u_2
$$

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

:::{tip} **Solving simple linear and homogeneous ODEs**

**Going from ODE to algebraic equations**

- To solve **linear** (no powers of $y$) and **homogeneous** (no constants, right-hand side is zero) ODEs, we plug in an exponential function, e.g. $y(x) \rightarrow e^{kx}$.
- This turns the ODE into a simple algebraic equation in which the only variable is $k$.
- In our case of the second-order wave equation, we will be dealing with simple quadratic equations: 

$$a y^{''} + by^{'} + cy = 0$$

$$ak^2 + bk + c = 0,$$

The solutions of which are given as:

$$
k_{1,2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
$$

- The most general solution is then written as a linear combination. We need extra information to determine $c_1$ and $c_2$ (e.g. boundary or initial conditions).

$$y = c_1e^{k_1}+c_2 e^{k_2}$$

**Example ODE**

$$
\frac{d^2 y}{dx^2} +4y = 0
$$

- For instance, if we plug $y=e^{kx}$ into the following equation and cancel the exponentials on both sides, we get an algebraic equation in terms of $k$. 

$$
k^2 +4 = 0
$$

- We get two solutions (which could be complex, real, or repeated), which we then use to write the general solution in the form of a superposition. 

$$
k=\pm 2i
$$

$$
y=c_1e^{+2i} + c_2e^{-2i}
$$

:::

:::{tip} **Solving the spatial part: when $K > 0$**
:class: dropdown

- If $K > 0$, we specify $K = \beta^2$, where $\beta$ is a constant. The general solution for $X(x)$ is represented as a linear combination of particular solutions (principle of superposition):

  $$
  X(x) = c_1 e^{\beta x} + c_2 e^{-\beta x}
  $$

  Applying the boundary conditions $X(0) = X(L) = 0$ leads to $c_1 = c_2 = 0$. Since a non-trivial linear combination of two exponential functions cannot be zero everywhere, this results in the trivial solution:

  $$
  X(x) = 0
  $$

  This implies that the string does not move, so there is no music!

:::

:::{tip} **Solving the spatial part: when $K < 0$**
:class: dropdown

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

  $$
  X(x) = B \sin \left(\frac{n \pi}{L} x \right)
  $$

:::


:::{tip} **Solving temporal part**
:class: dropdown


- Having identified the $K<0$ condition through the solution of the spatial part, we can now solve for $T(t)$:

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


$$\omega_n = \beta v = \frac{n \pi v}{L}$$

:::

#### Solution for spatial part

- Because of the boundary conditions ($X(x)=X(L)=0$) imposed at the ends of the guitar string, we found an infinite number of solutions indexed by an integer $n$. These terms are called **normal modes** and are visualized below. 

$$
X(x) = B \sin \left(\frac{n \pi}{L} x \right)
$$

:::{figure} ./images/modes-x.png
:label: fig-the-wave-equation-3
:alt: applied photoelectric
:width: 30%

The first seven solutions (normal modes) of the spatial part of the wave equation on a string of length $L$, shown at positive and negative amplitude.
:::

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0
B = 1.0
ns = [1, 2, 3, 4]
x = np.linspace(0, L, 800)

# 2x2 subplot
fig, axes = plt.subplots(2, 2, figsize=(8, 6))

for ax, n in zip(axes.ravel(), ns):
    Xn = B * np.sin(n * np.pi * x / L)
    ax.plot(x, Xn, color="C0")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title(f"n = {n}")
    ax.set_xlabel("x")
    ax.set_ylabel("X(x)")
    ax.set_xlim(0, L)

fig.suptitle("Normal modes of a fixed–fixed string")
fig.tight_layout(rect=[0, 0, 1, 0.96])
```

#### Solution for temporal part

- For the temporal part, we do not have boundary conditions! Time is allowed to march forward into infinity. We find the solution in the form of a linear combination of sine and cosine functions with $\omega_n = \beta v = \frac{n \pi v}{L}$, where $n = 1, 2, 3, \ldots$ indexes the normal modes. 


$$
T(t) = D_n \cos(\omega_n t) + E_n \sin(\omega_n t) = A_n \cos (\omega_n t + \phi_n)
$$

- In the second line we use a trig identity to express the sum of cosine and sine in terms of a single cosine. We still have two constants to determine.
- The constants $A_n$ and $\phi_n$ in the temporal part are determined by **initial conditions**, e.g. what the amplitude and phase of the wave should be at the starting time $t=0$.

### Step 3 Full solution: A linear combination of normal modes

- After solving the ODEs for the spatial and temporal parts, we now combine them into a full solution. 
- The complete description of any vibrational motion of the guitar string is given by the sum of the normal modes, $X_n(x)$. 
- While the terms involving time, $T_n(t)$, depend on how and where the string is plucked, the normal modes $X_n(x)$ remain the same for a given string.

:::{important}

$$
u(x, t) = \sum_n X_n(x) T_n(t)
$$

$$
u(x, t) = \sum_n A_n \sin \left(\frac{n \pi}{L} x \right) \cdot \cos (\omega_n t + \phi_n)
$$

- $x$ spatial profile of wave bounded in region $[0, L]$
- $t$ time variable is free $(0, \infty$)
- $n=0,1,2,$ index of normal mode
- $A_n$ and $\phi_n$ coefficients specified as part of initial conditions
:::


#### About nodes 

Places where the guitar string stays at the resting position of 0 are called **nodes.** We notice that the number of nodal points increases with $n$. 

- **For $n = 1$**: There are 0 nodes (excluding the endpoints). This is called the fundamental frequency or first harmonic.

- **For $n = 2$**: There is 1 node. This is known as the first overtone or second harmonic.

- **For $n = 3$**: There are 2 nodes. This is called the second overtone or third harmonic.

- Note that the general solution to wave equation is expressed as **a linear combination of all normal modes**  

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Parameters (reduced frames for faster export)
L = 1.0
v = 1.0
B = 1.0
A = {1: 1.0, 2: 1.0, 3: 1.0}
phi = {1: 0.0, 2: 0.0, 3: 0.0}

x = np.linspace(0, L, 600)

def X(n, x):
    return np.sin(n * np.pi * x / L)

def T(n, t):
    omega_n = n * np.pi * v / L
    return np.cos(omega_n * t + phi[n])

def u_mode(n, x, t):
    return B * X(n, x) * T(n, t)

def u_sum(modes, x, t):
    s = np.zeros_like(x)
    for n in modes:
        s += A[n] * X(n, x) * T(n, t)
    return s

omega1 = np.pi * v / L
T1 = 2 * np.pi / omega1
tmax = 2 * T1
frames = 120  # fewer frames
ts = np.linspace(0, tmax, frames)

fig, axes = plt.subplots(2, 2, figsize=(8, 6))
axes = axes.ravel()
titles = ["n = 1", "n = 3", "n = 1 + 2", "n = 1 + 2 + 3"]
lines = []
for ax, title in zip(axes, titles):
    ax.set_xlim(0, L)
    ax.set_ylim(-1.6, 1.6)
    ax.set_xlabel("x")
    ax.set_ylabel("u(x,t)")
    ax.set_title(title)
    ax.axhline(0, linewidth=0.8)
    line, = ax.plot([], [])
    lines.append(line)

fig.suptitle("Standing waves on a fixed–fixed string")

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def update(idx):
    t = ts[idx]
    lines[0].set_data(x, u_mode(1, x, t))
    lines[1].set_data(x, u_mode(3, x, t))
    lines[2].set_data(x, u_sum([1, 2], x, t))
    lines[3].set_data(x, u_sum([1, 2, 3], x, t))
    return lines

ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=1000*(tmax/frames))

plt.close(fig)  # Prevents static display of the last frame
HTML(ani.to_jshtml())
```

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
      "plotly",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
import plotly.graph_objects as go
```

```{marimo} python
:hide-code: true

n_mode = mo.ui.slider(1, 10, step=1, value=2, show_value=True, label="mode n")
t_gtr = mo.ui.slider(0, 10.0, step=0.1, value=0.0, show_value=True, label="time t")
mo.hstack([n_mode, t_gtr], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

x_gtr = np.linspace(0, 1, 1000)
y_gtr = np.sin(n_mode.value * np.pi * x_gtr) * np.cos(np.pi * t_gtr.value)
fig_gtr, ax_gtr = plt.subplots(figsize=(7, 3))
ax_gtr.plot(x_gtr, y_gtr, lw=3)
ax_gtr.set_ylim(-1, 1)
ax_gtr.grid(True, ls="--", alpha=0.5)
ax_gtr.set_xlabel("position along string x")
ax_gtr.set_ylabel("displacement")
ax_gtr.set_title(f"normal mode n = {n_mode.value}", fontsize=11)
fig_gtr
```

### 2D Membrane Vibrations

- The wave function of a 2D membrane with fixed edges depends on two independent spatial variables, $x$ and $y$. By applying the method of separation of variables, we decompose the wave function into three ordinary differential equations.

$$
u(x, y, t) = X(x) Y(y) T(t)
$$

- For the spatial components $X(x)$ and $Y(y)$, there are boundary conditions that must be satisfied at the fixed edges: Boundary condition along the $X$-axis: $X(0) = X(L) = 0$ and Boundary condition along the $Y$-axis: $Y(0) = Y(L) = 0$
- The 2D normal mode is the product of two 1D modes. Since the dimensions are independent, we get integers $n$ for the $x$-direction and $m$ for the $y$-direction:

$$
u(x, y, t) = \sum_n \sum_m A_{nm} \cos(\omega_{nm}t + \phi_{nm}) \sin\left(\frac{n\pi x}{a}\right) \sin\left(\frac{m\pi y}{b}\right)
$$

- The angular frequency $\omega_{nm}$ depends on the geometry of the membrane (with dimensions $a$ and $b$) and the mode numbers $n$ and $m$:

$$
\omega_{nm} = v\pi \left(\frac{n^2}{a^2} + \frac{m^2}{b^2}\right)^{1/2}
$$

Where:
- $v$ is the wave speed,
- $n$ and $m$ are the mode numbers,
- $a$ and $b$ are the dimensions of the membrane.



:::{figure} ./images/2dmemvib.gif
:label: fig-the-wave-equation-4
:alt: membrane vibrations
:width: 50%

Vibrations of a 2D membrane.
:::


:::{tip} **Full derivation of 2D rectangular membrane problem**
:class: dropdown

To extend the solution of the 1D guitar string problem to 2D, you can analyze a 2D vibrating membrane, such as a rectangular or circular drumhead. Here is a step-by-step solution for a 2D rectangular membrane:



**Solution for a 2D Rectangular Membrane**


Consider a rectangular membrane with dimensions $L_x$ and $L_y$, fixed along its edges. The wave equation for the membrane is:

$$
\frac{\partial^2 u(x, y, t)}{\partial t^2} = c^2 \left( \frac{\partial^2 u(x, y, t)}{\partial x^2} + \frac{\partial^2 u(x, y, t)}{\partial y^2} \right)
$$

where $c$ is the wave speed.

**Separation of Variables**

Assume the solution can be written as a product of functions, each depending on only one variable:

$$
u(x, y, t) = X(x) Y(y) T(t)
$$

Substitute this into the wave equation:

$$
\frac{d^2}{dt^2}[X(x) Y(y) T(t)] = c^2 \left( \frac{d^2}{dx^2}[X(x) Y(y) T(t)] + \frac{d^2}{dy^2}[X(x) Y(y) T(t)] \right)
$$

This simplifies to:

$$
X(x) Y(y) \frac{d^2 T(t)}{dt^2} = c^2 \left( T(t) \frac{d^2 X(x)}{dx^2} Y(y) + T(t) X(x) \frac{d^2 Y(y)}{dy^2} \right)
$$

Divide through by $X(x) Y(y) T(t)$:

$$
\frac{1}{c^2} \frac{1}{T(t)} \frac{d^2 T(t)}{dt^2} = \frac{1}{X(x)} \frac{d^2 X(x)}{dx^2} + \frac{1}{Y(y)} \frac{d^2 Y(y)}{dy^2}
$$

Since the left side depends only on  $t$ and the right side depends only on  $x$ and $y$, each side must equal a constant, which we denote as $-\lambda$:

$$
\frac{1}{c^2} \frac{d^2 T(t)}{dt^2} = -\lambda
$$

$$
\frac{d^2 X(x)}{dx^2} + \frac{d^2 Y(y)}{dy^2} = -\lambda X(x)
$$

**Solving for $T(t)$**

The ODE for $T(t)$ is:

$$
\frac{d^2 T(t)}{dt^2} + \lambda c^2 T(t) = 0
$$

This has the general solution:

$$
T(t) = A \cos(\omega t) + B \sin(\omega t)
$$

where $(\omega = \sqrt{\lambda} c)$.

**Solving for $X$ and $Y$**

To solve the spatial part, we need to separate the problem into two parts:

$$
\frac{d^2 X(x)}{dx^2} + \frac{d^2 Y(y)}{dy^2} = -\lambda X(x)
$$

Assume:

$$
\frac{d^2 X(x)}{dx^2} = -\alpha^2 X(x)
$$

$$
\frac{d^2 Y(y)}{dy^2} = -(\lambda - \alpha^2) Y(y)
$$

where $(\lambda = \alpha^2 + \beta^2)$. 

So, we have:

$$
\frac{d^2 X(x)}{dx^2} + \alpha^2 X(x) = 0
$$

$$
\frac{d^2 Y(y)}{dy^2} + \beta^2 Y(y) = 0
$$

**Boundary Conditions:**

For a rectangular membrane with boundaries $x = 0$, $x = L_x$, $y = 0$, and $y = L_y$, we apply:

$$
X(0) = X(L_x) = 0
$$

$$
Y(0) = Y(L_y) = 0
$$

The solutions for $X(x)$ and $Y(y)$ are:

$$
X(x) = C \sin\left(\frac{n \pi x}{L_x}\right)
$$

$$
Y(y) = D \sin\left(\frac{m \pi y}{L_y}\right)
$$

where $n$ and $m$ are positive integers, and:

$$
\alpha = \frac{n \pi}{L_x}, \quad \beta = \frac{m \pi}{L_y}
$$

So, the general solution for $u(x, y, t)$ is:

$$
u(x, y, t) = \sum_{n=1}^\infty \sum_{m=1}^\infty \left[ A_{nm} \cos\left(\omega_{nm} t\right) + B_{nm} \sin\left(\omega_{nm} t\right) \right] \sin\left(\frac{n \pi x}{L_x}\right) \sin\left(\frac{m \pi y}{L_y}\right)
$$

where:

$$
\omega_{nm} = c \sqrt{\left(\frac{n \pi}{L_x}\right)^2 + \left(\frac{m \pi}{L_y}\right)^2}
$$

This solution describes the vibration modes of a 2D rectangular membrane, with each mode characterized by different integer values of $n$ and $m$.
:::

```{code-cell} python
:tags: [hide-input]
import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def membrane2d_mode(n=1, m=1, t=0):
    """
    Calculates the 2D grid of points (X, Y) and the normal mode displacement (Z) of a vibrating 
    rectangular membrane at a specific time t.

    Parameters:
    n (int): Mode number along the x-direction. Default is 1.
    m (int): Mode number along the y-direction. Default is 1.
    t (float): Time at which to evaluate the normal mode. Default is 0.

    Returns:
    X, Y, Z (numpy arrays): Grid of points in the X-Y plane and the corresponding 
                            membrane displacement Z(X, Y, t).
    """
    
    # Constants
    Lx, Ly = 1.0, 1.0  # Dimensions of the rectangular region
    v = 0.1            # Wave speed 
    omega = v * np.pi / Lx * (n**2 + m**2)  # Angular frequency for the normal mode
    
    # Create a spatial grid
    Nx, Ny = 100, 100  # Number of grid points in each dimension
    x, y = np.linspace(0, Lx, Nx), np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y)

    # Compute the spatial part of the normal mode
    Z = np.sin(m * np.pi * X / Lx) * np.sin(n * np.pi * Y / Ly) * np.cos(omega * t)
    
    return X, Y, Z

def viz_membrane2d_plotly(n=1, m=1, t=0): 
    """
    Visualizes the 2D normal modes of a vibrating membrane on a square geometry using Plotly.
    
    This function displays both a 2D contour plot and a 3D surface plot of the membrane displacement.

    Parameters:
    n (int): Mode number along the x-direction. Default is 1.
    m (int): Mode number along the y-direction. Default is 1.
    t (float): Time at which to evaluate the normal mode. Default is 0.
    """
    
    # Get the membrane displacement at time t
    X, Y, Z = membrane2d_mode(n, m, t)
    
    # Create a Plotly subplot with 2 views: 2D contour and 3D surface
    fig = make_subplots(
        rows=1, 
        cols=2, 
        subplot_titles=('2D Contour Plot', '3D Surface Plot'),
        specs=[[{"type": "contour"}, {"type": "surface"}]]
    )
    
    # Add 2D contour plot to the left side
    fig.add_trace(
        go.Contour(x=X.flatten(), y=Y.flatten(), z=Z.flatten(), colorscale='RdBu'),
        row=1, col=1
    )

    # Add 3D surface plot to the right side
    fig.add_trace(
        go.Surface(x=X, y=Y, z=Z, colorscale='RdBu'),
        row=1, col=2
    )

    # Update the layout for better visualization
    fig.update_layout(
        title_text="2D Contour and 3D Surface Plots of Membrane Vibrational Normal Modes",
        width=1000,
        height=500
    )
    
    # Show the figure
    fig.show()

viz_membrane2d_plotly(n=2, m=3, t=0)
```

```{marimo} python
:hide-code: true

n_mem = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="mode n (x)")
m_mem = mo.ui.slider(1, 4, step=1, value=2, show_value=True, label="mode m (y)")
mo.hstack([n_mem, m_mem], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

xs_m = np.linspace(0, 1, 80)
Xm, Ym = np.meshgrid(xs_m, xs_m)
Zm = np.sin(m_mem.value * np.pi * Xm) * np.sin(n_mem.value * np.pi * Ym)

fig_mem = go.Figure(data=go.Surface(x=Xm, y=Ym, z=Zm, colorscale="RdBu", showscale=False))
fig_mem.update_layout(
    width=650, height=450,
    title_text=f"membrane mode (n, m) = ({n_mem.value}, {m_mem.value})",
    scene=dict(zaxis=dict(range=[-1.2, 1.2])),
)
fig_mem
```

### The sound of music.

 - Music produced by musical instruments is a combination of sound waves with frequencies corresponding to a superposition of the normal modes (called harmonics or overtones in music) of those instruments. 
- Learn more from [this series](https://www.youtube.com/watch?v=jveKIYyafaQ).

:::{figure} ./images/lec4_music.jpg
:label: fig-the-wave-equation-5
:width: 40%

The size of a musical instrument reflects the range of frequencies it is designed to produce: smaller instruments produce higher frequencies, larger instruments lower frequencies.
:::

### Example Problems 

#### Problem 1: Simple Harmonic Oscillator

Solve the ODE:

$$
\frac{d^2 y}{dt^2} + \omega^2 y = 0
$$

where $\omega$ is a constant.

:::{admonition} **Solution:**
:class: dropdown solution

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

:::{admonition} **Solution:**
:class: dropdown solution

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


#### Problem 3: ODE with Constant Coefficients


Solve the ODE:

$$
\frac{d^2 y}{dt^2} - 4 y = 0
$$

:::{admonition} **Solution:**
:class: dropdown solution

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

#### Problem 4: Simple 2nd order ODE

Solve the ODE:

$$
\frac{d^2 y}{dt^2} + 9 y = 0
$$

:::{admonition} **Solution:**
:class: dropdown solution

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


#### Problem 5: When ODE gives repeated roots

Solve the ODE:

$$
\frac{d^2 y}{dt^2} - 6 \frac{dy}{dt} + 9 y = 0
$$

:::{admonition} **Solution:**
:class: dropdown solution

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


