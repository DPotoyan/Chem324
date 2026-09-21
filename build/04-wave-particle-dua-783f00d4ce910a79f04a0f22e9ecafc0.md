---
kernelspec:
  name: python3
  display_name: Python 3
---
# Wave-particle duality


:::{note} **What you will learn**

- Compton scattering and electron diffraction experiments have demonstrated that the concepts of particles and waves are not mutually exclusive.

- A physical entity exhibits both wave-like (e.g., wavelength, interference, diffraction) and particle-like (e.g., momentum, collisions, countable) characteristics. For instance, an electron has a wavelength, while a photon has momentum.

- The relationship between wave-like and particle-like characteristics is inversely proportional and is quantified by the de Broglie relation: $\lambda = \frac{h}{p}$, where $\lambda$ is the wavelength, $h$ is Planck's constant, and $p$ is momentum.

- Therefore, all quantum objects can behave as both waves and particles! The dominant behavior, wave-like or particle-like, depends on the specific experimental conditions.
:::

### Diffraction, interference and the double-slit experiment


:::{figure} images/ext_double_slit.gif
:label: fig-wave-particle-duality-1
:alt: compton
:width: 300px

Waves passing through two slits create a diffraction pattern on the screen.
:::

- **Diffraction:** spreading of waves around obstacles or through small openings. Diffraction can occur with any type of wave, including light, sound, radio, and water.

- **Interference:** when two waves meet, their combined intensity goes up or down depending on whether the waves are in phase or out of phase, respectively.

- **Double-slit experiment:** light waves (or water waves) pass through a wall with two slits, which results in wave-like interference patterns, or bands, on the detector screen.

### Bragg's formula for diffraction

- X-rays interact with the atoms in a crystal. The phase shift upon scattering off of atoms causes constructive (left figure) or destructive (right figure) interferences.


:::{figure} ./images/lec3_Xscatter2.png
:label: fig-wave-particle-duality-3
:alt: compton
:width: 400px

X-rays scattering off atoms in a crystal: constructive interference (left) and destructive interference (right).
:::


**Maxima and minima in interference patterns** arise from simple geometry, as captured by **Bragg’s law**:

:::{important} **Bragg's law**

$$
\boxed{2d \sin\theta = n\lambda}
$$

:::

* $d$: spacing between atomic planes in the lattice

* $\lambda$: wavelength of the radiation

* $n$: order of diffraction. For $n=1$, the extra path length is one wavelength; for $n=2$, it is two wavelengths, and so on. Higher-order reflections ($n > 1$) occur at larger angles and are usually weaker, so in practice most analyses focus on $n=1$.

* Waves such as X-rays produce interference patterns according to this relation. Historically, such interference was regarded as a hallmark of wave-like behavior.


### Both X-rays and electrons show diffraction patterns


:::{figure} ./images/lec3_DavisonGermer.png
:label: fig-wave-particle-duality-4
:alt: compton
:width: 500px

Demonstration of electron diffraction. 
:::

- In 1927, Davisson and Germer were studying electron scattering from various materials. To their great surprise, they discovered that at certain angles there was a peak in the intensity of the scattered electron beam. 
- This peak indicated wave behavior for the electrons and could be interpreted by Bragg's law (previously only applied to X-ray scattering) to give values for the lattice spacing in the nickel crystal. 


### Compton scattering

:::{figure} ./images/lec3_compton.jpeg
:label: fig-wave-particle-duality-5
:alt: compton
:width: 300px

Compton scattering: photons scatter off electrons just as massive particles do.
:::


- Arthur Compton showed that X-rays get scattered off free electrons like elastic billiard balls. Applying conservation of momentum principle (previously only applied to particle-like objects), it was shown that the outgoing X-rays should be of longer wavelength than the incoming ones. 
- This means that a moving photon hits the resting free electron and transfers some energy to get the electron moving. Note that this experimental result makes sense only if you think of a photon as a particle with linear momentum which gets bounced off the electron.

:::{important} **Photon momentum and the Compton shift**

$$p_{photon} = \frac{E}{c} = \frac{h\nu}{c} = \frac{h}{\lambda}$$

$$\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}\,(1-\cos\theta)$$

- $\theta$ is the angle by which the photon is deflected and $\lambda_C = h/m_e c = 2.43 \times 10^{-12}$ m is the **Compton wavelength** of the electron.
- The shift depends only on the angle, not on the incoming wavelength, exactly what conservation of energy and momentum predict for a collision between two particles. The relation $p = h/\lambda$ for a photon is the one de Broglie extended to matter below.
:::



### De Broglie wavelength and wave-particle duality

- Light is a wave and a particle. An electron is also a particle and a wave. Is everything a wave and a particle? The answer is YES! This is what is meant by wave-particle duality. Sometimes we only see one side of the duality because, under certain conditions, either the wave or the particle characteristics are more pronounced.


- The wave-like and particle-like characteristics of a physical entity are inversely proportional to each other as described by the de Broglie relationship.


:::{important} **De Broglie relation**

$$\boxed{\lambda = \frac{h}{p}}$$

- Where $h$: Planck's constant. $p$: the momentum of the object (electron, photon, molecule, chair, etc.). $\lambda$: wavelength associated with the object. 

:::

- The relation implies that heavy objects have a small wavelength, and light objects have a large wavelength. 

- The smaller the object, the more pronounced wave-like qualities it will have. And vice versa, the bigger the object, the more particle-like qualities it will have. 


#### Effect of potential energy

According to classical physics, the total energy for a particle is given as a sum of the kinetic and potential energies:

$$
E = \frac{1}{2}mv^2 + V = \frac{p^2}{2m} + V = T + V
$$

If we substitute de Broglie's expression for momentum we get:

$$\lambda = \frac{h}{\sqrt{2m(E - V)}}$$

- This equation shows that the de Broglie wavelength of a particle such as an electron with constant total energy $E$ changes as it moves into a region with different potential energy.
- This has implications for chemical bonding, where electrons experience different fields in atoms and molecules.


### Waves have to fit

The de Broglie relation has a consequence that goes far beyond diffraction. Take the
electron wave and wrap it around a closed loop, as in an orbit around a nucleus. After one
complete trip around the loop, called a **pass**, the wave meets itself and has no choice but
to agree with where it started. If the circumference holds a whole number of wavelengths,
every pass reinforces the one before it and a **standing wave** survives. If it does not,
successive passes land out of step and the wave interferes itself away.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, GREEN = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#1a7f37"
R, AMP, LAPS = 1.0, 0.17, 8              # ring radius, wave amplitude, passes summed
th1 = np.linspace(0, 2 * np.pi, 900)             # first pass around the loop
th2 = np.linspace(2 * np.pi, 4 * np.pi, 900)     # second pass around the loop

# amplitude left after LAPS passes: the passes add as phasors exp(2 pi i n k)
n_grid = np.linspace(1.5, 6.5, 2000)
survival = np.abs(np.exp(2j * np.pi * n_grid * np.arange(LAPS)[:, None]).sum(axis=0)) / LAPS

n_seq = [2.0] * 4                        # sweep n, pausing on each whole number
for target in (3.0, 4.0, 5.0, 6.0):
    n_seq += list(np.linspace(n_seq[-1], target, 11, endpoint=False)) + [target] * 4

fig, (ax, bx) = plt.subplots(1, 2, figsize=(8.8, 4.2), gridspec_kw={"width_ratios": [1, 1.15]})

ax.add_patch(Circle((0, 0), R, fill=False, color=GRAY, lw=1.2, ls="--"))
ax.plot(0, 0, "o", color=CARDINAL, ms=9)
(lap1,) = ax.plot([], [], color=PURPLE, lw=2.4, label="1st pass")
(lap2,) = ax.plot([], [], color="#e07b00", lw=2.0, ls="--", label="2nd pass")
(gap,) = ax.plot([], [], color=CARDINAL, lw=3.4, solid_capstyle="butt", zorder=6)
(startdot,) = ax.plot([], [], "o", color=PURPLE, ms=8, mec="white", mew=1.2, zorder=7)
(enddot,) = ax.plot([], [], "o", color="#e07b00", ms=8, mec="white", mew=1.2, zorder=7)
gaplabel = ax.text(0, -1.42, "", fontsize=10.5, ha="center", va="center")
verdict = ax.set_title("", fontsize=12, pad=10)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False, fontsize=9)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.55); ax.set_aspect("equal"); ax.axis("off")

bx.plot(n_grid, survival, color=TEAL, lw=2.2)
bx.fill_between(n_grid, survival, color=TEAL, alpha=0.10)
(marker,) = bx.plot([], [], "o", color=CARDINAL, ms=9, zorder=5)
vline = bx.axvline(2.0, color=CARDINAL, lw=1.2, ls=":")
bx.set_xlim(1.5, 6.5); bx.set_ylim(-0.03, 1.18); bx.set_xticks(range(2, 7))
bx.set_xlabel(r"wavelengths around the orbit,  $n = 2\pi r / \lambda$", fontsize=11)
bx.set_ylabel("amplitude left after 8 passes", fontsize=11)
bx.set_title(r"Only integer $n$ survives", fontsize=12, pad=10)
for s in ("top", "right"):
    bx.spines[s].set_visible(False)
fig.suptitle(r"A standing wave on a Bohr orbit:  $2\pi r = n\lambda = nh/p$", fontsize=13.5, y=0.99)
fig.tight_layout(rect=(0, 0, 1, 0.93))

def update(i):
    n = n_seq[i]
    lap1.set_data((R + AMP * np.sin(n * th1)) * np.cos(th1), (R + AMP * np.sin(n * th1)) * np.sin(th1))
    lap2.set_data((R + AMP * np.sin(n * th2)) * np.cos(th2), (R + AMP * np.sin(n * th2)) * np.sin(th2))
    r1 = R + AMP * np.sin(2 * np.pi * n)          # where the wave sits after one full pass
    gap.set_data([R, r1], [0, 0]); startdot.set_data([R], [0]); enddot.set_data([r1], [0])
    closes = abs(n - round(n)) < 1e-9
    off = abs(n - round(n))
    verdict.set_text(f"$n$ = {n:.2f}   " + ("the wave closes on itself" if closes else "the wave misses itself"))
    verdict.set_color(GREEN if closes else CARDINAL)
    gaplabel.set_text("the 2nd pass lands on the 1st" if closes else rf"the 2nd pass is {off:.2f}$\lambda$ out of step")
    gaplabel.set_color(GREEN if closes else CARDINAL)
    marker.set_data([n], [abs(np.exp(2j * np.pi * n * np.arange(LAPS)).sum()) / LAPS])
    vline.set_xdata([n, n])
    return lap1, lap2, gap, startdot, enddot, gaplabel, marker, vline, verdict

ani = FuncAnimation(fig, update, frames=len(n_seq), interval=80, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Left: an electron wave wrapped around an orbit, drawn for two passes. Right: the
amplitude left after eight passes, which is sharply peaked at whole numbers of wavelengths.

The closure condition is nothing more than the circumference holding $n$ wavelengths:

$$
2\pi r = n\lambda = \frac{nh}{p}, \qquad n = 1, 2, 3, \ldots
$$

Rearranging gives the quantization of angular momentum,

$$
L = pr = mvr = n\frac{h}{2\pi} = n\hbar
$$

:::{note} **Quantization is what waves do when you confine them**

Nothing was postulated here. A whole number appeared because a wave in a closed region has
to match itself, exactly as a guitar string of fixed length can only sound a discrete set of
notes. This standing-wave condition is the starting point of Bohr's model of the hydrogen
atom in the next lecture, and the same idea returns as the particle in a box in Chapter 3.
:::

### Double-slit experiment


<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/qCmtegdqOOA?si=cHMCoUJcuoS1nylO" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

:::{figure} images/ext_wave_particle_duality.gif
:label: fig-wave-particle-duality-6
:alt: compton
:width: 400px

Wave-particle duality in the double-slit experiment.
:::

**Electron displays wave-like interference**

- The interference pattern arises only if we consider electrons as waves that
interfere with each other (i.e., constructive and destructive interference).
- When the experiment is carried out many times with only one electron going through
the slits at a time, we still observe the interference effect.

:::{figure} ./images/double_slit1.png
:label: fig-wave-particle-duality-7
:alt: compton
:width: 400px

Where electrons are expected to land according to classical versus quantum theory.
:::

**But which slit did the electron go through??**

- If we try to determine which way the electron traveled, the interference pattern disappears!
- We will return to resolve this puzzle after establishing the formal theory of quantum mechanics and its postulates. 


:::{figure} ./images/double_slit2.png
:label: fig-wave-particle-duality-8
:alt: compton
:width: 300px

A detector fires photons to determine which slit each electron exits from.
:::



### Uncertainty relation

- The uncertainty principle, also known as Heisenberg's uncertainty principle, states that it is impossible to measure the exact position and momentum of a particle at the same time. This principle is based on the wave-particle duality of matter.

- The principle states that the more precisely the position is known, the more uncertain the momentum is, and vice versa. For example, if we know everything about where a particle is located, we know nothing about its momentum.

:::{figure} images/ext_uncertainty_momentum.gif
:label: fig-wave-particle-duality-9
:alt: compton
:width: 400px

Demonstration of the uncertainty principle. As the electron's position is localized by narrowing the slit, its momentum becomes more unpredictable, so the electrons hit the detector over a wider range.
:::


- Mathematically, the uncertainty relation is expressed in terms of the standard deviations of position $\sigma_x$ and momentum $\sigma_p$, which are obtained by repeating the experiment, measuring positions and momenta, and quantifying the spread via the standard deviation.

:::{important} **Heisenberg's uncertainty principle**

$$
\sigma_x \sigma_p \geq \hbar/2
$$

:::

### Problems

#### Problem 1: Electrons in an electron microscope

Estimate the wavelength of electrons that have been accelerated from
rest through a potential difference of $V = 40 kV$. 
- Note that the potential energy difference the electrons experience is simply $e×V$, where $e$ is the magnitude of the electron charge and $V$ is the potential difference.

:::{admonition} **Solution**
:class: dropdown solution

In order to calculate the de Broglie wavelength, we need to calculate the linear momentum of the electrons.
At the end of the acceleration, all the acquired energy is in the form of kinetic energy ($p^2 / 2m_e$).

$$
\frac{p^2}{2m_e} = eV \Rightarrow p = {\sqrt{2m_eeV}}
$$

$$
{\lambda = \frac{h}{p} = \frac{h}{\sqrt{2m_eeV}}}{= \frac{6.626\times 10^{-34}{ Js}}{\sqrt{2\times (9.109\times 10^{-31} { kg})\times (1.602\times 10^{-19} { C})\times (4.0\times 10^4 { V})}}}{ = 6.1\times 10^{-12}}\, m
$$
:::

#### Problem 2: Your own de Broglie wavelength

If you considered yourself a particle moving at $2 m/s$, what would your de Broglie wavelength be?
Would it make sense to use quantum mechanics in this case?

:::{admonition} **Solution**
:class: dropdown solution

- A. If you consider yourself a particle moving at $2 \, {m/s}$, we can calculate your de Broglie wavelength using the de Broglie relation:

$$
\lambda = \frac{h}{p}
$$

where $h$ is Planck's constant, $6.626 \times 10^{-34} \, {J·s}$, and $p$ is the momentum of the object. The momentum is given by:

$$
p = mv
$$

where $m$ is your mass and $v = 2 \, {m/s}$ is your velocity. Assuming your mass is $70 \, {kg}$, the momentum would be:

$$
p = 70 \, {kg} \times 2 \, {m/s} = 140 \, {kg·m/s}
$$

Now, plugging the values into the de Broglie relation:

$$
\lambda = \frac{6.626 \times 10^{-34} \, {J·s}}{140 \, {kg·m/s}} \approx 4.73 \times 10^{-36} \, {m}
$$

- B. This wavelength is extremely small, much smaller than the scale at which quantum effects become noticeable. In this case, it wouldn't make sense to use quantum mechanics, as classical mechanics is sufficient for describing the behavior of macroscopic objects like a person.


:::

#### Problem 3: Position uncertainty in the Bohr atom

Quantify the uncertainty in the position of an electron in the ground state of the H atom using Bohr's model.

:::{admonition} **Solution**
:class: dropdown solution

To quantify the uncertainty in the position of an electron in the ground state of a hydrogen atom using Bohr's model, we begin by recalling that the electron orbits the nucleus at a distance equal to the Bohr radius $a_0$ in the ground state. The Bohr radius is given by:

$$
a_0 = \frac{4 \pi \varepsilon_0 \hbar^2}{m_e e^2}
$$

where:

- $\varepsilon_0 = 8.854 \times 10^{-12} \, {F/m}$ (permittivity of free space),
- $\hbar = 1.055 \times 10^{-34} \, {J·s}$ (reduced Planck’s constant),
- $m_e = 9.109 \times 10^{-31} \, {kg}$ (mass of the electron),
- $e = 1.602 \times 10^{-19} \, {C}$ (elementary charge).

Substituting these values, we can calculate the Bohr radius:

$$
a_0 = \frac{4 \pi (8.854 \times 10^{-12}) (1.055 \times 10^{-34})^2}{(9.109 \times 10^{-31}) (1.602 \times 10^{-19})^2} \approx 5.29 \times 10^{-11} \, {m}
$$

Now, Bohr's model treats the electron as orbiting at this radius with a known trajectory. However, quantum mechanics introduces the Heisenberg uncertainty principle, which relates the uncertainties in position and momentum:

$$
\Delta x \Delta p \geq \frac{\hbar}{2}
$$

In the ground state, the uncertainty in momentum can be estimated from the momentum of the electron. The momentum $p$ of the electron in the Bohr model is related to the velocity $v$ and the mass $m_e$:

$$
p = m_e v
$$

Using the fact that the electron in the ground state has a velocity $v \approx \frac{e^2}{4 \pi \varepsilon_0 \hbar} \approx 2.18 \times 10^6 \, {m/s}$, we can calculate the momentum:

$$
p = (9.109 \times 10^{-31} \, {kg}) (2.18 \times 10^6 \, {m/s}) \approx 1.99 \times 10^{-24} \, {kg·m/s}
$$

Now, using the uncertainty relation:

$$
\Delta x \geq \frac{\hbar}{2 \Delta p}
$$

Substituting $\Delta p \approx p$, we get:

$$
\Delta x \geq \frac{1.055 \times 10^{-34} \, {J·s}}{2 (1.99 \times 10^{-24} \, {kg·m/s})} \approx 2.65 \times 10^{-11} \, {m}
$$

Thus, the uncertainty in the position of the electron in the ground state of a hydrogen atom is approximately $2.65 \times 10^{-11} \, {m}$, which is on the order of the Bohr radius.

This result suggests that the electron’s position is spread out over a region approximately the size of the atom, supporting the idea that the electron in an atom cannot be described as a classical particle with a well-defined position.

:::

#### Problem 4: Position uncertainty of a free electron

Quantify the uncertainty in the position of an electron traveling freely with a kinetic energy of $3 eV$.

:::{admonition} **Solution**
:class: dropdown solution

To quantify the uncertainty in the position of an electron traveling freely with a kinetic energy of 3 eV, we can use the Heisenberg uncertainty principle:

$$
\Delta x \Delta p \geq \frac{\hbar}{2}
$$

First, we need to calculate the momentum of the electron. The kinetic energy is related to the momentum by the equation:

$$
K = \frac{p^2}{2m_e}
$$

where:
- $K = 3 \, {eV} = 3 \times 1.602 \times 10^{-19} \, {J} = 4.806 \times 10^{-19} \, {J}$ (since $1 \, {eV} = 1.602 \times 10^{-19} \, {J}$),
- $m_e = 9.109 \times 10^{-31} \, {kg}$ is the mass of the electron.

Rearranging for momentum:

$$
p = \sqrt{2 m_e K}
$$

Substituting the values:

$$
p = \sqrt{2 \times 9.109 \times 10^{-31} \, {kg} \times 4.806 \times 10^{-19} \, {J}}
$$

$$
p \approx 1.176 \times 10^{-24} \, {kg·m/s}
$$

Now, using the Heisenberg uncertainty principle:

$$
\Delta x \geq \frac{\hbar}{2 \Delta p}
$$

Assuming $\Delta p \approx p$, we substitute the values:

$$
\Delta x \geq \frac{1.055 \times 10^{-34} \, {J·s}}{2 \times 1.176 \times 10^{-24} \, {kg·m/s}}
$$

$$
\Delta x \geq 4.48 \times 10^{-11} \, \text{m}
$$

Thus, the uncertainty in the position of the electron traveling with a kinetic energy of 3 eV is approximately $4.48 \times 10^{-11}$ meters.

This is on the order of atomic scales, which indicates that quantum effects are relevant in this case.

:::

#### Problem 5: Compton shift

X-rays from a molybdenum source ($\lambda = 71.1$ pm) scatter off electrons in a graphite target. Compute the wavelength of the photons scattered at 90 degrees and at 180 degrees. What fraction of the photon energy is handed to the electron in the 180 degree case? Explain why the Compton shift is unobservable with visible light.

#### Problem 6: Thermal neutrons see atoms

Neutrons in equilibrium with a moderator at 300 K have an average kinetic energy of $\tfrac{3}{2}k_BT$. Compute their de Broglie wavelength ($m_n = 1.675 \times 10^{-27}$ kg) and compare it with a typical spacing of atoms in a crystal, about 0.2 nm. Explain why neutron diffraction is used to locate hydrogen atoms in crystals when X-ray diffraction struggles.

#### Problem 7: Are helium atoms waves?

A beam of helium atoms leaves a nozzle at 300 K with a speed of about 1750 m/s. Compute the de Broglie wavelength of the atoms. In 1930 Estermann and Stern diffracted such a beam from a LiF crystal surface. Of the objects met so far (electron, X-ray photon, neutron, helium atom, a walking person), which show diffraction in practice, and what single quantity decides it?

#### Problem 8: Confinement costs energy

An electron is confined to a region the size of an atom, $\Delta x \approx 0.1$ nm. (a) Use the uncertainty relation to find the minimum spread in momentum. (b) Taking $p \sim \Delta p$, estimate the electron's kinetic energy in eV. (c) Repeat for a proton confined to a nucleus, $\Delta x \approx 10^{-15}$ m, and give the result in MeV. What does the comparison say about the energy scales of chemistry versus nuclear physics?

:::{seealso} Chapter demos
Run this chapter's interactive Python demos: [Python Calculator](../demos/06-python-calculator.md)
:::
