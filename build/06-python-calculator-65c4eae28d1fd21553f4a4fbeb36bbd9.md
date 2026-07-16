# Python Calculator

:::{note} **Your quantum chemistry workbench**

Every panel on this page runs **live in your browser**. Cells with a play button are fully editable: change the numbers, press play (or Ctrl-Enter), and the result updates. Come back here whenever you need to crunch a quick number, make a plot, take a derivative, or look at an orbital, without leaving the website.

Already imported for you on this page: `numpy as np`, `matplotlib.pyplot as plt`, `sympy as sp`, and `scipy.constants as const`. The button at the top opens the whole page as an editable notebook in molab.
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

### 1. Constants and quick calculations

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

Or let the slider do the arithmetic. Can this photon break a C-C bond?

```{marimo} python
:hide-code: true

lam_q = mo.ui.slider(start=200, stop=1000, step=2, value=532, show_value=True,
                     label="photon wavelength (nm)")
lam_q
```

```{marimo} python
:hide-code: true

e_q = const.h * const.c / (lam_q.value * 1e-9)
kjmol_q = e_q * const.N_A / 1000
region_q = "ultraviolet" if lam_q.value < 380 else ("visible" if lam_q.value <= 750 else "infrared")
verdict_q = "YES, breaks a C-C bond (347 kJ/mol)" if kjmol_q > 347 else "no, too weak for a C-C bond (347 kJ/mol)"
mo.vstack([
    mo.md(f"A **{lam_q.value} nm** photon ({region_q}) carries **{e_q/const.e:.2f} eV** "
          f"= **{kjmol_q:.0f} kJ/mol**: **{verdict_q}**"),
    mo.Html(f"<div style='width:120px;height:14px;border-radius:7px;background:{to_hex(wavelength_to_rgb(lam_q.value))}'></div>"),
])
```

### 2. Unit converter

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

### 3. Plotting panel

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


### 4. Numerical integral

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


### 5. Symbolic window

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

### 6. Orbital visualizer

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
ax6.set_title(f"orbital ({n6}, {l6}, {m6}) — xz cross-section")
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

### 7. Orbital overlap

Bonding starts here. The **overlap integral** $S = \int \psi_A \psi_B\,d^3r$ measures how much two atomic orbitals share the same region with the same sign. Pick an orbital on each center, slide them together, and watch the overlap. The left panel shows both orbitals along the bond ($z$) axis; the right panel is the product $\psi_A\psi_B$ whose integral is $S$. Try **1s with 2p_x** to see an overlap that cancels to zero by symmetry.

```{marimo} python
:hide-code: true

ao_choices = {"1s": "1s", "2s": "2s", "2p_z": "2pz", "2p_x": "2px"}
aoA = mo.ui.dropdown(options=ao_choices, value="1s", label="orbital on A")
aoB = mo.ui.dropdown(options=ao_choices, value="1s", label="orbital on B")
d_sep = mo.ui.slider(0.5, 8.0, step=0.25, value=3.0, show_value=True,
                     label="internuclear distance d (Bohr)")
mo.vstack([mo.hstack([aoA, aoB], justify="start", gap=1.5), d_sep])
```

```{marimo} python
:hide-code: true

# real hydrogenic atomic orbitals, aligned so p_z points along the bond axis
Y_S7 = 1 / np.sqrt(4 * np.pi)
Y_P7 = np.sqrt(3 / (4 * np.pi))

def ao_amp(kind, X, Y, Z):
    r = np.sqrt(X**2 + Y**2 + Z**2) + 1e-12
    if kind == "1s":  return radial_c(r, 1, 0) * Y_S7
    if kind == "2s":  return radial_c(r, 2, 0) * Y_S7
    if kind == "2pz": return radial_c(r, 2, 1) * Y_P7 * Z / r
    if kind == "2px": return radial_c(r, 2, 1) * Y_P7 * X / r
```

```{marimo} python
:hide-code: true

d7 = d_sep.value
kA7, kB7 = aoA.value, aoB.value
labA7 = [k for k, v in ao_choices.items() if v == kA7][0]
labB7 = [k for k, v in ao_choices.items() if v == kB7][0]

# 2D cross-section in the xz-plane: A at z = -d/2, B at z = +d/2
gp7 = np.linspace(-9, 9, 280)
Xp7, Zp7 = np.meshgrid(gp7, gp7)
Yp7 = np.zeros_like(Xp7)
psiA7 = ao_amp(kA7, Xp7, Yp7, Zp7 + d7 / 2)
psiB7 = ao_amp(kB7, Xp7, Yp7, Zp7 - d7 / 2)
prod7 = psiA7 * psiB7

# overlap S via a 3D grid integral
gx7 = np.linspace(-9, 9, 48)
gz7 = np.linspace(-(d7 / 2 + 9), d7 / 2 + 9, 64)
XX7, YY7, ZZ7 = np.meshgrid(gx7, gx7, gz7, indexing="ij")
fA7 = ao_amp(kA7, XX7, YY7, ZZ7 + d7 / 2)
fB7 = ao_amp(kB7, XX7, YY7, ZZ7 - d7 / 2)
S7 = float(np.trapezoid(np.trapezoid(np.trapezoid(fA7 * fB7, gz7, axis=2), gx7, axis=1), gx7, axis=0))

fig7, axes7 = plt.subplots(1, 2, figsize=(9.5, 4.2))
panels7 = [(axes7[0], psiA7 + psiB7, f"{labA7} (A)  +  {labB7} (B)"),
           (axes7[1], prod7, r"product $\psi_A\,\psi_B$")]
for ax7, fld7, ttl7 in panels7:
    amp7 = np.abs(fld7).max() + 1e-12
    ax7.pcolormesh(Xp7, Zp7, fld7, cmap="RdBu_r", vmin=-amp7, vmax=amp7, shading="auto")
    ax7.plot(0, -d7 / 2, "k+", ms=11, mew=2)
    ax7.plot(0, d7 / 2, "k+", ms=11, mew=2)
    ax7.set_aspect("equal")
    ax7.set_xlabel("x (Bohr)")
    ax7.set_ylabel("z (Bohr)")
    ax7.set_title(ttl7, fontsize=10)
fig7.suptitle(f"overlap  S = {S7:.3f}   at  d = {d7:.2f} a0", fontsize=12)
fig7.tight_layout()
fig7
```

```{marimo} python
:hide-code: true

if abs(S7) < 0.03:
    verdict7 = ("**essentially zero**: the positive and negative lobes of the product cancel, "
                "a symmetry-forbidden overlap (the origin of the sigma / pi distinction)")
elif S7 > 0:
    verdict7 = ("**positive**: the orbitals meet with the same sign between the nuclei, "
                "the constructive overlap that builds a bonding orbital")
else:
    verdict7 = ("**negative**: the facing lobes have opposite sign, "
                "the destructive combination behind antibonding orbitals")

mo.md(f"Overlap $S = {S7:.3f}$ for {labA7} on A and {labB7} on B at $d = {d7:.2f}\\,a_0$. This is {verdict7}.")
```

The window where $|S|$ is a few tenths is exactly where [chemical bonds live](../ch08/02-hydrogen-molecule-ion.md). Pushing the nuclei together raises $|S|$, while a mismatch in orbital symmetry drives it to zero no matter how close they get.

### 8. One-dimensional Schrödinger solver

Pick a potential and get its bound states instantly: energies as horizontal lines, wavefunctions drawn at their own energy (units: $\hbar = m = 1$, hard walls at $x = \pm 4$). To see how the solver works inside, open the [numerical Schrödinger lab](07-demo-numerical-schrodinger.md).

```{marimo} python
:hide-code: true

pot1 = mo.ui.dropdown(
    options={
        "infinite box, V = 0": "box",
        "linear well, V = a|x|": "linear",
        "harmonic, V = a x^2 / 2": "harmonic",
        "double well, V = a((x/2)^2 - 1)^2": "double",
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

Try the classics: the box gives the $n^2$ ladder, the harmonic well gives perfectly even spacing (the fingerprint of vibrations), the linear well spaces levels like Airy zeros, and the double well pairs levels into tunneling doublets.



:::{tip} Want more room?
The molab button at the top opens this whole page as an editable notebook where you can add as many cells as you like. For guided tutorials, see [Python basics](01-python-basics.md), [NumPy](02-numpy.md), and [SymPy](03-symbolic-math-with-sympy.md).
:::
