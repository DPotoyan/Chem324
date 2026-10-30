---
kernelspec:
  name: python3
  display_name: Python 3
---

# Molecular Vibrations

:::{note} **What you need to know**

- An infrared spectrum measures the vibrational ladder of [Lecture 4.2](02-quantum-harmonic-oscillator.md). Spectroscopists write energies as wavenumbers, $G(v) = E_v/hc = \tilde{\nu}\left(v + \frac{1}{2}\right)$ with $\tilde{\nu} = \frac{1}{2\pi c}\sqrt{k/\mu}$, and a photon is absorbed when its wavenumber matches a gap.
- Light pushes on charges, so a vibration absorbs only if it changes the dipole moment: N$_2$ and O$_2$ are invisible in the infrared. A molecule absorbs through a superposition of two levels, whose dipole swings at the gap frequency with amplitude $\langle v'|\hat{M}|v\rangle$, the **transition dipole**. In the harmonic approximation that is nonzero only one rung at a time, $\Delta v = \pm 1$. At room temperature nearly every molecule starts in $v = 0$, so each vibration gives one strong line, the **fundamental**.
- The wavenumber reports stiffness and mass: bonds to hydrogen and triple bonds absorb high, heavy atoms and single bonds low. An isotope keeps $k$ and shifts the line by the square root of the mass ratio.
- Real bonds are anharmonic: $G(v) = \tilde{\nu}_e\left(v + \frac{1}{2}\right) - \tilde{\nu}_ex_e\left(v + \frac{1}{2}\right)^2$. The steps shrink, the bond can dissociate, and weak **overtones** ($\Delta v = 2, 3$) appear. Two measured lines are enough to find $\tilde{\nu}_e$ and $x_e$.
- A polyatomic molecule is a set of independent oscillators, one per normal mode. A mode absorbs only if its motion changes the dipole: the symmetric stretch of CO$_2$ is silent, its bend and antisymmetric stretch absorb, and that makes CO$_2$ a greenhouse gas. The modes themselves are the eigenvectors of the mass-weighted force-constant matrix, $F\mathbf{u} = \omega^2\mathbf{u}$.

:::

### From the ladder to a spectrum

[Lecture 4.2](02-quantum-harmonic-oscillator.md) found the vibrational levels of a bond, $E_v = \hbar\omega\left(v + \frac{1}{2}\right)$, evenly spaced by $\hbar\omega$. A molecule absorbs a photon when the photon energy $h\nu$ matches the gap between two levels. This lecture asks which gaps light can actually bridge, what the measured lines reveal about bonds, and how real molecules differ from the perfect spring.

#### Spectroscopists count in wavenumbers

Infrared spectra are plotted against the **wavenumber** $\tilde{\nu} = 1/\lambda$, the number of wavelengths per centimeter. It is proportional to the photon's energy and frequency:

$$
E = h\nu = \frac{hc}{\lambda} = hc\,\tilde{\nu}
$$

So any energy divided by $hc$ becomes a wavenumber. For the oscillator, with $\hbar\omega = hc\,\tilde{\nu}$:

:::{important} **The harmonic oscillator in wavenumbers**

$$
G(v) = \frac{E_v}{hc} = \tilde{\nu}\left(v + \frac{1}{2}\right), \qquad \tilde{\nu} = \frac{\omega}{2\pi c} = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}
$$

- $G(v)$ is the energy of level $v$ in cm$^{-1}$; $\mu$ is the reduced mass and $k$ the force constant
- A photon that lifts the bond from $v$ to $v + 1$ has wavenumber $G(v + 1) - G(v) = \tilde{\nu}$, the bond's own vibrational wavenumber
:::

- Mind the symbols: the italic $v$ is the quantum number, $\tilde{\nu}$ ("nu tilde") the wavenumber.
- What one wavenumber is worth:

| quantity | value | what it tells you |
|:--|:--|:--|
| 1 cm$^{-1}$ | $1.986\times10^{-23}$ J $= 1.240\times10^{-4}$ eV $= 0.01196$ kJ/mol | the conversion factor $hc$ |
| 1 eV | 8066 cm$^{-1}$ | a typical chemical-bond scale is a few eV |
| $k_BT$ at 300 K | 208 cm$^{-1}$ | below this, levels are thermally populated |
| bond vibrations | 200 to 4400 cm$^{-1}$ | wavelengths 2.3 to 50 μm: the infrared |

:::{note} **Example: the HCl line**

HCl absorbs strongly at $\tilde{\nu} = 2886$ cm$^{-1}$. Find the wavelength, the frequency and the photon energy, and compare the energy with $k_BT$ at room temperature.

- Wavelength: $\lambda = 1/\tilde{\nu} = 1/(2886\ \text{cm}^{-1}) = 3.47\times10^{-4}$ cm $= 3.47$ μm, in the infrared.
- Frequency: $\nu = c\tilde{\nu} = (2.998\times10^{10}\ \text{cm/s})(2886\ \text{cm}^{-1}) = 8.65\times10^{13}$ Hz, the number of times per second the bond stretches and compresses.
- Energy: $E = hc\tilde{\nu} = 0.358$ eV $= 34.5$ kJ/mol, about 14 times $k_BT$ (208 cm$^{-1}$).

The line sits a little below the harmonic wavenumber of HCl, 2990 cm$^{-1}$ ($\hbar\omega$ in Lecture 4.2). The difference is anharmonicity, later in this lecture.
:::

### Which transitions light can drive

Start with a puzzle. N$_2$ vibrates at 2330 cm$^{-1}$ and HCl at 2886 cm$^{-1}$. Both lie in the middle of the infrared, and both ladders have rungs spaced to match an infrared photon. Yet the air, mostly N$_2$, is transparent to that light, while HCl gas absorbs it strongly. Matching the photon to a gap is only the tuning. Something else decides whether the molecule can take the photon at all.

#### Light pushes on the dipole

Light is an oscillating electric field, written $\mathcal{E}$ here because $E$ is an energy. Its wavelength, a few micrometers, is about $3\times10^4$ times the length of the HCl bond. So the field is uniform across the molecule, and it does the one thing a uniform field can do: push positive charges one way and negative charges the other. It therefore couples to the **dipole moment** $M$, with energy $-M\mathcal{E}$. (Chemistry texts often write the dipole moment as $\mu$, but here $\mu$ is the reduced mass, and a lowercase $d$ would look like a differential.)

The dipole depends on the bond length: $M(x)$, with $x = R - R_e$ the stretch. The force the field exerts on the stretch is

$$
F = -\frac{d}{dx}\Big(-M(x)\,\mathcal{E}\Big) = M'(x)\,\mathcal{E}
$$

The field's handle on the bond is the **slope** of the dipole, not the dipole itself. A vibrating bond with $M' \neq 0$ is a tiny antenna: its dipole oscillates at the vibration frequency and couples to light at that frequency.

```{code-cell} python
:tags: [hide-input]
# synced: dipole_antenna
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
nf = 32
ts = np.arange(nf) / nf                                     # one loop of the animation = two vibrations
GREEN, BLUE = "#2f9e44", "#1c7ed6"
rows = [(("H", "Cl"), ("white", GREEN), (0.15, 0.29), (1.0, 35.0), True,
         "HCl: the dipole swings with the bond", r"$M(t) = M_e + M'x(t)$: the swing couples to light"),
        (("N", "N"), (BLUE, BLUE), (0.24, 0.24), (14.0, 14.0), False,
         r"N$_2$: symmetric, no dipole at any length", r"$M = 0$ always: light has nothing to push on")]
fig, axes = plt.subplots(2, 2, figsize=(9.6, 4.6), gridspec_kw={"width_ratios": [1, 1.2], "hspace": 0.65, "wspace": 0.12})
tt = np.linspace(0, 1, 300)
parts = []
for (ax, bx), (labels, cols, rads, masses, polar, t1, t2) in zip(axes, rows):
    ax.set_xlim(-1.5, 1.5); ax.set_ylim(-0.6, 1.0); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(t1, loc="left", fontsize=12)
    (bond,) = ax.plot([], [], color="#adb5bd", lw=6, solid_capstyle="round", zorder=2)
    c1 = Circle((0, 0), rads[0], fc=cols[0], ec="k", lw=1, zorder=3); ax.add_patch(c1)
    c2 = Circle((0, 0), rads[1], fc=cols[1], ec="k", lw=1, zorder=3); ax.add_patch(c2)
    l1 = ax.text(0, 0, labels[0], ha="center", va="center", fontsize=10, weight="bold", zorder=4,
                 color="k" if cols[0] == "white" else "white")
    l2 = ax.text(0, 0, labels[1], ha="center", va="center", fontsize=10, weight="bold", zorder=4, color="white")
    (bar,) = ax.plot([], [], color=ORANGE, lw=6, solid_capstyle="butt")
    if polar:
        ax.text(-0.62, -0.5, r"$\delta+$", ha="center", fontsize=11, color=CARDINAL)
        ax.text(0.62, -0.5, r"$\delta-$", ha="center", fontsize=11, color=BLUE)
        ax.text(-1.45, 0.72, "dipole", fontsize=11, color=ORANGE, va="center")
    else:
        ax.text(-1.45, 0.72, r"dipole: $M = 0$", fontsize=11, color=ORANGE, va="center")
    bx.axhline(0, color=GRAY, lw=0.8)
    if polar:
        bx.axhline(1, color=GRAY, lw=1, ls=":")
        bx.text(1.0, 1.08, r"$M_e$", ha="right", fontsize=11, color=GRAY)
    bx.plot(tt, (1 + 0.45 * np.sin(4 * np.pi * tt)) if polar else 0 * tt, color="#dee2e6", lw=1.8)
    (trace,) = bx.plot([], [], color=ORANGE, lw=2.4)
    (dot,) = bx.plot([], [], "o", color=ORANGE, ms=7)
    bx.set_xlim(0, 1); bx.set_ylim(-0.25, 1.75); bx.set_yticks([]); bx.set_xticks([])
    bx.spines["bottom"].set_visible(False)
    bx.set_xlabel("time", fontsize=11); bx.set_ylabel(r"dipole $M(t)$", fontsize=11.5)
    bx.set_title(t2, loc="left", fontsize=12)
    parts.append((masses, polar, bond, c1, c2, l1, l2, bar, trace, dot))
fig.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.08)

def update(i):
    s = 0.2 * np.sin(4 * np.pi * ts[i])                     # the stretch, exaggerated
    for (m1, m2), polar, bond, c1, c2, l1, l2, bar, trace, dot in parts:
        p1, p2 = -0.6 - s * m2 / (m1 + m2), 0.6 + s * m1 / (m1 + m2)
        bond.set_data([p1, p2], [0, 0])
        c1.center, c2.center = (p1, 0), (p2, 0)
        l1.set_position((p1, 0)); l2.set_position((p2, 0))
        mu = 1 + 2.25 * s if polar else 0.0
        bar.set_data([-0.62, -0.62 + 0.9 * mu], [0.72, 0.72])
        sel = tt <= ts[i] + 1e-9
        trace.set_data(tt[sel], (1 + 0.45 * np.sin(4 * np.pi * tt[sel])) if polar else 0 * tt[sel])
        dot.set_data([ts[i]], [mu])

ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Top: HCl vibrating, with the partial charges $\delta+$ on H and $\delta-$ on Cl. Its dipole (orange bar) grows and shrinks with the bond length, so $M(t)$ oscillates about its equilibrium value $M_e$; that oscillation couples to light. Bottom: N$_2$ has no dipole at any bond length, so there is nothing for the light to push on. The stretch is exaggerated.

- A **homonuclear** diatomic (H$_2$, N$_2$, O$_2$) is symmetric at every bond length, so $M = 0$ always and $M' = 0$: the field has no handle on the bond. N$_2$ and O$_2$, 99% of the air, are transparent to infrared light. That settles the puzzle. Raman spectra, later in this lecture, still see them: they sense the polarizability, which does change as N$_2$ stretches.
- A **heteronuclear** diatomic (HCl, CO, NO) always has some $M' \neq 0$, and absorbs.

#### A stationary state is not an antenna

The classical picture says what to look for: a dipole that oscillates. An energy eigenstate cannot supply one. Its density $|\psi_v|^2$ never changes in time ([Lecture 3.7](../ch03/07-time-dependence.md)), so its average dipole is constant. A molecule that absorbs a photon passes through a superposition of the two levels, and Lecture 3.7 showed that a superposition moves at the Bohr frequencies. Apply that result to the dipole. Take real coefficients and the real oscillator states:

$$
\Psi(x, t) = c_v\,\psi_v\,e^{-iE_vt/\hbar} + c_{v'}\,\psi_{v'}\,e^{-iE_{v'}t/\hbar}
$$

The density has two constant parts and one cross term, whose two phases combine into a cosine ($e^{i\theta} + e^{-i\theta} = 2\cos\theta$):

$$
|\Psi|^2 = c_v^2\,\psi_v^2 + c_{v'}^2\,\psi_{v'}^2 + 2c_vc_{v'}\,\psi_v\psi_{v'}\cos\omega_{v'v}t, \qquad \omega_{v'v} = \frac{E_{v'} - E_v}{\hbar}
$$

Weight it by the dipole and integrate, $\langle M\rangle = \int M(x)\,|\Psi|^2\,dx$:

:::{important} **Absorption needs a swinging dipole**

$$
\langle M\rangle(t) = c_v^2\,\langle v|\hat{M}|v\rangle + c_{v'}^2\,\langle v'|\hat{M}|v'\rangle + 2c_vc_{v'}\,\langle v'|\hat{M}|v\rangle\cos\omega_{v'v}t
$$

- The first two terms are the constant dipoles of the two levels. Only the cross term oscillates, at exactly the frequency that matches the gap.
- Its amplitude is the **transition dipole** $\langle v'|\hat{M}|v\rangle = \int \psi_{v'}\,M(x)\,\psi_v\,dx$. The rate of absorption is proportional to its square ([Chapter 6](../ch06/03-time-dependent-perturbation-and-selection-rules.md)).
:::

Two readings of the same integral are worth keeping:

- **The size of the antenna.** If $\langle v'|\hat{M}|v\rangle = 0$, the dipole of the mixed state never swings. Light at $\omega_{v'v}$ has nothing to push on, and it can never move a molecule from $v$ to $v'$.
- **A projection.** The field enters the energy as $-\mathcal{E}\hat{M}$, so it acts on a state by multiplying $\psi_v$ by $M(x)$. Expand the result in oscillator states as in [Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md): the coefficient of $\psi_{v'}$ is $\langle v'|\hat{M}|v\rangle$. The light can feed only the states that this kicked function contains.

The same integral decided which lines an electron in a box can emit in Lecture 3.7, where parity removed the frequency $\omega_{31}$. Here it decides which rungs light can climb.

#### Each term of the dipole has one job

Expand the dipole about $R_e$:

$$
M(x) = M_e + M'x + \frac{1}{2}M''x^2 + \dots, \qquad M' = \left(\frac{\partial M}{\partial x}\right)_{R_e}
$$

Sandwich it between two vibrational states:

$$
\langle v'|\hat{M}|v\rangle = M_e\,\langle v'|v\rangle + M'\,\langle v'|\hat{x}|v\rangle + \frac{1}{2}M''\,\langle v'|\hat{x}^2|v\rangle + \dots
$$

- **The permanent dipole** $M_e$ gives $\langle v'|v\rangle = 0$ for $v' \neq v$, by orthogonality. Multiplying by a constant leaves the state where it was, so a permanent dipole alone cannot drive a vibrational transition.
- **The slope** $M'$ is the force term of the classical picture. By Lecture 4.2, $\hat{x} = (\hat{a} + \hat{a}^\dagger)/\sqrt{2\alpha}$ moves one rung up or down, so this term drives only $v \to v \pm 1$. From the ground state, $x\psi_0$ is $\psi_1$ itself, times $1/\sqrt{2\alpha}$.
- **The curvature** $M''$ multiplies $x^2$, which moves up to two rungs. It allows $0 \to 2$, but $M''$ is small, so the line is weak. Together with the anharmonic states later in this lecture, it produces the overtones.

```{code-cell} python
:tags: [hide-input]
# synced: dipole_kick
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(-4.5, 4.5, 1201)                            # units of 1/sqrt(alpha)
dx = x[1] - x[0]
nv = 5
psi = np.zeros((nv, x.size))                                # normalized oscillator states, filled by the recursion
psi[0] = np.pi ** -0.25 * np.exp(-x ** 2 / 2)
psi[1] = np.sqrt(2) * x * psi[0]
for v in range(1, nv - 1):
    psi[v + 1] = np.sqrt(2 / (v + 1)) * x * psi[v] - np.sqrt(v / (v + 1)) * psi[v - 1]
cols = [(np.ones_like(x), r"constant term $M_e$", r"$1\cdot\psi_0 = \psi_0$", None,
         r"$\langle v'|1|0\rangle$: no transition"),
        (x, r"linear term $M'x$", r"$x\,\psi_0 = \frac{1}{\sqrt{2}}\,\psi_1$", (1, r"$\frac{1}{\sqrt{2}}\psi_1$"),
         r"$\langle v'|x|0\rangle$: only $0 \to 1$"),
        (x ** 2, r"quadratic term $\frac{1}{2}M''x^2$", r"$x^2\psi_0 = \frac{1}{2}\psi_0 + \frac{1}{\sqrt{2}}\,\psi_2$",
         (2, r"$\frac{1}{\sqrt{2}}\psi_2$"), r"$\langle v'|x^2|0\rangle$: $0 \to 2$ too")]
fig, axes = plt.subplots(2, 3, figsize=(9.6, 4.1), gridspec_kw={"height_ratios": [1.2, 1], "hspace": 0.78, "wspace": 0.2})
for j, (f, head, ident, part, verdict) in enumerate(cols):
    ax, bx = axes[0, j], axes[1, j]
    kick = f * psi[0]
    comp = psi @ kick * dx                                  # <v'| f |0> for v' = 0..4
    ax.axhline(0, color=GRAY, lw=0.8)
    ax.plot(x, psi[0], color=GRAY, lw=1.6, ls="--")
    ax.plot(x, kick, color=ORANGE, lw=2.6)
    if part is not None:
        ax.plot(x, comp[part[0]] * psi[part[0]], color=TEAL, lw=2.2, ls=(0, (1.5, 1.8)))
        ax.text(1.9, 0.5, part[1], color=TEAL, fontsize=13)
    ax.set_xlim(-4, 4); ax.set_ylim(-0.5, 0.8); ax.set_yticks([]); ax.set_xticks([])
    ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
    ax.set_title(head + "\n" + ident, loc="left", fontsize=13, linespacing=1.6)
    bx.bar(np.arange(nv), comp, width=0.6, color=[PURPLE] + [ORANGE] * (nv - 1))
    for v in range(nv):
        if abs(comp[v]) > 0.005:
            bx.text(v, comp[v] + 0.05, f"{comp[v]:.2f}", ha="center", va="bottom", fontsize=12,
                    color=PURPLE if v == 0 else ORANGE)
    bx.axhline(0, color=GRAY, lw=0.8)
    bx.set_ylim(0, 1.3); bx.set_yticks([]); bx.spines["left"].set_visible(False)
    bx.set_xticks(range(nv)); bx.tick_params(labelsize=12)
    bx.set_xlabel(r"$v'$", fontsize=13, labelpad=0)
    bx.set_title(verdict, loc="left", fontsize=13)
axes[0, 1].text(-1.9, 0.66, r"$\psi_0$", color=GRAY, fontsize=13)
axes[0, 0].text(1.35, 0.52, "after the kick", color=ORANGE, fontsize=12.5)
fig.subplots_adjust(left=0.02, right=0.99, top=0.84, bottom=0.11)
plt.show()
```

Fig. What each term of the dipole does to the ground state, in units with $\alpha = 1$. Top: multiplying $\psi_0$ (gray dashed) by 1, $x$ or $x^2$ gives the orange function. $x\psi_0$ lies exactly on $\psi_1/\sqrt{2}$ (teal dotted), and $x^2\psi_0$ is $\frac{1}{2}\psi_0$ plus $\psi_2/\sqrt{2}$. Bottom: the components $\langle v'|\cdot|0\rangle$ of each result. The purple bar ($v' = 0$) leaves the molecule where it was; the orange bars are transitions.

#### Slosh or breathe

The widget shows the antenna at work. It mixes $v = 0$ with a higher level $v'$ and draws the density, the dipole function $M(x)$, and the swing of $\langle M\rangle(t)$. Switch the terms of $M(x)$ on and off and watch which lines light up.

```{anywidget} ../widgets/transition_dipole.mjs
{}
```

- $\psi_0 + \psi_1$ **sloshes** from side to side at $\omega$. Only a tilted $M(x)$ turns the slosh into a swinging dipole: the fundamental needs $M' \neq 0$.
- $\psi_0 + \psi_2$ **breathes**. Its width swings at $2\omega$ while its center stays put, so a straight $M(x)$ has nothing to grab. Only the curvature $M''$ feels the width, and the overtone is weak because $M''$ is small.
- $\psi_0 + \psi_3$ moves too, but neither $x$ nor $x^2$ reaches three rungs. In a real bond, $0 \to 3$ comes from the anharmonic states and is weaker still.
- The quantum frequencies are the classical ones. The fundamental is the bond's own vibration frequency $\omega$. The overtone at $2\omega$ is the second harmonic that a classical spring would radiate if its dipole had a curvature, since $x^2 = A^2\cos^2\omega t = \frac{1}{2}A^2(1 + \cos 2\omega t)$.

#### One rung at a time

The slope term is by far the largest, so keep it alone. Position connects only neighboring levels, $\langle v'|\hat{x}|v\rangle = 0$ unless $v' = v \pm 1$, so in a harmonic bond light climbs one rung at a time, and every allowed jump absorbs the same wavenumber $\tilde{\nu}$.

:::{important} **Selection rules for vibrational absorption**

$$
\langle v'|\hat{M}|v\rangle \approx M'\,\langle v'|\hat{x}|v\rangle, \qquad M' = \left(\frac{\partial M}{\partial x}\right)_{R_e}
$$

1. **The dipole must change** during the vibration, $M' \neq 0$. Homonuclear diatomics do not absorb.
2. **One rung at a time** (harmonic bond): $\Delta v = \pm 1$.
:::

#### Where the molecules start

A spectrum also depends on which levels are occupied. By the Boltzmann factor, the population of $v = 1$ relative to $v = 0$ is $e^{-\tilde{\nu}/(k_BT/hc)}$; for HCl at 300 K that is $e^{-2886/208} \approx 10^{-6}$ ([Lecture 4.1](01-molecular-degrees-of-freedom.md)). Nearly every molecule starts in $v = 0$, so the absorption is the single jump $0 \to 1$, called the **fundamental**: one strong line per infrared-active vibration.

### Stiffness and mass set the wavenumber

The vibrational wavenumber has two knobs, $\tilde{\nu} = \frac{1}{2\pi c}\sqrt{k/\mu}$: a stiff bond raises it, heavy atoms lower it. The force constant follows from a measured wavenumber, $k = \mu\,(2\pi c\tilde{\nu})^2$:

| molecule | $\tilde{\nu}$ (cm$^{-1}$) | $\mu$ (u) | $k$ (N/m) | infrared |
|:--|:-:|:-:|:-:|:-:|
| H$_2$ | 4401 | 0.504 | 575 | inactive |
| HF | 4138 | 0.957 | 966 | active |
| HCl | 2991 | 0.980 | 516 | active |
| HBr | 2649 | 0.995 | 411 | active |
| HI | 2309 | 1.000 | 314 | active |
| N$_2$ | 2359 | 7.00 | 2295 | inactive |
| CO | 2170 | 6.86 | 1902 | active |
| NO | 1904 | 7.47 | 1595 | active |
| O$_2$ | 1580 | 8.00 | 1177 | inactive |
| Cl$_2$ | 560 | 17.5 | 323 | inactive |
| I$_2$ | 215 | 63.5 | 172 | inactive |

```{code-cell} python
:tags: [hide-input]
# synced: diatomic_ruler
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False})
hyd = [("HF", 4138, 1, 1), ("HCl", 2991, 1, 1), ("HBr", 2649, 1, -1), ("HI", 2309, 1, 1), ("H$_2$", 4401, 0, -1)]
heavy = [("N$_2$", 2359, 0, 1), ("CO", 2170, 1, -1), ("NO", 1904, 1, 1), ("O$_2$", 1580, 0, -1),
         ("Cl$_2$", 560, 0, 1), ("I$_2$", 215, 0, -1)]
fig, ax = plt.subplots(figsize=(9.6, 3.7))
for y, group in ((1.0, hyd), (0.0, heavy)):
    ax.axhline(y, color="#dee2e6", lw=1, zorder=1)
    for name, w, act, side in group:
        ax.plot([w], [y], "o", ms=12, mfc=TEAL if act else "white", mec=TEAL, mew=2.2, zorder=3)
        ax.text(w, y + 0.2 * side, name, ha="center", va="center", fontsize=12.5)
ax.text(4580, 1.0, "one H atom\n" + r"$\mu \approx 1$ u", ha="right", va="center", fontsize=11, color=GRAY)
ax.text(4580, 0.0, "two heavy atoms\n" + r"$\mu$ = 7 to 63 u", ha="right", va="center", fontsize=11, color=GRAY)
ax.annotate("", xy=(2309, 1.42), xytext=(4138, 1.42),
            arrowprops=dict(arrowstyle="-|>", color=CARDINAL, lw=1.4, mutation_scale=14))
ax.text(3220, 1.52, "down the halogen group: weaker bond, lower wavenumber", ha="center", fontsize=11, color=CARDINAL)
ax.annotate("", xy=(560, -0.45), xytext=(2359, -0.45),
            arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.4, mutation_scale=14))
ax.text(1460, -0.62, r"N$\equiv$N, O=O, Cl$-$Cl: bond order 3, 2, 1", ha="center", fontsize=11, color=PURPLE)
ax.plot([], [], "o", ms=10, mfc=TEAL, mec=TEAL, label="IR active: the dipole changes")
ax.plot([], [], "o", ms=10, mfc="white", mec=TEAL, mew=2, label="IR inactive: no dipole at any length")
ax.legend(loc="upper right", frameon=False, fontsize=11, bbox_to_anchor=(1.0, 1.18), ncol=2)
ax.set_xlim(4600, 0); ax.set_ylim(-0.8, 1.7); ax.set_yticks([])
ax.set_xlabel(r"harmonic wavenumber $\tilde{\nu}$ (cm$^{-1}$)", fontsize=11.5)
fig.subplots_adjust(left=0.17, right=0.99, top=0.88, bottom=0.16)
plt.show()
```

Fig. Harmonic wavenumbers of common diatomic molecules. Top row: one partner is hydrogen, so $\mu \approx 1$ u (0.5 u for H$_2$). Bottom row: two heavy atoms. Filled circles absorb infrared light; hollow ones have no dipole at any bond length and do not.

- **Same mass, different stiffness.** The hydrogen halides all have $\mu \approx 1$ u, because the heavy halogen barely moves. Their wavenumbers fall from HF to HI because the bond weakens down the group: $k$ drops from 966 to 314 N/m.
- **Bond order.** N$\equiv$N, O=O and Cl$-$Cl have force constants 2295, 1177 and 323 N/m. More bonding electrons, a stiffer spring.
- **Mass alone.** H$_2$ is not the stiffest bond in the table, but it is the lightest oscillator ($\mu = 0.5$ u), so it vibrates fastest.
- **Isotopes.** The force constant is set by the electrons, which an isotope does not change. Only $\mu$ changes, so $\tilde{\nu} \propto 1/\sqrt{\mu}$.

:::{note} **Example: a carbon-13 label**

$^{12}$C$^{16}$O absorbs at 2143 cm$^{-1}$. Where does $^{13}$C$^{16}$O absorb?

The reduced masses are

$$
\mu(^{12}\text{C}^{16}\text{O}) = \frac{(12.000)(15.995)}{27.995} = 6.856\ \text{u}, \qquad \mu(^{13}\text{C}^{16}\text{O}) = \frac{(13.003)(15.995)}{28.998} = 7.172\ \text{u}
$$

and with the same $k$,

$$
\tilde{\nu}(^{13}\text{C}^{16}\text{O}) = 2143\ \text{cm}^{-1}\times\sqrt{\frac{6.856}{7.172}} = 2143 \times 0.9777 = 2095\ \text{cm}^{-1}
$$

The measured line is at 2096 cm$^{-1}$. A shift of 48 cm$^{-1}$ is easy to resolve, which is why isotope labels are used to tag one bond inside a large molecule, such as one C=O group in a protein.
:::

### Real bonds are anharmonic

The harmonic levels assume the parabola continues forever. The real bond potential (the Morse curve of [Lecture 4.1](01-molecular-degrees-of-freedom.md)) is steeper on the compressed side and flattens toward dissociation on the stretched side. Near the bottom the two agree; higher up they do not:

```{code-cell} python
:tags: [hide-input]
# synced: morse_ladder
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
D, a, re, hw = 4.62, 1.87, 1.275, 0.3708                   # HCl: eV, 1/A, A, hbar omega in eV
xe = hw**2 / (4 * D)                                        # Morse anharmonicity (eV)
k = 2 * D * a * a
G = lambda v: hw * (v + 0.5) - xe * (v + 0.5)**2
turn = lambda E: (re - np.log(1 + np.sqrt(E / D)) / a, re - np.log(1 - np.sqrt(E / D)) / a)
r = np.linspace(0.8, 3.8, 700)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.5), sharey=True, gridspec_kw={"wspace": 0.06})
ax1.plot(r, 0.5 * k * (r - re)**2, color=ORANGE, lw=2.4)
for v in range(15):
    E = hw * (v + 0.5)
    h = np.sqrt(2 * E / k)
    ax1.hlines(E, re - h, re + h, color=TEAL if v < 3 else "#adb5bd", lw=1.6 if v < 3 else 1.0)
ax1.set_title("harmonic: equal steps forever,\nthe bond never comes apart", loc="left", fontsize=12, color=ORANGE)
ax2.plot(r, D * (1 - np.exp(-a * (r - re)))**2, color="k", lw=2.4)
vmax = int(hw / (2 * xe) - 0.5)                         # last level below the dissociation limit
for v in range(vmax + 1):
    r1, r2 = turn(G(v))
    ax2.hlines(G(v), r1, r2, color=TEAL if v < 3 else "#adb5bd", lw=1.6 if v < 3 else 1.0)
ax2.axhline(D, color=GRAY, lw=1, ls="--")
ax2.text(3.75, D + 0.08, "atoms apart", ha="right", va="bottom", fontsize=11, color=GRAY)
ax2.annotate("", xy=(3.15, D), xytext=(3.15, 0), arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.4, shrinkA=0, shrinkB=0))
ax2.text(3.2, D / 2, r"$D_e$", fontsize=13, color=CARDINAL, va="center")
ax2.annotate("", xy=(2.75, D), xytext=(2.75, G(0)), arrowprops=dict(arrowstyle="<->", color=PURPLE, lw=1.4, shrinkA=0, shrinkB=0))
ax2.text(2.8, D / 2 + 0.3, r"$D_0$", fontsize=13, color=PURPLE, va="center")
ax2.set_title("Morse: the steps shrink, a last level,\nthen dissociation", loc="left", fontsize=12)
for ax in (ax1, ax2):
    ax.set_xlim(0.8, 3.8); ax.set_ylim(0, 5.3)
    ax.set_xlabel(r"bond length $R$ ($\AA$)", fontsize=11.5)
ax1.set_ylabel("energy (eV)", fontsize=11.5)
fig.subplots_adjust(left=0.07, right=0.99, top=0.86, bottom=0.13)
plt.show()
```

Fig. Vibrational levels of HCl in the harmonic approximation (left) and in a Morse potential fitted to HCl (right); the lowest three levels are teal. The harmonic steps are equal and never end. The Morse steps shrink as the energy rises, and above the last level the atoms come apart. $D_e$ is the depth of the well from its bottom, $D_0$ the energy needed to dissociate from $v = 0$.

The levels of the Morse potential can be found exactly. The harmonic formula gains one correction term:

$$
G(v) = \tilde{\nu}_e\left(v + \frac{1}{2}\right) - \tilde{\nu}_ex_e\left(v + \frac{1}{2}\right)^2
$$

- $\tilde{\nu}_e$ is the harmonic wavenumber, set by the curvature at the bottom of the well. The **anharmonicity constant** $x_e$ is small, typically 0.005 to 0.02.
- **The steps shrink.** The gap above level $v$ is

$$
G(v + 1) - G(v) = \tilde{\nu}_e - \tilde{\nu}_ex_e\left[\left(v + \tfrac{3}{2}\right)^2 - \left(v + \tfrac{1}{2}\right)^2\right] = \tilde{\nu}_e - 2\tilde{\nu}_ex_e(v + 1)
$$

  It falls by $2\tilde{\nu}_ex_e$ per rung and reaches zero near $v + 1 = 1/2x_e$. A Morse bond has a finite number of bound levels; above them, the atoms are free.
- **Dissociation energy.** Breaking the bond from $v = 0$ costs $D_0 = D_e - G(0)$; the zero-point energy is part of every bond energy (Lecture 4.2).

:::{important} **The anharmonic oscillator**

$$
G(v) = \tilde{\nu}_e\left(v + \frac{1}{2}\right) - \tilde{\nu}_ex_e\left(v + \frac{1}{2}\right)^2
$$

$$
\tilde{\nu}_{0 \to v} = G(v) - G(0) = v\,\tilde{\nu}_e - v(v + 1)\,\tilde{\nu}_ex_e
$$

- $\tilde{\nu}_e$: harmonic wavenumber; $x_e$: anharmonicity constant; $D_0 = D_e - G(0)$
- The second line is the wavenumber of a photon that lifts the bond from $v = 0$ to $v$
:::

### Overtones and hot bands

In an anharmonic well the selection rule $\Delta v = \pm 1$ is no longer strict. The states are not exactly harmonic, so $\hat{x}$ connects levels further apart, and the dipole has its own curvature $M''$. Jumps $0 \to 2$, $0 \to 3$, ... become weakly allowed: the **overtones**, each tens of times weaker than the one before.

```{code-cell} python
:tags: [hide-input]
# synced: hcl_overtones
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
we, wexe = 2990.0, 52.0                                     # cm^-1, from the fundamental and first overtone
G = lambda v: we * (v + 0.5) - wexe * (v + 0.5)**2
D, a, re = 37260.0, 1.87, 1.275                             # Morse well in cm^-1 for the drawing
turn = lambda E: (re - np.log(1 + np.sqrt(E / D)) / a, re - np.log(1 - np.sqrt(E / D)) / a)
lines = [(1, TEAL, "fundamental"), (2, ORANGE, "first overtone"), (3, PURPLE, "second overtone")]
fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.4), gridspec_kw={"width_ratios": [1, 1.25], "wspace": 0.18})
r = np.linspace(0.95, 2.1, 400)
ax.plot(r, D * (1 - np.exp(-a * (r - re)))**2, color="k", lw=2.2)
for v in range(4):
    r1, r2 = turn(G(v))
    ax.hlines(G(v), r1, r2, color=GRAY, lw=1.4)
    ax.text(r2 + 0.03, G(v), rf"$v = {v}$", va="center", fontsize=11)
for j, (v, col, name) in enumerate(lines):
    x = 1.17 + 0.09 * j
    ax.annotate("", xy=(x, G(v)), xytext=(x, G(0)),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=2.2, mutation_scale=15, shrinkA=0, shrinkB=0))
ax.set_xlim(0.95, 2.1); ax.set_ylim(0, 11500); ax.set_xticks([])
ax.set_ylabel(r"energy (cm$^{-1}$)", fontsize=11.5)
ax.set_title("absorption from $v = 0$", loc="left", fontsize=12)
inten = [1.0, 2.5e-2, 6e-4]                                 # schematic: each overtone tens of times weaker
for (v, col, name), I in zip(lines, inten):
    w = G(v) - G(0)
    bx.vlines(w, 1e-4, I, color=col, lw=3.2)
    bx.text(w, I * 1.6, f"{name}\n{w:.0f} cm$^{{-1}}$", ha="center", va="bottom", fontsize=11, color=col)
bx.set_yscale("log"); bx.set_ylim(1e-4, 20); bx.set_yticks([]); bx.minorticks_off()
bx.set_xlim(2000, 9400)
bx.set_xlabel(r"photon wavenumber (cm$^{-1}$)", fontsize=11.5)
bx.set_ylabel("absorption (log scale)", fontsize=11.5)
bx.set_title(r"not equally spaced: $2 \times 2886 = 5772$, not 5668", loc="left", fontsize=12)
fig.subplots_adjust(left=0.08, right=0.99, top=0.9, bottom=0.13)
plt.show()
```

Fig. Left: absorption from $v = 0$ of HCl to $v = 1$ (fundamental), $v = 2$ (first overtone) and $v = 3$ (second overtone), drawn on the anharmonic ladder. Right: the lines they produce, on a logarithmic intensity scale (schematic). Because the steps shrink, the first overtone sits below twice the fundamental.

:::{note} **Example: HCl constants from two lines**

The fundamental of HCl is at 2886 cm$^{-1}$ and its first overtone at 5668 cm$^{-1}$. Find $\tilde{\nu}_e$ and $\tilde{\nu}_ex_e$, and predict the second overtone.

From $\tilde{\nu}_{0\to v} = v\,\tilde{\nu}_e - v(v + 1)\,\tilde{\nu}_ex_e$:

$$
v = 1:\ \ \tilde{\nu}_e - 2\tilde{\nu}_ex_e = 2886, \qquad v = 2:\ \ 2\tilde{\nu}_e - 6\tilde{\nu}_ex_e = 5668
$$

Subtract twice the first equation from the second: $-2\tilde{\nu}_ex_e = 5668 - 5772 = -104$, so $\tilde{\nu}_ex_e = 52$ cm$^{-1}$, and then $\tilde{\nu}_e = 2886 + 104 = 2990$ cm$^{-1}$ ($x_e = 0.017$). The second overtone is predicted at

$$
\tilde{\nu}_{0\to 3} = 3(2990) - 12(52) = 8346\ \text{cm}^{-1}
$$

and measured at 8347 cm$^{-1}$. The harmonic wavenumber 2990 cm$^{-1}$ is the $\hbar\omega$ of Lecture 4.2, the curvature at the bottom of the well; the measured fundamental lies 104 cm$^{-1}$ below it.
:::

- **Hot bands** start from $v = 1$. In HCl the jump $1 \to 2$ absorbs at $\tilde{\nu}_e - 4\tilde{\nu}_ex_e = 2782$ cm$^{-1}$, slightly below the fundamental. At room temperature only one molecule in a million is in $v = 1$, so the hot band is faint; it grows as the gas is heated (Problem 4).

### Polyatomic molecules: one oscillator per normal mode

A molecule with $N$ atoms has $3N - 6$ normal modes ($3N - 5$ if linear), [Lecture 4.1](01-molecular-degrees-of-freedom.md). Near equilibrium the vibrational Hamiltonian is a sum of independent harmonic oscillators, one per mode, so by the separable-Hamiltonian rule of Lecture 4.1 the energies add. Each mode has its own wavenumber, and its own selection rule:

:::{important} **Infrared activity of a normal mode**

$$
G(v_1, v_2, \dots) = \sum_{i} \tilde{\nu}_i\left(v_i + \frac{1}{2}\right)
$$

A mode's fundamental absorbs infrared light only if the motion of that mode changes the dipole moment.
:::

```{code-cell} python
:tags: [hide-input]
# synced: co2_modes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle
nf = 36
ts = np.arange(nf) / nf
re, d = 1.0, 0.13                                           # bond (drawing units) and the oxygen amplitude
f = 2 * 16.0 / 12.0                                         # carbon moves this much more, to keep the center of mass
# displacements (x, y) of O1, C, O2 per unit amplitude; charges O -1, C +2
modes = [("symmetric stretch", 1388, 2, [(-1, 0), (0, 0), (1, 0)], False),
         ("antisymmetric stretch", 2349, 3, [(1, 0), (-f, 0), (1, 0)], True),
         ("bend (two of them)", 667, 1, [(0, -1), (0, f), (0, -1)], True)]
q = np.array([-1.0, 2.0, -1.0])
x0 = np.array([[-re, 0.0], [0.0, 0.0], [re, 0.0]])
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.6))
parts = []
for ax, (name, wn, cyc, disp, active) in zip(axes, modes):
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.0, 1.2); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(f"{name}\n{wn} cm$^{{-1}}$", fontsize=12.5, color=TEAL)
    ax.text(0, -0.98, "dipole swings: IR active" if active else "dipole stays 0: IR inactive",
            ha="center", va="bottom", fontsize=11.5, color=ORANGE if active else GRAY, weight="bold")
    (b1,) = ax.plot([], [], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
    (b2,) = ax.plot([], [], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
    atoms = [Circle((0, 0), r, fc=c, ec="k", lw=1, zorder=3) for r, c in ((0.25, CARDINAL), (0.22, "#495057"), (0.25, CARDINAL))]
    for c in atoms:
        ax.add_patch(c)
    arr = ax.annotate("", xy=(0, 0.62), xytext=(0, 0.62),
                      arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.6, mutation_scale=16, shrinkA=0, shrinkB=0))
    parts.append((np.array(disp, float), cyc, b1, b2, atoms, arr))
fig.subplots_adjust(left=0.01, right=0.99, top=0.84, bottom=0.02, wspace=0.05)

def update(i):
    for disp, cyc, b1, b2, atoms, arr in parts:
        pos = x0 + d * np.sin(2 * np.pi * cyc * ts[i]) * disp
        for c, p in zip(atoms, pos):
            c.center = tuple(p)
        b1.set_data(pos[:2, 0], pos[:2, 1]); b2.set_data(pos[1:, 0], pos[1:, 1])
        mu = (q[:, None] * pos).sum(axis=0) * 0.5           # the dipole, scaled for the drawing
        base = np.array([0.0, 0.62])                        # drawn from a point above the carbon
        arr.xy = tuple(base + mu); arr.set_position(tuple(base))

ani = FuncAnimation(fig, update, frames=nf, interval=80, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. The normal modes of CO$_2$, with the measured wavenumbers. The orange arrow is the molecule's dipole moment, computed from partial charges $+2q$ on C and $-q$ on each O. In the symmetric stretch the two halves cancel at every instant, so the dipole stays zero. In the antisymmetric stretch and the bend it swings, along the axis and across it. The bend can happen in two perpendicular planes, so there are two bends with the same wavenumber.

- CO$_2$ ($N = 3$, linear) has $3N - 5 = 4$ modes: the symmetric stretch at 1388 cm$^{-1}$ (silent in the infrared), the antisymmetric stretch at 2349 cm$^{-1}$, and two bends at 667 cm$^{-1}$.
- Water is bent and less symmetric, and all three of its modes absorb (1595, 3657 and 3756 cm$^{-1}$, Lecture 4.1).
- Modes that are silent in the infrared, such as the symmetric stretch of CO$_2$ or the stretches of N$_2$ and O$_2$, show up in **Raman spectroscopy**, which senses how the vibration changes the molecule's polarizability rather than its dipole.

:::{note} **Example: why CO$_2$ is a greenhouse gas**

The Earth's surface, at about 288 K, radiates infrared light, most strongly near $\lambda_{\max} = (2898\ \text{μm K})/(288\ \text{K}) = 10$ μm by [Wien's law](../ch01/02-the-need-for-quantization.md), with most of the energy between about 5 and 50 μm. Which molecules in the air can absorb it?

- N$_2$ and O$_2$, 99% of dry air, have no dipole at any bond length: transparent.
- The CO$_2$ bend absorbs at 667 cm$^{-1}$, a wavelength of $1/(667\ \text{cm}^{-1}) = 15.0$ μm, right inside the Earth's emission. The antisymmetric stretch absorbs at 4.26 μm; the symmetric stretch at 7.2 μm is silent.

So CO$_2$, about 0.04% of the air, absorbs where the main components of the air cannot. Water vapor, with three active modes, absorbs too.
:::

### Reading an infrared spectrum

In a larger molecule, a bond such as C=O or O$-$H vibrates almost like an isolated diatomic spring. Its wavenumber depends mostly on the two atoms and the bond order, and hardly on the rest of the molecule. These **group frequencies** let a chemist read functional groups off a spectrum:

```{code-cell} python
:tags: [hide-input]
# synced: group_frequencies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False})
bands = [("O-H", 3200, 3600, TEAL), ("N-H", 3300, 3500, TEAL), ("C-H", 2850, 3100, TEAL),
         (r"C$\equiv$N", 2210, 2260, PURPLE), (r"C$\equiv$C", 2100, 2260, PURPLE),
         ("C=O", 1650, 1780, ORANGE), ("C=C", 1620, 1680, ORANGE), ("C-O", 1000, 1300, GRAY)]
groups = [(0, 2, "stretches of a bond to H:\nthe light H atom", TEAL), (3, 4, "triple bonds:\nthe stiffest", PURPLE),
          (5, 6, "double bonds", ORANGE), (7, 7, "single bonds", GRAY)]
fig, ax = plt.subplots(figsize=(9.6, 4.2))
ax.axvspan(1500, 400, color=GRAY, alpha=0.1, lw=0)
ax.text(950, -0.75, "fingerprint region:\nsingle bonds and bends,\nunique to each molecule", ha="center", va="top",
        fontsize=10.5, color=GRAY)
n = len(bands)
for j, (name, lo, hi, col) in enumerate(bands):
    y = n - 1 - j
    ax.barh(y, hi - lo, left=lo, height=0.62, color=col, alpha=0.85)
    ax.text(lo - 40, y, name, va="center", ha="left", fontsize=12, color="k")
for j0, j1, txt, col in groups:
    ax.text(4520, n - 1 - (j0 + j1) / 2, txt, ha="left", va="center", fontsize=10.5, color=col)
ax.set_xlim(4550, 400); ax.set_ylim(-2.9, n - 0.4); ax.set_yticks([])
ax.set_xticks([4000, 3500, 3000, 2500, 2000, 1500, 1000, 500])
ax.set_xlabel(r"wavenumber (cm$^{-1}$)", fontsize=11.5)
fig.subplots_adjust(left=0.02, right=0.99, top=0.97, bottom=0.13)
plt.show()
```

Fig. Typical wavenumber ranges of common bond stretches. Below about 1500 cm$^{-1}$ (gray), single-bond stretches and bends overlap into a pattern unique to each molecule, its fingerprint.

- **Bonds to hydrogen** absorb highest, 2850 to 3600 cm$^{-1}$, because the light hydrogen atom makes $\mu \approx 1$ u. Their force constants are not unusual (Problem 5).
- **Triple bonds** come next (2100 to 2260 cm$^{-1}$), then **double bonds** (1620 to 1780 cm$^{-1}$), then **single bonds** below 1300 cm$^{-1}$: the bond order sets $k$.
- The same ideas read biological spectra. The backbone of a protein absorbs near 1650 cm$^{-1}$ in its **amide I** band, mostly the C=O stretch of each amide group, and the exact wavenumber shifts with the local structure (helix or sheet):

:::{figure} images/amide_modes.png
:alt: Amide I vibration of a protein probed by two-dimensional infrared spectroscopy
:width: 90%

The amide I vibration of a protein backbone, mostly the C=O stretch of each amide group (left), probed by two-dimensional infrared spectroscopy (right).
:::

### Normal mode analysis: finding the modes

The normal modes of water in [Lecture 4.1](01-molecular-degrees-of-freedom.md) came from a computer. Here is how they are found, in five steps. The tools are the Taylor expansion of Lecture 4.1 and the matrices of [Lecture 3.5](../ch03/04-operators.md).

#### Step 1: the potential near the minimum, in every coordinate at once

For one bond, Lecture 4.1 expanded the potential about its minimum and kept the first term that survives:

$$
V(x) \approx \frac{1}{2}k\,x^2, \qquad k = \frac{d^2V}{dx^2}
$$

A molecule has many displacements $x_1, x_2, \dots$, one per atomic coordinate. The Taylor expansion works the same way with all of them at once:

$$
V = V_{\min} + \sum_i \frac{\partial V}{\partial x_i}\,x_i + \frac{1}{2}\sum_{i,j}\frac{\partial^2 V}{\partial x_i\,\partial x_j}\,x_ix_j + \dots
$$

Measure $V$ from the minimum, where every slope $\partial V/\partial x_i$ vanishes. The first term that survives is again the quadratic one:

$$
V \approx \frac{1}{2}\sum_{i,j} K_{ij}\,x_ix_j, \qquad K_{ij} = \frac{\partial^2 V}{\partial x_i\,\partial x_j}
$$

The matrix $K$ of second derivatives is the **Hessian**: a force constant for every pair of coordinates. A diagonal entry $K_{ii}$ is the stiffness against moving coordinate $i$ alone. An off-diagonal entry $K_{ij}$ says how moving coordinate $j$ changes the force on coordinate $i$.

:::{note} **Example: the force-constant matrix of CO$_2$**

Put O, C, O on a line with displacements $x_1, x_2, x_3$ along the axis and one spring $k$ per bond. Each spring stores energy according to how much its bond is stretched:

$$
V = \frac{1}{2}k\,(x_2 - x_1)^2 + \frac{1}{2}k\,(x_3 - x_2)^2 = \frac{1}{2}k\left(x_1^2 - 2x_1x_2 + 2x_2^2 - 2x_2x_3 + x_3^2\right)
$$

Take the second derivatives, or match the terms to $\frac{1}{2}\sum K_{ij}x_ix_j$ (a cross term such as $-2x_1x_2$ is shared by $K_{12}$ and $K_{21}$):

$$
K = k\begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 1 \end{pmatrix}
$$

The carbon sits between two springs, so its diagonal entry is $2k$. The $-k$ entries say that moving an oxygen pulls on the carbon next to it; the two oxygens are not bonded, so their entry is 0.
:::

#### Step 2: Newton's equations are coupled

The force on coordinate $i$ is minus the slope of the potential, $-\partial V/\partial x_i = -\sum_j K_{ij}x_j$. (For CO$_2$: $-\partial V/\partial x_1 = k(x_2 - x_1)$, which is minus the first row of $K$ times $\mathbf{x}$.) So

$$
m_i\,\ddot{x}_i = -\sum_j K_{ij}\,x_j
$$

Because of the off-diagonal entries, the equation for each atom contains the positions of its neighbors: the atoms are **coupled**. Pull one oxygen of CO$_2$ and let go, and the motion of each atom is a tangle:

```{code-cell} python
:tags: [hide-input]
# synced: co2_decoupling
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
mO, mC, k = 16.0, 12.0, 1.0
m = np.array([mO, mC, mO])
K = k * np.array([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])
w2, u = np.linalg.eigh(K / np.sqrt(np.outer(m, m)))
w = np.sqrt(np.clip(w2, 0, None))
u = u * np.sign(u[2])                                        # right oxygen moves +1 in every mode
x0 = np.array([-0.3, 0.0, 0.0])                             # pull the left oxygen outward and let go
q0 = np.sqrt(m) * x0
Q0 = u.T @ q0
Q0[0] = 0.0                                                 # drop the translation: the center of mass stays put
t = np.linspace(0, 4, 800)                                  # time in periods of the symmetric stretch
ph = 2 * np.pi * t * w[None, 1:].T / w[1]                   # phases of the two vibrations
Q = Q0[1:, None] * np.cos(ph)                               # each normal coordinate: one cosine
x = (u[:, 1:] @ Q) / np.sqrt(m)[:, None]                    # back to atom displacements
fig, (ax, bx) = plt.subplots(2, 1, figsize=(9.6, 4.8), sharex=True, gridspec_kw={"hspace": 0.45})
for xi, lab, col, ls in ((x[0], "left O", CARDINAL, "-"), (x[1], "C", "#495057", "-"), (x[2], "right O", CARDINAL, "--")):
    ax.plot(t, xi, color=col, lw=2, ls=ls, label=lab)
ax.set_title("atom by atom: every displacement mixes two frequencies, and energy flows between the atoms",
             loc="left", fontsize=12)
ax.legend(loc="upper right", frameon=False, fontsize=11, ncol=3, bbox_to_anchor=(1.0, 1.02))
ax.set_ylabel("displacement", fontsize=11.5)
bx.plot(t, Q[0], color=TEAL, lw=2.4, label=r"$Q_{\mathrm{sym}}$: symmetric stretch")
bx.plot(t, Q[1], color=ORANGE, lw=2.4, label=r"$Q_{\mathrm{anti}}$: antisymmetric stretch")
bx.set_title(r"mode by mode, $Q_k = \mathbf{u}_k\cdot\mathbf{q}$: each is a single cosine, $\ddot{Q}_k = -\omega_k^2 Q_k$",
             loc="left", fontsize=12)
bx.legend(loc="upper right", frameon=False, fontsize=11, ncol=2, bbox_to_anchor=(1.0, 1.02))
bx.set_ylabel("normal coordinate", fontsize=11.5)
bx.set_xlabel("time (periods of the symmetric stretch)", fontsize=11.5)
for a in (ax, bx):
    a.axhline(0, color=GRAY, lw=0.8); a.set_yticks([]); a.set_xlim(0, 4)
    lo, hi = a.get_ylim(); a.set_ylim(lo, hi + 0.35 * (hi - lo))
fig.subplots_adjust(left=0.06, right=0.99, top=0.93, bottom=0.11)
plt.show()
```

Fig. CO$_2$ after its left oxygen is pulled outward and released (one spring per bond, center of mass fixed). Top: the displacement of each atom mixes two frequencies, and energy passes back and forth between the atoms. Bottom: the same motion written in the normal coordinates of Step 4 is two independent cosines, one per mode.

#### Step 3: weight by the masses, and look for a mode

The masses differ from atom to atom. In the coordinates $q_i = \sqrt{m_i}\,x_i$ every atom behaves as if it had unit mass:

$$
\ddot{q}_i = -\sum_j F_{ij}\,q_j, \qquad F_{ij} = \frac{K_{ij}}{\sqrt{m_im_j}}
$$

**A normal mode is all the atoms moving in step.** Look for a motion in which every coordinate oscillates at the same frequency, keeping fixed proportions $\mathbf{u}$:

$$
\mathbf{q}(t) = \mathbf{u}\cos\omega t
$$

This is a guess, an ansatz, like the Gaussian tried for the oscillator ground state in [Lecture 4.2](02-quantum-harmonic-oscillator.md): substitute it into Newton's equation and see which $\mathbf{u}$ and $\omega$ make it work. Step 4 justifies it, by showing that every motion is a sum of such solutions. Two time derivatives give $\ddot{\mathbf{q}} = -\omega^2\,\mathbf{u}\cos\omega t$. Newton's equation gives $\ddot{\mathbf{q}} = -F\mathbf{u}\cos\omega t$. The two agree at every instant only if

$$
F\,\mathbf{u} = \omega^2\,\mathbf{u}
$$

Finding the normal modes means finding the eigenvectors of $F$ (the shapes of the motion) and its eigenvalues (the squared frequencies). CO$_2$'s $3\times3$ matrix has three: a translation with $\omega = 0$, the symmetric stretch and the antisymmetric stretch (worked out below). $F$ is a real symmetric matrix, $F_{ij} = F_{ji}$, like the Hermitian matrices of [Operators 2](../ch03/05-hermitian-operators-and-commutators.md), so its eigenvalues are real and its eigenvectors are perpendicular:

$$
F\,\mathbf{u}_k = \omega_k^2\,\mathbf{u}_k, \qquad \mathbf{u}_k\cdot\mathbf{u}_l = \delta_{kl}
$$

#### Step 4: project onto the modes, and they come apart

Step 3 found special motions, each at a single frequency. Now show that every motion is made of them, and that they never disturb one another.

1. **The eigenvectors are axes.** With $n$ coordinates there are $n$ perpendicular unit eigenvectors, a full set of axes for $\mathbf{q}$. Any configuration is a combination of them,

$$
\mathbf{q} = \sum_k Q_k\,\mathbf{u}_k, \qquad Q_k = \mathbf{u}_k\cdot\mathbf{q}
$$

   The **normal coordinate** $Q_k$ is the component of $\mathbf{q}$ along the axis $\mathbf{u}_k$. Three symbols carry the whole argument, so keep them apart:

| symbol | what it is | changes in time? | CO$_2$ example |
|:--|:--|:-:|:--|
| $\mathbf{q}(t)$ | the configuration: every mass-weighted displacement at time $t$, one entry per coordinate | yes | $(\sqrt{m_O}\,x_1,\ \sqrt{m_C}\,x_2,\ \sqrt{m_O}\,x_3)$ |
| $\mathbf{u}_k$ | normal mode $k$: a fixed unit vector, the shape of the motion, an eigenvector of $F$ | no | $\mathbf{u}_{\text{sym}} = (-1, 0, 1)/\sqrt{2}$ |
| $Q_k(t)$ | the normal coordinate: one number, how much of mode $k$ is present now, $Q_k = \mathbf{u}_k\cdot\mathbf{q}$ | yes | $Q_{\text{sym}}(t) = A\cos\omega_{\text{sym}}t$ |

The configuration is (how much) times (shape), summed over the modes. It has the structure of a state written in a basis, $\psi = \sum_n c_n\psi_n$ ([Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md)): $\mathbf{q}$ plays $\psi$, the fixed $\mathbf{u}_k$ play the basis functions $\psi_n$, and the $Q_k$ play the coefficients $c_n$, found by the same kind of projection. The difference is that the $Q_k$ oscillate as cosines, where the $c_n$ only turn their phases. In the guess of Step 3, a single $Q_k(t) = \cos\omega_kt$ and every other $Q$ is zero.


2. **Project Newton's equation onto one axis.** Take the dot product of $\ddot{\mathbf{q}} = -F\mathbf{q}$ with $\mathbf{u}_k$, one step at a time:

$$
\begin{aligned}
\ddot{Q}_k &= \mathbf{u}_k\cdot\ddot{\mathbf{q}} && \text{the axis } \mathbf{u}_k \text{ does not move} \\
&= -\mathbf{u}_k\cdot(F\mathbf{q}) && \text{Newton's equation} \\
&= -(F\mathbf{u}_k)\cdot\mathbf{q} && F \text{ is symmetric} \\
&= -\omega_k^2\,\mathbf{u}_k\cdot\mathbf{q} && \mathbf{u}_k \text{ is an eigenvector} \\
&= -\omega_k^2\,Q_k
\end{aligned}
$$

   The third line moves $F$ from one side of the dot product to the other. That is allowed for a symmetric matrix: $\mathbf{a}\cdot(F\mathbf{b}) = \sum_{ij}a_iF_{ij}b_j = \sum_{ij}b_jF_{ji}a_i = (F\mathbf{a})\cdot\mathbf{b}$.

3. **Read the result.** Only $Q_k$ appears on the right: no other normal coordinate. Each one obeys its own spring equation, $Q_k(t) = A_k\cos(\omega_kt + \varphi_k)$, whatever the others are doing. The modes are **independent**, as in the bottom panel of the figure above.

- The motion of the atoms is a sum of modes, $\mathbf{q} = \sum_k Q_k\,\mathbf{u}_k$, just as a state is a sum of eigenfunctions. Each $Q_k$ oscillates at its own $\omega_k$, so the atoms (top panel) mix the frequencies.
#### Step 5: the Hamiltonian becomes a sum

The same change of coordinates splits the energy. In the mass-weighted coordinates the kinetic energy is $\sum_i \frac{1}{2}m_i\dot{x}_i^2 = \frac{1}{2}\sum_i\dot{q}_i^2$ and the potential energy is $\frac{1}{2}\sum_{ij}K_{ij}x_ix_j = \frac{1}{2}\sum_{ij}F_{ij}q_iq_j$, so

$$
H = \frac{1}{2}\,\dot{\mathbf{q}}\cdot\dot{\mathbf{q}} + \frac{1}{2}\,\mathbf{q}\cdot F\mathbf{q}
$$

Now insert $\mathbf{q} = \sum_k Q_k\mathbf{u}_k$. Every product of two different eigenvectors is zero, $\mathbf{u}_k\cdot\mathbf{u}_l = \delta_{kl}$, so the double sums collapse to single sums:

$$
\dot{\mathbf{q}}\cdot\dot{\mathbf{q}} = \sum_{k,l}\dot{Q}_k\dot{Q}_l\,\mathbf{u}_k\cdot\mathbf{u}_l = \sum_k\dot{Q}_k^2, \qquad
\mathbf{q}\cdot F\mathbf{q} = \sum_{k,l}Q_kQ_l\,\mathbf{u}_k\cdot(F\mathbf{u}_l) = \sum_{k,l}Q_kQ_l\,\omega_l^2\,\delta_{kl} = \sum_k\omega_k^2Q_k^2
$$

$$
H = \sum_k\left(\frac{1}{2}\dot{Q}_k^2 + \frac{1}{2}\omega_k^2Q_k^2\right) = \sum_k H_k
$$

- In atomic coordinates the potential energy has **cross terms**, such as $-kx_1x_2$ in CO$_2$, which pass energy from atom to atom. In normal coordinates there are none: each mode is a separate oscillator with its own energy, and that energy never leaks into another mode.
- Quantum mechanically, $\hat{H} = \sum_k\hat{H}_k$ is a sum of harmonic oscillators, one per mode. By the separable rule of [Lecture 4.1](01-molecular-degrees-of-freedom.md) the wavefunctions multiply and the energies add, $G = \sum_k\tilde{\nu}_k\left(v_k + \frac{1}{2}\right)$: the box at the start of this section.

The widget runs the CO$_2$ stretches live. Choose how much of each mode the molecule holds, or pull one oxygen, and compare the two ways of splitting the same energy:

```{anywidget} ../widgets/normal_modes.mjs
{}
```

- **Atom by atom** (left), the kinetic energy of each atom and the energy of each spring rise and fall as energy passes between them.
- **Mode by mode** (right), each mode trades energy between its own kinetic and potential parts, but its total stays fixed. Only with a single mode does the atom picture repeat itself; with both, it never quite does.

:::{important} **Normal mode analysis**

$$
F\,\mathbf{u}_k = \omega_k^2\,\mathbf{u}_k, \qquad F_{ij} = \frac{1}{\sqrt{m_im_j}}\frac{\partial^2 V}{\partial x_i\,\partial x_j}, \qquad \ddot{Q}_k = -\omega_k^2\,Q_k
$$

$$
H = \sum_k\left(\frac{1}{2}\dot{Q}_k^2 + \frac{1}{2}\omega_k^2Q_k^2\right)
$$

- The eigenvalues are the squared frequencies $\omega_k^2$ of the modes, $\tilde{\nu}_k = \omega_k/2\pi c$
- The eigenvectors are the mode shapes; divide component $i$ by $\sqrt{m_i}$ to get the displacement of that atom
- Six eigenvalues (five for a linear molecule) are zero: translations and rotations cost no energy
:::

- A quantum chemistry "frequency calculation" does exactly this, with $K$ computed from the electronic energy.

:::{note} **Example: the stretches of CO$_2$**

Find the stretching modes of CO$_2$ from the matrix $K$ above.

Instead of a $3\times3$ determinant, guess the patterns from symmetry and check each by row times column, as in Lecture 3.5. Newton's equation $m_i\ddot{x}_i = -(K\mathbf{x})_i$ must give every atom the same $\omega^2$:

- **All atoms move together**, $\mathbf{x} = (1, 1, 1)$: $K\mathbf{x} = 0$, so $\omega = 0$. This is a translation.
- **Symmetric stretch**, $\mathbf{x} = (-1, 0, 1)$: $K\mathbf{x} = k(-1, 0, 1)$. Carbon feels no force and stays put, and each oxygen obeys $m_O\ddot{x} = -kx$:

$$
\omega_{\text{sym}}^2 = \frac{k}{m_O}
$$

- **Antisymmetric stretch**: both oxygens move one way and the carbon the other, with the center of mass fixed, $\mathbf{x} = (1, -2m_O/m_C, 1)$. The first row gives $(K\mathbf{x})_1 = k\left(1 + 2m_O/m_C\right)$, so

$$
\omega_{\text{anti}}^2 = \frac{k}{m_O}\left(1 + \frac{2m_O}{m_C}\right)
$$

  (The middle row gives the same $\omega^2$ for the carbon: check it.)

The ratio of the frequencies does not depend on $k$: $\sqrt{1 + 2(16)/12} = \sqrt{3.67} = 1.91$. The measured ratio is $2349/1388 = 1.69$. One spring per bond gets the order and the rough size; real force fields also couple the two bonds, so that stretching one changes the stiffness of the other.
:::

numpy finds the same three modes from the mass-weighted matrix:

```{code-cell} python
import numpy as np

mO, mC, k = 16.0, 12.0, 1.0                    # masses in u; k sets the unit of omega^2
K = k * np.array([[1, -1, 0], [-1, 2, -1], [0, -1, 1]])    # force constants of O-C-O
m = np.array([mO, mC, mO])
F = K / np.sqrt(np.outer(m, m))                # the mass-weighted matrix
w2, u = np.linalg.eigh(F)                      # eigenvalues omega^2, eigenvectors u
print("omega^2 in units of k/mO:", np.round(w2 * mO / k, 3) + 0)
print("antisymmetric / symmetric frequency:", round(np.sqrt(w2[2] / w2[1]), 3))
x = u[:, 2] / np.sqrt(m)                       # displacements of the antisymmetric mode
print("antisymmetric mode, O C O:", np.round(x / x[0], 3))
```

- The bends need the full coordinates of each atom and a spring for the bond angle. The water modes of Lecture 4.1 were found this way: three atoms in a plane give a $6\times6$ matrix, with three zero eigenvalues (two shifts and one turn in the plane) and three vibrations.

### Problems

#### Problem 1: Bond order from wavenumbers

The C$-$O stretch of methanol absorbs near 1033 cm$^{-1}$, the C=O stretch of formaldehyde near 1746 cm$^{-1}$, and the C$\equiv$O stretch of carbon monoxide at 2143 cm$^{-1}$. Treat each as a C$-$O diatomic spring and find the ratio of the three force constants. How close is it to 1 : 2 : 3?

:::{admonition} **Solution**
:class: dropdown solution

The atoms are the same in all three, so $\mu$ is the same and $k = \mu(2\pi c\tilde{\nu})^2 \propto \tilde{\nu}^2$:

$$
k_1 : k_2 : k_3 = 1033^2 : 1746^2 : 2143^2 = 1 : 2.86 : 4.30
$$

The force constant grows with bond order, but faster than 1 : 2 : 3. A triple bond is shorter as well as more strongly bonded, and in a polyatomic molecule the "C$-$O stretch" also mixes with neighboring motions, so the diatomic picture is only approximate.
:::

#### Problem 2: Which molecules absorb?

Which of these have an infrared-active fundamental: HBr, O$_2$, NO, H$_2$? For the linear molecule OCS (O=C=S), which of its four modes absorb? Compare with CO$_2$ and explain the difference.

#### Problem 3: How many bound levels?

Using $\tilde{\nu}_e = 2990$ cm$^{-1}$ and $\tilde{\nu}_ex_e = 52$ cm$^{-1}$ for HCl, find the highest bound vibrational level and the well depth $D_e$ that this Morse potential implies. Compare with the actual $D_e = 4.62$ eV.

:::{admonition} **Solution**
:class: dropdown solution

$G(v)$ rises as long as the gap $\tilde{\nu}_e - 2\tilde{\nu}_ex_e(v + 1)$ is positive. $G(v)$ has its maximum where $dG/dv = \tilde{\nu}_e - 2\tilde{\nu}_ex_e\left(v + \frac{1}{2}\right) = 0$:

$$
v + \frac{1}{2} = \frac{\tilde{\nu}_e}{2\tilde{\nu}_ex_e} = \frac{2990}{104} = 28.75 \quad\Longrightarrow\quad v_{\max} = 28
$$

so the levels $v = 0$ to 28 are bound, 29 in all. The top of the ladder is the Morse well depth:

$$
D_e = G\!\left(v + \tfrac{1}{2} = \frac{\tilde{\nu}_e}{2\tilde{\nu}_ex_e}\right) = \frac{\tilde{\nu}_e^2}{4\tilde{\nu}_ex_e} = \frac{2990^2}{208} = 42\,980\ \text{cm}^{-1} = 5.33\ \text{eV}
$$

The real well is 4.62 eV deep. A two-parameter Morse curve fitted to the lowest levels overestimates the depth by 15%: the real potential flattens out sooner than the Morse form assumes.
:::

#### Problem 4: Hot bands as a thermometer

Find the wavenumber of the HCl hot band $v = 1 \to 2$. Estimate its intensity relative to the fundamental at 300 K and at 1000 K, assuming both transitions are equally strong per molecule. Why could the ratio serve as a thermometer?

#### Problem 5: Why bonds to hydrogen absorb high

A C$-$H stretch absorbs near 2900 cm$^{-1}$ and a C$-$C stretch near 1000 cm$^{-1}$. Compute both force constants, treating each bond as a diatomic spring. Is the C$-$H bond much stiffer?

:::{admonition} **Solution**
:class: dropdown solution

$$
\mu_{\text{CH}} = \frac{(12.000)(1.008)}{13.008} = 0.930\ \text{u}, \qquad \mu_{\text{CC}} = \frac{(12)(12)}{24} = 6.00\ \text{u}
$$

With $k = \mu(2\pi c\tilde{\nu})^2$ and $1\ \text{u} = 1.661\times10^{-27}$ kg:

$$
k_{\text{CH}} = (1.544\times10^{-27}\ \text{kg})\left[2\pi(2.998\times10^{10}\ \text{cm/s})(2900\ \text{cm}^{-1})\right]^2 = 461\ \text{N/m}
$$

$$
k_{\text{CC}} = (9.96\times10^{-27}\ \text{kg})\left[2\pi(2.998\times10^{10}\ \text{cm/s})(1000\ \text{cm}^{-1})\right]^2 = 354\ \text{N/m}
$$

The two springs are about equally stiff. The factor of 2.9 in wavenumber comes almost entirely from the mass: $\sqrt{6.00/0.930} = 2.5$. Bonds to hydrogen absorb high because hydrogen is light.
:::

#### Problem 6: Nitrous oxide

N$_2$O is linear, N=N=O. How many normal modes does it have? Its stretches absorb near 1285 and 2224 cm$^{-1}$ and its bend near 589 cm$^{-1}$, and all of them are infrared active. Why is the "symmetric" stretch active here when the one in CO$_2$ is not?

#### Problem 7: A Birge-Sponer estimate

For an anharmonic bond the gap $\Delta G(v) = G(v + 1) - G(v)$ falls linearly with $v$. Using the HCl constants of the overtone example, sketch $\Delta G$ against $v$, find where it reaches zero, and use the area under the line (the sum of all the gaps) to estimate $D_0$. Compare with the measured 4.43 eV.

#### Problem 8: One line, four units

Carbon monoxide absorbs at 2143 cm$^{-1}$. Give the photon's wavelength, frequency and energy (in eV and kJ/mol), and the fraction of CO molecules in $v = 1$ at 300 K.

:::{admonition} **Solution**
:class: dropdown solution

- Wavelength: $\lambda = 1/\tilde{\nu} = 4.67$ μm.
- Frequency: $\nu = c\tilde{\nu} = (2.998\times10^{10}\ \text{cm/s})(2143\ \text{cm}^{-1}) = 6.42\times10^{13}$ Hz.
- Energy: $E = hc\tilde{\nu} = (1.986\times10^{-23}\ \text{J cm})(2143\ \text{cm}^{-1}) = 4.26\times10^{-20}$ J $= 0.266$ eV $= 25.6$ kJ/mol.
- Population: relative to $v = 0$, $e^{-2143/208.5} = e^{-10.3} = 3.4\times10^{-5}$. Fewer than one CO molecule in 20 000 vibrates at room temperature.
:::
