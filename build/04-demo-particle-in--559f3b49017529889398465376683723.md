---
kernelspec:
  name: python3
  display_name: Python 3
---

# DEMO: Particle in a box



```{marimo-config}
---
echo: true
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
import plotly.graph_objects as go
from sympy import symbols, sqrt, sin, pi, diff, integrate, simplify, pprint, init_printing
```


```{marimo} python
#@title load particle in a box wavefunctions and energies for 1D and 2D

h, m = 1, 1 
hbar = h/(2*np.pi)

def Epib1d(n=1, L=1):
        '''Calculates energy of 1D PIB state.
        Args:
        n (int): Quantum number specifying state.
        L (float): Box dimensions in Bohr.
        Returns:
         Float energy value in Ha.
        '''

        En = (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

        return En

    
def psi(x, n=1, L=1):      
        '''Numeric representation of the normalized 1D PIB wavefunction.
        Args:
         x  (float or array): Cartesian spatial values.
         n  (int):   Quantum number
         L  (float): Box dimensions in Bohr.
        Returns:
        Wavefunction evaulated at a point or array if input x are arrays.
        '''

        fn = np.sqrt(2/L)*np.sin(n*np.pi*x/L)

        return fn

def psi_reg(x, y, z, nx=1, ny=1, nz=1, lx=1, ly=1, lz=1):
        '''Numeric representation of the normalized 3D PIB wavefunction.
        Args:
         x, y, z (float or array): Cartesian spatial values.
         q_nx, q_ny, q_nz (int): Quantum numbers specifying state.
         lx, ly, lz (int): Box dimensions in Bohr.
        Returns:
         Wavefunction evaulated at a point or array if input x, y, z are arrays.
        '''

        return psi(x, nx, lx) * psi(y, ny, ly) * psi(z, nz, lz)

def psi_ener(nx, ny, nz, lx, ly, lz):
        '''Calculates energy of 3D PIB state.
        Args:
         qnx, qny, qnz (int): Quantum numbers specifying state.
         lx, ly, lz (float): Box dimensions in Bohr.
        Returns:
         Float energy value in Ha.
        '''

        return Epib1d(nx, lx) + Epib1d(ny, ly) + Epib1d(nz, lz)
```

### Interactive exploration of 1D quantum particle in a box

```{marimo} python
def plot_energy_levels(L=1, max_n=1):
    
    fig, (ax, ax2) = plt.subplots(figsize=(8, 6), ncols=2)

    for n in range(1, max_n+1):
        
        En = Epib1d(n, L)
        
        ax.hlines(En, 0.5, 1.5, colors='blue', linewidth=2)
        ax.text(1.6, En, f"n={n}, E={En:.2f}", verticalalignment='center')
        
    ax.set_xlim(0, 3)
    ax.set_ylim(0, Epib1d(n=max_n+1, L=L ))
    ax.set_xlabel("Particle in a Box")
    ax.set_ylabel("Energy")
    ax.set_title("Energy Levels of a 1D Quantum Particle in a Box")
    ax.axes.get_xaxis().set_visible(False)
    
    x = np.linspace(0, L, 1000)
    psi1d = psi(x, n=max_n, L=L)
   
    ax2.fill(x, psi1d**2, color="green", lw=3)
    ax2.set_xlim([-0.1, L+0.1])
    ax2.set_ylim([0, 4])
    
    # Put two red lines to indicate boundaries
    ax2.axvline(0,0,10*L, color='red',lw=3)
    ax2.axvline(L,0,10*L, color='red',lw=3)
    
    # Label axis
    ax2.set_xlabel('x',fontsize=20)
    ax2.set_ylabel('$\psi_n^2(x)$',fontsize=20)
    
    #Put tiltle
    ax2.set_title('n='+str(n))
    
    plt.tight_layout()
    plt.show()
```

```{marimo} python
:hide-code: true

box_L = mo.ui.slider(0.5, 2.0, step=0.1, value=1.0, show_value=True, label="box length L")
n_max = mo.ui.slider(1, 10, step=1, value=3, show_value=True, label="highest state n")
mo.hstack([box_L, n_max], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

hbar_m = 1 / (2 * np.pi)

fig1d, (ax_lev, ax_psi) = plt.subplots(figsize=(9, 4.2), ncols=2)
for n_i in range(1, n_max.value + 1):
    E_i = (n_i**2 * np.pi**2 * hbar_m**2) / (2 * box_L.value**2)
    ax_lev.hlines(E_i, 0.5, 1.5, colors="steelblue", lw=2)
    ax_lev.text(1.6, E_i, f"n={n_i}, E={E_i:.2f}", va="center", fontsize=9)
ax_lev.set_xlim(0, 3)
ax_lev.set_ylim(0, ((n_max.value + 1) ** 2 * np.pi**2 * hbar_m**2) / (2 * box_L.value**2))
ax_lev.set_ylabel("energy")
ax_lev.axes.get_xaxis().set_visible(False)
ax_lev.set_title("energy levels", fontsize=11)

x_b = np.linspace(0, box_L.value, 800)
psi_b = np.sqrt(2 / box_L.value) * np.sin(n_max.value * np.pi * x_b / box_L.value)
ax_psi.fill_between(x_b, psi_b**2, color="seagreen", alpha=0.85)
ax_psi.axvline(0, color="red", lw=3)
ax_psi.axvline(box_L.value, color="red", lw=3)
ax_psi.set_xlim(-0.1, box_L.value + 0.1)
ax_psi.set_ylim(0, 4)
ax_psi.set_xlabel("x")
ax_psi.set_title(f"probability density, n={n_max.value}", fontsize=11)
fig1d.tight_layout()
fig1d
```

### Particle in 3D Box

```{marimo} python
def pib3d_plotly(nx=1, ny=1, nz=1, lx=10, ly=10, lz=10):
  '''Displays and saves isosurface of 3D PIB wavefunction.
  Args:
      nx_val, ny_val, nz_val (int): Quantum numbers specifying state.
      lx, ly, lz (int): Box dimensions in Bohr.
      psi_square (bool): Calculate prob. density (true) or wavefunction (false).
      plot_save (bool): Save a .png file of display.
  '''
  # construct 3d grid of points
  nx_p, ny_p, nz_p = 7 * lx, 7 * ly, 7 * lz
  xp, yp, zp       = np.linspace(0, lx, nx_p), np.linspace(0, ly, ny_p), np.linspace(0, lz, nz_p)
  X, Y, Z          = np.meshgrid(xp, yp, zp, indexing='ij')
  psi              = psi_reg(X, Y, Z, nx, ny, nz, lx, ly, lz)
  psi2             = psi**2
  mean_dens        = psi2.mean()

  figure = go.Figure(data=go.Isosurface(
  x=X.flatten(),
  y=Y.flatten(),
  z=Z.flatten(),
  value=psi2.flatten(), # pis or psi2
  colorscale='BlueRed',
  isomin= -mean_dens,
  isomax=  mean_dens,
  surface_count=2,
  showscale=False,
  caps=dict(x_show=False, y_show=False, z_show=False)
  ))

  figure.update_layout(scene = dict(
                  xaxis_title='x',
                  yaxis_title='y',
                  zaxis_title='z',
                  aspectmode='data'),
                  width=800,
                  height=500,
                  title_text=f'Prob. Den., isovalue = {mean_dens:.4f}')

  figure.show()
```

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

### Visualize energy levels of 3D PIB

```{marimo} python
def plot_energy_levels(nx_max=10, ny_max=10, nz_max=10, lx=1, ly=1, lz=1):

    fig, ax = plt.subplots(figsize=(8, 6))

    for nx in range(1, nx_max+1):

        Enx = Epib1d(nx, lx)
        ax.hlines(Enx, 0.6, 1, colors='blue', linewidth=2)

    for ny in range(1, ny_max+1):

        Eny = Epib1d(ny, ly)
        ax.hlines(Eny, 1.1, 1.5, colors='green', linewidth=2)

    for nz in range(1, nz_max+1):

        Enz = Epib1d(nz, lz)
        ax.hlines(Enz, 1.6, 2.0, colors='yellow', linewidth=2)

    E_max =     Epib1d(nx_max+1, lx)+Epib1d(ny_max+1, ly)+Epib1d(nz_max+1, lz)
    ax.set_xlim(0.5, 2.1)
    ax.set_ylim(0, E_max)
    ax.set_xlabel("Particle in a 3d Box")
    ax.set_ylabel("Energy")
    ax.set_title(f"Energy Levels of a 3D Quantum Particle in a Box E={E_max:2f}")
    ax.axes.get_xaxis().set_visible(False)

    plt.tight_layout()
    plt.show()
```

```{marimo} python
:hide-code: true

lx_l = mo.ui.slider(0.5, 2.0, step=0.25, value=1.0, show_value=True, label="lx")
ly_l = mo.ui.slider(0.5, 2.0, step=0.25, value=1.0, show_value=True, label="ly")
lz_l = mo.ui.slider(0.5, 2.0, step=0.25, value=1.0, show_value=True, label="lz")
mo.hstack([lx_l, ly_l, lz_l], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

hbar_l = 1 / (2 * np.pi)
fig_lad, ax_lad = plt.subplots(figsize=(7, 4.2))
for side_l, x0, x1, color_l, lbl in [
    (lx_l.value, 0.6, 1.0, "steelblue", "x"),
    (ly_l.value, 1.1, 1.5, "seagreen", "y"),
    (lz_l.value, 1.6, 2.0, "goldenrod", "z"),
]:
    for n_j in range(1, 7):
        E_j = (n_j**2 * np.pi**2 * hbar_l**2) / (2 * side_l**2)
        ax_lad.hlines(E_j, x0, x1, colors=color_l, lw=2)
    ax_lad.text((x0 + x1) / 2, -0.35, lbl, ha="center")
ax_lad.set_xlim(0.5, 2.1)
ax_lad.set_ylim(-0.7, (36 * np.pi**2 * hbar_l**2) / (2 * min(lx_l.value, ly_l.value, lz_l.value) ** 2) * 1.05)
ax_lad.set_ylabel("energy")
ax_lad.axes.get_xaxis().set_visible(False)
ax_lad.set_title("level ladders per direction: stretch a side, break degeneracy", fontsize=11)
fig_lad.tight_layout()
fig_lad
```

### Symbolic evaluations of Paritcle in a box integrals

```{marimo} python
# Initialize pretty printing
init_printing()

# Define symbols
x, L, n, hbar = symbols('x L n hbar', real=True, positive=True)
```

#### Step 1: Define the wavefunction

```{marimo} python
psi_n = sqrt(2/L) * sin(n * pi * x / L)

print("Wavefunction ψ_n(x):")

pprint(psi_n)
```

#### Step 2: Compute the second derivative of ψ_n(x)

```{marimo} python
d2psi_dx2 = diff(psi_n, x, x)

print("Second derivative d²ψ_n/dx²:")

pprint(d2psi_dx2)
```

#### Step 3: Apply the momentum squared operator: -ħ² d²ψ_n/dx²

```{marimo} python
op_psi = -hbar**2 * d2psi_dx2

print("Momentum operator applied to ψ_n(x): -ħ² d²ψ_n/dx²:")

pprint(op_psi)
```

#### Step 4: Compute the integrand ψ_n(x) * op_ψ_n(x)

```{marimo} python
integrand = psi_n * op_psi

print("Integrand ψ_n(x) * (-ħ² d²ψ_n/dx²):")

pprint(integrand)
```

#### Step 5: Compute the expectation value ⟨p²⟩

```{marimo} python
expectation = integrate(integrand, (x, 0, L))

print("Expectation value ⟨p²⟩ before simplification:")

pprint(expectation)
```

#### Step 6: Simplify the result

```{marimo} python
expectation_simplified = simplify(expectation)

print("Simplified expectation value ⟨p²⟩:")

pprint(expectation_simplified)
```
