---
redirect_from:
  - "/waves-1d"
interact_link: content/waves_1d.ipynb
kernel_name: python3
has_widgets: false
title: '2.2 Visualizing and animating waves.'
prev_page:
  url: /Lec5-Chem324
  title: '2.1 Mathematics of Waves'
next_page:
  url: /Lec6-Chem324
  title: '3.0 Schrodinger Equation.'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


## Visualizing and animating waves via python.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# First load the libs
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# a and load interactive widgets
import ipywidgets as widgets
from IPython.display import display

```
</div>

</div>



### Standing and traveling waves in 1D

We beging by plotting a simple periodic function
$$y = sin(kx)=sin\Big(2\pi \cdot \frac{x}{\lambda}\Big)$$



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
L=0.1            # Try different wavelengths

x = np.linspace(0.0, 1.0, 1000)

y = np.sin(2 * np.pi * x/L)

plt.plot(x, y)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[<matplotlib.lines.Line2D at 0x10e262b38>]
```


</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](images/waves_1d_3_1.png)

</div>
</div>
</div>



**Using python function to make wavelength exploration simple**



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def wave(L):
    
    x = np.linspace(0.0, 1.0, 1000)

    y = np.sin(2*np.pi * x/L)

    plt.plot(x, y)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
wave(0.1)
wave(0.4)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

{:.output_png}
![png](images/waves_1d_6_0.png)

</div>
</div>
</div>



### Adding an interactive widget to the plots



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
@widgets.interact(L=(0.1,4))

def wavef(L):
    
    x = np.linspace(0, +1., 1000)
    
    y = np.sin(2*np.pi * x/L)
    
    plt.plot(x, y)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
interactive(children=(FloatSlider(value=2.05, description='L', max=4.0, min=0.1), Output()), _dom_classes=('wi…
```

</div>
</div>
</div>



### Traveling wave



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
@widgets.interact(k=(1,10),t=(0,50.0))

def wavef2(k=1,t=0):
    v=1
    
    x = np.linspace(0, 1., 1000)
    
    y = np.sin(k*x-k*v*t) 
    
    plt.plot(x, y)
    
    plt.grid('on')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
interactive(children=(IntSlider(value=1, description='k', max=10, min=1), FloatSlider(value=0.0, description='…
```

</div>
</div>
</div>



## Normal modes



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
@widgets.interact(L=(0.1,4),n=(1,10))

def wavef(L,n=1):
    
    x = np.linspace(0, +1., 1000)
    
    y = np.sin(n*np.pi * x/L)
    
    plt.plot(x, y, lw=3, color='red')
    
    plt.grid('on')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_data_text}
```
interactive(children=(FloatSlider(value=2.05, description='L', max=4.0, min=0.1), IntSlider(value=1, descripti…
```

</div>
</div>
</div>

