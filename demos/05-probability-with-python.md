---
kernelspec:
  name: python3
  display_name: Python 3
---

# Probability with Python

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
```

```{code-cell} python
# Load the libs for numiercs and plotting
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#Load interactive widgets
import ipywidgets as widgets
from IPython.display import display

#If your screen has retina display this will increase resolution of plots
%config InlineBackend.figure_format = 'retina'
```

### Gaussian (Normal) distribution

Lets make gaussian distribution function with mu and sigma as parameters

$$p(x)= \frac{1}{2\pi \sigma^2} e^{-(x-\mu)^2/2\sigma^2}$$

```{code-cell} python
def p_gauss(x, mu, sigma):   # x is the variable over which p is distributed while sigma and mu are parameters affecting the distribution
    
    coeff = 1/(2* np.pi * sigma**2)
    
    return coeff * np.exp( -(x-mu)**2 / (2 * sigma**2) )
```

Now you can try different values of x, mu sigma. Probability is higher when x is closer to mu. 

```{code-cell} python

p_gauss(4, mu=0, sigma=1)
```

Better yet we can make a plot for different values of mu and sigma. Here we show that sigma indeed corresponds to the variance of the distirbution

```{code-cell} python
def plot_gauss(mu, sigma):
    
    x = np.linspace(-100,100,10000)  # The range is arbitrary. The point is to have value of mu inside the range.
    
    y = p_gauss(x,mu,sigma)      # Notice how we are using a function defined before instead of recreating again. 
    
    plt.plot(x, y, lw=5)
    
    plt.xlim([mu-3*sigma, mu+3*sigma]) # Showing values 3 standard deviation away from mean is enough to cover the function!
```

```{code-cell} python
# try plotting different values of mu and sigma
plot_gauss(0, 0.5)
plot_gauss(0, 1)
plot_gauss(0, 2)
```

Even better way to explore gaussian distirbution is via interactive widgets! 

```{code-cell} python
@widgets.interact(mu=(-10,10), sigma=(1,25))

def plot_gauss(mu, sigma):
    
    x = np.linspace(-100,100,10000)  
    
    y = p_gauss(x,mu,sigma)      
    
    plt.plot(x, y, lw=5)
```

```{marimo} python
:editor: true

rolls = np.random.default_rng(7).integers(1, 7, size=1000)
np.bincount(rolls)[1:]   # counts of faces 1..6
```

### Uniform distribution

$$p(x) = \frac{1}{b-a} \quad \text{for } x \in [a,b]$$

```{code-cell} python
def p_unif(x, a, b):  # Make sure b is greater than a! 
    
    return x / (x*(b-a))  
```

Test that probability is uniformly distirbuted for all values of x

```{code-cell} python
p_unif(1, 0, 10), p_unif(2, 0, 10),  p_unif(9, 0, 10)
```

Lets make a plot of uniform distribution

```{code-cell} python
def plot_unif(a, b):
    
    x = np.linspace(a,b,1000)  # The range needs to be inside a and b
    
    y = p_unif(x, a, b)       # Notice how we are using a function defined before instead of recreating again. 
    
    plt.plot(x, y, lw=5)
    
    plt.xlim([a, b])
```

```{code-cell} python
plot_unif(1,2)
plot_unif(1,2.5)
plot_unif(1,3)
```

```{code-cell} python
@widgets.interact(b=(2,20))

def plot_uniform(b):
    
    x = np.linspace(1,b,1000)  # We fixed a at 1 and only vary b
    
    y = p_unif(x, 1, b)       
    
    plt.plot(x, y, lw=5)
    
    plt.ylim([0,1])
```

### Try it live

:::{tip}
Draw random samples **in your browser**: move the slider to change the sample size, and edit the code to try other distributions (`rng.exponential(1.0, ...)`, `rng.uniform(-1, 1, ...)`).
:::


```{marimo} python
n_samples = mo.ui.slider(100, 10000, step=100, value=1000, show_value=True, label="number of samples")
n_samples
```

```{marimo} python
:editor: true

rng = np.random.default_rng(3240)
samples = rng.normal(0.0, 1.0, n_samples.value)
fig, ax = plt.subplots(figsize=(7, 3.5))
ax.hist(samples, bins=40, color="steelblue", edgecolor="white")
ax.set_title(f"{n_samples.value} samples, mean = {samples.mean():.3f}, std = {samples.std():.3f}")
fig
```
