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
      "plotly",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
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

A ready-to-edit plotting template. Swap in any function of `x_p`; the slider is yours to repurpose:

```{marimo} python
:hide-code: true

k_p = mo.ui.slider(1, 12, step=1, value=3, show_value=True, label="parameter k")
k_p
```

```{marimo} python
:editor: true

x_p = np.linspace(0, 2 * np.pi, 500)
y_p = np.sin(k_p.value * x_p) * np.exp(-x_p / 4)   # edit me

fig_p, ax_p = plt.subplots(figsize=(7, 3.5))
ax_p.plot(x_p, y_p, lw=2)
ax_p.set_xlabel("x")
ax_p.grid(True, ls="--", alpha=0.4)
fig_p
```

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

Pick quantum numbers; the menus only ever offer valid combinations. Drag to rotate the orbital (blue and red are the wavefunction's positive and negative lobes):

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

ext_v = 6.0 * n_v.value
g_v = np.linspace(-ext_v, ext_v, 45)
X_v, Y_v, Z_v = np.meshgrid(g_v, g_v, g_v, indexing="ij")
r_v = np.sqrt(X_v**2 + Y_v**2 + Z_v**2)
th_v = np.where(np.isclose(r_v, 0.0), 0.0, np.arccos(Z_v / (r_v + 1e-12)))
ph_v = np.arctan2(Y_v + 1e-10, X_v)
psi_v = (radial_c(r_v, n_v.value, l_v.value) * sph_harm_y(l_v.value, m_v.value, th_v, ph_v)).real
amp_v = 0.5 * np.abs(psi_v).max()

fig_v = go.Figure(data=go.Isosurface(
    x=X_v.flatten(), y=Y_v.flatten(), z=Z_v.flatten(), value=psi_v.flatten(),
    colorscale="RdBu", isomin=-amp_v, isomax=amp_v, surface_count=2,
    showscale=False, caps=dict(x_show=False, y_show=False, z_show=False),
))
fig_v.update_layout(scene=dict(aspectmode="data"), width=660, height=460,
                    title_text=f"orbital ({n_v.value}, {l_v.value}, {m_v.value})")
fig_v
```

### 6. Orbital overlap

Bonding starts here: slide two 1s orbitals together and watch their **overlap integral** $S(d) = e^{-d}\left(1 + d + d^2/3\right)$ grow (distances in Bohr radii). The shaded region is the product $\psi_A \psi_B$ whose integral is $S$:

```{marimo} python
:hide-code: true

d_sep = mo.ui.slider(0.5, 8.0, step=0.25, value=2.0, show_value=True,
                     label="internuclear distance d (Bohr)")
d_sep
```

```{marimo} python
:hide-code: true

d_val = d_sep.value
x_o = np.linspace(-8, 8, 800)
psi_A = np.exp(-np.abs(x_o + d_val / 2)) / np.sqrt(np.pi)
psi_B = np.exp(-np.abs(x_o - d_val / 2)) / np.sqrt(np.pi)
S_curve_d = np.linspace(0.01, 8, 200)
S_curve = np.exp(-S_curve_d) * (1 + S_curve_d + S_curve_d**2 / 3)
S_now = np.exp(-d_val) * (1 + d_val + d_val**2 / 3)

fig_o, (ax_oa, ax_ob) = plt.subplots(1, 2, figsize=(9.5, 3.6))
ax_oa.plot(x_o, psi_A, lw=1.8, color="steelblue", label=r"$\psi_A$ (1s)")
ax_oa.plot(x_o, psi_B, lw=1.8, color="seagreen", label=r"$\psi_B$ (1s)")
ax_oa.fill_between(x_o, psi_A * psi_B * 6, color="crimson", alpha=0.35, label=r"$\psi_A \psi_B$ (scaled)")
ax_oa.axvline(-d_val / 2, color="0.6", ls=":", lw=1)
ax_oa.axvline(d_val / 2, color="0.6", ls=":", lw=1)
ax_oa.set_xlabel("x (Bohr)")
ax_oa.legend(fontsize=8, frameon=False)
ax_oa.set_title("two 1s orbitals (cut along the bond axis)", fontsize=10)

ax_ob.plot(S_curve_d, S_curve, lw=2, color="0.4")
ax_ob.plot(d_val, S_now, "o", ms=9, color="crimson")
ax_ob.set_xlabel("separation d (Bohr)")
ax_ob.set_ylabel("overlap S(d)")
ax_ob.set_title(f"S({d_val:.2f}) = {S_now:.3f}", fontsize=10)
ax_ob.set_ylim(0, 1.02)
fig_o.tight_layout()
fig_o
```

At $d = 0$ the orbitals coincide and $S = 1$; by $d \approx 8\,a_0$ the overlap is essentially gone. The window where $S$ is a few tenths is exactly where [chemical bonds live](../ch08/02-hydrogen-molecule-ion.md).

:::{tip} Want more room?
The molab button at the top opens this whole page as an editable notebook where you can add as many cells as you like. For guided tutorials, see [Python basics](01-python-basics.md), [NumPy](02-numpy.md), and [SymPy](03-symbolic-math-with-sympy.md).
:::
