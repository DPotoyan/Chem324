
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
|Area|$A = \lim\limits_{n\to\infin} R_{n} = \lim\limits_{n\to\infin} \sum\limits_{i=1}^{n}f(x_i)\Delta x$|
|Definite integral|$\int_{a}^{b} f(x) \ dx = \lim\limits_{n\to\infin} \sum\limits_{i=1}^{n}f(x_i^*)\Delta x$|
|Operational definition of definite integral as Riemann sum|$\int_a^b f(x) \ dx = \lim\limits_{n\to\infin} \sum\limits_{i=1}^n f(x_i)\Delta x$ <br/> $\Delta x = \frac{b-a}{n} \newline x_i = a+i\Delta x$|
|Sums of powers of positive integers|$\sum\limits_{i=1}^{n}i = \frac{n(n+1)}{2} \newline \sum\limits_{i=1}^{n}i^2 = \frac{n(n+1)(2n+1)}{6} \newline \sum\limits_{i=1}^{n}i^3 = \left[ \frac{n(n+1)}{2} \right]^2$|
|Properties of summation|$\sum\limits_{i=1}^{n}c = nc \newline \sum\limits_{i=1}^{n}ca_i = c\sum\limits_{i=1}^{n}a_i \newline \sum\limits_{i=1}^{n}(a_i \pm b_i) = \sum\limits_{i=1}^{n}a_i \pm \sum\limits_{i=1}^{n}b_i$|

### Properties of definite integrals

|Description|Equations|
|-:|:-|
|Reversing the bounds changes the sign of definite integrals|$\int_a^b f(x) \ dx = -\int_b^a f(x) \ dx$|
|Definite integral is zero if upper and lower bounds are the same|$\int_a^a f(x) \ dx = 0$|
|Definite integrals of constant|$\int_a^b c \ dx = c(b-a)$|
|Addition and subtraction of definite integrals|$\int_a^b [f(x) \pm g(x)] \ dx \newline = \int_a^b f(x) \ dx \pm \int_a^b g(x) \ dx$|
|Constant multiple of definite integrals|$\int_a^b cf(x) \ dx = c\int_a^b f(x) \ dx$|
|Comparison properties of definite integrals|If $f(x) \ge 0$ for $x\in[a,b]$, <br/> then $\int_a^b f(x) \ dx \ge 0$|
|Comparison properties of definite integrals|If $f(x) \ge g(x)$ for $x\in[a,b]$, <br/> then $\int_a^b f(x) \ dx \ge \int_a^b g(x) \ dx$|
|Comparison properties of definite integrals|If $m \le f(x) \le M$ for $x\in[a,b]$, <br/> then $m(b-a) \le \int_a^b f(x) \ dx \le M(b-a)$|

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

### Approximating integrals

|Description|Equations|
|-:|:-|
|Midpoint rule|$\int_a^b f(x) \ dx \approx \sum\limits_{i=1}^n f(\bar{x}_i)\Delta x$ <br/> $\Delta x = \frac{b-a}{n} \newline \bar{x}_i = \frac{1}{2}(x_{i-1}+x_i)$|
|Error bound for midpoint rule|$\lvert E_M \rvert \le \dfrac{K(b-a)^3}{24n^2}$|
|Trapezoidal rule|$\int_a^b f(x) \ dx \approx \frac{1}{2}\Delta x [f(x_0) + 2f(x_1) + ... + 2f(x_{n-1}) + f(x_n)]$ <br/> $\Delta x = \frac{b-a}{n} \newline x_i = a + i\Delta x$|
|Error bound for trapezoidal rule|$\lvert E_T \rvert \le \dfrac{K(b-a)^3}{12n^2}$|
|Simpson's rule|$\int_a^b f(x) \ dx \approx \frac{1}{3}\Delta x [f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + ... + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n)]$ <br/> $\Delta x = \frac{b-a}{n}$, n is even|
|Error bound for Simpson's rule|$\lvert E_S \rvert \le \dfrac{K(b-a)^5}{180n^4}$|

### Trigonometric integrals

|Description|Equations|
|-:|:-|
|Integral of odd power of cosine <br/> $(u = \sin x)$|$\int \sin^m(x)\cos^{2k+1}(x) \ dx \newline = \int \sin^m(x) [\cos^2 (x)]^k \ dx \newline = \int \sin^m(x)[1-\sin^2(x)]^k \ dx$|
|Integral of odd power of sine <br/> $(u = \cos x)$|$\int \sin^{2k+1}(x)\cos^{n}(x) \ dx \newline = \int [\sin^2 (x)]^k \cos^n(x) \sin(x) \ dx \newline = \int [1-\cos^2(x)]^k \cos^n(x) \sin(x) \ dx$|
|Integral of even power of sine and cosine use trig identities|$\sin^2(x) = \frac{1}{2}(1-\cos(2x)) \newline \cos^2(x) = \frac{1}{2}(1+\cos(2x)) \newline \sin(x)\cos(x) = \frac{1}{2}\sin(2x)$|
|Integral of even power of secant <br/> $(u = \tan x)$|$\int \tan^m(x)\sec^{2k}(x) \ dx \newline = \int \tan^m(x)[\sec^2(x)]^{k-1}\sec^2(x) \ dx \newline = \int \tan^m(x)[1+\tan^2(x)]^{k-1}\sec^2(x) \ dx$|
|Integral of odd power of tangent <br/> $(u = \sec x)$|$\int tan^{2k+1}(x)\sec^n(x) \ dx \newline = \int[\tan^2(x)]^k\sec^{n-1}(x)\sec(x)\tan(x) \ dx \newline = \int [\sec^2(x)-1]^k\sec^{n-1}(x)\sec(x)\tan(x) \ dx$|
|Trig identity for solving <br/> $\int \sin(mx)\cos(nx) \ dx$|$\sin A \cos B = \frac{1}{2}[\sin(A-B) + \sin(A+B)]$|
|Trig identity for solving <br/> $\int \sin(mx)\sin(nx) \ dx$|$\sin A \sin B = \frac{1}{2}[\cos(A-B) - \cos(A+B)]$|
|Trig identity for solving <br/> $\int \cos(mx)\cos(nx) \ dx$|$\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$|

### Trigonometric substitution

|Expression|Substitution|Trigonometric Identity|
|:-:|:-:|:-:|
|$\sqrt{a^2 - x^2}$|$x = a\sin\theta$|$1 - \sin^2\theta = \cos^2\theta$|
|$\sqrt{a^2 + x^2}$|$x = a\tan\theta$|$1+\tan^2\theta = \sec^2\theta$|
|$\sqrt{x^2 - a^2}$|$x = a\sec\theta$|$\sec^2\theta-1 = \tan^2\theta$|

### Improper integrals

|Description|Equations|
|-:|:-|
|Improper integrals with single one-side infinite intervals|$\int_a^\infin f(x) \ dx = \lim\limits_{t\to\infin}\int_a^t f(x) \ dx \newline \int_{-\infin}^b f(x) \ dx = \lim\limits_{t\to-\infin}\int_t^b f(x) \ dx$|
|Improper integrals with single two-side infinite intervals|$\int_{-\infin}^\infin f(x) \ dx \newline = \int_{-\infin}^a f(x) \ dx + \int_a^\infin f(x) \ dx$|
|Convergence and divergence of improper integrals of power functions|$\displaystyle\int_1^\infin \dfrac{1}{x^p} \ dx$ <br/> convergent if $p>1$ <br/> divergent if $p \le 1$|
|Improper integrals with discontinuous integrand on one side|$\int_a^b f(x) \ dx = \lim\limits_{t\to b^-}\int_a^t f(x) \ dx \newline \int_a^b f(x) \ dx = \lim\limits_{t\to a^+}\int_t^b f(x) \ dx$|
|Improper integrals with discontinuous integrand in the middle $c$|$\int_a^b f(x) \ dx = \int_a^c f(x) \ dx + \int_c^b f(x) \ dx$|
|Comparison theorem <br/> $(f(x) \ge g(x) \ge 0, x \ge a)$|(a) If $\int_a^\infin f(x) \ dx$ is convergent, <br/> then $\int_a^\infin g(x) \ dx$ is convergent. <br/> (b) If $\int_a^\infin g(x) \ dx$ is divergent, <br/> then $\int_a^\infin f(x) \ dx$ is divergent.|

## Applications of Integration

|Description|Equations|
|-:|:-|
|Areas between curves|$A = \int_a^b [f(x) - g(x)] \ dx$|
|Volume by method of disks and washers|$V = \int_a^b A(x) \ dx$|
|Volume by method of cylindrical shells <br/> (rotating about y-axis)|$V = \int_a^b 2\pi x f(x) \ dx$|
|Average value of a function|$\bar{f} = \frac{1}{b-a}\int_a^b f(x) \ dx$|
|The mean value theorem of integrals|If $f$ is continuous on $[a,b]$, <br/> then there exists $c\in[a,b]$ such that <br/> $f(c) = \bar{f} = \frac{1}{b-a}\int_a^b f(x) \ dx$,<br/> $\int_a^b f(x) \ dx = f(c)(b-a)$|
|Arc length formula|$L = \int_a^b \sqrt{1+[f'(x)]^2} \ dx$|
|Arc length function|$s(x) = \int_a^x \sqrt{1+[f'(t)]^2} \ dt$|
|Surface area of surface of resolution about x-axis|$S = \int_a^b 2\pi f(x)\sqrt{1 + [f'(x)]^2} \ dx$|
