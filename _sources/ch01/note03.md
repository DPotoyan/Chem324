
## Photoelectric effect


:::{admonition} What you need to know
:class: note

- **Photoelectric effect** Electrons are ejected when surface of a material is subjected to radiation exceeding a certain threshold frequency. 
- Below the threshold fequency no electrons are ejected regardless of intensity of light (brightness)
- Photoelectric effect is impossible to explain classically because energy in Classical Mechanics energy is thought to only grows with intensity of light. 
- In QM energy of radiation just like matter is quantized. Radiation can be viewed as a stream of photons: a tiny and discrete packets of energy.
- One photon can eject one electron only if it has sufficient energy. Any extra energy gets converted into kinetic energy resulting in electrons flying faster.
- Photons with insufficent energy scatters of the electron
- High intensity light meaning lots of photons per unit area per unit time are unable to eject a single electron
:::


### Photoelectric effect challanges classical mechanical thinking.

:::{figure-md} markdown-fig

<img src="./images/lect2_Eflying.png" alt="applied photoelectric" class="bg-primary mb-1" width="70%">

Shown are different effects of radiation on material depending on frequency. From left to right frequency of radiation is increasing. 
:::


- When you shine a light on a metal surface exceeding certain threshold frequency electrons, start flying off the surface. But below this frequency no electrons are ejected regardless of the intensity of light. This experiment challanged classical way of thinking about light according to which energy of light is proportional to amplitude of wave or intensity. 

- Recall that to reconcile experiment with theory Planck was already forced to introduce quantization of black bodies modlled as spings that can only assume discrete energies: $0, h\nu, 2h\nu, 3h\nu, …$.  At a time this discreteness was thought to be nothing more than a temporary mathematical trick to fit experimental curve. 

- Einstein, on the other hand, was more imaginative and saw in Plank’s prescription more than just a math trick. He suggested that light can behave like a stream of particles with discrete countable energy packets which he called photons. This view was instrumental in making sense of the photoelectric experiment. 

### Kinetic energy: frequency vs intensity


:::{figure-md} markdown-fig

<img src="./images/photoel1.png" alt="applied photoelectric" class="bg-primary mb-1" width="70%">

Shown are dependece of electron kinetic energy on frequency of radiation that hits the surface of material (left plot) and on intensity of light for frequencies below and above threoshold (right plot).
:::


1. Frequency $\nu$ determines weather electrons will be ejected: $\nu>\nu_0$ but does not affect the number of electrons (current)


2. Kinetic energy of an ejected electron is a linearly increasing function of the frequency of light with no dependence on the intensity: $KE\sim \nu$ 
   
3.  Contrary to wave theory of light increasing intensity (brighter) of light does not eject electrons when frequency is below the threshold $\nu < \nu_0$

   

### Electric current: frequency vs intensity

:::{figure-md} markdown-fig
<img src="./images/photoel2.png" alt="applied photoelectric" class="bg-primary mb-1" width="70%">

Shown are dependece of electron current on frequency of radiation that hits the surface of material (left plot) and on intensity of light for some frequency above threoshold (right plot).  
:::

1. Once threoshold is reached $\nu>\nu_0$  frequency has no effect on electron current (number of electrons)

2. Once threoshold is reached $\nu>\nu_0$ Increasing intensity of light on the other hand increases the current linearly.



### Photons explains photoelectric effect 

- **Light consists of photons**: tiny packets of energy carrying $h\nu$ energy. 
- **Intensity of light**  quantifies number of photons. 
- **Frequency of light**  quantifies energy of photons. 
- **Particular nature of light** 1 photon can "collide" with 1 electron and eject it if photon has sufficient energy.
- **The work function $W_0$** is the minimum amount of energy needed to remove an electron from a metal's surface which has different values for different materials.
- Any extra energy gets converted into kinetic energy $KE$ of the ejected electron
- If frequency is lower than threshold photon does not transfer any energy to the electron! 

:::{admonition} **energy of photon = work function + kinetic energy of electron**
:class: important

$$\boxed{E_{photon} = W_0 + KE}$$

$$\boxed{h\nu = h\nu_0 + \frac{mv_e^2}{2}}$$

:::




### Applications of photoelectric effect

:::{figure-md} markdown-fig
<img src="./images/lec2_applic.jpg" alt="applied photoelectric" class="bg-primary mb-1" width="70%">

Besides its historical role in the establishment of QM photoelectric effect has many practical applications. It is relevant for the design of solar cells, photovoltaics, photoelectron spectroscopy, night vision, etc. ! 
:::


### Explore photoelectric effect

<iframe src="https://phet.colorado.edu/sims/cheerpj/photoelectric/latest/photoelectric.html?simulation=photoelectric"
        width="800"
        height="800"
        allowfullscreen>
</iframe>


### Example Problems

::::{admonition} **Problem 1: Calculating the Threshold Frequency**  
:class: note

A certain metal has a work function of 4.5 eV. Calculate the threshold frequency ($\nu_0$) required to emit electrons from the metal surface.

:::{admonition} **Solution:**
:class: dropdown

The threshold frequency $\nu_0$ is related to the work function $\phi$ by the equation:

$$
\phi = h\nu_0
$$

Where:
- $\phi = 4.5 \, \text{eV}$
- $h = 4.1357 \times 10^{-15} \, \text{eV} \cdot \text{s}$ (Planck's constant)

Now, solve for $\nu_0$:

$$
\nu_0 = \frac{\phi}{h} = \frac{4.5 \, \text{eV}}{4.1357 \times 10^{-15} \, \text{eV} \cdot \text{s}} \approx 1.088 \times 10^{15} \, \text{Hz}
$$

:::

::::

---

::::{admonition} **Problem 2: Maximum Kinetic Energy of Photoelectrons**
:class: note 

Ultraviolet light with a wavelength of 250 nm is incident on a metal surface with a work function of 3.0 eV. Calculate the maximum kinetic energy of the emitted photoelectrons.

:::{admonition} **Solution:**
:class: dropdown

First, calculate the energy of the incident photons:

$$
E_{\text{photon}} = \frac{hc}{\lambda}
$$

Where:
- $h = 6.626 \times 10^{-34} \, \text{J} \cdot \text{s}$
- $c = 3.00 \times 10^8 \, \text{m/s}$
- $\lambda = 250 \, \text{nm} = 250 \times 10^{-9} \, \text{m}$

$$
E_{\text{photon}} = \frac{6.626 \times 10^{-34} \times 3.00 \times 10^8}{250 \times 10^{-9}} \, \text{J} = 7.95 \times 10^{-19} \, \text{J}
$$

Convert this energy to eV:

$$
E_{\text{photon}} = \frac{7.95 \times 10^{-19} \, \text{J}}{1.602 \times 10^{-19} \, \text{J/eV}} \approx 4.96 \, \text{eV}
$$

The maximum kinetic energy $K_{\text{max}}$ of the emitted photoelectrons is given by:

$$
K_{\text{max}} = E_{\text{photon}} - \phi = 4.96 \, \text{eV} - 3.0 \, \text{eV} = 1.96 \, \text{eV}
$$
:::

::::

---

::::{admonition} **Problem 3: Photoelectric Current and Light Intensity**  
:class: note

Explain how the intensity of incident light affects the photoelectric current, assuming the frequency of the light is above the threshold frequency.

:::{admonition} **Solution:**
:class: dropdown

In the photoelectric effect, the intensity of the incident light is proportional to the number of photons striking the metal surface per unit time. If the frequency of the light is above the threshold frequency, each photon has sufficient energy to eject an electron.

As the intensity increases, more photons hit the surface, leading to the emission of more photoelectrons. Consequently, the photoelectric current, which is proportional to the number of emitted electrons, increases with the intensity of the incident light. However, the kinetic energy of the emitted electrons remains the same and is determined by the energy of the individual photons, not the intensity of the light. \, \text{eV}
$$

:::

::::





