---
kernelspec:
  name: python3
  display_name: Python 3
---

# DEMO: H wavefunctions

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "scipy",
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
from scipy.special import sph_harm_y, genlaguerre, factorial
```

```{marimo} python
:hide-code: true

def radial_m(r, n=1, l=0):
    pre = np.sqrt(((2 / n) ** 3 * factorial(n - l - 1)) / (2 * n * factorial(n + l)))
    p = 2 * r / n
    return pre * np.exp(-p / 2) * p**l * genlaguerre(n - l - 1, 2 * l + 1)(p)
```

#### Requirements | Importing libraries

```{code-cell} python
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.special import sph_harm_y, genlaguerre, factorial
```

#### 1. Describing a radial function $R_{nl}(r)$

$$R_{nl} = \sqrt{ \Big( \frac{2}{n a_0} \Big)^3 \frac{(n-l-1)!}{2n(n+l)!}} \cdot e^{-\frac{r}{n a_0}} \cdot \Big( \frac{2 r}{n a_0} \Big)^l \cdot L^{2l+1}_{n-l-1}\Big( \frac{2 r}{n a_0} \Big)$$

```{code-cell} python

def radial_function(r, 
                    n=1, 
                    l=0):
    '''Rnl(r) normalized radial function
    r: radial distance Float (0, inf)
    n: principal quantum number Int (1,2,3... inf)
    l: angular quantum number Int (0,1,2,... n-1)
    '''
    
    a0 = 1 # set Bohr radius to 1 (Hartree units)

    prefactor = np.sqrt( ((2 / n * a0) ** 3 * (factorial(n - l - 1))) / (2 * n * (factorial(n + l))) )

    laguerre = genlaguerre(n - l - 1, 2 * l + 1)

    p = 2 * r / (n * a0)
    

    return  prefactor * np.exp(-p / 2) * (p ** l) * laguerre(p)
```

```{code-cell} python
r = np.linspace(0, 20, 1000)

Rnl = radial_function(r, n=2, l=0)

#plt.plot(r, Rnl)
#plt.plot(r, Rnl**2)
plt.plot(r, r**2 * Rnl**2)
plt.xlabel(r'$r [a_0]$')
plt.ylabel(r'$R_nl(r) r^2$')
```

**Check properties of radial distributon functions**

```{code-cell} python
r = np.linspace(0, 100, 10000)
dr = r[1]-r[0]

Rnl = radial_function(r, n=5, l=3)

pr = r**2 * Rnl**2 

norm = np.trapezoid(pr * dr) # Check normalizaton
#cdf  = np.cumsum(pr * dr) 

print(norm)
```

```{code-cell} python
np.trapezoid(pr*r*dr)
```

```{marimo} python
:hide-code: true

n_r = mo.ui.slider(1, 6, step=1, value=2, show_value=True, label="n")
n_r
```

```{marimo} python
:hide-code: true

l_r = mo.ui.dropdown(
    options={str(v): v for v in range(n_r.value)}, value="0", label="l"
)
l_r
```

```{marimo} python
:hide-code: true

l_eff = l_r.value
r_g = np.linspace(1e-6, 12 * n_r.value, 900)
R_g = radial_m(r_g, n_r.value, l_eff)

fig_r, (ax_R, ax_P) = plt.subplots(figsize=(9, 3.6), ncols=2)
ax_R.plot(r_g, R_g, lw=2)
ax_R.axhline(0, color="0.8", lw=0.8)
ax_R.set_xlabel("r (Bohr)")
ax_R.set_title(f"radial function R({n_r.value},{l_eff})", fontsize=11)
ax_P.plot(r_g, r_g**2 * R_g**2, lw=2, color="seagreen")
ax_P.set_xlabel("r (Bohr)")
ax_P.set_title("radial probability r^2 R^2", fontsize=11)
fig_r.tight_layout()
fig_r
```

#### 2. Describing an angular function | Spherical harmonic $Y_{l}^{m}(\theta, \varphi)$

- We will make use of [sph_harm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.sph_harm.html#scipy.special.sph_harm) function from Scipy
- We can also build up spherical harmonics using Associated Legendre function using [lpvm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.lpmv.html#scipy.special.lpmv) 

$$
Y_{lm}(\phi,\theta) = \sqrt{\frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!} } P_{lm}(cos \phi) \cdot e^{im\theta}
$$

```{code-cell} python
sph_harm_y(0, 0, np.pi, np.pi) # test a few spherical harmonics
```

```{code-cell} python
def plot_Yml(l, m):
    '''Visualizing spherical harmonics using sph_harm funcion from Scipy special function library
     Note that the name of angles is different from the notation adopted in QM textbooks!
     l: angular quantum number (0,1,2,...)
     m: magnetic quantum number (-l,...l)
     '''

    #Creade grid of phi and theta angles for ploting surface mesh
    phi, theta = np.linspace(0, np.pi, 100), np.linspace(0, 2*np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)

    #Calcualte spherical harmonic with given m and l
    Ylm = sph_harm_y(l, m, phi, theta) 
    R=abs(Ylm)
    
    # Let's normalize color scale
    fcolors    = Ylm.real
    fmax, fmin = fcolors.max(), fcolors.min()
    fcolors    = (fcolors - fmin)/(fmax - fmin)

    # Since we want to plot on cartesian reference frame we will use cartesian coordiniates x, y, z using R as the absolute value of Yml
    # Try a plot without R part. 
    fig = go.Figure(data=[go.Surface(x=R*np.sin(phi) * np.cos(theta), 
                                     y=R*np.sin(phi) * np.sin(theta), 
                                     z=R*np.cos(phi), 
                                     surfacecolor=fcolors,
                                     colorscale='balance')])

    # Show the plot
    fig.update_layout(title=fr'$Y_{l, m}$', autosize=False,
                      width=700, height=700,
                      margin=dict(l=65, r=50, b=65, t=90)
    )
    fig.show()
```

```{code-cell} python
plot_Yml(l=1, m=0)
```

#### 3. Describing the normalized probability as wavefunction squared $|\psi _{nlm}(r,\theta ,\varphi)|^2$ 

$$\psi_{nlm} = R_{nl}(r) \cdot Y_{l}^{m}(\theta, \varphi)$$

```{code-cell} python

def normalized_wavefunction(n, 
                            l, 
                            m):

    '''Ψnlm(r,θ,φ) normalized wavefunction
    by definition of quantum numbers n, l, m and a bohr radius augmentation coefficient'''

    # Compute where radial function has nearly decayed to zero and determine cutoff distance
    r     = np.linspace(0, 500, 10000)
    pr = radial_function(r, n, l)**2 * r**2 * (r[1]-r[0])
    max_r = r[ np.where(np.cumsum(pr) >0.95)[0][0] ] 

    # Set coordinates grid to assign a certain probability to each point (x, y) in the plane
    x = y = np.linspace(-max_r, max_r, 501)
    x, y = np.meshgrid(x, y)
    r = np.sqrt((x ** 2 + y ** 2))

    # Ψnlm(r,θ,φ) = Rnl(r).Ylm(θ,φ)
    psi = radial_function(r, n, l) * sph_harm_y(l, m, np.arctan(x / (y + 1e-7)), 0)
    psi_sq = np.abs(psi)**2

    # Plot orbitals
    fig, ax = plt.subplots()
    ax.contour(psi_sq, 40, cmap='RdBu', extent=[-max_r, max_r,-max_r, max_r])
    ax.set_title(r'$|\psi_{{({0}, {1}, {2})}}|^2$'.format(n, l, m), fontsize=15)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_xlim(-max_r, max_r)
    ax.set_ylim(-max_r, max_r)
```

```{code-cell} python
normalized_wavefunction(n=3, 
                            l=2, 
                            m=1)
```

### Full Atomic orbitals in 3D

```{code-cell} python
xyz = np.linspace(-10, 10, 51)
x,y,z = np.meshgrid(xyz, xyz, xyz, sparse=False)

r = np.sqrt(x**2 + y**2 + z**2)
phi = np.arctan2(y+1e-10, x)
theta = np.where( np.isclose(r, 0.0), np.zeros_like(r), np.arccos(z/r) )

n,l,m=4,1,0
psi = radial_function(r, n, l) * sph_harm_y(l, m, theta, phi) 
```

```{code-cell} python
fig= go.Figure(data=go.Isosurface(
    x=x.flatten(),
    y=y.flatten(),
    z=z.flatten(),
    value=abs(psi).flatten(),
    colorscale='RdBu',
    isomin=-.75*abs(psi).max(),
    isomax=.75*abs(psi).max(),
    surface_count=6,
    opacity=0.5,
    caps=dict(x_show=False,y_show=False,z_show=False)
))

fig.show()
```

### Explore any orbital in 3D

Pick quantum numbers and rotate the resulting orbital. Blue and red surfaces are the positive and negative lobes of the wavefunction.

```{marimo} python
:hide-code: true

n_o = mo.ui.slider(1, 5, step=1, value=3, show_value=True, label="n")
n_o
```

```{marimo} python
:hide-code: true

l_o = mo.ui.dropdown(
    options={str(v): v for v in range(n_o.value)}, value=str(n_o.value - 1), label="l"
)
l_o
```

```{marimo} python
:hide-code: true

m_o = mo.ui.dropdown(
    options={str(v): v for v in range(-l_o.value, l_o.value + 1)}, value="0", label="m"
)
m_o
```

```{marimo} python
:hide-code: true

l_o_eff = l_o.value
m_o_eff = m_o.value

ext = 6.0 * n_o.value
g_o = np.linspace(-ext, ext, 45)
x_o, y_o, z_o = np.meshgrid(g_o, g_o, g_o, indexing="ij")
r_o = np.sqrt(x_o**2 + y_o**2 + z_o**2)
phi_o = np.arctan2(y_o + 1e-10, x_o)
theta_o = np.where(np.isclose(r_o, 0.0), 0.0, np.arccos(z_o / (r_o + 1e-12)))

psi_o = (radial_m(r_o, n_o.value, l_o_eff) * sph_harm_y(l_o_eff, m_o_eff, theta_o, phi_o)).real
amp_o = 0.5 * np.abs(psi_o).max()

fig_o = go.Figure(data=go.Isosurface(
    x=x_o.flatten(), y=y_o.flatten(), z=z_o.flatten(), value=psi_o.flatten(),
    colorscale="RdBu", isomin=-amp_o, isomax=amp_o, surface_count=2,
    showscale=False, caps=dict(x_show=False, y_show=False, z_show=False),
))
fig_o.update_layout(
    scene=dict(aspectmode="data"),
    width=680, height=480,
    title_text=f"orbital ({n_o.value}, {l_o_eff}, {m_o_eff})",
)
fig_o
```
