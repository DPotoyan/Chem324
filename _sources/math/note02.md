

## Differentiation

### Derivatives

|Description|Equations|
|-:|:-|
|Derivative as a function|$f'(x) = \lim\limits_{h \to 0}\dfrac{f(x+h) - f(x)}{h}$|
|Geometric interpretation of derivatives|The tangent line of $y = f(x)$ at $(a, f(a))$ has a slope of $f'(a)$ <br/> $m = \lim\limits_{x \to a} \dfrac{f(x) - f(a)}{x-a} = f'(a)$|
|Derivatives and instantaneous rate of change|The derivative $f'(a)$ is the instantaneous rate of change of $y=f(x)$ with respect to $x$ when $x=a$: <br/> $v(a) = \lim\limits_{h \to 0} \dfrac{f(a+h) - f(a)}{h} = f'(a)$|
|Differentiation and continuity|If $f$ is differentiable at $a$, <br/> then $f$ is continuous at $a$.|
|Non-differentiable conditions|1. a corner <br/> 2. a discontinuity <br/> 3. a vertical tangent|

### Differentiation rules

|Description|Equations|
|-:|:-|
|Constant multiple rule|$\frac{d}{dx}[cf(x)] = c\frac{d}{dx}f(x)$|
|Addition and subtraction rule|$\frac{d}{dx}[f(x)\pm g(x)] = \frac{d}{dx}f(x) \pm \frac{d}{dx}g(x)$|
|Product rule|$\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$|
|Quotient rule <br/> (best practice: use product rule)|$\frac{d}{dx}\dfrac{f(x)}{g(x)} = \dfrac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}$|
|Constant rule|$\frac{d}{dx}c = 0$|
|Power rule|$\frac{d}{dx} x^n = nx^{n-1}$|
|Chain rule|$\dfrac{dy}{dx} = \dfrac{dy}{du}\dfrac{du}{dx} \newline \frac{d}{dx} f(g(x)) = f'(g(x))\cdot g'(x)$|
|Linear approximations|$f(x) \approx f(a) + f'(a)(x-a)$|
|Differentials|$dy = f'(x) \ dx$|

### Special limits

|Description|Equations|
|-:|:-|
|Limit associated with sine|$\lim\limits_{\theta \to 0}\dfrac{\sin\theta}{\theta} = 1$|
|Limit associated with cosine|$\lim\limits_{\theta\to 0}\dfrac{\cos\theta - 1}{\theta} = 0$|
|Definition of $e$|$\lim\limits_{h\to 0}\dfrac{e^h - 1}{h} = 1$|
|$e$ as a limit|$e = \lim\limits_{x\to 0} (1+x)^{1/x}$|
|$e$ as a limit|$e = \lim\limits_{n\to \infin} (1+\frac{1}{n})^{n}$|

### Table of derivatives

|Function $f(x)$|Derivative $f'(x)$|Function $f(x)$|Derivative $f'(x)$|
|-:|:-|-:|:---|
|$c$|$0$|$x^n$|$nx^{n-1}$|
|$x$|$1$|$\lvert x \rvert$|$\dfrac{x}{\lvert x \rvert}$|
|$e^x$|$e^x$|$\ln x$|$\dfrac{1}{x}$|
|$a^x$|$a^x\ln(a)$|$\log_{a}x$|$\dfrac{1}{x\ln(a)}$|
|$\sin x$|$\cos x$|$\sec x$|$\sec x \tan x$|
|$\cos x$|$-\sin x$|$\csc x$|$-\csc x \cot x$|
|$\tan x$|$\sec^2 x$|$\cot x$|$-\csc^2 x$|
|$\arcsin x$|$\dfrac{1}{\sqrt{1-x^2}}$|$\arctan x$|$\dfrac{1}{1+x^2}$|
|$\arccos x$|$\dfrac{-1}{\sqrt{1-x^2}}$

