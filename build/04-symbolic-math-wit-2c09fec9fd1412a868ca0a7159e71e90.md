---
kernelspec:
  name: python3
  display_name: Python 3
---

# Symbolic Math with SymPy

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "sympy",
  ]
---
```

```{marimo} python
:hide-code: true

import sympy as sp
```

- SymPy is the main library in the SciPy ecosystem for performing symbolic mathematics, and it is suitable for a wide audience from high school students to scientific researchers. 
- SymPy like a free, open source Mathematica substitute that is built on Python and is arguably more accessible in terms of cost and ease of acquisition. All of the following SymPy code relies on the following import which makes all of the SymPy modules available.
- Before SymPy will accept a variable as a symbol, the variable must first be defined as a SymPy symbol using the `symbols()` function. It takes one or more symbols at a time and attaches them to variables.
- If you plan on using Sympy and not mixing functions from other libraries we can importing everything from sympy with the following command and not worry about attaching sympy.F to every function F

```{code-cell} python

from sympy import *
```

```{code-cell} python
x, y, a, b, c, m = symbols('x y a b c m')

x
```

### Common SymPy Functions

SymPy contains an assortment of standard mathematical operators such as square root and trigonometric functions. A table of common functions is below. 

|      |       |        |        |        |
| :--: | :---: | :---:  | :---:  | :----: |   
|`Abs()`| `sin()` | `cos()` | `tan()`| `cot()` |
|`sec()` | `csc()` | `asin()` | `acos()` | `atan()` |
|`ceiling()` | `floor()` | `Min()` | `Max()` | `sqrt()` |

### Common Algebraic Methods

SymPy is quite capable at algebraic operations. Some of the most important ones are listed in the table below. We will focus on those

| Method | Description |
|:------:|:----------  |
|`sympy.expand()` | Expand polynomials |
|`sympy.factor()` | Factors polynomials |
|`sympy.simplify()` | Simplifies the expression |
|`sympy.solve()` | Equates the expression to zero and solves for the requested variable |
|`sympy.subs()`  | Substitutes a variable for a value, expression, or another variable |
|`sympy.series()`  | Expands functon in taylor series |

### Expand and factor

The first steps in an algebraic manipulation

```{code-cell} python

(x+1)*(x+2)*(x+3)
```

```{code-cell} python

expand((x+1)*(x+2)*(x+3))
```

The `expand` function takes a number of keywords arguments which we can tell the functions what kind of expansions we want to have performed. For example, to expand trigonometric expressions, use the `trig=True` keyword argument:

```{code-cell} python

sin(a+b)
```

```{code-cell} python

expand(sin(a+b), trig=True)
```

See `help(expand)` for a detailed explanation of the various types of expansions the `expand` functions can perform.

The opposite of product expansion is of course factoring. To factor an expression in SymPy use the `factor` function:

```{code-cell} python

factor(x**3 + 6 * x**2 + 11*x + 6)
```

### Simplification

```{code-cell} python

expr = 3*x**2 - 4*x - 15 / (x - 3)
```

```{code-cell} python
expr
```

```{code-cell} python
simplify(expr)
```

### Solving equations

```{code-cell} python
expr = x**2 + 1.4*x - 5.76
expr
```

```{code-cell} python
solve(expr)
```

### Complex numbers

The imaginary unit is denoted `I` in SymPy.

```{code-cell} python

1+1*I
```

```{code-cell} python

I**2
```

```{code-cell} python

(x * I + 1)**2
```

```{marimo} python
:editor: true

y = sp.symbols("y")
sp.solve(y**2 - 5*y + 6, y)   # sp is sympy, already imported on this page
```

### Taylor Series

Series expansion is also one of the most useful features of a CAS. In SymPy we can perform a series expansion of an expression using the series function:

```{code-cell} python

x = Symbol('x', real=True)
```

```{code-cell} python
series(exp(x), x)
```

- By default it expands the expression around  𝑥=0 , but we can expand around any value of  𝑥  by explicitly include a value in the function call:

```{code-cell} python
series(exp(x), x, 1)
```

And we can explicitly define to which order the series expansion should be carried out:

```{code-cell} python
series(exp(x), x, 1, 4)
```

### Differentiation

Differentiation is usually simple. Use the `diff` function. The first argument is the expression to take the derivative of, and the second argument is the symbol by which to take the derivative:

```{code-cell} python

y
```

```{code-cell} python

diff(y**2, x)
```

For higher order derivatives we can do:

```{code-cell} python

diff(y**2, x, x)
```

```{code-cell} python

diff(y**2, x, 2) # same as above
```

To calculate the derivative of a multivariate expression, we can do:

```{code-cell} python

x, y, z = symbols("x,y,z")
```

```{code-cell} python

f = sin(x*y) + cos(y*z)
```

$\frac{d^3f}{dxdy^2}$

```{code-cell} python

diff(f, x, 1, y, 2)
```

### Integration

Integration is done in a similar fashion:

```{code-cell} python

f
```

```{code-cell} python

integrate(f, x)
```

By providing limits for the integration variable we can evaluate definite integrals:

```{code-cell} python

integrate(f, (x, -1, 1))
```

and also improper integrals

```{code-cell} python

integrate(exp(-x**2), (x, -oo, oo))
```

Remember, `oo` is the SymPy notation for inifinity.

**Definite Integral example**

$$
\int_{0}^{\ln(4)} \frac{e^x \cdot d x} {\sqrt(e^{2x} + 9)}
$$

```{code-cell} python
integrate(exp(x) / sqrt(exp(2*x) + 9), (x, 0, log(4)))
```

### Sums and products

We can evaluate sums using the function `Sum`:

```{code-cell} python

n = Symbol("n")
```

```{code-cell} python

Sum(1/n**2, (n, 1, 10))
```

```{code-cell} python

Sum(1/n**2, (n,1, 10)).evalf()
```

```{code-cell} python

Sum(1/n**2, (n, 1, oo)).evalf()
```

Products work much the same way:

```{code-cell} python

Product(n, (n, 1, 10)) # 10!
```

```{marimo} python
:editor: true

u = sp.symbols("u")
sp.diff(sp.exp(-u**2) * sp.sin(u), u)   # differentiate anything
```

### Physics functions

- [Sympy Physics functions](https://docs.sympy.org/latest/reference/public/physics/index.html)

SymPy contains several physics functions. In this section, we will be working with the radial density functions ($\psi$) for hydrogen atomic orbitals. The squares of these functions ($\psi ^2$) provide the probability of finding an electron with respect to distance from the nucleus. While these equations are available in various textbooks, SymPy provides a `physics` module with a `R_nl()` function for generating these equations based on the principle (*n*) quantum number, angular (*l*) quantum number, and the atomic number (*Z*). For example, to generate the function for the 2p orbital of hydrogen, *n* = 2, *l* = 1, and *Z* = 1.

```{code-cell} python

import sympy
from sympy.physics.hydrogen import R_nl, Psi_nlm, E_nl

r, phi, theta = sympy.symbols('r, phi, theta')
```

```{code-cell} python
Psi_nlm(n=3,
        l=2,
        m=0,
        r=r,
        phi=phi,
        theta=theta,
        Z=1)
```

```{code-cell} python
R_nl(n=2,
     l=1,
     r=r,
     Z=1)
```

This provides the wavefunction equation with respect to the radius, *r*. We can also convert it to a Python function using the `sympy.lambdify()` method.

```{code-cell} python

R_21 = R_nl(n=2, l=1, r=r, Z=1)
f = sympy.lambdify(r, R_21, modules='numpy')
```

This function is now callable by providing a value for *r*.

```{code-cell} python

f(0.5)
```

```{code-cell} python

dR_21 = diff(R_21, r)
mx = float(solve(dR_21, r)[0])  # radius of maximum probability
integrate(R_21**2 * r**2, (r,0, mx)).evalf()
```

There is a 5.27% probability finding an electron between the nucleus and the radius of maximum probability. This is probably may be a bit surprising, but examination of the radial density plot reveals that the radius of maximum probabily is quite close to the nucleus with a significant amount of density beyond the maximum radius. Let's see the probability of finding an electron between 0 and 10 Bohrs from the nucleus.

```{code-cell} python

sympy.integrate(R_21**2 * r**2, (r,0,10)).evalf()
```

There is a 97.1% chance of finding the electron between 0 and 10 angstroms.

The SciPy library also includes functions in the `integrate` module for integrating mathematical functions.

### Example problem

As an example problem, the radius of maximum density can be found by taking the first derivative of the radial equation and solving for zero slope.

```{code-cell} python

from sympy.physics.hydrogen import R_nl

r = sympy.symbols('r', real=True )
```

```{code-cell} python
R_21 = R_nl(n=2, l=1, r=r, Z=1)

R_21
```

```{code-cell} python
dR_21 = diff(R_21, r, 1)
dR_21
```

```{code-cell} python
mx = float( solve(dR_21)[0] )
mx
```

The `solve()` function returns an array, so we need to index it to get the single value out. We can plot the radial density and the maximum density point to see if it worked.

```{code-cell} python

f = lambdify(r, R_21, modules='numpy')
```

```{code-cell} python

import numpy as np
import matplotlib.pyplot as plt

R = np.linspace(0,20,100)
plt.plot(R, f(R))
plt.plot(mx, f(mx), 'o')
plt.xlabel('Radius, $a_0$')
plt.ylabel('Probability Density');
```

The radius is in Bohrs ($a_0$) which is equal to approximately 0.53 angstroms.

### Exercises

1. Factor the following polynomial using SymPy: $x^2 + x - 6$

2.  Simplify the following mathematical expression using SymPy: $ z = 3x + x^2 + 2xy $

3. Expand the following expression using SymPy: $(x - 2)(x + 5)(x)$

4. The following is the equation for the work performed by a reversible, isothermal (i.e., constant T) expansion of a piston by a fixed quantity of gas.

    $$ w = \int_{v_i}^{v_f} -nRT \frac{1}{V}dV $$

    a) Using SymPy, integrate this expression symbolically for $V_i$ $\rightarrow$ $V_f$. Try having SymPy simplify the answer to see if there is a simpler form.

    b) Integrate the same express above for the expansion of 2.44 mol of He gas from 0.552 L to 1.32 L at 298 K. Feel free to use either SymPy or SciPy.

### Try it live

:::{tip}
A symbolic scratchpad that runs **in your browser**: edit the integral (or swap in `sp.diff`, `sp.series`, `sp.solve`) and press play. Results render as typeset math.
:::


```{marimo} python
:editor: true

x = sp.symbols("x")
sp.integrate(sp.sin(x) ** 2, (x, 0, sp.pi))   # try your own integral
```
