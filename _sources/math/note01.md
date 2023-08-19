## Integrals

### Indefinite integrals

|Description|Equations|
|-:|:-|
|Indefinite integral (antiderivative)|$F(x) = \displaystyle\int f(x) \ dx \newline F'(x) = f(x)$|
|Antiderivative as a family of functions <br/> (Plus $C$!)|If $F$ is an antiderivative of $f$, $C$ is a constant, <br/> then the most general antiderivative is $F(x) + C$|

### Table of indefinite integrals

|Function $f(x)$|Antiderivative $F(x)$|Function $f(x)$|Antiderivative $F(x)$|
|-:|:-|-:|:---|
|$x^n$|$\dfrac{x^{n+1}}{n+1}+C$|$\dfrac{1}{x}$|$\ln\lvert x \rvert + C$|
|$e^x$|$e^x + C$|$b^x$|$\dfrac{b^x}{\ln b} + C$|
|$\sin x$|$-\cos x + C$|$\cos x$|$\sin x + C$|
|$\sec^2 x$|$\tan x + C$|$csc^2 x$|$-\cot x + C$|
|$\sec x\tan x$|$\sec x + C$|$\csc x\cot x$|$-\csc x + C$|
|$\dfrac{1}{x^2 + a^2}$|$\dfrac{1}{a}\arctan \left(\dfrac{x}{a}\right) + C$|$\dfrac{1}{\sqrt{a^2-x^2}}$|$\arcsin \left(\dfrac{x}{a}\right) + C$|

### Definite integrals as Riemann sums

|Description|Equations|
|-:|:-|
|Area|$A = \lim\limits_{n\to\infty} R_{n} = \lim\limits_{n\to\infty} \sum\limits_{i=1}^{n}f(x_i)\Delta x$|
|Definite integral|$\int_{a}^{b} f(x) \ dx = \lim\limits_{n\to\infty} \sum\limits_{i=1}^{n}f(x_i^*)\Delta x$|
|Operational definition of definite integral as Riemann sum|$\int_a^b f(x) \ dx = \lim\limits_{n\to\infty} \sum\limits_{i=1}^n f(x_i)\Delta x$ <br/> $\Delta x = \frac{b-a}{n} \newline x_i = a+i\Delta x$|


### Properties of definite integrals

|Description|Equations|
|-:|:-|
|Reversing the bounds changes the sign of definite integrals|$\int_a^b f(x) \ dx = -\int_b^a f(x) \ dx$|
|Definite integral is zero if upper and lower bounds are the same|$\int_a^a f(x) \ dx = 0$|
|Definite integrals of constant|$\int_a^b c \ dx = c(b-a)$|
|Addition and subtraction of definite integrals|$\int_a^b [f(x) \pm g(x)] \ dx \newline = \int_a^b f(x) \ dx \pm \int_a^b g(x) \ dx$|
|Constant multiple of definite integrals|$\int_a^b cf(x) \ dx = c\int_a^b f(x) \ dx$|

### Fundamental theorem of calculus

|Description|Equations|
|-:|:-|
|**Fundamental theorem of calculus I** <br/> ($f$ is continuous on $[a,b]$)|$g(x) = \displaystyle\int_a^x f(t) \ dt \newline g'(x) = f(x)$|
|**Fundamental theorem of calculus II** <br/> ($f$ is continuous on $[a,b]$)|$\displaystyle\int_a^b f(x) \ dx = F(b) - F(a)$ <br/> where $F$ is any antiderivative of $f$|
|Net change theorem <br/> The integral of a rate of change is the net change|$\displaystyle\int_a^b F'(x) \ dx = F(b) - F(a)$|

### Substitution rule

|Description|Equations|
|-:|:-|
|Substitution rule (u-substitution) <br/> $u \equiv g(x)$|$\displaystyle\int f(g(x)) g'(x) \ dx = \int f(u) \ du$|
|Substitution rule for definite integrals <br/> $u \equiv g(x)$|$\displaystyle\int_a^b f(g(x))g'(x) \ dx = \int_{g(a)}^{g(b)} f(u) \ du$|
|Integrals of even functions|$\int_{-a}^a f(x) \ dx = 2 \int_{0}^a f(x) \ dx$|
|Integrals of odd functions|$\int_{-a}^a f(x) \ dx = 0$|

## Techniques of Integration

### Integration by parts

|Description|Equations|
|-:|:-|
|Integration by parts|$\int f(x)g'(x) \ dx \newline =  f(x)g(x) - \int g(x)f'(x) \ dx$|
|Integration by parts|$\int u \ dv = uv - \int v \ du$|
|Integration by parts for definite integrals|$\int_a^b fg' \ dx = [fg]_a^b - \int_a^b f'g \ dx$|


### Trigonometric integrals

|Description|Equations|
|-:|:-|
|Integral of odd power of cosine <br/> $(u = \sin x)$|$\int \sin^m(x)\cos^{2k+1}(x) \ dx \newline = \int \sin^m(x) [\cos^2 (x)]^k \ dx \newline = \int \sin^m(x)[1-\sin^2(x)]^k \ dx$|
|Integral of odd power of sine <br/> $(u = \cos x)$|$\int \sin^{2k+1}(x)\cos^{n}(x) \ dx \newline = \int [\sin^2 (x)]^k \cos^n(x) \sin(x) \ dx \newline = \int [1-\cos^2(x)]^k \cos^n(x) \sin(x) \ dx$|
|Integral of even power of sine and cosine use trig identities|$\sin^2(x) = \frac{1}{2}(1-\cos(2x)) \newline \cos^2(x) = \frac{1}{2}(1+\cos(2x)) \newline \sin(x)\cos(x) = \frac{1}{2}\sin(2x)$|
|Trig identity for solving <br/> $\int \sin(mx)\cos(nx) \ dx$|$\sin A \cos B = \frac{1}{2}[\sin(A-B) + \sin(A+B)]$|
|Trig identity for solving <br/> $\int \sin(mx)\sin(nx) \ dx$|$\sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$|
|Trig identity for solving <br/> $\int \cos(mx)\cos(nx) \ dx$|$\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$|



