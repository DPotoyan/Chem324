---
kernelspec:
  name: python3
  display_name: Python 3
---

# Molecular Degrees of Freedom and Classical Vibrations

:::{note} **What you need to know**

- A molecule moves in four ways at once: it **translates**, **rotates** and **vibrates**, and its **electrons** rearrange. To a good approximation the energies add, $E = E_{\text{trans}} + E_{\text{rot}} + E_{\text{vib}} + E_{\text{elec}}$, and the wavefunctions multiply.
- The four ladders have wildly different spacings, from $10^{-15}$ cm$^{-1}$ (translation) to $10^4$ or $10^5$ cm$^{-1}$ (electrons). That is why each motion has its own spectroscopy, and why at room temperature molecules fly and tumble freely but hardly vibrate.
- $N$ nuclei carry $3N$ coordinates: 3 for translation, 3 for rotation (2 for a linear molecule), and $3N - 6$ ($3N - 5$) for vibrations.
- Each motion gets its own exactly solvable model: the **particle in a box** (translation), the **rigid rotor** (rotation) and the **harmonic oscillator** (vibration).
- Near its minimum every bond potential is a parabola, so every bond is a spring: $m\ddot{x} = -kx$, $x(t) = A\cos(\omega t + \phi)$, $\omega = \sqrt{k/m}$. A vibrating diatomic is one bead with the **reduced mass** $\mu = m_1m_2/(m_1 + m_2)$.

:::

### A molecule moves in four ways

The wavefunction of a molecule with $N$ nuclei and $n$ electrons depends on $3(N + n)$ coordinates. They sort into four kinds of motion:

- **Translation**: the molecule as a whole moves; its center of mass changes.
- **Rotation**: it turns; its orientation changes, its shape does not.
- **Vibration**: its shape changes; bond lengths and angles stretch and bend.
- **Electronic**: its electrons rearrange (Chapters 5 to 8).

In a gas all of them happen at once. The animation shows the first three for carbon monoxide, one at a time and then together.

```{code-cell} python
:tags: [hide-input]
# synced: dof_motions
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle
nf = 40
ts = np.arange(nf) / nf                                     # one loop of the GIF = 1
mC, mO, re = 12.0, 16.0, 0.95                               # carbon monoxide, bond in drawing units
fC, fO = mO / (mC + mO), mC / (mC + mO)                     # distance of each atom from the center of mass, per unit bond
heads = [("translation", "the center of mass moves", GRAY), ("rotation", "the orientation turns", PURPLE),
         ("vibration", "the bond length changes", TEAL), ("all three at once", "the real motion is the sum", "k")]
# center of mass (x, y), angle and bond length of each panel at loop time s
wrap = lambda s: -2.4 + 4.8 * ((s + 0.5) % 1)              # cross the panel once per loop; frame 0 in the middle
paths = [lambda s: (wrap(s), 0.0, np.radians(25), re),
         lambda s: (0.0, 0.0, 2 * np.pi * s, re),
         lambda s: (0.0, 0.0, 0.0, re * (1 + 0.24 * np.sin(6 * np.pi * s))),
         lambda s: (wrap(s), 0.0, 2 * np.pi * s + 0.4, re * (1 + 0.24 * np.sin(6 * np.pi * s)))]
fig, axes = plt.subplots(1, 4, figsize=(9.6, 2.85))
parts = []
for ax, (t1, t2, col) in zip(axes, heads):
    ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.3, 1.3); ax.set_aspect("equal")
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color("#ced4da")
    ax.set_title(t1, color=col, fontsize=13.5, weight="bold")
    ax.set_xlabel(t2, fontsize=11.5, color=GRAY)
    (bond,) = ax.plot([], [], color="#adb5bd", lw=6, solid_capstyle="round", zorder=2)
    cC = Circle((0, 0), 0.25, fc="#495057", ec="k", lw=1, zorder=3); ax.add_patch(cC)
    cO = Circle((0, 0), 0.29, fc=CARDINAL, ec="k", lw=1, zorder=3); ax.add_patch(cO)
    tC = ax.text(0, 0, "C", color="white", ha="center", va="center", fontsize=10, weight="bold", zorder=4)
    tO = ax.text(0, 0, "O", color="white", ha="center", va="center", fontsize=10, weight="bold", zorder=4)
    (com,) = ax.plot([], [], "+", color="k", ms=10, mew=2.2, zorder=5)
    parts.append((bond, cC, cO, tC, tO, com))
axes[0].axhline(0, color=GRAY, lw=1, ls=":", zorder=1)
axes[3].axhline(0, color=GRAY, lw=1, ls=":", zorder=1)
th = np.linspace(0, 2 * np.pi, 200)
axes[1].plot(fO * re * np.cos(th), fO * re * np.sin(th), color=PURPLE, lw=1, ls=":", zorder=1)
axes[1].plot(fC * re * np.cos(th), fC * re * np.sin(th), color=PURPLE, lw=1, ls=":", zorder=1)
fig.subplots_adjust(left=0.01, right=0.99, top=0.86, bottom=0.12, wspace=0.08)

def update(i):
    for path, (bond, cC, cO, tC, tO, com) in zip(paths, parts):
        X, Y, a, r = path(ts[i])
        u = np.array([np.cos(a), np.sin(a)])
        pC, pO = np.array([X, Y]) - fC * r * u, np.array([X, Y]) + fO * r * u
        bond.set_data([pC[0], pO[0]], [pC[1], pO[1]])
        cC.center, cO.center = tuple(pC), tuple(pO)
        tC.set_position(pC); tO.set_position(pO)
        com.set_data([X], [Y])

ani = FuncAnimation(fig, update, frames=nf, interval=85, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Carbon monoxide translating, rotating and vibrating, one at a time and then all at once. The cross marks the center of mass: translation moves it, rotation and vibration leave it in place. A molecule in a gas does all three at once, and its motion is their sum.

### Each motion has its own ladder

Molecules are microscopic, so each of these motions is quantized, and to a good approximation the energy is a sum of four parts:

$$
E = E_{\text{trans}} + E_{\text{rot}} + E_{\text{vib}} + E_{\text{elec}}
$$

The four ladders have very different spacings. The figure shows them for HCl, each one a magnified view of the lowest rung of the one before.

```{code-cell} python
:tags: [hide-input]
# synced: level_zoom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import ConnectionPatch, Rectangle
kT = 208.5                                                  # k_B T at 300 K in cm^-1
E1 = 4.57e-16                                               # HCl in a 1 cm box: h^2/8mL^2 in cm^-1
panels = [("electronic", ORANGE, [0, 65000], 80000, r"gap $\approx$ 65 000 cm$^{-1}$", "ultraviolet"),
          ("vibrational", TEAL, [0, 2886, 5668, 8347, 10923], 12500, r"gap $\approx$ 2 900 cm$^{-1}$", "infrared"),
          ("rotational", PURPLE, [10.59 * J * (J + 1) for J in range(9)], 800, r"gaps $\approx$ 20 cm$^{-1}$", "microwave"),
          ("translational", GRAY, [(n * n - 1) * E1 for n in range(1, 15)], 9.0e-14, r"gaps $\approx 10^{-15}$ cm$^{-1}$",
           "none: a continuum")]
fig, axes = plt.subplots(1, 4, figsize=(9.6, 4.3))
for k, (ax, (name, col, lev, top, gap, spec)) in enumerate(zip(axes, panels)):
    ax.axhspan(0, min(kT, top), color="#fcc419", alpha=0.32, lw=0, zorder=0)
    ax.hlines(lev, 0.12, 0.88, color=col, lw=2.2, zorder=2)
    ax.set_xlim(0, 1); ax.set_ylim(-0.03 * top, top)
    ax.set_xticks([])
    for sp in ("top", "right", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_title(name + "\n", color=col, fontsize=13, weight="bold", pad=2)
    ax.text(0.5, 1.015, gap, transform=ax.transAxes, ha="center", va="bottom", fontsize=10.5, color="k")
    ax.set_xlabel(spec, fontsize=11.5, color=col, labelpad=6)
    ax.tick_params(labelsize=9.5)
axes[0].set_yticks([0, 40000, 80000]); axes[0].set_yticklabels(["0", "40 000", "80 000"])
axes[1].set_yticks([0, 5000, 10000]); axes[1].set_yticklabels(["0", "5 000", "10 000"])
axes[2].set_yticks([0, 400, 800])
axes[3].set_yticks([0, 8e-14]); axes[3].set_yticklabels(["0", r"$8{\times}10^{-14}$"])
axes[0].set_ylabel(r"energy above the lowest level (cm$^{-1}$)", fontsize=11)
axes[0].text(0.5, 15500, "$k_BT$ at 300 K:\ntoo thin to see", ha="center", va="bottom", fontsize=9.5, color="#a07800")
axes[1].text(0.5, 1150, r"$k_BT$ = 208 cm$^{-1}$", ha="center", va="bottom", fontsize=9.5, color="#a07800")
axes[2].text(0.5, kT + 14, "$k_BT$: several\nrungs are warm", ha="center", va="bottom", fontsize=9.5, color="#a07800",
             bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))
axes[3].text(0.5, 0.5 * 9e-14, "all of it lies\nbelow $k_BT$", ha="center", va="center", fontsize=10, color="#a07800",
             bbox=dict(fc="white", ec="none", alpha=0.8, pad=2))
for k, mag in zip(range(3), [r"$\times 6$", r"$\times 16$", r"$\times 10^{16}$"]):
    a, b = axes[k], axes[k + 1]
    top_a = panels[k][3]
    h = max(panels[k + 1][3], 0.012 * top_a)                # the next panel's range, drawn at least 1.2% tall
    a.add_patch(Rectangle((0.08, -0.012 * top_a), 0.84, h + 0.012 * top_a, fill=False, ec="k", lw=1.2, zorder=4))
    for ya, yb in ((h, 1.0), (-0.012 * top_a, 0.0)):
        fig.add_artist(ConnectionPatch(xyA=(0.92, ya), coordsA=a.transData, xyB=(0.0, yb), coordsB=b.transAxes,
                                       color=GRAY, lw=0.9, ls="--"))
    a.text(0.97, h + 0.02 * top_a, mag, ha="left", va="bottom", fontsize=10.5, color=GRAY, clip_on=False)
fig.subplots_adjust(left=0.09, right=0.985, top=0.83, bottom=0.11, wspace=0.62)
plt.show()
```

Fig. The energy levels of HCl. Each panel magnifies the lowest level of the panel to its left: under the lowest electronic level sit the vibrational levels, under the lowest vibrational level the rotational levels, and under the lowest rotational level the translational levels of the molecule in a 1 cm box. The yellow band is the thermal energy $k_BT$ at 300 K.

- A molecule absorbs light when the photon energy $h\nu$ matches a gap. The gaps span twenty orders of magnitude, so each ladder answers to its own part of the spectrum:

| motion | lowest gap in HCl | wavelength $1/\tilde{\nu}$ | spectroscopy |
|:--|:--|:--|:--|
| electronic | about 65 000 cm$^{-1}$ | about 150 nm | ultraviolet |
| vibrational | 2886 cm$^{-1}$ | 3.5 μm | infrared |
| rotational | 21 cm$^{-1}$ | 0.5 mm | microwave |
| translational | $10^{-15}$ cm$^{-1}$ | none | none: a continuum |

- Translational levels are so close that translation is classical in practice. Even at thermal energies, where the box quantum number is about $10^9$, neighboring levels are only $10^{-6}$ cm$^{-1}$ apart.
- The yellow band answers a second question: which motions does heat reach? At room temperature $k_BT = 208$ cm$^{-1}$, compared with the gaps above.

:::{note} **Example: which motions are awake at room temperature?**

By the Boltzmann distribution ([Appendix B](../physics/04-statistical-mechanics.md)), a state $\Delta E$ above the lowest one is populated relative to it by $e^{-\Delta E/k_BT}$. For HCl at 300 K, with $k_BT = 208$ cm$^{-1}$:

- **vibration**, $v = 1$: $e^{-2886/208} = e^{-13.9} \approx 10^{-6}$. One molecule in a million vibrates; the rest sit in $v = 0$.
- **rotation**, $J = 1$: $e^{-21.2/208} = e^{-0.10} = 0.90$. Many rotational levels are populated.
- **electronic**: $e^{-65\,000/208} \approx 10^{-136}$. Never, without light.

Molecules at room temperature fly and tumble freely, but their bonds sit in the lowest vibrational state.
:::

### Separating the motions

#### Born-Oppenheimer: nuclei move on a potential made by electrons

- An electron has $1/1836$ of a proton's mass and moves much faster than the nuclei. For each frozen arrangement of the nuclei, the electrons settle into a state with energy $E(\mathbf{R}_1, \dots, \mathbf{R}_N)$. The nuclei then move on this **potential energy surface**:

$$
\hat{H}_{\text{nuc}} = \sum_{i=1}^{N} -\frac{\hbar^2}{2m_i}\nabla_i^2 + E(\mathbf{R}_1, \dots, \mathbf{R}_N)
$$

- With no external field, $E$ depends only on the **shape** of the molecule (its bond lengths and angles), not on where the molecule is or which way it points. That is what lets the motions separate. The full story of this approximation is in [Chapter 8](../ch08/01-born-oppenheimer-approximation.md).

#### A sum of Hamiltonians gives a product of wavefunctions

- In the right coordinates (the center of mass, three angles for the orientation, and displacements that change the shape), the nuclear Hamiltonian splits into parts that act on different coordinates:

$$
\hat{H} = \hat{H}_{\text{trans}} + \hat{H}_{\text{rot}} + \hat{H}_{\text{vib}}
$$

- You have seen this before. The 3D box of [Lecture 3.2](../ch03/02-particle-in-a-box.md) had $\hat{H} = \hat{H}_x + \hat{H}_y + \hat{H}_z$, and its states were products $X(x)\,Y(y)\,Z(z)$ with $E = E_x + E_y + E_z$. The reason fits in one line. Let $\hat{H}_a$ act only on the coordinates of $\psi_a$ and $\hat{H}_b$ only on those of $\psi_b$. Each operator treats the other factor as a constant, so

$$
\hat{H}\,(\psi_a\psi_b) = (\hat{H}_a\psi_a)\,\psi_b + \psi_a\,(\hat{H}_b\psi_b) = E_a\,\psi_a\psi_b + E_b\,\psi_a\psi_b = (E_a + E_b)\,\psi_a\psi_b
$$

:::{important} **Separable Hamiltonian**

If $\hat{H} = \hat{H}_a + \hat{H}_b$, with $\hat{H}_a$ acting only on the coordinates of $a$ and $\hat{H}_b$ only on those of $b$, then

$$
\psi = \psi_a\,\psi_b, \qquad E = E_a + E_b
$$

where $\hat{H}_a\psi_a = E_a\psi_a$ and $\hat{H}_b\psi_b = E_b\psi_b$. For a molecule: $\psi = \psi_{\text{trans}}\,\psi_{\text{rot}}\,\psi_{\text{vib}}$ and $E = E_{\text{trans}} + E_{\text{rot}} + E_{\text{vib}}$.
:::

- One hard problem in $3N$ coordinates becomes several small ones. Probabilities multiply too, $\lvert\psi\rvert^2 = \lvert\psi_a\rvert^2\lvert\psi_b\rvert^2$: the motions are statistically independent.
- The separation is approximate. A spinning molecule stretches its bonds, and a vibrating bond changes how hard the molecule is to spin. These couplings show up as small corrections in spectra ([Lecture 4.5](05-rigid-rotor.md)).

### Counting coordinates

$N$ nuclei carry $3N$ coordinates, an $x$, $y$ and $z$ for each. Split them by motion:

- **3** for the center of mass (translation),
- **3** angles for the orientation (rotation), or only **2** for a linear molecule,
- the rest for the shape: $3N - 6$ **vibrations** for a nonlinear molecule, $3N - 5$ for a linear one.

Why does a linear molecule lose a rotation? Turn it about its own axis:

```{code-cell} python
:tags: [hide-input]
# synced: linear_rotations
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle
el, az = np.radians(16), np.radians(-32)                    # orthographic camera
Ry = np.array([[np.cos(az), 0, np.sin(az)], [0, 1, 0], [-np.sin(az), 0, np.cos(az)]])
Rx = np.array([[1, 0, 0], [0, np.cos(el), -np.sin(el)], [0, np.sin(el), np.cos(el)]])
view = Rx @ Ry
mols = [("H$_2$O, bent: 3 rotations",
         np.array([[0, 0.066, 0], [0.757, -0.520, 0], [-0.757, -0.520, 0]]),
         [0.27, 0.17, 0.17], [CARDINAL, "white", "white"], [(0, 1), (0, 2)]),
        ("CO$_2$, linear: 2 rotations",
         np.array([[0, 0, 0], [1.16, 0, 0], [-1.16, 0, 0]]),
         [0.25, 0.27, 0.27], ["#495057", CARDINAL, CARDINAL], [(0, 1), (0, 2)])]
axis_names = ["x", "y", "z"]
fig, axes = plt.subplots(2, 3, figsize=(9.0, 5.6))
phi = np.linspace(0, 2 * np.pi, 200)
for row, (label, P, rad, cols, bonds) in enumerate(mols):
    for c in range(3):
        ax = axes[row, c]
        ax.set_xlim(-1.75, 1.75); ax.set_ylim(-1.45, 1.45); ax.set_aspect("equal"); ax.axis("off")
        e = np.eye(3)[c]
        Q = (view @ P.T).T
        dist = np.linalg.norm(P - np.outer(P @ e, e), axis=1)
        still = dist.max() < 0.02
        acol = CARDINAL if still else TEAL
        ends = view @ np.array([-1.3 * e, 1.3 * e]).T
        ax.plot(ends[0], ends[1], color=acol, lw=1.6, ls="--", zorder=1)
        lab = view @ ((1.72 if c == 0 else 1.45) * e)       # the x label clears the CO2 oxygen
        ax.text(lab[0], lab[1], axis_names[c], color=acol, fontsize=12.5, style="italic", ha="center", va="center")
        for p, d in zip(P, dist):
            if d > 0.02:
                perp = p - (p @ e) * e
                orbit = np.outer(p @ e, e) + np.outer(np.cos(phi), perp) + np.outer(np.sin(phi), np.cross(e, perp))
                o2 = (view @ orbit.T)
                ax.plot(o2[0], o2[1], color=TEAL, lw=1.3, alpha=0.75, zorder=1)
                j = 60
                ax.annotate("", xy=(o2[0, j + 6], o2[1, j + 6]), xytext=(o2[0, j], o2[1, j]),
                            arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.3, mutation_scale=12))
        for a, b in bonds:
            ax.plot([Q[a, 0], Q[b, 0]], [Q[a, 1], Q[b, 1]], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
        for j in np.argsort(Q[:, 2]):
            ax.add_patch(Circle((Q[j, 0], Q[j, 1]), rad[j], fc=cols[j], ec="k", lw=1, zorder=3 + Q[j, 2]))
        if still:
            ax.text(0, -0.95, "every atom sits on the axis:\nnothing moves, nothing to count",
                    ha="center", va="center", fontsize=11, color=CARDINAL)
        ax.set_title(f"turn about {axis_names[c]}", fontsize=12, color=acol)
    axes[row, 0].text(-1.75, 1.75, label, fontsize=13.5, weight="bold", ha="left", va="bottom")
fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.01, hspace=0.42, wspace=0.04)
plt.show()
```

Fig. Turning a molecule about three perpendicular axes through its center of mass. Water (top) moves atoms in all three turns, so it has three distinct rotations. In CO$_2$ (bottom) every nucleus sits on the axis $x$, so a turn about $x$ moves nothing and gives no new orientation. The coordinate that rotation does not use goes to the vibrations.

:::{note} **Example: counting the vibrations**

| molecule | shape | $N$ | $3N$ | translation | rotation | vibration |
|:--|:--|:-:|:-:|:-:|:-:|:-:|
| H$_2$O | bent | 3 | 9 | 3 | 3 | **3** |
| CO$_2$ | linear | 3 | 9 | 3 | 2 | **4** |
| CH$_4$ | tetrahedral | 5 | 15 | 3 | 3 | **9** |
| benzene | planar | 12 | 36 | 3 | 3 | **30** |

Benzene's 30 vibrations are why its infrared spectrum is so rich.
:::

- Each vibration is a **normal mode**: a pattern in which all the atoms swing at one frequency, in step, while the center of mass stays put. Water's three:

```{code-cell} python
:tags: [hide-input]
# synced: water_modes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle
m = np.array([16.0, 16.0, 1.0, 1.0, 1.0, 1.0])              # O (x, y), H1 (x, y), H2 (x, y) in u
re, th0 = 0.958, np.radians(104.5)                          # angstrom, equilibrium angle
kr, kt = 8.45, 0.76                                         # stretch (mdyn/A) and bend (mdyn A/rad^2) force constants
q0 = np.array([0, 0, re * np.sin(th0 / 2), -re * np.cos(th0 / 2), -re * np.sin(th0 / 2), -re * np.cos(th0 / 2)])
bl = lambda q, j: np.hypot(q[j] - q[0], q[j + 1] - q[1])
ang = lambda q: np.arccos(((q[2] - q[0]) * (q[4] - q[0]) + (q[3] - q[1]) * (q[5] - q[1])) / (bl(q, 2) * bl(q, 4)))
V = lambda q: 0.5 * kr * ((bl(q, 2) - re)**2 + (bl(q, 4) - re)**2) + 0.5 * kt * (ang(q) - th0)**2
Hs, e, I6 = np.zeros((6, 6)), 1e-4, np.eye(6)
for i in range(6):                                          # Hessian by central differences
    for j in range(6):
        Hs[i, j] = (V(q0 + e * I6[i] + e * I6[j]) - V(q0 + e * I6[i] - e * I6[j])
                    - V(q0 - e * I6[i] + e * I6[j]) + V(q0 - e * I6[i] - e * I6[j])) / (4 * e * e)
w2, vec = np.linalg.eigh(Hs / np.sqrt(np.outer(m, m)))      # mass-weighted: three zeros (2 shifts, 1 turn), then 3 modes
d = vec[:, 3:] / np.sqrt(m)[:, None]
bend, s1, s2 = 0, 1, 2
asym = s1 if abs(d[0, s1]) > abs(d[0, s2]) else s2          # only the antisymmetric stretch moves O sideways
sym = s2 if asym == s1 else s1
order = [(sym, "symmetric stretch", 3657, 2), (bend, "bend", 1595, 1), (asym, "antisymmetric stretch", 3756, 2)]
nf = 36
ts = np.arange(nf) / nf
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.3))
parts = []
for ax, (k, name, wn, cyc) in zip(axes, order):
    dk = d[:, k] / np.abs(d[2:, k]).max() * 0.2             # the H atoms swing 0.2 A (exaggerated)
    dk = dk * (np.sign(dk[2] * q0[2] + dk[3] * q0[3]) or 1)  # start with H1 moving out along its bond
    ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.2, 0.55); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(name, fontsize=13, color=TEAL, weight="bold")
    ax.text(0, -1.17, rf"{wn} cm$^{{-1}}$", ha="center", va="bottom", fontsize=12)
    for j in range(3):                                      # equilibrium ghost and the direction of motion
        ax.add_patch(Circle((q0[2 * j], q0[2 * j + 1]), 0.27 if j == 0 else 0.17, fc="none", ec="#ced4da", lw=1, ls="--"))
        if np.hypot(dk[2 * j], dk[2 * j + 1]) > 0.02:
            ax.annotate("", xy=(q0[2 * j] + 2.2 * dk[2 * j], q0[2 * j + 1] + 2.2 * dk[2 * j + 1]),
                        xytext=(q0[2 * j] + 1.25 * dk[2 * j], q0[2 * j + 1] + 1.25 * dk[2 * j + 1]),
                        arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.6, mutation_scale=13), zorder=1)
    (b1,) = ax.plot([], [], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
    (b2,) = ax.plot([], [], color="#adb5bd", lw=5, zorder=2, solid_capstyle="round")
    cO = Circle((0, 0), 0.27, fc=CARDINAL, ec="k", lw=1, zorder=3); ax.add_patch(cO)
    cH1 = Circle((0, 0), 0.17, fc="white", ec="k", lw=1, zorder=3); ax.add_patch(cH1)
    cH2 = Circle((0, 0), 0.17, fc="white", ec="k", lw=1, zorder=3); ax.add_patch(cH2)
    parts.append((dk, cyc, b1, b2, cO, cH1, cH2))
fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.02, wspace=0.05)

def update(i):
    for dk, cyc, b1, b2, cO, cH1, cH2 in parts:
        q = q0 + np.sin(2 * np.pi * cyc * ts[i]) * dk
        cO.center, cH1.center, cH2.center = (q[0], q[1]), (q[2], q[3]), (q[4], q[5])
        b1.set_data([q[0], q[2]], [q[1], q[3]]); b2.set_data([q[0], q[4]], [q[1], q[5]])

ani = FuncAnimation(fig, update, frames=nf, interval=75, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. The three normal modes of water with their measured frequencies (gas phase). Dashed circles mark the equilibrium positions and arrows the direction of motion; the amplitudes are exaggerated. The modes are computed from a model with two bond springs and one angle spring.

- Near equilibrium each normal mode behaves as an independent harmonic oscillator, so a molecule is $3N - 6$ independent springs. How to find the modes, and which ones absorb infrared light, is the subject of [Molecular Vibrations](03-molecular-vibrations.md).

### Three motions, three model systems

```{code-cell} python
:tags: [hide-input]
# synced: model_map
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import FancyBboxPatch
W, Ht = 10.1, 4.75
fig = plt.figure(figsize=(W, Ht))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, Ht); ax.axis("off")
tint = {GRAY: "#f1f3f5", PURPLE: "#f1ecf7", TEAL: "#e3f1f5", ORANGE: "#fdf0e0", "k": "#f8f9fa"}
xm, xo, xd, xl, xs = 0.9, 3.45, 6.0, 7.55, 8.2              # columns: molecule, motion, model, ladder, spectroscopy
rows = [(3.65, ORANGE, "electrons", "make the potential E(R)", "atoms and orbitals", "Chapters 5 to 8",
         [1 - 1 / n**2 for n in range(1, 5)], "UV-visible", r"$10^4$ to $10^5$ cm$^{-1}$"),
        (2.6, GRAY, "translation", "center of mass: 3", "particle in a box", "Lecture 3.2",
         [(n * n - 1) / 15 for n in range(1, 5)], "none: a continuum", r"$10^{-15}$ cm$^{-1}$"),
        (1.55, PURPLE, "rotation", "orientation: 3 (linear: 2)", "rigid rotor", "Lectures 4.4, 4.5",
         [J * (J + 1) / 12 for J in range(4)], "microwave", r"1 to 20 cm$^{-1}$"),
        (0.5, TEAL, "vibration", r"shape: $3N-6$ (or $3N-5$)", "harmonic oscillator", "Lectures 4.2, 4.3",
         [v / 3 for v in range(4)], "infrared", r"$10^3$ cm$^{-1}$")]

def box(x, y, w, h, title, line, col):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=tint[col], ec=col, lw=1.6, zorder=2))
    ax.text(x, y + 0.13, title, ha="center", va="center", fontsize=12.5, color=col, weight="bold", zorder=3)
    ax.text(x, y - 0.17, line, ha="center", va="center", fontsize=11.5, zorder=3)

for x, head in ((xo, "motion"), (xd, "model system"), (xl + 0.25, "levels"), (xs + 0.6, "spectroscopy")):
    ax.text(x, 4.42, head, ha="center", fontsize=11.5, color=GRAY, style="italic")
ax.add_patch(FancyBboxPatch((xm - 0.72, 1.45), 1.44, 1.3, boxstyle="round,pad=0,rounding_size=0.1",
                            fc="#f8f9fa", ec="k", lw=1.6, zorder=2))
ax.text(xm, 2.38, "a molecule", ha="center", va="center", fontsize=12.5, weight="bold")
ax.text(xm, 2.0, "N nuclei", ha="center", va="center", fontsize=11.5)
ax.text(xm, 1.7, "n electrons", ha="center", va="center", fontsize=11.5)
for y, col, motion, mline, model, mlect, lev, spec, gap in rows:
    ax.annotate("", xy=(xo - 1.1, y), xytext=(xm + 0.74, 2.1), zorder=1,
                arrowprops=dict(arrowstyle="-|>", color=col, lw=1.5, mutation_scale=15, shrinkA=0, shrinkB=2))
    box(xo, y, 2.2, 0.72, motion, mline, col)
    ax.annotate("", xy=(xd - 1.08, y), xytext=(xo + 1.1, y), zorder=1,
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4, mutation_scale=14, shrinkA=2, shrinkB=2))
    box(xd, y, 2.12, 0.72, model, mlect, col)
    ax.hlines([y - 0.3 + 0.6 * v for v in lev], xl, xl + 0.5, color=col, lw=2)
    ax.text(xs, y + 0.13, spec, ha="left", va="center", fontsize=12, color=col, weight="bold")
    ax.text(xs, y - 0.17, gap, ha="left", va="center", fontsize=11)
ax.text(1.4, 3.3, "Born-\nOppenheimer", ha="center", va="center", fontsize=10.5, color=GRAY, style="italic")
ax.text(1.4, 0.85, "nuclei move\non E(R)", ha="center", va="center", fontsize=10.5, color=GRAY, style="italic")
plt.show()
```

Fig. The plan of this chapter. The Born-Oppenheimer approximation splits off the electrons, which make the potential $E(R)$ the nuclei move on. Each nuclear motion has its own model system, its own pattern of levels and its own spectroscopy.

For a diatomic molecule the three models look like this; you will derive the levels of the last two in the coming lectures:

| motion | coordinates | classical energy | model system | energy levels |
|:--|:--|:--|:--|:--|
| translation | center of mass | $\dfrac{P^2}{2M}$ | particle in a box ([3.2](../ch03/02-particle-in-a-box.md)) | $\dfrac{h^2n^2}{8ML^2}$ |
| rotation | two angles $\theta$, $\phi$ | $\dfrac{L^2}{2I}$, $\ I = \mu R_e^2$ | rigid rotor ([4.5](05-rigid-rotor.md)) | $\dfrac{\hbar^2}{2I}\,J(J+1)$ |
| vibration | stretch $x = R - R_e$ | $\dfrac{p^2}{2\mu} + \dfrac{1}{2}kx^2$ | harmonic oscillator ([4.2](02-quantum-harmonic-oscillator.md)) | $\hbar\omega\left(v + \tfrac{1}{2}\right)$ |

- $M$ is the total mass, $L$ the angular momentum, $I$ the moment of inertia, and $\mu$ the reduced mass of the two atoms (defined below).
- The recipe is the one from Chapter 3: write the classical energy, turn it into an operator, solve $\hat{H}\psi = E\psi$.
- Translation needs nothing new: a molecule in a container is a particle in a 3D box of mass $M$.
- Rotation has no potential at all. Its levels are quantized because an angle comes back to itself after a full turn, a periodic boundary condition.
- Vibration is where the potential $E(R)$ lives. The rest of this lecture builds the classical spring that [Lecture 4.2](02-quantum-harmonic-oscillator.md) quantizes.

### Why every bond is a spring

The potential energy of HCl as a function of its bond length $R$:

```{code-cell} python
:tags: [hide-input]
# synced: bond_parabola
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Rectangle, ConnectionPatch
D, a, re = 4.62, 1.87, 1.275                                # HCl: well depth (eV), Morse range (1/A), bond length (A)
hw = 0.3708                                                 # hbar omega = 2991 cm^-1, from k = 2 D a^2 = 518 N/m
xe = hw**2 / (4 * D)                                        # Morse anharmonicity (eV)
r = np.linspace(0.75, 4.2, 800)
U = D * (1 - np.exp(-a * (r - re)))**2
k = 2 * D * a * a                                           # curvature at the bottom, eV/A^2
P = 0.5 * k * (r - re)**2
G = lambda v: hw * (v + 0.5) - xe * (v + 0.5)**2
turn = lambda E: (re - np.log(1 + np.sqrt(E / D)) / a, re - np.log(1 - np.sqrt(E / D)) / a)
fig, (ax, az) = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"width_ratios": [1.5, 1], "wspace": 0.25})
for v in range(24):
    E = G(v)
    if E < D:
        r1, r2 = turn(E)
        ax.hlines(E, r1, r2, color=TEAL if v < 3 else "#adb5bd", lw=1.6 if v < 3 else 0.9, zorder=2)
ax.plot(r, U, color="k", lw=2.4, zorder=3, label="true potential (Morse fit)")
ax.plot(r, P, color=ORANGE, lw=2.2, ls="--", zorder=3, label=r"parabola $\frac{1}{2}k(R - R_e)^2$")
ax.axhline(D, color=GRAY, lw=1, ls=":")
ax.text(4.15, D + 0.08, r"$D_e$ = 4.6 eV: the atoms come apart", ha="right", va="bottom", fontsize=10.5, color=GRAY)
ax.set_xlim(0.75, 4.2); ax.set_ylim(-0.15, 5.6)
ax.set_xlabel(r"bond length $R$ ($\AA$)", fontsize=11.5); ax.set_ylabel("energy (eV)", fontsize=11.5)
ax.legend(loc="lower right", frameon=False, fontsize=10.5)
ax.set_title("HCl: the potential the nuclei move on", loc="left", fontsize=12)
ax.add_patch(Rectangle((1.02, -0.06), 0.56, 1.36, fill=False, ec="k", lw=1.1, zorder=4))
rz = np.linspace(1.0, 1.6, 300)
az.plot(rz, D * (1 - np.exp(-a * (rz - re)))**2, color="k", lw=2.4)
az.plot(rz, 0.5 * k * (rz - re)**2, color=ORANGE, lw=2.2, ls="--")
for v in range(3):
    r1, r2 = turn(G(v))
    az.hlines(G(v), r1, r2, color=TEAL, lw=2)
    az.text(r1 + 0.012, G(v) + 0.025, rf"$v = {v}$", va="bottom", ha="left", fontsize=11, color=TEAL)
az.set_xlim(1.0, 1.6); az.set_ylim(-0.04, 1.3)
az.set_xlabel(r"$R$ ($\AA$)", fontsize=11.5)
az.set_title("zoom: the bottom is a parabola", loc="left", fontsize=12)
for ya, yb in ((1.3, 1.0), (-0.06, 0.0)):
    fig.add_artist(ConnectionPatch(xyA=(1.58, ya), coordsA=ax.transData, xyB=(0.0, yb), coordsB=az.transAxes,
                                   color=GRAY, lw=0.9, ls="--"))
for s in (ax, az):
    s.spines["top"].set_visible(False); s.spines["right"].set_visible(False)
fig.subplots_adjust(left=0.07, right=0.985, top=0.91, bottom=0.14)
plt.show()
```

Fig. Left: the potential energy of HCl against bond length, a Morse curve fitted to HCl (black), and the parabola with the same curvature at the minimum (orange, dashed). Gray lines are the vibrational levels of the Morse well; the lowest three are teal. Right: near the bottom the two curves agree, and that is where the lowest levels live.

- Expand the potential in a Taylor series about the equilibrium bond length $R_e$, with $x = R - R_e$:

$$
U(R) = U(R_e) + U'(R_e)\,x + \frac{1}{2}U''(R_e)\,x^2 + \frac{1}{6}U'''(R_e)\,x^3 + \dots
$$

- Measure energy from the bottom of the well, so $U(R_e) = 0$. At a minimum the slope vanishes, so $U'(R_e) = 0$. The first term that survives is the quadratic one:

:::{important} **The harmonic approximation**

$$
U(R) \approx \frac{1}{2}k\,(R - R_e)^2, \qquad k = \left.\frac{d^2U}{dR^2}\right|_{R_e}
$$

The **force constant** $k$ is the curvature of the potential at its minimum: a stiff bond sits in a sharply curved well.
:::

- The cubic and higher terms are the **anharmonicity**. They matter for large stretches (high levels, bond breaking), not for the lowest levels; [Lecture 4.3](03-molecular-vibrations.md) adds them back. Problem 4 finds $k$ for the Morse curve of HCl: $516$ N/m.

### The classical harmonic oscillator

#### Hooke's law and Newton's equation

- The force is minus the slope of the potential, $F = -dU/dx = -kx$ (**Hooke's law**): a stretched spring pulls back, a compressed one pushes out. Newton's second law gives

$$
m\ddot{x} = -kx \qquad\Longrightarrow\qquad \ddot{x} = -\omega^2 x, \qquad \omega = \sqrt{\frac{k}{m}}
$$

- Which function comes back as minus itself after two derivatives? Cosine and sine. Check $x(t) = A\cos(\omega t + \phi)$:

$$
\dot{x} = -A\omega\sin(\omega t + \phi), \qquad \ddot{x} = -A\omega^2\cos(\omega t + \phi) = -\omega^2 x \quad\checkmark
$$

- The **amplitude** $A$ and the **phase** $\phi$ come from the starting conditions: a mass released from rest at $x = A$ has $\phi = 0$. (Shifting $\phi$ by $\pi/2$ turns the cosine into the sine you may have seen elsewhere.)
- The period is $T = 2\pi/\omega$. A stiffer spring oscillates faster, a heavier mass slower:

```{code-cell} python
:tags: [hide-input]
# synced: spring_masses
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
nf, A, wall = 48, 0.9, -2.6
ts = np.linspace(0, 2, nf, endpoint=False)                  # time in periods T of the light mass
zig = np.zeros(70); zig[4:-4] = 0.2 * (2 * np.abs((np.arange(62) / 4.0) % 1 - 0.5) * 2 - 1)
rows = [("mass $m$", TEAL, 1.0, 0.42), (r"mass $4m$, same spring", PURPLE, 0.5, 0.62)]
fig, axes = plt.subplots(2, 2, figsize=(9.0, 3.9), gridspec_kw={"width_ratios": [1, 1.25], "hspace": 0.55, "wspace": 0.12})
parts = []
tt = np.linspace(0, 2, 400)
for (ax, ax2), (name, col, w, size) in zip(axes, rows):
    ax.axvline(wall, color="k", lw=5)
    ax.axhline(-0.5, color=GRAY, lw=0.8)
    ax.axvline(0, color=GRAY, lw=1, ls=":")
    (spring,) = ax.plot([], [], color=GRAY, lw=1.5)
    (block,) = ax.fill([0, 0, 0, 0], [0, 0, 0, 0], color=col, alpha=0.9)
    ax.set_xlim(wall - 0.1, 1.75); ax.set_ylim(-0.55, 0.85); ax.axis("off")
    ax.set_title(name, loc="left", fontsize=12.5, color=col, weight="bold")
    ax2.plot(tt, A * np.cos(2 * np.pi * w * tt), color="#dee2e6", lw=1.6)
    (trace,) = ax2.plot([], [], color=col, lw=2.4)
    (dot,) = ax2.plot([], [], "o", color=col, ms=8)
    ax2.axhline(0, color=GRAY, lw=0.6)
    ax2.set_xlim(0, 2); ax2.set_ylim(-1.15, 1.15); ax2.set_yticks([-A, 0, A]); ax2.set_yticklabels(["-A", "0", "A"])
    ax2.set_xticks([0, 1, 2]); ax2.set_xticklabels(["0", "T", "2T"])
    ax2.set_ylabel("x(t)", fontsize=11)
    parts.append((w, size, spring, block, trace, dot))
axes[0, 1].set_title(r"$\omega = \sqrt{k/m}$: period $T$", loc="left", fontsize=12, color=TEAL)
axes[1, 1].set_title(r"$\omega = \sqrt{k/4m}$: half as fast, period $2T$", loc="left", fontsize=12, color=PURPLE)
axes[1, 1].set_xlabel("time", fontsize=11)
fig.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.13)

def update(i):
    for w, size, spring, block, trace, dot in parts:
        x = A * np.cos(2 * np.pi * w * ts[i])
        spring.set_data(np.linspace(wall, x - size / 2, 70), zig + 0.05)
        block.set_xy([[x - size / 2, -0.5], [x + size / 2, -0.5], [x + size / 2, -0.5 + size * 1.2], [x - size / 2, -0.5 + size * 1.2]])
        sel = tt <= ts[i] + 1e-9
        trace.set_data(tt[sel], A * np.cos(2 * np.pi * w * tt[sel]))
        dot.set_data([ts[i]], [x])

ani = FuncAnimation(fig, update, frames=nf, interval=70, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Two masses on the same spring, both released from rest at $x = A$. Quadrupling the mass halves $\omega = \sqrt{k/m}$, so the heavy mass completes one swing while the light one completes two.

#### Energy sloshes, the total stays

- The potential energy is $V = \frac{1}{2}kx^2$ and the kinetic energy $K = p^2/2m$ with $p = m\dot{x}$. Insert the solution and use $m\omega^2 = k$:

$$
K + V = \frac{1}{2}m A^2\omega^2\sin^2(\omega t + \phi) + \frac{1}{2}kA^2\cos^2(\omega t + \phi) = \frac{1}{2}kA^2
$$

:::{important} **Classical harmonic oscillator**

$$
x(t) = A\cos(\omega t + \phi), \qquad \omega = \sqrt{\frac{k}{m}}, \qquad E = \frac{p^2}{2m} + \frac{1}{2}kx^2 = \frac{1}{2}kA^2
$$
:::

```{code-cell} python
:tags: [hide-input]
# synced: energy_slosh
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
nf, E = 36, 0.5                                             # k = m = A = 1: E = 1/2
ts = np.arange(nf) / nf                                     # one period
x = np.linspace(-1.35, 1.35, 300)
fig, (ax, axb) = plt.subplots(1, 2, figsize=(8.4, 3.5), gridspec_kw={"width_ratios": [2.4, 1], "wspace": 0.3})
ax.plot(x, 0.5 * x**2, color="k", lw=2.2)
ax.axhline(E, color=CARDINAL, lw=1.6, ls="--")
ax.text(1.33, E + 0.02, "E", color=CARDINAL, fontsize=13, ha="right", va="bottom")
ax.text(0, 0.88, r"$V = \frac{1}{2}kx^2$", fontsize=13, ha="center", va="top")
for s in (-1, 1):
    ax.axvline(s, color=GRAY, lw=0.8, ls=":")
ax.text(-1, -0.075, "turning\npoint", ha="center", va="top", fontsize=10, color=GRAY)
ax.text(1, -0.075, "turning\npoint", ha="center", va="top", fontsize=10, color=GRAY)
(vbar,) = ax.plot([], [], color=TEAL, lw=7, solid_capstyle="butt")
(kbar,) = ax.plot([], [], color=ORANGE, lw=7, solid_capstyle="butt")
(ball,) = ax.plot([], [], "o", color="k", ms=13, zorder=5)
ax.set_xlim(-1.4, 1.4); ax.set_ylim(-0.25, 0.92); ax.set_yticks([]); ax.set_xticks([])
ax.spines["left"].set_visible(False); ax.set_xlabel("position x", fontsize=11.5)
bv = axb.bar([0], [0], width=0.6, color=TEAL, label=r"potential $V$")[0]
bk = axb.bar([0], [0], width=0.6, color=ORANGE, label=r"kinetic $K = \frac{p^2}{2m}$")[0]
axb.axhline(E, color=CARDINAL, lw=1.6, ls="--")
axb.axhline(0, color="k", lw=0.8)
axb.set_xlim(-0.6, 0.6); axb.set_ylim(-0.25, 0.92); axb.set_xticks([]); axb.set_yticks([])   # same heights as the left panel
axb.spines["left"].set_visible(False); axb.spines["bottom"].set_visible(False)
axb.legend(loc="upper center", frameon=False, fontsize=11, bbox_to_anchor=(0.5, 1.02))
axb.set_xlabel(r"$E = K + V$", fontsize=12.5)
fig.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.17)

def update(i):
    xi = np.cos(2 * np.pi * ts[i])
    V = 0.5 * xi**2
    vbar.set_data([xi, xi], [0, V]); kbar.set_data([xi, xi], [V, E]); ball.set_data([xi], [V])
    bv.set_height(V); bk.set_y(V); bk.set_height(E - V)

ani = FuncAnimation(fig, update, frames=nf, interval=85, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. A mass oscillating in the parabolic well $V = \frac{1}{2}kx^2$. At each position the total energy $E$ splits into potential (teal) and kinetic (orange) parts. The split changes twice per period; the total never does.

- At the **turning points** $x = \pm A$ all the energy is potential and the mass is momentarily at rest. Beyond them $V > E$, so a classical oscillator never goes there. (The quantum one will, as in the [finite well](../ch03/03-tunneling-and-finite-square-well.md).)
- The energy written with $p$ instead of the velocity is the **Hamiltonian**, the function that Lecture 4.2 turns into an operator. Its phase-space picture is in [Appendix B](../physics/01-classical-mechanics.md).

#### Where is a classical oscillator found?

- Take snapshots at random times and record the position. The mass is fastest in the middle and slowest near the turning points, so it is caught most often near $\pm A$.
- The chance of catching it in a strip $dx$ is the fraction of the period it spends there. It crosses each strip twice per period, taking $dt = dx/\lvert\dot{x}\rvert$ each time, with $\lvert\dot{x}\rvert = \omega\sqrt{A^2 - x^2}$ and $T = 2\pi/\omega$:

$$
P(x)\,dx = \frac{2\,dt}{T} = \frac{dx}{\pi\sqrt{A^2 - x^2}}, \qquad -A < x < A
$$

```{code-cell} python
:tags: [hide-input]
# synced: spring_histogram
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
rng = np.random.default_rng(2)
A = 1.0
xs = A * np.cos(2 * np.pi * rng.random(5000))               # snapshots at random times
yj = rng.random(5000)
counts = np.unique(np.round(np.geomspace(1, 5000, 40)).astype(int))
counts = np.concatenate([counts, np.full(8, counts[-1])])
edges = np.linspace(-1.25, 1.25, 41); mid = 0.5 * (edges[1:] + edges[:-1]); dx = edges[1] - edges[0]
xc = np.linspace(-0.999, 0.999, 600)
fig, (ta, ha) = plt.subplots(2, 1, figsize=(8.0, 3.9), sharex=True, gridspec_kw={"height_ratios": [1, 2.3], "hspace": 0.12})
for ax in (ta, ha):
    ax.axvspan(-1.25, -A, color=GRAY, alpha=0.1, lw=0); ax.axvspan(A, 1.25, color=GRAY, alpha=0.1, lw=0)
    ax.axvline(-A, color=GRAY, lw=1, ls=":"); ax.axvline(A, color=GRAY, lw=1, ls=":")
ta.set_ylim(0, 1); ta.set_yticks([]); ta.spines["left"].set_visible(False); ta.tick_params(bottom=False)
ta.set_title("a mass on a spring; each dot is a snapshot at a random time", loc="left", fontsize=11.5)
scat = ta.scatter([], [], s=4, color=TEAL, alpha=0.5, lw=0)
(ball,) = ta.plot([], [], "o", color=ORANGE, ms=13, zorder=5)
bars = ha.bar(mid, 0 * mid, width=0.9 * dx, color=TEAL, alpha=0.55)
(pc,) = ha.plot([], [], color=CARDINAL, lw=2.4, label=r"$P(x) = \dfrac{1}{\pi\sqrt{A^2 - x^2}}$")
ha.set_xlim(-1.25, 1.25); ha.set_yticks([])
ha.set_xticks([-A, 0, A]); ha.set_xticklabels(["-A", "0", "A"]); ha.set_xlabel("position x", fontsize=11.5)
ha.set_ylabel("times found here", fontsize=11)
ha.legend(loc="upper center", frameon=False, fontsize=12)
ha.text(-1.235, 0.03, "never\nfound", transform=ha.get_xaxis_transform(), fontsize=10, color=GRAY, va="bottom")
ha.text(1.235, 0.03, "never\nfound", transform=ha.get_xaxis_transform(), fontsize=10, color=GRAY, va="bottom", ha="right")
fig.subplots_adjust(left=0.05, right=0.99, top=0.85, bottom=0.14)
sup = fig.suptitle("", fontsize=12, x=0.99, ha="right")

def update(i):
    N = counts[i]
    scat.set_offsets(np.column_stack([xs[:N], yj[:N]]))
    ball.set_data([A * np.cos(2 * np.pi * i / 13)], [0.5])
    h = np.histogram(xs[:N], bins=edges)[0]
    for b, c in zip(bars, h):
        b.set_height(c)
    pc.set_data(xc, N * dx / (np.pi * np.sqrt(A * A - xc**2)))
    ha.set_ylim(0, 1.25 * max(3.0, h.max(), N * dx * 0.9))
    sup.set_text(f"N = {N} snapshot" + ("" if N == 1 else "s"))

ani = FuncAnimation(fig, update, frames=len(counts), interval=140, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Snapshots of a mass on a spring taken at random times. Top: each dot is one snapshot. Bottom: the snapshots pile up into the classical probability density $P(x)$, which is smallest in the middle and largest at the turning points. Nothing is ever found beyond them.

- Keep this picture for the next lecture. The quantum oscillator in its lowest state is found most often in the middle, where the classical one is found least, and sometimes beyond the turning points. At high energies the quantum density approaches this classical curve, just as the box did at large $n$.

#### A diatomic is one bead with the reduced mass

- Two atoms, $m_1$ at $x_1$ and $m_2$ at $x_2$, joined by a spring of rest length $R_e$. The stretch is $x = x_2 - x_1 - R_e$. When it is positive the spring pulls the atoms together:

$$
m_1\ddot{x}_1 = +kx, \qquad m_2\ddot{x}_2 = -kx
$$

- **Add** the two equations: $m_1\ddot{x}_1 + m_2\ddot{x}_2 = 0$. The center of mass $X = (m_1x_1 + m_2x_2)/(m_1 + m_2)$ has $\ddot{X} = 0$, so it drifts at constant velocity: that is translation, which needs no spring.
- **Divide** each equation by its mass and subtract:

$$
\ddot{x} = \ddot{x}_2 - \ddot{x}_1 = -\left(\frac{1}{m_1} + \frac{1}{m_2}\right)kx = -\frac{k}{\mu}\,x
$$

:::{important} **Reduced mass**

$$
\mu = \frac{m_1m_2}{m_1 + m_2}, \qquad \mu\ddot{x} = -kx, \qquad \omega = \sqrt{\frac{k}{\mu}}
$$

The stretch of a vibrating diatomic moves exactly like one bead of mass $\mu$ on a spring attached to a wall.
:::

```{code-cell} python
:tags: [hide-input]
# synced: two_body
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
nf = 32
ts = np.arange(nf) / nf                                     # one period
m1, m2, re, A = 12.0, 16.0, 2.2, 0.55                       # C and O (u), bond and stretch amplitude in drawing units
M, mu = m1 + m2, m1 * m2 / (m1 + m2)
zig = np.zeros(70); zig[4:-4] = 0.16 * (2 * np.abs((np.arange(62) / 4.0) % 1 - 0.5) * 2 - 1)
fig, (ax, bx) = plt.subplots(2, 1, figsize=(8.0, 3.4), gridspec_kw={"hspace": 0.5})
for a in (ax, bx):
    a.set_xlim(-2.6, 2.6); a.set_ylim(-0.55, 0.65); a.axis("off"); a.axhline(-0.48, color=GRAY, lw=0.8)
eq1, eq2 = -m2 / M * re, m1 / M * re
ax.axvline(eq1, color=GRAY, lw=1, ls=":"); ax.axvline(eq2, color=GRAY, lw=1, ls=":")
ax.plot([0], [-0.43], "^", color="k", ms=11)
ax.text(0.08, -0.36, "center of mass", fontsize=10, color="k", va="bottom")
ax.set_title(r"C (12 u) and O (16 u): each atom moves; the lighter one moves farther", loc="left", fontsize=12)
(s1,) = ax.plot([], [], color=GRAY, lw=1.5)
(a1,) = ax.plot([], [], "o", color="#495057", ms=26, mec="k")
(a2,) = ax.plot([], [], "o", color=CARDINAL, ms=29, mec="k")
wall = -2.1
bx.axvline(wall, color="k", lw=5)
bx.axvline(wall + re, color=GRAY, lw=1, ls=":")
bx.set_title(rf"one bead of reduced mass $\mu$ = {mu:.2f} u on a wall: the same stretch $x(t)$", loc="left", fontsize=12)
(s2,) = bx.plot([], [], color=GRAY, lw=1.5)
(bead,) = bx.plot([], [], "o", color=TEAL, ms=24, mec="k")
(arr,) = bx.plot([], [], color=ORANGE, lw=3)
(d1,) = ax.plot([], [], color=ORANGE, lw=3)                 # each atom's own displacement
(d2,) = ax.plot([], [], color=ORANGE, lw=3)
bx.text(wall + re + 0.75, 0.32, "x", color=ORANGE, fontsize=13, style="italic")
fig.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.03)

def update(i):
    x = A * np.sin(2 * np.pi * ts[i])
    p1, p2 = eq1 - m2 / M * x, eq2 + m1 / M * x
    a1.set_data([p1], [0]); a2.set_data([p2], [0])
    s1.set_data(np.linspace(p1, p2, 70), zig)
    bead.set_data([wall + re + x], [0])
    s2.set_data(np.linspace(wall, wall + re + x, 70), zig)
    arr.set_data([wall + re, wall + re + x], [0.3, 0.3])
    d1.set_data([eq1, p1], [0.42, 0.42]); d2.set_data([eq2, p2], [0.42, 0.42])

ani = FuncAnimation(fig, update, frames=nf, interval=80, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Top: carbon monoxide vibrating about its fixed center of mass (triangle); the orange bars are each atom's displacement. The lighter carbon moves farther, in the ratio $16:12$. Bottom: one bead of mass $\mu$ on a wall, whose displacement is the change in bond length.

- $\mu$ is smaller than either mass. When one atom is much heavier, $\mu$ is close to the lighter mass and the heavy atom acts as the wall. In HCl, $\mu = 0.980$ u, within 3% of the mass of H: hydrogen does nearly all the moving. That is why bonds to hydrogen vibrate fast (2800 to 3700 cm$^{-1}$), and why replacing H by D slows them by almost $\sqrt{2}$ (Problem 3).
- The same $\mu$ sets how hard a diatomic is to spin: its moment of inertia is $I = \mu R_e^2$ ([Lecture 4.5](05-rigid-rotor.md)).

### Preview: the quantum spring

Replace the momentum by $-i\hbar\,d/dx$ and the classical energy becomes the Hamiltonian of [Lecture 4.2](02-quantum-harmonic-oscillator.md):

$$
\hat{H} = -\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2} + \frac{1}{2}kx^2
$$

You have solved it already, with the trial-energy slider of [Lecture 3.1](../ch03/01-schrodinger-equation.md) and with the five lines of numpy of [Lecture 3.5](../ch03/04-operators.md). Here they are again, in units with $\hbar = \mu = \omega = 1$:

```{code-cell} python
import numpy as np

N = 400                                       # grid points
x = np.linspace(-8, 8, N); dx = x[1] - x[0]
D2 = (np.eye(N, k=1) - 2 * np.eye(N) + np.eye(N, k=-1)) / dx**2   # second derivative
H = -0.5 * D2 + np.diag(0.5 * x**2)           # kinetic + potential energy

E, psi = np.linalg.eigh(H)                    # eigenvalues and eigenvectors of a Hermitian matrix
print(np.round(E[:5], 4))                     # in units of hbar * omega
```

The levels are $0.5, 1.5, 2.5, \dots$ in units of $\hbar\omega$: evenly spaced, and the lowest one is not at the bottom of the well.

```{code-cell} python
:tags: [hide-input]
# synced: ho_preview
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
N = 600                                                     # the spring on a grid, hbar = m = omega = 1 (Lecture 3.5)
x = np.linspace(-6, 6, N); dx = x[1] - x[0]
D2 = (np.eye(N, k=1) - 2 * np.eye(N) + np.eye(N, k=-1)) / dx**2
E, psi = np.linalg.eigh(-0.5 * D2 + np.diag(0.5 * x**2))
psi = psi / np.sqrt(dx)
fig, (ab, ah) = plt.subplots(1, 2, figsize=(9.2, 4.0), sharey=True, gridspec_kw={"wspace": 0.08})
L, E1 = 3.6, 0.42                                           # a box drawn about as wide as the spring's middle rungs
xb = np.linspace(0, L, 300)
ab.plot([0, 0, L, L], [7.2, 0, 0, 7.2], color="k", lw=2.4)
for n in range(1, 5):
    En = E1 * n * n
    ab.hlines(En, 0, L, color=GRAY, lw=0.9, ls="--")
    ab.plot(xb, En + 0.36 * np.sin(n * np.pi * xb / L), color=TEAL, lw=2.2)
    ab.text(L + 0.12, En, rf"$n = {n}$", va="center", fontsize=11)
for n in range(1, 4):
    ab.annotate("", xy=(L * 0.5 + 0.9, E1 * (n + 1)**2), xytext=(L * 0.5 + 0.9, E1 * n * n),
                arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.4, shrinkA=0, shrinkB=0))
ab.set_xlim(-0.3, L + 0.9); ab.set_ylim(0, 7.2); ab.set_xticks([]); ab.set_yticks([])
ab.spines["left"].set_visible(False); ab.spines["bottom"].set_visible(False)
ab.set_title("box: fixed walls, the gaps grow", loc="left", fontsize=12.5)
xx = np.linspace(-3.9, 3.9, 400)
ah.plot(xx, 0.5 * xx**2, color="k", lw=2.4)
for v in range(6):
    xt = np.sqrt(2 * E[v])                                  # turning point
    s = psi[:, v] * np.sign(psi[np.argmin(np.abs(x - 0.9 * xt)), v])   # outermost lobe up
    ah.hlines(E[v], -xt, xt, color=GRAY, lw=0.9, ls="--")
    sel = np.abs(x) < 3.95
    ah.plot(x[sel], E[v] + 0.62 * s[sel], color=TEAL, lw=2.2)
    ah.text(4.15, E[v], rf"$v = {v}$:  {E[v]:.2f}", va="center", fontsize=11)
for v in range(3):
    ah.annotate("", xy=(-2.9, E[v + 1]), xytext=(-2.9, E[v]),
                arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.4, shrinkA=0, shrinkB=0))
ah.text(-3.0, 1.95, r"$\hbar\omega$", color=CARDINAL, fontsize=13, ha="right", va="center")
ah.annotate("", xy=(0, E[0]), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6, shrinkA=0, shrinkB=0))
ah.text(1.45, 0.22, r"$\frac{1}{2}\hbar\omega$: zero-point energy", color=ORANGE, fontsize=11.5, va="center")
ah.set_xlim(-4.4, 6.3); ah.set_xticks([]); ah.spines["left"].set_visible(False); ah.spines["bottom"].set_visible(False)
ah.set_title(r"spring: the walls widen, equal gaps $\hbar\omega$", loc="left", fontsize=12.5)
fig.subplots_adjust(left=0.01, right=0.99, top=0.91, bottom=0.03)
plt.show()
```

Fig. Left: a particle in a box, whose gaps grow as $n^2$. Right: the spring from numpy, whose levels are evenly spaced by $\hbar\omega$ and start $\frac{1}{2}\hbar\omega$ above the bottom of the well.

:::{tip} **Why equal steps? A rough argument**
:class: dropdown

A box of width $L$ has levels $E \approx n^2h^2/8mL^2$. A parabolic well has no fixed width: at energy $E$ the classical oscillator spans $L = 2A$ with $\frac{1}{2}kA^2 = E$, so $L^2 = 8E/k$. Put this width into the box formula:

$$
E \approx \frac{n^2h^2k}{64\,mE} \qquad\Longrightarrow\qquad E^2 \approx \frac{n^2h^2\omega^2}{64} \qquad\Longrightarrow\qquad E \approx \frac{\pi}{4}\,n\,\hbar\omega
$$

Linear in $n$: each higher level gets a wider well, and the extra room pays for the extra node. The exact answer, derived next lecture, has steps of exactly $\hbar\omega$.
:::

- For HCl, $\hbar\omega$ corresponds to 2991 cm$^{-1}$. The lowest level sits about 1500 cm$^{-1}$ above the bottom of the well even at absolute zero: the **zero-point energy**. The infrared spectrum shows one strong line near $\hbar\omega$; anharmonicity moves it to 2886 cm$^{-1}$.
- Next: [Lecture 4.2](02-quantum-harmonic-oscillator.md) derives $E_v = (v + \frac{1}{2})\hbar\omega$ and the wavefunctions; [Lecture 4.3](03-molecular-vibrations.md) turns them into infrared spectra.

### Problems

#### Problem 1: Count the coordinates

How many vibrations do (a) ammonia NH$_3$ (pyramidal), (b) acetylene C$_2$H$_2$ (linear), (c) hydrogen cyanide HCN (linear) and (d) sulfur hexafluoride SF$_6$ (octahedral) have?

:::{admonition} **Solution**
:class: dropdown solution

(a) NH$_3$: $N = 4$, nonlinear: $3N - 6 = 6$.
(b) C$_2$H$_2$: $N = 4$, linear: $3N - 5 = 7$.
(c) HCN: $N = 3$, linear: $3N - 5 = 4$ (two stretches and a bend that can happen in two perpendicular planes).
(d) SF$_6$: $N = 7$, nonlinear: $3N - 6 = 15$.
:::

#### Problem 2: The HCl stretch

The force constant of H$^{35}$Cl is $k = 516$ N/m. Compute the reduced mass, the angular frequency $\omega = \sqrt{k/\mu}$, and the wavenumber $\tilde{\nu} = \omega/2\pi c$.

:::{admonition} **Solution**
:class: dropdown solution

$$
\mu = \frac{(1.008)(34.97)}{35.98}\ \text{u} = 0.980\ \text{u} = 1.627\times10^{-27}\ \text{kg}
$$

$$
\omega = \sqrt{\frac{516\ \text{N/m}}{1.627\times10^{-27}\ \text{kg}}} = 5.63\times10^{14}\ \text{s}^{-1}, \qquad \tilde{\nu} = \frac{5.63\times10^{14}\ \text{s}^{-1}}{2\pi\,(2.998\times10^{10}\ \text{cm/s})} = 2990\ \text{cm}^{-1}
$$

The measured line is at 2886 cm$^{-1}$; the difference is anharmonicity ([Lecture 4.3](03-molecular-vibrations.md)).
:::

#### Problem 3: Isotope shift

Predict the wavenumber of the D$^{35}$Cl stretch from that of H$^{35}$Cl (2886 cm$^{-1}$) without computing $k$. Why does the force constant not change when H is replaced by D? Compare with the measured 2091 cm$^{-1}$.

#### Problem 4: The force constant of a Morse bond

The Morse potential is $U(x) = D\left(1 - e^{-ax}\right)^2$, with $x = R - R_e$. Expand it about $x = 0$ to find the force constant, and evaluate it for HCl ($D = 4.62$ eV, $a = 1.87$ Å$^{-1}$).

:::{admonition} **Solution**
:class: dropdown solution

Expand the exponential: $e^{-ax} = 1 - ax + \frac{1}{2}a^2x^2 - \dots$, so $1 - e^{-ax} = ax - \frac{1}{2}a^2x^2 + \dots$ and

$$
U(x) = D\left(a^2x^2 - a^3x^3 + \dots\right)
$$

Matching the quadratic term to $\frac{1}{2}kx^2$ gives $k = 2Da^2$. For HCl, $D = 4.62 \times 1.602\times10^{-19}$ J $= 7.40\times10^{-19}$ J and $a = 1.87\times10^{10}$ m$^{-1}$:

$$
k = 2\,(7.40\times10^{-19}\ \text{J})\,(1.87\times10^{10}\ \text{m}^{-1})^2 = 518\ \text{N/m}
$$

close to the 516 N/m of Problem 2. The cubic term $-Da^3x^3$ is negative for a stretch: the real well is softer than the parabola on the side where the bond breaks.
:::

#### Problem 5: Energy bookkeeping

A classical oscillator has amplitude $A$. At which positions is its energy half kinetic and half potential? Sketch $V(x)$, $K(x)$ and $E$ on one plot.

#### Problem 6: Two springs at right angles

A particle moves in the plane in the potential $V = \frac{1}{2}k_xx^2 + \frac{1}{2}k_yy^2$. Using the oscillator levels $\hbar\omega\left(v + \frac{1}{2}\right)$ previewed above, write its energy levels. If $k_x = k_y$, how many states share each level?

:::{admonition} **Solution**
:class: dropdown solution

The Hamiltonian is a sum, $\hat{H} = \hat{H}_x + \hat{H}_y$, with each part acting on one coordinate. By the separable-Hamiltonian rule, $\psi = \psi_{v_x}(x)\,\psi_{v_y}(y)$ and

$$
E = \hbar\omega_x\left(v_x + \tfrac{1}{2}\right) + \hbar\omega_y\left(v_y + \tfrac{1}{2}\right), \qquad \omega_x = \sqrt{k_x/m},\ \omega_y = \sqrt{k_y/m}
$$

If $k_x = k_y$, then $E = \hbar\omega\,(v_x + v_y + 1)$. The level with $v_x + v_y = n$ can be reached by $(n, 0), (n-1, 1), \dots, (0, n)$: $n + 1$ states. As in the cubic box, the degeneracy comes from symmetry: the two directions are equivalent.
:::

#### Problem 7: Where the time goes

Show that the classical density $P(x) = 1/\pi\sqrt{A^2 - x^2}$ is normalized. What fraction of the time does the oscillator spend in the middle half, $\lvert x\rvert < A/2$? (Hint: $\int dx/\sqrt{A^2 - x^2} = \arcsin(x/A)$.)

#### Problem 8: Who moves?

In a vibrating diatomic the center of mass stays put. Show that the two atoms move in opposite directions, with displacements in the ratio $m_2 : m_1$. What fraction of the stretch does each atom carry in HCl, and in I$_2$?
