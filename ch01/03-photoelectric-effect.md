
# Photoelectric effect


:::{note} **What you will learn**

- **Photoelectric Effect:** Electrons are ejected from the surface of a material when it is exposed to radiation with a frequency exceeding a specific threshold frequency.
- **Threshold Frequency:** No electrons are ejected if the radiation's frequency is below this threshold, regardless of the light's intensity (brightness).
- **Classical vs. Quantum:** The photoelectric effect cannot be explained using classical mechanics, where energy is thought to increase continuously with light intensity. However, in quantum mechanics, energy is quantized. Radiation is treated as a stream of photons, which are discrete packets of energy.
- **Photon-Electron Interaction:** A single photon can eject a single electron if the photon has sufficient energy. Any excess energy is converted into the kinetic energy of the ejected electron, causing it to move faster.
- **Insufficient Energy:** Photons with energy below the threshold will not eject electrons; instead, they scatter off the material.
- **High-Intensity Light:** Even high-intensity light, which means more photons per unit area per unit time, cannot eject electrons if the photons lack sufficient energy.
:::


### Photoelectric effect challenges classical mechanical thinking.

:::{figure} ./images/lect2_Eflying.png
:label: fig-photoelectric-effect-1
:alt: applied photoelectric
:width: 70%

Effect of radiation on a material depending on frequency. Frequency increases from left to right.
:::

- When you shine radiation on a metal surface, above some **threshold frequency** electrons start flying off the surface. 
- Below this frequency no electrons are ejected, regardless of the intensity of the radiation. 
- This experiment challenged the classical way of thinking about radiation, according to which the energy of radiation is proportional to the amplitude of the wave, that is, its intensity or the brightness of the light. 

### Introducing Photon

- Recall that to reconcile experiment with theory, Planck was already forced to introduce quantization of black bodies modeled as springs that can only assume discrete energies: $0, h\nu, 2h\nu, 3h\nu, …$ giving off radiation with the same frequencies! 

- At that time, this discreteness introduced by Planck was thought to be nothing more than a temporary mathematical trick to fit the experimental curve. 

- Einstein, on the other hand, was more imaginative and saw in Planck’s prescription more than just a math trick. He suggested that light can behave like a stream of particles with discrete, countable energy packets, which he called photons. This view was instrumental in making sense of the photoelectric experiment. 

:::{important} **Energy of Photon**

$$
E_{photon} = h\nu = \frac{hc}{\lambda}
$$

- $E_{photon}$ energy of a photon.
- $\nu$ frequency of a single photon.

:::

- Thus we see that both matter and radiation are quantized and given by the same relation of frequency times the Planck constant.

### Kinetic energy: frequency vs intensity


:::{figure} ./images/photoel1.png
:label: fig-photoelectric-effect-2
:alt: applied photoelectric
:width: 70%

Dependence of electron kinetic energy on the frequency of radiation hitting the material surface (left) and on the intensity of light for frequencies below and above threshold (right).
:::


1. Frequency $\nu$ determines whether electrons will be ejected: $\nu>\nu_0$, but it does not affect the number of electrons (current)


2. Kinetic energy of an ejected electron is a linearly increasing function of the frequency of light with no dependence on the intensity: $KE\sim \nu$ 
   
3.  Contrary to the wave theory of light, increasing the intensity (brightness) of light does not eject electrons when the frequency is below the threshold $\nu < \nu_0$

   

### Electric current: frequency vs intensity

:::{figure} ./images/photoel2.png
:label: fig-photoelectric-effect-3
:alt: applied photoelectric
:width: 70%

Dependence of electron current on the frequency of radiation hitting the material surface (left) and on the intensity of light for a frequency above threshold (right).
:::

1. Once the threshold is reached $\nu>\nu_0$, frequency has no effect on electron current (number of electrons)

2. Once the threshold is reached $\nu>\nu_0$, increasing the intensity of light, on the other hand, increases the current linearly.



### Photons explain photoelectric effect 

- **Light consists of photons**: tiny packets of energy carrying $E_{photon}=h\nu$ energy. 
- **Intensity of light**  quantifies number of photons. 
- **Frequency of light**  quantifies energy of photons. 
- If light radiates $n$ photons per second, then the total energy radiated per second is $nh\nu$
- **Particle nature of light:** 1 photon can "collide" with 1 electron and eject it if the photon has sufficient energy.


:::{important} **Energy of photon = work function + kinetic energy of electron**

$${E_{photon} = W_0 + KE}$$

$${h\nu = h\nu_0 + \frac{mv_e^2}{2}}$$

- **The work function $W_0=h\nu_0$** is the minimum amount of energy needed to remove an electron from a metal's surface, and it has different values for different materials. 
- The $\nu_0$ is the **threshold frequency:** the minimum frequency needed to eject an electron. If the frequency is lower than the threshold, the photon does not transfer any energy to the electron! 
- Any extra energy gets converted into kinetic energy $KE=mv_e^2/2$ of the ejected electron, where $v_e$ is the magnitude of the ejected electron's velocity. 
:::




### Applications of photoelectric effect

:::{figure} ./images/lec2_applic.jpg
:label: fig-photoelectric-effect-4
:alt: applied photoelectric
:width: 70%

Besides its historical role in the establishment of QM, the photoelectric effect has many practical applications. It is relevant to the design of solar cells, photovoltaics, photoelectron spectroscopy, night vision, and more.
:::


### Explore photoelectric effect

Pick a metal and a wavelength. The line is Einstein's equation $KE_{max} = h\nu - W_0$ for that metal: its slope is always $h$, and only the intercept (the threshold $\nu_0$) moves when you change the metal. The marker shows the light you chose: a dot on the line when electrons come out, a cross on the axis when the photon energy falls short.

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
:hide-code: true

metal_pe = mo.ui.dropdown(
    options={
        "cesium (W0 = 2.14 eV)": 2.14,
        "sodium (W0 = 2.28 eV)": 2.28,
        "potassium (W0 = 2.30 eV)": 2.30,
        "zinc (W0 = 4.33 eV)": 4.33,
        "copper (W0 = 4.70 eV)": 4.70,
        "platinum (W0 = 5.65 eV)": 5.65,
    },
    value="sodium (W0 = 2.28 eV)",
    label="metal",
)
lam_pe = mo.ui.slider(150, 800, step=5, value=400, show_value=True, label="light wavelength (nm)")
mo.vstack([metal_pe, lam_pe])
```

```{marimo} python
:hide-code: true

h_eV, c_pe = 4.1357e-15, 2.998e8
W_pe = metal_pe.value
nu0_pe = W_pe / h_eV
nu_light = c_pe / (lam_pe.value * 1e-9)
E_light = h_eV * nu_light
KE_light = E_light - W_pe
nu_ax = np.linspace(0, 2.5e15, 500)
ke_ax = np.where(nu_ax > nu0_pe, h_eV * nu_ax - W_pe, np.nan)
fig3, ax3 = plt.subplots(figsize=(6.5, 3.6))
ax3.plot(nu_ax / 1e14, ke_ax, lw=2, color="C3", label="KE_max = hν - W0")
ax3.plot([0, nu0_pe / 1e14], [0, 0], lw=5, color="gray", alpha=0.4, solid_capstyle="butt", label="no emission")
ax3.axhline(0, color="k", lw=0.8)
ax3.axvline(nu0_pe / 1e14, color="gray", ls=":", lw=1)
ax3.text(nu0_pe / 1e14 + 0.3, 6.3, "ν0", fontsize=10, color="gray")
if KE_light > 0:
    ax3.plot(nu_light / 1e14, KE_light, "o", ms=9, color="C0", zorder=5)
else:
    ax3.plot(nu_light / 1e14, 0, "x", ms=11, mew=2.5, color="C0", zorder=5)
ax3.axvspan(c_pe / 750e-9 / 1e14, c_pe / 380e-9 / 1e14, color="gold", alpha=0.15)
ax3.set_xlim(0, 25)
ax3.set_ylim(-0.5, 7)
ax3.set_xlabel(r"frequency $\nu$ ($10^{14}$ Hz)")
ax3.set_ylabel("KE$_{max}$ (eV)")
ax3.set_title(f"Fig. Photoelectron KE vs light frequency, threshold {nu0_pe / 1e14:.1f} x 10^14 Hz, shaded band is visible light", fontsize=9)
ax3.legend(frameon=False, fontsize=9, loc="center right")
fig3.tight_layout()
fig3
```

```{marimo} python
:hide-code: true

verdict_pe = (
    f"electrons fly off with KE_max = **{KE_light:.2f} eV**"
    if KE_light > 0
    else "**no electrons**, no matter how bright the light"
)
mo.md(f"Photon energy **{E_light:.2f} eV** at {lam_pe.value} nm versus work function **{W_pe:.2f} eV**: {verdict_pe}.")
```


### Problems

#### Problem 1: Threshold frequency

A certain metal has a work function of 4.5 eV. Calculate the threshold frequency ($\nu_0$) required to emit electrons from the metal surface.

:::{admonition} **Solution**
:class: dropdown solution

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

#### Problem 2: Maximum kinetic energy of photoelectrons

Ultraviolet light with a wavelength of 250 nm is incident on a metal surface with a work function of 3.0 eV. Calculate the maximum kinetic energy of the emitted photoelectrons.

:::{admonition} **Solution**
:class: dropdown solution

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

#### Problem 3: Photoelectric current and light intensity

Explain how the intensity of incident light affects the photoelectric current, assuming the frequency of the light is above the threshold frequency.

:::{admonition} **Solution**
:class: dropdown solution

In the photoelectric effect, the intensity of the incident light is proportional to the number of photons striking the metal surface per unit time. If the frequency of the light is above the threshold frequency, each photon has sufficient energy to eject an electron.

As the intensity increases, more photons hit the surface, leading to the emission of more photoelectrons. Consequently, the photoelectric current, which is proportional to the number of emitted electrons, increases with the intensity of the incident light. However, the kinetic energy of the emitted electrons remains the same and is determined by the energy of the individual photons, not the intensity of the light.
:::

#### Problem 4: Which metal is it?

Light of wavelength 300 nm shines on an unknown metal, and the fastest photoelectrons are stopped by a reverse voltage of 1.85 V (so $KE_{max} = 1.85$ eV). Find the work function and identify the metal from this list: cesium 2.14 eV, sodium 2.28 eV, zinc 4.33 eV, copper 4.70 eV. What is the longest wavelength that still ejects electrons from it?

#### Problem 5: From photons to current

A 2.0 mW beam of 400 nm light falls on a potassium surface (work function 2.30 eV). (a) How many photons hit the surface per second? (b) If one photon in twenty ejects an electron, what current flows? (c) How does the answer to (b) change if the intensity doubles? And if the wavelength is halved at the same power?

#### Problem 6: Visible light and cesium

Cesium has the lowest work function of the common metals, 2.14 eV. Find its threshold wavelength. Which colors of visible light can eject electrons from cesium and which cannot? Suggest why cesium-coated cathodes were the material of choice for early photocells and night-vision tubes.

#### Problem 7: The missing time delay

In the wave picture an electron would have to soak up energy gradually from the light wave. For a very dim source of intensity $10^{-10}$ W/m$^2$, estimate how long an atom of cross-sectional area $10^{-20}$ m$^2$ would need to collect the 2 eV required to escape. Experimentally, photoelectrons appear within nanoseconds of switching on the light, however dim. What does this tell you about how light delivers its energy?
