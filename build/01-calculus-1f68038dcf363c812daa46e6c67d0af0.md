---
kernelspec:
  name: python3
  display_name: Python 3
---

# Calculus Essentials

:::{note} **What you will learn**

- **The derivative as a limit and as a slope.** The derivative measures the instantaneous rate of change of a function and the slope of its tangent line.
- **The rules of differentiation.** Constant multiple, sum, product, quotient, power, and chain rules let you differentiate almost any function you meet in chemistry.
- **The integral as accumulated area.** A definite integral is the limit of a sum of thin rectangles, giving the net area under a curve.
- **The fundamental theorem of calculus.** Differentiation and integration are inverse operations, and this theorem is the workhorse for evaluating integrals.
- **Techniques of integration.** Substitution, integration by parts, and trigonometric identities handle almost every integral in quantum mechanics.
:::

Calculus is the language of change. In quantum mechanics we differentiate wavefunctions to build momentum and energy operators, and we integrate them to compute probabilities and expectation values. This page collects the essentials, with a picture for the two ideas that matter most: the derivative as a slope, and the integral as an area.

## Differentiation

### The derivative as a slope

The derivative of $f$ at a point is the slope of the line tangent to the curve there. We build it from the slope of a **secant line** through two nearby points and then let those points merge:

:::{important} **The derivative as a limit**

$$
f'(x) = \lim_{h \to 0}\frac{f(x+h) - f(x)}{h}
$$
:::

As the spacing $h$ shrinks, the secant line pivots into the tangent line. The plot below shows this for $f(x) = x^2$ at $x = 1$: three secant lines with shrinking $h$ close in on the true tangent of slope $2$.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2
x0 = 1.0
x = np.linspace(-0.5, 2.5, 400)

fig, ax = plt.subplots(figsize=(6.5, 5))
ax.plot(x, f(x), 'k', lw=2, label=r'$f(x)=x^2$')

# Secant lines for shrinking h
for h, color in zip([1.0, 0.5, 0.2], ['#d1495b', '#edae49', '#66a182']):
    slope = (f(x0 + h) - f(x0)) / h
    sec = f(x0) + slope * (x - x0)
    ax.plot(x, sec, '--', color=color, lw=1.5, label=f'secant, h={h} (slope {slope:.1f})')
    ax.plot([x0, x0 + h], [f(x0), f(x0 + h)], 'o', color=color, ms=5)

# True tangent (slope 2)
ax.plot(x, f(x0) + 2 * (x - x0), color='#2e4057', lw=2, label='tangent (slope 2)')
ax.plot(x0, f(x0), 'ko', ms=6)

ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-1, 6)
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.legend(fontsize=8, loc='upper left')
ax.set_title('Fig.1 Secant lines converging to the tangent as h shrinks')
plt.tight_layout()
plt.show()
```

The derivative is also the **instantaneous rate of change**: if $f$ is position, $f'$ is velocity; if $f$ is concentration, $f'$ is reaction rate. A function is differentiable only where it is smooth, so no corners, jumps, or vertical tangents.

### Rules of differentiation

| Rule | Equation |
|-:|:-|
| Constant multiple | $\dfrac{d}{dx}[cf(x)] = c\,f'(x)$ |
| Sum and difference | $\dfrac{d}{dx}[f(x)\pm g(x)] = f'(x) \pm g'(x)$ |
| Product | $\dfrac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$ |
| Quotient | $\dfrac{d}{dx}\dfrac{f(x)}{g(x)} = \dfrac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}$ |
| Power | $\dfrac{d}{dx} x^n = n\,x^{n-1}$ |
| Chain | $\dfrac{d}{dx} f(g(x)) = f'(g(x))\cdot g'(x)$ |
| Linear approximation | $f(x) \approx f(a) + f'(a)(x-a)$ |

:::{tip} **The chain rule is the one you will use most**
:class: dropdown

Almost every wavefunction is a composition: $e^{-x^2}$, $\sin(kx)$, $e^{ikx}$. Each needs the chain rule. For $\dfrac{d}{dx} e^{-\alpha x^2}$, take the outer derivative $e^{u}$ times the inner derivative $-2\alpha x$, giving $-2\alpha x\, e^{-\alpha x^2}$.
:::

### Table of common derivatives

| Function $f(x)$ | Derivative $f'(x)$ | Function $f(x)$ | Derivative $f'(x)$ |
|-:|:-|-:|:---|
| $c$ | $0$ | $x^n$ | $nx^{n-1}$ |
| $e^{x}$ | $e^{x}$ | $\ln x$ | $\dfrac{1}{x}$ |
| $\sin x$ | $\cos x$ | $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ | $e^{ax}$ | $a\,e^{ax}$ |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ | $\arctan x$ | $\dfrac{1}{1+x^2}$ |

A few limits underlie these results: $\displaystyle\lim_{\theta\to 0}\frac{\sin\theta}{\theta}=1$, $\displaystyle\lim_{\theta\to 0}\frac{\cos\theta-1}{\theta}=0$, and the definition $\displaystyle\lim_{h\to 0}\frac{e^{h}-1}{h}=1$, which is exactly what makes $e^{x}$ its own derivative.


:::{tip} **Activity: differentiate like a quantum chemist**

The Gaussian $f(x) = e^{-a x^2}$ is the single most-differentiated function in this course (it is the harmonic oscillator ground state). Use the chain rule to find $f'(x)$ and $f''(x)$, and check where $f''(x) = 0$.
:::

:::{seealso} Solution
:class: dropdown

$f'(x) = -2ax\, e^{-ax^2}$ (chain rule), and the product plus chain rules give $f''(x) = (4a^2x^2 - 2a)\, e^{-ax^2}$. Setting $f'' = 0$ gives $x = \pm 1/\sqrt{2a}$: the inflection points, which for the oscillator ground state sit exactly at the classical turning points.
:::

## Integration

### The integral as accumulated area

A definite integral measures the net area between a curve and the $x$ axis. We approximate that area with a **Riemann sum** of $n$ rectangles and let $n\to\infty$:

:::{important} **The definite integral as a limit of sums**

$$
\int_a^b f(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^{n} f(x_i)\,\Delta x,
\qquad \Delta x = \frac{b-a}{n}
$$
:::

The plot shows the rectangles filling the area under $f(x)=x^2$ on $[0,2]$ as $n$ grows from coarse to fine. The exact area is $\int_0^2 x^2\,dx = 8/3 \approx 2.667$.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: x**2
a, b = 0, 2
xs = np.linspace(a, b, 400)

fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), sharey=True)
for ax, n in zip(axes, [4, 8, 32]):
    edges = np.linspace(a, b, n + 1)
    mids = 0.5 * (edges[:-1] + edges[1:])   # midpoint rule
    dx = (b - a) / n
    approx = np.sum(f(mids) * dx)
    ax.bar(mids, f(mids), width=dx, align='center',
           color='#66a182', edgecolor='white', alpha=0.7)
    ax.plot(xs, f(xs), 'k', lw=2)
    ax.set_title(f'n = {n},  sum = {approx:.3f}', fontsize=10)
    ax.set_xlabel('x')
axes[0].set_ylabel('f(x)')
plt.suptitle('Fig.2 Riemann sums approaching the exact area 8/3 = 2.667 as n grows', y=1.04)
plt.tight_layout()
plt.show()
```

We can watch that convergence numerically:

```{code-cell} python
import numpy as np

f = lambda x: x**2
a, b = 0.0, 2.0
for n in [4, 16, 64, 256, 1024]:
    x = np.linspace(a, b, n + 1)
    mids = 0.5 * (x[:-1] + x[1:])
    approx = np.sum(f(mids) * (b - a) / n)
    print(f"n = {n:5d}   Riemann sum = {approx:.5f}")

exact = 8 / 3
print(f"\nexact value  = {exact:.5f}")
```

### Antiderivatives and the fundamental theorem

An **antiderivative** $F$ of $f$ satisfies $F'(x)=f(x)$. Because the derivative of a constant is zero, antiderivatives come as a family $F(x)+C$. The fundamental theorem of calculus ties the two halves of the subject together:

:::{important} **Fundamental theorem of calculus**

If $F$ is any antiderivative of a continuous $f$, then

$$
\int_a^b f(x)\,dx = F(b) - F(a).
$$
:::

This is why we rarely compute Riemann sums by hand: finding an antiderivative turns an infinite sum into a single subtraction.

### Table of indefinite integrals

| Function $f(x)$ | Antiderivative $F(x)$ | Function $f(x)$ | Antiderivative $F(x)$ |
|-:|:-|-:|:---|
| $x^n\ (n\neq -1)$ | $\dfrac{x^{n+1}}{n+1} + C$ | $\dfrac{1}{x}$ | $\ln\lvert x \rvert + C$ |
| $e^{x}$ | $e^{x} + C$ | $e^{ax}$ | $\dfrac{1}{a}e^{ax} + C$ |
| $\sin x$ | $-\cos x + C$ | $\cos x$ | $\sin x + C$ |
| $\dfrac{1}{x^2 + a^2}$ | $\dfrac{1}{a}\arctan\!\left(\dfrac{x}{a}\right) + C$ | $\dfrac{1}{\sqrt{a^2-x^2}}$ | $\arcsin\!\left(\dfrac{x}{a}\right) + C$ |

Useful properties: reversing the limits flips the sign, $\int_a^a f\,dx = 0$, and integrals are linear, $\int (cf \pm g)\,dx = c\int f\,dx \pm \int g\,dx$. For symmetric limits, an **even** function gives $\int_{-a}^{a} f\,dx = 2\int_0^a f\,dx$ while an **odd** function gives $\int_{-a}^{a} f\,dx = 0$, a shortcut that kills many quantum-mechanical integrals on sight.

### Techniques of integration

:::{important} **Substitution ($u = g(x)$)**

$$
\int f(g(x))\,g'(x)\,dx = \int f(u)\,du
$$
:::

:::{important} **Integration by parts**

$$
\int u\,dv = uv - \int v\,du
$$
:::

Integration by parts is the reverse of the product rule, and it is the standard tool for integrals like $\int x\,e^{-x}\,dx$ or $\int x\sin x\,dx$ that appear constantly in expectation-value calculations.

For products of sines and cosines, the power-reduction and product-to-sum identities do the work:

$$
\sin^2 x = \tfrac{1}{2}(1-\cos 2x), \qquad
\cos^2 x = \tfrac{1}{2}(1+\cos 2x),
$$

$$
\sin A\sin B = \tfrac{1}{2}\big[\cos(A-B)-\cos(A+B)\big], \qquad
\cos A\cos B = \tfrac{1}{2}\big[\cos(A-B)+\cos(A+B)\big].
$$

These are exactly the integrals that enforce **orthogonality** of particle-in-a-box wavefunctions.


:::{tip} **Activity: the two integrals you will use all semester**

Evaluate (a) $\int_0^L \sin^2(n\pi x/L)\, dx$ and (b) $\int_0^\infty x^2 e^{-x}\, dx$. Both reappear constantly: (a) normalizes every particle in a box state, (b) belongs to the Gamma-function family behind hydrogen atom integrals.
:::

:::{seealso} Solution
:class: dropdown

(a) With $\sin^2 u = \tfrac{1}{2}(1 - \cos 2u)$, the cosine integrates to zero over full half-periods, leaving $L/2$. That is why box wavefunctions carry the prefactor $\sqrt{2/L}$.

(b) Integrate by parts twice (or recognize $\Gamma(3) = 2!$): the answer is $2$. In general $\int_0^\infty x^n e^{-x} dx = n!$, the workhorse of radial hydrogen integrals.
:::

## Problems

### Problem 1: Differentiate a Gaussian

Differentiate $f(x) = e^{-\alpha x^2}$ with respect to $x$.

:::{admonition} **Solution**
:class: dropdown solution

Chain rule with outer $e^{u}$ and inner $u = -\alpha x^2$:

$$
f'(x) = e^{-\alpha x^2}\cdot(-2\alpha x) = -2\alpha x\,e^{-\alpha x^2}.
$$

Note the derivative is zero at $x=0$, the peak of the Gaussian.
:::

### Problem 2: Product and chain together

Differentiate $g(x) = x\sin(kx)$.

:::{admonition} **Solution**
:class: dropdown solution

Product rule, and the chain rule on $\sin(kx)$:

$$
g'(x) = \sin(kx) + x\cdot k\cos(kx).
$$
:::

### Problem 3: A normalization integral

Evaluate $\displaystyle\int_0^{L} \sin^2\!\left(\frac{\pi x}{L}\right)dx$.

:::{admonition} **Solution**
:class: dropdown solution

Use $\sin^2\theta = \tfrac{1}{2}(1-\cos 2\theta)$ with $\theta = \pi x/L$:

$$
\int_0^L \tfrac{1}{2}\left(1 - \cos\tfrac{2\pi x}{L}\right)dx
= \tfrac{1}{2}\left[x - \tfrac{L}{2\pi}\sin\tfrac{2\pi x}{L}\right]_0^L
= \frac{L}{2}.
$$

The sine term vanishes at both limits. This is the integral behind the particle-in-a-box normalization constant $\sqrt{2/L}$.
:::

### Problem 4: Integration by parts

Evaluate $\displaystyle\int_0^{\infty} x\,e^{-x}\,dx$.

:::{admonition} **Solution**
:class: dropdown solution

Let $u = x$, $dv = e^{-x}dx$, so $du = dx$ and $v = -e^{-x}$:

$$
\int_0^\infty x\,e^{-x}\,dx = \big[-x e^{-x}\big]_0^\infty + \int_0^\infty e^{-x}\,dx = 0 + 1 = 1.
$$
:::

### Problem 5: Symmetry shortcut

Without computing an antiderivative, evaluate $\displaystyle\int_{-a}^{a} x\,e^{-x^2}\,dx$.

:::{admonition} **Solution**
:class: dropdown solution

The integrand is **odd**: replacing $x\to -x$ flips its sign. The integral over symmetric limits is therefore $0$.
:::

### Problem 6: Verify a Riemann sum numerically

Modify the Riemann-sum code above to estimate $\int_0^{\pi}\sin x\,dx$ and compare with the exact value $2$.

### Problem 7: Chain rule on a plane wave

Differentiate $\psi(x) = e^{ikx}$ with respect to $x$, and again to find $\psi''(x)$.

### Problem 8: An expectation-value integral

Evaluate $\displaystyle\int_0^{\infty} x^2\,e^{-x}\,dx$ using integration by parts twice.
