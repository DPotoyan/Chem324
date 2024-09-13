
## Waves

```{admonition} What you need to know
:class: note

- **A wave is a self-propagating disturbance** that transfers energy, momentum, and information through a medium, without transporting matter. 
- In quantum mechanics, waves are fundamental to understanding the behavior of particles at small scales.

- The behavior of waves is governed by the **wave equation**, a partial differential equation (PDE) that describes their spatial and temporal evolution. This equation allows us to predict how a wave will propagate, oscillate, and interact with its environment.

- Two major classes of waves we will be examining are **Standing waves** which remain fixed in space, exhibiting nodes and antinodes. **Traveling waves** which propagate through space, transferring energy from one location to another.

- Additionally, waves can be classified as **Transverse**, where the disturbance is perpendicular to the direction of propagation, or **Longitudinal**, where the disturbance is parallel to the direction of propagation.
```


### Types of Waves

- **Disturbance of medium** Sound Waves. Waves on a guitar string. Waves propogating on the surface of the water
- **Quantum mechanical waves** They will be described by complex wavefunctions providing us expanation for the wave like behavior electrons and atoms. 
- **Electromagnetic waves** (e.g. light, UV, X-rays) this is the only kind of wave which does not require a medium! EM waves can travel in vacuum. In a sense, an EM wave "rolls out its own carpet” hence creating its own medium as it moves forward. 
- [**Gravitational waves traveling through spacetime!**]((https://www.youtube.com/watch?v=xj6vV3T4ok8)) 


:::{figure-md} markdown-fig

<img src="./images/propage_stand.gif" alt="applied photoelectric" class="bg-primary mb-1" width="40%">

Visualiziing 1D propagating (or traveling) and standing waves waves. Traveling waves move with respect to a fixed reference frame. Standing waves move in place. 
:::

:::{figure-md} markdown-fig

<img src="https://media.giphy.com/media/og52So0BUmZVe/giphy.gif" alt="applied photoelectric" class="bg-primary mb-1" width="50%">

Transverse waves carry distrubance perpendicular to the direction of wave propogation. Longitudinal waves carry disturbance along the direction of wave propogation. 
:::


### Defining wave mathematically  

- Since wave is a moving disturbance $u$, we describe this disturbance (e.g. vertical displacement) by specifying change of disturbance as a function of space $x$ and time $t$ via some mathematical function $f$: 

$$u = f(x, t)$$

- Imagine surfing on an ocean wave. For an observer (surfer) standing on a wave the wave stands still at the same coordinate $x'$. 
- For the observer standing on the shore the coordinate x of wave front moves away with a constant velocity: 

$$x=x'+vt$$

- Assuming that shape of the wave stays the same we can express the motion of wave in the reference frame of the still observer: 

$$f(x,t)=f(x')$$

$$u(x,t) = f(x-vt)$$


### Periodic traveling waves.

:::{figure-md} markdown-fig

<img src="./images/lec5_Introwave.jpg" alt="applied photoelectric" class="bg-primary mb-1" width="50%">

Wave that is periodic in space and time
:::

- We will be working a lot with periodic waves that have a periodic shape hence can be described by sine or cosine or their combination. Here is a general expression of sin wave: 

$$y(x,t)= A \sin(kx+\phi)$$

- Let us now turn this sinusoidal form into a wave traveling along x axis:

$$
y(x,t)= A \sin(k(x-vt)+\phi)=A \sin(kx-\omega t+\phi)
$$

- **Amplitude** $A$: specifies maximum disturbance. 
- **Wave number** $k$: specifies periodicity in space.
- **Angular frequency** $\omega=kv$: specifies periodicity in time.
- **Initial phase** $\phi$: initial phase. E.g where does wave start at $t=0$ $x=0$ often we just set $\phi=0$.

- When describing waves it is much more convenient to work with complex representation. One can always extract real or imaginary part after calculations. 

:::{admonition} **Complex exponential representation of waves**
:class: warning

$$u(x,t) = Ae^{i(kx-\omega t)}$$

:::


### Wave equation. 

- We obtain equation of motion by using the chain rule and taking partial derivatives of $u$ with respect to $x$ and $t$.

:::{admonition} **Waves satisfy a wave equation**
:class: dropdown, tip

 - take two derivatives with respect to $t$

$$u_{xx}^{''} = (ik)^2 u = -k^2u$$

- take two derivatives with respect to $x$

$$u_{tt}^{''} = (-i\omega)^2 u= -\omega^2u$$

- Now take the ration to replace u:


$$\frac{u_{xx}^{''}}{u_{tt}^{''}}  = \frac{k^2}{\omega^2} = \frac{1}{v^2}$$

$$u_{xx}^{''} = \frac{1}{v^2}u_{tt}^{''} $$

:::

- Just as in classical mechanics we need to take second derivative in order to get the equation of motion that is determined by initial position and velocity. By using the chain rule and taking one more derivative with respect to $x$ and $t$ we obtain:


:::{admonition}
:class: important

$$\frac{\partial^2 u(x,t)}{\partial x^2 } = \frac{1}{v^2}\frac{\partial^2 u(x,t)}{\partial t^2}$$ 

:::

- We just obtained a 1D classical wave equation. Solutions of this equation are functions of time and space called wave functions. 

### Combinding waves: interference

- We are often interested in the result of multiple waves interacting with one another which can be described mathematically when we add up waves. 

- Combinging waves creates a new wave that again obyes wave equation. This known as the **linear superposition principle**  if waves $u_A$ and $u_B$ are both solutions of the wave equation, then so is a wave $u_C = u_A + u_B$.


- **Interference** – a phenomenon of combining waves which results in a new wave of greater, lower, or the same amplitude.

:::{figure-md} markdown-fig

<img src="https://media.giphy.com/media/F3RijSq6e8fi8/giphy.gif" alt="applied photoelectric" class="bg-primary mb-1" width="70%">

Illustration of wave interference
:::



:::{admonition} **Wave interference: derivation**
:class: dropdown, tip

Consider two waves with the same wave number $k$ and angular frequency $\omega$, but with different phases $\phi_1$ and $\phi_2$. These two waves are given by:

$$
\Psi_1(x,t) = e^{i(kx - \omega t + \phi_1)}
$$

$$
\Psi_2(x,t) = e^{i(kx - \omega t + \phi_2)}
$$

To find the total wave function, we sum these two waves:

$$
\Psi_{\text{total}}(x,t) = \Psi_1(x,t) + \Psi_2(x,t) = e^{i(kx - \omega t + \phi_1)} + e^{i(kx - \omega t + \phi_2)}
$$

We can factor out the common term $e^{i(kx - \omega t)}$:

$$
\Psi_{\text{total}}(x,t) = e^{i(kx - \omega t)} \left( e^{i\phi_1} + e^{i\phi_2} \right)
$$

Next, we use Euler’s formula to express $e^{i\phi_1}$ and $e^{i\phi_2}$ in terms of cosines and sines:

$$
e^{i\phi_1} = \cos(\phi_1) + i\sin(\phi_1)
$$

$$
e^{i\phi_2} = \cos(\phi_2) + i\sin(\phi_2)
$$

So, the sum becomes:

$$
e^{i\phi_1} + e^{i\phi_2} = \left( \cos(\phi_1) + \cos(\phi_2) \right) + i \left( \sin(\phi_1) + \sin(\phi_2) \right)
$$

Thus, the total wave is:

$$
\Psi_{\text{total}}(x,t) = e^{i(kx - \omega t)} \left[ \left( \cos(\phi_1) + \cos(\phi_2) \right) + i \left( \sin(\phi_1) + \sin(\phi_2) \right) \right]
$$

- This expression describes the interference of two waves with the same $k$ and $\omega$ but different phases $\phi_1$ and $\phi_2$. The resulting wave depends on the sum of their real and imaginary parts, and the interference pattern is determined by the phase difference $\Delta \phi = \phi_2 - \phi_1$.

- For constructive interference, $\phi_1$ and $\phi_2$ must be in phase, while destructive interference occurs when they are out of phase.

:::

### Wave interference: demonstration. 

- When two waves interfere, their amplitude can double (constructive interference) become 0 (destructive interference) or anything in between:

- $\phi=0$ Fully constructive interference $y(x,t)=2A \cos(kx-\omega t)$
- $\phi=\pi$ Fully destructive interference. $y(x,t)=0$

:::{figure-md} markdown-fig

<img src="https://upload.wikimedia.org/wikipedia/commons/5/5d/Waventerference.gif" alt="applied photoelectric" class="bg-primary mb-1" width="70%">

Constructive vs destructive intereference. 
:::

### Example Problems





