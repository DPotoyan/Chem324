---
kernelspec:
  name: python3
  display_name: Python 3
---

# Visualizing Spherical harmonics

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
from scipy.special import sph_harm_y
```

```{code-cell} python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm, colors
```

### Import [spherical harmonics](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.sph_harm.html#scipy.special.sph_harm) from scipy [special functions collection](https://docs.scipy.org/doc/scipy/reference/special.html)

```{code-cell} python
#Import spherical harmonics
from scipy.special import sph_harm_y
```

$$
Y_{lm}(\phi,\theta) = \sqrt{\frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!} } P_{lm}(cos \phi) \cdot e^{im\theta}
$$

Notice that scipy adopts slightly different convenient of angles than what is adopted in textbook. 

- **m array_like**
Order of the harmonic (int); must have |m| <= l.

- **l array_like**
Degree of the harmonic (int); must have l >= 0. 

- **$\theta$ array_like**
Azimuthal (longitudinal) coordinate; must be in $[0, 2\pi]$.

- **$\phi$ array_like**
Polar (colatitudinal) coordinate; must be in $[0, \pi]$.

```{code-cell} python
# Create 2D grid of angular variables

phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

# Convert to cartesian coordinates. r=const=1 for convenience
x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)
```

```{code-cell} python
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

m, l = 4, 4
Ylm  = sph_harm_y(l, m, phi, theta).real

#normalize color to [0,1] corresponding to magnitude of spherical harmonic

fcolors = (Ylm - Ylm.min())/(Ylm.max() - Ylm.min())

ax.plot_surface(x, y, z, facecolors=cm.seismic(fcolors))

# Turn off the axis planes
ax.set_axis_off()
```

```{marimo} python
:hide-code: true

l_s = mo.ui.slider(0, 8, step=1, value=3, show_value=True, label="l")
m_s = mo.ui.slider(-8, 8, step=1, value=0, show_value=True, label="m (clamped to |m| <= l)")
mo.hstack([l_s, m_s], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

m_eff5 = max(-l_s.value, min(l_s.value, m_s.value))
ph_m = np.linspace(0, np.pi, 90)
th_m = np.linspace(0, 2 * np.pi, 90)
ph_m, th_m = np.meshgrid(ph_m, th_m)
Y_m = sph_harm_y(l_s.value, m_eff5, ph_m, th_m).real

xs5 = np.sin(ph_m) * np.cos(th_m)
ys5 = np.sin(ph_m) * np.sin(th_m)
zs5 = np.cos(ph_m)
fc5 = (Y_m - Y_m.min()) / (Y_m.max() - Y_m.min() + 1e-12)

fig5 = plt.figure(figsize=(6, 6))
ax5 = fig5.add_subplot(111, projection="3d")
ax5.plot_surface(xs5, ys5, zs5, facecolors=plt.cm.seismic(fc5), rstride=1, cstride=1)
ax5.set_axis_off()
ax5.set_title(f"Y(l={l_s.value}, m={m_eff5}) on the unit sphere", fontsize=11)
fig5
```

### Interactive 3D surface with Plotly

Instead of coloring a unit sphere, we can let the radius itself carry the magnitude, $r = |Y_l^m|$, which produces the familiar lobed shapes of atomic orbitals. The same sliders above drive this figure; drag to rotate it.

```{marimo} python
:hide-code: true

r5 = np.abs(Y_m)
fig5b = go.Figure(data=[go.Surface(
    x=r5 * np.sin(ph_m) * np.cos(th_m),
    y=r5 * np.sin(ph_m) * np.sin(th_m),
    z=r5 * np.cos(ph_m),
    surfacecolor=Y_m, colorscale="RdBu", showscale=False,
)])
fig5b.update_layout(
    width=650, height=480, scene=dict(aspectmode="data"),
    title_text=f"r = |Y(l={l_s.value}, m={m_eff5})|",
)
fig5b
```

