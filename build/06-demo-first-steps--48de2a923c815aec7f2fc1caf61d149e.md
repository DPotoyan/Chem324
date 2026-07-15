# DEMO: First Steps with Python

:::{note} **What you need to know**

- You do not need to install anything. The Python cells on this page run **live in your browser**: move a slider and every result that depends on it recomputes.
- A few lines of Python replace a pocket calculator, a formula sheet, and a unit-conversion table. This page walks through the four skills you will reuse all semester:
  - **Calculating** with physical constants (no more typing $6.626 \times 10^{-34}$ by hand)
  - **Writing functions** so a formula is typed once and reused forever
  - **Plotting** to see physics that tables of numbers hide
  - **Symbolic math** with `sympy`, which does calculus for you
- Everything here uses the physics of this chapter: photons, the hydrogen spectrum, and blackbody radiation.
:::

The page has five stations, and each one introduces exactly one library at the moment it becomes useful: physical constants, then arrays and plots, then symbolic math.

### 1. Python as a scientific calculator

Our first import: `scipy.constants` knows every physical constant, so you never mistype one ([full list](https://docs.scipy.org/doc/scipy/reference/constants.html)). One line of code, and $h$, $c$, $e$, $k_B$, $N_A$ are all at your fingertips:

```{marimo-config}
---
echo: true
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
```

```{marimo} python
import scipy.constants as const
```

```{marimo} python
:hide-code: true

mo.md(f"""
| constant | symbol | value |
|---|---|---|
| Planck | $h$ | {const.h:.4e} J s |
| speed of light | $c$ | {const.c:.4e} m/s |
| electron charge | $e$ | {const.e:.4e} C |
| Boltzmann | $k_B$ | {const.k:.4e} J/K |
| Avogadro | $N_A$ | {const.N_A:.4e} 1/mol |
""")
```

```{marimo} python
:hide-code: true

from matplotlib.colors import to_hex

def wavelength_to_rgb(nm):
    """Rough RGB color of a visible wavelength; gray outside 380 to 750 nm."""
    if 380 <= nm < 440:
        rgb = (-(nm - 440) / 60, 0.0, 1.0)
    elif 440 <= nm < 490:
        rgb = (0.0, (nm - 440) / 50, 1.0)
    elif 490 <= nm < 510:
        rgb = (0.0, 1.0, -(nm - 510) / 20)
    elif 510 <= nm < 580:
        rgb = ((nm - 510) / 70, 1.0, 0.0)
    elif 580 <= nm < 645:
        rgb = (1.0, -(nm - 645) / 65, 0.0)
    elif 645 <= nm <= 750:
        rgb = (1.0, 0.0, 0.0)
    else:
        rgb = (0.55, 0.55, 0.55)
    return rgb
```

A green laser pointer emits 532 nm light. What is the energy of one of its photons? Type the formula $E = h c / \lambda$ almost exactly as you would write it:

```{marimo} python
lam_green = 532e-9                          # wavelength in meters
E_green = const.h * const.c / lam_green     # photon energy in joules

E_green
```

Joules are inconvenient at the atomic scale, so chemists quote photon energies in **electron volts** (divide by the electron charge) or **kJ/mol** (multiply by Avogadro's number). Unit conversion is just arithmetic:

```{marimo} python
ev_green = E_green / const.e                # joules -> electron volts
kjmol_green = E_green * const.N_A / 1000    # per photon -> kJ per mole
```

```{marimo} python
:hide-code: true

mo.md(
    f"one green photon carries **{E_green:.3e} J**, i.e. **{ev_green:.2f} eV**, "
    f"and a mole of them delivers **{kjmol_green:.0f} kJ/mol**"
)
```

A mole of green photons carries about 225 kJ, and a typical C-C single bond costs 347 kJ/mol. Can light break a bond? Drag the slider and find out. Making an interactive control is one line of code:

```{marimo} python
lam_pick = mo.ui.slider(
    start=200, stop=1000, step=2, value=532,
    show_value=True, label="photon wavelength (nm)",
)
lam_pick
```

```{marimo} python
:hide-code: true

e_pick = const.h * const.c / (lam_pick.value * 1e-9)
ev_pick = e_pick / const.e
kjmol_pick = e_pick * const.N_A / 1000

if lam_pick.value < 380:
    region_pick = "ultraviolet"
elif lam_pick.value <= 750:
    region_pick = "visible"
else:
    region_pick = "infrared"

verdict = "YES, breaks a C-C bond (347 kJ/mol)" if kjmol_pick > 347 else "no, too weak for a C-C bond (347 kJ/mol)"
chip = to_hex(wavelength_to_rgb(lam_pick.value))

mo.vstack([
    mo.md(
        f"A **{lam_pick.value} nm** photon ({region_pick}) carries "
        f"**{ev_pick:.2f} eV**, or **{kjmol_pick:.0f} kJ/mol** per mole of photons: "
        f"**{verdict}**."
    ),
    mo.Html(f"<div style='width:120px;height:14px;border-radius:7px;background:{chip}'></div>"),
])
```

Notice the chemistry hiding in this toy: visible light cannot touch a C-C bond, but ultraviolet light below roughly 345 nm can. That is why UV radiation damages molecules and sunscreen exists.

### 2. The de Broglie wavelength, in three lines

The same calculator settles a chapter question: why do electrons diffract but baseballs do not? Compute $\lambda = h / mv$ for both. For the electron we use its speed in the ground state of the Bohr model [@bohr1913], $v \approx 2.19 \times 10^6$ m/s:

```{marimo} python
lam_electron = const.h / (const.m_e * 2.19e6)    # electron at Bohr-orbit speed
lam_baseball = const.h / (0.145 * 40.0)          # 145 g fastball at 40 m/s
```

```{marimo} python
:hide-code: true

mo.md(
    f"electron: **{lam_electron*1e9:.3f} nm**, about the size of an atom; "
    f"baseball: **{lam_baseball:.1e} m**, hopelessly smaller than anything measurable"
)
```

### 3. Functions: the hydrogen spectrum

When a formula gets used more than once, wrap it in a **function**. The Rydberg formula predicts every line hydrogen emits when an electron falls from level $n_{hi}$ to $n_{lo}$:

$$
\frac{1}{\lambda} = R_H \left( \frac{1}{n_{lo}^2} - \frac{1}{n_{hi}^2} \right)
$$

```{marimo} python
def rydberg_nm(n_lo, n_hi):
    """Wavelength (nm) of the hydrogen emission line n_hi -> n_lo."""
    inv_lam = const.Rydberg * (1 / n_lo**2 - 1 / n_hi**2)
    return 1e9 / inv_lam

rydberg_nm(2, 3)   # the famous red Balmer line, in nm
```

Now the function powers a live energy-level diagram. Pick a series and an upper level; the diagram draws the transition and colors the emitted photon:

```{marimo} python
:hide-code: true

series_pick = mo.ui.dropdown(
    options={"Lyman (down to n=1)": 1, "Balmer (down to n=2)": 2, "Paschen (down to n=3)": 3},
    value="Balmer (down to n=2)",
    label="series",
)
series_pick
```

```{marimo} python
:hide-code: true

n_upper = mo.ui.slider(
    start=series_pick.value + 1, stop=series_pick.value + 8, step=1,
    value=series_pick.value + 1, show_value=True,
    label=f"upper level n (lowest allowed: {series_pick.value + 1})",
)
n_upper
```

```{marimo} python
:hide-code: true

n_lo_sel = series_pick.value
n_hi_sel = n_upper.value
lam_line = rydberg_nm(n_lo_sel, n_hi_sel)
ry_ev = const.Rydberg * const.h * const.c / const.e   # 13.606 eV

fig_lev, ax_lev = plt.subplots(figsize=(7, 4.6))
for n_i in range(1, 11):
    e_i = -ry_ev / n_i**2
    ax_lev.hlines(e_i, 0.1, 0.9, color="0.6", lw=1.2)
    if n_i <= 5 or n_i == 10:
        ax_lev.text(0.92, e_i, f"n = {n_i}", va="center", fontsize=9)

arrow_color = wavelength_to_rgb(lam_line)
ax_lev.annotate(
    "", xy=(0.5, -ry_ev / n_lo_sel**2), xytext=(0.5, -ry_ev / n_hi_sel**2),
    arrowprops=dict(arrowstyle="->", color=arrow_color, lw=2.5),
)
ax_lev.text(
    0.55, (-ry_ev / n_lo_sel**2 - ry_ev / n_hi_sel**2) / 2,
    f"{n_hi_sel} to {n_lo_sel}:  {lam_line:.0f} nm", color=arrow_color, fontsize=11,
)
ax_lev.set_ylim(-14.2, 0.8)
ax_lev.set_xlim(0, 1.15)
ax_lev.set_xticks([])
ax_lev.set_ylabel("energy (eV)")
ax_lev.set_title(f"hydrogen levels, E_n = -13.6/n^2 eV", fontsize=11)
fig_lev
```

Gray arrows mean the photon lies outside the visible window. Only the Balmer series lands in it, which is why hydrogen discharge tubes glow red-pink: you are looking mostly at the 656 nm line you computed above.

### 4. Plotting: blackbody radiation

Two more imports, and they are the workhorses of all scientific Python: `numpy` handles arrays of numbers, and `matplotlib` turns them into figures.

```{marimo} python
import numpy as np
import matplotlib.pyplot as plt
```

Planck's law [@planck1901] started quantum mechanics. Typed as code, it is three lines:

```{marimo} python
def planck(lam_m, T):
    """Spectral radiance (kW per sr per m^2 per nm) at wavelength lam_m (meters)."""
    x = const.h * const.c / (lam_m * const.k * T)
    with np.errstate(over="ignore"):   # exp overflows harmlessly at short wavelengths
        return 2 * const.h * const.c**2 / lam_m**5 / (np.exp(x) - 1) * 1e-12
```

```{marimo} python
:hide-code: true

temp_pick = mo.ui.slider(
    start=1000, stop=10000, step=250, value=5800,
    show_value=True, label="temperature (K)",
)
temp_pick
```

```{marimo} python
:hide-code: true

lam_grid = np.linspace(100e-9, 3000e-9, 600)
lam_nm_grid = lam_grid * 1e9

fig_bb, ax_bb = plt.subplots(figsize=(7, 4.4))
for t_ref in (4000, 7000):
    ax_bb.plot(lam_nm_grid, planck(lam_grid, t_ref), color="0.82", lw=1.2)
    ax_bb.text(2500, planck(2500e-9, t_ref), f"{t_ref} K", color="0.6", fontsize=9)
ax_bb.plot(lam_nm_grid, planck(lam_grid, temp_pick.value), color="crimson", lw=2.2)
ax_bb.axvspan(380, 750, color="gold", alpha=0.18)
lam_wien = const.Wien / temp_pick.value * 1e9
ax_bb.axvline(lam_wien, color="0.3", ls="--", lw=1)
ax_bb.text(lam_wien + 40, ax_bb.get_ylim()[1] * 0.05, f"peak: {lam_wien:.0f} nm", fontsize=10)
ax_bb.set_xlabel("wavelength (nm)")
ax_bb.set_ylabel("spectral radiance (kW / sr / m$^2$ / nm)")
ax_bb.set_title(f"blackbody spectrum at {temp_pick.value} K (shaded band: visible light)", fontsize=11)
ax_bb.set_ylim(bottom=0)
fig_bb
```

The default 5800 K is the surface of the Sun: its peak sits right in the visible band (evolution is not a coincidence). Cool the slider to 3000 K, a light bulb filament, and watch the peak slide into the infrared, which is why incandescent bulbs waste most of their energy as heat.

### 5. Symbolic math: let the computer do calculus

Our final import is `sympy`, an entire computer algebra system:

```{marimo} python
import sympy as sp
```

The dashed "peak" line obeys **Wien's law**, $\lambda_{max} T = b$. In 1900 deriving it took real work; `sympy` differentiates Planck's law and finds the root for you. One standard physics trick first: substitute the dimensionless variable $x = hc / \lambda k_B T$, so Planck's law becomes a clean scale-free shape $x^5 / (e^x - 1)$ and every temperature collapses onto one curve:

```{marimo} python
x_s = sp.symbols("x", positive=True)
shape = x_s**5 / (sp.exp(x_s) - 1)   # Planck's law in x = hc/(lam kB T)

dshape = sp.diff(shape, x_s)         # calculus, done symbolically
x_star = sp.solve(dshape, x_s)[0]    # solved exactly, no numerics

x_star
```

That output is not a decimal: `sympy` solved the transcendental equation **exactly**, in terms of the Lambert W function. Turned into numbers, it hands us Wien's constant:

```{marimo} python
:hide-code: true

wien_b = const.h * const.c / (const.k * float(x_star))

mo.md(
    f"numerically $x^* = {float(x_star):.4f}$, so the derived Wien constant is "
    f"$b = hc / x^* k_B$ = **{wien_b:.4e} m K** (scipy tabulates {const.Wien:.4e}), "
    f"which puts the 5800 K peak at **{wien_b / 5800 * 1e9:.0f} nm**"
)
```

The result matches the dashed line in the plot above and scipy's tabulated constant to four digits. You will use the same maximize-by-differentiating trick later to locate maxima of probability densities.

### 6. Complex numbers: a 30-second preview

Quantum wavefunctions are complex-valued, so Python treats complex numbers as first-class citizens (`1j` is the imaginary unit). Take $z = 1 + \sqrt{3}\,i$:

```{marimo} python
z = 1 + np.sqrt(3) * 1j    # 1j is the imaginary unit

z_conj = z.conjugate()
z_mod = abs(z)
z_phase = np.angle(z)
```

```{marimo} python
:hide-code: true

mo.md(
    f"$z = {z.real:.0f} + {z.imag:.3f}\\,i$, with conjugate "
    f"$z^* = {z_conj.real:.0f} - {abs(z_conj.imag):.3f}\\,i$, modulus "
    f"$|z| = \\sqrt{{z z^*}} = {z_mod:.3f}$, and polar form "
    f"$r = {z_mod:.3f}$, $\\varphi = {z_phase/np.pi:.3f}\\,\\pi$"
)
```

The quantity $z z^* = |z|^2$ is exactly how probability densities are built from wavefunctions in [Chapter 3](../ch03/02-wavefunction.md).

:::{attention} **Things to try**

- Find the longest wavelength that can break a C-C bond, then look up where the ozone layer absorbs. Coincidence?
- Set the series to Lyman and push the upper level to 10. Estimate the **series limit**, the wavelength an electron falling from $n = \infty$ would emit, and check it against $\lambda = 1/R_H$ with the calculator cells.
- The cosmic microwave background is a 2.725 K blackbody. Use `const.Wien / 2.725` in any code cell (open the notebook via the button at the top of the page) to find its peak wavelength, then classify the radiation.
- Compute your own de Broglie wavelength walking at 1.5 m/s. Report it in units of the Bohr radius, `const.value("Bohr radius")`.
:::

:::{tip} How this page works
:class: dropdown

The Python cells are [marimo](https://marimo.io) cells executed while the site is built, so the page loads instantly with correct static output. The first time you move a control, a Python runtime (Pyodide, Python compiled to WebAssembly) loads in the background with NumPy, SciPy, Matplotlib, and SymPy, and from then on every cell reruns locally in your browser. The button at the top of the page opens the whole thing as an editable notebook if you want to change the code itself.
:::
