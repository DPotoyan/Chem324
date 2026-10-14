---
kernelspec:
  name: python3
  display_name: Python 3
---
# Atomic spectra

:::{note} **What you will learn**

- Excited atoms emit light only at **discrete wavelengths**. Each element has its own line spectrum, an atomic fingerprint that classical physics cannot explain.
- The hydrogen lines are captured by the empirical **Rydberg formula**, $\tilde{\nu} = R_H(1/n_1^2 - 1/n_2^2)$, whose integers $n_1, n_2$ hinted that something in the atom is quantized.
- **Bohr's model** (1913) adds one quantum rule to classical orbits, angular momentum in units of $\hbar$, and from it derives the orbit radii $r_n = n^2 a_0$, the energy levels $E_n = -13.6\,\text{eV}/n^2$, and the Rydberg constant from fundamental constants.
- Spectral lines are **transitions between energy levels**: a photon carries away exactly the energy difference, $h\nu = E_{n_2} - E_{n_1}$. The same formulas work for any one-electron ion once the nuclear charge $Z$ is included.
- Bohr's model nonetheless **fails** past hydrogen: no helium, no line intensities, no fine structure, and an orbit that the uncertainty principle forbids. Keep the quantization, discard the orbit.
:::


### Spectroscopy of Atoms


- **Spectroscopy** is the study of the interaction between matter and electromagnetic radiation.  
- By analyzing the emitted or absorbed light, spectroscopy reveals information about the **structure and composition** of atoms and molecules.  
- When heated or subjected to electrical discharge, atoms emit radiation at characteristic frequencies. The resulting spectrum is **unique for each element**, serving as a kind of atomic fingerprint.  


:::{figure} images/lec1_AtomicSpectrum.png
:label: fig-atomic-spectra-1
:alt: Hydrogen atomic spectrum
:width: 70%

**Atomic spectroscopy of the hydrogen atom.**  
Hydrogen in a gas-discharge tube emits light at discrete wavelengths, which appear as distinct spectral lines when passed through a prism.
:::

Every element produces its own set of lines. Below is what a spectrograph records from a
discharge lamp of each gas: no two patterns are alike, which is why a spectrum taken through
a telescope tells you what a star is made of.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

def wl_to_rgb(wl):
    """Approximate sRGB colour of a single wavelength in nm."""
    if wl < 440:    r, g, b = -(wl - 440) / 60, 0.0, 1.0
    elif wl < 490:  r, g, b = 0.0, (wl - 440) / 50, 1.0
    elif wl < 510:  r, g, b = 0.0, 1.0, -(wl - 510) / 20
    elif wl < 580:  r, g, b = (wl - 510) / 70, 1.0, 0.0
    elif wl < 645:  r, g, b = 1.0, -(wl - 645) / 65, 0.0
    else:           r, g, b = 1.0, 0.0, 0.0
    return (min(r, 1.0), min(g, 1.0), min(b, 1.0))

# (wavelength in nm, relative brightness) for the strong visible lines
spectra = {
    "H":  [(656.3, 1.0), (486.1, 0.6), (434.0, 0.4), (410.2, 0.3)],
    "He": [(447.1, 0.5), (471.3, 0.3), (492.2, 0.3), (501.6, 0.6),
           (587.6, 1.0), (667.8, 0.5), (706.5, 0.4)],
    "Na": [(498.3, 0.2), (568.8, 0.3), (589.0, 1.0), (589.6, 1.0), (615.4, 0.3)],
    "Hg": [(404.7, 0.6), (435.8, 1.0), (546.1, 1.0), (577.0, 0.6), (579.1, 0.6)],
    "Ne": [(585.2, 0.8), (588.2, 0.6), (594.5, 0.7), (607.4, 0.5), (614.3, 0.7),
           (621.7, 0.5), (626.6, 0.6), (633.4, 0.8), (640.2, 1.0), (650.7, 0.6),
           (659.9, 0.5), (692.9, 0.4), (703.2, 0.5)],
}

fig, axes = plt.subplots(len(spectra), 1, figsize=(9, 4.0), sharex=True)
for ax, (name, lines) in zip(axes, spectra.items()):
    ax.set_facecolor("black")
    for wl, intensity in lines:
        ax.axvline(wl, color=wl_to_rgb(wl), lw=1.8, alpha=0.35 + 0.65 * intensity)
    ax.set_yticks([])
    ax.set_ylabel(name, rotation=0, ha="right", va="center", fontsize=12, labelpad=14)
    for spine in ax.spines.values():
        spine.set_visible(False)
axes[-1].set_xlim(380, 750)
axes[-1].set_xlabel("wavelength (nm)")
fig.suptitle("Fig. Visible emission lines of five elements. Each element has its own fingerprint.",
             fontsize=10)
fig.tight_layout()
```

:::{figure} images/spectra.png
:label: fig-atomic-spectra-2
:alt: Solar spectra
:width: 70%

**Spectroscopy of the Sun.**  
By analyzing spectral lines, one can identify the presence of different elements in the solar atmosphere.  
:::


### Spectral lines and Rydberg's formula

- The existence of discrete spectral lines is impossible to describe with classical mechanics.  In 1885, Johann Balmer demonstrated that a subset of the hydrogen atom spectrum (the Balmer series) could be described by the equation

$$\lambda = B\,\frac{n^2}{n^2-4}, \qquad B = 364.6\ \text{nm}$$

where $n=3,4,5,...$. Written in terms of the wavenumber $\tilde{\nu} = 1/\lambda$ this is $\tilde{\nu} = \frac{4}{B}\left(\frac{1}{2^2}-\frac{1}{n^2}\right)$ with $4/B = 1.097\times10^{7}\ \text{m}^{-1}$.  Later, Johannes Rydberg generalized this formula to account for the entire hydrogen atom spectrum yielding the Rydberg formula

:::{important} **Rydberg formula**


$$\tilde{\nu} = R_H\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right)$$

where 
- $R_H = 1.097 \times 10^7 \ \text{m}^{-1}$ is the Rydberg constant.
- $n_1 = 1,2,3,...$, and $n_2 = n_1+1,n_1+2,...$.  

:::

- While these equations fit the hydrogen atom spectrum nicely, they do not prescribe any physics to the system.  They do not present a model of the hydrogen atom but rather a heuristic equation that fits the data.  Nonetheless, scientists were perplexed by the presence of the integers $n_1$ and $n_2$. 


:::{figure} images/bohr_series_orbits.png
:label: fig-atomic-spectra-3
:alt: atomic series
:width: 30%

Atomic spectral lines are named after their discoverers. Each series contains all transitions to a distinct lower level $n=1,2,3$.
:::


### Bohr's Model of the Hydrogen Atom

:::{figure} images/evolution_atom.png
:label: fig-atomic-spectra-4
:alt: Evolution of atomic models
:width: 70%

**Evolution of atomic models.**  
From pre-quantum pictures of atoms to the modern quantum mechanical description.  
:::

- In 1913, Niels Bohr proposed a model of the hydrogen atom that successfully explained its **discrete emission spectrum**.  
- The atom was pictured as an electron moving in **circular orbits** around a central proton. Because the proton is far more massive than the electron, it was treated as fixed in space.  
- To prevent the electron from spiraling into the nucleus, Bohr introduced a new **quantization rule**: the electron’s orbital motion must accommodate an integer number of standing wave modes, $n = 1, 2, 3, \ldots$  
- This postulate leads directly to an expression for the allowed **energy levels of hydrogen**, each labeled by a principal quantum number $n$.  

:::{figure} images/bohring.png
:label: fig-atomic-spectra-5
:alt: Niels Bohr horseshoe anecdote
:width: 20%

**Anecdote about Niels Bohr.**  
A visitor once noticed a horseshoe (a Scandinavian good-luck charm) hanging above Bohr’s door:  

*"But Niels, you are a scientist! Surely you don’t believe in this superstition?"*  

*"Of course I don’t,"* Bohr replied. *"But I am told it works even if you don’t believe in it!"*  
:::


### Quantizing the States of the Electron in the Hydrogen Atom

:::{figure} images/bohr_standing_waves.png
:label: fig-atomic-spectra-6
:alt: Quantized orbits of the electron
:width: 60%

Bohr rationalized discrete orbits by requiring that an integer number of electron wavelengths fit around the circumference of each orbit: four waves close on themselves (a), four and a half do not (b).
:::

- Imposing this condition gives the relation  

$$
2\pi r = n \lambda_e, \quad n = 1, 2, 3, \ldots
$$

- Here, $\lambda_e$ is the **de Broglie wavelength** of the electron:  

$$
\lambda_e = \frac{h}{m_e v}.
$$

- Substituting this expression for $\lambda_e$ into the quantization condition yields  

$$
m_e v r = \frac{n h}{2\pi} = n \hbar.
$$

- We introduce the shorthand $\hbar = \tfrac{h}{2\pi}$ because it appears frequently in quantum mechanics. The left-hand side, $m_e v r$, represents the **angular momentum** of the electron.  
- Thus, Bohr’s model predicts that the electron’s angular momentum is **quantized** in integer multiples of $\hbar$.  

:::{note} **A word on history**

Bohr's 1913 paper contains no de Broglie waves, because matter waves were still eleven
years away. Bohr simply postulated that angular momentum comes in whole units of $\hbar$
and defended the postulate by showing it reproduces classical physics for very large
orbits. The standing-wave picture above is de Broglie's 1924 reading of the same rule, and
it is the one worth remembering: confinement plus waves gives quantization, here and
everywhere else in this course.
:::


### Force Balance

After introducing his quantization rule, Bohr turned back to **classical mechanics** to determine the allowed electron energies. He assumed that, in a stationary orbit, the **electrostatic attraction** between the proton and electron is exactly balanced by the **centrifugal force** of the orbiting electron.  

**Electrostatic force**  

$$
f_{\text{el}} = \frac{e^2}{4\pi\varepsilon_0 r^2},
$$  

where $e$ is the elementary charge and the factor $4\pi \varepsilon_0$ ensures SI units.  

**Centrifugal force**  

$$
f_{\text{cf}} = \frac{m_e v^2}{r},
$$  

where $m_e$ is the electron mass and $v$ its orbital velocity.  

Equating these two forces gives  

$$
\frac{e^2}{4\pi\varepsilon_0 r^2} = \frac{m_e v^2}{r}.
$$  

:::{warning} **Careful: the centrifugal force is fictitious**

In the laboratory frame there is only one force on the electron, the Coulomb pull, and it
is unbalanced: it supplies the **centripetal acceleration** $a = v^2/r$ that keeps bending
the velocity into a circle. The **centrifugal force** appears only when you ride along with
the electron, in the rotating frame, where it exactly cancels the Coulomb pull and the
electron sits still. Both bookkeepings give the same equation above, which is why Bohr
could write it either way.
:::

::::{admonition} **Watch it move: position, velocity and acceleration on a circular orbit**
:class: dropdown tip

The three vectors keep constant length and only turn. The velocity is always tangent, the
acceleration always points at the nucleus, and the centrifugal arrow is its mirror image in
the rotating frame. The right panel is worth remembering for later: each component of
circular motion is simple harmonic motion, with $v_x$ a quarter cycle ahead of $x$ and
$a_x$ exactly opposite to it. The same machinery returns for angular momentum in Chapter 4
and the rigid rotor in Chapter 5.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE = "#107895", "#C8102E", "#6c757d", "#6a3d9a"
R2, N_FR, OM = 1.0, 72, 1.0           # radius, frames, angular velocity
SV, SA = 0.62, 0.48                   # arrow scale factors
th_seq = np.linspace(0, 2 * np.pi, N_FR, endpoint=False)

fig_cm, (cx, dx) = plt.subplots(1, 2, figsize=(10.4, 4.5),
                                gridspec_kw={"width_ratios": [1.15, 1.2]})

cx.add_patch(Circle((0, 0), R2, fill=False, color=GRAY, lw=1.2, ls="--"))
cx.plot(0, 0, "o", color=CARDINAL, ms=11)
cx.text(0.10, -0.22, "nucleus", color=CARDINAL, fontsize=8)
(bead,) = cx.plot([], [], "o", color="k", ms=9, zorder=6)

def arrow(color, ls="-", lw=2.2):
    return cx.annotate("", xy=(0, 0), xytext=(0, 0), zorder=5,
                       arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                       ls=ls, shrinkA=0, shrinkB=0))

a_r, a_v, a_a, a_cf = arrow(GRAY, lw=1.3), arrow(TEAL), arrow(PURPLE), arrow(CARDINAL, "--")
a_r.arrow_patch.set_alpha(0.45)
cx.set_xlim(-1.75, 1.75)
cx.set_ylim(-1.6, 1.6)
cx.set_aspect("equal")
cx.axis("off")
cx.legend(handles=[plt.Line2D([], [], color=GRAY, lw=1.3, alpha=0.45, label=r"$\vec{r}$  position"),
                   plt.Line2D([], [], color=TEAL, lw=2.2, label=r"$\vec{v}$  velocity (tangent)"),
                   plt.Line2D([], [], color=PURPLE, lw=2.2, label=r"$\vec{a}$  centripetal (inward)"),
                   plt.Line2D([], [], color=CARDINAL, lw=2.2, ls="--",
                              label="centrifugal (rotating frame)")],
          loc="lower center", bbox_to_anchor=(0.5, -0.16), fontsize=7.5, frameon=False)

t_full = th_seq / OM
dx.plot(t_full, R2 * np.cos(th_seq), color=GRAY, lw=1.6, label=r"$x = R\cos\omega t$")
dx.plot(t_full, -OM * R2 * np.sin(th_seq), color=TEAL, lw=1.6, label=r"$v_x = -\omega R\sin\omega t$")
dx.plot(t_full, -OM**2 * R2 * np.cos(th_seq), color=PURPLE, lw=1.6,
        label=r"$a_x = -\omega^2 R\cos\omega t$")
sweep = dx.axvline(0, color="k", lw=0.9, alpha=0.45)
(m_x,) = dx.plot([], [], "o", color=GRAY, ms=7)
(m_v,) = dx.plot([], [], "o", color=TEAL, ms=7)
(m_a,) = dx.plot([], [], "o", color=PURPLE, ms=7)
dx.axhline(0, color="k", lw=0.6, alpha=0.3)
dx.set_xlim(0, t_full[-1])
dx.set_ylim(-1.5, 1.9)
dx.set_xlabel("time")
dx.set_yticks([])
dx.legend(loc="upper right", fontsize=7.5, frameon=False)
dx.set_title("each component is simple harmonic motion", fontsize=9)
for sp in ("top", "right", "left"):
    dx.spines[sp].set_visible(False)

fig_cm.suptitle("Fig. Circular motion: position, velocity and centripetal acceleration.\n"
                "The magnitudes never change, only the directions.", fontsize=10)
fig_cm.tight_layout()

def frame_cm(i):
    th = th_seq[i]
    p = np.array([R2 * np.cos(th), R2 * np.sin(th)])
    rhat, that = p / R2, np.array([-np.sin(th), np.cos(th)])
    bead.set_data([p[0]], [p[1]])
    a_r.xy = p
    a_r.set_position((0, 0))
    a_v.xy = p + SV * OM * R2 * that
    a_v.set_position(p)
    a_a.xy = p - SA * OM**2 * R2 * rhat
    a_a.set_position(p)
    a_cf.xy = p + SA * OM**2 * R2 * rhat
    a_cf.set_position(p)
    sweep.set_xdata([t_full[i], t_full[i]])
    m_x.set_data([t_full[i]], [p[0]])
    m_v.set_data([t_full[i]], [-OM * R2 * np.sin(th)])
    m_a.set_data([t_full[i]], [-OM**2 * R2 * np.cos(th)])
    return bead, a_r, a_v, a_a, a_cf, sweep, m_x, m_v, m_a

ani_cm = FuncAnimation(fig_cm, frame_cm, frames=N_FR, interval=50, blit=False)
plt.close(fig_cm)
HTML(ani_cm.to_jshtml())
```
::::

---

The **force-balance equation** together with the **quantized angular momentum condition** restricts the allowed radii $r$ of electron orbits. Solving step by step:  

1. From angular momentum quantization:  

   $$
   m_e v r = n\hbar \quad \Rightarrow \quad v = \frac{n\hbar}{m_e r}.
   $$  

2. Substituting into the force-balance equation:  

   $$
   \frac{e^2}{4\pi\varepsilon_0 r^2} = \frac{m_e}{r} \left( \frac{n\hbar}{m_e r} \right)^2.
   $$  

3. Simplifying:  

   $$
   \frac{e^2}{4\pi\varepsilon_0} = \frac{(n\hbar)^2}{m_e r}.
   $$  

4. Solving for $r$:  

   $$
   r = \frac{4\pi \varepsilon_0 (n\hbar)^2}{m_e e^2} = n^2 a_0, \quad n = 1, 2, 3, \ldots
   $$  

- where the constant $a_0$ is the **Bohr radius**, corresponding to the size of the ground-state orbit.  
- We see clearly that the radius of an orbit grows with increasing quantum number $n=1,2,3$.


:::{tip} **Bohr radius**

$$
a_0 = \frac{4\pi \varepsilon_0 \hbar^2}{m_e e^2}
$$  

$$a_0 \approx 0.529 \,\text{Å}$$

- We will encounter the Bohr radius many times. It sets the fundamental length scale for atomic physics!
:::


### Energy of the Hydrogen Atom

The total energy of the electron-proton system is the sum of the electron’s **kinetic energy** and the **Coulomb potential energy**:  

$$
E(r) = \tfrac{1}{2} m_e v^2 - \frac{e^2}{4\pi\varepsilon_0 r}.
$$  

Using the force-balance relation  

$$
m_e v^2 = \frac{e^2}{4\pi\varepsilon_0 r},
$$  

we substitute into the energy expression:  

$$
\begin{align}
E(r) &= \tfrac{1}{2}\frac{e^2}{4\pi\varepsilon_0 r} - \frac{e^2}{4\pi\varepsilon_0 r} \\
     &= -\tfrac{1}{2}\frac{e^2}{4\pi\varepsilon_0 r}.
\end{align}
$$  

Next, inserting the quantized orbital radius  

$$
r = \frac{4\pi \varepsilon_0 (n\hbar)^2}{m_e e^2},
$$  

gives the **Bohr energy levels**:  

$$
E_n = -\frac{m_e e^4}{8 \varepsilon_0^2 h^2} \cdot \frac{1}{n^2}, 
\quad n = 1, 2, 3, \ldots
$$  


:::{important} **Bohr Energy formula**

$$
E_n = -13.6\frac{ 1}{n^2} \,\,\,[eV]
$$  

- This is the most useful form for problem solving. You can quickly compute the energy of any hydrogenic level just by inserting the principal quantum number $n$.  

- Ionization energy corresponds to taking the electron from $n=1$ to $n \to \infty$, requiring exactly 13.6 eV.  

- You can compute the energy (or frequency) of the photon for a jump from state $n$ to $m$ by taking the difference between energy levels: $\Delta E_{n\rightarrow m} = 13.6\,(1/m^2-1/n^2)\,\text{eV} = h\nu$ for an emission from a higher level $n$ down to a lower level $m$  

:::



### Spectral lines and the Rydberg constant  

The energy difference between two levels $n_1$ and $n_2$ is  

$$
\Delta E = \frac{m_e e^4}{8 \varepsilon_0^2 h^2}
\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right).
$$  

Relating this to photon energy $E = h\nu$ and the wavenumber $\tilde{\nu} = \nu/c$ gives  

$$
\tilde{\nu} = \frac{m_e e^4}{8 \varepsilon_0^2 c h^3}
\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
= R_H \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right),
$$  

where $R_H$ is the **Rydberg constant**, which we now know expressed in fundamental constants rather than obtained as the result of an experimental fit!

$$
R_H = \frac{m_e e^4}{8 \varepsilon_0^2 c h^3}
$$  

:::{figure} images/hydrogen_levels_series.png
:label: fig-atomic-spectra-7
:alt: Hydrogen energy levels with Lyman, Balmer and Paschen transitions
:width: 75%

Fig. Hydrogen energy levels and the three lowest spectral series. Every series shares one
lower level, and the lines of a series crowd together as $n_2$ grows, converging on the
series limit where the electron is set free.
:::


:::{tip} **A note about wavenumbers and $cm^{-1}$ units**

- Wavenumbers $\tilde{\nu}$ in **cm⁻¹** are standard in spectroscopy.  
- To convert to wavelength: $\lambda = 1 / \tilde{\nu}$ (with $\tilde{\nu}$ in cm⁻¹, $\lambda$ will come out in cm).  


$$
\tilde{\nu}\ \text{(cm}^{-1}\text{)} 
= R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right),
\quad n_2 > n_1,
$$  

- $R_H = 1.097 \times 10^5 \ \text{cm}^{-1}$ is the Rydberg constant in spectroscopic units.
:::

### Hydrogen-like atoms

- For one-electron atoms such as $He^{+}$ and $Li^{2+}$, the Bohr model still works, but we have to account for the increased nuclear charge $Z$.

$$
E_n = -13.6 \frac{Z^2}{n^2}, [eV]
$$

- E.g. for the $H$ atom $Z=1$, for $He^{+}$ $Z=2$, etc.

### Explore the hydrogen spectrum

Every spectral series is the set of transitions that end on one lower level. Slide $n_1$ to move from the Lyman series (ultraviolet) through Balmer (the visible lines of a hydrogen lamp) to Paschen and Brackett (infrared). Raise $Z$ to see how a one-electron ion like $He^+$ pulls all levels down by $Z^2$ and pushes every line to shorter wavelengths.

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

n_low = mo.ui.slider(1, 4, step=1, value=2, show_value=True, label="lower level n1")
Z_h = mo.ui.slider(1, 3, step=1, value=1, show_value=True, label="nuclear charge Z")
mo.vstack([n_low, Z_h])
```

```{marimo} python
:hide-code: true

E_ry = 13.6
n1_h, Z1 = n_low.value, Z_h.value
levels_h = np.arange(1, 9)
E_h = -E_ry * Z1**2 / levels_h**2
series_names = {1: "Lyman", 2: "Balmer", 3: "Paschen", 4: "Brackett"}
def wl_color(w):                       # true colour of a line, grey outside the visible
    if w < 380 or w > 750: return "#8c8c8c"
    if w < 440: return "#7b2fbe"
    if w < 490: return "#2b6fd6"
    if w < 510: return "#12b5a6"
    if w < 580: return "#3aa93a"
    if w < 645: return "#e0a521"
    return "#C8102E"
fig4, (axL, axR) = plt.subplots(1, 2, figsize=(9, 3.8), gridspec_kw={"width_ratios": [1, 1.4]})
for n_i, E_i in zip(levels_h, E_h):
    axL.hlines(E_i, 0, 1, color="C3" if n_i == n1_h else "k", lw=1.6)
    if n_i <= 3:
        axL.text(1.03, E_i, f"n = {n_i}", va="center", fontsize=8)
axL.hlines(0, 0, 1, color="gray", ls="--", lw=1)
axL.text(1.03, 0, "n = ∞", va="center", fontsize=8, color="gray")
lam_lines = []
for k_i, n2_i in enumerate(range(n1_h + 1, n1_h + 7)):
    dE_i = E_ry * Z1**2 * (1 / n1_h**2 - 1 / n2_i**2)
    lam_lines.append(1239.84 / dE_i)
    c_i = wl_color(lam_lines[-1])
    x_i = 0.12 + 0.13 * k_i
    axL.annotate("", xy=(x_i, E_h[n1_h - 1]), xytext=(x_i, -E_ry * Z1**2 / n2_i**2),
                 arrowprops=dict(arrowstyle="->", color=c_i, lw=1.3))
    axR.axvline(lam_lines[-1], color=c_i, lw=2)
axL.set_xlim(0, 1.5)
axL.set_ylim(E_h[0] * 1.08, 0.08 * E_ry * Z1**2)
axL.set_xticks([])
axL.set_ylabel("energy (eV)")
axR.axvspan(380, 750, color="gold", alpha=0.15)
axR.set_title("shaded band: visible light", fontsize=8, color="darkgoldenrod")
axR.set_xscale("log")
axR.set_xlim(10, 5000)
axR.set_yticks([])
axR.set_xlabel("wavelength (nm), log scale")
fig4.suptitle(f"Fig. {series_names[n1_h]} series for Z = {Z1}, lines from {lam_lines[-1]:.0f} nm to {lam_lines[0]:.0f} nm", fontsize=10)
fig4.tight_layout()
fig4
```

### Where Bohr's model breaks down

Bohr's model reproduces the hydrogen spectrum to four digits, and that success is exactly
why its failures matter. Within a decade it was clear that the model was a lucky halfway
house rather than the final theory.

- **It fails for every atom with more than one electron.** Applied to neutral helium it
  misses the measured ionization energy of 24.6 eV badly, and it says nothing at all about
  the periodic table.
- **It predicts where lines are but not how bright.** Real spectra have strong lines, weak
  lines, and transitions that never appear at all. Bohr's rules give no intensities and no
  selection rules.
- **It cannot see fine structure.** At high resolution each Balmer line splits into closely
  spaced components, and a magnetic field splits them further (the Zeeman effect). A single
  quantum number $n$ has no room for this.
- **It assumes an orbit at all.** A definite radius together with a definite speed violates
  the uncertainty principle from the previous lecture. The ground state of hydrogen in fact
  has zero orbital angular momentum, not $\hbar$.

What survives is the physics, not the picture: energies are quantized, the quantum number
is an integer, and light is emitted when the atom drops from one level to another. Chapter
5 replaces the orbit with a wavefunction and gets the levels right for the right reason,
Chapter 6 supplies the missing selection rules, and Chapter 7 takes on helium.

### Problems

#### Problem 1: Lyman alpha

The so-called Lyman series of lines in the emission spectrum of hydrogen corresponds to transitions from various excited states to the n = 1 orbit. Calculate the wavelength of the lowest-energy line in the Lyman series to three significant figures. In what region of the electromagnetic spectrum does it occur?

:::{admonition} **Solution**
:class: dropdown solution

**A** We can use the Rydberg equation  to calculate the wavelength for the Lyman series, $n_1 = 1$.

$$
\dfrac{1}{\lambda }=R_H \left ( \dfrac{1}{n_{1}^{2}} - \dfrac{1}{n_{2}^{2}}\right )
$$

The lowest energy results from a transition to or from the nearest energy level, hence $n_2 = n_1+1$.

$$
\begin{align*} \dfrac{1}{\lambda } &=R_H \left ( \dfrac{1}{n_{1}^{2}} - \dfrac{1}{n_{2}^{2}}\right ) \\[4pt] &=1.097 \times 10^{7}\, m^{-1}\left ( \dfrac{1}{1}-\dfrac{1}{4} \right )\\[4pt] &= 8.228 \times 10^{6}\; m^{-1} \end{align*}
$$


Spectroscopists often talk about energy and frequency as equivalent. The $cm^{-1}$ unit (wavenumbers) is particularly convenient. We can convert the answer in part A to $cm^{-1}$

$$
\begin{align*} \widetilde{\nu} &=\dfrac{1}{\lambda } \\[4pt] &= 8.228\times 10^{6}\cancel{m^{-1}}\left (\dfrac{\cancel{m}}{100\;cm} \right ) \\[4pt] &= 82,280\: cm^{-1} \end{align*}
$$

and

$$\lambda = 1.215 \times 10^{−7}\; m = 122 \,\,nm$$

This emission line is called Lyman alpha. It is the strongest atomic emission line from the Sun and drives the chemistry of the upper atmosphere of all the planets, producing ions by stripping electrons from atoms and molecules. It is completely absorbed by oxygen in the upper stratosphere, dissociating O2 molecules into O atoms, which react with other O2 molecules to form stratospheric ozone.

**B** This wavelength is in the UV region of the spectrum.
:::

#### Problem 2: Photon from n = 4 to n = 1

- A. Calculate the energy of a photon that is produced when an electron in a hydrogen atom goes from an orbit with $n=4$ to an orbit with $n=1$.
- B. What happens to the energy of the photon as the initial value of $n$ approaches infinity?


:::{admonition} **Solution**
:class: dropdown solution

**A.**  We will use Bohr's formula in electron volts, $E_n = -13.6 \frac{1}{n^2}$, to calculate the energy of a photon.

$$\Delta E = 13.6  \Big ( \frac{1}{1^2} - \frac{1}{4^2} \Big) = 13.6 \cdot 0.9375 = 12.75\,\, \text{eV}$$

**B.** The energy of the photon goes up as the electron starts from higher and higher levels, but it saturates. As $n \rightarrow \infty$ the photon energy approaches the ionization energy of hydrogen: $E = 13.6 \cdot \Big( \frac{1}{1^2} - \frac{1}{\infty} \Big) = 13.6\,\, \text{eV}$. Lines pile up against this limit, which is why each spectral series ends in a continuum.
:::

#### Problem 3: First lines of the Lyman series

Use Rydberg's formula to calculate the first few lines of the Lyman series ($n_1=1$).

:::{admonition} **Solution**
:class: dropdown solution
The Rydberg formula is given by:

$$
\frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)
$$

For the Lyman series, $n_1 = 1$, and $n_2 = 2, 3, 4, \dots$. The Rydberg constant for hydrogen is:

$$
R_H = 1.097 \times 10^7 \ \text{m}^{-1}
$$

**First few lines of the Lyman series:**

For $n_2 = 2$:

$$
\frac{1}{\lambda} = 1.097 \times 10^7 \left( \frac{1}{1^2} - \frac{1}{2^2} \right)
$$

$$
\lambda = 1.2157 \times 10^{-7} \ \text{m} = 121.57 \ \text{nm}
$$

For $n_2 = 3$:

$$
\frac{1}{\lambda} = 1.097 \times 10^7 \left( \frac{1}{1^2} - \frac{1}{3^2} \right)
$$

$$
\lambda = 1.0257 \times 10^{-7} \ \text{m} = 102.57 \ \text{nm}
$$

For $n_2 = 4$:

$$
\frac{1}{\lambda} = 1.097 \times 10^7 \left( \frac{1}{1^2} - \frac{1}{4^2} \right)
$$

$$
\lambda = 9.724 \times 10^{-8} \ \text{m} = 97.24 \ \text{nm}
$$

So, the first three wavelengths of the Lyman series are approximately $121.57$ nm, $102.57$ nm, and $97.24$ nm.


:::

#### Problem 4: Which level did the electron come from?

A line in the Lyman series of hydrogen has a wavelength of $1.03 \cdot 10^{-7} m$. Find the original level of the electron.

:::{admonition} **Solution**
:class: dropdown solution

We are given a wavelength $\lambda = 1.03 \times 10^{-7} \ \text{m}$ and asked to find the original level $n_2$ of the electron in the Lyman series (where $n_1 = 1$).

Using the Rydberg formula:

$$
\frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)
$$

For the Lyman series, $n_1 = 1$, so the equation becomes:

$$
\frac{1}{\lambda} = R_H \left( 1 - \frac{1}{n_2^2} \right)
$$

Rearranging to solve for $n_2$:

$$
\frac{1}{n_2^2} = 1 - \frac{1}{R_H \lambda}
$$

Substituting the values:

$$
R_H = 1.097 \times 10^7 \ \text{m}^{-1}
$$

$$
\frac{1}{n_2^2} = 1 - \frac{1}{(1.097 \times 10^7) \times (1.03 \times 10^{-7})}
$$

$$
\frac{1}{n_2^2} = 1 - \frac{1}{1.13091} = 1 - 0.884 = 0.116
$$

Now, solving for $n_2$:

$$
n_2^2 = \frac{1}{0.116} = 8.621
$$

$$
n_2 = \sqrt{8.621} \approx 2.94
$$

Since $n_2$ must be an integer, we round it to $n_2 = 3$.

Thus, the original level of the electron is $n_2 = 3$.


:::


#### Problem 5: Ionization energy of He+

Using Bohr theory calculate the ionization energy of singly ionized helium $He^{+}$.

:::{admonition} **Solution**
:class: dropdown solution

The ionization energy is the energy required to remove an electron from its ground state to infinity. Using Bohr's theory, the energy of an electron in an orbit is given by:

$$
E_n = -\frac{Z^2 E_{\text{Ry}}}{n^2}
$$

Where:
- $Z$ is the atomic number,
- $E_{\text{Ry}} = 13.6 \ \text{eV}$ is the Rydberg energy, the ionization energy of hydrogen (not to be confused with the Rydberg constant $R_H$ in $\text{m}^{-1}$, which is $E_{\text{Ry}}/hc$),
- $n$ is the principal quantum number.

For singly ionized helium $He^+$, the atomic number $Z = 2$. In the ground state, $n = 1$.

Thus, the energy in the ground state is:

$$
E_1 = -\frac{Z^2 E_{\text{Ry}}}{1^2} = -\frac{(2)^2 \times 13.6 \ \text{eV}}{1^2} = -4 \times 13.6 \ \text{eV} = -54.4 \ \text{eV}
$$

The ionization energy is the negative of this ground state energy (since we want to bring the electron to $n = \infty$):

$$
E_{\text{ionization}} = 54.4 \ \text{eV}
$$

Therefore, the ionization energy of singly ionized helium $He^+$ is $54.4 \ \text{eV}$.

:::

#### Problem 6: Bohr radii

- Calculate the radii of the Bohr orbits for the first few levels. 

- (Optional) Using python plot $r_n$ vs $n$

:::{admonition} **Solution**
:class: dropdown solution

The radius of the Bohr orbit is given by the formula:

$$
r_n = \frac{n^2 a_0}{Z}
$$

Where:
- $n$ is the principal quantum number (level),
- $a_0 = 5.29 \times 10^{-11} \ \text{m}$ is the Bohr radius for hydrogen,
- $Z$ is the atomic number (for hydrogen, $Z = 1$).

For hydrogen ($Z = 1$), the radii for the first few levels are:

**For $n = 1$:**
$$
r_1 = \frac{1^2 \times 5.29 \times 10^{-11} \ \text{m}}{1} = 5.29 \times 10^{-11} \ \text{m}
$$

**For $n = 2$:**
$$
r_2 = \frac{2^2 \times 5.29 \times 10^{-11} \ \text{m}}{1} = 4 \times 5.29 \times 10^{-11} \ \text{m} = 2.116 \times 10^{-10} \ \text{m}
$$

**For $n = 3$:**
$$
r_3 = \frac{3^2 \times 5.29 \times 10^{-11} \ \text{m}}{1} = 9 \times 5.29 \times 10^{-11} \ \text{m} = 4.761 \times 10^{-10} \ \text{m}
$$

**For $n = 4$:**
$$
r_4 = \frac{4^2 \times 5.29 \times 10^{-11} \ \text{m}}{1} = 16 \times 5.29 \times 10^{-11} \ \text{m} = 8.464 \times 10^{-10} \ \text{m}
$$

Therefore, the radii of the Bohr orbits for the first few levels are:
- $r_1 = 5.29 \times 10^{-11} \ \text{m}$,
- $r_2 = 2.116 \times 10^{-10} \ \text{m}$,
- $r_3 = 4.761 \times 10^{-10} \ \text{m}$,
- $r_4 = 8.464 \times 10^{-10} \ \text{m}$.

:::

#### Problem 7: The color of H-alpha

The brightest visible line of hydrogen, H-alpha, is the $n = 3 \to 2$ transition of the Balmer series. Compute its wavelength and name its color. Do the same for $n = 4 \to 2$ (H-beta). These two lines are what you see in a hydrogen discharge tube, and they give emission nebulae their red glow.

#### Problem 8: A coincidence between He+ and H

Show that the $n = 4 \to 2$ transition of $He^+$ emits a photon of exactly the same energy as the $n = 2 \to 1$ (Lyman alpha) transition of hydrogen. Find the general rule: which $He^+$ transitions coincide with hydrogen lines, and why?

#### Problem 9: How fast is the electron?

Using $m_e v r = n\hbar$ and $r = n^2 a_0$, find the speed of the electron in the ground state of hydrogen and express it as a fraction of the speed of light. This dimensionless ratio is the fine-structure constant $\alpha \approx 1/137$. What does it say about the need for relativity in hydrogen, and what happens to the innermost electron of uranium ($Z = 92$)?

#### Problem 10: The edge of a series

Every spectral series has a longest wavelength (its first line) and a shortest (the series limit, $n_2 \to \infty$). Compute both for the Paschen series ($n_1 = 3$). In which region of the electromagnetic spectrum do they fall, and can the Paschen lines ever overlap with the Balmer lines?
