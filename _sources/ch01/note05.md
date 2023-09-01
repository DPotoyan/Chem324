

## Wave-particle duality


```{admonition} What you need to know
:class: note
- Compton scattering and electron diffraction experiment shave demonstrated that concepts of a particle and wave are not mutually exclusive.

- A physical entity has both wave-like (wavelengths, interference, diffraction, etc.) and particle-like (momentum, collision, countable, etc.) characteristics. An electron has a wavelength; a photon has momentum.

- Wave-like and particle-like characteristics are inversely proportional to each other and are quantified by de Broglie relation: $\lambda = \frac{h}{p}$

-  Thus all quantum objects can behave both as a wave and a particle! Which behavior would be more pronounced depends on the experiment!
```

### Diffraction and Double Slit experiment 

![](https://i0.wp.com/opencurve.info/wp-content/uploads/2020/05/double_slit.gif)

- In classical double slit experiment light is permitted to diffract through slits that display diffraction: that is producing wave-like interference patterns or bands on an opposite screen.

### Refraction and prisms

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Light_dispersion_conceptual_waves.gif/330px-Light_dispersion_conceptual_waves.gif)

- Another closely related phenomenon is refraction: change in direction of propagation of any wave as a result of its traveling at different speeds at different points along the wave front.
- For example, light bends when it travels from air to glass. 
 The bending of light by refraction makes it possible for us to have lenses, magnifying glasses, prisms, and rainbows. Even our eyes depend upon this bending of light

### Bragg's formula for diffraction. 

- X-rays interact with the atoms in a crystal. The phase shift upon scattering off of atoms causes constructive (left figure) or destructive (right figure) interferences.

![](./images/lec3_Xscatter.png)

- Maxima and minima in interference patters are dictated by simple geometric  argument captured in Bragg’s formula: 

$$\boxed{2d sin\theta = n\lambda}$$

- One expects waves like X-rays to show interference patterns according to this formula. Interference was thought to be a purely a wave like phenomenon. 

### Both X-rays and electrons show diffraction patterns. 

![](./images/lec3_Xscatter2.png)


- In 1925, Davisson and Germer were studying electron scattering from various materials. To their great surprise, they discovered that at certain angles there was a peak in the intensity of the scattered electron beam. 
- This peak indicated wave behavior for the electrons and could be interpreted by Bragg's law (previously only applied to X-ray scattering) to give values for the lattice spacing in the nickel crystal. 

![](./images/lec3_DavisonGermer.png)



### Particles can behave like waves in appropriate circumstances.  


![](https://upload.wikimedia.org/wikipedia/commons/7/7d/Wave-particle_duality.gif)

- Observing diffraction patterns and computing wavelength from de Broglie relation confirmed that thinking of matter as a dual wave-particle was correct with an impressive agreement between experimental predictions and theory. 

### But which way did the electron go??

:::{figure-md} markdown-fig
<img src="./images/double_slit1.png" alt="compton" class="bg-primary mb-1" width="300px">
:::

- The interference pattern would arise only if we consider electrons as waves, which
interfere with each other (i.e. constructive and deconstructive interference)
- When the experiment is carried out many times with only one electron going through
the holes at once, we still observe the interference effect.

:::{figure-md} markdown-fig
<img src="./images/double_slit2.png" alt="compton" class="bg-primary mb-1" width="300px">
:::

- If we try to determine which way the electron traveled, the interference pattern disappears!

- We will return to resolve this puzzle after establishing the formal theory of quantum mechanics and its postulates. 
### Compton scattering

:::{figure-md} markdown-fig
<img src="./images/lec3_compton.jpeg" alt="compton" class="bg-primary mb-1" width="200px">

Compton scattering: A phenomenon where photons scatter off electrons the same way other particles with mass do.
:::


- Arthur Compton showed that X-rays get scattered off free electrons like elastic billiard balls. Applying conservation of momentum principle (previously only applied to particle-like objects), it was shown that the outgoing X-rays should be of longer wavelength than the incoming ones. 
- This means that a moving photon hits the resting free electron and transfers some energy to get the electron moving. Note that this experimental result makes sense only if you think of a photon as a particle with linear momentum which gets bounced off the electron.


### Wave particle duality as universal feature of nature. 

- Light is a wave and a particle. An electron is also a particle and a wave. Is everything a wave and a particle? The answer is YES! This is what is meant by wave-particle duality.  Sometimes we only see one side of the duality because under some conditions, either wave or particle characteristics are more pronounced. 

- The wave-like and particle-like characteristics of a physical entity are inversely proportional to each other as described by the de Broglie relationship.

### De Broglie relation

$$\boxed{\lambda = \frac{h}{p}}$$

- Where $h$: Planck's constant. $p$: the momentum of the object (electron, photon, molecule, chair, etc.). $\lambda$: wavelength associated with the object. 

- The relation implies that heavy objects have a small wavelength, and light objects have a large wavelength. 

- The smaller the object, the more pronounced wave-like qualities it will have. And vice versa, the bigger the object, the more particle-like qualities it will have. 


### Effect of potential energy

According to classical physics, the total energy for a particle is given as a sum of the kinetic and potential energies:

$$
E = \frac{1}{2}mv^2 + V = \frac{p^2}{2m} + V = T + V
$$

If we substitute de Broglie's expression for momentum we get:

$$\lambda = \frac{h}{\sqrt{2m(E - V)}}$$

- This equation shows that the de Broglie wavelength for particle like electron with constant total energy $E$ would change as it moves into a region with different potential energy. 
- This has implications of chemical bonding where electrons experience different fields in atoms and molecules. 

### Uncertainty relation

- The uncertainty principle, also known as Heisenberg's Uncertainty Principle, states that it is impossible to measure the exact position and momentum of a particle at the same time. This principle is based on the wave-particle duality of matter

- The principle states that the more precisely the position is known, the more uncertain the momentum is, and vice versa. For example, if we know everything about where a particle is located, we know nothing about its momentum.


![](https://upload.wikimedia.org/wikipedia/commons/7/78/Uncertainty_Momentum_1.gif)

### Heisenberg's uncertainty principle

- Mathematically uncertainly relation is expressed in terms of standard deviations of position $\sigma_x$ and momenta $\sigma_p$ which are quantified by doing repeat experiments measuring positions, momenta followed by quantifying the spread via standard deviation.

$$
\sigma_x \sigma_p \geq \hbar/2
$$

### Problems

#### Problem 1

Estimate the wavelength of electrons that have been accelerated from
rest through a potential difference of $V = 40 kV$. 
- Note that potential energy difference that the electrons experience is simply $e×V$ where e is the magnitude of electron charge and $V$ potential difference.

:::{dropdown} Solution
In order to calculate the de Broglie wavelength, we need to calculate the linear momentum of the electrons.
At the end of the acceleration, all the acquired energy is in the form of kinetic energy ($p^2 / 2m_e$).

$$
\frac{p^2}{2m_e} = eV \Rightarrow p = {\sqrt{2m_eeV}}
$$

$$
{\lambda = \frac{h}{p} = \frac{h}{\sqrt{2m_eeV}}}{= \frac{6.626\times 10^{-34}\textnormal{ Js}}{\sqrt{2\times (9.109\times 10^{-31}\textnormal{ kg})\times (1.609\times 10^{-19}\textnormal{ C})\times (4.0\times 10^4\textnormal{ V})}}}{ = 6.1\times 10^{-12}}\, m
$$
:::

#### Problem 2

If you would consider yourself as a particle moving at $2 m/s$, what would be your de Broglie wavelength? 
Would it make sense to use quantum mechanics in this case?

:::{dropdown} Hint
- A. Plug in velocity in the classical mechanics expression for momentum $p=mv$ then use de Brglie equation to compute wavelength
:::

#### Problem 3

Quantify uncertainty in position of electron in the ground state of H atom by using Bohr's model. 

:::{dropdown} Hint
- Bohr's equation expresses velocty, energy and radius of electron orbit as a function of quantum number n. 
:::

#### Problem 4

Quantify uncertainty in the position of electron traveling freely with kinetic energy of $3 eV$

:::{dropdown} Hint
$$KE = \frac{p^2}{2m}$$
:::