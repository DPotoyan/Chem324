## Complex numbers

:::{admonition} What you need to know
:class: note

- **Complex numbers generalize oridnary 1D numbers to 2D**  To descirbe complex numbers 
 we need two compoenents called real and imaginary parts. Complex numbers appear naturally in quantum mechanics and are essential part of physics.

- **The imaginary unit: $i = \sqrt{-1}$** This symbol, $i$, represents the imaginary component of a complex number, where $i^2 = -1$.

- **Complex numbers as roots of polynomial equations.**  For example, quadratic equations can have two complex roots, showcasing their relevance in solving equations.

- **Cartesian and polar representations**
Complex numbers can be expressed in Cartesian form $(x + iy)$ or polar form $(re^{i\phi})$, where $r$ is the magnitude, and $\phi$ is the phase (angle).

- **Euler’s formula: A beautiful and fundamental equation** $re^{i\phi} = r(\cos \phi + i\sin \phi)$, elegantly connects complex numbers to trigonometric functions. uler's equation makes it much easier to manipulate complex numbers, especially in their polar form, simplifying multiplication and division.

- **Rotation in the complex plane**
Multiplying by a complex number in polar form corresponds to a rotation. For instance, $re^{i\phi}$ rotates a vector of length $r$ counterclockwise by an angle $\phi$, while $re^{-i\phi}$ rotates it clockwise by $\phi$.

- **Complex conjugate: Flipping the imaginary part** The conjugate of a complex number $z = x + iy$ is given by $z^* = x - iy$. 

- **Multiplying by the conjugate** When you multiply a complex number by its conjugate, $z \cdot z^*$, the result is a real number equal to the square of its distance from the origin in the complex plane: $|z|^2 = x^2 + y^2$.
:::


### Complex number living in 2D

- A complex number $z$ is a kind of 2D number that lives in 2D space and requires two components for its full specification. Watch the video to get a visual feel for why we need complex numbers. 

<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/T647CGsuOVU?si=Q2QdaM1jhy4SEdkx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>


### Introducing imaginary number $ i $ 


- **Fundamental theorem of algebra.** says that polynomial equations like quadratic, cubic, quartic etc must have numbers of roots equal to the highest power. E.g quadratic must have two roots. Complex numbers ensure the existence of roots for polynomials.

- This equation must have two solutions/roots. How do we visualize them?

$$x^2+1=0$$

$$x_{1,2}= \pm\sqrt{-1} = \pm i$$

- The answer: we will need two dimensions! quantifying how much real and how much imaginary component the number has.

- **What is the definition of $ i $?** The imaginary number $ i $ is defined solely by the property that its square is $−1$, that is: $i\cdot i=-1$. 

- **How does $i$ change what I know about math of real variables?** Imaginary numbers extend the real number system $\mathbb{R}$ to the complex number system $\mathbb{C}$.

:::{figure-md} markdown-fig
align: left

<img src="images/SumNums.png" alt="applied photoelectric" class="bg-primary mb-1" style="background-color: white;" width="60%">

Complex numbers live in 2D: You must specify real and imaginary components to fully define a complex number
:::


### Cartesian vrepresentation

:::{figure-md} markdown-fig
align: left

<img src="images/Cart.png" alt="applied photoelectric" class="bg-primary mb-1" style="background-color: white;" width="60%">

Visualizing complaex numbers in cartesian coordinates. 

:::

:::{admonition} **Cartesian Representation**
:class: important

$$z = x+iy$$

- $x$ real component
- $y$ imaginary component
- $i$ imaginary number, $i^2=-1$
- $z$ complex number
:::


- **Example:** Identify real and imaginary components of the following complex numbers $z_1 = 3 +2$, $z_2 = -2i$, $z_3=1.1$

    - $Re(z_1) = 3$, $Im(z_1)=2$
    - $Re(z_2) = 0$, $Im(z_2)=-2$
    - $Re(z_3) = 1.1$, $Im(z_1)=0$

### Polar vrepresentation

:::{figure-md} markdown-fig
align: left

<img src="images/PolCart.png" alt="applied photoelectric" class="bg-primary mb-1" style="background-color: white;" width="60%">

Visualizing complaex numbers in polar coordinates. 

:::

- Polar representation expresses complex numbers in terms of radius from origin $r$ and angle of counterclockwise rotation $\phi$

    - $x = r\cos\phi$
    - $y = r\sin\phi$

$$z= x+iy = rcos\phi + ri\sin\phi =r(cos\phi+isin\phi)$$

- What's the big deal? We will find that life is much much easier in polar represnation when deriving new expressions or manipulating complex numbers. 
- This dramatic simplification.is thanks to "magical" Euler's formula that turns trig functions into exponentss!

:::{admonition} **Euler’s formula**
:class: important 

$$\cos{\phi} + i \sin{\phi} = e^{i\phi}$$
:::



:::{figure-md} markdown-fig
align: left

<img src="images/Rising_circular.gif" alt="applied photoelectric" class="bg-primary mb-1" style="background-color: white;" width="60%">

Visualization of Euler's formula as a helix in three-dimensional space. The helix is formed by plotting points for various values of $\phi$ and is determined by both the cosine and sine components of the formula. One curve represents the real component  $cos\phi$ of the formula, while another curve, rotated 90 degrees around the z-axis (due to multiplication by 
$i$ represents the imaginary component $sin\phi$


:::



:::{admonition} **Proof Euler's formula**
:class: tip, dropdown

We will prove this by using the Taylor series expansions of the exponential function, cosine, and sine.

**Step 1: Taylor Series Expansion of $e^x$**

The Taylor series expansion of $e^x$ around $x = 0$ is:

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \cdots
$$

For $e^{i\phi}$, substitute $x = i\phi$ into the series:

$$
e^{i\phi} = 1 + i\phi + \frac{(i\phi)^2}{2!} + \frac{(i\phi)^3}{3!} + \frac{(i\phi)^4}{4!} + \cdots
$$

**Step 2: Simplifying Powers of $i$**
We know that powers of $i$ cycle as follows:

$$
i^1 = i, \quad i^2 = -1, \quad i^3 = -i, \quad i^4 = 1, \quad \text{and so on}.
$$

Using these identities, we simplify each term in the series:

$$
e^{i\phi} = 1 + i\phi - \frac{\phi^2}{2!} - i\frac{\phi^3}{3!} + \frac{\phi^4}{4!} + i\frac{\phi^5}{5!} - \cdots
$$

**Step 3: Grouping Real and Imaginary Terms**
Now, we group the real and imaginary terms separately:

$$
e^{i\phi} = \left(1 - \frac{\phi^2}{2!} + \frac{\phi^4}{4!} - \cdots\right) + i\left(\phi - \frac{\phi^3}{3!} + \frac{\phi^5}{5!} - \cdots\right)
$$

**Step 4: Recognizing Taylor Series for $\cos\phi$ and $\sin\phi$**

The Taylor series for $\cos\phi$ is:

$$
\cos\phi = 1 - \frac{\phi^2}{2!} + \frac{\phi^4}{4!} - \cdots
$$

And the Taylor series for $\sin\phi$ is:

$$
\sin\phi = \phi - \frac{\phi^3}{3!} + \frac{\phi^5}{5!} - \cdots
$$

**Step 5: Substituting the Series Back**
We see that the real part of the series matches $\cos\phi$, and the imaginary part matches $i\sin\phi$. Therefore:


$$
e^{i\phi} = \cos\phi + i\sin\phi
$$

**Conclusion**
This completes the proof of Euler's formula:
$$
e^{i\phi} = \cos\phi + i\sin\phi
$$

:::


:::{admonition} **Polar Representation**
:class: important

$$z =  re^{i\phi}$$

- $r=\sqrt{x^2+y^2}$ distance from origin.
- $\phi$ rotation angle in complex plane.
:::


### Complex Conjugate

:::{admonition} **Complex Conjugate**
:class: important 

$$\bar z = x-iy$$


$$\bar z = re^{-i\phi}$$


:::


#### Extracting absolute value

- Multiplying complex number by its conjugate always results in positive real number!
- Geometrically this means rotating back to real axis!
- Product of complex number and its conjugate returns the distance from the origin in complex plane. 

$$|z|^2 = \bar z \cdot z = (x-iy)\cdot (x+iy) = x^2+y^2$$
$$|z|^2 = \bar z \cdot z = re^{-i\phi}\cdot re^{i\phi}=r^2$$


#### Expressing sin and cos via complex exponentials

- Using Euler's formula we can take the sum and difference of $z$ and $\bar z$ to express sin and cos in terms of compelx exponentials. 
- These representations of sin and cos are super powerful in simplifying various integrals and for deriving experssions. 

$$
\cos{\phi} = \frac{e^{i\phi} + e^{-i\phi}}{2}
$$

$$
\sin{\phi} = \frac{e^{i\phi} - e^{-i\phi}}{2i}
$$

#### Going From Carteisan to Polar

- **Extract r** The value $r$ is the Euclidean distance of vector $(x,y)$ from the origin and is equal to the modulus of $|z|=\sqrt{\bar{z}z}$

$$r = |z| = \sqrt{x^2 + y^2}$$

-  **Extract $\phi$** The value $\phi$ is the angle of with respect to the real axis.  The tangent of $\phi$ is $\left(\frac{y}{x}\right) $. Therefore using simple trigonometry we can backcalculate angle and sin, cos tan functions from cartesia representatn 

$$
\tan{\phi} = \frac{y}{x}
$$

$$
\phi = \tan^{-1} \Big(\frac{y}{x} \Big)
$$



### Examples of using complex numbers

:::{admonition} **De Moivre’s Theorem**
:class: tip, dropdown

[De Moivre’s theorem](https://en.wikipedia.org/wiki/De_Moivre%27s_formula) states that:

$$
z^n=(r(\cos{\theta} + i \sin{\theta}))^n =
r^n e^{in\theta} =
r^n(\cos{n\theta} + i \sin{n\theta})
$$

We raised complex number to power n, used polar representation and realized that exponent raised to power n simply multiplies polar angle by n. 
Note that de Moivre’s theorem allows relating trigonometric functions of angle $\theta$ raised to power $n$ to trignomoteric functions of of angle $n\theta$ of power one:

$$
r^n(\cos{\theta} + i \sin{\theta})^n = r^n (\cos{n\theta} + i \sin{n\theta})
$$

$$
(\cos{\theta} + i \sin{\theta})^n = (\cos{n\theta} + i \sin{n\theta})
$$

The proof of de Moivre's theorem can be done via [induction](https://en.wikipedia.org/wiki/De_Moivre%27s_formula), e.g one can expand the parentheses ans assert the equality for cases n=2, n=3, ...
:::

:::{admonition} **Deriving Pythagoras' theorem**
:class: tip, dropdown

We can use de Moivre’s theorem to show that
$ r = \sqrt{x^2 + y^2} $.

We have

$$
\begin{aligned}
1 &= e^{i\theta} e^{-i\theta} \\
&= (\cos{\theta} + i \sin{\theta})(\cos{(\text{-}\theta)} + i \sin{(\text{-}\theta)}) \\
&= (\cos{\theta} + i \sin{\theta})(\cos{\theta} - i \sin{\theta}) \\
&= \cos^2{\theta} + \sin^2{\theta} \\
&= \frac{x^2}{r^2} + \frac{y^2}{r^2}
\end{aligned}
$$

and thus

$$
x^2 + y^2 = r^2
$$

We recognize this as a theorem of **Pythagoras**.
:::


:::{admonition} **Deriving Trigonometric Identities**
:class: tip, dropdown

We can obtain a complete suite of trigonometric identities by
appropriately manipulating polar forms of complex numbers.

We’ll get many of them by deducing implications of the equality

$$e^{i(\omega + \theta)} = e^{i\omega} e^{i\theta}$$

For example, we’ll calculate identities for $\cos{(\omega + \theta)} $ and $ \sin{(\omega + \theta)}$.

Using the sine and cosine formulas presented at the beginning of this
lecture, we have:

$$\begin{aligned}
\cos{(\omega + \theta)} = \frac{e^{i(\omega + \theta)} + e^{-i(\omega + \theta)}}{2} \\
\sin{(\omega + \theta)} = \frac{e^{i(\omega + \theta)} - e^{-i(\omega + \theta)}}{2i}
\end{aligned}$$

We can also obtain the trigonometric identities as follows:

$$
\begin{aligned}
\cos{(\omega + \theta)} + i \sin{(\omega + \theta)}
&= e^{i(\omega + \theta)} \\
&= e^{i\omega} e^{i\theta} \\
&= (\cos{\omega} + i \sin{\omega})(\cos{\theta} + i \sin{\theta}) \\
&= (\cos{\omega}\cos{\theta} - \sin{\omega}\sin{\theta}) +
i (\cos{\omega}\sin{\theta} + \sin{\omega}\cos{\theta})
\end{aligned}
$$

Since both real and imaginary parts of the above formula should be
equal, we get:

$$
\begin{aligned}
\cos{(\omega + \theta)} = \cos{\omega}\cos{\theta} - \sin{\omega}\sin{\theta} \\
\sin{(\omega + \theta)} = \cos{\omega}\sin{\theta} + \sin{\omega}\cos{\theta}
\end{aligned}
$$

The equations above are also known as the **angle sum identities**. 

:::


:::{admonition} **Evaluating Trigonometric Integrals**
:class: tip, dropdown

We can also compute the trigonometric integrals using polar forms of
complex numbers.

For example, we want to solve the following integral:

$$\int_{-\pi}^{\pi} \cos(\omega) \sin(\omega) \, d\omega$$

Using Euler’s formula, we have:

$$\begin{aligned}
\int \cos(\omega) \sin(\omega) \, d\omega
&=
\int
\frac{(e^{i\omega} + e^{-i\omega})}{2}
\frac{(e^{i\omega} - e^{-i\omega})}{2i}
\, d\omega  \\
&=
\frac{1}{4i}
\int
e^{2i\omega} - e^{-2i\omega}
\, d\omega  \\
&=
\frac{1}{4i}
\bigg( \frac{-i}{2} e^{2i\omega} - \frac{i}{2} e^{-2i\omega} + C_1 \bigg) \\
&=
-\frac{1}{8}
\bigg[ \bigg(e^{i\omega}\bigg)^2 + \bigg(e^{-i\omega}\bigg)^2 - 2 \bigg] + C_2 \\
&=
-\frac{1}{8}  (e^{i\omega} - e^{-i\omega})^2  + C_2 \\
&=
\frac{1}{2} \bigg( \frac{e^{i\omega} - e^{-i\omega}}{2i} \bigg)^2 + C_2 \\
&= \frac{1}{2} \sin^2(\omega) + C_2
\end{aligned}$$

and thus:

$$
\int_{-\pi}^{\pi} \cos(\omega) \sin(\omega) \, d\omega =
\frac{1}{2}\sin^2(\pi) - \frac{1}{2}\sin^2(-\pi) = 0
$$
:::


:::{admonition} **Applications to X-ray diffraction and crystalography**
:class: tip, dropdown

Complex numbers play a significant role in various chemistry problems, especially in the context of **X-ray diffraction** and **crystallography**. These applications are crucial for determining the atomic structures of molecules and solids.

**X-ray Diffraction and the Phase Problem**
In X-ray crystallography, a crystal is bombarded with X-rays, which are diffracted by the electrons in the crystal. The resulting diffraction pattern contains crucial information about the crystal's structure. However, to reconstruct the atomic arrangement from the diffraction pattern, we must solve two key problems: the **magnitude** of the diffracted waves (intensity) and the **phase** of those waves.

- The **phase problem** refers to the challenge of determining the phase of the diffracted X-rays, which is not directly observable from the diffraction pattern. The phase is necessary to accurately reconstruct the electron density of the crystal.

**Complex Numbers in Diffraction**
To solve this, we model the diffracted waves as complex numbers. Each wave can be described in terms of a complex number:

$$
A(k) = |A(k)|e^{i\phi(k)}
$$

where:

- $|A(k)|$ is the magnitude of the diffraction wave, corresponding to the intensity of the observed diffraction pattern.
- $\phi(k)$ is the phase of the wave, which contains essential structural information but is not directly measurable.

By representing diffraction waves as complex numbers, we can manipulate and combine them to solve for the electron density in the crystal.

**Structure Factor: The Key to Electron Density**
The **structure factor** is a complex quantity that relates the electron density in a crystal to the observed diffraction pattern. The structure factor $F({h})$ is given by:

$$
F({h}) = \sum_{j} f_j e^{i{h} \cdot {r_j}}
$$

where:

- ${h}$ is the reciprocal lattice vector, representing the direction of diffraction.
- $f_j$ is the scattering factor for atom $j$ (how much it scatters X-rays).
- ${r_j}$ is the position of atom $j$ in the unit cell.

The structure factor is complex, with both real and imaginary components:
$$
F({h}) = |F({h})|e^{i\phi({h})}
$$
Here, $|F({h})|$ represents the amplitude (related to the intensity of the diffracted wave), and $\phi({h})$ is the phase.

**Electron Density Calculation**
Once the structure factors are known, the **electron density** $\rho({r})$ can be calculated using the inverse Fourier transform:

$$
\rho({r}) = \frac{1}{V} \sum_{{h}} F({h}) e^{-i{h} \cdot {r}}
$$

where $V$ is the volume of the unit cell, and the sum is over all reciprocal lattice points ${h}$.

In this equation:

- The structure factor $F({h})$ is complex, and complex numbers allow for the combination of the magnitudes and phases of the diffracted waves to accurately reconstruct the electron density.
- The result is a 3D map of the electron density within the crystal, which reveals the positions of atoms.

**Solving the Phase Problem**

The phase problem is addressed using various techniques, such as:
- **Direct methods**: Mathematical techniques that estimate phases based on probabilistic relationships between structure factors.
- **Molecular replacement**: Using a known structure of a related molecule to estimate phases.
- **Anomalous dispersion**: Utilizing the scattering of X-rays at different wavelengths to provide phase information.

In all these methods, complex numbers are central to solving for the electron density and, thus, determining the molecular structure.

**Conclusion**
In chemistry, particularly in X-ray diffraction and crystallography, complex numbers provide a powerful framework for solving the phase problem and calculating structure factors. They allow for the accurate modeling and manipulation of waves, which are essential for determining the atomic structures of molecules and materials.
:::



### Problems

#### Problem 1: Multiplication

Multiply the two complex numbers $z_1 = 3 + 4i$ and $z_2 = 1 - 2i$.

:::{admonition} **Solution 1** 
:class: dropdown

To multiply complex numbers, we use distributive property:

$$
z_1 \cdot z_2 = (3 + 4i)(1 - 2i)
$$

Expanding:

$$
z_1 \cdot z_2 = 3(1) + 3(-2i) + 4i(1) + 4i(-2i)
$$

$$
= 3 - 6i + 4i - 8i^2
$$

Since $i^2 = -1$:

$$
= 3 - 6i + 4i + 8 = 11 - 2i
$$
:::


#### Problem 2: Find conjugate

Find the complex conjugate of $z = -3 + 5i$.


:::{admonition} **Solution 2** 
:class: dropdown

The complex conjugate of a complex number $z = x + iy$ is given by $z^* = x - iy$. For $z = -3 + 5i$, the conjugate is:

$$
z^* = -3 - 5i
$$

:::


#### Problem 3: from polar to cartesian

Convert the complex number $z = 5e^{i\frac{\pi}{4}}$ to its Cartesian form.


:::{admonition} **Solution 3** 
:class: dropdown

Using Euler’s formula:

$$
z = r(\cos\phi + i\sin\phi)
$$

For $z = 5e^{i\frac{\pi}{4}}$, we have $r = 5$ and $\phi = \frac{\pi}{4}$, so:

$$
z = 5\left(\cos\frac{\pi}{4} + i\sin\frac{\pi}{4}\right)
$$

Since $\cos\frac{\pi}{4} = \sin\frac{\pi}{4} = \frac{\sqrt{2}}{2}$, we get:

$$
z = 5\left(\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right) = \frac{5\sqrt{2}}{2} + i\frac{5\sqrt{2}}{2}
$$

:::

#### Problem 4: Division

Divide the complex numbers $z_1 = 3 + 4i$ by $z_2 = 1 - 2i$.

:::{admonition} **Solution 4** 
:class: dropdown

To divide complex numbers, multiply both the numerator and denominator by the conjugate of the denominator:

$$
\frac{z_1}{z_2} = \frac{3 + 4i}{1 - 2i} \times \frac{1 + 2i}{1 + 2i}
$$

First, multiply the numerator:

$$
(3 + 4i)(1 + 2i) = 3(1) + 3(2i) + 4i(1) + 4i(2i) = 3 + 6i + 4i - 8 = -5 + 10i
$$

Next, multiply the denominator:

$$
(1 - 2i)(1 + 2i) = 1^2 - (2i)^2 = 1 + 4 = 5
$$

Now, divide the result:

$$
\frac{-5 + 10i}{5} = -1 + 2i
$$

Thus, $\frac{z_1}{z_2} = -1 + 2i$.

:::

#### Problem 5: Find Modulus

Find the modulus of the complex number $z = 7 + 24i$.

:::{admonition} **Solution 5** 
:class: dropdown

The modulus of a complex number $z = x + iy$ is given by:

$$
|z| = \sqrt{x^2 + y^2}
$$

For $z = 7 + 24i$, we have $x = 7$ and $y = 24$:

$$
|z| = \sqrt{7^2 + 24^2} = \sqrt{49 + 576} = \sqrt{625} = 25
$$
Thus, the modulus of $z$ is 25.

:::

#### Problem 6: Multiplication

Multiply the complex numbers $z_1 = 2e^{i\frac{\pi}{6}}$ and $z_2 = 3e^{i\frac{\pi}{3}}$.

:::{admonition} **Solution 5** 
:class: dropdown

To multiply two complex numbers in polar form, multiply their magnitudes and add their angles:

$$
z_1 \cdot z_2 = (2e^{i\frac{\pi}{6}})(3e^{i\frac{\pi}{3}}) = 6e^{i(\frac{\pi}{6} + \frac{\pi}{3})}= 6e^{i\frac{\pi}{2}}
$$



Thus, the product is:

$$
z_1 \cdot z_2 = 6e^{i\frac{\pi}{2}} = 6i
$$

:::


#### Problem 7: from cartesian to polar

Express the complex number $z = -4 + 4i$ in polar form.

:::{admonition} **Solution 5** 
:class: dropdown

1. **Modulus**:

   $$ 
   r = \sqrt{x^2 + y^2} = \sqrt{(-4)^2 + 4^2} = \sqrt{16 + 16} = \sqrt{32} = 4\sqrt{2} 
   $$

2. **Argument**:

   $$ 
   \phi = \tan^{-1}\left(\frac{y}{x}\right) = \tan^{-1}\left(\frac{4}{-4}\right) = \tan^{-1}(-1) 
   $$ 

   Since $z$ is in the second quadrant:

   $$ 
   \phi = \frac{3\pi}{4}
   $$

Thus, the polar form of $z$ is:

$$ 
z = 4\sqrt{2}e^{i\frac{3\pi}{4}}
$$

:::

