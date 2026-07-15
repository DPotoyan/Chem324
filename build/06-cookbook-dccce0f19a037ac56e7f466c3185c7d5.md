---
kernelspec:
  name: python3
  display_name: Python 3
---

# Cookbook of Worked Examples

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/appendix-cookbook.ipynb)



### Using python to tame the math!

```{code-cell} python
# Hit enter to import all these goodies
import numpy as np  
import sympy as sp
import matplotlib.pyplot as plt
from ipywidgets import interact
import scipy  
from scipy.constants import physical_constants, hbar, h, c, k, m_e, Rydberg, e, N_A

%matplotlib inline
%config InlineBackend.figure_format='retina'
```

### Example-0: Use python as calculator

- Calculate energy and wavelength of photon that has frequency of $4\cdot 10^{14}$ Hz. You will have to use Planck's equation and wavelength-frequency conversion equations.

$$E= h\nu$$

$$\lambda = \frac{c}{\nu}$$

```{code-cell} python
#Start typing anything inside physica_constnats it will bring it up. 
physical_constants['Planck constant']
```

```{code-cell} python
# we also have most common constants ready to use. But you have to remember what are the units!
print(h)
```

```{code-cell} python
# e here tands for 10 and not exponent! exponent is defined via np.exp()
nu = 4e14

E = h*nu

print(E)
```

```{code-cell} python
#lambda is a protected word in pythong cant use it ugh
wavel = c/nu  

print(wavel)
```

### Example-1: Show orthogonality

- Show that wavefunctions $f_1 = sin(x)$ and $f_2=cos(x)$ are orthogonal on $(0, 2\pi)$ interval. That is you are going to show one of the most ubiquitous equalities in quantum mechanics

$$\int^{2\pi}_0 f_1(x) f_2(x)dx = 0$$

#### Numerical solution

```{code-cell} python
# Define the range of x values
x = np.linspace(0, 2 * np.pi, 1000)

# Calculate sin(x) and cos(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Calculate the numerical integral (dot product)
dot_product = np.trapezoid(y_sin * y_cos, x)

# Print the result
print(f"The numerical integral (dot product) of sin(x) * cos(x) over [0, 2π] is approximately: {dot_product:.4f}")
```

#### Symbolic solution

```{code-cell} python
# Define the symbolic variable
x = sp.symbols('x')

# Define sin(x) and cos(x)
sin_x = sp.sin(x)
cos_x = sp.cos(x)

# Calculate the symbolic integral of sin(x) * cos(x) over [0, 2π]
integral = sp.integrate(sin_x * cos_x, (x, 0, 2 * sp.pi))

# Print the result
print(f"The symbolic integral of sin(x) * cos(x) over [0, 2π] is: {integral}")
```

#### Visual solution

```{code-cell} python
def plot_orthogonality():
    '''Defining functions to encampuslate code is a good habit'''

    # Define the range of x values
    x = np.linspace(0, 2 * np.pi, 1000)
    
    # Calculate sin(x) and cos(x)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    
    # Plotting sin(x) and cos(x)
    plt.plot(x, y_sin, label='sin(x)')
    plt.plot(x, y_cos, label='cos(x)')
    
    # Fill the area between two horizontal curves (optional)
    plt.fill_between(x, y_sin * y_cos, alpha=0.3, color='gray', label='sin(x) * cos(x)')
    
    # Labels and title
    plt.xlabel('x')
    plt.ylabel('Function Value')
    plt.title('Orthogonality of sin(x) and cos(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Call the function
plot_orthogonality()
```
