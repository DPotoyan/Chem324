---
kernelspec:
  name: python3
  display_name: Python 3
---

# Angular Momentum

:::{note} **What you need to know**

- Angular momentum measures rotation. The clean model system is a particle on a circle, which is what a rigid dumbbell (a diatomic with a fixed bond length) reduces to. Classically $\vec{L} = \vec{r}\times\vec{p}$, $L = I\omega$ and $E = L^2/2I$, and with no torque $\vec{L}$ is conserved: the spinning skater. Noether's theorem traces this to rotational symmetry; in quantum mechanics it means $\hat{L}$ commutes with $\hat{H}$, which is why angular momentum labels the states of rotating molecules and of electrons in atoms.
- Quantum mechanically, on a ring $\hat{L}_z = -i\hbar\,d/d\phi$. Its eigenfunctions $e^{im\phi}$ must join up after a full turn, so $m$ is a whole number and $L_z = m\hbar$, where a classical rotor could have any $L$. The energies $E_m = m^2\hbar^2/2I$ come in pairs, $\pm m$ for the two directions of travel, and start at zero: a ring has no zero-point energy.
- In three dimensions the components of $\hat{L}$ do not commute, $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ and cyclic, just as turns about different axes do not commute. Only the length $\hat{L}^2$ and one component, $\hat{L}_z$ by convention, can be sharp together.
- Their shared eigenfunctions are the **spherical harmonics** $Y_l^m(\theta, \phi)$, with $L^2 = \hbar^2 l(l+1)$ and $L_z = m\hbar$ for $l = 0, 1, 2, \dots$ and $m = -l, \dots, l$. $Y_l^m$ has $l$ nodal lines on the sphere.
- The length $\sqrt{l(l+1)}\,\hbar$ is longer than the largest projection $l\hbar$, so $\vec{L}$ never points exactly along $z$, and $L_x$, $L_y$ stay uncertain. The raising and lowering operators $\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y$ step $m$ by one and explain where $l(l+1)$ comes from.

:::

### Classical rotation

Molecules tumble, and electrons circle nuclei. [Lecture 4.1](01-molecular-degrees-of-freedom.md) found the rotational levels of HCl about 20 cm$^{-1}$ apart, in the microwave, and Chapter 5 names the atomic orbitals s, p, d after their angular momentum. Angular momentum is the quantity that organizes all of this.

The simplest rotation, and the model system of this lecture, is **a particle moving on a circle**. This section describes it classically and defines the quantities of rotation along the way; the next section treats the same particle quantum mechanically. [Appendix B](../physics/03-angular-momentum-classical.md) covers the classical side in more depth.

#### Kinematics on a circle

Press play or move the slider. Drag the picture to turn it, and look "from above" to see $\vec{\omega}$ point straight out of the screen.

```{anywidget} ../widgets/circle_vectors.mjs
{}
```

The particle goes counterclockwise around a circle of radius $r$. The angle $\phi$ grows, and the particle covers the arc $s = r\phi$ (teal). The angular velocity $\vec{\omega}$ points along the axis, and at every instant $\vec{v} = \vec{\omega}\times\vec{r}$ is perpendicular to $\vec{r}$ (the right-angle mark) and to $\vec{\omega}$, so it runs along the circle.

- The angle $\phi$ is measured in radians, so the arc length is $s = r\phi$.
- The **angular velocity** $\omega = d\phi/dt$ says how fast the angle grows. It is the same for every point of a rigid body.
- The speed along the circle is $v = ds/dt = r\,d\phi/dt = r\omega$: at the same $\omega$, points farther from the axis move faster.

As vectors, the angular velocity $\vec{\omega}$ points along the rotation axis, with length $\omega$ and direction set by the right-hand rule (fingers curl with the motion, the thumb gives $\vec{\omega}$). The velocity is then a **vector product**, $\vec{v} = \vec{\omega}\times\vec{r}$: perpendicular to both $\vec{\omega}$ and $\vec{r}$, so tangent to the circle. Its length is $\omega r\sin\alpha$, with $\alpha$ the angle between $\vec{\omega}$ and $\vec{r}$. Measured from the center of the circle, $\vec{r}$ is perpendicular to the axis, $\alpha = 90^\circ$, and $v = \omega r$ as above. Measured from any other point on the axis, $\alpha$ is smaller, but $r\sin\alpha$ is still the radius of the circle.

#### Angular momentum is a vector product

Momentum $\vec{p} = \mu\vec{v}$ measures straight-line motion. Its rotational partner is the **angular momentum**, built with the same vector product as $\vec{\omega}\times\vec{r}$, now of position and momentum:

$$
\vec{L} = \vec{r}\times\vec{p} =
\begin{vmatrix}
\hat{\imath} & \hat{\jmath} & \hat{k} \\
x & y & z \\
p_x & p_y & p_z
\end{vmatrix}
= \left(yp_z - zp_y\right)\hat{\imath} + \left(zp_x - xp_z\right)\hat{\jmath} + \left(xp_y - yp_x\right)\hat{k}
$$

```{code-cell} python
:tags: [hide-input]
# synced: angular_momentum_vector
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle, FancyArrowPatch
fig, ax = plt.subplots(figsize=(6.0, 4.4))
k = 0.32                                                    # the circle seen from above at an angle: an ellipse
t = np.linspace(0, 2 * np.pi, 300)
ax.plot(np.cos(t), k * np.sin(t), color=GRAY, lw=1.2, ls=":")
tp = np.radians(-38)
P = np.array([np.cos(tp), k * np.sin(tp)])
d = np.array([-np.sin(tp), k * np.cos(tp)]); d /= np.linalg.norm(d)
ax.add_patch(FancyArrowPatch((0, 0), P, arrowstyle="-|>", mutation_scale=16, color="k", lw=2, zorder=4))
ax.text(0.45 * P[0] + 0.02, 0.45 * P[1] - 0.1, r"$\vec{r}$", fontsize=18, va="top")
ax.add_patch(FancyArrowPatch(P, P + 0.6 * d, arrowstyle="-|>", mutation_scale=18, color=ORANGE, lw=2.6, zorder=4))
ax.text(*(P + 0.62 * d + np.array([0.04, -0.02])), r"$\vec{p} = \mu\vec{v}$", fontsize=17, color=ORANGE, va="center")
ax.add_patch(Circle(P, 0.06, fc=PURPLE, ec="k", lw=1, zorder=5))
ax.add_patch(FancyArrowPatch((0, 0), (0, 1.45), arrowstyle="-|>", mutation_scale=22, color=PURPLE, lw=3.4, zorder=4))
ax.text(0.09, 1.38, r"$\vec{L} = \vec{r}\times\vec{p}$", fontsize=18, color=PURPLE, va="center")
u = np.linspace(np.radians(200), np.radians(500), 120)     # the right-hand curl, counterclockwise seen from above
ax.plot(0.26 * np.cos(u), 0.95 + 0.08 * np.sin(u), color=GRAY, lw=1.5)
ax.add_patch(FancyArrowPatch((0.26 * np.cos(u[-6]), 0.95 + 0.08 * np.sin(u[-6])), (0.26 * np.cos(u[-1]), 0.95 + 0.08 * np.sin(u[-1])),
                             arrowstyle="-|>", mutation_scale=12, color=GRAY, lw=1.5))
ax.text(-0.33, 0.95, "right\nhand", fontsize=12, color=GRAY, ha="right", va="center")
ax.set_xlim(-1.15, 2.0); ax.set_ylim(-0.48, 1.58); ax.set_aspect("equal"); ax.axis("off")
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
plt.show()
```

Fig. A particle moving counterclockwise on a circle, seen from above at an angle. $\vec{L} = \vec{r}\times\vec{p}$ is perpendicular to both $\vec{r}$ and $\vec{p}$: it points along the rotation axis, by the right-hand rule.

- $\vec{L}$ is perpendicular to the plane of $\vec{r}$ and $\vec{p}$, and its length is $\lvert\vec{L}\rvert = rp\sin\alpha$, with $\alpha$ the angle between them.
- On a circle $\vec{r}$ and $\vec{p}$ are perpendicular, and $v = r\omega$ from the kinematics:

$$
\begin{aligned}
L &= rp\sin\alpha && \text{length of } \vec{r}\times\vec{p} \\
&= r\,\mu v && \text{circle: } \alpha = 90^\circ,\ p = \mu v \\
&= \mu r^2\omega && v = r\omega \\
&= I\omega && I = \mu r^2
\end{aligned}
$$
#### Kinetic energy in terms of $L$

The energy of the particle is all kinetic. Rewrite it step by step in the quantities of rotation:

$$
\begin{aligned}
E &= \tfrac{1}{2}\mu v^2 && \text{kinetic energy} \\
&= \tfrac{1}{2}\mu r^2\omega^2 && v = r\omega \\
&= \tfrac{1}{2}I\omega^2 && I = \mu r^2 \\
&= \frac{L^2}{2I} && \omega = L/I
\end{aligned}
$$

This has the same form as $p^2/2\mu$ for straight-line motion, with $L$ in place of the momentum and $I$ in place of the mass, and it carries straight into quantum mechanics.

:::{important} **Classical angular momentum**

$$
\vec{L} = \vec{r}\times\vec{p}, \qquad L = I\omega, \qquad E = \frac{1}{2}I\omega^2 = \frac{L^2}{2I}, \qquad I = \mu r^2
$$
:::

#### Linear and angular motion: the analogy

Every quantity of straight-line motion has a rotational partner:

| | straight line | rotation |
| :-- | :-- | :-- |
| position | $x$ | angle $\phi$ |
| velocity | $v = dx/dt$ | angular velocity $\omega = d\phi/dt$ |
| inertia | mass $\mu$ | moment of inertia $I = \mu r^2$ |
| momentum | $p = \mu v$ | angular momentum $L = I\omega$ |
| kinetic energy | $p^2/2\mu$ | $L^2/2I$ |
| changed by | force, $dp/dt = F$ | torque, $d\vec{L}/dt = \vec{r}\times\vec{F}$ |
| conserved when | no force acts | no torque acts |
| quantum operator | $\hat{p} = -i\hbar\,d/dx$ | $\hat{L}_z = -i\hbar\,d/d\phi$ (next section) |

- The mass is written $\mu$, as for the reduced mass, and $r$ is the distance from the rotation axis. The letter $m$ is saved for a quantum number.

#### A model system: the rigid dumbbell

A rigid dumbbell, such as a diatomic molecule turning with a fixed bond length, is the particle on a circle in disguise:

```{code-cell} python
:tags: [hide-input]
# synced: dumbbell_reduce
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle, FancyArrowPatch
mC, mO, R = 12.0, 16.0, 1.9
rC, rO = mO / (mC + mO) * R, mC / (mC + mO) * R            # distances from the center of mass, m_C r_C = m_O r_O
t = np.linspace(0, 2 * np.pi, 300)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.0))
for a_ in (ax, bx):
    a_.set_xlim(-2.5, 2.5); a_.set_ylim(-2.3, 2.4); a_.set_aspect("equal"); a_.axis("off")
    a_.add_patch(FancyArrowPatch((2.2 * np.cos(np.radians(25)), 2.2 * np.sin(np.radians(25))),
                                 (2.2 * np.cos(np.radians(70)), 2.2 * np.sin(np.radians(70))),
                                 connectionstyle="arc3,rad=0.2", arrowstyle="-|>", mutation_scale=16, color=PURPLE, lw=1.8))
    a_.text(1.9, 1.78, r"$\omega$", fontsize=15, color=PURPLE)
ax.plot(rC * np.cos(t), rC * np.sin(t), color="#495057", lw=1, ls=":")
ax.plot(rO * np.cos(t), rO * np.sin(t), color=CARDINAL, lw=1, ls=":")
ax.plot([-rC, rO], [0, 0], color="#adb5bd", lw=6, solid_capstyle="round", zorder=2)
ax.add_patch(Circle((-rC, 0), 0.27, fc="#495057", ec="k", lw=1, zorder=3))
ax.add_patch(Circle((rO, 0), 0.31, fc=CARDINAL, ec="k", lw=1, zorder=3))
ax.text(-rC, 0, "C", color="white", ha="center", va="center", fontsize=12, weight="bold", zorder=4)
ax.text(rO, 0, "O", color="white", ha="center", va="center", fontsize=12, weight="bold", zorder=4)
ax.plot([0], [0], "+", color="k", ms=13, mew=2.2, zorder=5)
ax.annotate("", xy=(-rC, -0.5), xytext=(0, -0.5), arrowprops=dict(arrowstyle="<->", color="#495057", lw=1.2))
ax.annotate("", xy=(rO, -0.5), xytext=(0, -0.5), arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.2))
ax.text(-rC / 2, -0.62, "$r_C$", ha="center", va="top", fontsize=13, color="#495057")
ax.text(rO / 2, -0.62, "$r_O$", ha="center", va="top", fontsize=13, color=CARDINAL)
ax.text(0, -2.1, r"$I = m_C r_C^2 + m_O r_O^2$", ha="center", fontsize=14)
bx.plot(R * np.cos(t), R * np.sin(t), color=PURPLE, lw=1.2, ls=":")
bx.plot([0, R * np.cos(np.radians(30))], [0, R * np.sin(np.radians(30))], color="k", lw=1.6)
bx.add_patch(Circle((R * np.cos(np.radians(30)), R * np.sin(np.radians(30))), 0.27, fc=PURPLE, ec="k", lw=1, zorder=3))
bx.text(R * np.cos(np.radians(30)), R * np.sin(np.radians(30)), r"$\mu$", color="white", ha="center", va="center",
        fontsize=14, zorder=4)
bx.plot([0], [0], "+", color="k", ms=13, mew=2.2)
bx.text(0.55 * np.cos(np.radians(30)) - 0.05, 0.55 * np.sin(np.radians(30)) + 0.12, "$r$", fontsize=14,
        ha="right", va="bottom")
bx.text(0, -2.1, r"$I = \mu r^2$ with $\mu = m_Cm_O/(m_C + m_O)$, $r = r_C + r_O$", ha="center", fontsize=13.5)
fig.text(0.5, 0.53, "=", ha="center", va="center", fontsize=30, color=GRAY)
fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.02, wspace=0.1)
plt.show()
```

Fig. Left: carbon monoxide as a rigid dumbbell, turning about its center of mass (+). Each atom moves on its own circle, with $m_Cr_C = m_Or_O$. Right: the same motion as one particle of reduced mass $\mu$ on a circle of radius $r = r_C + r_O$, the bond length. Both have the same moment of inertia.

With $r_C = m_OR/(m_C + m_O)$ and $r_O = m_CR/(m_C + m_O)$,

$$
I = m_Cr_C^2 + m_Or_O^2 = \frac{m_Cm_O^2 + m_Om_C^2}{(m_C + m_O)^2}\,r^2 = \frac{m_Cm_O}{m_C + m_O}\,r^2 = \mu r^2
$$

the same reduced mass that turned a vibrating diatomic into one bead on a spring in Lecture 4.1. Everything in this lecture therefore applies to a rotating diatomic molecule, with $I = \mu r^2$; in three dimensions (later) the dumbbell can also point in any direction.

#### No torque, no change: the spinning skater

Differentiate $\vec{L} = \vec{r}\times\vec{p}$ with the product rule. The first term is $\vec{v}\times\mu\vec{v} = 0$, since the vector product of parallel vectors vanishes, and Newton's law turns $d\vec{p}/dt$ into the force:

$$
\frac{d\vec{L}}{dt} = \frac{d\vec{r}}{dt}\times\vec{p} + \vec{r}\times\frac{d\vec{p}}{dt} = \vec{r}\times\vec{F} = \vec{\tau}
$$

The **torque** $\vec{\tau}$ changes angular momentum the way a force changes momentum. With no torque, $\vec{L}$ stays fixed in size and direction. A force along $\vec{r}$, toward or away from the axis, exerts no torque, so pulling a mass inward cannot change $\vec{L}$. A spinning skater who pulls the arms in therefore spins faster:

```{code-cell} python
:tags: [hide-input]
# synced: skater_spin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Circle
nf = 44
I0, mm, rout, rin = 0.12, 0.5, 1.0, 0.36                  # the body, each hand weight, arm lengths out and in
s = 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(nf) / nf)    # 0 -> 1 -> 0: arms out, in, out again
r = rout + (rin - rout) * s
I = I0 + 2 * mm * r ** 2
Lc = I[0] * 0.17                                           # fixed angular momentum; arms out turn 0.17 rad per frame
w = Lc / I                                                 # rad per frame
ang = np.cumsum(w) - w[0]
fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 4.2), gridspec_kw={"width_ratios": [1, 1.15], "wspace": 0.1})
ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(Circle((0, 0), 0.22, fc="#adb5bd", ec="k", lw=1, zorder=3))
(arms,) = ax.plot([], [], color="#495057", lw=5, solid_capstyle="round", zorder=2)
hands = [ax.add_patch(Circle((0, 0), 0.11, fc=CARDINAL, ec="k", lw=1, zorder=4)) for _ in range(2)]
trails = [ax.plot([], [], color=CARDINAL, lw=4, alpha=0.3, solid_capstyle="round")[0] for _ in range(2)]
names = ["moment of inertia $I$", r"angular velocity $\omega$", r"angular momentum $L = I\omega$"]
cols = [ORANGE, TEAL, PURPLE]
vals = [I / I[0], w / w[0], I * w / (I[0] * w[0])]
bars = bx.barh(range(3)[::-1], [v[0] for v in vals], color=cols, height=0.42)
texts = [bx.text(0, 2 - j, "", va="center", fontsize=12.5, color=cols[j]) for j in range(3)]
for j, nm in enumerate(names):
    bx.text(0.02, 2 - j + 0.36, nm, ha="left", va="bottom", fontsize=13, color=cols[j])
bx.axvline(1, color=GRAY, lw=0.8, ls=":")
bx.set_xlim(0, 5.6); bx.set_ylim(-0.45, 2.95); bx.set_yticks([]); bx.set_xticks([0, 1, 2, 3, 4, 5])
for sp in ("top", "right", "left"):
    bx.spines[sp].set_visible(False)
bx.set_xlabel("relative to the arms-out value", fontsize=11.5)
fig.subplots_adjust(left=0.01, right=0.98, top=0.98, bottom=0.14)

def update(i):
    c, sn = np.cos(ang[i]), np.sin(ang[i])
    arms.set_data([-r[i] * c, r[i] * c], [-r[i] * sn, r[i] * sn])
    for k_, sg in enumerate((1, -1)):
        hands[k_].center = (sg * r[i] * c, sg * r[i] * sn)
        sweep = np.linspace(ang[i] - 1.6 * w[i], ang[i], 30)   # the angle swept just before: a streak as long as the speed
        trails[k_].set_data(sg * r[i] * np.cos(sweep), sg * r[i] * np.sin(sweep))
    for j, (bar, v) in enumerate(zip(bars, vals)):
        bar.set_width(v[i])
        texts[j].set_position((v[i] + 0.08, 2 - j)); texts[j].set_text(f"{v[i]:.2f}")

ani = FuncAnimation(fig, update, frames=nf, interval=110, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. A spinning skater seen from above: a body with a weight in each hand. As the arms come in, the moment of inertia drops (orange). $L = I\omega$ must stay the same (purple), so the angular velocity rises by the same factor (teal).

:::{note} **Example: the spinning skater**

A skater spins at 1 turn per second with the arms out, $I = 4.0$ kg m$^2$, then pulls them in to $I' = 1.6$ kg m$^2$. How fast does the skater spin now, and what happens to the kinetic energy?

- $L$ stays fixed: $L = I\omega = (4.0\ \text{kg m}^2)(2\pi\ \text{s}^{-1}) = 25.1$ kg m$^2$ s$^{-1}$.
- Arms in: $\omega' = L/I' = 25.1/1.6 = 15.7$ s$^{-1}$, that is 2.5 turns per second, faster by the factor $I/I' = 2.5$.
- The energy $L^2/2I$ grows by the same factor, from 79 J to 197 J. The extra 118 J is the work the arms do pulling the weights inward.
:::

The same rule turns a diver's tuck into a fast somersault, a collapsing star into a rapidly spinning pulsar, and keeps a molecule tumbling at a steady rate between collisions: nothing changes $\vec{L}$ unless something twists.

#### Conservation from symmetry: Noether's theorem

:::{figure} ./images/E-noether.png
:alt: Emmy Noether, with drawings of symmetries and a conservation law
:width: 420px

Fig. Emmy Noether (1882 to 1935) proved that every continuous symmetry of the laws of physics comes with a conserved quantity.
:::

Why is angular momentum conserved at all? Noether's theorem answers with symmetry:

| if nothing changes when you | then this is conserved |
| :-- | :-- |
| shift the system in space | momentum |
| turn the system about an axis | angular momentum |
| shift the clock | energy |

A free molecule, or an electron pulled toward a nucleus, looks the same after any turn about the center: its potential energy depends only on the distance. So its angular momentum is conserved. In quantum language, [Lecture 3.7](../ch03/07-time-dependence.md) showed that an observable is a constant of motion when its operator commutes with $\hat{H}$. For these systems $\hat{L}$ commutes with $\hat{H}$, and angular momentum quantum numbers can label the stationary states.

### A particle on a ring

Now the same particle on a circle, of mass $\mu$ and radius $r$ with no potential energy, treated quantum mechanically. Real examples are the $\pi$ electrons that circulate around benzene (below), a methyl group spinning about its C$-$C bond (Problem 1), or a diatomic turning in a plane.

#### The operator

The arc length along the ring is $s = r\phi$. Momentum along the ring is $\hat{p}_s = -i\hbar\,d/ds$, and the angular momentum about the axis is $r$ times it:

$$
\hat{L}_z = r\,\hat{p}_s = -i\hbar\,r\,\frac{d}{ds} = -i\hbar\,\frac{d}{d\phi}
$$

The energy is all kinetic, $\hat{p}_s^2/2\mu$, which with $I = \mu r^2$ becomes

$$
\hat{H} = \frac{\hat{L}_z^2}{2I} = -\frac{\hbar^2}{2I}\,\frac{d^2}{d\phi^2}
$$

- $\hat{L}_z$ is the momentum operator with the angle in place of $x$, and $I$ plays the part of the mass.
- $\hat{H}$ is built from $\hat{L}_z$ alone, so the two commute and share eigenfunctions ([Operators 2](../ch03/05-hermitian-operators-and-commutators.md)).

#### The wave must join up

The eigenvalue equation $\hat{L}_z\Phi = L_z\Phi$ reads $-i\hbar\,d\Phi/d\phi = L_z\Phi$, and its solution is

$$
\Phi(\phi) = e^{iL_z\phi/\hbar}
$$

On an infinite line any value of $L_z$ would do, as any momentum does for a free particle. On a ring, $\phi$ and $\phi + 2\pi$ are the same point, so after one full turn the wavefunction must return to its starting value:

$$
\Phi(\phi + 2\pi) = \Phi(\phi) \quad\Longrightarrow\quad e^{2\pi iL_z/\hbar} = 1 \quad\Longrightarrow\quad \frac{L_z}{\hbar} = m = 0, \pm 1, \pm 2, \dots
$$

By Euler's formula ([Appendix A.2](../math/02-trigonometry-and-complex-numbers.md)), $e^{2\pi im} = \cos 2\pi m + i\sin 2\pi m$ equals 1 exactly when $m$ is a whole number. A value such as $m = 2.5$ fails: after one turn the wave returns with $e^{5\pi i} = -1$, the opposite sign, so the function would have two values at one point.

```{code-cell} python
:tags: [hide-input]
# synced: ring_waves
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
phi = np.linspace(0, 2 * np.pi, 721)
fig, axes = plt.subplots(1, 4, figsize=(9.6, 2.75))
for ax, m in zip(axes, range(4)):
    w = 0.34 * np.cos(m * phi)                              # the real part of e^{im phi}, drawn out from the ring
    r = 1 + w
    for sgn, col in ((1, TEAL), (-1, ORANGE)):              # shaded between wave and ring: positive out, negative in
        rr = np.where(sgn * w > 0, r, 1.0)
        ax.fill(np.concatenate([rr * np.cos(phi), np.cos(phi[::-1])]),
                np.concatenate([rr * np.sin(phi), np.sin(phi[::-1])]), color=col, alpha=0.3, lw=0)
        rs = np.where(sgn * w >= 0, r, np.nan)
        ax.plot(rs * np.cos(phi), rs * np.sin(phi), color=col, lw=2.6)
    ax.plot(np.cos(phi), np.sin(phi), color=GRAY, lw=1.3, ls=":")          # the ring itself: the zero line
    ax.set_xlim(-1.42, 1.42); ax.set_ylim(-1.42, 1.42); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(rf"$m = {m}$", fontsize=16)
fig.subplots_adjust(left=0.01, right=0.99, top=0.86, bottom=0.01, wspace=0.06)
plt.show()
```

Fig. The real part of $e^{im\phi}$, $\cos m\phi$, drawn around the ring (dotted): outward where it is positive (teal), inward where it is negative (orange). For $m = 0, 1, 2, 3$ a whole number of wavelengths fits, so the wave joins itself after one turn. For $m = 1$ one positive and one negative lobe make the curve look like the ring pushed sideways.

The quantization comes from no wall and no potential, only from the ring closing on itself. Normalizing on the ring, $\int_0^{2\pi}\lvert\Phi\rvert^2\,d\phi = 1$, gives the factor $1/\sqrt{2\pi}$. Each $\Phi_m$ is an eigenfunction of $\hat{H}$ as well:

$$
\hat{H}\,\Phi_m = \frac{1}{2I}\,\hat{L}_z\big(m\hbar\,\Phi_m\big) = \frac{m^2\hbar^2}{2I}\,\Phi_m
$$

:::{important} **Particle on a ring**

$$
\Phi_m(\phi) = \frac{1}{\sqrt{2\pi}}\,e^{im\phi}, \qquad L_z = m\hbar, \qquad E_m = \frac{m^2\hbar^2}{2I}, \qquad m = 0, \pm 1, \pm 2, \dots
$$

- $I = \mu r^2$ is the moment of inertia. Positive $m$ travels counterclockwise seen from $+z$, negative $m$ clockwise
:::

#### Pairs, and no zero-point energy

Cut the ring open and straighten it: a box of length $2\pi r$ ([Lecture 3.2](../ch03/02-particle-in-a-box.md)). In the box, $n$ half wavelengths fit between the walls; on the ring, a whole number $\lvert m\rvert$ of wavelengths must fit around. So the ring keeps only the box states with even $n = 2\lvert m\rvert$, and gains one that the box cannot have:

```{code-cell} python
:tags: [hide-input]
# synced: ring_ladder
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
fig, ax = plt.subplots(figsize=(9.6, 4.3))
b0, b1 = 0.6, 2.9                                           # box column
r0, r1 = 6.3, 9.0                                           # ring column: +m on the left half, -m on the right
rc = 0.5 * (r0 + r1)
for n in range(1, 5):                                       # box: E_n = n^2/4 in units of hbar^2/2I
    E, even = n * n / 4, n % 2 == 0
    ax.hlines(E, b0, b1, color=GRAY, lw=2.6 if even else 1.6, ls="-" if even else (0, (4, 3)),
              alpha=1 if even else 0.65)
    ax.text(b0 - 0.12, E, rf"$n = {n}$", ha="right", va="center", fontsize=12, color=GRAY)
    if even:                                                # the same wavelength fits around the ring
        ax.plot([b1 + 0.1, r0 - 0.1], [E, E], color=PURPLE, lw=1.1, ls=":", alpha=0.7)
for m in range(3):                                          # ring: E_m = m^2 in units of hbar^2/2I
    E = m * m
    if m == 0:
        ax.hlines(E, r0, r1, color=PURPLE, lw=2.8)
        ax.text(r1 + 0.12, E, r"$m = 0$", va="center", fontsize=12, color=PURPLE)
    else:
        ax.hlines(E, r0, rc - 0.1, color=PURPLE, lw=2.8)
        ax.hlines(E, rc + 0.1, r1, color=PURPLE, lw=2.8)
        ax.text(r1 + 0.12, E, rf"$m = \pm {m}$", va="center", fontsize=12, color=PURPLE)
        ax.text(0.5 * (r0 + rc), E + 0.11, rf"$+{m}$ ↺", ha="center", va="bottom", fontsize=11.5, color=PURPLE)
        ax.text(0.5 * (rc + r1), E + 0.11, rf"$-{m}$ ↻", ha="center", va="bottom", fontsize=11.5, color=PURPLE)
ax.text(0.5 * (b0 + b1), 4.65, r"box of length $2\pi r$", ha="center", fontsize=13, color=GRAY, weight="bold")
ax.text(0.5 * (r0 + r1), 4.65, r"ring of radius $r$", ha="center", fontsize=13, color=PURPLE, weight="bold")
ax.set_xlim(-0.6, 10.4); ax.set_ylim(-0.2, 5.0)
ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
ax.set_yticks([0, 0.25, 1, 2.25, 4]); ax.set_yticklabels(["0", "1/4", "1", "9/4", "4"]); ax.tick_params(labelsize=11)
ax.spines["left"].set_bounds(0, 4.25)
ax.set_ylabel(r"energy (units of $\hbar^2/2I$)", fontsize=12)
fig.subplots_adjust(left=0.08, right=0.99, top=0.98, bottom=0.03)
plt.show()
```

Fig. Energy levels of a ring of radius $r$ (purple) and of the box of length $2\pi r$ made by cutting it open (gray), in units of $\hbar^2/2I$. The box has $n^2/4$, the ring $m^2$. The ring keeps the even box levels, each twice: $+m$ runs counterclockwise (↺) and $-m$ clockwise (↻). Its lowest level, $m = 0$, has no energy at all.

- **Pairs.** $m$ and $-m$ have the same energy: the same speed, in opposite directions. Every level above the lowest is doubly degenerate.
- **No zero-point energy.** $\Phi_0 = 1/\sqrt{2\pi}$ is flat. It has no curvature, so no kinetic energy. The box needs $n \geq 1$ because its walls force $\psi = 0$ at both ends; the ring has no ends. There is no conflict with the uncertainty principle: in $\Phi_0$ the position on the ring is completely unknown.
- **Widening gaps.** The levels grow as $m^2$, like those of the box.

The same comparison with matrices. In [Lecture 3.5](../ch03/04-operators.md) the box became a matrix with the curvature row $(1, -2, 1)$ on every line. On a ring the last point's neighbor is the first point, so gluing the ends changes just two corner entries:

```{code-cell} python
import numpy as np

N = 400                                         # grid points around the ring
dphi = 2 * np.pi / N                            # grid spacing in angle
D2 = np.eye(N, k=1) - 2 * np.eye(N) + np.eye(N, k=-1)
box = -D2[1:, 1:] / dphi**2                     # H = -(hbar^2/2I) d^2/dphi^2 in units of hbar^2/2I; walls at 0 and 2 pi
D2[0, -1] = D2[-1, 0] = 1                       # glue the ends: the first and last points become neighbors
ring = -D2 / dphi**2
print("box: ", np.round(np.linalg.eigvalsh(box)[:6], 3) + 0)
print("ring:", np.round(np.linalg.eigvalsh(ring)[:7], 3) + 0)
```

- The box gives $n^2/4 = 0.25, 1, 2.25, 4, 6.25, 9$. The ring gives $m^2$: a level at 0, then $1$, $4$ and $9$ twice each. These are the even box levels, doubled, and a new level at zero (up to the grid error in the last digit).

#### Running and standing waves

The density of a ring state is the same everywhere, $\lvert\Phi_m\rvert^2 = 1/2\pi$. A state with sharp $L_z$ is spread evenly around the ring, while its phase winds $m$ times around it. With its time factor, $\Phi_m\,e^{-iE_mt/\hbar} \propto e^{i(m\phi - E_mt/\hbar)}$ is a wave running around the ring: counterclockwise for $m > 0$, clockwise for $m < 0$.

The states $m$ and $-m$ have the same energy, and that is the physical point: any linear superposition of them is again a state of that energy. Take the simplest one,

$$
\Psi = \frac{\Phi_m + \Phi_{-m}}{\sqrt{2}} = \frac{\cos m\phi}{\sqrt{\pi}}, \qquad \hat{H}\Psi = \frac{E_m\Phi_m + E_m\Phi_{-m}}{\sqrt{2}} = E_m\Psi
$$

(by Euler's formula, $e^{im\phi} + e^{-im\phi} = 2\cos m\phi$). Because the energies match, the superposition is still a stationary state, and its density $\cos^2 m\phi/\pi$ never changes. That is unlike a superposition of different energies, whose density moves ([Lecture 3.7](../ch03/07-time-dependence.md)). It is a standing wave with $2\lvert m\rvert$ nodes, like a state of the box. It is an eigenfunction of $\hat{H}$ but not of $\hat{L}_z$: a measurement of $L_z$ gives $+m\hbar$ or $-m\hbar$, each with probability $1/2$ ([Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md)), and $\langle L_z\rangle = 0$. The free particle showed the same pair, $e^{ikx}$ against $\cos kx$, in [Operators 2](../ch03/05-hermitian-operators-and-commutators.md).

```{code-cell} python
:tags: [hide-input]
# synced: ring_flow
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import FancyArrowPatch, Patch
from matplotlib.lines import Line2D
nf = 36
phi = np.linspace(0, 2 * np.pi, 361)
cases = [(2, r"$e^{+2i\phi}$"), (-2, r"$e^{-2i\phi}$"), (0, r"$2\cos 2\phi$")]
fig, axes = plt.subplots(1, 3, figsize=(9.6, 3.4), gridspec_kw={"wspace": 0.32})
parts = []
for ax, (m, title) in zip(axes, cases):
    ax.set_xlim(-1.62, 1.62); ax.set_ylim(-1.62, 1.62); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(title, fontsize=17)
    dens = np.ones_like(phi) if m else 2 * np.cos(2 * phi) ** 2     # |Psi|^2 in units of its average
    band = 0.1 * dens
    ax.fill(np.r_[(1 + band) * np.cos(phi), ((1 - band) * np.cos(phi))[::-1]],
            np.r_[(1 + band) * np.sin(phi), ((1 - band) * np.sin(phi))[::-1]], color=TEAL, alpha=0.25, lw=0)
    ax.plot(np.cos(phi), np.sin(phi), color=GRAY, lw=0.8, ls=":")
    (wave,) = ax.plot([], [], color=TEAL, lw=2.4)
    if m:
        a0, a1 = np.radians(55), np.radians(125)
        if m < 0:
            a0, a1 = a1, a0
        ax.add_patch(FancyArrowPatch((1.45 * np.cos(a0), 1.45 * np.sin(a0)), (1.45 * np.cos(a1), 1.45 * np.sin(a1)),
                                     connectionstyle=f"arc3,rad={0.22 if m > 0 else -0.22}", arrowstyle="-|>",
                                     mutation_scale=18, color=PURPLE, lw=2))
    parts.append((m, wave))
fig.subplots_adjust(left=0.01, right=0.99, top=0.88, bottom=0.13)
fig.legend(handles=[Line2D([0], [0], color=TEAL, lw=2.4, label=r"real part of $\Psi$"),
                    Patch(facecolor=TEAL, alpha=0.25, label=r"probability density $|\Psi|^2$")],
           loc="lower center", ncol=2, frameon=False, fontsize=13, bbox_to_anchor=(0.5, 0.0), columnspacing=3)
for k, sign in ((0, "+"), (1, "=")):                        # running + running = standing
    x = 0.5 * (axes[k].get_position().x1 + axes[k + 1].get_position().x0)
    fig.text(x, 0.45, sign, ha="center", va="center", fontsize=34, color=GRAY)

def update(i):
    wt = 2 * np.pi * i / nf                                 # E t / hbar over one period of the phase
    for m, wave in parts:
        if m:                                               # the real part of e^{i(m phi - w t)}
            re, amp = np.cos(m * phi - wt), 0.25
        else:                                               # the sum of the two running waves
            re, amp = np.cos(2 * phi - wt) + np.cos(-2 * phi - wt), 0.25
        r = 1 + amp * re
        wave.set_data(r * np.cos(phi), r * np.sin(phi))

ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Two running waves add up to a standing wave. The line is the real part of the wavefunction, drawn as bumps around the ring; the shaded band is the probability density $\lvert\Psi\rvert^2$. Left and middle: $e^{+2i\phi}$ and $e^{-2i\phi}$ run counterclockwise and clockwise, and their density is even all around and never changes. Right: their sum, $2\cos 2\phi$, stands still; its density drops to zero at four nodes.

:::{note} **Example: benzene's $\pi$ electrons on a ring**

Treat the six $\pi$ electrons of benzene as particles on a ring of radius $r = 139$ pm, the C$-$C bond length (in a regular hexagon the distance from the center to each atom equals the side). Where should benzene absorb light?

- **The energy unit.** With the electron mass $m_e$ in place of $\mu$:

$$
\frac{\hbar^2}{2m_e r^2} = \frac{(1.055\times10^{-34}\ \text{J s})^2}{2\,(9.109\times10^{-31}\ \text{kg})(1.39\times10^{-10}\ \text{m})^2} = 3.16\times10^{-19}\ \text{J} = 1.97\ \text{eV}
$$

- **Fill the levels**, two electrons per state (Pauli), as for the dyes of [Lecture 3.2](../ch03/02-particle-in-a-box.md). $m = 0$ takes two electrons and $m = \pm 1$ four more: all six. The highest filled level is $\lvert m\rvert = 1$, the lowest empty one $\lvert m\rvert = 2$.
- **The gap.** $\Delta E = (2^2 - 1^2)(1.97\ \text{eV}) = 5.9$ eV, so $\lambda = hc/\Delta E = (1240\ \text{eV nm})/(5.9\ \text{eV}) = 210$ nm, in the ultraviolet.

Benzene is colorless and absorbs between 180 and 260 nm, with a band near 200 nm. A ring of free electrons of the right size lands in the right place.
:::

#### Classical and quantum, side by side

| | classical particle on a circle | quantum particle on a ring |
| :-- | :-- | :-- |
| angular momentum | any value, $L = I\omega$ | only $L_z = m\hbar$, $m = 0, \pm 1, \pm 2, \dots$ |
| energy | any value, $L^2/2I$ | only $E_m = m^2\hbar^2/2I$ |
| where it is | a definite angle, $\phi = \omega t$ | with sharp $L_z$, anywhere: $\lvert\Phi_m\rvert^2 = 1/2\pi$ |
| lowest energy | 0, at rest at a known angle | 0, with the angle completely unknown |
| two directions | same energy at the same speed | the pair $\pm m$ |

- The quantum steps are tiny for heavy or large rotors. The methyl group of Problem 1 has 13 levels below $k_BT$ at room temperature, and a spinning wheel has $m \approx 10^{31}$: its levels are far too close to resolve, and it behaves classically.

### Angular momentum in three dimensions

#### Spherical coordinates

Rotation in space is easiest to describe with a distance and two angles: the polar angle $\theta$, measured down from the $z$ axis, and the azimuthal angle $\phi$, measured around it as on the ring.

:::{figure} ./images/spherical_coord.png
:alt: Spherical coordinates r, theta and phi, with a small patch of the sphere r dtheta tall and r sin theta dphi wide
:width: 340px

Fig. Spherical coordinates. A small patch of the sphere is $r\,d\theta$ tall and $r\sin\theta\,d\phi$ wide.
:::

$$
x = r\sin\theta\cos\phi, \qquad y = r\sin\theta\sin\phi, \qquad z = r\cos\theta, \qquad 0 \leq \theta \leq \pi, \quad 0 \leq \phi < 2\pi
$$

- The patch in the figure has area $r^2\sin\theta\,d\theta\,d\phi$. On a sphere of radius 1 it is the **surface element** $\sin\theta\,d\theta\,d\phi$, used by every integral over angles below. The factor $\sin\theta$ shrinks the patches near the poles, where the circles of latitude are short.

#### Three components, three operators

Classically each component of $\vec{L} = \vec{r}\times\vec{p}$ uses the two coordinates perpendicular to its own axis: $L_x = yp_z - zp_y$, $L_y = zp_x - xp_z$ and $L_z = xp_y - yp_x$. Replacing each momentum by $-i\hbar$ times a derivative gives the operators:

:::{important} **Angular momentum operators**

$$
\hat{L}_x = -i\hbar\left(y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y}\right), \qquad
\hat{L}_y = -i\hbar\left(z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z}\right), \qquad
\hat{L}_z = -i\hbar\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right)
$$

$$
\hat{L}^2 = \hat{L}_x^2 + \hat{L}_y^2 + \hat{L}_z^2
$$
:::

$\hat{L}_z$ is the ring operator in disguise. Turning a point about $z$ changes only $\phi$. By the chain rule, with $\partial x/\partial\phi = -r\sin\theta\sin\phi = -y$ and $\partial y/\partial\phi = r\sin\theta\cos\phi = x$,

$$
\frac{\partial}{\partial\phi} = \frac{\partial x}{\partial\phi}\frac{\partial}{\partial x} + \frac{\partial y}{\partial\phi}\frac{\partial}{\partial y} = x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x} \quad\Longrightarrow\quad \hat{L}_z = -i\hbar\,\frac{\partial}{\partial\phi}
$$

So $\hat{L}_z$ measures how a function changes when it is turned a little about the $z$ axis, and $\hat{L}_x$, $\hat{L}_y$ do the same for turns about $x$ and $y$. The ring had a single axis. Space has three, and turns about different axes get in each other's way.

#### Turns about different axes do not commute

Give a book a quarter turn about $x$, then a quarter turn about $y$. Start again and make the same two turns in the other order. The book ends up facing a different way:

```{code-cell} python
:tags: [hide-input]
# synced: rotation_order
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from matplotlib.patches import Polygon
from matplotlib.colors import to_rgb
nf = 42
el, az = np.radians(24), np.radians(35)
cam = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])     # unit vector toward the viewer
ex = np.array([-np.sin(az), np.cos(az), 0.0])                                     # screen right
ey = np.cross(cam, ex)                                                            # screen up
to2d = lambda p: np.c_[p @ ex, p @ ey]
Rx = lambda a: np.array([[1, 0, 0], [0, np.cos(a), -np.sin(a)], [0, np.sin(a), np.cos(a)]])
Ry = lambda a: np.array([[np.cos(a), 0, np.sin(a)], [0, 1, 0], [-np.sin(a), 0, np.cos(a)]])
a, b, c = 0.5, 0.72, 0.13                                   # half sizes of the book: width, height, thickness
corners = np.array([[sx * a, sy * b, sz * c] for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)])
PAGES = "#f3ead8"
faces = [((0, 0, 1), [1, 5, 7, 3], TEAL), ((0, 0, -1), [0, 2, 6, 4], "#adb5bd"), ((-1, 0, 0), [0, 1, 3, 2], PURPLE),
         ((1, 0, 0), [4, 6, 7, 5], PAGES), ((0, 1, 0), [2, 3, 7, 6], PAGES), ((0, -1, 0), [0, 4, 5, 1], PAGES)]
arrow = np.array([[-0.07, -0.45], [0.07, -0.45], [0.07, 0.16], [0.2, 0.16], [0, 0.5], [-0.2, 0.16], [-0.07, 0.16]])
arrow = np.c_[arrow, np.full(len(arrow), c + 0.004)]        # an arrow printed on the cover, pointing to the top edge
ease = lambda s: np.clip(s, 0, 1) ** 2 * (3 - 2 * np.clip(s, 0, 1))
s1 = lambda k: ease((k - 3) / 12)                           # first quarter turn over frames 4 to 15
s2 = lambda k: ease((k - 19) / 12)                          # second quarter turn over frames 20 to 31
orders = [("x", "y", lambda k: Ry(np.pi / 2 * s2(k)) @ Rx(-np.pi / 2 * s1(k))),
          ("y", "x", lambda k: Rx(-np.pi / 2 * s2(k)) @ Ry(np.pi / 2 * s1(k)))]
unit = {"x": np.array([1.0, 0, 0]), "y": np.array([0, 1.0, 0]), "z": np.array([0, 0, 1.0])}
fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.1))
parts = []
for ax, (first, second, R) in zip(axes, orders):
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.18, 1.12); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(rf"turn about ${first}$, then about ${second}$", fontsize=14)
    polys = [ax.add_patch(Polygon(np.zeros((4, 2)), closed=True, fc=col, ec="#495057", lw=1.2, zorder=2))
             for _, _, col in faces]
    mark = ax.add_patch(Polygon(np.zeros((7, 2)), closed=True, fc="white", ec="none", alpha=0.95, zorder=3))
    (axis_line,) = ax.plot([], [], color=CARDINAL, lw=1.8, ls=(0, (5, 3)), zorder=4)
    axis_lab = ax.text(0, 0, "", color=CARDINAL, fontsize=15, weight="bold", ha="center", va="center", zorder=4)
    o = np.array([-1.05, -0.95])                            # a fixed triad of axes in the corner
    triad = {}
    for name, v in unit.items():
        d = 0.28 * to2d(v[None])[0]
        ln = ax.annotate("", xy=o + d, xytext=o, arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.6,
                                                                 mutation_scale=12, shrinkA=0, shrinkB=0))
        tx = ax.text(*(o + 1.38 * d), name, color=GRAY, fontsize=12, ha="center", va="center")
        triad[name] = (ln, tx)
    step = None
    parts.append((first, second, R, polys, mark, axis_line, axis_lab, triad, step))
fig.subplots_adjust(left=0.01, right=0.99, top=0.91, bottom=0.01, wspace=0.04)

def update(k):
    for first, second, R, polys, mark, axis_line, axis_lab, triad, step in parts:
        M = R(k)
        pts = corners @ M.T
        for poly, (n, idx, col) in zip(polys, faces):
            nv = M @ np.array(n, float)
            poly.set_visible(nv @ cam > 1e-6)              # a convex box: draw only the faces turned to us
            poly.set_xy(to2d(pts[idx]))
            if poly.get_visible():
                rgb = np.array(to_rgb(col))
                poly.set_facecolor(rgb * (0.78 + 0.22 * (nv @ cam)))
        cover = M @ np.array([0, 0, 1.0])
        mark.set_visible(cover @ cam > 1e-6)
        mark.set_xy(to2d(arrow @ M.T))
        now = None if k >= 32 else (first if k < 18 else second)
        for name, (ln, tx) in triad.items():
            on = name == now
            ln.arrow_patch.set_color(CARDINAL if on else GRAY)
            tx.set_color(CARDINAL if on else GRAY); tx.set_fontweight("bold" if on else "normal")
        if now is None:
            axis_line.set_data([], []); axis_lab.set_text("")
        else:
            ends = to2d(np.array([-1.08, 1.08])[:, None] * unit[now])
            axis_line.set_data(ends[:, 0], ends[:, 1])
            axis_lab.set_position(1.12 * ends[1]); axis_lab.set_text(now)

ani = FuncAnimation(fig, update, frames=nf, interval=85, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. A book given the same two quarter turns in opposite orders. Left: about $x$ (dashed red line), then about $y$. Right: about $y$, then about $x$. The axes stay fixed in space (corner triad). The two books end facing different directions, with the arrow on the cover pointing different ways.

Each component of $\hat{L}$ measures the effect of a small turn about its axis, so if the turns do not commute, neither can the components. The [flip and swap](../ch03/05-hermitian-operators-and-commutators.md) matrices of Operators 2 showed the same thing for mirrors. Turns add one more feature: two small turns, about $x$ and then about $y$, differ from the opposite order by a small extra turn about $z$. That is why the commutator of $\hat{L}_x$ and $\hat{L}_y$ comes out proportional to $\hat{L}_z$.

#### The commutators

The commutator follows from $[\hat{x}, \hat{p}_x] = i\hbar$. Expand $[\hat{L}_x, \hat{L}_y] = [y\hat{p}_z - z\hat{p}_y,\ z\hat{p}_x - x\hat{p}_z]$ into four commutators. A coordinate and the momentum along a *different* axis commute, as do two coordinates or two momenta; only $z$ and $\hat{p}_z$ fail to commute. So the two terms without both $z$ and $\hat{p}_z$, $[y\hat{p}_z, x\hat{p}_z]$ and $[z\hat{p}_y, z\hat{p}_x]$, vanish, and in the other two the remaining factors slide out:

$$
\begin{aligned}
[\hat{L}_x, \hat{L}_y] &= [y\hat{p}_z,\ z\hat{p}_x] + [z\hat{p}_y,\ x\hat{p}_z] \\
&= y\hat{p}_x\,[\hat{p}_z, z] + x\hat{p}_y\,[z, \hat{p}_z] \\
&= -i\hbar\,y\hat{p}_x + i\hbar\,x\hat{p}_y = i\hbar\,\hat{L}_z
\end{aligned}
$$

Cycling the labels $x \to y \to z \to x$ gives the other two.

:::{important} **Angular momentum commutators**

$$
[\hat{L}_x, \hat{L}_y] = i\hbar\,\hat{L}_z, \qquad [\hat{L}_y, \hat{L}_z] = i\hbar\,\hat{L}_x, \qquad [\hat{L}_z, \hat{L}_x] = i\hbar\,\hat{L}_y
$$

$$
[\hat{L}^2, \hat{L}_x] = [\hat{L}^2, \hat{L}_y] = [\hat{L}^2, \hat{L}_z] = 0
$$
:::

The second line says the length commutes with every component:

:::{tip} **Why $\hat{L}^2$ commutes with $\hat{L}_z$**
:class: dropdown

Use the product rule $[\hat{A}, \hat{B}\hat{C}] = [\hat{A}, \hat{B}]\,\hat{C} + \hat{B}\,[\hat{A}, \hat{C}]$ (Problem 5 of [Operators 2](../ch03/05-hermitian-operators-and-commutators.md)) on each square:

$$
[\hat{L}_z, \hat{L}_x^2] = [\hat{L}_z, \hat{L}_x]\,\hat{L}_x + \hat{L}_x\,[\hat{L}_z, \hat{L}_x] = i\hbar\left(\hat{L}_y\hat{L}_x + \hat{L}_x\hat{L}_y\right)
$$

$$
[\hat{L}_z, \hat{L}_y^2] = [\hat{L}_z, \hat{L}_y]\,\hat{L}_y + \hat{L}_y\,[\hat{L}_z, \hat{L}_y] = -i\hbar\left(\hat{L}_x\hat{L}_y + \hat{L}_y\hat{L}_x\right)
$$

and $[\hat{L}_z, \hat{L}_z^2] = 0$. The three add up to zero, so $[\hat{L}_z, \hat{L}^2] = 0$. The same steps work for $\hat{L}_x$ and $\hat{L}_y$.
:::

#### A concrete check: $\hat{L}_z$ acting on $x$, $y$ and $z$

:::{note} **Example: $\hat{L}_z$ turns $x$ into $y$**

Apply $\hat{L}_z = -i\hbar\,(x\,\partial/\partial y - y\,\partial/\partial x)$ to the three simplest functions, $x$, $y$ and $z$:

$$
\hat{L}_z\,x = -i\hbar\,(0 - y) = i\hbar\,y, \qquad \hat{L}_z\,y = -i\hbar\,(x - 0) = -i\hbar\,x, \qquad \hat{L}_z\,z = 0
$$

A turn about $z$ mixes $x$ and $y$ and leaves $z$ alone. So $x$ and $y$ are not eigenfunctions of $\hat{L}_z$, but the mixtures $x \pm iy$ are:

$$
\hat{L}_z\,(x + iy) = i\hbar\,y + i\,(-i\hbar\,x) = \hbar\,(x + iy), \qquad \hat{L}_z\,(x - iy) = i\hbar\,y - i\,(-i\hbar\,x) = -\hbar\,(x - iy)
$$

In spherical coordinates, $x \pm iy = r\sin\theta\,(\cos\phi \pm i\sin\phi) = r\sin\theta\,e^{\pm i\phi}$: the ring states $e^{\pm i\phi}$ again, with $m = \pm 1$. And $z = r\cos\theta$ has $m = 0$.
:::

:::{tip} **Going further: angular momentum as $3\times3$ matrices**
:class: dropdown

Any combination $f = c_x\,x + c_y\,y + c_z\,z$ stays a combination of the three, so $\hat{L}_z$ acts on the column of coefficients $(c_x, c_y, c_z)$ as a $3\times3$ matrix, as operators did in [Lecture 3.5](../ch03/04-operators.md). Column $k$ holds what $\hat{L}_z$ makes of the $k$-th function, and $\hat{L}_x$, $\hat{L}_y$ follow the same way:

$$
L_z = \hbar\begin{pmatrix} 0 & -i & 0 \\ i & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \qquad
L_x = \hbar\begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -i \\ 0 & i & 0 \end{pmatrix}, \qquad
L_y = \hbar\begin{pmatrix} 0 & 0 & i \\ 0 & 0 & 0 \\ -i & 0 & 0 \end{pmatrix}
$$

The eigenvalues of $L_z$ are $+\hbar$, $-\hbar$ and $0$, with eigenvectors $(1, \pm i, 0)$ and $(0, 0, 1)$: the functions $x \pm iy$ and $z$ of the example. numpy checks the commutator and the eigenvalues of all three:

```python
import numpy as np
Lx = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])      # in units of hbar
Ly = np.array([[0, 0, 1j], [0, 0, 0], [-1j, 0, 0]])
Lz = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])
print(np.allclose(Lx @ Ly - Ly @ Lx, 1j * Lz))           # True: [Lx, Ly] = i Lz
print((Lx @ Lx + Ly @ Ly + Lz @ Lz).real)                # 2 times the identity: L^2 = 2 hbar^2
print(np.linalg.eigvalsh(Lx), np.linalg.eigvalsh(Lz))    # [-1, 0, 1] for both
```

- The commutator holds as a matrix identity, entry by entry.
- $\hat{L}^2$ is $2\hbar^2$ times the identity: all three functions have $L^2 = 2\hbar^2$, the value $l(l + 1) = 2$ of $l = 1$.
- Every component has the same three eigenvalues, $-\hbar$, $0$ and $+\hbar$: no axis is special. But the eigenvectors differ from axis to axis, so no function here is an eigenfunction of two components at once.
:::

#### Only one component at a time

- **Two components cannot both be sharp.** By [Operators 2](../ch03/05-hermitian-operators-and-commutators.md), sharp values of $L_x$ and $L_y$ in one state $\psi$ would need $[\hat{L}_x, \hat{L}_y]\,\psi = i\hbar\,\hat{L}_z\psi = 0$, so $L_z = 0$ as well, and cycling the argument makes all three components zero. Only a state with no rotation at all has sharp components. For any other state the uncertainty principle of [Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md) bounds the spreads, $\sigma_{L_x}\,\sigma_{L_y} \geq \frac{\hbar}{2}\,\lvert\langle L_z\rangle\rvert$.
- **The length and one component can.** $\hat{L}^2$ commutes with every component, so it shares eigenfunctions with any one of them. By convention that one is $\hat{L}_z$. The $z$ axis can be any direction you choose: along a magnetic field, along the polarization of a laser, or along a molecule's own axis.
- Contrast linear momentum: $\hat{p}_x$, $\hat{p}_y$ and $\hat{p}_z$ commute, and a plane wave has all three sharp. For rotation you can know the length of $\vec{L}$ and one projection, never its full direction.

### A particle on a sphere: the spherical harmonics

#### $\hat{L}^2$ and the Hamiltonian

Written in spherical coordinates (a long application of the chain rule), the squared length is

$$
\hat{L}^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\,\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]
$$

- It acts on the angles only; the distance $r$ never appears. It is the angular part of the Laplacian,

$$
\nabla^2 = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial}{\partial r}\right) - \frac{\hat{L}^2}{\hbar^2r^2}
$$

  so the kinetic energy of any particle splits into a radial part and a rotational part, $\hat{L}^2/2\mu r^2$. [Chapter 5](../ch05/01-hydrogenlike-atoms.md) uses this split for the hydrogen atom.
- A particle of mass $\mu$ held on a sphere of radius $r$, with no potential, keeps only the rotational part:

$$
\hat{H} = \frac{\hat{L}^2}{2I}, \qquad I = \mu r^2
$$

  This is the **rigid rotor**, a diatomic molecule turning with a fixed bond length ([Lecture 4.5](05-rigid-rotor.md)). Its eigenfunctions are those of $\hat{L}^2$.

#### The solution

Separate the angles, $Y(\theta, \phi) = \Theta(\theta)\,\Phi(\phi)$. The angle $\phi$ enters $\hat{L}^2$ only through $\partial^2/\partial\phi^2 = -\hat{L}_z^2/\hbar^2$, so the $\phi$ part is the ring all over again: $\Phi_m = e^{im\phi}/\sqrt{2\pi}$ with whole $m$. What remains is an equation for $\Theta(\theta)$. Its solutions stay finite at both poles only when the eigenvalue of $\hat{L}^2$ is $\hbar^2l(l + 1)$, with $l$ a whole number no smaller than $\lvert m\rvert$. Otherwise they blow up at $\theta = 0$ or $\pi$, much as the oscillator's series blew up at large $x$ unless it stopped ([Lecture 4.2](02-quantum-harmonic-oscillator.md)). The finite solutions are polynomials in $\cos\theta$ and $\sin\theta$ (associated Legendre functions).

:::{important} **Spherical harmonics: eigenfunctions of $\hat{L}^2$ and $\hat{L}_z$**

$$
\hat{L}^2\,Y_l^m = \hbar^2\,l(l+1)\,Y_l^m, \qquad \hat{L}_z\,Y_l^m = m\hbar\,Y_l^m
$$

$$
l = 0, 1, 2, \dots \qquad m = -l, -l+1, \dots, l-1, l \quad (2l + 1\ \text{values})
$$

$$
\langle l'm'|lm\rangle = \int_0^{2\pi}\!\!\int_0^{\pi} Y_{l'}^{m'*}\,Y_l^m\,\sin\theta\,d\theta\,d\phi = \delta_{ll'}\,\delta_{mm'}
$$

- $l$ sets the length of $\vec{L}$, $\lvert\vec{L}\rvert = \sqrt{l(l+1)}\,\hbar$; $m$ sets its projection on $z$
- The functions are orthonormal on the sphere, with the surface element $\sin\theta\,d\theta\,d\phi$
:::

- Chemists know $l$ by letters: s, p, d, f for $l = 0, 1, 2, 3$. $m$ is often written $m_l$ and called the **magnetic quantum number**, because a magnetic field along $z$ separates states of different $m$ ([Spin](../ch05/03-spin.md)). For a rotating molecule, spectroscopists write $J$ and $M_J$.

| $l$ | $m$ | $Y_l^m(\theta, \phi)$ | $r^l\,Y_l^m$ in $x, y, z$ | |
| :-: | :-: | :-- | :-- | :-: |
| 0 | 0 | $\sqrt{\dfrac{1}{4\pi}}$ | $\sqrt{\dfrac{1}{4\pi}}$ | s |
| 1 | 0 | $\sqrt{\dfrac{3}{4\pi}}\,\cos\theta$ | $\sqrt{\dfrac{3}{4\pi}}\,z$ | p |
| 1 | $\pm 1$ | $\mp\sqrt{\dfrac{3}{8\pi}}\,\sin\theta\,e^{\pm i\phi}$ | $\mp\sqrt{\dfrac{3}{8\pi}}\,(x \pm iy)$ | p |
| 2 | 0 | $\sqrt{\dfrac{5}{16\pi}}\,(3\cos^2\theta - 1)$ | $\sqrt{\dfrac{5}{16\pi}}\,(3z^2 - r^2)$ | d |
| 2 | $\pm 1$ | $\mp\sqrt{\dfrac{15}{8\pi}}\,\sin\theta\cos\theta\,e^{\pm i\phi}$ | $\mp\sqrt{\dfrac{15}{8\pi}}\,z\,(x \pm iy)$ | d |
| 2 | $\pm 2$ | $\sqrt{\dfrac{15}{32\pi}}\,\sin^2\theta\,e^{\pm 2i\phi}$ | $\sqrt{\dfrac{15}{32\pi}}\,(x \pm iy)^2$ | d |

- Every $Y_l^m$ is $e^{im\phi}$ times a function of $\theta$: a ring state wrapped around the $z$ axis.
- In $x, y, z$ the $l = 1$ functions are $z$ and $x \pm iy$, the $\hat{L}_z$ eigenfunctions of the example above. The $l = 2$ functions are products of two of them: $r^l\,Y_l^m$ is a polynomial of degree $l$ in $x$, $y$ and $z$.
- The $\mp$ signs follow the usual convention (Condon and Shortley's). Some books leave them out; they change no probability.

:::{note} **Example: check $Y_1^0$**

Show that $Y_1^0 \propto \cos\theta$ has $l = 1$ and $m = 0$.

It does not depend on $\phi$, so every $\phi$ derivative gives zero: $\hat{L}_z\cos\theta = 0$, and $m = 0$. For $\hat{L}^2$, work from the inside out:

$$
\frac{\partial}{\partial\theta}\cos\theta = -\sin\theta, \qquad \sin\theta\cdot(-\sin\theta) = -\sin^2\theta, \qquad \frac{1}{\sin\theta}\,\frac{\partial}{\partial\theta}\left(-\sin^2\theta\right) = -2\cos\theta
$$

$$
\hat{L}^2\cos\theta = -\hbar^2\,(-2\cos\theta) = 2\hbar^2\cos\theta = \hbar^2\,l(l+1)\cos\theta \quad\text{with}\quad l = 1
$$
:::

#### Normalized and orthogonal on the sphere

:::{note} **Example: normalize $Y_0^0$, and check that it is orthogonal to $Y_1^0$**

$Y_0^0$ is a constant $c$. Integrate $c^2$ over the sphere:

$$
\int_0^{2\pi}\!\!\int_0^{\pi} c^2\sin\theta\,d\theta\,d\phi = c^2\,\Big[-\cos\theta\Big]_0^{\pi}\,\Big[\phi\Big]_0^{2\pi} = c^2\cdot 2\cdot 2\pi = 4\pi c^2 = 1 \quad\Longrightarrow\quad c = \frac{1}{\sqrt{4\pi}}
$$

($4\pi$ is the area of a sphere of radius 1.) Against $Y_1^0 \propto \cos\theta$, the $\theta$ integral vanishes:

$$
\int_0^{\pi}\cos\theta\,\sin\theta\,d\theta = \left[\frac{\sin^2\theta}{2}\right]_0^{\pi} = 0
$$
:::

- Two states with different $m$ are orthogonal through the $\phi$ integral alone: $\int_0^{2\pi} e^{i(m - m')\phi}\,d\phi = 0$ for $m' \neq m$. States with the same $m$ and different $l$ cancel in the $\theta$ integral. Both are guaranteed because $\hat{L}_z$ and $\hat{L}^2$ are Hermitian ([Operators 2](../ch03/05-hermitian-operators-and-commutators.md)).

numpy integrates every pair with $l \leq 2$ on a grid of angles:

```{code-cell} python
import numpy as np
from scipy.special import sph_harm_y            # sph_harm_y(l, m, theta, phi)

n = 200
theta = (np.arange(n) + 0.5) * np.pi / n        # polar angle: midpoints of n strips
phi = np.arange(2 * n) * np.pi / n              # azimuth: once around
TH, PH = np.meshgrid(theta, phi, indexing="ij")
dA = np.sin(TH) * (np.pi / n) ** 2              # surface element sin(theta) dtheta dphi
lm = [(l, m) for l in range(3) for m in range(-l, l + 1)]    # the 9 states with l <= 2
Y = np.array([sph_harm_y(l, m, TH, PH).ravel() for l, m in lm])
S = Y.conj() @ (Y * dA.ravel()).T               # S[a, b] = <a|b>
print(np.round(S.real, 3) + 0)
```

The $9\times9$ overlap matrix is the identity: each $Y_l^m$ has length 1 and is perpendicular to the other eight.

#### Pictures on the globe: $l$ nodal lines

A spherical harmonic is a wave on the surface of a sphere. Color each point by the sign of its real part:

```{code-cell} python
:tags: [hide-input]
# synced: harmonic_globes
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
from scipy.special import sph_harm_y
from matplotlib.colors import to_rgb
S = 261
u = np.linspace(-1, 1, S)
U, V = np.meshgrid(u, u[::-1])                              # screen coordinates, V upward
inside = U ** 2 + V ** 2 < 1
W = np.sqrt(np.clip(1 - U ** 2 - V ** 2, 0, None))          # toward the viewer
el, az = np.radians(22), np.radians(-55)                    # the north pole tipped 22 degrees toward us
cam = np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])
ex = np.array([-np.sin(az), np.cos(az), 0.0])
ey = np.cross(cam, ex)
P = U[..., None] * ex + V[..., None] * ey + W[..., None] * cam      # the point of the sphere behind each pixel
TH, PH = np.arccos(np.clip(P[..., 2], -1, 1)), np.arctan2(P[..., 1], P[..., 0])
light = np.array([-0.45, 0.55, 0.7]) / np.linalg.norm([-0.45, 0.55, 0.7])
shade = 0.5 + 0.5 * np.clip(U * light[0] + V * light[1] + W * light[2], 0, 1)
white, pos, neg = np.ones(3), np.array(to_rgb(TEAL)), np.array(to_rgb(ORANGE))
th1 = np.linspace(0, np.pi, 721)
fig, axes = plt.subplots(4, 4, figsize=(9.6, 7.5))
for l in range(4):
    for m in range(4):
        ax = axes[l, m]
        ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.15, 1.35); ax.set_aspect("equal"); ax.axis("off")
        if m > l:
            continue
        top = np.abs(sph_harm_y(l, m, th1, 0 * th1).real).max()          # the largest |Re Y| on the sphere
        s = sph_harm_y(l, m, TH, PH).real / top                          # -1 .. 1
        rgb = np.where(s[..., None] > 0, white + s[..., None] * (pos - white), white - s[..., None] * (neg - white))
        rgb = np.clip(rgb, 0, 1)
        img = np.dstack([rgb * shade[..., None], inside.astype(float)])
        ax.imshow(img, extent=(-1, 1, -1, 1), interpolation="bilinear", zorder=1)
        if l > 0:
            ax.contour(U, V, np.ma.masked_where(U ** 2 + V ** 2 > 0.985, s), levels=[0], colors="#212529",
                       linewidths=1.4, zorder=2)
        ax.add_patch(plt.Circle((0, 0), 1, fill=False, ec="#868e96", lw=0.8, zorder=3))
        ax.plot([0, 0], [ey[2], ey[2] + 0.3], color="#495057", lw=1.4, zorder=3)     # the z axis leaving the north pole
        ax.text(0.08, ey[2] + 0.28, "$z$", fontsize=10, color="#495057", va="center")
        ax.text(0, -1.12, f"{l - m} + {m} = {l}", ha="center", va="top", fontsize=10.5, color=GRAY)
for l in range(4):
    axes[l, 0].text(-1.45, 0.1, rf"$l = {l}$", ha="right", va="center", fontsize=14)
for m in range(4):
    axes[0, m].set_title(rf"$m = {m}$", fontsize=14)
fig.subplots_adjust(left=0.07, right=0.995, top=0.955, bottom=0.035, wspace=0.0, hspace=0.12)
plt.show()
```

Fig. The real part of $Y_l^m$ on a sphere, for $l = 0$ to 3 and $m = 0$ to $l$, with the north pole tipped toward the viewer. Teal is positive, orange negative, and the dark lines are nodes. Under each globe: the nodal circles around the $z$ axis plus the circles through the poles, which always add up to $l$.

- **$l - \lvert m\rvert$ circles around the axis.** These are the zeros of $\Theta(\theta)$: circles of latitude where the wave changes sign on the way from pole to pole.
- **$\lvert m\rvert$ circles through the poles.** The real part carries $\cos m\phi$, which changes sign $2\lvert m\rvert$ times around the axis: $\lvert m\rvert$ great circles through both poles.
- **$l$ in all**, like the $n - 1$ nodes of the box and the $v$ nodes of the oscillator. More nodes mean more bending and more kinetic energy: $L^2$ grows with $l$.
- **The density does not depend on $\phi$.** $\lvert Y_l^m\rvert^2 = \lvert\Theta\rvert^2/2\pi$, so a state with sharp $L_z$ is symmetric about the $z$ axis, like the even density on the ring. The circles through the poles belong to the real part, a standing wave made of $+m$ and $-m$. Such real combinations are the familiar orbitals $p_x$, $p_y$, $d_{xy}$, ... of [Atomic Orbitals](../ch05/02-atomic-orbitals.md).

Try it: pick $l$ and $m$, drag the globe to turn it, and switch to the density to watch the circles through the poles disappear. The panel on the right is the vector model of the next section.

```{anywidget} ../widgets/spherical_harmonics.mjs
{}
```

### The vector model

The two sharp numbers fix the length of $\vec{L}$ and its height along $z$. Draw $\vec{L}$ as an arrow with exactly those two properties:

```{code-cell} python
:tags: [hide-input]
# synced: vector_cones
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.7), gridspec_kw={"width_ratios": [1, 1.32], "wspace": 0.02})
t = np.linspace(0, 2 * np.pi, 300)
LIGHT = "#cdb9e3"
lz = {-2: r"-2\hbar", -1: r"-\hbar", 0: "0", 1: r"+\hbar", 2: r"+2\hbar"}
for ax, l in zip(axes, (1, 2)):
    R = np.sqrt(l * (l + 1))                                # |L| in units of hbar
    ax.plot(R * np.cos(t), R * np.sin(t), color=GRAY, lw=1, ls=":")
    ax.annotate("", xy=(0, R + 0.62), xytext=(0, -R - 0.35),
                arrowprops=dict(arrowstyle="-|>", color="k", lw=1.4, mutation_scale=14, shrinkA=0, shrinkB=0))
    ax.text(0.14, R + 0.55, "$z$", fontsize=14, va="center")
    for m in range(-l, l + 1):
        rm = np.sqrt(R * R - m * m)                         # radius of the cone's rim: the part of L off the z axis
        ax.plot(rm * np.cos(t), m + 0.2 * rm * np.sin(t), color=LIGHT, lw=1.6)
        ax.plot([-rm, 0, rm], [m, 0, m], color=LIGHT, lw=1.2)
        tip = (rm * np.cos(np.radians(-42)), m + 0.2 * rm * np.sin(np.radians(-42)))
        ax.annotate("", xy=tip, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=2.2,
                                                              mutation_scale=15, shrinkA=0, shrinkB=0))
        ax.plot([0], [m], "o", color=PURPLE, ms=5, zorder=5)
        ax.plot([0.05, R + 0.25], [m, m], color=GRAY, lw=0.8, ls=(0, (2, 3)))
        ax.text(R + 0.32, m, rf"$m = {m:+d}$: $L_z = {lz[m]}$" if m else r"$m = 0$: $L_z = 0$", va="center",
                fontsize=12, color=PURPLE)
    root = "2" if l == 1 else "6"
    ax.set_title(rf"$l = {l}$", fontsize=15)
    ax.set_xlim(-R - 0.25, R + 2.75 if l == 2 else R + 2.55); ax.set_ylim(-R - 0.5, R + 0.75)
    ax.set_aspect("equal"); ax.axis("off")
fig.subplots_adjust(left=0.0, right=0.99, top=0.92, bottom=0.01)
plt.show()
```

Fig. The vector model for $l = 1$ and $l = 2$. Every arrow has the same length $\sqrt{l(l+1)}\,\hbar$ (dotted circle), and its height $m\hbar$ takes $2l + 1$ values. Where the arrow points around the $z$ axis is unknown, so each state is drawn as a cone of possible directions.

- **$\vec{L}$ never points along $z$.** The largest projection, $l\hbar$, is shorter than the length $\sqrt{l(l+1)}\,\hbar$. If $\vec{L}$ lay along $z$, then $L_x = L_y = 0$ would both be sharp, which the commutator forbids.
- **The rest is in $L_x$ and $L_y$.** Since $\hat{L}_x^2 + \hat{L}_y^2 = \hat{L}^2 - \hat{L}_z^2$, every $Y_l^m$ has

$$
\langle L_x^2\rangle + \langle L_y^2\rangle = \hbar^2\left[l(l+1) - m^2\right] > 0 \qquad (l > 0)
$$

  By the symmetry about $z$ each takes half, and $\langle L_x\rangle = \langle L_y\rangle = 0$. The part of $\vec{L}$ perpendicular to $z$ has a definite size but no definite direction: that is the cone.
- **Do not take the cone literally.** In a stationary state nothing moves, and $\vec{L}$ does not sweep around its cone. The cone is a picture of what is sharp (the length and the height) and what is not (the direction around $z$).

:::{note} **Example: how close can $\vec{L}$ come to the $z$ axis?**

The smallest angle between $\vec{L}$ and the $z$ axis belongs to $m = l$:

$$
\cos\theta_{\min} = \frac{l}{\sqrt{l(l+1)}} = \frac{1}{\sqrt{1 + 1/l}}
$$

- $l = 1$: $\cos\theta_{\min} = 1/\sqrt{2}$, so $\theta_{\min} = 45°$.
- $l = 2$: $2/\sqrt{6} = 0.816$, so $35.3°$.
- $l = 10$: $10/\sqrt{110} = 0.953$, so $17.5°$.
- A spinning top with $L \approx 10^{-3}$ J s has $l \approx L/\hbar \approx 10^{31}$. For large $l$, $\theta_{\min} \approx 1/\sqrt{l} \approx 3\times10^{-16}$ rad: the top's axis can point anywhere, for all practical purposes.

The quantum fuzziness shrinks as $l$ grows, and a large angular momentum behaves classically: the correspondence principle again, as for the box at large $n$ and the oscillator at large $v$.
:::

::::{tip} **Going further: why $m$ climbs in steps of one (raising and lowering operators)**
:class: dropdown

The spherical harmonics came from solving a differential equation. As for the oscillator in [Lecture 4.2](02-quantum-harmonic-oscillator.md), the commutators alone give the whole ladder of $m$ values, and they explain the $l(l + 1)$.

**Two new operators.** Combine the two components that are not sharp:

$$
\hat{L}_+ = \hat{L}_x + i\hat{L}_y, \qquad \hat{L}_- = \hat{L}_x - i\hat{L}_y
$$

Their commutators with $\hat{L}_z$ follow from the cyclic rules, $[\hat{L}_z, \hat{L}_x] = i\hbar\hat{L}_y$ and $[\hat{L}_z, \hat{L}_y] = -i\hbar\hat{L}_x$:

$$
[\hat{L}_z, \hat{L}_\pm] = [\hat{L}_z, \hat{L}_x] \pm i\,[\hat{L}_z, \hat{L}_y] = i\hbar\hat{L}_y \pm \hbar\hat{L}_x = \pm\hbar\left(\hat{L}_x \pm i\hat{L}_y\right) = \pm\hbar\,\hat{L}_\pm
$$

**Climbing.** Let $\hat{L}_zY = m\hbar\,Y$. Rewrite the commutator as $\hat{L}_z\hat{L}_+ = \hat{L}_+\hat{L}_z + \hbar\hat{L}_+$ and apply it to $Y$:

$$
\hat{L}_z\big(\hat{L}_+Y\big) = \hat{L}_+\big(\hat{L}_z + \hbar\big)Y = (m + 1)\,\hbar\,\big(\hat{L}_+Y\big)
$$

$\hat{L}_+Y$ is again an eigenfunction of $\hat{L}_z$, with $m$ one higher: $\hat{L}_+$ **raises** $m$ by one, and in the same way $\hat{L}_-$ **lowers** it by one. Both commute with $\hat{L}^2$, so $l$ does not change. Compare $\hat{H}\hat{a}^\dagger = \hat{a}^\dagger(\hat{H} + \hbar\omega)$ for the oscillator.

**The ladder has a top and a bottom.** Climbing cannot go on forever. Write $L^2 = \lambda\hbar^2$. Then

$$
\langle L_x^2\rangle + \langle L_y^2\rangle = \langle L^2\rangle - \langle L_z^2\rangle = (\lambda - m^2)\,\hbar^2
$$

and an average of squares cannot be negative, so $m^2 \leq \lambda$. There must be a top rung that $\hat{L}_+$ turns into nothing, $\hat{L}_+Y_{\text{top}} = 0$, and a bottom rung with $\hat{L}_-Y_{\text{bottom}} = 0$. To find where they are, multiply out

$$
\hat{L}_-\hat{L}_+ = \hat{L}_x^2 + \hat{L}_y^2 + i\,[\hat{L}_x, \hat{L}_y] = \hat{L}^2 - \hat{L}_z^2 - \hbar\hat{L}_z
$$

Call the $m$ of the top rung $l$. There the left side gives zero:

$$
0 = \hat{L}_-\hat{L}_+Y_{\text{top}} = \left(\lambda - l^2 - l\right)\hbar^2\,Y_{\text{top}} \quad\Longrightarrow\quad \lambda = l(l + 1)
$$

The same steps with $\hat{L}_+\hat{L}_- = \hat{L}^2 - \hat{L}_z^2 + \hbar\hat{L}_z$ put the bottom rung at $m = -l$. In between the rungs are one apart, so $2l$ is a whole number:

- **$L^2 = \hbar^2l(l + 1)$ follows from the commutators alone.** The extra $l\hbar^2$ beyond $l^2\hbar^2$ is $\langle L_x^2 + L_y^2\rangle$ on the top rung: the part of $\vec{L}$ that cannot line up with $z$, because $\hat{L}_x$ and $\hat{L}_y$ do not commute. It plays the role of the oscillator's $\frac{1}{2}\hbar\omega$.
- **$l$ can be $0, \frac{1}{2}, 1, \frac{3}{2}, 2, \dots$** The algebra allows half-integers. A particle moving in space needs whole $m$, because $e^{im\phi}$ must join up around the ring, so orbital motion and molecular rotation have whole $l$. The half-integer ladders are realized by **spin**: the electron's own angular momentum has $l = \frac{1}{2}$, written $s = \frac{1}{2}$ ([Spin](../ch05/03-spin.md)).

:::{figure} ./images/m_ladders.png
:alt: Ladders of m values for l = 0, 1, 2 and for l = 1/2, 3/2, with raising and lowering arrows on the l = 2 ladder
:width: 100%

Every ladder the commutators allow. Each has $2l + 1$ rungs one $\hbar$ apart, from $m = -l$ to $m = +l$. On the $l = 2$ ladder, $\hat{L}_+$ (orange) climbs and $\hat{L}_-$ (purple) descends, and both stop at the ends. Ladders with whole $l$ describe rotation in space; the half-integer ones (dashed) describe spin.
:::

**In summary:**

$$
\hat{L}_\pm = \hat{L}_x \pm i\hat{L}_y, \qquad [\hat{L}_z, \hat{L}_\pm] = \pm\hbar\,\hat{L}_\pm
$$

$$
\hat{L}_\pm\,Y_l^m = \hbar\sqrt{l(l+1) - m(m \pm 1)}\;Y_l^{m\pm1}, \qquad \hat{L}_+Y_l^l = 0, \qquad \hat{L}_-Y_l^{-l} = 0
$$

- The square root keeps the states normalized, like the $\sqrt{v + 1}$ of the oscillator. Since $\hat{L}_-$ is the adjoint of $\hat{L}_+$, the squared length of $\hat{L}_+Y_l^m$ is $\langle Y_l^m|\hat{L}_-\hat{L}_+|Y_l^m\rangle = \hbar^2\left[l(l+1) - m^2 - m\right]$.
- $\hat{L}_x = (\hat{L}_+ + \hat{L}_-)/2$ connects $m$ only to $m \pm 1$, so $\langle L_x\rangle = 0$ in every $Y_l^m$, as the cone said. It is the same nearest-neighbor pattern as $\hat{x}$ among the oscillator states.
- In spherical coordinates (Problem 8):

$$
\hat{L}_\pm = \hbar\,e^{\pm i\phi}\left(\pm\frac{\partial}{\partial\theta} + i\cot\theta\,\frac{\partial}{\partial\phi}\right)
$$
::::

### Toward the rigid rotor

| | particle on a ring | particle on a sphere |
| :-- | :-- | :-- |
| coordinates | $\phi$ | $\theta$ and $\phi$ |
| sharp observables | $\hat{L}_z$ | $\hat{L}^2$ and $\hat{L}_z$ |
| quantum numbers | $m = 0, \pm 1, \pm 2, \dots$ | $l = 0, 1, 2, \dots$ and $m = -l, \dots, l$ |
| states | $e^{im\phi}/\sqrt{2\pi}$ | $Y_l^m(\theta, \phi)$ |
| Hamiltonian | $\hat{L}_z^2/2I$ | $\hat{L}^2/2I$ |
| energies | $m^2\hbar^2/2I$ | $l(l+1)\hbar^2/2I$ |
| states per level | 2 (1 for $m = 0$) | $2l + 1$ |
| lowest energy | 0 | 0 |

- A diatomic molecule turning with a fixed bond length $R_e$ is a particle with its reduced mass $\mu$ on a sphere of radius $R_e$ ([Lecture 4.1](01-molecular-degrees-of-freedom.md)): $\hat{H} = \hat{L}^2/2I$ with $I = \mu R_e^2$. Its states are the $Y_l^m$ of this lecture, and its energies $l(l + 1)\hbar^2/2I$ climb with ever wider gaps.
- The dipole of a diatomic points along its axis, so light couples to the rotation through $\cos\theta$, and $\cos\theta\,Y_l^m$ is a mixture of $Y_{l+1}^m$ and $Y_{l-1}^m$. That gives the rotational selection rule $\Delta l = \pm 1$. [Lecture 4.5](05-rigid-rotor.md) writes $J$ for $l$ and turns these levels into microwave spectra.

### Problems

#### Problem 1: A methyl group as a rotor

A methyl group spins about the C$-$C bond of ethane. Treat it as three H atoms ($m_{\text{H}} = 1.008$ u) on a ring of radius 1.02 Å, with the carbon on the axis. Find the moment of inertia, the energy unit $\hbar^2/2I$ in cm$^{-1}$, and the first gap. How many states lie below $k_BT$ at 300 K ($k_BT = 208$ cm$^{-1}$)? (Real methyl groups are hindered by a threefold barrier, which this model leaves out.)

:::{admonition} **Solution**
:class: dropdown solution

Each H atom sits $r = 1.02$ Å from the axis, so

$$
I = 3m_{\text{H}}r^2 = 3\,(1.008)(1.661\times10^{-27}\ \text{kg})(1.02\times10^{-10}\ \text{m})^2 = 5.22\times10^{-47}\ \text{kg m}^2
$$

$$
\frac{\hbar^2}{2I} = \frac{(1.055\times10^{-34}\ \text{J s})^2}{2\,(5.22\times10^{-47}\ \text{kg m}^2)} = 1.06\times10^{-22}\ \text{J} = 5.36\ \text{cm}^{-1}
$$

dividing by $hc = 1.986\times10^{-23}$ J cm. The levels are $E_m = 5.36\,m^2$ cm$^{-1}$, so the first gap, from $m = 0$ to $m = \pm 1$, is 5.36 cm$^{-1}$. A level lies below $k_BT$ when $m^2 < 208/5.36 = 38.8$, that is $\lvert m\rvert \leq 6$: thirteen states, $m = -6$ to $6$. A free methyl rotor would be almost classical at room temperature. The real barrier, about 1000 cm$^{-1}$ in ethane, turns its lowest levels into torsional vibrations instead.
:::

#### Problem 2: An electron circling benzene

In the benzene example, an electron in the highest filled level has $\lvert m\rvert = 1$ on a ring of radius 139 pm. Using $L_z = m_e vr$, find its speed, compare it with the speed of light, and find the time for one lap. Its density is the same all around the ring; in what sense is it "circling"? What changes for $\lvert m\rvert = 2$?

#### Problem 3: A lopsided state on a ring

A particle on a ring is in the state $\psi(\phi) = N\cos^2\phi$. Normalize it, write it as a sum of ring states $\Phi_m$, and give the possible results of measuring $L_z$ with their probabilities. Find $\langle L_z\rangle$ and $\langle E\rangle$.

:::{admonition} **Solution**
:class: dropdown solution

**Normalize.** $\int_0^{2\pi}\cos^4\phi\,d\phi = 3\pi/4$, so $N^2 = 4/3\pi$.

**Expand.** With $\cos\phi = (e^{i\phi} + e^{-i\phi})/2$,

$$
\cos^2\phi = \frac{1}{4}\left(e^{2i\phi} + 2 + e^{-2i\phi}\right) = \sqrt{2\pi}\left(\frac{1}{2}\,\Phi_0 + \frac{1}{4}\,\Phi_2 + \frac{1}{4}\,\Phi_{-2}\right)
$$

so $c_0 = N\sqrt{2\pi}/2$ and $c_{\pm 2} = N\sqrt{2\pi}/4$. With $2\pi N^2 = 8/3$:

$$
\lvert c_0\rvert^2 = \frac{8}{3}\cdot\frac{1}{4} = \frac{2}{3}, \qquad \lvert c_{\pm 2}\rvert^2 = \frac{8}{3}\cdot\frac{1}{16} = \frac{1}{6}\ \text{each}
$$

The three add up to 1.

**Measure.** $L_z = 0$ with probability $2/3$, and $+2\hbar$ or $-2\hbar$ with probability $1/6$ each. The two directions balance, so $\langle L_z\rangle = 0$.

**Energy.** $E_0 = 0$ and $E_{\pm 2} = 4\hbar^2/2I$, so

$$
\langle E\rangle = \frac{2}{3}\cdot 0 + \frac{1}{3}\cdot\frac{2\hbar^2}{I} = \frac{2\hbar^2}{3I}
$$

Check directly: $\langle E\rangle = \frac{\hbar^2}{2I}\int_0^{2\pi}\left\lvert\frac{d\psi}{d\phi}\right\rvert^2 d\phi = \frac{\hbar^2}{2I}\,N^2\int_0^{2\pi}\sin^2 2\phi\,d\phi = \frac{\hbar^2}{2I}\cdot\frac{4}{3\pi}\cdot\pi = \frac{2\hbar^2}{3I}$.
:::

#### Problem 4: Powers of $x + iy$

Show that $\hat{L}_z(x + iy) = \hbar\,(x + iy)$ and, using the product rule, that $\hat{L}_z(x + iy)^k = k\hbar\,(x + iy)^k$. Write $(x + iy)^k$ in spherical coordinates. Which spherical harmonic is it proportional to for $k = 1$ and $k = 2$ (on the unit sphere)? Why must $(x + iy)^k/r^k$ be the top rung of its ladder?

#### Problem 5: Measuring $L_x$ when $L_z$ is sharp

A particle is in the $l = 1$ state $x + iy$ (up to normalization), which has $L_z = +\hbar$. Using the $3\times3$ matrices (the "Going further" box after the $\hat{L}_z$ example), find the possible results of measuring $L_x$ and their probabilities, and compute $\langle L_x\rangle$ and $\langle L_x^2\rangle$. Compare with the vector model.

:::{admonition} **Solution**
:class: dropdown solution

The state is the column $\mathbf{v} = (1, i, 0)/\sqrt{2}$. The matrix $L_x$ only mixes $y$ and $z$, so its eigenvectors are

$$
L_x = 0:\ (1, 0, 0), \qquad L_x = +\hbar:\ \frac{1}{\sqrt{2}}(0, 1, i), \qquad L_x = -\hbar:\ \frac{1}{\sqrt{2}}(0, 1, -i)
$$

(check one: $L_x(0, 1, i) = \hbar\,(0, -i\cdot i, i\cdot 1) = \hbar\,(0, 1, i)$). Project the state onto each, $c_k = \langle\mathbf{u}_k|\mathbf{v}\rangle$ with the bra conjugated ([Lecture 3.6](../ch03/06-eigenvalues-and-expectation.md)):

$$
c_0 = \frac{1}{\sqrt{2}}, \qquad c_{+} = \frac{1}{2}\,(0 + 1\cdot i + 0) = \frac{i}{2}, \qquad c_{-} = \frac{1}{2}\,(0 + 1\cdot i + 0) = \frac{i}{2}
$$

So $L_x = 0$ with probability $1/2$, and $+\hbar$ or $-\hbar$ with probability $1/4$ each. Then $\langle L_x\rangle = 0$ and $\langle L_x^2\rangle = \frac{1}{4}\hbar^2 + \frac{1}{4}\hbar^2 = \frac{1}{2}\hbar^2$.

The vector model predicts $\langle L_x^2\rangle = \frac{1}{2}\hbar^2\left[l(l+1) - m^2\right] = \frac{1}{2}\hbar^2\,(2 - 1) = \frac{1}{2}\hbar^2$, in agreement. A sharp $L_z$ leaves $L_x$ spread over all three of its values.

```python
import numpy as np
Lx = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])     # hbar = 1
v = np.array([1, 1j, 0]) / np.sqrt(2)
vals, U = np.linalg.eigh(Lx)
print(vals.round(6), (np.abs(U.conj().T @ v) ** 2).round(6))   # [-1, 0, 1] with [0.25, 0.5, 0.25]
```
:::

#### Problem 6: The magic angle

Show that $Y_2^0 \propto 3\cos^2\theta - 1$ is an eigenfunction of $\hat{L}^2$ with eigenvalue $6\hbar^2$. Find the angles $\theta$ of its two nodal cones. Solid-state NMR spins samples at the first of these angles, the "magic angle"; look up why.

#### Problem 7: How fuzzy are $L_x$ and $L_y$?

Use $\langle L_x^2\rangle = \langle L_y^2\rangle = \frac{1}{2}\hbar^2\left[l(l+1) - m^2\right]$ and $\langle L_x\rangle = \langle L_y\rangle = 0$ to find $\sigma_{L_x}\sigma_{L_y}$ in the state $Y_l^m$. Compare it with the bound $\frac{\hbar}{2}\lvert\langle L_z\rangle\rvert$ from Lecture 3.6. For which $m$ is the bound reached exactly? Interpret the result with the cones.

#### Problem 8: Climbing with $\hat{L}_+$

Use $\hat{L}_+ = \hbar\,e^{i\phi}\left(\partial/\partial\theta + i\cot\theta\,\partial/\partial\phi\right)$ to compute $\hat{L}_+Y_1^0$ and $\hat{L}_+Y_1^1$, with the functions from the table. Check both against $\hat{L}_+Y_l^m = \hbar\sqrt{l(l+1) - m(m+1)}\,Y_l^{m+1}$.

:::{admonition} **Solution**
:class: dropdown solution

**From $Y_1^0 = \sqrt{3/4\pi}\,\cos\theta$.** There is no $\phi$, so only the $\theta$ derivative acts:

$$
\hat{L}_+Y_1^0 = \hbar\,e^{i\phi}\sqrt{\frac{3}{4\pi}}\,(-\sin\theta) = -\hbar\sqrt{\frac{3}{4\pi}}\,\sin\theta\,e^{i\phi}
$$

The formula gives $\hbar\sqrt{2 - 0}\;Y_1^1 = \hbar\sqrt{2}\left(-\sqrt{\frac{3}{8\pi}}\,\sin\theta\,e^{i\phi}\right) = -\hbar\sqrt{\frac{3}{4\pi}}\,\sin\theta\,e^{i\phi}$, the same.

**From $Y_1^1 = -\sqrt{3/8\pi}\,\sin\theta\,e^{i\phi}$.** The two terms are

$$
\frac{\partial Y_1^1}{\partial\theta} = -\sqrt{\frac{3}{8\pi}}\,\cos\theta\,e^{i\phi}, \qquad i\cot\theta\,\frac{\partial Y_1^1}{\partial\phi} = i\cot\theta\,(i)\left(-\sqrt{\frac{3}{8\pi}}\,\sin\theta\,e^{i\phi}\right) = +\sqrt{\frac{3}{8\pi}}\,\cos\theta\,e^{i\phi}
$$

They cancel: $\hat{L}_+Y_1^1 = 0$. The formula agrees, $\sqrt{2 - 1\cdot 2} = 0$: $m = 1$ is the top rung of the $l = 1$ ladder.
:::
