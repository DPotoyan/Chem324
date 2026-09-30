---
kernelspec:
  name: python3
  display_name: Python 3
---

# Particle in a Box

 :::{note} **What you need to know**

 **Particle in a Box (PIB) as a Model System**  
   The Particle in a Box (PIB) is a simple model that helps illustrate the behavior of electrons confined within atoms and molecules. It serves as a useful tool to introduce key quantum concepts:

   - **Energetic Quantization**: Energy levels in quantum systems are discrete, not continuous, as seen in the PIB model.
   
   - **Probabilistic Nature of Quantum Particles**: The probability distribution for the particle's position is non-uniform, with nodal points where the probability is zero, emphasizing the inherent uncertainty in the particle's exact location.
   
   - **Uncertainty Principle**: There is an inverse relationship between the uncertainty in position and momentum, demonstrating the fundamental limit on how precisely both quantities can be known simultaneously.
   
   - **Zero-Point Energy**: Quantum particles always possess a minimum kinetic energy, even at absolute zero. This zero-point energy highlights the impossibility of freezing all motion in quantum systems.
   
   - **Quantum-Classical Correspondence**: As the system scales up, quantum behavior smoothly transitions to classical behavior, illustrating the correspondence principle.

   - **Degeneracy of Energy Levels**: In systems with symmetries, multiple wave functions can correspond to the same energy level, a phenomenon known as degeneracy.
:::

### Classical vs Quantum particle in a box

- The particle in a box is a toy model of an electron (or atom, molecule, or small quantum object) trapped in some region of space $[0,L]$.
- The positional information of a quantum "particle" is described by a quantum wave function $\psi(x)$, which is obtained by solving the Schrödinger equation with boundary conditions.
- Wave functions are standing waves, just as in the vibrating guitar string problem, with one major difference: a quantum wave function has a probabilistic meaning and hence is completely different from the classical notion of a "wave".
- **According to classical mechanics**, in the absence of any attractive interactions the particle bounces back and forth between the walls with constant speed. We therefore expect to find it with equal probability at all locations $x$.
- **According to quantum mechanics**, the quantum particle in the box is found in some regions with high probability and in others with little or zero probability.

```{code-cell} python
:tags: [hide-input]
# synced: box_bounce
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
rng = np.random.default_rng(5)
xc = rng.random(4000)                                       # classical: snapshots at random times
cand = rng.random(16000)
xq = cand[rng.random(16000) < np.sin(3 * np.pi * cand) ** 2][:4000]   # quantum: samples of |psi_3|^2
yj = rng.random(4000)
counts = np.unique(np.round(np.geomspace(1, 4000, 44)).astype(int))
counts = np.concatenate([counts, np.full(8, counts[-1])])
edges = np.linspace(0, 1, 31); mid = 0.5 * (edges[1:] + edges[:-1]); dx = edges[1] - edges[0]
xs = np.linspace(0, 1, 300)
fig, axes = plt.subplots(2, 2, figsize=(8, 3.9), sharex=True,
                         gridspec_kw={"height_ratios": [1, 2.2], "hspace": 0.12, "wspace": 0.1})
(ta, tb), (ha, hb) = axes
for ax in (ta, tb):
    ax.axvline(0, color="k", lw=3); ax.axvline(1, color="k", lw=3)
    ax.set_ylim(0, 1); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.tick_params(bottom=False)
ta.set_title("classical: a ball bouncing at constant speed", loc="left", fontsize=10.5)
tb.set_title(r"quantum, $n = 3$: each dot is one detection", loc="left", fontsize=10.5)
(trail,) = ta.plot([], [], "o", color=ORANGE, ms=9, alpha=0.25)
(ball,) = ta.plot([], [], "o", color=ORANGE, ms=12)
scat = tb.scatter([], [], s=5, color=TEAL, alpha=0.6, lw=0)
bars_c = ha.bar(mid, 0 * mid, width=0.92 * dx, color=ORANGE, alpha=0.5)
bars_q = hb.bar(mid, 0 * mid, width=0.92 * dx, color=TEAL, alpha=0.5)
(pc,) = ha.plot([], [], color=GRAY, lw=2.4, ls="--", label=r"flat: $1/L$")
(pq,) = hb.plot([], [], color=CARDINAL, lw=2.4, label=r"$|\psi_3(x)|^2$")
for ax in (ha, hb):
    ax.set_xlim(-0.02, 1.02); ax.set_yticks([])
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("position x")
    ax.legend(loc="upper right", frameon=False, fontsize=9.5)
ha.set_ylabel("times caught here")
fig.subplots_adjust(left=0.05, right=0.99, top=0.84, bottom=0.13)
sup = fig.suptitle("", fontsize=11.5)
tri = lambda s: 0.04 + 0.92 * (1 - np.abs(2 * (s % 1) - 1))  # bounce between the walls

def update(i):
    N = counts[i]
    pos = tri(np.arange(i - 3, i + 1) / 11.0)
    trail.set_data(pos[:-1], np.full(3, 0.5)); ball.set_data(pos[-1:], [0.5])
    scat.set_offsets(np.column_stack([xq[:N], yj[:N]]))
    hc = np.histogram(xc[:N], bins=edges)[0]; hq = np.histogram(xq[:N], bins=edges)[0]
    for b, c in zip(bars_c, hc):
        b.set_height(c)
    for b, c in zip(bars_q, hq):
        b.set_height(c)
    pc.set_data(xs, np.full_like(xs, N * dx)); pq.set_data(xs, N * dx * 2 * np.sin(3 * np.pi * xs) ** 2)
    top = 1.3 * max(1.0, hc.max(), hq.max(), 2 * N * dx)
    ha.set_ylim(0, top); hb.set_ylim(0, top)
    sup.set_text(f"N = {N} position measurement" + ("" if N == 1 else "s"))

ani = FuncAnimation(fig, update, frames=len(counts), interval=150, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Catching the particle many times. Left: a classical ball bounces between the walls at constant speed, so its position measurements pile up evenly. Right: in the quantum state $n = 3$ the measurements pile up into three lobes, and the particle is never found at $x = L/3$ or $x = 2L/3$. Each dot is one measurement, as in the Born-rule figure of the [previous lecture](01-schrodinger-equation.md).

### Solving the Schrödinger Equation for the Particle in a Box (PIB)


:::{figure} images/ext_infinite_well.svg
:label: fig-particle-in-a-box-2
:alt: Particle in a box
:width: 300px

Particle in a box subject to infinitely high potential walls.
:::

The Schrödinger equation for a particle in a box (PIB) is defined by a Hamiltonian operator that incorporates a potential energy which is infinitely large at the boundaries of the box and zero inside. This potential confines the particle within the box, where it can only possess kinetic energy.

- **The potential energy for PIB is defined:**

$$
V(x) =
\begin{cases} 
\infty & x \le 0 \text{ or } x \ge L \\ 
0 & 0 < x < L
\end{cases}
$$

- **The boundary conditions are:**

$$
\psi(0) = \psi(L) = 0
$$

- **The Hamiltonian operator** in this case accounts only for kinetic energy:

$$
\hat{H} = \hat{K} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2}
$$

- Now, we have all the necessary ingredients to solve the time-independent Schrödinger equation for the 1D PIB:

$$
\hat{H} \psi(x) = E \psi(x)
$$

- Substituting the Hamiltonian, we get:

$$
-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \psi(x) = E \psi(x)
$$

$$
\psi''(x) = -k^2 \psi(x)
$$

- where $k^2$ is a positive real number that relates the particle's energy $E$ to its wavefunction.

$$
k^2 = \frac{2mE}{\hbar^2}
$$

### Solution and Boundary Conditions

- Mathematically, the form of the 1D PIB problem is similar to the ordinary differential equation (ODE) used in the 1D vibrating guitar string problem. The key differences lie in the constant coefficients and the interpretation of the wavefunction.

$$
\psi''(x) = -k^2 \psi(x)
$$

- The general solution to this differential equation is:

$$
\psi(x) = c_1 e^{ikx} + c_2 e^{-ikx} = A \cos(kx) + B \sin(kx)
$$

- Applying the boundary condition $\psi(0) = 0$, we find that $A = 0$, leaving us with:

$$
\psi(x) = B \sin(kx)
$$

- Applying the boundary condition $\psi(L) = 0$, we get:

$$
B \sin(kL) = 0
$$

- This condition is satisfied when:

$$
kL = n\pi \quad \text{or} \quad k = \frac{n\pi}{L}
$$

- Thus, the wavefunction becomes:

$$
\psi(x) = B \sin\left(\frac{n\pi}{L}x\right)
$$

- Using the relationship $k^2 = \frac{n^2\pi^2}{L^2} = \frac{2mE}{\hbar^2}$, we can express the energy levels as:

$$
E_n = \frac{n^2 h^2}{8mL^2}
$$

- The quantization of energy results from confining the wavefunction within a finite space. This is the reason bound states exhibit quantized energy levels. Atoms, molecules, and solids all possess discrete energy levels due to similar constraints.
- This is the trial-energy experiment of the [previous lecture](01-schrodinger-equation.md) in its simplest form. There the decaying tails admitted only special energies; here the walls do: $\sin kx$ reaches zero at $x = L$ only when a whole number of half-waves fits, $L = n\lambda/2$.

### Wavefunctions Must Be Normalized

- Next, we determine the constant coefficient $B_n$ by enforcing the normalization condition:

$$
\int_0^L \psi_n(x)^2 \, dx = 1
$$

- To evaluate the integral, we use the trigonometric identity $\sin^2 x = \frac{1}{2}(1 - \cos 2x)$

$$
B_n^2 \int_0^L \sin^2\left(\frac{n\pi x}{L}\right) dx = \frac{B_n^2}{2} \int_0^L \left[ 1 - \cos\left(\frac{2n\pi x}{L}\right) \right] dx =1
$$

- Since the integral of $\cos\left(\frac{2n\pi x}{L}\right)$ over a full period from $0$ to $L$ is zero, we are left with:

$$
\frac{B_n^2}{2} \cdot L = 1
$$

- Solving for $B_n$, we determine the **normalization constant**, which ensures that the square of the wavefunction integrates to 1.

$$
B_n = \sqrt{\frac{2}{L}}
$$

### PIB Eigenfunctions and Eigenvalues

:::{important} **Eigenfunctions and eigenvalues of 1D particle in a box**

$${\psi_n(x) = \Big (\frac{2}{L}\Big)^{\frac{1}{2}} \sin\frac{n\pi x}{L}}$$

$${E_n=\frac{n^2 h^2}{8mL^2}}$$

:::

:::{important} **Full time dependent solution**

$${\psi_n(x, t) = \Big (\frac{2}{L}\Big)^{\frac{1}{2}} \sin\frac{n\pi x}{L}}\cdot e^{-i\frac{E_n t}{\hbar}}$$

$$\Psi(x,t) = \sum_n c_n \psi_n(x, t)$$

- where the coefficients $c_n$ depend on the initial condition. For example, all could be zero except one (a pure state), or a few could be non-zero (a mixed state).

:::

```{code-cell} python
:tags: [hide-input]
# synced: pib_ladder
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 400)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.4), sharey=True, gridspec_kw={"wspace": 0.08})
for ax in (ax1, ax2):
    ax.plot([0, 0, 1, 1], [18.3, 0, 0, 18.3], color="k", lw=2.6)
    ax.set_xlim(-0.04, 1.04); ax.set_ylim(-0.4, 18.3)
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("x")
    ax.spines["left"].set_visible(False)
for n in range(1, 5):
    E, s = n * n, np.sin(n * np.pi * x)
    for ax in (ax1, ax2):
        ax.hlines(E, 0, 1, color=GRAY, lw=0.8, ls="--")
    ax1.plot(x, E + 1.25 * s, color=TEAL, lw=2.4)
    ax2.fill_between(x, E, E + 1.6 * s**2, color=CARDINAL, alpha=0.18, lw=0)
    ax2.plot(x, E + 1.6 * s**2, color=CARDINAL, lw=2.2)
    ax2.plot(np.arange(1, n) / n, np.full(n - 1, E), "o", color="k", ms=5, zorder=5)
    ax2.text(1.06, E, rf"$n = {n}$,  " + (r"$E_1$" if n == 1 else rf"${E}E_1$"), va="center", fontsize=11.5)
ax1.set_yticks([]); ax1.set_ylabel("energy")
ax1.set_title(r"$\psi_n(x)$, drawn on its level $E_n$", loc="left", fontsize=11)
ax2.set_title(r"$|\psi_n(x)|^2$: dots mark the $n-1$ nodes", loc="left", fontsize=11)
fig.subplots_adjust(left=0.05, right=0.83, top=0.92, bottom=0.12)
plt.show()
```

Fig. The four lowest states of the particle in a box, each drawn on its energy level $E_n = n^2E_1$. Left: the wavefunctions $\psi_n(x)$. Right: the probability densities $|\psi_n(x)|^2$; the dots mark the $n-1$ nodes, where the particle is never found.

### Discrete energy levels and zero point energy

**Quantum particles are never at rest**

- The lowest energy an electron in a box can have is at $n=1$, and it is not zero!

$$E_1 = h^2/8mL^2$$

- Keeping in mind that the energy is purely kinetic, this means a quantum particle never ceases its motion.

- This is the **uncertainty principle** at work. Confining the particle to a length $L$ leaves a position spread $\sigma_x \approx 0.18L$ in the ground state (Problem 2), and the momentum cannot be pinned down either: $\langle p \rangle = 0$ but $\langle p^2 \rangle = (h/2L)^2$, so $\sigma_p = h/2L$. The product $\sigma_x\sigma_p \approx 0.57\hbar$ sits just above the Heisenberg limit $\hbar/2$. A smaller box means a larger $\sigma_p$ and a larger kinetic energy.

- The spacing of energy levels is finite and depends on the size of the box:

$$E_{n+1} - E_n = (2n+1)\frac{h^2}{8mL^2}$$

**Increasing Box size leads to more classical behavior**

- As the box size is increased, the energy spacing gets smaller.
- Thus quantum effects are more pronounced when an electron is bound in smaller regions of space.

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
      "plotly",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
import plotly.graph_objects as go
TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
```

```{marimo} python
:hide-code: true

box_L = mo.ui.slider(0.5, 1.0, step=0.05, value=1.0, show_value=True, label="box length L (units of L₀)")
box_L
```

```{marimo} python
:hide-code: true

_L = box_L.value
_x = np.linspace(0, _L, 300)
_fig, (_ax, _axl) = plt.subplots(1, 2, figsize=(7.5, 3.4), gridspec_kw={"width_ratios": [1.4, 1]})
_ax.plot([0, 0, _L, _L], [38, 0, 0, 38], color="k", lw=2.6)
for _n, _c in zip((1, 2, 3), (TEAL, ORANGE, PURPLE)):
    _E = _n**2 / _L**2
    _ax.hlines(_E, 0, _L, color=_c, lw=0.9, ls="--")
    _ax.plot(_x, _E + 1.2 * np.sin(_n * np.pi * _x / _L), color=_c, lw=2.4)
    _ax.text(_L + 0.05, _E, rf"$E_{_n} = {_E:.1f}$", color=_c, va="center", fontsize=11)
_ax.text(0, -1.5, "0", ha="center", va="top", fontsize=11)
_ax.text(_L, -1.5, "L", ha="center", va="top", fontsize=11)
_ax.set_xlim(-0.05, 1.42); _ax.set_ylim(-4.5, 38); _ax.set_xticks([]); _ax.set_yticks([])
_ax.spines["left"].set_visible(False); _ax.spines["bottom"].set_visible(False)
_ax.set_title(rf"$L = {_L:.2f}\,L_0$", loc="left", fontsize=11)
_Lg = np.linspace(0.45, 3, 300)
_axl.plot(_Lg, 1 / _Lg**2, color=TEAL, lw=2.2)
_axl.plot([_L], [1 / _L**2], "o", color=TEAL, ms=9)
_axl.set_xlim(0.4, 3); _axl.set_ylim(0, 5)
_axl.set_xlabel(r"$L / L_0$"); _axl.set_ylabel(r"$E_1$")
_axl.set_title(r"$E_1 \propto 1/L^2$: never zero", loc="left", fontsize=11)
_fig.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.17, wspace=0.22)
_fig
```

Fig. Left: the three lowest levels of a particle in a box of length $L$, each wavefunction drawn on its level. Right: the ground-state energy against box length. Shrinking the box raises every level as $1/L^2$; enlarging it lowers $E_1$ toward zero without ever reaching it. Energies in units of $h^2/8mL_0^2$.

### Non-uniform probabilities and nodes

1. **Nodes imply zero probability to find an electron in the box**. 
    - $|\psi_n|^2=0$ at nodal points, which means zero probability.
    - This sharply contradicts classical mechanics, which bases its prediction on purely particle-like motion of the electron.
    - The existence of nodes implies a wave-like character of the electron.

2. **There are $n-1$ nodes for quantum state $n$**

- Recall that the sine function hits zero at integer multiples of $\pi$: $\sin(n\pi)=0$ when $n=1,2,3,4,...$
- The wavefunction $\psi_n(x) = \sin \frac{n\pi x}{L}$ then has $n-1$ nodes at the points $x=L/n$, $2L/n$, $3L/n$, ..., $(n-1)L/n$.
- Note that we do not count the $x=0$ and $x=L$ points as nodes, because they are part of the boundary conditions that apply to all wavefunctions.
    - For instance, the $n=3$ nodes are at $x=L/3$ and $x=2L/3$.
    - For instance, the $n=4$ nodes are at $L/4$, $2L/4$, and $3L/4$.

- The dots in the right panel of the figure of the four lowest states mark these nodes.

### Large quantum numbers: the classical box returns

- As $n$ grows, the lobes of $|\psi_n|^2$ crowd together. A real detector has a finite resolution and averages over many lobes, and $\sin^2$ averages to $\frac{1}{2}$ over whole half-waves, so the measured density approaches the flat classical value $1/L$.
- Problem 1 gives the probability of catching the particle in the middle third of the box:

$$
P_n = \frac{1}{3} + \frac{\sin(2n\pi/3) - \sin(4n\pi/3)}{2n\pi}
$$

- The correction to the classical $\frac{1}{3}$ dies off as $1/n$. This is the **correspondence principle**: quantum predictions go over to classical ones at large quantum numbers. A 1 g marble crawling at 1 cm/s across a 30 cm box has $n \approx 10^{28}$, far beyond any lobe we could resolve.

```{marimo} python
:hide-code: true

n_c = mo.ui.slider(1, 40, step=1, value=1, show_value=True, label="quantum number n")
n_c
```

```{marimo} python
:hide-code: true

_n = n_c.value
_x = np.linspace(0, 1, 3000)
_p = 2 * np.sin(_n * np.pi * _x) ** 2
_P = 1 / 3 + (np.sin(2 * _n * np.pi / 3) - np.sin(4 * _n * np.pi / 3)) / (2 * _n * np.pi)
_fig, _ax = plt.subplots(figsize=(7, 3.0))
_ax.axvspan(1 / 3, 2 / 3, color=PURPLE, alpha=0.09, lw=0)
_ax.fill_between(_x, _p, color=CARDINAL, alpha=0.2, lw=0)
_ax.plot(_x, _p, color=CARDINAL, lw=1.4 if _n < 12 else 0.8, label=r"$|\psi_n|^2$")
_ax.axhline(1, color="k", lw=2, ls="--", label=r"classical: $1/L$")
_ax.plot([0, 0, 1, 1], [2.6, 0, 0, 2.6], color="k", lw=2.6)
_ax.set_xlim(-0.02, 1.02); _ax.set_ylim(0, 2.6)
_ax.set_yticks([0, 1, 2]); _ax.set_yticklabels(["0", "1/L", "2/L"])
_ax.set_xticks([0, 1 / 3, 2 / 3, 1]); _ax.set_xticklabels(["0", "L/3", "2L/3", "L"])
_ax.legend(loc="upper right", frameon=False, fontsize=10, ncol=2, bbox_to_anchor=(1.0, 1.18))
_ax.set_title(f"n = {_n}:  P(middle third) = {_P:.3f}", loc="left", fontsize=11, color=PURPLE)
_fig.tight_layout()
_fig
```

Fig. The probability density of state $n$ against the flat classical density $1/L$. The shaded band is the middle third of the box; its probability tends to the classical $\frac{1}{3}$ as $n$ grows.

### Superposition: the particle sloshes

- A single state $\psi_n(x)\,e^{-iE_nt/\hbar}$ is stationary. Its phase turns, but the time factor has absolute value one, so $|\psi_n(x,t)|^2 = |\psi_n(x)|^2$ never changes (see the phase clocks in the [previous lecture](01-schrodinger-equation.md)).
- A superposition of two states does move. Take equal amounts of the two lowest states:

$$
\Psi(x,t) = \frac{1}{\sqrt{2}}\left[\psi_1(x)\,e^{-iE_1t/\hbar} + \psi_2(x)\,e^{-iE_2t/\hbar}\right]
$$

- Multiplying by the complex conjugate (Problem 2 of the previous lecture) leaves a fixed part and a **cross term** that oscillates at the difference of the two phase rates, $\omega = (E_2 - E_1)/\hbar$:

$$
|\Psi(x,t)|^2 = \frac{1}{2}\left[\psi_1^2(x) + \psi_2^2(x)\right] + \psi_1(x)\,\psi_2(x)\cos\omega t
$$

```{code-cell} python
:tags: [hide-input]
# synced: box_slosh
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 400)
p1, p2 = np.sqrt(2) * np.sin(np.pi * x), np.sqrt(2) * np.sin(2 * np.pi * x)
fixed, cross = 0.5 * (p1**2 + p2**2), p1 * p2               # |Psi|^2 = fixed + cross cos(wt): even + odd about L/2
nf = 60
ts = np.linspace(0, 2 * np.pi, nf, endpoint=False)          # E1 = 1, E2 = 4, hbar = 1: w = 3, three sloshes
xbar = lambda t: 0.5 - 16 / (9 * np.pi**2) * np.cos(3 * t)  # <x>(t) = L/2 + x12 cos(wt), x12 = -16L/9pi^2
th = np.linspace(0, 2 * np.pi, 200)
fig = plt.figure(figsize=(7.2, 3.4))
gs = fig.add_gridspec(2, 2, width_ratios=[2.3, 1], height_ratios=[2, 1], hspace=0.42, wspace=0.08)
ax, axx = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[1, 0])
axc, axl = fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])
ax.plot(x, fixed, color=GRAY, lw=1.8, ls="--", label=r"$\frac{1}{2}(\psi_1^2 + \psi_2^2)$")
(dens,) = ax.plot([], [], color=CARDINAL, lw=2.8, label=r"$|\Psi|^2$")
band = [ax.fill_between(x, 0 * x, color=CARDINAL, alpha=0.18, lw=0)]
(mark,) = ax.plot([], [], marker="^", color=PURPLE, ms=14, zorder=6, ls="none", label=r"$\langle x\rangle$")
ax.plot([0, 0, 1, 1], [3.35, 0, 0, 3.35], color="k", lw=2.6)          # peak of |Psi|^2 is 3.10
ax.set_xlim(-0.02, 1.02); ax.set_ylim(0, 3.35); ax.set_xticks([]); ax.set_yticks([])
ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
ax.legend(loc="lower left", bbox_to_anchor=(0, 0.97), ncol=3, frameon=False, fontsize=13,
          handlelength=1.6, columnspacing=1.4)
axx.axhline(0, color=GRAY, lw=0.8)
(crs,) = axx.plot([], [], color=PURPLE, lw=2.6)
cband = [axx.fill_between(x, 0 * x, color=PURPLE, alpha=0.18, lw=0)]
axx.set_xlim(-0.02, 1.02); axx.set_ylim(-1.7, 1.7); axx.set_yticks([])
axx.set_xticks([0, 0.5, 1]); axx.set_xticklabels(["0", "L/2", "L"], fontsize=13)
axx.spines["left"].set_visible(False)
axx.set_title(r"cross term $\psi_1\psi_2\cos\omega t$", loc="left", fontsize=13, color=PURPLE)
for a in (ax, axx):
    a.axvline(0.5, color=GRAY, lw=0.8, ls=":")
axc.plot(np.cos(th), np.sin(th), color=GRAY, lw=1, ls="--")
(arc,) = axc.plot([], [], color=PURPLE, lw=3.2, label=r"$\omega t$")
(h1,) = axc.plot([], [], color=TEAL, lw=3.2, label=r"$E_1$")
(h2,) = axc.plot([], [], color=ORANGE, lw=3.2, label=r"$E_2 = 4E_1$")
axc.set_aspect("equal"); axc.set_xlim(-1.15, 1.15); axc.set_ylim(-1.15, 1.15); axc.set_axis_off()
axc.set_title("phase clocks", fontsize=13)
axl.set_axis_off()
axl.legend(handles=[h1, h2, arc], loc="center", frameon=False, fontsize=13, handlelength=1.2)
fig.subplots_adjust(left=0.02, right=0.99, top=0.87, bottom=0.1)

def update(i):
    t = ts[i]
    c = cross * np.cos(3 * t)
    dens.set_data(x, fixed + c)
    band[0].remove(); band[0] = ax.fill_between(x, fixed + c, color=CARDINAL, alpha=0.18, lw=0)
    mark.set_data([xbar(t)], [0.14])
    crs.set_data(x, c)
    cband[0].remove(); cband[0] = axx.fill_between(x, c, color=PURPLE, alpha=0.18, lw=0)
    a1, a2 = -t, -4 * t                                     # clock hands: e^{-iE1 t}, e^{-iE2 t}
    d = (a1 - a2) % (2 * np.pi)                             # angle between the hands, w t
    s = np.linspace(a2, a2 + d, 40) if d <= np.pi else np.linspace(a1, a1 + 2 * np.pi - d, 40)
    arc.set_data(0.42 * np.cos(s), 0.42 * np.sin(s))
    h1.set_data([0, np.cos(a1)], [0, np.sin(a1)]); h2.set_data([0, np.cos(a2)], [0, np.sin(a2)])

ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. An equal superposition of $\psi_1$ and $\psi_2$. Top: the density $|\Psi|^2$ is the fixed part $\frac{1}{2}(\psi_1^2 + \psi_2^2)$ (dashed) plus the cross term; the triangle marks $\langle x \rangle$. Bottom: the cross term $\psi_1\psi_2\cos\omega t$. Right: the phase clocks of the two states; the angle between their hands is $\omega t$.

- The fixed part is symmetric about the center of the box, so on its own it balances at $L/2$. The cross term is odd about the center: it adds probability on one side, removes the same amount on the other, and flips sign every half period. The mean position swings with it:

$$
\langle x \rangle(t) = \frac{L}{2} + \cos\omega t \int_0^L x\,\psi_1\psi_2\,dx = \frac{L}{2} - \frac{16L}{9\pi^2}\cos\omega t
$$

- For an electron, an oscillating $\langle x \rangle$ is an oscillating electric dipole: a tiny antenna that emits or absorbs light of angular frequency $\omega$, that is photons with $h\nu = E_2 - E_1$. This is the link to the colors of conjugated molecules in the applications below. The general theory is in [Time Dependence](06-time-dependence.md).

### Quantum PIB in 3D

:::{figure} ./images/pib3d.png
:label: fig-particle-in-a-box-3
:alt: pib1
:width: 300px

Particle in a 3D box subject to infinitely high potential walls.
:::

$$\hat{H}\psi(x,y,z) = E\psi(x,y,z)$$


$${-\frac{\hbar^2}{2m}\left(\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2}\right) = E\psi}$$

- Where we set $V=0$ for particle inside the box and enforce the solutions $\psi$ to be normalized within the confines of the box (electron must be somewhere in the box!)

$${\int\limits_{-\infty}^{\infty}\int\limits_{-\infty}^{\infty}\int\limits_{-\infty}^{\infty}\left|\psi(x,y,z)\right|^2dxdydz = 1}$$

- Consider a particle in a box with side lengths $a$ in $x$, $b$ in $y$, and $c$ in $z$. The potential is zero inside the box and infinite outside it. Again, the potential term can be handled by boundary conditions (i.e., infinite potential implies that the wavefunction must be zero there). The above equation can now be written as:

$${-\frac{\hbar^2}{2m}\Delta\psi = E\psi} \\
{\textnormal{with }\psi(a,y,z) = \psi(x,b,z) = \psi(x,y,c) = 0} \\
{\textnormal{and }\psi(0,y,z) = \psi(x,0,z) = \psi(x,y,0) = 0}$$

- **Note the Laplacian symbol $\Delta$**, which concisely denotes the sum of the three second-order derivatives with respect to the spatial variables. We will see this operator in all 3D problems.
- In general, when the potential term can be expressed as a sum of terms that depend separately on $x$, $y$, and $z$, the solutions can be written as a product:

$${\psi(x,y,z) = X(x)Y(y)Z(z)}$$

- By substituting and dividing by $X(x)Y(y)Z(z)$, we obtain:

$${-\frac{\hbar^2}{2m}\left[\frac{1}{X(x)}\frac{d^2X(x)}{dx^2} + \frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2} + \frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}\right] = E}$$

- The total energy $E$ consists of a sum of three terms, each depending separately on $x$, $y$, and $z$. Thus we can write $E = E_x + E_y + E_z$ and separate the equation into three one-dimensional problems:

$${-\frac{\hbar^2}{2m}\left[\frac{1}{X(x)}\frac{d^2X(x)}{dx^2}\right] = E_x\textnormal{ with }X(0) = X(a) = 0}\\
{-\frac{\hbar^2}{2m}\left[\frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2}\right] = E_y\textnormal{ with }Y(0) = Y(b) = 0}\\
{-\frac{\hbar^2}{2m}\left[\frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}\right] = E_z\textnormal{ with }Z(0) = Z(c) = 0}$$

- Thus we find energy quantization due to spatial confinement of the quantum wave function in the $x$, $y$, and $z$ dimensions:

$${X(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n_x\pi x}{a}\right)}\\
{Y(y) = \sqrt{\frac{2}{b}}\sin\left(\frac{n_y\pi y}{b}\right)}\\
{Z(z) = \sqrt{\frac{2}{c}}\sin\left(\frac{n_z\pi z}{c}\right)}$$

:::{important} **Eigenfunctions and eigenvalues of particle in 3D Box**

**Rectangular Box**

$${\psi(x,y,z) = X(x)Y(y)Z(z) = \sqrt{\frac{8}{abc}}\sin\left(\frac{n_x\pi x}{a}\right)\sin\left(\frac{n_y\pi y}{b}\right)\sin\left(\frac{n_z\pi z}{c}\right)}$$

$${E_{n_x,n_y,n_z} = \frac{h^2}{8m}\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2}\right)}$$

**Cubic Box**

$$
\psi_{n_x, n_y, n_z}(x, y, z) = \frac{2}{L^{3/2}} \sin\left( \frac{n_x \pi x}{L} \right) \sin\left( \frac{n_y \pi y}{L} \right) \sin\left( \frac{n_z \pi z}{L} \right)
$$


$$
E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)
$$


:::


- Energy is quantized and when $a = b = c$, we find that the energy levels can also be **degenerate** (i.e., the same energy with different values of $n_x, n_y$ and $n_z$).

- In most cases, **degeneracy in quantum mechanics arises from symmetry**. When $a = b = c$, the first excited level is triply degenerate: $(2,1,1)$, $(1,2,1)$ and $(1,1,2)$ are one shape turned to face different axes. When only $a = b \neq c$, that level splits into a pair and a single state; the pair lies lower when $c$ is shorter than $a$.


:::{admonition} **Table of energy levels for a cubic box**
:class: dropdown

Energies in units of $E_0 = \dfrac{h^2}{8mL^2}$, so $E = (n_x^2 + n_y^2 + n_z^2)\,E_0$. The degeneracy $g$ counts the states on each level.

| $n_x^2 + n_y^2 + n_z^2$ | states $(n_x, n_y, n_z)$ | degeneracy $g$ |
| :-- | :-- | :-- |
| 3 | (1,1,1) | 1 |
| 6 | (2,1,1), (1,2,1), (1,1,2) | 3 |
| 9 | (2,2,1), (2,1,2), (1,2,2) | 3 |
| 11 | (3,1,1), (1,3,1), (1,1,3) | 3 |
| 12 | (2,2,2) | 1 |
| 14 | all six orderings of (3,2,1) | 6 |
| 17 | (3,2,2), (2,3,2), (2,2,3) | 3 |
| 18 | (4,1,1), (1,4,1), (1,1,4) | 3 |
| 19 | (3,3,1), (3,1,3), (1,3,3) | 3 |
| 21 | all six orderings of (4,2,1) | 6 |
| 22 | (3,3,2), (3,2,3), (2,3,3) | 3 |
| 24 | (4,2,2), (2,4,2), (2,2,4) | 3 |
| 26 | all six orderings of (4,3,1) | 6 |
| 27 | (3,3,3) and the three orderings of (5,1,1) | 4 |

The last row is an **accidental** degeneracy: $3^2 + 3^2 + 3^2 = 5^2 + 1^2 + 1^2$, and no rotation of the cube turns $(3,3,3)$ into $(5,1,1)$.
:::


```{marimo} python
:hide-code: true

nx3 = mo.ui.slider(1, 4, step=1, value=2, show_value=True, label="nx")
ny3 = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="ny")
nz3 = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="nz")
mo.hstack([nx3, ny3, nz3], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

side3 = 10.0
g3 = np.linspace(0, side3, 48)
X3, Y3, Z3 = np.meshgrid(g3, g3, g3, indexing="ij")

def psi1d_m(q, n_q):
    return np.sqrt(2 / side3) * np.sin(n_q * np.pi * q / side3)

psi_3d = psi1d_m(X3, nx3.value) * psi1d_m(Y3, ny3.value) * psi1d_m(Z3, nz3.value)
amp3 = 0.5 * np.abs(psi_3d).max()

fig3d = go.Figure(data=go.Isosurface(
    x=X3.flatten(), y=Y3.flatten(), z=Z3.flatten(), value=psi_3d.flatten(),
    colorscale="RdBu", isomin=-amp3, isomax=amp3, surface_count=2,
    showscale=False, caps=dict(x_show=False, y_show=False, z_show=False),
))
fig3d.update_layout(
    scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="z", aspectmode="data"),
    width=680, height=460,
    title_text=f"wavefunction isosurfaces, state ({nx3.value}, {ny3.value}, {nz3.value})",
)
fig3d
```

Fig. Surfaces of constant $\psi_{n_x n_y n_z}$ in a cubic box, red and blue for the two signs. Set $(2,1,1)$ and then $(1,2,1)$: the same shape turned by $90°$, so the two states share an energy.

- The level diagram below does the counting. Each short bar is one state. With all three sides equal, states related by a rotation of the box share a level; stretch or squeeze one side and those levels split.

```{marimo} python
:hide-code: true

side_a = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side a (units of L)")
side_b = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side b")
side_c = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side c")
mo.hstack([side_a, side_b, side_c], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

_s = (side_a.value, side_b.value, side_c.value)
_E = {}
for _i in range(1, 9):
    for _j in range(1, 9):
        for _k in range(1, 9):
            _E[(_i, _j, _k)] = _i**2 / _s[0]**2 + _j**2 / _s[1]**2 + _k**2 / _s[2]**2
_levels = []
for _st in sorted(_E, key=_E.get):
    if _levels and abs(_E[_st] - _levels[-1][0]) < 1e-6:
        _levels[-1][1].append(_st)
    else:
        _levels.append([_E[_st], [_st]])
_levels = _levels[:7]
_top = _levels[-1][0] * 1.08
_fig, _ax = plt.subplots(figsize=(7, 4.2))
_ylab = -1.0
for _Eg, _ss in _levels:
    _g = len(_ss)
    _col = PURPLE if _g > 1 else TEAL
    for _q in range(_g):
        _ax.hlines(_Eg, 0.1 + 0.34 * _q, 0.38 + 0.34 * _q, color=_col, lw=3.2)
    _ylab = max(_Eg, _ylab + 0.055 * _top)                  # keep labels of close levels apart
    _lab = f"g = {_g}:  " + ", ".join(f"({_a},{_b},{_c})" for _a, _b, _c in _ss) if _g <= 3 else f"g = {_g}"
    _ax.text(2.2, _ylab, _lab, va="center", fontsize=10, color=_col)
_ax.set_xlim(0, 5.4); _ax.set_ylim(0, _top)
_ax.set_xticks([]); _ax.set_yticks([]); _ax.spines["bottom"].set_visible(False)
_ax.set_ylabel(r"energy (units of $h^2/8mL^2$)")
_ax.set_title(f"sides a, b, c = {_s[0]:.2f}, {_s[1]:.2f}, {_s[2]:.2f}: the seven lowest levels", loc="left", fontsize=11)
_fig.tight_layout()
_fig
```

Fig. The seven lowest levels of a particle in a rectangular box. Each bar is one state and $g$ counts the states on a level. A cube has levels with $g = 1, 3, 3, 3, 1, 6, 3$; changing one side breaks the symmetry and splits them.

### Note on Computing Average Properties from a Wave Function

Because of the probabilistic interpretation of the wave function, average properties can be computed from the wave function.  The general formula is

$$
\langle A \rangle = \int \psi^*(x)\hat{A}\psi(x)dx
$$

where $\hat{A}$ is any operator. This could be momentum, kinetic energy, and so on. Below are a few problems illustrating how to do such calculations.

To calculate the average position (or **expectation value** of position) for a particle in a 1D box, follow the steps shown in the example below.

:::{note} **Example: Calculate average (expectation) of position, $\langle x\rangle$**
:class: dropdown

**1. Wavefunction of the Particle in a 1D Box**

The wavefunction for a particle in a 1D box of length $L$ with infinite potential walls at $x = 0$ and $x = L$ is given by:

$$
\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)
$$

where:
- $n$ is the quantum number (1, 2, 3, ...),
- $L$ is the length of the box,
- $\psi_n(x)$ is the wavefunction.

**2. Expectation Value of Position $\langle x \rangle$**

The expectation value of the position $x$ for a particle is given by:

$$
\langle x \rangle = \int_0^L x |\psi_n(x)|^2 \, dx
$$

This integral gives the average position of the particle based on the probability density $|\psi_n(x)|^2$. For the wavefunction $\psi_n(x)$, the probability density is:

$$
|\psi_n(x)|^2 = \left( \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right) \right)^2 = \frac{2}{L} \sin^2\left(\frac{n\pi x}{L}\right)
$$

**3. Set Up the Integral**

Substitute $|\psi_n(x)|^2$ into the expression for $\langle x \rangle$:

$$
\langle x \rangle = \int_0^L x \frac{2}{L} \sin^2\left(\frac{n\pi x}{L}\right) \, dx
$$

This is the integral you need to solve to find the average position.

**4. Solve the Integral**

The integral can be simplified using known trigonometric identities. First, use the identity:

$$
\sin^2 \theta = \frac{1}{2} \left(1 - \cos(2\theta)\right)
$$

So, the integral becomes:

$$
\langle x \rangle = \frac{2}{L} \int_0^L x \left( \frac{1}{2} \left( 1 - \cos\left( \frac{2n\pi x}{L} \right) \right) \right) dx
$$

Simplifying:

$$
\langle x \rangle = \frac{1}{L} \int_0^L x \left( 1 - \cos\left( \frac{2n\pi x}{L} \right) \right) dx
$$

Now split this into two integrals:

$$
\langle x \rangle = \frac{1}{L} \left( \int_0^L x \, dx - \int_0^L x \cos\left( \frac{2n\pi x}{L} \right) dx \right)
$$

**5. Evaluate the Integrals**

- The first integral is straightforward:

$$
\int_0^L x \, dx = \frac{L^2}{2}
$$

- The second integral can be solved using integration by parts or by referring to standard integral tables. It turns out that this integral evaluates to 0 for any integer $n$. Thus:

$$
\int_0^L x \cos\left( \frac{2n\pi x}{L} \right) dx = 0
$$

**6. Final Result**

Thus, the expectation value of position simplifies to:

$$
\langle x \rangle = \frac{1}{L} \times \frac{L^2}{2} = \frac{L}{2}
$$

**7. Interpretation**

For any quantum state $n$, the average position $\langle x \rangle$ of a particle in a 1D box is always:

$$
\langle x \rangle = \frac{L}{2}
$$

This result makes sense intuitively because, due to the symmetry of the problem, the particle is equally likely to be found on either side of the box, so its average position is right in the middle of the box at $x = \frac{L}{2}$.

**Summary**

To find the average position of a particle in a 1D box for a general wavefunction:
- Use the wavefunction $\psi_n(x)$,
- Set up the expectation value integral $\langle x \rangle = \int_0^L x\,|\psi_n(x)|^2 \, dx$,
- Solve the integral, which results in $\langle x \rangle = \frac{L}{2}$ for all $n$.

Thus, the particle's average position is always at the midpoint of the box, independent of the quantum number $n$.
:::


### Applications: electronic transitions in conjugated molecules

One of the most useful applications of the particle in a box is estimating the color of light absorbed by **π-conjugated molecules**. In molecules with alternating single and double bonds, the π-electrons are **delocalized** over the conjugated region and behave, to a first approximation, like particles confined to a box whose length is the length of the conjugated chain.

:::{figure} images/pib1d-1.jpeg
:width: 70%

A linear conjugated system (a polyene) modeled as a 1D particle in a box: the delocalized π-electrons are confined to the length of the conjugated chain.
:::

- **1D box** models linear conjugated systems such as butadiene and longer polyenes. The box length is the length of the conjugated chain, and the level spacing sets the wavelength of light absorbed.
- **2D box** models π-electrons delocalized over a two-dimensional region, such as aromatic rings or graphene fragments.

:::{figure} images/pib-applic2.jpeg
:width: 70%

Aromatic and extended π-systems modeled as a 2D particle in a box.
:::

#### Worked example: butadiene

Consider butadiene (C₄H₆), whose four π-electrons are delocalized over the conjugated chain. We estimate the wavelength that excites one π-electron across the gap.

**Step 1: length of the box.** Butadiene, CH₂=CH-CH=CH₂, has two C=C bonds and one C-C bond between its end carbons (C=C ≈ 1.35 Å, C-C ≈ 1.54 Å):

$$
L = 1.35\,\text{Å} + 1.54\,\text{Å} + 1.35\,\text{Å} = 4.24\,\text{Å}.
$$

**Step 2: fill the levels.** Each level holds two electrons (Pauli), so the four π-electrons fill $n=1$ and $n=2$. The highest occupied level is $n=2$ and the lowest empty one is $n=3$, so the absorption is the $n=2 \to n=3$ transition.

**Step 3: transition energy and wavelength.** With $E_n = \dfrac{n^2 h^2}{8mL^2}$, the absorbed photon satisfies

$$
\Delta E = E_3 - E_2 = \frac{(3^2 - 2^2)h^2}{8mL^2} = \frac{hc}{\lambda}.
$$

```{code-cell} python
:tags: [hide-input]
import numpy as np

h = 6.626e-34    # Planck constant (J s)
m = 9.109e-31    # electron mass (kg)
c = 3.0e8        # speed of light (m/s)
# box ending at the end carbons, then one carbon radius (0.77 A) past each end
for label, L in [("L = 4.24 A", 4.24e-10), ("L = 5.78 A", 5.78e-10)]:
    E = lambda n: n**2 * h**2 / (8 * m * L**2)
    dE = E(3) - E(2)             # HOMO (n=2) -> LUMO (n=3)
    lam = h * c / dE
    print(f"{label}:  Delta E (2 -> 3) = {dE:.3e} J,  absorption wavelength = {lam * 1e9:.0f} nm")
```

With the box ending at the end carbons, the estimate (about 119 nm) lands deep in the ultraviolet, well short of the measured 217 nm. The π-electrons do not stop at the end carbons, though: extending the box by one carbon radius (0.77 Å) past each end gives $L = 5.78$ Å and about 220 nm, close to experiment. The simple model captures the key trend: **longer conjugation means a longer box, smaller level spacing, and absorption shifted toward the red**, which is why extended π-systems like carotenes are colored.

### Problems

#### Problem 1: Compute probability of finding particle somewhere

Compute the probability of observing the particle in a box in the domain $\frac{a}{3} \leq x \leq \frac{2a}{3}$.

:::{admonition} **Solution**
:class: dropdown solution

Since the square of the wave function is a probability density, we can determine the probability of observing the particle in a particular domain using the relationship

$$\begin{equation}
\text{Prob}(x_1 \leq x \leq x_2) = \int_{x_1}^{x_2}P(x)dx = \int_{x_1}^{x_2} \psi^*(x)\psi(x)dx
\end{equation}$$

We simply use the above equation together with the normalized particle-in-a-box wave function:

$$\begin{align}
\text{Prob}(\frac{a}{3} \leq x \leq \frac{2a}{3}) = \frac{2}{a}\int_{\frac{a}{3}}^{\frac{2a}{3}} \sin^2\frac{n\pi x}{a}dx
\end{align}$$

We will use the definite integral of $\sin^2ax$ from a table:

$$\begin{equation}
\int\sin^2axdx = \frac{x}{2} - \frac{\sin2ax}{4a}
\end{equation}$$

Perform a $u$-substitution on the integral above to put it into the table form:

$$\begin{align}
\text{Prob}(\frac{a}{3} \leq x \leq \frac{2a}{3}) &= \frac{2}{a}\left[ \frac{x}{2} - \frac{\sin\frac{2n\pi x}{a}}{\frac{4n\pi}{a}}\right]_{\frac{a}{3}}^{\frac{2a}{3}} \\
&= \frac{2}{a}\left[ \frac{x}{2} - \frac{a\sin\frac{2n\pi x}{a}}{4n\pi}\right]_{\frac{a}{3}}^{\frac{2a}{3}} \\
&= \frac{2}{a}\left[ \frac{a}{3} - \frac{a\sin\frac{4n\pi}{3}}{4n\pi} - \frac{a}{6} + \frac{a\sin\frac{2n\pi }{3}}{4n\pi}\right] \\
&= 2\left[ \frac{1}{6}  + \frac{\sin\frac{2n\pi }{3} - \sin\frac{4n\pi}{3}}{4n\pi}\right]
\end{align}$$
:::

#### Problem 2: Compute an expectation of $x^2$

Compute the average of $x^2$ for a particle in a box.

:::{admonition} **Solution**
:class: dropdown solution

To compute the average value of $x^2$, we start by writing the integral expression:

$$\begin{equation}
\langle x^2 \rangle = \int \psi^*(x) x^2 \psi(x)dx
\end{equation}$$

For the particle in a box, we can limit the domain, and thus the bounds of integration, to $0\leq x \leq a$. We can also set $\psi_n(x) = \sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}$.

Thus, for a particle in a 1D box of size $a$, we get

$$\begin{align}
\langle x^2 \rangle &= \int_0^a \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) x^2 \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)dx \\
&= \frac{2}{a} \int_0^a x^2 \sin^2\frac{n\pi x}{a}dx
\end{align}$$

From an integral table we find that

$$\begin{equation}
\int x^2\sin^2\alpha xdx = \frac{x^3}{6} - \left(\frac{x^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha x - \frac{x\cos 2\alpha x}{4\alpha^2} + C
\end{equation}$$

We use this equation with $\alpha = \frac{n\pi}{a}$ and get:

$$\begin{align}
\langle x^2 \rangle &= \int_0^a \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) x^2 \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)dx \\
&= \frac{2}{a} \int_0^a x^2 \sin^2\frac{n\pi x}{a}dx \\
&= \frac{2}{a}\left[ \frac{x^3}{6} - \left(\frac{x^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha x - \frac{x\cos 2\alpha x}{4\alpha^2}\right]_0^a \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \left(\frac{a^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha a - \frac{a\cos 2\alpha a}{4\alpha^2} \right] \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \left(\frac{a^2}{4\frac{n\pi}{a}} - \frac{1}{8\left(\frac{n\pi}{a}\right)^3}\right)\sin2\frac{n\pi}{a} a - \frac{a\cos 2\frac{n\pi}{a} a}{4\left(\frac{n\pi}{a}\right)^2} \right] \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \frac{a^3}{\left(2n\pi\right)^2} \right] \\
&=  \frac{a^2}{3} - \frac{a^2}{2\left(n\pi\right)^2} 
\end{align}$$

This result, combined with the result for $\langle x \rangle$, can be used to determine $\sigma_x$, the standard deviation of the particle's position:

$$\begin{equation}
\sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} = \frac{a}{2\pi n}\sqrt{\frac{\pi^2n^2}{3} -2}
\end{equation}$$
:::

#### Problem 3: Compute expectation of energy

Compute the average energy of a particle in a box.

:::{admonition} **Solution**
:class: dropdown solution

The average energy of the particle in a box is a special case of computing an average quantity. We start by writing out the standard definition of an average computed from a wavefunction:

$$\begin{equation}
\langle E \rangle = \int_0^a \psi_n^*(x)\hat{E}\psi_n(x)dx
\end{equation}$$

where $\hat{E}$ is the total energy operator. We know the total energy operator by another symbol, namely $\hat{E} = \hat{H}$. We plug this into the above equation to get:

$$\begin{equation}
\langle E \rangle = \int_0^a \psi_n^*(x)\hat{H}\psi_n(x)dx.
\end{equation}$$

We now recognize that the particle-in-a-box wavefunctions we are discussing were derived from the Schrödinger equation:

$$\begin{equation}
\hat{H}\psi_n(x)  = E_n\psi_n(x)
\end{equation}$$

where $E_n$ is a scalar. Thus, for the average energy we get:

$$\begin{align}
\langle E \rangle &= \int_0^a \psi_n^*(x)\hat{H}\psi_n(x)dx \\
&=\int_0^a \psi_n^*(x)E_n\psi_n(x)dx \\
&=E_n\int_0^a \psi_n^*(x)\psi_n(x)dx \\
&= E_n
\end{align}$$

The last equality holds because the wave functions are normalized.
:::

#### Problem 4: Compute expectation of momentum

Compute the average momentum for a particle in a box.

:::{admonition} **Solution**
:class: dropdown solution

To compute the average momentum of a particle in a 1D box, we start in the usual way:

$$\begin{equation}
\langle p \rangle = \int_0^a \psi_n^*(x)\hat{p}\psi_n(x)dx
\end{equation}$$

Recall that the momentum operator in one dimension is given by

$$\begin{equation}
\hat{p}_x = -i\hbar\frac{d}{dx}
\end{equation}$$

We now substitute this into the above equation and solve:

$$\begin{align}
\langle p \rangle &= \int_0^a \psi_n^*(x)\left(-i\hbar\frac{d}{dx}\right)\psi_n(x)dx \\
&= -\frac{2i\hbar}{a}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\frac{d}{dx}\left(\sin\left(\frac{n\pi x}{a}\right)\right)dx \\
&= -\frac{2i\hbar}{a}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\frac{n\pi}{a}\cos\left(\frac{n\pi x}{a}\right)dx \\
&= -\frac{2in\pi\hbar}{a^2}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\cos\left(\frac{n\pi x}{a}\right)dx \\
&= 0
\end{align}$$

where the last equality can be found in an integral table.

So the average momentum of a particle in a box is zero. This is because it is equally probable for the particle to be moving forward and backward.
:::

#### Problem 5

 Consider an electron in superfluid helium ($^4$He) where it forms a solvation cavity with a radius of $18 \text{Å}$. Calculate the zero-point energy and the energy difference between the ground and first excited states by approximating the electron by a particle in a 3-dimensional box.


:::{admonition} **Solution**
:class: dropdown solution

The zero-point energy can be obtained from the lowest-state energy ($n = 1$) with $a = b = c = 36 \text{Å}$. The first excited state is triply degenerate ($E_{112}$, $E_{121}$, and $E_{211}$).

$$E_{111} = \frac{h^2}{8m_e}\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2}\right)$$
$$= \frac{(6.626076\times 10^{-34}\textnormal{ Js})^2}{8(9.109390\times 10^{-31}\textnormal{ kg})}\left(\frac{1}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1}{(36\times 10^{-10}\textnormal{ m})^2}\right)$$
$$= 1.39\times10^{-20}\textnormal{ J} = 87.0\textnormal{ meV}$$


$$E_{211} = E_{121} = E_{112} = \frac{(6.626076\times 10^{-34}\textnormal{ Js})^2}{8(9.109390\times 10^{-31}\textnormal{ kg})}$$
$$\times\left(\frac{2^2}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1^2}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1^2}{(36\times 10^{-10}\textnormal{ m})^2}\right)$$
$$= 2.79\times 10^{-20}\textnormal{ J} = 174\textnormal{ meV} \Rightarrow \Delta E = 87\textnormal{ meV}$$
(Experimental value: 105 meV; Phys. Rev. B 41, 6366 (1990))

:::

#### Problem 6: Energy Levels in a 3D Box

A particle is confined in a 3D box with side lengths $L_x = L_y = L_z = L$. The energy levels for a particle in this box are given by the formula:

$$E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)$$

where $n_x$, $n_y$, $n_z$ are the quantum numbers associated with the particle's motion in the $x$-, $y$-, and $z$-directions.

Calculate the energy levels for the quantum states with $n_x = 1$, $n_y = 1$, $n_z = 2$ and $n_x = 2$, $n_y = 2$, $n_z = 1$. Are these energy levels degenerate?

:::{admonition} **Solution**
:class: dropdown solution

The energy for the state $(n_x, n_y, n_z) = (1, 1, 2)$ is:

$$E_{1,1,2} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 1^2 + 1^2 + 2^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} (1 + 1 + 4) = \frac{\hbar^2 \pi^2}{2mL^2} \times 6$$

The energy for the state $(n_x, n_y, n_z) = (2, 2, 1)$ is:

$$E_{2,2,1} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 2^2 + 2^2 + 1^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} (4 + 4 + 1) = \frac{\hbar^2 \pi^2}{2mL^2} \times 9$$

Since $E_{1,1,2} \neq E_{2,2,1}$, these energy levels are **not degenerate**.

:::

#### Problem 7: Degeneracy of Energy Levels

Consider a particle confined in a cubic box with side lengths $L_x = L_y = L_z = L$. The energy levels are given by the same formula as in Problem 6.

- **Part 1:** Find the degeneracy of the energy level corresponding to the quantum number sum $n_x^2 + n_y^2 + n_z^2 = 14$.
- **Part 2:** Write down all the quantum number triplets $(n_x, n_y, n_z)$ that correspond to this energy level.

:::{admonition} **Solution**
:class: dropdown solution

**Part 1:**
We want to find the quantum numbers that satisfy:

$n_x^2 + n_y^2 + n_z^2 = 14$

We can check different combinations of $n_x$, $n_y$, and $n_z$:

- For $n_x = 3$, $n_y = 2$, and $n_z = 1$:

$$3^2 + 2^2 + 1^2 = 9 + 4 + 1 = 14$$

- Other permutations of these quantum numbers will give the same energy:
  
  - $(3, 2, 1)$
  - $(3, 1, 2)$
  - $(2, 3, 1)$
  - $(2, 1, 3)$
  - $(1, 3, 2)$
  - $(1, 2, 3)$

**Part 2:**
The energy level corresponding to $n_x^2 + n_y^2 + n_z^2 = 14$ has **6 degenerate states**, since the quantum number triplets are $(3, 2, 1)$, $(3, 1, 2)$, $(2, 3, 1)$, $(2, 1, 3)$, $(1, 3, 2)$, and $(1, 2, 3)$.

:::

#### Problem 8: Degeneracy of the Ground State

- **Part 1:** What is the degeneracy of the ground state (the lowest energy state) for a particle in a cubic box?
- **Part 2:** Explain why the ground state does not have degeneracy.

:::{admonition} **Solution**
:class: dropdown solution

**Part 1:**
The ground state corresponds to the quantum numbers $n_x = n_y = n_z = 1$. The energy for this state is:

$$E_{1,1,1} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 1^2 + 1^2 + 1^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} \times 3$$

There is only **one** combination of quantum numbers that gives this energy, so the degeneracy of the ground state is **1**.

**Part 2:**
The ground state is non-degenerate because there is only one way to assign the quantum numbers $n_x = n_y = n_z = 1$. Degeneracy arises when multiple different sets of quantum numbers give the same energy, which is not the case for the ground state.

:::

#### Problem 9: Higher Energy Degeneracy

Consider a particle in a cubic box. The energy levels are quantized as:

$$E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)$$

- **Part 1:** Find the quantum numbers that give the same energy for the quantum number sum $n_x^2 + n_y^2 + n_z^2 = 9$. How many degenerate states correspond to this energy?
- **Part 2:** What is the degeneracy of this energy level?

:::{admonition} **Solution**
:class: dropdown solution

**Part 1:**
We want to solve:

$n_x^2 + n_y^2 + n_z^2 = 9$

Possible combinations of $n_x$, $n_y$, and $n_z$:

- $n_x = 2$, $n_y = 2$, $n_z = 1$ gives $2^2 + 2^2 + 1^2 = 4 + 4 + 1 = 9$.
- Permutations of $(2, 2, 1)$ are:
  - $(2, 2, 1)$
  - $(2, 1, 2)$
  - $(1, 2, 2)$
- $(3, 0, 0)$ also gives 9, but it is not allowed: each quantum number is at least 1, since $n = 0$ makes $\psi = 0$.

**Part 2:**
The degeneracy for the energy level corresponding to $n_x^2 + n_y^2 + n_z^2 = 9$ is **3**: the three permutations of $(2,2,1)$.

:::

#### Problem 10: Absorption of a conjugated diene

A conjugated diene has a conjugation length of 5 Å. Using the 1D particle in a box, calculate the wavelength absorbed when a π-electron is excited from $n = 1$ to $n = 2$. Use $m = 9.109 \times 10^{-31}\,\text{kg}$ and $h = 6.626 \times 10^{-34}\,\text{J s}$.

:::{admonition} **Solution**
:class: dropdown solution

The gap between $n = 1$ and $n = 2$ is

$$
\Delta E = \frac{(2^2 - 1^2)h^2}{8mL^2} = \frac{3h^2}{8mL^2},
$$

with $L = 5 \times 10^{-10}\,\text{m}$. Compute $\Delta E$, then use $\Delta E = \dfrac{hc}{\lambda}$ to find $\lambda$.
:::

#### Problem 11: Total conjugation length of a polyene

A polyene has 6 alternating bonds with $C=C \approx 1.35$ Å and $C\text{-}C \approx 1.45$ Å. Find the total conjugation length and the wavelength needed to excite a π-electron from $n = 1$ to $n = 2$.

:::{admonition} **Solution**
:class: dropdown solution

$$
L = 4 \times 1.35\,\text{Å} + 3 \times 1.45\,\text{Å} = 10.55\,\text{Å} = 10.55 \times 10^{-10}\,\text{m}.
$$

Then $\Delta E = \dfrac{3h^2}{8mL^2}$ and $\lambda = \dfrac{hc}{\Delta E}$.
:::

#### Problem 12: A higher transition

A linear conjugated molecule has 8 alternating C-C bonds (1.40 Å single, 1.35 Å double). Calculate the wavelength absorbed for the $n = 1 \to n = 3$ transition.

:::{admonition} **Solution**
:class: dropdown solution

For 8 bonds, take 4 double and 4 single:

$$
L = 4 \times 1.35\,\text{Å} + 4 \times 1.40\,\text{Å} = 11.0\,\text{Å}.
$$

The energy gap is

$$
\Delta E = E_3 - E_1 = \frac{(3^2 - 1^2)h^2}{8mL^2} = \frac{8h^2}{8mL^2} = \frac{h^2}{mL^2},
$$

and $\lambda = \dfrac{hc}{\Delta E}$.
:::

#### Problem 13: Triene transition

A conjugated triene has a conjugation length of 7.5 Å. Find the wavelength absorbed for the $n = 1 \to n = 3$ transition.

:::{admonition} **Solution**
:class: dropdown solution

With $L = 7.5 \times 10^{-10}\,\text{m}$,

$$
\Delta E = E_3 - E_1 = \frac{8h^2}{8mL^2} = \frac{h^2}{mL^2},
$$

then $\lambda = \dfrac{hc}{\Delta E}$.
:::

#### Problem 14: A transition between excited states

A polyene of 10 carbons has $C=C \approx 1.34$ Å and $C\text{-}C \approx 1.54$ Å. Find the total conjugation length and the wavelength for the $n = 2 \to n = 3$ transition.

:::{admonition} **Solution**
:class: dropdown solution

$$
L = 5 \times 1.34\,\text{Å} + 4 \times 1.54\,\text{Å} = 12.86\,\text{Å}.
$$

The gap is

$$
\Delta E = E_3 - E_2 = \frac{(3^2 - 2^2)h^2}{8mL^2} = \frac{5h^2}{8mL^2},
$$

then $\lambda = \dfrac{hc}{\Delta E}$.
:::

#### Problem 15: A 2D box for a graphene fragment

Model the π-electrons of a graphene-like fragment as a 2D particle in a box with $L_x = 2\,\text{nm}$ and $L_y = 1\,\text{nm}$. Calculate the energy of the state $n_x = 1$, $n_y = 2$.

:::{admonition} **Solution**
:class: dropdown solution

The 2D energy is

$$
E_{n_x, n_y} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2}\right).
$$

With $L_x = 2 \times 10^{-9}\,\text{m}$ and $L_y = 1 \times 10^{-9}\,\text{m}$,

$$
\frac{1^2}{L_x^2} + \frac{2^2}{L_y^2} = 2.5 \times 10^{17} + 4.0 \times 10^{18} = 4.25 \times 10^{18}\,\text{m}^{-2},
$$

and $\dfrac{h^2}{8m} \approx 6.02 \times 10^{-38}\,\text{J m}^2$, giving

$$
E_{1,2} \approx 2.56 \times 10^{-19}\,\text{J} \approx 1.60\,\text{eV}.
$$
:::
