
## Variational Method

:::{admonition} What you need to know
:class: note


- The Schrodinger equation can only be solved analytically for simple systems, which consist of just one particle. When many particles interact e.g He atom and other mulit-electron systems,  analytic solution is not possible. 
- It is important to develop approximate methods for finding the solutions and to be able to evaluate how close the approximate solution is to the correct one.
- Variational method provides a powerful tool to make systematic  approximations and quantiatively measure convergence of predictions towards true values.
- In variational method one first makes an "educated" guess by picking trial functions for the hamiltonian. One then minimizes parameters of the trial function to get solutions closer to the truth.
- Variational method, when applied to linear combination of trial functions can turn hard QM problem into an easier linear algebra task: solution of systems of linear equations. Instead of solving differentiation equations for eignefunctions/eigenvalues we instead are solving for matrix eigevnalues and eigenvectors.
:::



### Variational theorem

- The variational method states, that for any trial function $\mid \phi \rangle$ The energy computed will always be greater or equal to exact (or true) energy.

$$
E_{\phi}=\frac{\langle \phi \mid \hat{H}  \mid \phi\rangle}{\langle \phi \mid \phi\rangle} \geq E_0
$$

- Where $\hat{H}$ is the Hamiltonian and $E_0$ is the true ground-state energy. Note that the trial function is not generally normalized. The expression simplifies when trial function is normalized beforehand $\langle \phi \mid \phi\rangle=1$

-  If the true ground-state wavefunction $\psi_0$ is inserted in place of $\psi_t$, the equality is reached. For all other wavefunctions (often called trial wavefunctions) the energy expectation value (i.e. the left side) will always be larger. The ratio on the first line is also called the ``Rayleigh ratio''.

**Consequences of Variational theorem**

1. Ground state energy is the lowest possible energy for the system.

2. By minimizing the energy functions we can make most accurate prediction for a given trail function.

3. More parameters give us more handles to vary and get more acurate solutions.


:::{admonition} **Example**
:class: note

Consider a particle in a one-dimensional box problem (boundaries at $0$ and $a$). Use the variational theorem to obtain an upper bound for the ground state energy by using the following normalized wavefunction:

$$\psi_t(x) = \frac{\sqrt{30}}{a^{5/2}}x(a - x)$$
:::

:::{admonition} **Solution**
:class: note, dropdown

Clearly, this is not the correct ground state wavefunction. Next, we check that this wavefunction satisfies the boundary conditions: $\psi_t(0) = 0$ and $\psi_t(a) = 0$ (OK). The Hamiltonian for this problem is:

$$\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}\textnormal{ (}0\le x\le a\textnormal{)}$$

Plugging in both the Hamiltonian and $\psi_t$ into energy expression gives:

$$\int_0^a\psi_t^*\hat{H}\psi_td\tau = -\frac{30\hbar^2}{2a^5m}\int_0^a\left( ax - x^2\right)\frac{d^2}{dx^2}\left( ax - x^2\right)dx$$
$$= \frac{30\hbar^2}{a^5m}\int_0^a\left( ax-x^2\right) dx = \frac{5\hbar^2}{a^2m}\ge E_1$$

As indicated above, this gives an upper limit for the ground state energy $E_1$.
:::


:::{admonition} **Example**
:class: note

- Exact solution for ground state: $\psi(r)=\frac{1}{(\pi a^3_0)^{1/2}}e^{-r/a_0}$ and $E_1 = -0.5 h$

- Use a trial function $\phi=e^{-\alpha r^2}$ to predict ground state energy
:::

:::{admonition} **Solution**
:class: note

- plug the trial function into energy expression computing energy as a function of a parmater $\alpha$

$$
E_{trial} = \frac{\langle \phi \mid \hat{H}  \mid \phi\rangle}{\langle \phi \mid \phi\rangle}
$$


$$
E_{trial}(\alpha) = \frac{4\pi \int^{\infty}_0 \hat{ e^{-\alpha r^2}[-\frac{\hbar^2}{2\mu}\nabla_r^2}-\frac{e^2}{4\pi \epsilon_0 r}] e^{-\alpha r^2} r^2 dr }{4\pi \int^{\infty}_0 e^{-2\alpha r^2} r^2 dr}
$$


$$
E_{trial}(\alpha)=\frac{3\hbar^2 \alpha}{2m_e}-\frac{e^2 \alpha^{1/2}}{\sqrt{2}\epsilon_0 \pi^{3/2}}
$$

- Minimization with respect to paramter $\alpha$ gives the best values of energy


$$
E_{trial}=\frac{3\hbar^2 \alpha}{2m_e}-\frac{e^2 \alpha^{1/2}}{\sqrt{2}\epsilon_0 \pi^{3/2}}
$$

$$
\frac{\partial E_{trial}(\alpha)}{\partial \alpha} = 0
$$

$$
\alpha_{min} = \frac{m_e e^4}{18 \pi^3 \epsilon^2_0 \hbar^4}
$$

- FInally we need to plug this parameter back into energy function to get the  energy minimized with respect to $\alpha$, e.g $E(\alpha_{min})$


$$
E_0 = -0.5 h
$$


$$
E_{trial}(\alpha_{min}) = -0.424
$$

- About 15% error. But hey it is not too bad for a start!
- Adding more parameters and functions will reduce the error.
:::


### Helium atom problem is tough!

- The Schrodinger equation for helium atom is already extremely complicated from the mathematical point of view. No analytic solutions to this equation has been found. However, with certain approximations, useful results can be obtained. The Hamiltonian for He atom can be written as:

$${\hat{H} = \underbrace{-\frac{\hbar^2}{2m_e}\left(\Delta_1 + \Delta_2\right)}_{\textnormal{Kinetic energy}} 
\underbrace{- \frac{1}{4\pi\epsilon_0}\left(\frac{Ze^2}{r_1} + \frac{Ze^2}{r_2} \overbrace{- \frac{e^2}{r_{12}}}^{\textnormal{Tough!!}}\right)}_{\textnormal{Potential energy}}}$$

- where $\Delta_1$ is the Laplacian for the coordinates of electron 1, $\Delta_2$ for electron 2, $r_1$ is the distance of electron 1 from the nucleus, $r_2$ is the distance of electron 2 from the nucleus and $r_{12}$ is the distance between electrons 1 and 2. For He atom $Z = 2$.

### Independent electron apprximation

- Ignore the ``Tough'' term containing $r_{12}$. In this case the Hamiltonian consists of a sum of two hydrogenlike atoms:

$${\hat{H} = \hat{H}_1 + \hat{H}_2}$$

$${\hat{H}_1 = -\frac{\hbar^2}{2m_e}\Delta_1 - \frac{Ze^2}{4\pi\epsilon_0r_1}}$$

$${\hat{H}_2 = -\frac{\hbar^2}{2m_e}\Delta_2 - \frac{Ze^2}{4\pi\epsilon_0r_2}}$$


- Because the Hamiltonian is a sum of two independent parts, the Schr\"odinger equation separates into two (each hydrogelike atom equation):

$${\hat{H}_1\psi(r_1) = E_1\psi(r_1)}$$
$${\hat{H}_2\psi(r_2) = E_2\psi(r_2)}$$

The total energy is a sum of $E_1$ and $E_2$ and the total wavefunction is a product of $\psi(r_1)$ and $\psi(r_2)$. Based on our previous wavefunction table for hydrogenlike atoms, we have:

$${E = E_1 + E_2 = -RZ^2\left(\frac{1}{n_1^2} + \frac{1}{n_2^2}\right)}$$

$${\psi(r_1)\psi(r_2) = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_1/a_0}\frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_2/a_0}
=\frac{1}{\pi}\left(\frac{Z}{a_0}\right)^3e^{-Z(r_1 + r_2)/a_0}}$$

### Consequences of independent electron approximation
- For a ground state He atom both electron reside on the lowest energy orbital and therefore the total wavefunction is $\psi(r_1,r_2) = \psi(r_1)\psi(r_2) = \psi(1)\psi(2) = 1s(1)1s(2)$. The energy obtained from this approximation is not sufficiently accurate (missing electron -- electron repulsion) but the wavefunction can be used for qualitative analysis. The variational principle  gives a systematic way to asses how good our approximation is. 
- The exact ground state energy has been found (very extensive analytic \& numerical calculations) as -79.0 eV. By using the approximate wavefunction, we can calculate the expectation value for energy. This yields -74.8 eV and thus the error in energy for this wavefunction is -5.2 eV. Note that the approximate value is, in accordance with the variational principle, higher than the true energy.

### A better approximation

- We can take the wavefunction from the previous step and use the nuclear charge $Z$ as a variational parameter. The variational principle states that minimization of the energy expectation value with respect to $Z$ should approach the true value from above (but obviously will not reach it). 
- By judging the energy, we can say that this new wavefunction is better than the previous wavefunction. The obtained value of $Z$ is less than the true $Z$ (= 2). This can be understood in terms of electrons shielding the nucleus from each other and hence giving a reduced nuclear charge. 

$${E = \langle\psi |\hat{H}|\psi\rangle = ... = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}}$$


- In order to minimize this expression we should differentiate it with respect to $Z$ and set it to zero (extremum point; here it is clear that this point is a minimum):

$${\frac{dE}{dZ} = \left(2Z - \frac{27}{8}\right)\frac{e^2}{4\pi\epsilon_0a_0} = 0}$$


- The above equation gives $Z = 27/16 \approx 1.7$ and $E \approx -77.5$ eV (previous -74.8 eV and exact -79.0 eV). This result could be improved by adding more terms and variables into
the trial wavefunction. For example, higher hydrogenlike atom orbitals with appropriate variational coefficients would yield a much better result.


- Another type of approximate method is based on \underline{perturbation theory}, which would typically assume that the electron -- electron repulsion is treated as an additional (small) perturbation to case 1) above.

### Problems

#### Problem-1

Use the variational principle to obtain the lowest energy solution to the hydrogen atom Schrodinger equation in spherical coordinates by using the following trial wavefunctions:
- (a) $\psi_{trial} = e^{-kr}$ with $k$ as a variational parameter.
- (b) $\psi_{trial} = e^{-kr^2}$ with $k$ as a variational parameter.

- Note that both trial functions depend only on $r$ and the angular terms disappear
from the Laplacian. You may find the following integrals useful:


$$\int_0^\infty x^ne^{-ax}dx = \frac{n!}{a^{n+1}}$$

$$\int_0^\infty x^me^{-ax^2}dx = \frac{\Gamma[(m + 1)/2]}{2a^{(m + 1) / 2}}$$

$$\Gamma[n + 1] = n!$$

$$\Gamma[n + 1] = n\Gamma[n]$$

$$\Gamma\left[\frac{1}{2}\right] = \sqrt{\pi}$$



:::{dropdown} **Solution**
Use the variational principle and employ spherical coordinates in integrations:\\

$E = \frac{\int\psi^*_{trial}H\psi_{trial}d\tau}{\int\psi^*_{trial}\psi_{trial}d\tau}$


$$\int\psi^*_{trial}\psi_{trial}d\tau = \int_0^\infty e^{-2kr}
\underbrace{4\pi r^2dr}_{d\tau} = 4\pi\int_0^\infty r^2e^{-2kr}dr
= \frac{\pi}{k^3}$$

$$\int\psi_{trial}^*H\psi_{trial}d\tau = \int\left( e^{-kr}\right)
\left( -\frac{\hbar^2}{2m_e}\Delta - \frac{e^2}{4\pi\epsilon_0r}\right)
\left( e^{-kr}\right)d\tau$$

$$= \int_0^\infty\left( e^{-kr}\right)
\left( -\frac{\hbar^2}{2m_e}\left[\frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}
{\partial r}\right] - \frac{e^2}{4\pi\epsilon_0r}\right)\left( e^{-kr}\right)
\left( 4\pi r^2dr\right)$$

$$= -\frac{4\pi\hbar^2}{2m_e}\int_0^\infty \left( e^{-kr}\right)
\left( k^2e^{-kr} - \frac{2k}{r}e^{-kr}\right)r^2dr 
- \frac{e^2}{\epsilon_0}\int_0^\infty\frac{e^{-2kr}}{r}r^2dr$$

$$= -\frac{4\pi\hbar^2}{2m_e}\int_0^\infty e^{-2kr}(r^2k^2 - 2kr)dr
- \frac{e^2}{\epsilon_0}\int_0^\infty re^{-2kr}dr$$

$$= -\frac{2\pi\hbar^2k^2}{m_e}\underbrace{\int_0^\infty r^2 e^{-2kr}dr}_{= \frac{2}{(2k)^3}}
+ \frac{4\pi\hbar^2k}{m_e}\underbrace{\int_0^\infty re^{-2kr}dr}_{= 
\frac{1}{(2k)^2}} - \frac{e^2}{\epsilon_0}\underbrace{\int_0^\infty
re^{-2kr}dr}_{= \frac{1}{(2k)^2}}$$

$$= -\frac{\pi\hbar^2}{2m_ek} + \frac{\pi\hbar^2}{m_ek}
- \frac{e^2}{4k^2\epsilon_0}$$


These results give:

$$\frac{\int\psi^*H\psi d\tau}{\int\psi^*\psi d\tau} =
\left( -\frac{\pi\hbar^2}{2m_ek} + \frac{\pi\hbar^2}{m_ek}
- \frac{e^2}{4k^2\epsilon_0}\right) / \left( \pi / k^3\right)$$

$$ = -\frac{\hbar^2k^2}{2m_e} + \frac{\hbar^2k^2}{m_e} - \frac{e^2k}
{4\pi\epsilon_0} = \frac{\hbar^2k^2}{2m_e} - \frac{e^2k}{4\pi\epsilon_0}$$


This expression must be minimized with respect to variational parameter
$k$:

$$\frac{dE}{dk} = d\left( \frac{\hbar^2k^2}{2m_e} - \frac{e^2k}
{4\pi\epsilon_0}\right) / dk = \frac{\hbar^2k}{m_e} - \frac{e^2}
{4\pi\epsilon_0} = 0$$

$$\Rightarrow k = \frac{m_ee^2}{4\pi\epsilon_0\hbar^2} \Rightarrow
E = -\frac{1}{2}\frac{m_ee^4}{(4\epsilon_0)^2\hbar^2} = -hcR$$


where $R$ is the Rydberg constant.


**b)** The logic is exactly the same as in part a).

$$\int\psi^*_{trial}\psi_{trial}d\tau = \int_0^\infty e^{-2kr^2}
\underbrace{4\pi r^2dr}_{d\tau} = \frac{4\pi\Gamma[3/2]}{2(2k)^{3/2}}
= \frac{\pi^{3/2}}{(2k)^{3/2}}$$

\noindent
The Laplacian of this function is given by:

$$\Delta\psi_{trial} = \frac{\partial}{\partial r}\left( -2kre^{-kr^2}
\right) + \frac{2}{r}\left( -2kr\right)e^{-kr^2} = \left( 4k^2r^2
- 6k\right) e^{-kr^2}$$


Thus the energy expectation value is (without normalization):\\

$$\int_o^\infty\left( -\frac{2\hbar^2k^2r^2}{m_e} + \frac{3k\hbar^2}
{m_e} - \frac{e^2}{4\pi\epsilon_0}\frac{1}{r}\right)e^{-2kr^2}\times
4\pi r^2dr$$

$$= 4\pi\int_0^\infty\left( -\frac{2\hbar^2k^2r^4}{m_e} 
+ \frac{3k\hbar^2r^2}{m_e} - \frac{e^2r}{4\pi\epsilon_0}\right) e^{-2kr^2}dr$$

$$= -\frac{8\pi\hbar^2k^2}{m_e}\underbrace{\int_0^\infty r^4 
e^{-2kr^2}dr}_{\frac{\Gamma[5/2]}{2(2k)^{5/2}} = \frac{3\sqrt{\pi}}{8(2k)^{5/2}}}
+ \underbrace{\frac{12\pi k\hbar^2}{m_e}\int_o^\infty 
r^2e^{-2kr^2}dr}_{\frac{\Gamma[3/2]}{2(2k)^{3/2}} = \frac{\sqrt{\pi}}{4(2k)^{3/2}}}
- \frac{e^2}{\epsilon_0}\underbrace{\int_0^\infty 
re^{-2kr^2}dr}_{\frac{\Gamma[1]}{2(2k)} = 1/(4k)}
$$

$$= - \frac{3\pi^{3/2}\hbar^2}{4m_e\sqrt{2k}} + \frac{3\pi^{3/2}\hbar^2}
{2m_e\sqrt{2k}} - \frac{e^2}{4\epsilon_0k}$$

$$\Rightarrow \frac{\int\psi^*_{trial}\psi_{trial}d\tau}
{\int\psi^*_{trial}\psi_{trial}d\tau} 
= \frac{-\frac{3\pi^{3/2}\hbar^2}{4m_e\sqrt{2k}} + \frac{3\pi^{3/2}\hbar^2}
{2m_e\sqrt{2k}} - \frac{e^2}{4\epsilon_0k}}{\frac{\pi^{3/2}}{(2k)^{3/2}}}
= -\frac{3\hbar^2k}{2m_e} + \frac{6\hbar^2k}{2m_e} - \frac{e^2\sqrt{2k}}
{2\pi^{3/2}\epsilon_0}
$$

$$= \frac{3\hbar^2k}{2m_e} - \frac{e^2\sqrt{k}}{\sqrt{2}\pi^{3/2}\epsilon_0}$$


To find the minimum value for energy (with respect to $k$), we calculate
the first derivative and set it to zero:\\

$$E = \frac{3\hbar^2k}{2m_e} - \frac{e^2\sqrt{k}}{\sqrt{2}\pi^{3/2}\epsilon_0}$$

$$\Rightarrow \frac{\partial E}{\partial k} = \frac{3\hbar^2}{2m_e}
- \frac{e^2}{2\sqrt{2}\pi^{3/2}\epsilon_0\sqrt{k}} = 0$$

$$\Rightarrow k=\left(\frac{m_ee^2}{3\sqrt{2}\pi^{3/2}\epsilon_0\hbar^2}
\right)^2 = \frac{m_e^2e^4}{18\pi^3\epsilon_0^2\hbar^4}$$


The total energy at this point is:

$$E = \frac{3\hbar^2}{2m_e}\times\frac{m_e^2e^4}{18\pi^3\epsilon_0^2
\hbar^4} - \frac{e^2}{\sqrt{2}\pi^{3/2}\epsilon_0}\times
\frac{m_ee^2}{3\sqrt{2}\pi^{3/2}\epsilon_0\hbar^2}
= \frac{m_ee^4}{12\pi^3\epsilon_0^2\hbar^2} - \frac{2m_ee^4}
{12\pi^3\epsilon^2_0\hbar^2}$$

$$ = -\frac{m_ee^4}{12\pi^3\epsilon_0^2\hbar^2} = -\frac{8}{3\pi}hcR \approx -0.85hcR$$


**c)** The function in a) gives lower energy and therefore that trial function
is better.
:::