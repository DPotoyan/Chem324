---
kernelspec:
  name: python3
  display_name: Python 3
---

# Calculus Essentials

:::{note} **What you will learn**

- **The derivative as a slope and as a step.** The derivative is the slope of the tangent line, and read the other way it is the recipe for stepping from $f(x)$ to a neighboring value $f(x+h)$.
- **The rules of differentiation.** Constant multiple, sum, product, quotient, power, and chain rules let you differentiate almost any function you meet in chemistry.
- **The integral as accumulated area.** A definite integral is the limit of a sum of thin rectangles, giving the net area under a curve.
- **The fundamental theorem of calculus.** Differentiation and integration are inverse operations, and this theorem is the workhorse for evaluating integrals.
- **Partial derivatives.** When a function depends on several variables, differentiate with respect to one while holding the others fixed. The chain rule then shows that any shape sliding at constant speed, $f(x - vt)$, obeys a simple relation between its space and time derivatives.
- **Techniques of integration.** Substitution, integration by parts, and trigonometric identities handle almost every integral in this course.
:::

Calculus is the language of change. Chemistry is full of quantities that vary with position, time, temperature, or pressure, and two questions come up again and again: how fast does a quantity change, which is a derivative, and how much of it accumulates, which is an integral. Later in the course the same two operations act on the functions that describe waves and, eventually, quantum states, so it pays to have them at your fingertips now. This page collects the essentials with a picture for each of the two ideas that matter most: the derivative as a slope and the integral as an area. In between sits a short section on partial derivatives, the small extension needed when a function depends on more than one variable, such as a wave $u(x,t)$ that depends on both position and time.

## Differentiation

### The derivative as a slope

The derivative of $f$ at a point is the slope of the line tangent to the curve there. We build it from the slope of a **secant line** through two nearby points and then let those points merge:

:::{important} **The derivative as a limit**

$$
f'(x) = \lim_{h \to 0}\frac{f(x+h) - f(x)}{h}
$$
:::

As the spacing $h$ shrinks, the secant line pivots into the tangent line. Drag the slider below for $f(x) = x^2$ at $x = 1$: the secant slope $2 + h$ closes in on the true tangent slope $2$.

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
plt.rcParams["figure.dpi"] = 150
```

```{marimo} python
:hide-code: true

h1 = mo.ui.slider(0.05, 1.5, step=0.05, value=1.0, show_value=True, label="spacing h")
h1
```

```{marimo} python
:hide-code: true

f1 = lambda x: x**2
x1 = 1.0
h = h1.value
xx1 = np.linspace(-0.5, 2.8, 400)
slope1 = (f1(x1 + h) - f1(x1)) / h
pred1 = f1(x1) + 2 * (x1 + h - x1)          # tangent-line prediction of f(x1 + h)

fig1, ax1 = plt.subplots(figsize=(6.5, 5))
ax1.plot(xx1, f1(xx1), "k", lw=2, label=r"$f(x)=x^2$")
ax1.plot(xx1, f1(x1) + slope1 * (xx1 - x1), "--", color="#d1495b", lw=1.8,
         label=f"secant, slope {slope1:.2f}")
ax1.plot(xx1, f1(x1) + 2 * (xx1 - x1), color="#2e4057", lw=2, label="tangent, slope 2")
ax1.plot([x1, x1 + h], [f1(x1), f1(x1 + h)], "o", color="#d1495b", ms=6)
ax1.plot(x1, f1(x1), "ko", ms=7)
ax1.plot(x1 + h, pred1, "s", color="#2e4057", ms=6, label=r"step prediction $f(x)+f'(x)\,h$")
ax1.plot([x1 + h, x1 + h], [pred1, f1(x1 + h)], color="#66a182", lw=2.5)
ax1.text(x1 + h + 0.05, 0.5 * (pred1 + f1(x1 + h)), f"error {h**2:.3f}", color="#66a182", fontsize=9, va="center")
ax1.set_xlim(-0.5, 2.8)
ax1.set_ylim(-1, 7)
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.legend(fontsize=8, loc="upper left")
ax1.set_title(f"Fig.1 Secant for h = {h:.2f}: slope {slope1:.2f} vs tangent slope 2")
plt.gcf()
```

The derivative is also the **instantaneous rate of change**: if $f$ is position, $f'$ is velocity; if $f$ is concentration, $f'$ is reaction rate. A function is differentiable only where it is smooth, so no corners, jumps, or vertical tangents.

### The derivative as a step

Read the definition backwards and it becomes a recipe for moving along the curve. For a small step $h$,

$$
f(x + h) \approx f(x) + f'(x)\,h .
$$

Knowing the value and the slope at one position is enough to predict the value at a neighboring position: the derivative is the **rate at which $f$ responds to a shift** in $x$. The green bar in the slider figure measures how far this prediction misses the true $f(x+h)$. For $x^2$ the miss is exactly $h^2$, so halving the step quarters the error, and in the limit the prediction is perfect. That is what "linear approximation" means, and it is why a tangent line is the best straight-line stand-in for a curve near a point.

:::{tip} **Taylor series: the derivative generates shifts**
:class: dropdown

Keep going with higher derivatives and the approximation becomes exact for any smooth function:

$$
f(x + a) = f(x) + a\,f'(x) + \frac{a^2}{2!}\,f''(x) + \frac{a^3}{3!}\,f'''(x) + \cdots
= \sum_{n=0}^{\infty} \frac{a^n}{n!}\,\frac{d^n f}{dx^n}.
$$

The sum has the same shape as the exponential series, which is why one writes $f(x + a) = e^{a\, d/dx} f(x)$: exponentiating the derivative **translates** a function by $a$. Later in the course the operator $d/dx$ reappears, dressed as $-i\hbar\,d/dx$, as momentum, and this formula is the deep reason momentum and translation belong together.
:::

### Rules of differentiation

:::{note} **Six Key Derivative Rules**

1. **Constant multiple**: if $h(x) = c\, f(x)$, then

    $$\frac{dh}{dx} = c\, \frac{df}{dx}$$

2. **Sum and difference**: if $h(x) = f(x) \pm g(x)$, then

    $$\frac{dh}{dx} = \frac{df}{dx} \pm \frac{dg}{dx}$$

3. **Power rule**:

    $$\frac{d}{dx}\, x^n = n\, x^{n-1}$$

4. **Product rule**: if $h(x) = f(x)\, g(x)$, then

    $$\frac{dh}{dx} = \frac{df}{dx}\, g + f\, \frac{dg}{dx}$$

    Equivalently, $h'(x) = f'(x)g(x) + f(x)g'(x)$.

5. **Quotient rule**: if $h(x) = \dfrac{f(x)}{g(x)}$, then

    $$\frac{dh}{dx} = \frac{f'(x)\,g(x) - f(x)\,g'(x)}{g(x)^2}$$

6. **Chain rule**: if $h(x) = f(g(x))$, then

    $$\frac{dh}{dx} = \frac{df}{dg} \cdot \frac{dg}{dx}$$

    Equivalently, $h'(x) = f'(g(x))\, g'(x)$.

Bonus, used everywhere in approximations: the **linear approximation** $f(x) \approx f(a) + f'(a)(x - a)$.
:::

### Example: a product with a composition inside

Differentiate $f(x) = x^2 e^{-\alpha x^2}$. Attempt this before peeking at the solution. (Functions of exactly this shape describe vibrating molecules later in the course.)

:::{seealso} Solution
:class: dropdown

Split into $x^2$ times $e^{-\alpha x^2}$ and apply the **product rule**:

$$\frac{df}{dx} = \underbrace{2x}_{(x^2)'}\, e^{-\alpha x^2} + x^2\, \underbrace{(-2\alpha x)\, e^{-\alpha x^2}}_{(e^{-\alpha x^2})' \text{ by the chain rule}}
= 2x\, (1 - \alpha x^2)\, e^{-\alpha x^2}.$$

The chain rule handled the inner function $g(x) = -\alpha x^2$ inside the exponential. Setting $f'(x) = 0$ gives $x = 0$ and $x = \pm 1/\sqrt{\alpha}$: a minimum at the origin flanked by two maxima.
:::

:::{tip} **The chain rule is the one you will use most**
:class: dropdown

Almost every function you will meet in this course is a composition: $e^{-x^2}$, $\sin(kx)$, $e^{ikx}$. Each needs the chain rule. For $\dfrac{d}{dx} e^{-\alpha x^2}$, take the outer derivative $e^{u}$ times the inner derivative $-2\alpha x$, giving $-2\alpha x\, e^{-\alpha x^2}$.
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

The Gaussian $f(x) = e^{-a x^2}$ is the single most-differentiated function in this course. Use the chain rule to find $f'(x)$ and $f''(x)$, and check where $f''(x) = 0$.
:::

:::{seealso} Solution
:class: dropdown

$f'(x) = -2ax\, e^{-ax^2}$ (chain rule), and the product plus chain rules give $f''(x) = (4a^2x^2 - 2a)\, e^{-ax^2}$. Setting $f'' = 0$ gives $x = \pm 1/\sqrt{2a}$: the inflection points where the bell curve changes from concave down to concave up. Remember this pair of points; when the Gaussian returns as a vibrational state they turn out to be the classical turning points.
:::

## Functions of several variables

### Partial derivatives

Most quantities in chemistry depend on more than one variable. The pressure of an ideal gas depends on both volume and temperature, $P(V,T) = nRT/V$, and the displacement of a plucked guitar string depends on where you look and when, $u(x,t)$. Graphically, a function of two variables $f(x,y)$ is a surface over the $xy$ plane, and a surface has no single slope: it can be steep along $x$ and nearly flat along $y$.

The fix is to vary one variable at a time. The **partial derivative** of $f$ with respect to $x$ is the ordinary derivative along $x$ with every other variable frozen:

:::{important} **Partial derivatives**

$$
\frac{\partial f}{\partial x} = \lim_{h \to 0}\frac{f(x+h,\,y) - f(x,\,y)}{h},
\qquad
\frac{\partial f}{\partial y} = \lim_{h \to 0}\frac{f(x,\,y+h) - f(x,\,y)}{h}
$$

The curly $\partial$ announces that the other variables are held constant. Common shorthands are $f_x$ and $f_y$; thermodynamics names the frozen variable explicitly, as in $\left(\partial P/\partial V\right)_T$.
:::

Nothing new is needed to compute one: treat the other variables as constants and apply the rules of the previous section. Geometrically, slicing the surface with the plane $y = y_0$ leaves an ordinary curve, and $\partial f/\partial x$ is the slope of that curve.

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: 4 - x**2 - y**2 / 4
fx = lambda x, y: -2 * x
fy = lambda x, y: -y / 2
x0, y0 = 1.0, 1.0

X, Y = np.meshgrid(np.linspace(-2, 2, 60), np.linspace(-3, 3, 60))
fig = plt.figure(figsize=(7.5, 5.5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, f(X, Y), color='lightgray', alpha=0.35, linewidth=0)

xs = np.linspace(-2, 2, 100)
ys = np.linspace(-3, 3, 100)
ax.plot(xs, np.full_like(xs, y0), f(xs, y0), color='#d1495b', lw=2.5,
        label=r'slice $y = 1$: slope is $\partial f/\partial x$')
ax.plot(np.full_like(ys, x0), ys, f(x0, ys), color='#66a182', lw=2.5,
        label=r'slice $x = 1$: slope is $\partial f/\partial y$')

tx = np.array([x0 - 0.8, x0 + 0.8])
ax.plot(tx, np.full_like(tx, y0), f(x0, y0) + fx(x0, y0) * (tx - x0), '--', color='#d1495b', lw=1.5)
ty = np.array([y0 - 1.2, y0 + 1.2])
ax.plot(np.full_like(ty, x0), ty, f(x0, y0) + fy(x0, y0) * (ty - y0), '--', color='#66a182', lw=1.5)
ax.scatter([x0], [y0], [f(x0, y0)], color='k', s=40)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.view_init(elev=25, azim=-60)
ax.legend(loc='upper left', fontsize=8)
ax.set_title('Fig.2 Partial derivatives are slopes of slices through the surface')
plt.tight_layout()
plt.show()
```

For the hill $f(x,y) = 4 - x^2 - y^2/4$ in the figure, $\partial f/\partial x = -2x$ and $\partial f/\partial y = -y/2$. At the marked point $(1, 1)$ the surface drops four times faster along $x$ than along $y$, which is why the red tangent is steeper than the green one.

:::{note} **Example: partial derivatives by the ordinary rules**

For $f(x,y) = x^2 y + \sin(xy)$:

- Holding $y$ fixed, the power rule and the chain rule give $\dfrac{\partial f}{\partial x} = 2xy + y\cos(xy)$.
- Holding $x$ fixed, $\dfrac{\partial f}{\partial y} = x^2 + x\cos(xy)$.

In each line the frozen variable rides along exactly like the constant $\alpha$ did in $e^{-\alpha x^2}$.
:::

### Second and mixed partial derivatives

Differentiating twice along the same variable gives $\dfrac{\partial^2 f}{\partial x^2}$, written $f_{xx}$; differentiating once along each gives the **mixed** partial $\dfrac{\partial^2 f}{\partial y\,\partial x}$, written $f_{xy}$. For every smooth function the order does not matter:

$$
\frac{\partial^2 f}{\partial y\,\partial x} = \frac{\partial^2 f}{\partial x\,\partial y}.
$$

For the example above, $f_{xy} = 2x + \cos(xy) - xy\sin(xy)$ whichever variable you differentiate first. This innocent-looking equality is the origin of the Maxwell relations of thermodynamics.

### The chain rule on a sliding shape

The most important partial-derivative calculation in this course involves a function of the single combination $x - vt$. Take any smooth profile $f$ and a constant $v$, and define

$$
u(x,t) = f(x - vt).
$$

At $t = 0$ the graph of $u$ is just the graph of $f$; at a later time the same shape has moved a distance $vt$ to the right. So $u$ describes a shape sliding at speed $v$ without changing form. Its partial derivatives follow from the chain rule with the inner function $s = x - vt$, for which $\partial s/\partial x = 1$ and $\partial s/\partial t = -v$:

$$
\frac{\partial u}{\partial x} = f'(s)\cdot 1 = f'(s),
\qquad
\frac{\partial u}{\partial t} = f'(s)\cdot(-v) = -v\,f'(s).
$$

Differentiate once more and every factor of $v$ appears again:

$$
\frac{\partial^2 u}{\partial x^2} = f''(s),
\qquad
\frac{\partial^2 u}{\partial t^2} = v^2 f''(s).
$$

Eliminating $f''$ between the two lines gives a relation that holds for **every** sliding shape, whatever $f$ is:

$$
\frac{\partial^2 u}{\partial x^2} = \frac{1}{v^2}\,\frac{\partial^2 u}{\partial t^2}.
$$

This is the classical wave equation. Here it emerged from calculus alone; in [the waves lecture](../ch02/01-waves.md) the same equation gets its physical meaning, and the shorthand $u_{xx}$ and $u_{tt}$ used there is the subscript notation introduced above. The same steps with $f(x + vt)$ give a shape sliding to the left and the identical relation, since $v$ enters only as $v^2$.

:::{tip} **Activity: partial derivatives of the ideal gas law**

For $P(V,T) = nRT/V$ compute $\left(\partial P/\partial V\right)_T$ and $\left(\partial P/\partial T\right)_V$. Then write the total change in pressure for small changes $dV$ and $dT$ as $dP = \left(\partial P/\partial V\right)_T dV + \left(\partial P/\partial T\right)_V dT$.
:::

:::{seealso} Solution
:class: dropdown

$\left(\partial P/\partial V\right)_T = -nRT/V^2$ (power rule in $V$ with $T$ frozen) and $\left(\partial P/\partial T\right)_V = nR/V$ (linear in $T$ with $V$ frozen). Hence

$$
dP = -\frac{nRT}{V^2}\,dV + \frac{nR}{V}\,dT.
$$

This **total differential** adds up the change coming from each variable separately, one partial derivative per variable. It is the everyday tool of thermodynamics.
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
plt.suptitle('Fig.3 Riemann sums approaching the exact area 8/3 = 2.667 as n grows', y=1.04)
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

### Problem 6: Mixed partial derivatives

For $f(x,y) = x^3 y^2 + e^{xy}$ find $\partial f/\partial x$ and $\partial f/\partial y$, then verify that the two mixed second derivatives agree.

:::{admonition} **Solution**
:class: dropdown solution

With $y$ frozen, $\dfrac{\partial f}{\partial x} = 3x^2 y^2 + y\,e^{xy}$; with $x$ frozen, $\dfrac{\partial f}{\partial y} = 2x^3 y + x\,e^{xy}$.

Differentiating the first result with respect to $y$ and the second with respect to $x$:

$$
\frac{\partial^2 f}{\partial y\,\partial x} = 6x^2 y + e^{xy} + xy\,e^{xy},
\qquad
\frac{\partial^2 f}{\partial x\,\partial y} = 6x^2 y + e^{xy} + xy\,e^{xy}.
$$

They match, as they must for any smooth function.
:::

### Problem 7: Verify a Riemann sum numerically

Modify the Riemann-sum code above to estimate $\int_0^{\pi}\sin x\,dx$ and compare with the exact value $2$.

### Problem 8: Chain rule on a plane wave

Differentiate $\psi(x) = e^{ikx}$ with respect to $x$, and again to find $\psi''(x)$.

### Problem 9: A Gamma-function integral

Evaluate $\displaystyle\int_0^{\infty} x^2\,e^{-x}\,dx$ using integration by parts twice.

### Problem 10: A standing shape

Show that $u(x,t) = \sin(kx)\cos(\omega t)$ satisfies $\dfrac{\partial^2 u}{\partial x^2} = \dfrac{k^2}{\omega^2}\,\dfrac{\partial^2 u}{\partial t^2}$. Compare with the relation obeyed by the sliding shape $f(x - vt)$ and read off the speed $v$.
