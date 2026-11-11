---
kernelspec:
  name: python3
  display_name: Python 3
---

# Atomic Orbitals

:::{note} **What you need to know**

- An **atomic orbital** is one stationary state of a one-electron atom, $\psi_{nlm} = R_{nl}(r)\,Y_l^m(\theta, \phi)$, named by $n$ and the letter of $l$: 1s, 2p, 3d. [Lecture 5.1](01-hydrogenlike-atoms.md) solved for them. This lecture draws them, and learns to read the drawings.
- "Where is the electron?" has three answers. $\lvert\psi\rvert^2\,dV$ is the probability of finding it in a small volume; the **radial distribution** $P(r) = r^2R_{nl}^2$ is the probability per unit length of finding it at distance $r$, at any angle (the $r^2$ is the area of the shell); $\lvert Y_l^m\rvert^2$ is the probability per unit solid angle of finding it in a direction. The 1s density is largest at the nucleus, but $P(r)$ peaks at $a_0$: the **most probable distance**. The average distance is $\tfrac{3}{2}a_0$, and 90% of the electron lies inside $2.66\,a_0$.
- Sizes grow as $n^2a_0/Z$. For $l = n - 1$ the most probable distance is exactly Bohr's $n^2a_0/Z$; s states keep small inner lobes close to the nucleus, which is why 2s lies below 2p once there are other electrons ([Chapter 7](../ch07/02-multi-electron-atoms.md)).
- The $Y_l^m$ with $m \neq 0$ are complex and their densities are rings around $z$. Because the $2l + 1$ states of one $n$ and $l$ have the same energy, any combination of them is again a stationary state, and the combinations $(Y_l^{-m} \mp Y_l^{m})/\sqrt{2}$ are **real orbitals** that point along axes: $p_x$, $p_y$, $p_z$ and the five $d$. They keep $E$ and $L^2$ but have no definite $L_z$.
- **Nodes:** $n - l - 1$ radial nodes (spheres) plus $l$ angular nodes (planes or cones), $n - 1$ in all. A **boundary surface** encloses 90% of the probability; it is what the textbook drawings show.

:::

### An orbital is a one-electron wavefunction

[Lecture 5.1](01-hydrogenlike-atoms.md) ended with every state of the hydrogenlike atom, $\psi_{nlm} = R_{nl}(r)\,Y_l^m(\theta, \phi)$, labelled by $n = 1, 2, \dots$, $l = 0, \dots, n - 1$ and $m = -l, \dots, l$. Chemists call each of these functions an **atomic orbital** and name it by $n$ and the letter of $l$:

| $n$ | $l$ | orbitals | how many | energy |
| :-: | :-: | :-- | :-: | :-: |
| 1 | 0 | 1s | 1 | $-E_h/2$ |
| 2 | 0, 1 | 2s, 2p | $1 + 3 = 4$ | $-E_h/8$ |
| 3 | 0, 1, 2 | 3s, 3p, 3d | $1 + 3 + 5 = 9$ | $-E_h/18$ |

The word deserves care. An orbital is a **wavefunction of one electron**, not a path: nothing orbits. For hydrogen the orbitals are exact; for every other atom the word is kept for the one-electron functions out of which the many-electron state is built, an approximation that [Chapter 7](../ch07/01-helium-atom.md) makes precise. Everything a chemist draws about atoms, from the periodic table to a $\pi$ bond, is drawn in the language of these functions, so this lecture is about drawing them well: where the electron is, what shape the orbital has, where it vanishes, and what a picture of it does and does not show.

### Where is the electron?

#### Three distributions

$\lvert\psi_{nlm}\rvert^2$ is a probability per unit volume ([Lecture 3.1](../ch03/01-schrodinger-equation.md)). In spherical coordinates ([Lecture 4.4](../ch04/04-angular-momentum.md)) the volume element is $dV = r^2\,dr\,\sin\theta\,d\theta\,d\phi$, and since $\psi$ factors into a radial and an angular part, so does the probability:

:::{important} **Where the electron is: three distributions**

$$
\lvert\psi_{nlm}\rvert^2\,dV = \underbrace{R_{nl}^2(r)\,r^2\,dr}_{\text{distance}}\;\times\;\underbrace{\lvert Y_l^m(\theta, \phi)\rvert^2\,\sin\theta\,d\theta\,d\phi}_{\text{direction}}
$$

$$
P(r) = r^2R_{nl}^2(r), \qquad \int_0^\infty P(r)\,dr = 1 \qquad\qquad \lvert Y_l^m\rvert^2, \qquad \int\lvert Y_l^m\rvert^2\,\sin\theta\,d\theta\,d\phi = 1
$$

- $P(r)\,dr$ is the probability of finding the electron between $r$ and $r + dr$, in any direction: the **radial distribution**
- $\lvert Y_l^m\rvert^2\,d\Omega$ is the probability of finding it within the solid angle $d\Omega$, at any distance: the **angular distribution**
:::

#### Why $r^2$: the area of a shell

The radial distribution is not the density. Take the ground state, $\psi_{1s} = e^{-r/a_0}/\sqrt{\pi a_0^3}$. Its density $\lvert\psi_{1s}\rvert^2$ is largest at the nucleus and falls off from there. But "at distance $r$" means anywhere on a shell of radius $r$ and thickness $dr$, whose volume is $4\pi r^2\,dr$, and that area starts at zero:

```{code-cell} python
:tags: [hide-input]
# synced: shell_volume
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Wedge, Circle
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
fig, (ax, bx, cx, dx) = plt.subplots(1, 4, figsize=(9.6, 2.9), gridspec_kw={"wspace": 0.42, "width_ratios": [1.0, 1, 1, 1]})
# (a) the 1s cloud cut through the nucleus, with a thin shell between r and r + dr
g = np.linspace(-3, 3, 301)
X, Y = np.meshgrid(g, g)
cmap = LinearSegmentedColormap.from_list("ts", ["white", TEAL])
ax.imshow(np.exp(-2 * np.hypot(X, Y)), extent=(-3, 3, -3, 3), cmap=cmap, vmin=0, vmax=1, origin="lower", zorder=0)
r0, dr0 = 1.7, 0.3
ax.add_patch(Wedge((0, 0), r0 + dr0, 0, 360, width=dr0, facecolor=ORANGE, edgecolor=ORANGE, alpha=0.75, lw=1.2, zorder=2))
ax.add_patch(Circle((0, 0), r0, fill=False, ec=ORANGE, lw=1.2, zorder=3))
ax.annotate("", xy=(r0 * np.cos(0.6), r0 * np.sin(0.6)), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="#212529", lw=1.3, shrinkA=0, shrinkB=0), zorder=4)
ax.text(0.95, 0.3, r"$r$", fontsize=12, color="#212529", zorder=5)
ax.text(r0 + dr0 + 0.12, -0.05, r"$dr$", fontsize=11, color=ORANGE, va="center", zorder=5)
ax.plot(0, 0, "o", color="#212529", ms=4, zorder=5)
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_aspect("equal"); ax.axis("off")
# (b) the density, (c) the area of the shell, (d) their product
r = np.linspace(0, 5, 400)
dens, area = np.exp(-2 * r) / np.pi, 4 * np.pi * r**2
for a_, y, col, lab in ((bx, dens, TEAL, r"$|\psi_{1s}|^2$"), (cx, area, GRAY, r"$4\pi r^2$"), (dx, dens * area, TEAL, r"$P(r)$")):
    a_.plot(r, y, color=col, lw=2.4)
    a_.set_xlim(0, 5); a_.set_ylim(0, 1.12 * y.max())
    a_.set_xlabel(r"$r$ ($a_0$)", fontsize=11); a_.set_yticks([])
    a_.set_title(lab, fontsize=13, color=col)
    a_.set_xticks([0, 1, 2, 3, 4, 5])
cx.set_ylim(0, 4 * np.pi * 4.2)
dx.axvline(1, color=CARDINAL, lw=1.2, ls=":")
dx.text(1.12, 0.52 * (dens * area).max(), r"$a_0$", fontsize=11.5, color=CARDINAL)
fig.subplots_adjust(left=0.02, right=0.99, top=0.86, bottom=0.2)
plt.show()
```

Fig. Left: the 1s cloud cut through the nucleus, with a shell between $r$ and $r + dr$. Then the density $\lvert\psi_{1s}\rvert^2$, the area of the shell $4\pi r^2$, and their product, the radial distribution $P(r)$, which peaks at $a_0$.

- The density $\lvert\psi_{1s}\rvert^2 = e^{-2r/a_0}/\pi a_0^3$ wins at small $r$, the area $4\pi r^2$ wins at large $r$, and their product $P(r) = 4r^2e^{-2r/a_0}/a_0^3$ peaks in between.
- For an s state $\lvert Y_0^0\rvert^2 = 1/4\pi$, so $P(r) = 4\pi r^2\lvert\psi\rvert^2$ exactly. For other states the angular part is averaged out: $P(r)\,dr$ counts the electron at distance $r$ whatever its direction.
- $P(r) = 0$ at the nucleus for **every** state, even 1s, because a shell of zero radius has no volume. The density at the nucleus is a different question, with a different answer (Problem 5).

:::{note} **Example: the most probable distance of the 1s electron**

Where is $P(r)$ largest for the ground state?

With $r$ in units of $a_0$, $P(r) = 4r^2e^{-2r}$, and

$$
\frac{dP}{dr} = 8r\,e^{-2r} - 8r^2e^{-2r} = 8r\,(1 - r)\,e^{-2r} = 0 \quad\Longrightarrow\quad r = a_0
$$

The most probable distance of the electron from the proton is the Bohr radius. Bohr's orbit of Lecture 1.5 is gone (the state has $l = 0$, no angular momentum, and the electron is found at every $r$), but its radius survives as the peak of $P(r)$: the answer to Problem 8 of the last lecture.
:::

:::{note} **Example: inside the Bohr radius, and the average distance**

What fraction of the time is the 1s electron found closer to the nucleus than $a_0$? And what is its average distance?

The antiderivative of $4r^2e^{-2r}$ is $-e^{-2r}(2r^2 + 2r + 1)$ (differentiate to check), so the probability inside a radius $x$ (in $a_0$) is

$$
P(r < x) = 1 - e^{-2x}\,(2x^2 + 2x + 1), \qquad P(r < a_0) = 1 - 5e^{-2} = 0.323
$$

Only a third of the time. Two thirds of the time the electron is outside the Bohr radius, because $P(r)$ has a long tail. For the average use $\int_0^\infty r^ke^{-ar}\,dr = k!/a^{k+1}$:

$$
\langle r\rangle = \int_0^\infty r\,P(r)\,dr = 4\int_0^\infty r^3e^{-2r}\,dr = 4\cdot\frac{3!}{2^4} = \frac{3}{2}\,a_0
$$

The average lies beyond the peak, as it does for every lopsided distribution. Three different lengths describe one state: the most probable distance $a_0$, the average $1.5\,a_0$, and the radius inside which 90% of the probability lies, $2.66\,a_0$ (solve $P(r < x) = 0.9$ numerically).
:::

#### Radial distributions for $n \leq 3$

```{code-cell} python
:tags: [hide-input]
# synced: radial_distributions
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
R = {(1, 0): lambda p: 2 * np.exp(-p),
     (2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
     (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
     (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
     (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
     (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.3), gridspec_kw={"wspace": 0.28, "width_ratios": [0.8, 1, 1.2]})
for ax, n, xm in zip(axes, (1, 2, 3), (6, 16, 30)):
    r = np.linspace(0, xm, 600)
    for l in range(n):
        P = r**2 * R[(n, l)](r)**2
        ax.plot(r, P, color=cols[l], lw=2.4, label=f"{n}{'spd'[l]}")
    ax.axvline(n * n, color=GRAY, lw=1.1, ls=":")
    ax.text(n * n + 0.02 * xm, 0.56, f"${n * n if n > 1 else ''}a_0$", fontsize=11, color=GRAY)
    leg = ax.legend(loc="upper right", frameon=False, fontsize=12, handlelength=1.2, borderaxespad=0.2)
    for t, h in zip(leg.get_texts(), leg.legend_handles):
        t.set_color(h.get_color()); t.set_weight("bold")
    ax.set_xlim(0, xm); ax.set_ylim(0, 0.6)
    ax.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5)
    ax.set_title(f"$n = {n}$", fontsize=13)
    ax.tick_params(labelsize=10)
axes[0].set_ylabel(r"$P(r) = r^2R_{nl}^2$  (per $a_0$)", fontsize=11.5)
for ax in axes[1:]:
    ax.set_yticklabels([])
fig.subplots_adjust(left=0.08, right=0.99, top=0.88, bottom=0.18)
plt.show()
```

Fig. The radial distributions $P(r) = r^2R_{nl}^2$ for $n = 1$, 2 and 3, each shell on its own range of $r$. The dotted line marks $n^2a_0$, Bohr's radius for orbit $n$.

- **One hump for $l = n - 1$, at Bohr's radius.** For 1s, 2p and 3d the polynomial is a single power, $P \propto r^{2n}e^{-2Zr/na_0}$, and $dP/dr = 0$ gives $r = n^2a_0/Z$: the radii of Bohr's orbits, $a_0$, $4a_0$, $9a_0$, reappear as most probable distances (Problem 1).
- **More humps for smaller $l$.** $R_{nl}$ has $n - l - 1$ nodes, so $P(r)$ has $n - l$ humps, and the outermost always carries most of the probability. The inner humps of 2s and 3s sit close to the nucleus: an s electron **penetrates** to small $r$ where a p or d electron of the same $n$ does not. In hydrogen that changes nothing, since all states of one $n$ share one energy. In every other atom the inner electrons screen the nucleus, penetration lets 2s feel more of the nuclear charge than 2p, and 2s drops below 2p: the origin of the aufbau order of [Chapter 7](../ch07/02-multi-electron-atoms.md).
- **The average distance** is the formula of the radial averages dropdown of Lecture 5.1, $\langle r\rangle_{nl} = \dfrac{n^2a_0}{Z}\left[1 + \dfrac{1}{2}\left(1 - \dfrac{l(l+1)}{n^2}\right)\right]$: $1.5\,a_0$ for 1s, $6\,a_0$ for 2s, $5\,a_0$ for 2p. For a given $n$ the s state reaches out farthest on average, even though its outer hump peaks beyond the p hump by only a little.
- **Everything scales.** $P(r)$ for a nucleus $Ze$ is the hydrogen curve squeezed by $1/Z$: every length in the table below divides by $Z$.

Three lengths for the six states, computed by numpy from the radial functions of the last lecture (all in $a_0$, $Z = 1$):

```{code-cell} python
import numpy as np

r = np.linspace(0, 60, 60001); dr = r[1] - r[0]           # r in a0
R = {"1s": 2 * np.exp(-r),
     "2s": (2 - r) * np.exp(-r / 2) / (2 * np.sqrt(2)),
     "2p": r * np.exp(-r / 2) / (2 * np.sqrt(6)),
     "3s": 2 * (27 - 18 * r + 2 * r**2) * np.exp(-r / 3) / (81 * np.sqrt(3)),
     "3p": 4 * (6 - r) * r * np.exp(-r / 3) / (81 * np.sqrt(6)),
     "3d": 4 * r**2 * np.exp(-r / 3) / (81 * np.sqrt(30))}
for name, Rn in R.items():
    P = r**2 * Rn**2                                        # radial distribution, per a0
    inside = np.cumsum(P) * dr                              # probability inside r
    print(f"{name}: r_mp = {r[P.argmax()]:5.2f}   <r> = {np.sum(r * P) * dr:5.2f}   r_90 = {r[np.searchsorted(inside, 0.9)]:5.2f}")
```

| orbital | most probable $r$ | average $\langle r\rangle$ | 90% inside |
| :-: | :-: | :-: | :-: |
| 1s | $a_0$ | $1.5\,a_0$ | $2.66\,a_0$ |
| 2s | $5.24\,a_0$ | $6\,a_0$ | $9.12\,a_0$ |
| 2p | $4\,a_0$ | $5\,a_0$ | $7.99\,a_0$ |
| 3s | $13.07\,a_0$ | $13.5\,a_0$ | $19.44\,a_0$ |
| 3p | $12\,a_0$ | $12.5\,a_0$ | $18.39\,a_0$ |
| 3d | $9\,a_0$ | $10.5\,a_0$ | $15.80\,a_0$ |

Pick a state, then drag the slider: the darker area is the probability of finding the electron inside the chosen radius. Find the radius that holds half of the 1s electron, and watch how far out 90% of a 3s electron reaches.

```{anywidget} ../widgets/radial_explorer.mjs
{"probe": true}
```

#### The boundary surface

An orbital has no edge: $P(r)$ falls off exponentially and never reaches zero. To draw a size, chemists draw the surface inside which the electron is found 90% of the time, the **boundary surface**. For an s orbital it is a sphere; its radius is the last column of the table.

```{code-cell} python
:tags: [hide-input]
# synced: probability_inside
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
R = {(1, 0): lambda p: 2 * np.exp(-p),
     (2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
     (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
     (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
     (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
     (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.6), gridspec_kw={"wspace": 0.3, "width_ratios": [1, 1.25]})
r = np.linspace(0, 6, 601)
P = 4 * r**2 * np.exp(-2 * r)
ax.plot(r, P, color=TEAL, lw=2.4)
ax.fill_between(r, P, where=r <= 1, color=TEAL, alpha=0.45, lw=0)
ax.fill_between(r, P, where=(r > 1) & (r <= 2.661), color=TEAL, alpha=0.18, lw=0)
ax.axvline(1, color=CARDINAL, lw=1.2, ls=":"); ax.axvline(2.661, color=GRAY, lw=1.2, ls=":")
ax.text(0.5, 0.1, "32%", ha="center", fontsize=12, color="white", weight="bold")
ax.text(1.8, 0.1, "58%", ha="center", fontsize=12, color=TEAL, weight="bold")
ax.text(1.06, 0.57, r"$a_0$", fontsize=11.5, color=CARDINAL)
ax.text(2.72, 0.57, r"$2.66\,a_0$", fontsize=11.5, color=GRAY)
ax.set_xlim(0, 6); ax.set_ylim(0, 0.62)
ax.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5); ax.set_ylabel(r"$P(r)$ for 1s  (per $a_0$)", fontsize=11.5)
ax.tick_params(labelsize=10)
rr = np.linspace(0, 32, 3201)
dr = rr[1] - rr[0]
for (n, l), f in R.items():
    c = np.cumsum(rr**2 * f(rr)**2) * dr
    bx.plot(rr, c, color=cols[l], lw=2.2, ls={1: "-", 2: "-", 3: "-"}[n])
    k = np.searchsorted(c, 0.9)
    bx.plot(rr[k], 0.9, "o", color=cols[l], ms=5.5, zorder=5)
    dx_, dy_, ha_ = {(1, 0): (0.0, 0.95, "center"), (2, 1): (-0.5, 0.82, "right"), (2, 0): (0.5, 0.82, "left"),
                     (3, 2): (0.0, 0.68, "center"), (3, 1): (-0.5, 0.82, "right"), (3, 0): (0.5, 0.82, "left")}[(n, l)]
    bx.text(rr[k] + dx_, dy_, f"{n}{'spd'[l]}", fontsize=11, color=cols[l], weight="bold", ha=ha_)
bx.axhline(0.9, color=GRAY, lw=1, ls=":")
bx.text(31.5, 0.905, "90%", ha="right", va="bottom", fontsize=11, color=GRAY)
bx.set_xlim(0, 32); bx.set_ylim(0, 1.04)
bx.set_xlabel(r"$r$ ($a_0$)", fontsize=11.5); bx.set_ylabel("probability inside $r$", fontsize=11.5)
bx.tick_params(labelsize=10)
fig.subplots_adjust(left=0.07, right=0.99, top=0.95, bottom=0.17)
plt.show()
```

Fig. Left: the 1s radial distribution, with 32% of the probability inside $a_0$ and 90% inside $2.66\,a_0$. Right: the probability inside $r$ for every state with $n \leq 3$; the dots mark the 90% radii.

- The 90% radius of hydrogen's 1s is $2.66\,a_0 = 141$ pm. Compare the bond length of H$_2$, 74 pm, and the van der Waals radius of a hydrogen atom in a molecule, 120 pm: the orbital pictures in a textbook are drawn to about this size.
- The 90% radius grows roughly as $n^2$ (2.7, 8 to 9, 16 to 19 $a_0$ for $n = 1$, 2, 3) and shrinks as $1/Z$: the 1s boundary of He$^+$ is at $1.33\,a_0$.
- For a p or d orbital the boundary surface is not a sphere: it is a surface of constant $\lvert\psi\rvert$ enclosing 90% of the probability, with the lobes of the angular part. That is the standard orbital drawing, and the 3D widget below draws it.

### The shape: the angular part

#### The $L_z$ eigenstates are rings

The angular factor of $\psi_{nlm}$ is the spherical harmonic $Y_l^m$ of Lecture 4.4, and its density $\lvert Y_l^m\rvert^2$ does not depend on $\phi$, because $Y_l^m \propto e^{im\phi}$ and $\lvert e^{im\phi}\rvert = 1$. So every state with a definite $L_z$ is symmetric about the $z$ axis. For $l = 1$:

$$
\lvert Y_1^{0}\rvert^2 = \frac{3}{4\pi}\cos^2\theta \quad\text{(a dumbbell along } z\text{)}, \qquad \lvert Y_1^{\pm1}\rvert^2 = \frac{3}{8\pi}\sin^2\theta \quad\text{(a ring around } z\text{)}
$$

The $m = +1$ and $m = -1$ states have the same density, a ring in the $xy$ plane; they differ only in the sense in which their phase runs around $z$. These are the states a magnetic field along $z$ singles out ([Spin](03-spin.md)). But chemists rarely draw them. A molecule has no $z$ axis built in; it has bonds along definite directions, and the orbital pictures chemists use point along axes. Those pictures are the **real orbitals**, and they come from a simple freedom.

#### A degenerate level is a space: any combination is again a stationary state

If two functions solve the Schrödinger equation with the same energy, $\hat{H}\psi_a = E\psi_a$ and $\hat{H}\psi_b = E\psi_b$, then so does every combination:

$$
\hat{H}\,(c_a\psi_a + c_b\psi_b) = c_aE\psi_a + c_bE\psi_b = E\,(c_a\psi_a + c_b\psi_b)
$$

The $2l + 1$ states of one $n$ and $l$ share the energy $E_n$ (and the eigenvalue $\hbar^2l(l+1)$ of $\hat{L}^2$, which commutes with $\hat{H}$), so any combination of them is a stationary state with the same $n$ and $l$. The degenerate level is a $(2l+1)$-dimensional space, and $Y_l^{-l}, \dots, Y_l^{l}$ are one choice of axes in it. We may turn the axes, as Lecture 3.5 turned the axes of a matrix ([Appendix A.3](../math/03-linear-algebra.md)). The combinations are no longer eigenfunctions of $\hat{L}_z$ (that operator does not care about $n$ but does care about $m$), and that is the price of pointing them along $x$ or $y$.

#### The real $p$ orbitals

Pair $m$ with $-m$. From the table of Lecture 4.4, $Y_1^{\pm1} = \mp\sqrt{3/8\pi}\,\sin\theta\,e^{\pm i\phi}$, and $e^{i\phi} + e^{-i\phi} = 2\cos\phi$, $e^{i\phi} - e^{-i\phi} = 2i\sin\phi$:

:::{important} **The real $p$ orbitals**

$$
p_z = Y_1^0 = \sqrt{\frac{3}{4\pi}}\,\cos\theta = \sqrt{\frac{3}{4\pi}}\,\frac{z}{r}
$$

$$
p_x = \frac{Y_1^{-1} - Y_1^{+1}}{\sqrt{2}} = \sqrt{\frac{3}{4\pi}}\,\sin\theta\cos\phi = \sqrt{\frac{3}{4\pi}}\,\frac{x}{r}, \qquad
p_y = \frac{i\,(Y_1^{-1} + Y_1^{+1})}{\sqrt{2}} = \sqrt{\frac{3}{4\pi}}\,\sin\theta\sin\phi = \sqrt{\frac{3}{4\pi}}\,\frac{y}{r}
$$

- Multiplied by $R_{n1}(r)$ they are the orbitals $np_x$, $np_y$, $np_z$: same $n$, same $l = 1$, same energy $E_n$, same $L^2 = 2\hbar^2$
- They are real, normalized and orthogonal, and each is the same shape pointed along a different axis: $x/r$, $y/r$, $z/r$
- $p_x$ and $p_y$ have no definite $L_z$: a measurement of $L_z$ on $p_x$ gives $+\hbar$ or $-\hbar$, each half the time
:::

:::{note} **Example: build $p_x$**

Add the two $m = \pm1$ harmonics with the signs of the table:

$$
Y_1^{-1} - Y_1^{+1} = \sqrt{\frac{3}{8\pi}}\sin\theta\,e^{-i\phi} + \sqrt{\frac{3}{8\pi}}\sin\theta\,e^{+i\phi} = \sqrt{\frac{3}{8\pi}}\sin\theta\,(2\cos\phi) = \sqrt{\frac{3}{2\pi}}\sin\theta\cos\phi
$$

Divide by $\sqrt{2}$: $p_x = \sqrt{3/4\pi}\,\sin\theta\cos\phi$, and $r\sin\theta\cos\phi = x$. Normalization costs nothing: $Y_1^{-1}$ and $Y_1^{+1}$ are orthonormal, so $\lvert c_{-1}\rvert^2 + \lvert c_{+1}\rvert^2 = \tfrac{1}{2} + \tfrac{1}{2} = 1$. The same two numbers are the probabilities of the two $L_z$ readings. (Some books leave out the Condon-Shortley signs and write $p_x$ as a sum; the densities agree.)
:::

```{code-cell} python
:tags: [hide-input]
# synced: complex_to_real
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.colors import LightSource, to_rgb
th, ph = np.meshgrid(np.linspace(0, np.pi, 73), np.linspace(0, 2 * np.pi, 145), indexing="ij")
st, ct, cp, sp = np.sin(th), np.cos(th), np.cos(ph), np.sin(ph)
x, y, z = st * cp, st * sp, ct
ls = LightSource(azdeg=300, altdeg=40)
pos, neg, dcol = np.array(to_rgb(TEAL)), np.array(to_rgb(ORANGE)), np.array(to_rgb(PURPLE))
fig = plt.figure(figsize=(9.6, 5.6))
def balloon(ax, dens, sign, lab):
    rho = dens / dens.max()
    fc = np.where(sign[..., None] >= 0, pos, neg) if sign is not None else np.broadcast_to(dcol, rho.shape + (3,))
    ax.plot_surface(rho * x, rho * y, rho * z, facecolors=fc, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=True, lightsource=ls)
    for v, name, off in (((1.15, 0, 0), "$x$", (1.12, 0, 0)), ((0, 1.15, 0), "$y$", (0, 1.12, 0)), ((0, 0, 1.05), "$z$", (0.16, 0, 0.98))):
        ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color="#868e96", lw=1.0)
        ax.text(v[0] * off[0] + off[0] * (v[0] == 0), v[1] * off[1] + off[1] * (v[1] == 0), v[2] * off[2] + off[2] * (v[2] == 0), name, fontsize=11, color="#495057", ha="center", va="center")
    ax.set_xlim(-0.9, 0.9); ax.set_ylim(-0.9, 0.9); ax.set_zlim(-0.9, 0.9)
    ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=20, azim=-58); ax.set_axis_off()
    ax.set_title(lab, fontsize=14, y=0.97)
# top row: |Y_1^m|^2 for m = +1, 0, -1 (densities, purple: no sign to show)
for k, (m, lab) in enumerate(((1, r"$|Y_1^{+1}|^2$"), (0, r"$|Y_1^{0}|^2$"), (-1, r"$|Y_1^{-1}|^2$"))):
    ax = fig.add_subplot(2, 3, k + 1, projection="3d")
    d = (3 / (8 * np.pi)) * st**2 if m else (3 / (4 * np.pi)) * ct**2
    balloon(ax, d, None, lab)
# bottom row: the real combinations, coloured by sign
for k, (f, lab) in enumerate(((x, r"$p_x$"), (y, r"$p_y$"), (z, r"$p_z$"))):
    ax = fig.add_subplot(2, 3, k + 4, projection="3d")
    balloon(ax, f**2, f, lab)
fig.subplots_adjust(left=0.0, right=1.0, top=0.96, bottom=0.0, wspace=0.0, hspace=0.0)
plt.show()
```

Fig. Top: the angular densities $\lvert Y_1^m\rvert^2$ of the three $L_z$ eigenstates with $l = 1$, drawn as surfaces whose distance from the origin in each direction is the density in that direction: two rings and a dumbbell. Bottom: the three real orbitals $p_x$, $p_y$, $p_z$, coloured by the sign of the wavefunction (teal positive, orange negative).

- The two rings become two dumbbells. Nothing was added or lost: $p_x$ and $p_y$ span the same two-dimensional space as $Y_1^{+1}$ and $Y_1^{-1}$.
- Each real $p$ orbital has one **nodal plane**, where $x$, $y$ or $z$ is zero, and changes sign across it. The sign is not visible in the density, but it matters whenever two orbitals overlap: bonding in [Chapter 8](../ch08/01-born-oppenheimer-approximation.md) is built on it.
- These surfaces show the angular part only. They say nothing about size; the radial factor $R_{n1}$ does that, and 2p and 3p have the same three shapes.

#### Running and standing waves

Why is the $m = +1$ density a ring but the $p_x$ density two lobes? Watch the real part of each wavefunction in time, $\mathrm{Re}\,[\psi\,e^{-iEt/\hbar}]$, painted on a sphere as in Lecture 4.4:

```{code-cell} python
:tags: [hide-input]
# synced: p_running
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from scipy.special import sph_harm_y
from matplotlib.colors import to_rgb
S = 221
u = np.linspace(-1, 1, S)
U, V = np.meshgrid(u, u[::-1])
inside = U**2 + V**2 < 1
W = np.sqrt(np.clip(1 - U**2 - V**2, 0, None))
el, az = np.radians(22), np.radians(-55)
cam = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])
ex = np.array([-np.sin(az), np.cos(az), 0.0])
ey = np.cross(cam, ex)
Pt = U[..., None] * ex + V[..., None] * ey + W[..., None] * cam
TH, PH = np.arccos(np.clip(Pt[..., 2], -1, 1)), np.arctan2(Pt[..., 1], Pt[..., 0])
light = np.array([-0.45, 0.55, 0.7]) / np.linalg.norm([-0.45, 0.55, 0.7])
shade = (0.5 + 0.5 * np.clip(U * light[0] + V * light[1] + W * light[2], 0, 1))[..., None]
white, pos, neg, dcol = np.ones(3), np.array(to_rgb(TEAL)), np.array(to_rgb(ORANGE)), np.array(to_rgb(PURPLE))
paint = lambda s: np.dstack([np.clip(np.where(s[..., None] > 0, white + s[..., None] * (pos - white), white - s[..., None] * (neg - white)), 0, 1) * shade, inside.astype(float)])
dens = lambda d: np.dstack([np.clip(white + d[..., None] * (dcol - white), 0, 1) * shade, inside.astype(float)])
Yp = sph_harm_y(1, 1, TH, PH)                                   # m = +1
px = ((sph_harm_y(1, -1, TH, PH) - Yp) / np.sqrt(2)).real       # p_x
top1, top2 = np.sqrt(3 / (8 * np.pi)), np.sqrt(3 / (4 * np.pi))
fig, axes = plt.subplots(2, 2, figsize=(6.0, 6.2), gridspec_kw={"wspace": 0.05, "hspace": 0.12})
ims = []
for row, (Y, top, lab) in enumerate(((Yp, top1, r"$Y_1^{+1}$"), (px, top2, r"$p_x$"))):
    ax, bx = axes[row]
    for a_ in (ax, bx):
        a_.set_xlim(-1.08, 1.08); a_.set_ylim(-1.08, 1.3); a_.set_aspect("equal"); a_.axis("off")
        a_.add_patch(plt.Circle((0, 0), 1, fill=False, ec="#868e96", lw=0.8, zorder=3))
        a_.plot([0, 0], [ey[2], ey[2] + 0.28], color="#495057", lw=1.4, zorder=3)
        a_.text(0.07, ey[2] + 0.26, "$z$", fontsize=10.5, color="#495057", va="center")
    ims.append(ax.imshow(paint(Y.real / top), extent=(-1, 1, -1, 1), interpolation="bilinear", zorder=1))
    bx.imshow(dens(np.abs(Y)**2 / top**2), extent=(-1, 1, -1, 1), interpolation="bilinear", zorder=1)
    ax.text(-1.22, 0, lab, fontsize=15, ha="right", va="center")
axes[0, 0].set_title(r"Re $\psi(t)$", fontsize=13.5); axes[0, 1].set_title(r"$|\psi|^2$", fontsize=13.5)
frames = 30
def update(k):
    ph = np.exp(-1j * 2 * np.pi * k / frames)
    ims[0].set_data(paint((Yp * ph).real / top1))
    ims[1].set_data(paint((px * ph).real / top2))
fig.subplots_adjust(left=0.14, right=0.99, top=0.93, bottom=0.02)
ani = FuncAnimation(fig, update, frames=frames, interval=100, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Left column: the real part of $\psi(t)$ for the $m = +1$ state (top) and for $p_x$ (bottom), teal positive and orange negative. Right column: their densities, which do not change in time.

- $Y_1^{+1}e^{-iEt/\hbar} \propto \sin\theta\,e^{i(\phi - Et/\hbar)}$ is a wave **running** around the $z$ axis, the ring state of Lecture 4.4 wrapped on a sphere. Its real part turns; its density is the time average of a turning lobe pair, a ring.
- $p_x\,e^{-iEt/\hbar} \propto \sin\theta\cos\phi\,e^{-iEt/\hbar}$ is a **standing** wave: the lobes stay put along $x$ and pulse between teal and orange. Its density is the two fixed lobes.
- Both are stationary states of the same energy. The atom does not prefer one set; the question asked of it does. A magnetic field along $z$ asks for $L_z$ and picks the running waves; a neighbouring atom along $x$ asks for direction and picks $p_x$.

#### The real $d$ orbitals

The same pairing gives five real $d$ orbitals from $Y_2^{-2}, \dots, Y_2^{2}$, written here in $x$, $y$, $z$ on the unit sphere ($x/r$, $y/r$, $z/r$ are $\sin\theta\cos\phi$, $\sin\theta\sin\phi$, $\cos\theta$):

| orbital | combination | angular function | lobes |
| :-- | :-- | :-- | :-- |
| $d_{z^2}$ | $Y_2^0$ | $\sqrt{\dfrac{5}{16\pi}}\,\dfrac{3z^2 - r^2}{r^2}$ | two along $z$, a ring in the $xy$ plane |
| $d_{xz}$ | $(Y_2^{-1} - Y_2^{+1})/\sqrt{2}$ | $\sqrt{\dfrac{15}{4\pi}}\,\dfrac{xz}{r^2}$ | four, between the $x$ and $z$ axes |
| $d_{yz}$ | $i\,(Y_2^{-1} + Y_2^{+1})/\sqrt{2}$ | $\sqrt{\dfrac{15}{4\pi}}\,\dfrac{yz}{r^2}$ | four, between the $y$ and $z$ axes |
| $d_{x^2-y^2}$ | $(Y_2^{+2} + Y_2^{-2})/\sqrt{2}$ | $\sqrt{\dfrac{15}{16\pi}}\,\dfrac{x^2 - y^2}{r^2}$ | four, along the $x$ and $y$ axes |
| $d_{xy}$ | $(Y_2^{+2} - Y_2^{-2})/(i\sqrt{2})$ | $\sqrt{\dfrac{15}{4\pi}}\,\dfrac{xy}{r^2}$ | four, between the $x$ and $y$ axes |

```{code-cell} python
:tags: [hide-input]
# synced: orbital_shapes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.colors import LightSource, to_rgb
th, ph = np.meshgrid(np.linspace(0, np.pi, 73), np.linspace(0, 2 * np.pi, 145), indexing="ij")
st, ct, cp, sp = np.sin(th), np.cos(th), np.cos(ph), np.sin(ph)
x, y, z = st * cp, st * sp, ct
ls = LightSource(azdeg=300, altdeg=40)
pos, neg = np.array(to_rgb(TEAL)), np.array(to_rgb(ORANGE))
shapes = [("s", np.ones_like(x), TEAL), (r"$p_x$", x, PURPLE), (r"$p_y$", y, PURPLE), (r"$p_z$", z, PURPLE), None,
          (r"$d_{xy}$", x * y, ORANGE), (r"$d_{yz}$", y * z, ORANGE), (r"$d_{xz}$", x * z, ORANGE),
          (r"$d_{x^2-y^2}$", x**2 - y**2, ORANGE), (r"$d_{z^2}$", 3 * z**2 - 1, ORANGE)]
fig = plt.figure(figsize=(9.6, 4.4))
for k, item in enumerate(shapes):
    if item is None:
        continue
    lab, f, col = item
    ax = fig.add_subplot(2, 5, k + 1, projection="3d")
    rho = f**2 / (f**2).max()
    fc = np.where(f[..., None] >= 0, pos, neg)
    ax.plot_surface(rho * x, rho * y, rho * z, facecolors=fc, rstride=1, cstride=1, linewidth=0, antialiased=False, shade=True, lightsource=ls)
    for v, name, off in (((1.15, 0, 0), "$x$", (1.12, 0, 0)), ((0, 1.15, 0), "$y$", (0, 1.12, 0)), ((0, 0, 1.05), "$z$", (0.16, 0, 0.98))):
        ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color="#868e96", lw=0.9)
        ax.text(v[0] * off[0] + off[0] * (v[0] == 0), v[1] * off[1] + off[1] * (v[1] == 0), v[2] * off[2] + off[2] * (v[2] == 0), name, fontsize=10, color="#495057", ha="center", va="center")
    ax.set_xlim(-0.9, 0.9); ax.set_ylim(-0.9, 0.9); ax.set_zlim(-0.9, 0.9)
    ax.set_box_aspect((1, 1, 1)); ax.view_init(elev=20, azim=-58); ax.set_axis_off()
    ax.set_title(lab, fontsize=13.5, color=col, y=0.97)
fig.subplots_adjust(left=0.0, right=1.0, top=0.95, bottom=0.0, wspace=0.0, hspace=0.0)
plt.show()
```

Fig. The angular densities of the nine real orbitals with $l \leq 2$, coloured by the sign of the wavefunction. Every surface is drawn to the same largest radius; sizes are not compared here.

- The names are the polynomials: $r^lY$ for the real combinations is $x$, $y$, $z$ for $l = 1$ and $xy$, $yz$, $xz$, $x^2 - y^2$, $3z^2 - r^2$ for $l = 2$ (the row $r^lY_l^m$ of the table in Lecture 4.4, recombined).
- Four of the five $d$ orbitals are the same four-leaf clover turned in space: $d_{x^2-y^2}$ points its lobes along the $x$ and $y$ axes, $d_{xy}$ between them, and $d_{xz}$, $d_{yz}$ stand the clover up in the $xz$ and $yz$ planes.
- $d_{z^2}$ is the odd one, two lobes along $z$ and a ring, because $m = 0$ needs no partner. It is as much a $d$ orbital as the others: Problem 3 shows that the clover and the ring share one $L^2$ and one energy, and a different choice of axis would turn one into the other.
- Each real orbital with $l = 2$ has **two** nodal surfaces: two planes, or for $d_{z^2}$ the two cones where $3z^2 = r^2$. Each with $l = 1$ has one plane, and s has none.

### Nodes: spheres, planes and cones

Put the two parts together. The complete orbital $\psi = R_{nl}(r)\,Y(\theta, \phi)$ vanishes wherever either factor does:

:::{important} **The nodes of an orbital**

$$
\underbrace{n - l - 1}_{\text{radial nodes: spheres } R_{nl}(r) = 0} \;+\; \underbrace{l}_{\text{angular nodes: planes or cones } Y = 0} \;=\; n - 1 \ \text{nodal surfaces}
$$

- A radial node is a sphere on which $\psi = 0$: the electron is never found at that distance, in any direction
- An angular node is a plane through the nucleus (or a cone around an axis) on which $\psi = 0$: never in that direction, at any distance
- $n - 1$ in all, as the box state $n$ has $n - 1$ nodes and the oscillator state $v$ has $v$: more nodes, more bending, more kinetic energy, higher $E_n$
:::

```{code-cell} python
:tags: [hide-input]
# synced: orbital_slices
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.colors import LinearSegmentedColormap
cmap = LinearSegmentedColormap.from_list("ot", [ORANGE, "white", TEAL])
Rf = {(1, 0): lambda p: 2 * np.exp(-p),
      (2, 0): lambda p: (2 - p) * np.exp(-p / 2) / (2 * np.sqrt(2)),
      (2, 1): lambda p: p * np.exp(-p / 2) / (2 * np.sqrt(6)),
      (3, 0): lambda p: 2 * (27 - 18 * p + 2 * p**2) * np.exp(-p / 3) / (81 * np.sqrt(3)),
      (3, 1): lambda p: 4 * (6 - p) * p * np.exp(-p / 3) / (81 * np.sqrt(6)),
      (3, 2): lambda p: 4 * p**2 * np.exp(-p / 3) / (81 * np.sqrt(30))}
# (name, n, l, angular factor of (h, v) = the two in-plane coordinates over r, plane labels, box, colour clip)
panels = [("1s", 1, 0, lambda h, v, r: np.full_like(r, 1 / np.sqrt(4 * np.pi)), ("x", "z"), 4, 1.0),
          ("2s", 2, 0, lambda h, v, r: np.full_like(r, 1 / np.sqrt(4 * np.pi)), ("x", "z"), 10, 0.35),
          (r"2p$_z$", 2, 1, lambda h, v, r: np.sqrt(3 / (4 * np.pi)) * v / r, ("x", "z"), 10, 0.6),
          ("3s", 3, 0, lambda h, v, r: np.full_like(r, 1 / np.sqrt(4 * np.pi)), ("x", "z"), 20, 0.2),
          (r"3p$_z$", 3, 1, lambda h, v, r: np.sqrt(3 / (4 * np.pi)) * v / r, ("x", "z"), 20, 0.5),
          (r"3d$_{z^2}$", 3, 2, lambda h, v, r: np.sqrt(5 / (16 * np.pi)) * (3 * v**2 - r**2) / r**2, ("x", "z"), 20, 0.6),
          (r"3d$_{xz}$", 3, 2, lambda h, v, r: np.sqrt(15 / (4 * np.pi)) * h * v / r**2, ("x", "z"), 20, 0.6),
          (r"3d$_{x^2-y^2}$", 3, 2, lambda h, v, r: np.sqrt(15 / (16 * np.pi)) * (h**2 - v**2) / r**2, ("x", "y"), 20, 0.6)]
cols = {0: TEAL, 1: PURPLE, 2: ORANGE}
fig, axes = plt.subplots(2, 4, figsize=(9.6, 5.3), gridspec_kw={"wspace": 0.3, "hspace": 0.42})
for ax, (name, n, l, ang, (hl, vl), box, clip) in zip(axes.flat, panels):
    g = np.linspace(-box, box, 361)
    Hc, Vc = np.meshgrid(g, g)
    r = np.hypot(Hc, Vc) + 1e-9
    psi = Rf[(n, l)](r) * ang(Hc, Vc, r)
    top = clip * np.abs(psi).max()
    ax.contourf(Hc, Vc, np.clip(psi, -top, top), levels=np.linspace(-top, top, 41), cmap=cmap)
    if n > 1 or l > 0:
        ax.contour(Hc, Vc, psi, levels=[0], colors=CARDINAL, linewidths=1.3, linestyles="--")
    ax.set_aspect("equal"); ax.set_xlim(-box, box); ax.set_ylim(-box, box)
    ax.set_xticks([-box, 0, box]); ax.set_yticks([-box, 0, box]); ax.tick_params(labelsize=9.5)
    ax.set_xlabel(f"${hl}$ ($a_0$)", fontsize=10.5, labelpad=1); ax.set_ylabel(f"${vl}$ ($a_0$)", fontsize=10.5, labelpad=0)
    ax.set_title(name, fontsize=13, color=cols[l], weight="bold")
fig.subplots_adjust(left=0.06, right=0.99, top=0.94, bottom=0.08)
plt.show()
```

Fig. The wavefunction $\psi$ on a plane through the nucleus, teal positive and orange negative, with every node dashed in red. The $xz$ plane for all but the last, which is the $xy$ plane. Each panel has its own range of $r$ and its own colour scale.

- **Spheres** come from $R_{nl}$: one for 2s (at $2a_0$), two for 3s (at $1.9$ and $7.1\,a_0$), one for 3p (at $6a_0$), none for 1s, 2p and 3d.
- **Planes** come from $Y$: $z = 0$ for $p_z$, both $x = 0$ and $z = 0$ for $d_{xz}$, the two diagonals $x = \pm y$ for $d_{x^2-y^2}$.
- **Cones** are the nodes of $d_{z^2}$: $3\cos^2\theta = 1$ at $\theta = 54.7^\circ$ and $125.3^\circ$, which cut the $xz$ plane in two lines through the origin. The cone angle is the magic angle of Problem 6 of Lecture 4.4.
- Counting in the figure: 3p$_z$ has one sphere and one plane, $n - 1 = 2$; 3d$_{z^2}$ has no sphere and two cones, again 2. A 4f orbital would have three nodal surfaces, all angular.

:::{note} **Example: count the nodes of 3p$_z$ and 3d$_{z^2}$**

Where does each orbital vanish, and how many surfaces is that?

- $3p_z$: $n = 3$, $l = 1$. Radial nodes $n - l - 1 = 1$: $R_{31} \propto (6 - \rho)\rho\,e^{-\rho/3}$ vanishes at $\rho = 6$, a sphere of radius $6a_0$. Angular nodes $l = 1$: $\cos\theta = 0$, the plane $z = 0$. Two surfaces, $n - 1 = 2$.
- $3d_{z^2}$: $n = 3$, $l = 2$. Radial nodes $3 - 2 - 1 = 0$: $R_{32} \propto \rho^2e^{-\rho/3}$ never vanishes for $\rho > 0$. Angular nodes $l = 2$: $3\cos^2\theta - 1 = 0$, $\cos\theta = \pm1/\sqrt{3}$, two cones at $54.7^\circ$ from the $+z$ and $-z$ axes. Two surfaces again.

The total is fixed by $n$ alone; $l$ decides how many of the $n - 1$ surfaces are spheres and how many are planes or cones.
:::

| orbital | spheres | planes or cones | total |
| :-: | :-: | :-- | :-: |
| 1s | 0 | none | 0 |
| 2s | 1 | none | 1 |
| 2p | 0 | one plane | 1 |
| 3s | 2 | none | 2 |
| 3p | 1 | one plane | 2 |
| 3d | 0 | two planes, or two cones ($d_{z^2}$) | 2 |

### The orbitals in three dimensions

Every real orbital with $n \leq 3$, as a cloud of positions drawn from $\lvert\psi\rvert^2$ (each point coloured by the sign of $\psi$), or as the boundary surface that encloses 90% of the probability. Cut an orbital open to see its spheres and planes from inside, and put every orbital in the same box to compare sizes.

```{anywidget} ../widgets/orbital_cloud.mjs
{"orbitals": ["1s", "2s", "2px", "2py", "2pz", "3s", "3px", "3py", "3pz", "3dxy", "3dyz", "3dxz", "3dx2y2", "3dz2"], "orbital": "2pz", "height": 480}
```

### What an orbital picture shows, and what it does not

| picture | shows | hides |
| :-- | :-- | :-- |
| radial distribution $P(r)$ | how far out the electron is, the radial nodes, the size | the shape |
| angular surface $\lvert Y\rvert^2$ | the shape and the angular nodes | the size, and the sign unless coloured |
| $\psi$ on a plane | sign, every node, size | the other two dimensions |
| 90% boundary surface | size and shape together | the inside, the density, the tail beyond 90% |
| point cloud | the density itself | the sign unless coloured, the nodes unless cut open |

- No picture is the orbital. The orbital is a function of three coordinates; each drawing projects one aspect of it. The textbook "shapes" are angular surfaces or boundary surfaces, and the "sizes" are 90% radii.
- The sign is physics, not decoration. $\lvert\psi\rvert^2$ hides it, but the overlap of two orbitals, $\int\psi_A\psi_B\,dV$, depends on it, and that overlap is bonding ([Chapter 8](../ch08/01-born-oppenheimer-approximation.md)). Drawings of $\psi$ colour the lobes; drawings of the density do not.
- Real or complex is a choice of axes in a degenerate level. Nothing about the atom changes; what changes is which question the picture answers.
- The next lecture adds what the Schrödinger equation left out: the electron's own angular momentum, **spin**, which doubles every orbital and, in a magnetic field, separates the $m$ states that this lecture combined ([Spin](03-spin.md)).

### Problems

#### Problem 1: Bohr's radii return

For the states with $l = n - 1$ (1s, 2p, 3d, ...) the radial function is a single power times an exponential, $R \propto r^{n-1}e^{-Zr/na_0}$. Show that the most probable distance of the electron is $r = n^2a_0/Z$, the radius of Bohr's $n$th orbit, and that the average distance is larger, $\langle r\rangle = (n^2 + n/2)\,a_0/Z$.

:::{admonition} **Solution**
:class: dropdown solution

$P(r) = r^2R^2 \propto r^{2n}e^{-2Zr/na_0}$. Set the derivative to zero:

$$
\frac{dP}{dr} \propto \left(2n\,r^{2n-1} - \frac{2Z}{na_0}\,r^{2n}\right)e^{-2Zr/na_0} = 2n\,r^{2n-1}\left(1 - \frac{Zr}{n^2a_0}\right)e^{-2Zr/na_0} = 0 \quad\Longrightarrow\quad r_{\mathrm{mp}} = \frac{n^2a_0}{Z}
$$

For the average, normalize with $\int_0^\infty r^ke^{-ar}\,dr = k!/a^{k+1}$ and $a = 2Z/na_0$:

$$
\langle r\rangle = \frac{\int_0^\infty r^{2n+1}e^{-ar}\,dr}{\int_0^\infty r^{2n}e^{-ar}\,dr} = \frac{(2n+1)!/a^{2n+2}}{(2n)!/a^{2n+1}} = \frac{2n + 1}{a} = \frac{(2n+1)\,na_0}{2Z} = \left(n^2 + \frac{n}{2}\right)\frac{a_0}{Z}
$$

which is the general formula $\langle r\rangle_{nl}$ with $l = n - 1$. For 1s: $r_{\mathrm{mp}} = a_0$, $\langle r\rangle = 1.5\,a_0$; for 3d: $9a_0$ and $10.5\,a_0$. The most probable distance is Bohr's radius exactly, for every $n$; the average is always a little larger because the distribution has a longer tail outward than inward.
:::

#### Problem 2: The two humps of 2s

With $r$ in $a_0$, the 2s radial distribution is $P(r) = \tfrac{1}{8}r^2(2 - r)^2e^{-r}$. (a) Find the radial node and the two maxima of $P(r)$ (one is the root of a quadratic). (b) By numerical integration, find the fraction of the probability inside the node. (c) Sketch $P(r)$ for 2s and 2p on one axis and explain, in one sentence, why a 2s electron would lie lower than a 2p electron in an atom whose inner electrons screen the nucleus.

#### Problem 3: Build $d_{xy}$

Using $Y_2^{\pm2} = \sqrt{15/32\pi}\,\sin^2\theta\,e^{\pm2i\phi}$, show that $(Y_2^{+2} - Y_2^{-2})/(i\sqrt{2})$ is real, equals $\sqrt{15/4\pi}\,xy/r^2$, and is normalized. What values of $L_z$ can be measured in this state, with what probabilities? What is its $L^2$?

:::{admonition} **Solution**
:class: dropdown solution

$$
Y_2^{+2} - Y_2^{-2} = \sqrt{\frac{15}{32\pi}}\sin^2\theta\,\left(e^{2i\phi} - e^{-2i\phi}\right) = \sqrt{\frac{15}{32\pi}}\sin^2\theta\,(2i\sin2\phi)
$$

Divide by $i\sqrt{2}$: the $i$ cancels and $2/\sqrt{2} = \sqrt{2}$, so the function is $\sqrt{15/16\pi}\,\sin^2\theta\sin2\phi$, real. With $\sin2\phi = 2\sin\phi\cos\phi$ and $r\sin\theta\cos\phi = x$, $r\sin\theta\sin\phi = y$:

$$
d_{xy} = \sqrt{\frac{15}{16\pi}}\cdot2\,\frac{xy}{r^2} = \sqrt{\frac{15}{4\pi}}\,\frac{xy}{r^2}
$$

Normalization: the two harmonics are orthonormal and the coefficients are $\pm1/(i\sqrt{2})$, each of modulus squared $\tfrac{1}{2}$, summing to 1. Those same numbers are the probabilities: a measurement of $L_z$ gives $+2\hbar$ or $-2\hbar$, each with probability $\tfrac{1}{2}$, never 0 or $\pm\hbar$. $L^2$ is sharp, $\hbar^2\cdot2\cdot3 = 6\hbar^2$, because both components have $l = 2$. The clover is a superposition of two rings running in opposite senses.
:::

#### Problem 4: Draw the nodes

For each of $3p_x$, $3d_{xz}$ and $3d_{z^2}$: name every nodal surface (sphere, plane or cone, with its radius, equation or angle), check that they number $n - 1$, and sketch the orbital on the $xz$ plane with the signs of the lobes marked. Then do the same for $4d_{z^2}$ and $4f_{z^3}$, whose angular part is $\propto 5\cos^3\theta - 3\cos\theta$.

#### Problem 5: Is the electron ever at the nucleus?

$P(r)$ vanishes at $r = 0$ for every state, yet $\psi_{1s}(0) \neq 0$. (a) Show that the density at the nucleus is $\lvert\psi_{ns}(0)\rvert^2 = Z^3/\pi a_0^3n^3$ for s states and zero for every other $l$. (b) Reconcile the two statements. (c) Why does the hyperfine splitting of hydrogen's ground state (the 21 cm line of radio astronomy), which comes from the electron's magnetic moment interacting with the proton's at the proton's position, exist for 1s but not for 2p?

:::{admonition} **Solution**
:class: dropdown solution

(a) From the table of Lecture 5.1, $R_{n0}(0) = 2(Z/na_0)^{3/2}$ for every $n$ (the polynomial equals 1 at $\rho = 0$ once the normalization is taken into account), and $Y_0^0 = 1/\sqrt{4\pi}$, so

$$
\lvert\psi_{ns}(0)\rvert^2 = \frac{4Z^3}{n^3a_0^3}\cdot\frac{1}{4\pi} = \frac{Z^3}{\pi a_0^3n^3}
$$

For $l > 0$, $R_{nl} \propto r^l$ near the origin, so $\psi(0) = 0$: the centrifugal barrier of Lecture 5.1 keeps those electrons away. For hydrogen's 1s the density at the proton is $1/\pi a_0^3 = 2.1\times10^{30}$ m$^{-3}$, the largest anywhere in the atom.

(b) Both are true. The density is the probability **per unit volume**, largest at the nucleus; the radial distribution is the probability **per unit length** at distance $r$, which multiplies the density by the area $4\pi r^2$ of a shell, zero at $r = 0$. The electron is found in a tiny ball around the nucleus with the small probability $\lvert\psi(0)\rvert^2\cdot\frac{4}{3}\pi\epsilon^3$, not zero.

(c) The hyperfine interaction at the nucleus is proportional to $\lvert\psi(0)\rvert^2$ (the Fermi contact term). It is nonzero only for s states, falls as $1/n^3$, and vanishes for p, d, f. The 1s level of hydrogen splits by $5.9\,\mu$eV, the 21 cm line; the 2p level has no contact splitting at all. For the same reason an s electron "sees" the nucleus in NMR couplings and in the isotope shifts of heavy atoms.
:::

#### Problem 6: How big is 2p, and how big is He$^+$?

(a) Show that the probability of finding a 2p electron inside a radius $x$ (in $a_0$) is $1 - e^{-x}\left(1 + x + \tfrac{x^2}{2} + \tfrac{x^3}{6} + \tfrac{x^4}{24}\right)$, by repeated integration by parts or by differentiating the result. (b) Solve numerically for the 90% radius and compare it with the 1s value $2.66\,a_0$. (c) Without any new integral, give the 90% radii of 1s and 2p in He$^+$ and Li$^{2+}$, and the most probable distances. (d) The ionization energy of He$^+$ is four times hydrogen's. Is its 1s electron four times, twice, or half as close to the nucleus on average?

#### Problem 7: Where does a $p_z$ electron point?

An electron in a $2p_z$ orbital is measured for direction. (a) Find the probability that it is found within $30^\circ$ of the $z$ axis (above or below the nucleus). (b) Compare with an electron in 2s, which has no preferred direction. (c) What fraction of a $2p_z$ electron lies within $10^\circ$ of the $xy$ plane?

:::{admonition} **Solution**
:class: dropdown solution

The angular distribution is $\lvert Y_1^0\rvert^2 = \tfrac{3}{4\pi}\cos^2\theta$, and the direction does not depend on $r$, so the radial factor integrates to 1 and drops out.

(a) Both polar caps, $0 \leq \theta \leq \theta_0$ and $\pi - \theta_0 \leq \theta \leq \pi$, with $\theta_0 = 30^\circ$:

$$
P = 2\int_0^{2\pi}\!d\phi\int_0^{\theta_0}\frac{3}{4\pi}\cos^2\theta\,\sin\theta\,d\theta = 2\cdot2\pi\cdot\frac{3}{4\pi}\left[-\frac{\cos^3\theta}{3}\right]_0^{\theta_0} = 1 - \cos^3\theta_0 = 1 - 0.650 = 0.350
$$

(b) For 2s, $\lvert Y_0^0\rvert^2 = 1/4\pi$ and the probability is the fraction of solid angle in the two caps: $2\cdot2\pi(1 - \cos\theta_0)/4\pi = 1 - \cos30^\circ = 0.134$. The $p_z$ electron is 2.6 times as likely to be found near its axis.

(c) The band $80^\circ \leq \theta \leq 100^\circ$: $P = \tfrac{3}{2}\int_{80^\circ}^{100^\circ}\cos^2\theta\sin\theta\,d\theta = \tfrac{1}{2}\left[\cos^3(80^\circ) - \cos^3(100^\circ)\right] = \cos^3(80^\circ) = 0.0052$, about half a percent, against $\cos80^\circ = 0.174$ for the s electron. The $xy$ plane is the nodal plane: the $p_z$ electron is almost never found near it.
:::

#### Problem 8: Pointing a $p$ orbital

(a) Show that $(p_x + p_y)/\sqrt{2}$ is again a normalized $p$ orbital of the same energy, with a single nodal plane, and find the direction in which its lobes point. (b) Write $(p_x + ip_y)/\sqrt{2}$ in terms of $Y_1^{\pm1}$ and show that it is an $L_z$ eigenstate; which one? (c) Is the energy of a hydrogen atom in the state $(2p_x + 3s)/\sqrt{2}$ sharp? Is this state stationary? (The time evolution of Lecture 3.7 answers both.)
