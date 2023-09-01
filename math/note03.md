## Complex numbers

**Recommended:** Watch the  following YouTube video 
["complex numbers are real, part-1"](https://www.youtube.com/watch?v=T647CGsuOVU)

**Also recommended:** [A Visual, Intuitive Guide to Imaginary Numbers](https://betterexplained.com/articles/a-visual-intuitive-guide-to-imaginary-numbers/)

### "Complex numbers are every bit as real as every other number. "  

A complex number $z$ is a kind of 2D number that lives in 2D space and requires two components for its full specification:

![](./images/cnum_intro.png)

- **Real part** $ x $ 
.
- **Imaginary part** $ y $.

Complex numbers are every bit as real as  negative numbers. Sure, you do not count objects on your fingers by using complex numbers but complex numbers obey important relationships in math and physics the same way other numbers do. In fact we will see that the central equation of quantum mechanics, the Schrödinger equation, contains an imaginary number. As a result, solutions of the Schrödinger equation are functions of complex variable. Why? Because, apparently, that's how nature works. Nature operates on a complex plane, which includes real numbers as subset. Can we learn to use complex numbers with ease and develop an intuition and visual sense? Yup! And that will be our objective in this short Appendix. 

### Introducing $ i $ 

When first confronted with complex numbers they seem unintuitive and hard to visualize. The imaginary unit $ i $ in particular mystifies as to what it is and where did it come from. 
Some facts from mathematics are in order here:

- **What is the definition of $ i $?** The imaginary number $ i $ is defined solely by the property that its square is $−1$, that is: $i\cdot i=-1$. 

- **How does $i$ change what I know about math of real variables?** Imaginary numbers are an important mathematical concept, which extend the real number system $\mathbb{R}$ to the complex number system $\mathbb{C}$, which in turn provides at least one root for every nonconstant polynomial $P(x)$. (See the Fundamental theorem of algebra.) The term "imaginary" is used because there is no real number having a negative square.

- **Where does $i$ appear in math?** Most notably imaginary number (i) provide solutions to quadratic equation $x^2 + 1 = 0.$ Although there is no real number with this property, i can be used to extend the real numbers to what are called complex numbers, using addition and multiplication. Generally there are two complex square roots of every real number e.g square root of -1 is i and -i. 

- **What do you call a number that contains i?** A complex number z=1+2i. A function of complex variable is a function if it operates on complex variables z. 


### Eculidean vs polar representation of complex numbers

![](./images/cnum_2.png)

The Euclidean, polar, and trigonometric forms of a complex number $ z $ are given by:

$$z = x + iy = r(\cos{\phi} + i \sin{\phi}) = re^{i\phi} $$

The second equality above is known as [**Euler’s formula**](https://en.wikipedia.org/wiki/Euler%27s_formula#targetText=Euler's%20formula%20states%20that%20for,argument%20x%20given%20in%20radians.&targetText=When%20%2C%20Euler's%20formula%20evaluates%20to,is%20known%20as%20Euler's%20identity.) 
And equally widely regarded as one of the most beautiful and mysterious in mathematics.


The complex conjugate $\bar{z}$ of $z$ is defined as

$$\bar z = x-iy =  r (\cos{\phi} - i \sin{\phi} ) = re^{-i\phi}$$

The value $r$ is the Euclidean distance of vector $(x,y)$ from the
origin and is equal to the modulus of $|z|=\sqrt{\bar{z}z}$

$$r = |z| = \sqrt{x^2 + y^2}$$

The value $\phi$ is the angle of (0,0)-(x,y) line with respect to the real axis. 
The tangent of $\phi$ is $\left(\frac{y}{x}\right) $. Therefore,

$$
\phi = \tan^{-1} \Big(\frac{y}{x} \Big)
$$


Three elementary trigonometric functions are

$$
\cos{\phi} = \frac{x}{r} = \frac{e^{i\phi} + e^{-i\phi}}{2} , \quad
\sin{\phi} = \frac{y}{r} = \frac{e^{i\phi} - e^{-i\phi}}{2i} , \quad
\tan{\phi} = \frac{y}{x}
$$


## De Moivre’s Theorem

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


**Exercise:** set n=2 and first set real component to zero and obtain expresion for sine. Then set imaginary component to zero and obtain expression for cosine. 



### Example-1: Pythagoras' theorem

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


### Example-2: Trigonometric Identities

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

The equations above are also known as the **angle sum identities**. We
can verify the equations using the `simplify` function in the
`sympy` package.


### Example-3: Trigonometric Integrals

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