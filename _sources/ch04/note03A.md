## Harmonic Oscillator 

```{admonition} What you need to know
:class: note
In this section we study quantum mechanical version of [harmonic oscillator](https://en.wikipedia.org/wiki/Harmonic_oscillator). Harmonic oscillators have ubqiutuous presence in everyday world: beads bound by a spring which vibrate around equilibirum positions. Turns out beads on a pring is remarkably common in microsocpic world as nuclie of atoms in solids or molecules are in some sense "quantum beads" vibrating around equilibriu position of "quantum springs". The distinction between quantum vs classical regimes will again be highly illuminating about the role of quantum effects on small scales. The key topics we will learn are:

- **Quantization of vibrations in molecules.** Vibrational degrees of freedom are quantized which has implications for infrared and raman spectroscopies and bonding. 
- **Existence of zero point energy and tunneling.** Enenergy is not zero even at zero temperature. We appreciate this as a consequence of uncertainty relation.  
- **Hermite Polynomials are eigenfunctions** 
- **Effects of unharmonicity.** We will see the impact on energy levels of harmonic oscillators when one goes beyond harmonic approximation. 
- **Raising and lower operators offer an elegant way of solving harmonic oscilator problem** This will be our first introduction to raising and lowering operators which provide highly elegant way of solving problems in quantum mechanics. 
```

### Bead, spring and a wall. 

![](images/harm-osc1.png)

- The classical **harmonic oscillator** is a system of bead attached to a wall with a spring. When bead is displaced from its equilibrium or resting position $r_0$ to some point $r$, experiences a restoring force $F$ proportional to the displacement $x=r-r_0$:

$$F=-kx$$

- The above expression is also known as **Hooke's law**, where minus sign indicates that the direction of force is always towards restoring equilibrium location. The constant k characterizes stiffness of the spring and is called **spring constant.**

![](images/harm-osc1.png)

![](https://askeyphysics.files.wordpress.com/2011/08/solveharmonic.gif)



### Solving harmonic oscillator problem

- The classical equation of motion for a one-dimensional simple harmonic oscillator with a particle of mass m attached to a spring having spring constant k generates mechanical waves.

$$m \ddot x=−kx$$

$$m \ddot x+kx = 0 \,\,\,\,\rightarrow \,\,\,\, \ddot{x}+\omega^2 x =0$$

- The intorduced constant $\omega$ will be seen as the **frequency oscillations**.Note that frequency is inversly porportional to mass (heavier objects with same spring constant oscillate rapdily around equilibrium) and proprotional to spring constant (stiffer springs increase oscillations around equilibrium for same mass)

$$\omega=\Big(\frac{k}{m}\Big)^{1/2}$$

- The differneital equation is a simple second order, linear ODE  which can be solved by a standard trick of pluggin exponential $x(t)=e^{\alpha t}$ and convertin the problem to algebraic equation. The solution is

$$x(t)= A sin(\omega t+\phi)$$ 

- The two constnants  are: $A$ the **amplitude of oscillations** and $\phi$ is constant specifying the initial position of the bead. 

### Energy of the harmonic oscillator

- In classical mechanics the force and the potential energy of a conservative system are related via the formula:

$$F = - \frac{\partial V(x)}{\partial x} $$

- This means the steeper the potential the higher the force and minus sign indicates that force is restoring the equilibrium position. The potential energy can be obtained by integrating:

$$ V(x)= - \int F dx = - \int (-kx) dx =\frac{kx^2}{2}+C$$

- Thus the potential energy for a simple harmoncin oscillator is a parabolic function of displacement. It is  convenient  to set $C=0$ and measure potential energy relative to equilibrium state $V(x=0)=0$ 

- The total energy consisting of kinetic and potential enregies will be used to obtain Schordinger equation.

$$E=\frac{p^2}{2m} + \frac{kx^2}{2}$$

### Conservative system 


:::{figure-md} markdown-fig
<img src="https://www.physicslens.com/wp-content/uploads/2021/11/simple-harmonic-motion-graphs.gif" alt="compton" class="bg-primary mb-1" width="300px">

The harmonic oscilator (in a vacuum) is a conservative system becasue the kinetic and potential energies keep being interconverted with no amount of total energy being dissipated into the environment. Oscillations go on forever with position $x(t)$ velocity $v=\dot{x}(t)$ and acceleration $a=\ddot{x(t)}$ with same constant frequency $\omega$ but with different amplitudes.
:::


### Diatomic molecule and two-body problem


:::{figure-md} markdown-fig
<img src="images/osc-2.jpeg" alt="compton" class="bg-primary mb-1" width="300px">

Equations of motion for diatomic molecule modeled as beads bound by a spring are:

$$F_1=m_1 \ddot{x_1}=k(x_2-x_1-l_0)$$

$$F_2=m_2 \ddot{x_2}=-k(x_2-x_1-l_0)$$

Where $F_1=-F_2$ which is a reflection of Newtno's thrid law. By introducing a more convenient cooridnates in the from of relative distance $x$ and center of mass $x_{com}$ we are now going to reduce the two body problem to one body problem.

$$x=x_2-x_1-l_0$$

$$x_{com}=\frac{m_1x_2+x_2 m_2}{m_1+m_2}$$
:::

- Diatomic molecule is stable because the same force is acting on both ends

$$m_1\ddot{x_1}=kx \\  m_2\ddot{x_2}=-kx$$

- By expressing equations of motion in terms of the center of mass which, we find that center of mass moves freely without acceleration. 

$$m_1\ddot{x_1}+ m_2\ddot{x_2}=0\,\,\,\, \rightarrow \frac{m_1\ddot{x_1}+ m_2\ddot{x_2}}{m_1+m_2}=\ddot{x}_{com}=0$$

- Next by taking difference between coordinates $\ddot{x_2}=-\frac{k}{m_2}x_2$ and  $\ddot{x_1}=\frac{k}{m_1}x_1$we expres  the equations of motion in terms of relative distance

$$\ddot{x}=\ddot{x_2} - \ddot{x_1} =-\Big(\frac{1}{m_1}+\frac{1}{m_2} \Big)kx=-\frac{k}{\mu}x$$

- This equation looks identical to the probem of bead anchored to wall with a spring. We have thus managed to reduce the two body probelm to a one modey problem by replacing masses of bodies with a reduced mass:  $\mu=\frac{1}{m_1}+\frac{1}{m_2}=\frac{m_1 m_2}{m_1+m_2}$



### Beads and springs model of molecules

- Before discussing the harmonic oscillator approximation let us reflect on when this would be a good approximation and uner which cirumstances it will break down? For an aribtarry potential energy funciton of x we can carry out Taylor's expansion around equilibrium bond length $x_0$ obtaining infinitey series. 

$$U(x) = U(x_0)+U'(x_0)(x-x_0)+\frac{1}{2!}U''(x_0)(x-x_0)^2+\frac{1}{3!}U'''(x_0)(x-x_0)^3+...$$


:::{figure-md} markdown-fig
<img src="images/harm_approx.png" alt="compton" class="bg-primary mb-1" width="300px">

Deviation from simple harmonic potential approximation (red curve) of true/exact potential (blue curve) with cubic term (green)
:::

- Setting energy scale to be relative to  $U(x_0)=0$ and recongizing that first derivative vanishes at minima $x_0$ we have

$$U(x) = \frac{1}{2!}k(x-x_0)^2+\frac{1}{3!}\gamma(x-x_0)^3+...$$

- Hence we see that the Harmonic approximation is only the first non vanishing term! Furthermore we see that spring constant k and subsequent anharmonicity consnats such as $\gamma$ are higher order derivatives of potential energy. That is the more non-linear the potential the higer the contribution of these terms. And vice verse clsoer the potential to quadratic form the more accurate is the harmonic assumtion. 


## Quantum harmonic oscillator


- Taking the classical Hamiltonian for a harmonic oscillator is given by:

$${H =  \frac{1}{2\mu}p_x^2 + \frac{1}{2}kx^2}$$


- The [quantum mechanicalm harmonic oscillator](http://en.wikipedia.org/wiki/Quantum_harmonic_oscillator) is obtained by replacing the classical position and momentum by the corresponding quantum mechanical operators

$${\hat{H} = -\frac{\hbar^2}{2\mu}\frac{d^2}{dx^2} + \frac{1}{2}kx^2 }$$

- Note that the potential term may be expressed in terms of three parameters becasue of $k=\frac{\mu}{\omega}$ and $\omega=2\pi \nu$ relations

| $k$      | Force constant (kg $s^{-2}$)                                |
|----------|-------------------------------------------------------------|
| $\omega$ | Angular frequency ($\omega = 2\pi\nu$; Hz)                  |
| $\nu$    | Frequency (Hz; do not confuse this with quantum number $v$) |


- Depending on the context any of these constants may be used to specify the harmonic potential.

### Eigenfunctions and Eiganvalues 

$$\hat{H}\psi_v = E_v\psi_v$$

- The solutions to this equation produce eiganvalues (Energies) 

$${E_v = \left(v + \frac{1}{2}\right)h\nu = \left(v + \frac{1}{2}\right)\hbar\omega\textnormal{ where }v=0,1,2,3...}$$

- Eigenfunctions  (position wavefunctions)

$${\psi_v = N_v\times\overbrace{H_v\left(\sqrt{\alpha}x\right)}^{\textnormal{Hermite polynomial}}\times e^{-\alpha x^2/2}\textnormal{ where }\alpha = \sqrt{\frac{k\mu}{\hbar^2}}}$$

- Normalization factor ${N_v = \frac{1}{\sqrt{2^vv!}}\left(\frac{\alpha}{\pi}\right)^{1/4}}$

- where $H_v$'s are called [Hermite polynomials](http://en.wikipedia.org/wiki/Hermite_polynomials).

| n  | Hermite Polynomial $( H_n(x))$ |
|----|---------------------------------|
| 0  | $1$                               |
| 1  | $2x$                              |
| 2  | $4x^2 - 2$                        |
| 3  | $8x^3 - 12x$                      |
| 4  | $16x^4 - 48x^2 + 12$              |


For example, the wavefunctions for the two lowest states are:

$${\psi_0(x) = \left(\frac{\alpha}{\pi}\right)^{1/4}e^{-\alpha x^2/2}}$$

$${\psi_1(x) = \left(\frac{4\alpha^3}{\pi}\right)^{1/4} x e^{-\alpha x^2/2}}$$

:::{figure-md} markdown-fig

<img src="https://miro.medium.com/v2/resize:fit:1400/1*cn1pToIWATO5Am2bAv8b8Q.png" alt="ho1" class="bg-primary mb-1" width="500px">

Eigenfunctions and Eigenvalues of Harmonic Oscillator
:::

### Interpreting solutions

:::{figure-md} markdown-fig

<img src="./images/classical_quantum_ho.gif" alt="ho2" class="bg-primary mb-1" width="500px">

Classical vs quantum probabilities of finding oscillating particle at position x
:::



Some of the lowest state solutions to the harmonic oscillator (HO) problem are displayed below:


- Solutions $\psi_v$ with $v = 0, 2, 4, ...$ are even: $\psi_v(x) = \psi_v(-x)$.
-  Solutions $\psi_v$ with $v = 1, 3, 5, ...$ are odd: $\psi_v(x) = -\psi_v(-x)$.
- Integral of an odd function from $-a$ to $a$ ($a$ may be $\infty$) is zero.
- The tails of the wavefunctions penetrate into the potential barrier deeper than the classical physics would allow. This phenomenon is called quantum mechanical tunneling.

### Hermite Polynomials

The following realtions are useful when working with [Hermite polynomials](http://en.wikipedia.org/wiki/Hermite_polynomials):

$${H_v''(y) - 2yH_v'(y) + 2vH_v(y) = 0\textnormal{ (characteristic equation)}}$$

$${H_{v+1}(y) = 2yH_v(y) - 2vH_{v-1}(y)\textnormal{ (recursion relation)}}$$
$${\int\limits_{-\infty}^{\infty}H_{v'}(y)H_v(y)e^{-y^2}dy = \left\lbrace\begin{matrix}
0, & \textnormal{ if }v' \ne v\\
\sqrt{\pi}2^vv!, & \textnormal{ if }v' = v\\
\end{matrix}\right.
}$$

### Examples

:::{admonition} **Example**  
:class: note

Show that the lowest level of Harmonic oscillator obeys the uncertainty principle.
:::

:::{admonition} **Solution**
:class: dropdown

$$\Delta x = \sigma_x = \sqrt{\left<\hat{x}^2\right> - \left<\hat{x}\right>^2}\textnormal{ and }\Delta p_x = \sigma_{p_x} = \sqrt{\left<\hat{p}_x^2\right> - \left<\hat{p}_x\right>^2}$$

First we calculate $\left<\hat{x}\right>$ ($\psi_0$ is an even function, $x$ is odd, the integrand is odd overall):

$$\left<\hat{x}\right> = \int\limits_{-\infty}^{\infty} \psi_0(x)x\psi_0(x)dx = 0$$


For $\left<\hat{x}^2\right>$ we have (integration by parts or tablebook):

$$\left<\hat{x}^2\right> = \int\limits_{-\infty}^{\infty} \psi_0(x)x^2\psi_0(x)dx = \left(\frac{\alpha}{\pi}\right)^{1/2}\int\limits_{-\infty}^{\infty}x^2e^{-\alpha x^2}dx = \left(\frac{\alpha}{\pi}\right)^{1/2} \left[\frac{1}{2\alpha}\left(\frac{\pi}{\alpha}\right)^{1/2}\right]$$


$$= \frac{1}{2\alpha} = \frac{1}{2}\frac{\hbar}{\sqrt{\mu k}} \Rightarrow \Delta x = \sqrt{\frac{1}{2}\frac{\hbar}{\sqrt{\mu k}}}$$

For $\left<\hat{p}_x\right>$ we have again by symmetry:

$$\left<\hat{p}_x\right> = \int\limits_{-\infty}^{\infty} \underbrace{\psi_0(x)}_{\textnormal{even}} \underbrace{\left(-i\hbar\frac{d}{d x}\right) \underbrace{\psi_0(x)}_{\textnormal{even}}}_{\textnormal{odd}} dx = 0$$

Note that derivative of an even function is an odd function. For $\left<\hat{p}_x^2\right>$ we have:

$$\left<\hat{p}_x^2\right> = \int\limits_{-\infty}^{\infty} \psi_0(x)p_x^2\psi_0(x)dx = -\hbar^2\left(\frac{\alpha}{\pi}\right)^{1/2}\int\limits_{-\infty}^{\infty} e^{-\alpha x^2/2} \frac{d^2}{dx^2} e^{-\alpha x^2/2} dx$$
$$= \hbar^2\left(\frac{\alpha}{\pi}\right)^{1/2} \int\limits_{-\infty}^{\infty} (\alpha - \alpha^2 x^2)e^{-\alpha x^2}dx = \left[\hbar^2\left(\frac{\alpha}{\pi}\right)^{1/2}\right]$$
$$\times\left(\alpha\int\limits_{-\infty}^{\infty} e^{-\alpha x^2}dx - \alpha^2\int\limits_{-\infty}^{\infty}x^2e^{-\alpha x^2}dx\right)$$



$$ = \underbrace{\left[\hbar^2\left(\frac{\alpha}{\pi}\right)^{1/2}\right]\times \left(\alpha\sqrt{\frac{\pi}{\alpha}} - \alpha^2 \frac{\sqrt{\pi}}{2\alpha^{3/2}}\right)}_{\textnormal{\href{http://en.wikipedia.org/wiki/Gaussian_integral}{\underline{tablebook}}}}$$
$$ = \left[\hbar^2\sqrt{\frac{\alpha}{\pi}}\right]\times\left(\sqrt{\pi\alpha} - \frac{\sqrt{\pi\alpha}}{2}\right) = \frac{\hbar^2\alpha}{2} = \frac{\hbar\sqrt{\mu k}}{2} \Rightarrow \Delta p_x = \sqrt{\frac{\hbar\sqrt{\mu k}}{2}}$$

Finally, we can calculate $\Delta x\Delta p_x$:

$$\Delta x\Delta p_x = \sqrt{\frac{1}{2}\frac{\hbar}{\sqrt{\mu k}}}\times \sqrt{\frac{\hbar\sqrt{\mu k}}{2}} = \sqrt{\frac{\hbar^2}{4}} = \frac{\hbar}{2}$$

Recall that the uncertainty principle stated that: $\Delta x\Delta p_x \ge \frac{\hbar}{2}$


Thus we can conclude that $\psi_0$ fulfills the Heisenberg uncertainty principle.
:::




:::{admonition} **Example**  
:class: note

Quantization of nuclear motion. [Molecular vibration](http://en.wikipedia.org/wiki/Molecular_vibration) in a diatomic molecule can be approximated by the quantum mechanical harmonic oscillator model. There $\mu$ is the reduced mass as given previously and the variable $x$ is the distance between the atoms in the molecule (or more exactly, the deviation from the equilibrium bond length $R_e$).\\

- a. Derive the expression for the standard deviation of the bond length in a diatomic molecule when it is in its ground vibrational state.\\
- b. What percentage of the equilibrium bond length is this standard deviation for carbon monoxide in its ground vibrational state? For $^{12}C^{16}O$, we have:
$\tilde{v}$ = 2170 cm$^{-1}$ (vibrational frequency) and $R_e$ = 113 pm (equilibrium bond length)
:::


:::{admonition} **Solution**
:class: dropdown

The harmonic vibration frequency is given in wavenumber units ($cm^{-1}$). This must be converted according to: $\nu = c\tilde{v}$. The previous example gives expression for $\sigma_x$:

$$\sigma_x = \Delta x = \sqrt{\frac{1}{2}\frac{\hbar}{\sqrt{\mu k}}}$$

In considering spectroscopic data, it is convenient to express this in terms of $\tilde{v}$:

$$k = \left(2\pi c\tilde{v}\right)^2\mu\textnormal{ and }\Delta x = \sigma_x = \sqrt{\frac{\hbar}{4\pi c\tilde{v}\mu}}$$


In part (b) we have to apply the above expression to find out the standard deviation for carbon monoxide bond length in its ground vibrational state. First we need the reduced mass:

$$\mu = \frac{m_1m_2}{m_1 + m_2} = \frac{(12\times 10^{-3}\textnormal{ kg mol}^{-1})(15.995\times 10^{-3}\textnormal{ kg mol}^{-1})}
{((12 + 15.995)\times 10^{-3}\textnormal{ kg mol}^{-1})\underbrace{(6.022\times 10^{23}\textnormal{ mol}^{-1})}_{\textnormal{Avogadro's constant}}}$$
$$ = 1.139\times 10^{-26}\textnormal{ kg}$$

The standard deviation is now:

$$\Delta x = \sigma_x = \left[\frac{1.055\times 10^{-34}\textnormal{ Js}}{4\pi\underbrace{\left(2.998\times 10^{10}\textnormal{ cm s}^{-1}\right)}_{\textnormal{speed of light}}\left(2170\textnormal{ cm}^{-1}\right)\left(1.139\times 10^{-26}\textnormal{ kg}\right)}\right]^{1/2}$$
$$ = 3.37\textnormal{ pm} \Rightarrow \textnormal{\% of deviation} = 100\%\times\frac{3.37\textnormal{ pm}}{113\textnormal{ pm}} = 2.98\%$$
:::




### Harmonic Oscillator in 3D


In a three-dimensional harmonic oscillator potential, $V(x,y,z) = \frac{1}{2}k_xx^2 + \frac{1}{2}k_yy^2 + \frac{1}{2}k_zz^2$, the separation technique similar to the three-dimensional particle in a box problem can be used. The resulting eigenfunctions and eigenvalues are:

$${E = \left(v_x + \frac{1}{2}\right)h\nu_x + \left(v_y + \frac{1}{2}\right)h\nu_y + \left(v_z + \frac{1}{2}\right)h\nu_z}
{\psi(x,y,z) = N_{v_x}H_{v_x}\left(\sqrt{\alpha_x}x\right)e^{-\alpha_xx^2/2}}
{ \times N_{v_y}H_{v_y}\left(\sqrt{\alpha_y}y\right)e^{-\alpha_yy^2/2} \times N_{v_z}H_{v_z}\left(\sqrt{\alpha_z}z\right)e^{-\alpha_zz^2/2}}$$

where the $\alpha$, $N$, and $H$ are defined in above and the $v$'s are the quantum numbers along the Cartesian coordinates.
