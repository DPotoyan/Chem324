---
kernelspec:
  name: python3
  display_name: Python 3
---

# Trigonometry and Complex Numbers

:::{note} **What you will learn**

- **Trigonometry as geometry on the unit circle.** Sine and cosine are the coordinates of a point rotating around a circle of radius one.
- **The key identities.** The Pythagorean identity, angle-sum formulas, and power-reduction formulas that recur throughout quantum mechanics.
- **Complex numbers as 2D numbers.** A complex number carries a real and an imaginary part and lives in a plane.
- **Euler's formula.** $e^{i\phi} = \cos\phi + i\sin\phi$ fuses trigonometry and exponentials into one object and is the single most useful identity in the course.
- **Polar form, conjugation, and rotation.** Multiplying complex numbers rotates and scales them, and the conjugate reflects across the real axis.
:::

Trigonometry and complex numbers are two views of the same thing: rotation in a plane. Waves, oscillations, and quantum phases all live here, and Euler's formula is the bridge that connects them. We treat them together because in quantum mechanics you almost never use one without the other.

## Trigonometry

### Sine and cosine on the unit circle

Take a point on a circle of radius $1$ and rotate it counterclockwise by an angle $\theta$ (measured in **radians**, where a full turn is $2\pi$). Its coordinates are, by definition,

$$
x = \cos\theta, \qquad y = \sin\theta.
$$

Cosine is the horizontal coordinate, sine the vertical one, and the tangent $\tan\theta = \sin\theta/\cos\theta$ is the slope of the radius.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

theta = np.deg2rad(50)
t = np.linspace(0, 2 * np.pi, 400)

fig, ax = plt.subplots(figsize=(5.5, 5.5))
ax.plot(np.cos(t), np.sin(t), 'k', lw=1.5)           # unit circle
ax.plot([0, np.cos(theta)], [0, np.sin(theta)], color='#2e4057', lw=2)  # radius
ax.plot([np.cos(theta), np.cos(theta)], [0, np.sin(theta)], color='#66a182', lw=2, label=r'$\sin\theta$')
ax.plot([0, np.cos(theta)], [0, 0], color='#d1495b', lw=2, label=r'$\cos\theta$')
ax.plot(np.cos(theta), np.sin(theta), 'ko', ms=6)

ax.annotate(r'$(\cos\theta,\ \sin\theta)$', (np.cos(theta), np.sin(theta)),
            textcoords='offset points', xytext=(8, 8), fontsize=11)
ax.axhline(0, color='gray', lw=0.6)
ax.axvline(0, color='gray', lw=0.6)
ax.set_aspect('equal')
ax.set_xlim(-1.3, 1.5)
ax.set_ylim(-1.3, 1.3)
ax.legend(loc='lower left', fontsize=10)
ax.set_title(r'Fig.1 Sine and cosine as coordinates on the unit circle ($\theta=50^\circ$)')
plt.tight_layout()
plt.show()
```

As $\theta$ runs around the circle, the two coordinates trace out the familiar waves: cosine starts at $1$, sine starts at $0$, and each is the other shifted by a quarter turn.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 400)
fig, ax = plt.subplots(figsize=(7, 3.2))
ax.plot(t, np.cos(t), color='#d1495b', lw=2, label=r'$\cos\theta$')
ax.plot(t, np.sin(t), color='#66a182', lw=2, label=r'$\sin\theta$')
ax.axhline(0, color='gray', lw=0.6)
ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi])
ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
ax.set_xlabel(r'$\theta$ (radians)')
ax.legend(fontsize=10, loc='upper right')
ax.set_title('Fig.2 Cosine and sine as functions of the angle, offset by a quarter turn')
plt.tight_layout()
plt.show()
```

### Key identities

Because the point lies on a unit circle, its coordinates always satisfy the **Pythagorean identity**:

:::{important} **Pythagorean identity**

$$
\cos^2\theta + \sin^2\theta = 1
$$
:::

The identities you will reach for most often are the **angle-sum** and **power-reduction** formulas:

$$
\sin(A \pm B) = \sin A\cos B \pm \cos A\sin B, \qquad
\cos(A \pm B) = \cos A\cos B \mp \sin A\sin B,
$$

$$
\sin^2\theta = \tfrac{1}{2}(1-\cos 2\theta), \qquad
\cos^2\theta = \tfrac{1}{2}(1+\cos 2\theta).
$$

For small angles (in radians), the first terms of the Taylor series give the approximations $\sin\theta \approx \theta$ and $\cos\theta \approx 1 - \tfrac{1}{2}\theta^2$, which are what let us linearize a pendulum or a vibrating bond near equilibrium.

Rather than memorize the whole table of identities, it is easier to derive them from Euler's formula, which we build next.

## Complex numbers

### Complex numbers live in 2D

A complex number $z$ is a two-dimensional number: it needs two components for its full specification. They arise the moment we ask for the roots of a simple polynomial. The equation

$$
x^2 + 1 = 0 \quad\Longrightarrow\quad x_{1,2} = \pm\sqrt{-1} = \pm i
$$

has no real solution, so we extend the real line $\mathbb{R}$ into the complex plane $\mathbb{C}$ by introducing the **imaginary unit** $i$, defined solely by

$$
i^2 = -1.
$$

:::{figure} images/SumNums.png
:alt: Complex numbers live in 2D
:width: 40%

Fig.3 A complex number needs a real and an imaginary component to be fully specified, so it lives in a plane.
:::

:::{tip} **The quadratic formula and the discriminant**
:class: dropdown

For $ax^2 + bx + c = 0$ the roots are $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. The **discriminant** $\Delta = b^2 - 4ac$ decides their nature: $\Delta > 0$ gives two real roots, $\Delta = 0$ a repeated real root, and $\Delta < 0$ two complex conjugate roots.
:::

### Cartesian representation

:::{important} **Cartesian form**

$$
z = x + iy
$$

- $x = \operatorname{Re}(z)$ is the real part,
- $y = \operatorname{Im}(z)$ is the imaginary part.
:::

:::{note} **Example: Identify real and imaginary parts**

For $z_1 = 3 + 2i$, $z_2 = -2i$, and $z_3 = 1.1$:

- $\operatorname{Re}(z_1) = 3$, $\operatorname{Im}(z_1) = 2$
- $\operatorname{Re}(z_2) = 0$, $\operatorname{Im}(z_2) = -2$
- $\operatorname{Re}(z_3) = 1.1$, $\operatorname{Im}(z_3) = 0$
:::

### Polar representation and Euler's formula

Instead of horizontal and vertical parts, we can locate $z$ by its distance from the origin $r$ and its angle $\phi$. From the unit-circle picture, $x = r\cos\phi$ and $y = r\sin\phi$, so

$$
z = x + iy = r(\cos\phi + i\sin\phi).
$$

The magic step is **Euler's formula**, which collapses the parenthesis into an exponential:

:::{important} **Euler's formula**

$$
e^{i\phi} = \cos\phi + i\sin\phi
\qquad\Longrightarrow\qquad
z = r\,e^{i\phi}
$$

Here $r = \sqrt{x^2 + y^2}$ is the magnitude and $\phi$ is the phase angle.
:::

:::{tip} **Proof of Euler's formula from Taylor series**
:class: dropdown

Expand $e^{ix}$ and collect powers of $i$:

$$
e^{ix} = 1 + ix - \frac{x^2}{2!} - i\frac{x^3}{3!} + \frac{x^4}{4!} + \cdots
= \left(1 - \frac{x^2}{2!} + \cdots\right) + i\left(x - \frac{x^3}{3!} + \cdots\right).
$$

The two series are exactly $\cos x$ and $\sin x$, so $e^{ix} = \cos x + i\sin x$.
:::

The plot below shows why polar form is natural: the same complex number is one dot in the plane, described equally well by $(x, y)$ or by $(r, \phi)$.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

z = 2 + 1.5j
r, phi = np.abs(z), np.angle(z)

fig, ax = plt.subplots(figsize=(5.5, 5))
ax.annotate('', xy=(z.real, z.imag), xytext=(0, 0),
            arrowprops=dict(arrowstyle='->', color='#2e4057', lw=2))
arc = np.linspace(0, phi, 60)
ax.plot(0.6 * np.cos(arc), 0.6 * np.sin(arc), color='#d1495b', lw=1.5)
ax.plot([0, z.real], [z.imag, z.imag], '--', color='gray', lw=1)
ax.plot([z.real, z.real], [0, z.imag], '--', color='gray', lw=1)

ax.text(z.real + 0.1, z.imag + 0.1, fr'$z = {z.real:.0f}+{z.imag:.1f}i = {r:.2f}\,e^{{i\phi}}$', fontsize=11)
ax.text(0.7, 0.15, r'$\phi$', color='#d1495b', fontsize=13)
ax.text(z.real / 2, -0.25, r'$x=r\cos\phi$', color='gray', fontsize=9, ha='center')
ax.text(z.real + 0.05, z.imag / 2, r'$y=r\sin\phi$', color='gray', fontsize=9)

ax.axhline(0, color='black', lw=0.8)
ax.axvline(0, color='black', lw=0.8)
ax.set_xlim(-0.6, 3)
ax.set_ylim(-0.6, 2.4)
ax.set_aspect('equal')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_title('Fig.4 The same number in Cartesian (x, y) and polar (r, phi) form')
plt.tight_layout()
plt.show()
```

:::{note} **Example: Convert to polar form**

Write $z = -1 - 2i$ in polar form. Use `arctan2`, which picks the correct quadrant.

$$
r = \sqrt{(-1)^2 + (-2)^2} = \sqrt{5}, \qquad
\phi = \operatorname{arctan2}(-2, -1) \approx -2.034.
$$

Adding $2\pi$ gives an equivalent positive angle $\phi \approx 4.248$, so $z = \sqrt{5}\,e^{4.248\,i}$.
:::

### Multiplication is rotation

In polar form, multiplication becomes almost trivial: **magnitudes multiply and angles add**.

$$
(r_1 e^{i\phi_1})(r_2 e^{i\phi_2}) = r_1 r_2\, e^{i(\phi_1 + \phi_2)}.
$$

So multiplying by $e^{i\phi}$ **rotates** a number counterclockwise by $\phi$ without changing its length. Multiplying by $i = e^{i\pi/2}$ is a quarter-turn. This is the same rotation that trigonometry describes, now in one clean line of algebra.

:::{figure} images/ComplexHelix.gif
:alt: Euler's formula traced as a helix
:width: 60%

Fig.5 As $t$ increases, $e^{i\omega t}$ traces a helix. Its shadow on one wall is $\cos\omega t$ and on the other is $\sin\omega t$, so a single rotating phase carries both waves at once.
:::

### The complex conjugate

The **conjugate** flips the sign of the imaginary part, reflecting $z$ across the real axis:

:::{important} **Complex conjugate**

$$
\bar{z} = x - iy = r\,e^{-i\phi}
$$
:::

Multiplying a number by its conjugate rotates it back onto the real axis and returns a non-negative real number, the squared magnitude:

$$
|z|^2 = \bar{z}\,z = (x - iy)(x + iy) = x^2 + y^2 = r^2.
$$

This is exactly the operation that turns a quantum amplitude $\psi$ into a probability density $|\psi|^2 = \psi^*\psi$.

Taking sums and differences of $z$ and $\bar{z}$ recovers the trig functions as exponentials, a substitution that simplifies countless integrals:

$$
\cos\phi = \frac{e^{i\phi} + e^{-i\phi}}{2}, \qquad
\sin\phi = \frac{e^{i\phi} - e^{-i\phi}}{2i}.
$$

:::{tip} **Deriving the angle-sum identities from Euler's formula**
:class: dropdown

Expand $e^{i(\omega+\theta)} = e^{i\omega}e^{i\theta}$ and match real and imaginary parts:

$$
\cos(\omega+\theta) + i\sin(\omega+\theta)
= (\cos\omega + i\sin\omega)(\cos\theta + i\sin\theta).
$$

Multiplying out the right side and equating parts gives both angle-sum identities at once:

$$
\cos(\omega+\theta) = \cos\omega\cos\theta - \sin\omega\sin\theta, \qquad
\sin(\omega+\theta) = \sin\omega\cos\theta + \cos\omega\sin\theta.
$$

This is why we do not memorize the trig identities separately: they all fall out of one exponential rule. **De Moivre's theorem**, $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$, follows the same way from $(e^{i\theta})^n = e^{in\theta}$.
:::

:::{tip} **Where this shows up in chemistry**
:class: dropdown

Complex exponentials are the natural language of anything that oscillates or diffracts. In X-ray crystallography, each scattered wave is a complex number $A = |A|e^{i\phi}$, and the **structure factor** $F(\mathbf{h}) = \sum_j f_j\,e^{i\mathbf{h}\cdot\mathbf{r}_j}$ combines these amplitudes and phases to reconstruct electron density by an inverse Fourier transform. The hard part, the **phase problem**, is precisely that detectors measure $|F|$ but not the phase $\phi$ that the complex representation makes explicit.
:::

## Problems

### Problem 1: Multiplication in Cartesian form

Multiply $z_1 = 3 + 4i$ and $z_2 = 1 - 2i$.

:::{admonition} **Solution**
:class: dropdown solution

$$
(3 + 4i)(1 - 2i) = 3 - 6i + 4i - 8i^2 = 3 - 2i + 8 = 11 - 2i.
$$
:::

### Problem 2: Modulus

Find $|z|$ for $z = 7 + 24i$.

:::{admonition} **Solution**
:class: dropdown solution

$$
|z| = \sqrt{7^2 + 24^2} = \sqrt{49 + 576} = \sqrt{625} = 25.
$$
:::

### Problem 3: Division by the conjugate

Divide $z_1 = 3 + 4i$ by $z_2 = 1 - 2i$.

:::{admonition} **Solution**
:class: dropdown solution

Multiply numerator and denominator by $\bar{z}_2 = 1 + 2i$:

$$
\frac{(3+4i)(1+2i)}{(1-2i)(1+2i)} = \frac{-5 + 10i}{5} = -1 + 2i.
$$
:::

### Problem 4: Multiplication in polar form

Multiply $z_1 = 2e^{i\pi/6}$ and $z_2 = 3e^{i\pi/3}$.

:::{admonition} **Solution**
:class: dropdown solution

Magnitudes multiply, angles add:

$$
z_1 z_2 = 6\,e^{i(\pi/6 + \pi/3)} = 6\,e^{i\pi/2} = 6i.
$$
:::

### Problem 5: Cartesian to polar

Express $z = -4 + 4i$ in polar form.

:::{admonition} **Solution**
:class: dropdown solution

$$
r = \sqrt{(-4)^2 + 4^2} = 4\sqrt{2}, \qquad \phi = \frac{3\pi}{4}\ \text{(second quadrant)},
$$

so $z = 4\sqrt{2}\,e^{i 3\pi/4}$.
:::

### Problem 6: A famous identity

Use Euler's formula to evaluate $e^{i\pi}$.

### Problem 7: Trig from exponentials

Using $\cos\phi = \tfrac{1}{2}(e^{i\phi} + e^{-i\phi})$, show that $\cos^2\phi = \tfrac{1}{2}(1 + \cos 2\phi)$.

### Problem 8: Phase rotation

A quantum amplitude picks up a phase, $\psi \to e^{i\theta}\psi$. Show that the probability density $|\psi|^2$ is unchanged.
