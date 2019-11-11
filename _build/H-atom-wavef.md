---
redirect_from:
  - "/h-atom-wavef"
interact_link: content/H-atom-wavef.ipynb
kernel_name: python3
has_widgets: false
title: '5.3 Visualizing H atom wavefunctions'
prev_page:
  url: /Lec5-1
  title: '5.1 Schrodinger equation for Hydrogen atom'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%matplotlib inline
import matplotlib.pyplot as plt

from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

import scipy.integrate as integrate
import scipy.special as spe

# Increase resolution for retina display
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

# Load interactive widgets
import ipywidgets as widgets

```
</div>

</div>



## Hydrogen atom problem



In what follows we will adopt atomic units $a_0=1, \hbar=1, m_e=1, e=1$



## Plotting the radial part of wavefunction. The Laguerre polynomials



$$ R_{nl}(r) = \sqrt{\Big(\frac{2}{n a_0}\Big)^3 \frac{(n-l-1)!}{2n (n+l)!}} e^{-r/n a_0} \Big( \frac{2r}{na_0}\Big)^l  \cdot L^{2l+1}_{n-l-1} \Big(\frac{2r}{n a_0} \Big)$$



#### Step 1: Code up the function and do a basic plot



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def psi_R(r,n=1,l=0):

    coeff = np.sqrt((2.0/n)**3 * spe.factorial(n-l-1) /(2.0*n*spe.factorial(n+l)))
    
    laguerre = spe.assoc_laguerre(2.0*r/n,n-l-1,2*l+1)
    
    return coeff * np.exp(-r/n) * (2.0*r/n)**l * laguerre

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
r = np.linspace(0,100,1000)

plt.plot(r,psi_R(r,3,2)**2 * 4*np.pi * r**2, lw=3)

plt.xlabel('$r [a_0]$')

plt.ylabel('$R_{nl}(r)$')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
Text(0,0.5,'$R_{nl}(r)$')
```


</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](images/H-atom-wavef_7_1.png)

</div>
</div>
</div>



#### Step 2: Add an interactive widget



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

@widgets.interact(n = np.arange(1,10,1),l = np.arange(0,9,1))

def plot_radial(n,l):
    
    r =    np.linspace(0,250,10000)
    
    psi2 = psi_R(r,n,l)**2 * (4*np.pi*r**2)
    
    plt.plot(r,psi2, lw=2,color='red')
    

    ''' Styling the plot'''
    
    plt.xlabel('$r [a_0]$')

    plt.ylabel('$R_{nl}(r)$')
    
    rmax = n**2*(1+0.5*(1-l*(l+1)/n**2))
    
    plt.xlim([0, 2*rmax])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
interactive(children=(Dropdown(description='n', options=(1, 2, 3, 4, 5, 6, 7, 8, 9), value=1), Dropdown(descri…
```

</div>
</div>
</div>



## Plotting angular part of wavefunction: Spherical harmonics



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def psi_ang(phi,theta,l=0,m=0):
    
    sphHarm = spe.sph_harm(m,l,phi,theta)
    
    return sphHarm.real

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)

phi, theta = np.meshgrid(phi, theta)

Ylm = psi_ang(theta,phi,l=3,m=0)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Convert to Cartesian coordinates of the unit sphere, r=1
x = np.sin(phi) * np.cos(theta) * abs(Ylm)
y = np.sin(phi) * np.sin(theta) * abs(Ylm)
z = np.cos(phi) * abs(Ylm)

# Set up 3D plotting canvas
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')

# Calculate the spherical harmonic Y(l,m) and normalize to [0,1]

fcolors = (Ylm - Ylm.min())/(Ylm.max() - Ylm.min())

ax.plot_surface(x, y, z, facecolors=cm.seismic(fcolors))

# Turn off the axis planes
ax.set_axis_off()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](images/H-atom-wavef_13_0.png)

</div>
</div>
</div>



## Plot full atomic orbitlals



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def HFunc(r,theta,phi,n,l,m):
    '''
    Hydrogen wavefunction // a_0 = 1

    INPUT
        r: Radial coordinate
        theta: Polar coordinate
        phi: Azimuthal coordinate
        n: Principle quantum number
        l: Angular momentum quantum number
        m: Magnetic quantum number

    OUTPUT
        Value of wavefunction
    '''

    coeff = np.sqrt((2.0/n)**3 * spe.factorial(n-l-1) /(2.0*n*spe.factorial(n+l)))
    
    laguerre = spe.assoc_laguerre(2.0*r/n,n-l-1,2*l+1)
    
    sphHarm = spe.sph_harm(m,l,phi,theta) 

    return coeff * np.exp(-r/n) * (2.0*r/n)**l * laguerre * sphHarm

```
</div>

</div>

