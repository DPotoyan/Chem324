---
kernelspec:
  name: python3
  display_name: Python 3
---

# Bonus: Atomic Orbitals

```{code-cell} python
import  matplotlib.pyplot as plt
import numpy as np

%matplotlib inline
%config InlineBackend.figure_format = 'retina'
```

### Radial Part of Atomic Orbitals

$$ R_{nl}(r) = \sqrt{\Big(\frac{2}{n a_0}\Big)^3 \frac{(n-l-1)!}{2n (n+l)!}} e^{-r/n a_0} \Big( \frac{2r}{na_0}\Big)^l  \cdot L^{2l+1}_{n-l-1} \Big(\frac{2r}{n a_0} \Big)$$

**Problem-1**
- Using a few radial function of H-atom show that they are normalized and orthogonal. You can take a look at earlier demos on how to compute numerical integrals and derivatives using numpy functions. 
- Compute and plot probability to find electron withing first borh radius as a function of quantum number $n$. You will make use of Radial function in the demo notebook.
- Plot how the of 1/r depends on a quantum number n. Using radial functions to do computations numerically then compare the result to analytical expression which you can find in the book.

### Spherical part of Atomic Orbitals

$$
Y_{lm}(\theta,\phi) = \Theta_{lm}(\theta) \Phi_m (\phi) = \sqrt{\frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!} } P_{lm}(cos \theta) \cdot e^{im\phi}
$$

**Problem-2**

- Show that spherical harmonics are normalized and orthognal.
- Modfiy the function for plotting spherical harmonics in the demo which use the complex components to only use real parts. That way you will be able to generate familiar to chemist orbitals. Show that you can reproduce all five d orbitals and all three p orbitals.
- Visualize a linear combination of one $s$ and $p_z$ orbitals with equal weights.
- Visualize a linear combination of one $s$ and $p_x$ and $p_y$ orbitals with equal weights.
- Visualize a linear combination of one $s$ and all p orbitals with equal weights.
