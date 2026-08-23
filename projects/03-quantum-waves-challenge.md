---
kernelspec:
  name: python3
  display_name: Python 3
---

# Project 3: Quantum Waves

**Prerequisites**

- The [quantum waves demo](https://dpotoyan.github.io/Chem324/demo-quantum-waves) and
  the [particle in a box demo](https://dpotoyan.github.io/Chem324/demo-particle-in-a-box).
- The [Python and NumPy tutorials](https://dpotoyan.github.io/Chem324/python-basics)
  for the numerical tools.

**How to submit**: start with **File > Save a copy in Drive** so your work is saved
as you go. Add your code below each problem, using as many cells as you need. When you
are finished, run **Runtime > Restart and run all** to confirm the notebook works from
top to bottom, then use **File > Download > Download .ipynb** and upload that file to
Canvas.

```{code-cell} python
import numpy as np
import matplotlib.pyplot as plt
```

## Problem 1: Time independent particle in a box

Evaluate the following quantities using particle in a box wavefunctions:

- Probability of finding the particle in the middle third of the box
- Average momentum $\langle p \rangle$ and momentum squared $\langle p^2 \rangle$
- Average position $\langle x \rangle$ and position squared $\langle x^2 \rangle$
- Combine them to verify the uncertainty relation $\Delta x \, \Delta p \geq \hbar/2$

The example below shows the two numerical tools you need: derivatives with
[`np.gradient`](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html)
and integrals with
[`np.trapezoid`](https://numpy.org/doc/stable/reference/generated/numpy.trapezoid.html)
(the [trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule)).

```{code-cell} python
L = 1
N = 1000
x_ex = np.linspace(0, L, N)
f_ex = x_ex**2                       # try exp, sine, or a PIB wavefunction

dfdx = np.gradient(f_ex, x_ex)       # numerical derivative
int_f = np.trapezoid(dfdx, x_ex)     # numerical integral

fig_ex, ax_ex = plt.subplots(figsize=(7, 3.5))
ax_ex.plot(x_ex, f_ex, label=r"$f = x^2$")
ax_ex.plot(x_ex, dfdx, label=r"$df/dx = 2x$")
ax_ex.legend()
ax_ex.set_title(f"integral of df/dx over the box = {int_f:.4f}", fontsize=11)
fig_ex
```

```{code-cell} python
# TODO Problem 1: define psi_n(x), then compute the probabilities and averages
```

## Problem 2: Time dependent particle in a box

- Compute the time dependence of the average position $\langle x \rangle(t)$ for a
  particle in a box prepared as an equal-weight linear combination of the first two
  states.
- Show what happens when the second state is replaced by higher excited states.

```{code-cell} python
# TODO Problem 2: psi(x, t) = (psi_1 e^{-i E_1 t} + psi_n e^{-i E_n t}) / sqrt(2)
```

## Problem 3: Fourier transform and quantum mechanics

- Fourier transform the position wavefunction
  $\psi(x) = (2\pi\sigma_x^2)^{-1/2} \, e^{-x^2 / 2\sigma_x^2}$
  to obtain the momentum wavefunction $\psi(p)$.
- Show the uncertainty relation by varying $\sigma_x = 0.1, 1, 10$.

Two worked Fourier transform examples follow.

```{code-cell} python
x_fft = np.linspace(0, 2 * np.pi, 1000)
y_sin = np.sin(5 * x_fft)

Y_sin = np.fft.fft(y_sin)
freqs = np.fft.fftfreq(len(Y_sin))

fig_f1, (ax_f1a, ax_f1b) = plt.subplots(1, 2, figsize=(10, 3.5))
ax_f1a.plot(x_fft, y_sin)
ax_f1a.set_title("sine wave", fontsize=11)
ax_f1b.plot(freqs, np.abs(Y_sin))
ax_f1b.set_title("Fourier transform", fontsize=11)
fig_f1.tight_layout()
fig_f1
```

```{code-cell} python
y_gauss = np.exp(-((x_fft - np.pi) ** 2) / 0.1)
Y_gauss = np.fft.fft(y_gauss)

fig_f2, (ax_f2a, ax_f2b) = plt.subplots(1, 2, figsize=(10, 3.5))
ax_f2a.plot(x_fft, y_gauss)
ax_f2a.set_title("Gaussian pulse", fontsize=11)
ax_f2b.plot(freqs, np.abs(Y_gauss))
ax_f2b.set_title("Fourier transform", fontsize=11)
fig_f2.tight_layout()
fig_f2
```

```{code-cell} python
# TODO Problem 3: transform the Gaussian wavefunction for several sigma values
```
