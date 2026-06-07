---
kernelspec:
  name: python3
  display_name: Python 3
---

# Waves

:::{note} **What you will learn**

- **A wave is a self-propagating disturbance** that transfers energy, momentum, and information through a medium without transporting matter. 
- The behavior of waves is governed by the **wave equation**, a partial differential equation (PDE) that describes their spatial and temporal evolution. 
- One major class of waves we will examine is **standing waves**, which remain fixed in space, exhibiting nodes and antinodes. 
- The other is **traveling waves**, which propagate through space, transferring energy from one location to another.

:::


### Types of Waves

- **Disturbance of a medium**: sound waves, waves on a guitar string, waves propagating on the surface of water.
- **Quantum mechanical waves**: described by complex wavefunctions, which explain the wave-like behavior of electrons and atoms. 
- **Electromagnetic waves** (e.g. light, UV, X-rays): the only kind of wave that does not require a medium! EM waves can travel in vacuum. In a sense, an EM wave "rolls out its own carpet," creating its own medium as it moves forward. 
- [**Gravitational waves traveling through spacetime!**]((https://www.youtube.com/watch?v=xj6vV3T4ok8)) 

:::{figure} ./images/propage_stand.gif
:label: fig-waves-1
:alt: applied photoelectric
:width: 40%

1D traveling and standing waves. Traveling waves move with respect to a fixed reference frame, while standing waves oscillate in place. 
:::

:::{figure} images/ext_transverse_longitudinal.gif
:label: fig-waves-2
:alt: applied photoelectric
:width: 50%

Transverse waves carry a disturbance perpendicular to the direction of propagation. Longitudinal waves carry a disturbance along the direction of propagation. 
:::

### Defining a wave mathematically  

- Since a wave is a moving disturbance $u$, we describe this disturbance (e.g. vertical displacement) as a function of space $x$ and time $t$ via some mathematical function $f$: 

$$u = f(x, t)$$

- Imagine surfing on an ocean wave. For an observer (surfer) standing on the wave, the wave stays still at the same coordinate $x'$. 
- For an observer standing on the shore, the coordinate $x$ of the wave front moves away with a constant velocity: 

$$x=x'+vt$$

- Assuming that the shape of the wave stays the same, we can express the motion of the wave in the reference frame of the stationary observer: 

$$f(x,t)=f(x')$$

$$u(x,t) = f(x-vt)$$


- To see why $f(x-vt)$ implies motion to the right, take a constant front of the wave $x-vt=const$, which shows that $x = vt +const$; the same reasoning applied to $f(x+vt)$ gives motion to the left.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display

# Wave shape (Gaussian)
def f(x):
    return np.exp(-x**2)

# Parameters
v = 1.0
x = np.linspace(-10, 10, 600)
t_step = 0.08
n_frames = 150

# Figure
fig, ax = plt.subplots(figsize=(6, 4))
(line_right,) = ax.plot([], [], lw=2, label=r"$f(x-vt)$ (right)")
(line_left,)  = ax.plot([], [], lw=2, ls="--", label=r"$f(x+vt)$ (left)")
ax.set_xlim(-10, 10)
ax.set_ylim(-0.1, 1.1)
ax.set_xlabel("x")
ax.set_ylabel("u(x,t)")
ax.legend(loc="upper right")
ax.set_title("Traveling waves: $f(x\mp vt)$")

def init():
    line_right.set_data([], [])
    line_left.set_data([], [])
    return line_right, line_left

def update(frame):
    t = frame * t_step
    line_right.set_data(x, f(x - v*t))  # right-moving
    line_left.set_data(x,  f(x + v*t))  # left-moving
    return line_right, line_left

ani = FuncAnimation(fig, update, frames=n_frames, init_func=init, blit=True, interval=40)

# >>> Display as inline HTML (no saving needed)
display(HTML(ani.to_jshtml()))
plt.close(fig)
```

### Periodic traveling waves

:::{figure} ./images/lec5_Introwave.jpg
:label: fig-waves-3
:alt: applied photoelectric
:width: 50%

A wave that is periodic in both space and time.
:::

- We will work a lot with periodic waves, whose periodic shape can be described by a sine, a cosine, or their combination. Here is a general expression for a sine wave: 

$$y(x,t)= A \sin(kx+\phi)$$

- Let us now turn this sinusoidal form into a wave traveling along the $x$ axis:

$$
y(x,t)= A \sin(k(x-vt)+\phi)=A \sin(kx-\omega t+\phi)
$$

- **Amplitude** $A$: specifies maximum disturbance. 
- **Wave number** $k$: specifies periodicity in space.
- **Angular frequency** $\omega=kv$: specifies periodicity in time.
- **Initial phase** $\phi$: where the wave starts at $t=0$, $x=0$. Often we just set $\phi=0$.

- When describing waves, it is much more convenient to work with the complex representation. One can always extract the real or imaginary part after the calculations. 


:::{tip} **Complex exponential representation of waves**

$$u(x,t) = Ae^{i(kx-\omega t)}$$

:::

- We can visualize the sine and cosine components of the complex exponential and also visualize **the phasor**, the change of the exponential driven by the change in $t$ for any fixed value of $x$.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display

# -----------------------
# Parameters
# -----------------------
k = 2 * np.pi / 5.0         # wavenumber
omega = 2 * np.pi / 3.0     # angular frequency
x = np.linspace(-10, 10, 600)
x0 = 0.0                    # fixed position for phasor
t_step = 0.08
n_frames = 140              # keep size reasonable for inline JS

# -----------------------
# Figure with two subplots
# -----------------------
fig, (ax_wave, ax_phasor) = plt.subplots(1, 2, figsize=(10, 4))

# Left subplot: real and imaginary parts
(line_real,) = ax_wave.plot([], [], lw=2, label="Re$\\{e^{i(kx-\\omega t)}\\}$")
(line_imag,) = ax_wave.plot([], [], lw=2, ls="--", label="Im$\\{e^{i(kx-\\omega t)}\\}$")
ax_wave.set_xlim(x.min(), x.max())
ax_wave.set_ylim(-1.2, 1.2)
ax_wave.set_xlabel("x")
ax_wave.set_ylabel("Amplitude")
ax_wave.set_title("Real and Imaginary Parts vs x")
ax_wave.legend(loc="upper right")

# Right subplot: phasor
theta = np.linspace(0, 2*np.pi, 400)
ax_phasor.plot(np.cos(theta), np.sin(theta), lw=1)  # unit circle
(point_line,) = ax_phasor.plot([], [], lw=2)        # line from origin to tip
(point_tip,) = ax_phasor.plot([], [], marker='o', lw=0)
ax_phasor.set_aspect('equal', 'box')
ax_phasor.set_xlim(-1.2, 1.2)
ax_phasor.set_ylim(-1.2, 1.2)
ax_phasor.set_xlabel("Re")
ax_phasor.set_ylabel("Im")
ax_phasor.set_title(f"Phasor at x0 = {x0}")

def init():
    line_real.set_data([], [])
    line_imag.set_data([], [])
    point_line.set_data([], [])
    point_tip.set_data([], [])
    return (line_real, line_imag, point_line, point_tip)

def update(frame):
    t = frame * t_step
    phase = k * x - omega * t
    # Left subplot updates
    line_real.set_data(x, np.cos(phase))
    line_imag.set_data(x, np.sin(phase))
    # Right subplot updates (phasor at x0)
    angle = k * x0 - omega * t
    z = np.cos(angle) + 1j*np.sin(angle)
    point_line.set_data([0, z.real], [0, z.imag])
    point_tip.set_data([z.real], [z.imag])
    return (line_real, line_imag, point_line, point_tip)

ani = FuncAnimation(fig, update, frames=n_frames, init_func=init, blit=True, interval=40)

# Display as inline HTML JS animation; then close to avoid duplicate static rendering
display(HTML(ani.to_jshtml()))
plt.close(fig)
```

### Periodicity in space and time

Sine and cosine traveling waves are periodic in space and in time. We introduce two quantities that quantify these periodicities. 

- A periodic wave repeats itself at intervals $x=\lambda$, which is the definition of the wavelength. 
- Mathematically this means that every wavelength in space the wave repeats its pattern: $kx=k\lambda=2\pi$.

:::{important} **Wavevectors $k$: periodicity in space**

$$k=\frac{2\pi}{\lambda}$$

:::

- A periodic wave repeats itself at regular time periods $t=T$ or frequencies $\nu=1/T$. 
- Mathematically this means that after every period the wave repeats its pattern: $\omega t=\omega T=2\pi$.

:::{important} **Angular frequency $\omega$: periodicity in time**

$$\omega=\frac{2\pi}{T} = 2\pi\nu$$

:::




- The following expression makes it explicit that the wave repeats itself in space at every multiple of $\lambda$, and in time at every multiple of $T$:

$$u(x,t) = Asin\Big[2\pi \Big(\frac{x}{\lambda} - \frac{t}{T}\Big)\Big]$$

### Wave equation

- We obtain the equation of motion by using the chain rule and taking partial derivatives of $u$ with respect to $x$ and $t$.

:::{tip} **Waves satisfy a wave equation**
:class: dropdown

 - take two derivatives with respect to $x$

$$u_{xx}^{''} = (ik)^2 u = -k^2u$$

- take two derivatives with respect to $t$

$$u_{tt}^{''} = (-i\omega)^2 u= -\omega^2u$$

- Now take the ratio to eliminate $u$:


$$\frac{u_{xx}^{''}}{u_{tt}^{''}}  = \frac{k^2}{\omega^2} = \frac{1}{v^2}$$

$$u_{xx}^{''} = \frac{1}{v^2}u_{tt}^{''} $$

:::

- Just as in classical mechanics, we need to take a second derivative in order to get the equation of motion, which is determined by the initial position and velocity. By using the chain rule and taking one more derivative with respect to $x$ and $t$, we obtain:


:::{important} **Classical Wave Equation**

$$\frac{\partial^2 u(x,t)}{\partial x^2 } = \frac{1}{v^2}\frac{\partial^2 u(x,t)}{\partial t^2}$$ 

:::

- We just obtained the 1D classical wave equation. Solutions of this equation are functions of time and space called wave functions. 



### Combining waves: interference

- We are often interested in the result of multiple waves interacting with one another, which can be described mathematically by adding up the waves. 

- Combining waves creates a new wave that again obeys the wave equation. This is known as the **linear superposition principle**: if waves $u_A$ and $u_B$ are both solutions of the wave equation, then so is the wave $u_C = u_A + u_B$.


- **Interference**: a phenomenon of combining waves that results in a new wave of greater, lower, or the same amplitude.


:::{figure} images/ext_wave_interference.gif
:label: fig-waves-4
:alt: applied photoelectric
:width: 70%

Constructive vs. destructive interference of two cosine waves $Acos(kx-\omega t)$ and $Acos(kx-\omega t+\phi)$ differing only in phase $\phi$. When the waves differ in phase by $\phi=\pi/2$, they completely cancel each other. When the waves are fully in phase ($\phi=0$), constructive interference doubles the amplitude: $y(x,t)=2A \cos(kx-\omega t)$.
:::


:::{figure} ./images/phasors.gif
:label: fig-waves-5
:alt: applied photoelectric
:width: 20%

Combining waves produces a new wave, shown in both the complex and real representations. 
:::


:::{tip} **Wave interference: derivation**
:class: dropdown

Given the two waves:

$$
\Psi_1(x,t) = e^{i(kx - \omega t + \phi_1)}
$$

$$
\Psi_2(x,t) = e^{i(kx - \omega t + \phi_2)}
$$

We want to sum them:

$$
\Psi_{\text{total}}(x,t) = e^{i(kx - \omega t + \phi_1)} + e^{i(kx - \omega t + \phi_2)}
$$

**Step-by-Step Derivation**

1. **Factor out the common exponential term** $e^{i(kx - \omega t)}$:

$$
\Psi_{\text{total}}(x,t) = e^{i(kx - \omega t)} \left( e^{i\phi_1} + e^{i\phi_2} \right)
$$

2. **Use the exponential addition identity**:

We can rewrite the sum of two exponentials with different phases $\phi_1$ and $\phi_2$ as follows:

$$
e^{i\phi_1} + e^{i\phi_2} = e^{i \frac{\phi_1 + \phi_2}{2}} \left( e^{i \frac{\phi_1 - \phi_2}{2}} + e^{-i \frac{\phi_1 - \phi_2}{2}} \right)
$$

3. **Simplify the remaining terms**:

The term in parentheses is a sum of exponentials with opposite signs in the exponents, which is:

$$
e^{i \frac{\phi_1 - \phi_2}{2}} + e^{-i \frac{\phi_1 - \phi_2}{2}} = 2 \cos\left( \frac{\phi_1 - \phi_2}{2} \right)
$$

4. **Substitute back**:

Substitute this back into the expression for $\Psi_{\text{total}}(x,t)$:

$$
\Psi_{\text{total}}(x,t) = e^{i(kx - \omega t)} \cdot 2 \cos\left( \frac{\phi_1 - \phi_2}{2} \right) e^{i \frac{\phi_1 + \phi_2}{2}}
$$

5. **Combine the exponents**:

Finally, combine the exponents into one:

$$
\Psi_{\text{total}}(x,t) = 2 \cos\left( \frac{\phi_1 - \phi_2}{2} \right) e^{i \left( kx - \omega t + \frac{\phi_1 + \phi_2}{2} \right)}
$$

- Note that if the phases differ by $\pi/2$ we get zero amplitude (complete destructive interference). On the other hand, when they match, the amplitude is doubled.

**Conclusion**

Thus, the sum of two complex exponentials with different phases $\phi_1$ and $\phi_2$ can be expressed as a single complex exponential with the total phase $\frac{\phi_1 + \phi_2}{2}$ and an amplitude modulated by $\cos\left( \frac{\phi_1 - \phi_2}{2} \right)$.


:::

:::{figure} images/ext_wave_interference2.gif
:label: fig-waves-6
:alt: applied photoelectric
:width: 50%

Illustration of wave interference.
:::

### Problems

#### Problem 1: Traveling or standing

- Which of these functions can describe a traveling wave: $u=(x+t)^2$, $u=cos(x-2t)^2$, $cos(x)sin(t)$, and with what velocity?

:::{admonition} **Solution 1**
:class: dropdown solution

If a function can be cast in the form $f(x\pm vt)$, then it can describe a wave propagating with constant velocity $v$ along the $x$ axis. 

- $u=(x+t)^2$ describes a wave traveling in the direction opposite to the $x$ axis with velocity equal to 1.

- $u=cos(x-2t)$ describes a wave traveling in the direction of the $x$ axis with velocity equal to 2.
- $cos(x)sin(t)$ describes a standing wave.
:::


#### Problem 2: Wavelength and frequency 

Given a traveling sine wave $u(x) = sin(2x-10t+\pi/2)$, extract its wavelength, frequency, velocity, and amplitude.

:::{admonition} **Solution 2**
:class: dropdown solution

Traveling waves have the functional form $f\big(k(x-v t)\big) = f(kx-\omega t)$, where $k=2\pi/\lambda$ and $\omega =2\pi\nu$.

Now we can just read off the quantities:

- $|v| = 10$ read off from the sine argument
- $A=1$, the multiplier in front of the sine function
- $k=2$ hence $\lambda = 2\pi/2 = \pi$
- $\omega = kv = 2\cdot 10 = 20$ hence $\nu = \omega/2\pi = 10/\pi$

:::
