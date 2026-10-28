# Python Calculator

:::{note} **Your quantum chemistry workbench**

Every panel on this page runs **live in your browser**. Cells with a play button are fully editable: change the numbers, press play (or Ctrl-Enter), and the result updates. Come back here whenever you need to crunch a quick number, make a plot, take a derivative, or look at an orbital, without leaving the website.

Already imported for you on this page: `numpy as np`, `matplotlib.pyplot as plt`, `sympy as sp`, and `scipy.constants as const`. Nothing here needs to be saved or submitted: it is a scratchpad, not an assignment.
:::

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "scipy",
      "matplotlib",
      "sympy",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
import scipy.constants as const
import sympy as sp
from scipy.special import sph_harm_y, genlaguerre, factorial
from matplotlib.colors import to_hex
```

```{marimo} python
:hide-code: true

def wavelength_to_rgb(nm):
    if 380 <= nm < 440: rgb = (-(nm - 440) / 60, 0.0, 1.0)
    elif 440 <= nm < 490: rgb = (0.0, (nm - 440) / 50, 1.0)
    elif 490 <= nm < 510: rgb = (0.0, 1.0, -(nm - 510) / 20)
    elif 510 <= nm < 580: rgb = ((nm - 510) / 70, 1.0, 0.0)
    elif 580 <= nm < 645: rgb = (1.0, -(nm - 645) / 65, 0.0)
    elif 645 <= nm <= 750: rgb = (1.0, 0.0, 0.0)
    else: rgb = (0.55, 0.55, 0.55)
    return rgb
```

### 1. Units, Constants and quick calculations

```{marimo} python
:hide-code: true

to_joules = {
    "J": 1.0,
    "eV": 1.602176634e-19,
    "cm^-1": 1.986445857e-23,
    "kJ/mol": 1000 / 6.02214076e23,
    "hartree": 4.3597447222e-18,
    "Hz": 6.62607015e-34,
}
amount_c = mo.ui.number(value=1.0, step=0.1, label="value")
unit_c = mo.ui.dropdown(options=list(to_joules), value="eV", label="from unit")
mo.hstack([amount_c, unit_c], justify="start", gap=1.5)
```

```{marimo} python
:hide-code: true

val_c = amount_c.value if amount_c.value is not None else 0.0
joules_c = val_c * to_joules[unit_c.value]
rows_c = "\n".join(f"| {u} | {joules_c / f:.6g} |" for u, f in to_joules.items())
mo.md(f"**{val_c:g} {unit_c.value}** equals:\n\n| unit | value |\n|:--|--:|\n{rows_c}")
```


`scipy.constants` knows every physical constant ([full list](https://docs.scipy.org/doc/scipy/reference/constants.html)):

```{marimo} python
:hide-code: true

mo.md(f"""
| constant | symbol | value |
|---|---|---|
| Planck | $h$ | {const.h:.4e} J s |
| speed of light | $c$ | {const.c:.4e} m/s |
| electron charge | $e$ | {const.e:.4e} C |
| electron mass | $m_e$ | {const.m_e:.4e} kg |
| Boltzmann | $k_B$ | {const.k:.4e} J/K |
| Avogadro | $N_A$ | {const.N_A:.4e} 1/mol |
| Bohr radius | $a_0$ | {const.value("Bohr radius"):.4e} m |
| Rydberg | $R_\\infty$ | {const.Rydberg:.4e} 1/m |
""")
```

A scratchpad, seeded with a photon-energy calculation. Edit it and press play; the value of the last line is displayed:

```{marimo} python
:editor: true

lam = 532e-9                       # a green laser pointer
E_photon = const.h * const.c / lam
E_photon / const.e                 # in electron volts







```


### 2. Plotting panel

A ready-to-edit plotting template. Swap in any function of `x`; the slider is yours to repurpose:

```{marimo} python
:hide-code: true

k = mo.ui.slider(1, 12, step=1, value=3, show_value=True, label="parameter k")
k
```

```{marimo} python
:editor: true

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(k.value * x) * np.exp(-x / 4)   # edit me

fig, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(x, y, lw=2)
ax.set_xlabel("x")
ax.grid(True, ls="--", alpha=0.4)
fig
```


### 3. Numerical integral

Define any function and limits in the pad; the plot shades area above the axis in green and below in red, and the value comes from `np.trapezoid`, the same tool your homework uses:

```{marimo} python
:editor: true

def f(x):
    return np.sin(3 * x) * np.exp(-x / 4)   # edit me

a, b = 0.0, 10.0                             # integration limits
```

```{marimo} python
:hide-code: true

xg2 = np.linspace(a, b, 2000)
yg2 = f(xg2)
val2 = np.trapezoid(yg2, xg2)
pos2 = np.trapezoid(np.clip(yg2, 0, None), xg2)
neg2 = np.trapezoid(np.clip(yg2, None, 0), xg2)

fig2, ax2 = plt.subplots(figsize=(7, 3.8))
ax2.plot(xg2, yg2, lw=2, color="0.25")
ax2.fill_between(xg2, yg2, 0, where=yg2 >= 0, color="seagreen", alpha=0.45)
ax2.fill_between(xg2, yg2, 0, where=yg2 < 0, color="crimson", alpha=0.45)
ax2.axhline(0, color="0.6", lw=0.8)
ax2.set_xlabel("x")
ax2.set_title(
    f"integral = {val2:.4f}   (positive area {pos2:.4f}, negative area {neg2:.4f})",
    fontsize=11,
)
fig2
```

The green and red areas fight each other: an integral is a **signed** sum. For probability densities like $|\psi|^2$ the red never appears, which is exactly why they can be interpreted as probabilities.


### 4. Symbolic window

Derivatives, integrals, and equation solving with `sympy`; results render as typeset math. Each pad is editable:

```{marimo} python
:editor: true

u = sp.symbols("u")
sp.diff(sp.exp(-u**2) * sp.sin(u), u)          # derivative pad
```

```{marimo} python
:editor: true

w = sp.symbols("w", positive=True)
sp.integrate(w**2 * sp.exp(-w), (w, 0, sp.oo))  # integral pad
```

```{marimo} python
:editor: true

q = sp.symbols("q")
sp.solve(q**3 - 6*q**2 + 11*q - 6, q)           # solver pad
```

### 5. Orbital visualizer

Pick quantum numbers (the menus only ever offer valid combinations). The first plot is a **2D cross-section** of the orbital in the xz-plane, with blue and red marking the wavefunction's positive and negative lobes. Below it, the **radial view** shows the radial function $R_{nl}(r)$ and the radial distribution $P(r) = r^2 R^2$, and reports the most probable radius, the mean radius $\langle r\rangle$, and the node count.

```{marimo} python
:hide-code: true

def radial_c(r, n=1, l=0):
    pre = np.sqrt(((2 / n) ** 3 * factorial(n - l - 1)) / (2 * n * factorial(n + l)))
    p = 2 * r / n
    return pre * np.exp(-p / 2) * p**l * genlaguerre(n - l - 1, 2 * l + 1)(p)
```

```{marimo} python
:hide-code: true

n_v = mo.ui.slider(1, 5, step=1, value=2, show_value=True, label="n")
n_v
```

```{marimo} python
:hide-code: true

l_v = mo.ui.dropdown(options={str(v): v for v in range(n_v.value)}, value=str(n_v.value - 1), label="l")
l_v
```

```{marimo} python
:hide-code: true

m_v = mo.ui.dropdown(options={str(v): v for v in range(-l_v.value, l_v.value + 1)}, value="0", label="m")
m_v
```

```{marimo} python
:hide-code: true

# 2D cross-section of the orbital in the xz-plane (y = 0)
n6, l6, m6 = n_v.value, l_v.value, m_v.value
ext6 = 2.2 * n6**2 + 6
g6 = np.linspace(-ext6, ext6, 320)
Xg6, Zg6 = np.meshgrid(g6, g6)
Rg6 = np.sqrt(Xg6**2 + Zg6**2)
Thg6 = np.arccos(np.clip(Zg6 / (Rg6 + 1e-12), -1.0, 1.0))
Phg6 = np.arctan2(np.zeros_like(Xg6), Xg6)   # 0 for x>0, pi for x<0
psi6 = (radial_c(Rg6, n6, l6) * sph_harm_y(l6, m6, Thg6, Phg6)).real
amp6 = np.abs(psi6).max() + 1e-12

fig6, ax6 = plt.subplots(figsize=(5.2, 4.8))
mesh6 = ax6.pcolormesh(Xg6, Zg6, psi6, cmap="RdBu_r", vmin=-amp6, vmax=amp6, shading="auto")
ax6.set_aspect("equal")
ax6.set_xlabel("x (Bohr)")
ax6.set_ylabel("z (Bohr)")
ax6.set_title(f"orbital ({n6}, {l6}, {m6}): xz cross-section")
fig6.colorbar(mesh6, ax=ax6, shrink=0.85, label="wavefunction (sign)")
fig6
```

```{marimo} python
:hide-code: true

# radial function R(r) and radial distribution P(r) = r^2 R^2
r_ax6 = np.linspace(1e-6, 2.5 * n_v.value**2 + 12, 1400)
Rrad6 = radial_c(r_ax6, n_v.value, l_v.value)
Prad6 = r_ax6**2 * Rrad6**2
rpeak6 = r_ax6[np.argmax(Prad6)]
rmean6 = np.trapezoid(r_ax6 * Prad6, r_ax6) / np.trapezoid(Prad6, r_ax6)
nodes6 = n_v.value - l_v.value - 1

figR6, (axR6a, axR6b) = plt.subplots(2, 1, figsize=(6, 5), sharex=True)
axR6a.plot(r_ax6, Rrad6, color="steelblue", lw=2)
axR6a.axhline(0, color="0.7", lw=0.7)
axR6a.set_ylabel(r"$R_{nl}(r)$")
axR6a.set_title(f"radial part of ({n_v.value}, {l_v.value}):  {nodes6} radial node(s)")
axR6b.plot(r_ax6, Prad6, color="crimson", lw=2)
axR6b.axvline(rpeak6, color="0.35", ls="--", lw=1.2, label=f"most probable r = {rpeak6:.2f} a0")
axR6b.axvline(rmean6, color="seagreen", ls=":", lw=1.6, label=f"mean r = {rmean6:.2f} a0")
axR6b.set_ylabel(r"$P(r) = r^2 R^2$")
axR6b.set_xlabel("r (Bohr)")
axR6b.legend(fontsize=8, frameon=False)
figR6.tight_layout()
figR6
```

```{marimo} python
:hide-code: true

mo.md(
    f"**Orbital ({n_v.value}, {l_v.value}, {m_v.value})** &nbsp;|&nbsp; "
    f"most probable radius $r_{{\\max}} = {rpeak6:.2f}\\,a_0$ &nbsp;|&nbsp; "
    f"mean radius $\\langle r\\rangle = {rmean6:.2f}\\,a_0$ "
    f"(exact $\\tfrac{{1}}{{2}}[3n^2 - l(l+1)] = {(3*n_v.value**2 - l_v.value*(l_v.value+1))/2:.2f}$) &nbsp;|&nbsp; "
    f"radial nodes $= n-l-1 = {nodes6}$, angular nodes $= l = {l_v.value}$"
)
```



### 6. One-dimensional Schrödinger solver

Pick a potential and get its bound states instantly: energies as horizontal lines, wavefunctions drawn at their own energy (units: $\hbar = m = 1$, hard walls at $x = \pm 4$). To see how the solver works inside, open the [numerical Schrödinger lab](07-demo-numerical-schrodinger.md).

```{marimo} python
:hide-code: true

pot1 = mo.ui.dropdown(
    options={
        "infinite box, V = 0": "box",
        "linear well, V = a|x|": "linear",
        "harmonic, V = a x^2 / 2": "harmonic",
        "double well, V = a((x/2)^2 - 1)^2": "double",
        "square barrier, height a, width 1": "barrier",
    },
    value="harmonic, V = a x^2 / 2", label="potential",
)
amp1 = mo.ui.slider(0.5, 30.0, step=0.5, value=4.0, show_value=True, label="strength a")
nst1 = mo.ui.slider(2, 8, step=1, value=5, show_value=True, label="states to show")
mo.hstack([pot1, amp1, nst1], justify="start", gap=1.5)
```

```{marimo} python
:hide-code: true

from scipy.linalg import eigh_tridiagonal

x1 = np.linspace(-4, 4, 802)[1:-1]
dx1 = x1[1] - x1[0]
if pot1.value == "box":
    v1 = np.zeros_like(x1)
elif pot1.value == "linear":
    v1 = amp1.value * np.abs(x1)
elif pot1.value == "harmonic":
    v1 = 0.5 * amp1.value * x1**2
elif pot1.value == "barrier":
    v1 = np.where(np.abs(x1) < 0.5, amp1.value, 0.0)
else:
    v1 = amp1.value * ((x1 / 2) ** 2 - 1) ** 2

en1, vec1 = eigh_tridiagonal(
    1.0 / dx1**2 + v1, np.full(len(x1) - 1, -0.5 / dx1**2),
    select="i", select_range=(0, nst1.value - 1),
)
wf1 = vec1 / np.sqrt(dx1)

fig1, ax1 = plt.subplots(figsize=(7, 4.6))
ax1.plot(x1, v1, color="0.35", lw=1.8)
span1 = max(en1.max() - en1.min(), 1.0)
for e1, psi1 in zip(en1, wf1.T):
    ax1.axhline(e1, color="0.85", lw=0.7)
    ax1.plot(x1, e1 + psi1 * span1 * 0.12, lw=1.6)
ax1.set_xlabel("x")
ax1.set_ylabel("energy")
ax1.set_ylim(min(v1.min(), en1.min()) - 0.05 * span1, en1.max() + 0.35 * span1)
ax1.set_title(f"{pot1.value}:  E = " + ", ".join(f"{e:.2f}" for e in en1[:4]) + (" ..." if len(en1) > 4 else ""), fontsize=10)
fig1
```

Try the classics: the box gives the $n^2$ ladder, the harmonic well gives perfectly even spacing (the fingerprint of vibrations), the linear well spaces levels like Airy zeros, and the double well pairs levels into tunneling doublets. The square barrier does the same with sharp walls: it cuts the box into two halves that talk only by tunneling, so raise $a$ and watch each pair of levels squeeze together.



### 7. Tunneling through a square barrier

An electron with energy $E$ comes in from the left toward a barrier of height $V_0$ and width $a$. Classically it bounces back whenever $E < V_0$. Quantum mechanically the wave leaks in, decays as $e^{-\kappa x}$ inside, and whatever amplitude reaches the far side carries on as a transmitted wave. The fraction that gets through is

$$
T = \left[1 + \frac{V_0^2 \sinh^2(\kappa a)}{4E(V_0 - E)}\right]^{-1}, \qquad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}
$$

For a thick barrier ($\kappa a \gg 1$) this becomes $T \approx 16\frac{E}{V_0}\left(1 - \frac{E}{V_0}\right)e^{-2\kappa a}$, exponential in the width. Units here are eV and Å with the electron mass. The derivation is in the [tunneling lecture](../ch03/03-tunneling-and-finite-square-well.md).

```{marimo} python
:hide-code: true

V0_8 = mo.ui.slider(0.5, 10.0, step=0.5, value=4.0, show_value=True, label="barrier height V0 (eV)")
w8 = mo.ui.slider(0.25, 10.0, step=0.25, value=3.0, show_value=True, label="width a (Å)")
E8 = mo.ui.slider(0.05, 15.0, step=0.05, value=2.0, show_value=True, label="energy E (eV)")
log8 = mo.ui.checkbox(value=False, label="log scale for T")
mo.vstack([mo.hstack([V0_8, w8], justify="start", gap=1.5), mo.hstack([E8, log8], justify="start", gap=1.5)])
```

```{marimo} python
:hide-code: true

c8 = const.hbar**2 / (2 * const.m_e) / const.e * 1e20   # hbar^2/2m = 3.81 eV Å^2 for an electron
V8, a8 = V0_8.value, w8.value
en8 = E8.value if abs(E8.value - V8) > 1e-3 else V8 + 1e-3   # step off E = V0, where the basis degenerates

def trans8(E, V, a):
    """exact T(E) for a square barrier; sinh(x)/x and sin(x)/x keep E = V0 finite"""
    d = (V - E) / c8
    qa = np.sqrt(np.abs(d)) * a
    sx = np.where(d > 0, np.sinh(qa) / np.where(qa > 1e-9, qa, 1.0), np.sinc(qa / np.pi))
    sx = np.where(qa > 1e-9, sx, 1.0)
    return 1.0 / (1.0 + V**2 * a**2 * sx**2 / (4 * E * c8))

# scattering state: e^{ikx} + r e^{-ikx} | C e^{q(x-a)} + D e^{-qx} | t e^{ikx}, matched at x = 0 and x = a
k8 = np.sqrt(en8 / c8)
q8 = np.sqrt((V8 - en8) / c8 + 0j)
eq8 = np.exp(-q8 * a8)
M8 = np.array([
    [1, -eq8, -1, 0],
    [-1j * k8, -q8 * eq8, q8, 0],
    [0, 1, eq8, -np.exp(1j * k8 * a8)],
    [0, q8, -q8 * eq8, -1j * k8 * np.exp(1j * k8 * a8)],
])
r8, C8, D8, t8 = np.linalg.solve(M8, np.array([-1, -1j * k8, 0, 0]))
T8, R8 = abs(t8) ** 2, abs(r8) ** 2

side8 = float(np.clip(3 * np.pi / k8, 8.0, 25.0))   # about 1.5 wavelengths on each side
xs8 = np.linspace(-side8, a8 + side8, 1600)
psi8 = np.where(xs8 < 0, np.exp(1j * k8 * xs8) + r8 * np.exp(-1j * k8 * xs8),
       np.where(xs8 <= a8, C8 * np.exp(q8 * (xs8 - a8)) + D8 * np.exp(-q8 * xs8),
                t8 * np.exp(1j * k8 * xs8)))

# left: Re psi drawn at height E over the barrier; right: T(E) with the current E marked
inside8 = (xs8 >= 0) & (xs8 <= a8)
top8 = max(V8, en8)
fig8, (axL8, axR8) = plt.subplots(1, 2, figsize=(9.6, 4.0), gridspec_kw={"width_ratios": [1.3, 1]})
axL8.fill_between(xs8, np.where(inside8, V8, 0.0), color="0.88")
axL8.plot(xs8, np.where(inside8, V8, 0.0), color="0.35", lw=1.8)
axL8.axhline(en8, color="0.6", ls="--", lw=0.9)
axL8.plot(xs8, en8 + 0.22 * top8 * psi8.real / np.abs(psi8.real).max(), color="steelblue", lw=1.6)
axL8.text(xs8[0], en8, " E", va="bottom", fontsize=10, color="0.4")
axL8.text(a8 / 2, V8, "$V_0$", ha="center", va="bottom", fontsize=10, color="0.35")
axL8.set_xlim(xs8[0], xs8[-1])
axL8.set_ylim(min(-0.05 * top8, en8 - 0.3 * top8), max(V8, en8 + 0.3 * top8) * 1.08)
axL8.set_xlabel("x (Å)")
axL8.set_ylabel("energy (eV)")
axL8.set_title(f"electron from the left:  T = {T8:.3g},  R = {R8:.3g}", fontsize=10)

eg8 = np.linspace(0.005, max(2.5 * V8, 1.15 * en8), 600)
tg8 = trans8(eg8, V8, a8)
axR8.plot(eg8, tg8, color="0.2", lw=2, label="quantum")
axR8.plot(eg8, (eg8 > V8).astype(float), color="0.6", ls=":", lw=1.6, label="classical")
axR8.axvline(V8, color="0.75", lw=0.8)
axR8.plot(en8, T8, "o", color="crimson", ms=8, zorder=5)
if log8.value:
    axR8.set_yscale("log")
    axR8.set_ylim(max(tg8.min(), 1e-300) / 3, 3)
else:
    axR8.set_ylim(-0.03, 1.08)
axR8.set_xlabel("E (eV)")
axR8.set_ylabel("transmission T")
axR8.set_title(f"barrier: $V_0$ = {V8:g} eV, a = {a8:g} Å", fontsize=10)
axR8.legend(loc="lower right", fontsize=9, frameon=False)
fig8.suptitle("Fig. Square barrier: the wave decays inside and leaks through (left); transmission versus energy (right)", fontsize=10, y=1.02)
fig8.tight_layout()
fig8
```

```{marimo} python
:hide-code: true

def sci8(v):
    """3 significant figures, as LaTeX powers of ten when small"""
    if v >= 1e-3:
        return f"{v:.3g}"
    m8, p8 = f"{v:.2e}".split("e")
    return f"{m8} \\times 10^{{{int(p8)}}}"

if abs(E8.value - V8) <= 1e-3:
    text8 = (
        f"**At the barrier top.** $E = V_0$, so $\\kappa = 0$: inside the barrier the wave neither decays "
        f"nor oscillates. The formula's limit is $T = \\left[1 + m V_0 a^2/2\\hbar^2\\right]^{{-1}} = {sci8(T8)}$."
    )
elif en8 < V8:
    kap8 = np.sqrt((V8 - en8) / c8)
    est8 = 16 * (en8 / V8) * (1 - en8 / V8) * np.exp(-2 * kap8 * a8)
    text8 = (
        f"**Below the barrier.** $\\kappa = {kap8:.3g}$ Å$^{{-1}}$, so inside the barrier the wave loses "
        f"a factor of $e$ every $1/\\kappa = {1 / kap8:.3g}$ Å, and $\\kappa a = {kap8 * a8:.3g}$.\n\n"
        f"Exact $T = {sci8(T8)}$. Thick-barrier estimate "
        f"$16\\frac{{E}}{{V_0}}\\left(1 - \\frac{{E}}{{V_0}}\\right)e^{{-2\\kappa a}} = {sci8(est8)}$, "
        f"off by {abs(est8 / T8 - 1):.0%}."
    )
else:
    kp8 = np.sqrt((en8 - V8) / c8)
    text8 = (
        f"**Above the barrier.** A classical electron always gets through, yet $R = {R8:.3g}$ of the wave "
        f"reflects. Inside, the wave oscillates with $k' = {kp8:.3g}$ Å$^{{-1}}$ and $k'a/\\pi = {kp8 * a8 / np.pi:.2f}$; "
        f"$T = 1$ exactly when $k'a/\\pi$ is a whole number, so the barrier holds a whole number of half wavelengths."
    )
mo.md(text8)
```

Start below the barrier and widen it in steps of 1 Å: $T$ drops by roughly the same factor each step, and the log scale turns that exponential into a straight line. Then push $E$ above $V_0$: the classical electron always passes, but the quantum one still reflects, and $T$ wiggles up to 1 only at the resonances. The same exponential is why a scanning tunneling microscope current changes about tenfold per ångström of tip height, and why a proton, 1836 times heavier than an electron, has a $\kappa$ about 43 times larger and tunnels only through barriers a fraction of an ångström thick.



### 8. Quadratic equation solver

Every quadratic $ax^2 + bx + c = 0$ is solved by one formula:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

The sign of the **discriminant** $\Delta = b^2 - 4ac$ decides what comes out: two real crossings for $\Delta > 0$, one repeated root for $\Delta = 0$, and for $\Delta < 0$ a pair of complex conjugates that never touch the axis. Drag the coefficients and watch the roots leave the real line.

```{marimo} python
:hide-code: true

a7 = mo.ui.slider(-3.0, 3.0, step=0.25, value=1.0, show_value=True, label="a")
b7 = mo.ui.slider(-6.0, 6.0, step=0.25, value=-2.0, show_value=True, label="b")
c7 = mo.ui.slider(-6.0, 6.0, step=0.25, value=-3.0, show_value=True, label="c")
mo.hstack([a7, b7, c7], justify="start", gap=1.5)
```

```{marimo} python
:hide-code: true

av7, bv7, cv7 = a7.value, b7.value, c7.value
disc7 = bv7**2 - 4 * av7 * cv7
if av7 == 0:
    roots7 = [] if bv7 == 0 else [complex(-cv7 / bv7, 0.0)]
elif disc7 >= 0:
    sq7 = np.sqrt(disc7) / (2 * av7)
    roots7 = [complex(-bv7 / (2 * av7) - sq7, 0.0), complex(-bv7 / (2 * av7) + sq7, 0.0)]
else:
    sq7 = np.sqrt(-disc7) / (2 * abs(av7))
    roots7 = [complex(-bv7 / (2 * av7), -sq7), complex(-bv7 / (2 * av7), sq7)]

def par7(v):
    """format a coefficient, wrapping negatives in parentheses for substitution"""
    return f"({v:g})" if v < 0 else f"{v:g}"

if av7 == 0:
    if bv7 == 0:
        text7 = f"With $a = 0$ and $b = 0$ nothing is left to solve: the equation reads ${cv7:g} = 0$."
    else:
        text7 = (f"With $a = 0$ the parabola flattens into the line $bx + c = 0$, "
                 f"which has the single root $x = -c/b = {roots7[0].real:.4g}$.")
else:
    kind7 = ("two real roots" if disc7 > 0 else
             "one repeated real root" if disc7 == 0 else
             "two complex conjugate roots")
    if disc7 >= 0:
        result7 = f"x_1 = {roots7[0].real:.4g}, \\qquad x_2 = {roots7[1].real:.4g}"
    else:
        result7 = f"x = {roots7[1].real:.4g} \\pm {roots7[1].imag:.4g}\\, i"
    text7 = (
        f"$$\\Delta = b^2 - 4ac = {par7(bv7)}^2 - 4 \\cdot {par7(av7)} \\cdot {par7(cv7)} = {disc7:g}$$\n\n"
        f"$\\Delta {'>' if disc7 > 0 else '=' if disc7 == 0 else '<'} 0$, so **{kind7}**:\n\n"
        f"$$x = \\frac{{-{par7(bv7)} \\pm \\sqrt{{{disc7:g}}}}}{{2 \\cdot {par7(av7)}}}"
        f"\\qquad\\Longrightarrow\\qquad {result7}$$"
    )
mo.md(text7)
```

```{marimo} python
:hide-code: true

# left: the parabola against the real axis; right: where the roots sit in the complex plane
if av7 != 0:
    xv7 = -bv7 / (2 * av7)
    half7 = max(3.0, 1.6 * max(abs(r.real - xv7) for r in roots7) + 1.0)
else:
    xv7 = 0.0 if not roots7 else roots7[0].real
    half7 = 4.0
xs7 = np.linspace(xv7 - half7, xv7 + half7, 400)
ys7 = av7 * xs7**2 + bv7 * xs7 + cv7
real7 = [r for r in roots7 if abs(r.imag) < 1e-12]
cplx7 = [r for r in roots7 if abs(r.imag) >= 1e-12]

fig7, (axL7, axR7) = plt.subplots(1, 2, figsize=(9.6, 4.0), gridspec_kw={"width_ratios": [1.25, 1]})
axL7.plot(xs7, ys7, color="0.2", lw=2.2)
axL7.axhline(0, color="k", lw=1.2)
axL7.axvline(0, color="0.75", lw=0.8)
for r in real7:
    axL7.plot(r.real, 0, "o", color="#C8102E", ms=9, zorder=5)
if av7 != 0 and cplx7:
    yv7 = av7 * xv7**2 + bv7 * xv7 + cv7
    axL7.annotate("", xy=(xv7, yv7), xytext=(xv7, 0), arrowprops=dict(arrowstyle="<->", color="#107895", lw=1.6))
    axL7.text(xv7, yv7 / 2, "  no crossing", color="#107895", fontsize=10, va="center")
ylo7, yhi7 = ys7.min(), ys7.max()
pad7 = 0.12 * (yhi7 - ylo7 + 1e-9)
axL7.set_ylim(min(ylo7, 0) - pad7, max(yhi7, 0) + pad7)
axL7.set_xlabel("x")
axL7.set_ylabel(r"$ax^2 + bx + c$")
def term7(v, power):
    """one term of the polynomial as text: drop zero terms, hide unit coefficients"""
    if v == 0:
        return ""
    mag = "" if abs(v) == 1 and power else f"{abs(v):g}"
    var = {2: "x²", 1: "x", 0: ""}[power]
    return f" {'-' if v < 0 else '+'} {mag}{var}"
poly7 = (term7(av7, 2) + term7(bv7, 1) + term7(cv7, 0)).strip() or "0"
poly7 = poly7[2:] if poly7.startswith("+ ") else "-" + poly7[2:] if poly7.startswith("- ") else poly7
axL7.set_title(f"y = {poly7}", fontsize=11)

axR7.axhline(0, color="k", lw=1.0)
axR7.axvline(0, color="k", lw=1.0)
for r in real7:
    axR7.plot(r.real, 0, "o", color="#C8102E", ms=10, zorder=5)
    axR7.annotate(f"{r.real:.3g}", (r.real, 0), textcoords="offset points", xytext=(6, 8), color="#C8102E", fontsize=10)
for r in cplx7:
    axR7.plot(r.real, r.imag, "o", color="#107895", ms=10, zorder=5)
    axR7.annotate(f"{r.real:.3g} {r.imag:+.3g}i", (r.real, r.imag), textcoords="offset points", xytext=(6, 6 if r.imag > 0 else -14), color="#107895", fontsize=10)
if cplx7:
    axR7.plot([cplx7[0].real] * 2, [cplx7[0].imag, cplx7[1].imag], ls="--", color="#107895", lw=1, alpha=0.6)
lim7 = max(1.5, 1.35 * max([abs(r) for r in roots7] + [1.0]))
axR7.set_xlim(-lim7, lim7)
axR7.set_ylim(-lim7, lim7)
axR7.set_aspect("equal")
axR7.set_xlabel("Re x")
axR7.set_ylabel("Im x")
axR7.set_title(f"{len(roots7)} root(s) in the complex plane", fontsize=11)
fig7.suptitle("Fig. Roots of the quadratic: crossings of the real axis (left) and positions in the complex plane (right)", fontsize=10, y=1.02)
fig7.tight_layout()
fig7
```

Start from the defaults and raise $c$: the two crossings slide together, merge at $\Delta = 0$, and then step off the real line as a mirror pair, real part shared and imaginary parts opposite. The curve stops touching the axis, but the number of roots never changes. That is the fundamental theorem of algebra in miniature: a degree $n$ polynomial has exactly $n$ complex roots. The background is in the [complex numbers appendix](../math/02-trigonometry-and-complex-numbers.md).

:::{tip} Want more room?
Every cell above is editable in place, so use this page as a scratchpad whenever you need a quick number, plot, or derivative. For guided tutorials that you can open in Colab, see [Python basics](01-python-basics.md), [NumPy](02-numpy.md), and [SymPy](03-symbolic-math-with-sympy.md).
:::
