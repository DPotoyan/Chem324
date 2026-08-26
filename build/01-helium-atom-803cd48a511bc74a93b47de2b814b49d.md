---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Helium Atom

:::{note} **What you will learn**

- **Why helium is hard:** The two-electron Schrodinger equation contains an electron, electron repulsion term $1/r_{12}$ that prevents an exact analytic solution.
- **The independent-electron approximation:** Dropping the repulsion term turns helium into two hydrogenlike atoms, giving a separable problem and a first estimate of the energy.
- **The variational principle in action:** Treating the nuclear charge $Z$ as an adjustable parameter improves the energy from above and introduces the idea of nuclear shielding.
- **How good is good enough:** We compare approximate ground-state energies against the essentially exact value of $-79.0$ eV and learn to read the error.
:::

## The Helium Hamiltonian

The Schrodinger equation for the helium atom is already extremely complicated from a mathematical point of view. No analytic solution to this equation has been found. However, with certain approximations, useful results can be obtained. The Hamiltonian for the He atom can be written as:

$${\hat{H} = \underbrace{-\frac{\hbar^2}{2m_e}\left(\Delta_1 + \Delta_2\right)}_{\textnormal{Kinetic energy}}
\underbrace{- \frac{1}{4\pi\epsilon_0}\left(\frac{Ze^2}{r_1} + \frac{Ze^2}{r_2} \overbrace{- \frac{e^2}{r_{12}}}^{\textnormal{Tough!!}}\right)}_{\textnormal{Potential energy}}}$$

where $\Delta_1$ is the Laplacian for the coordinates of electron 1, $\Delta_2$ for electron 2, $r_1$ is the distance of electron 1 from the nucleus, $r_2$ is the distance of electron 2 from the nucleus, and $r_{12}$ is the distance between electrons 1 and 2. For the He atom $Z = 2$.

The term that makes this problem unsolvable is the electron, electron repulsion $e^2/r_{12}$. It couples the two electron coordinates so that the Hamiltonian no longer separates into independent one-electron pieces.

## The Independent-Electron Approximation

A first approximation is to ignore the "tough" term containing $r_{12}$. In this case the Hamiltonian becomes a sum of two hydrogenlike atoms:

$${\hat{H} = \hat{H}_1 + \hat{H}_2}$$

$${\hat{H}_1 = -\frac{\hbar^2}{2m_e}\Delta_1 - \frac{Ze^2}{4\pi\epsilon_0r_1}}$$

$${\hat{H}_2 = -\frac{\hbar^2}{2m_e}\Delta_2 - \frac{Ze^2}{4\pi\epsilon_0r_2}}$$

Because the Hamiltonian is a sum of two independent parts, the Schrodinger equation separates into two equations, each a hydrogenlike atom problem:

$${\hat{H}_1\psi(r_1) = E_1\psi(r_1)}$$

$${\hat{H}_2\psi(r_2) = E_2\psi(r_2)}$$

The total energy is the sum of $E_1$ and $E_2$, and the total wavefunction is a product of $\psi(r_1)$ and $\psi(r_2)$. Based on our previous wavefunction table for hydrogenlike atoms, we have:

:::{important} **Separable two-electron solution**

$${E = E_1 + E_2 = -RZ^2\left(\frac{1}{n_1^2} + \frac{1}{n_2^2}\right)}$$

$${\psi(r_1)\psi(r_2) = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_1/a_0}\frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_2/a_0}
= \frac{1}{\pi}\left(\frac{Z}{a_0}\right)^3e^{-Z(r_1 + r_2)/a_0}}$$

:::

For a ground-state He atom both electrons reside in the lowest-energy orbital, so the total wavefunction is

$$\psi(r_1,r_2) = \psi(r_1)\psi(r_2) = \psi(1)\psi(2) = 1s(1)1s(2).$$

The energy obtained from this approximation is not sufficiently accurate (it misses electron, electron repulsion) but the wavefunction can be used for qualitative analysis. The variational principle gives a systematic way to assess how good our approximation is.

:::{tip} **Comparing with the exact answer**

The exact ground-state energy has been found, after very extensive analytic and numerical calculations, to be $-79.0$ eV. Using the approximate wavefunction above to calculate the expectation value for energy yields $-74.8$ eV, so the error in energy for this wavefunction is about $5.2$ eV. Note that the approximate value is, in accordance with the variational principle, higher than the true energy.
:::

## A Better Approximation: Variational Nuclear Charge

We can take the wavefunction from the previous step and use the nuclear charge $Z$ as a variational parameter. The variational principle states that minimization of the energy expectation value with respect to $Z$ should approach the true value from above (but obviously will not reach it).

By judging the energy, we can say that this new wavefunction is better than the previous one. The obtained value of $Z$ is less than the true $Z$ ($=2$). This can be understood in terms of electrons shielding the nucleus from each other and hence giving a reduced effective nuclear charge.

If this trial wavefunction is used in calculating the energy expectation value, we get:

$${E = \langle\psi |\hat{H}|\psi\rangle = \cdots = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}}$$

In order to minimize the energy we differentiate it with respect to $Z$ and set the result to zero (an extremum point; here it is clear that this point is a minimum):

$${\frac{dE}{dZ} = \left(2Z - \frac{27}{8}\right)\frac{e^2}{4\pi\epsilon_0a_0} = 0}$$

:::{important} **Optimal effective charge for helium**

$${Z = \frac{27}{16} \approx 1.7, \qquad E \approx -77.5 \textnormal{ eV}}$$

(compared with $-74.8$ eV for $Z = 2$ and the exact $-79.0$ eV).
:::

This result could be improved by adding more terms and variables to the trial wavefunction. For example, higher hydrogenlike orbitals with appropriate variational coefficients would yield a much better result.

Another type of approximate method is based on **perturbation theory**, which would typically treat the electron, electron repulsion as an additional (small) perturbation to the independent-electron case above.

:::{tip} **The lesson of helium**

Even the simplest two-electron atom has no closed-form solution. Two themes that recur throughout multi-electron quantum chemistry already appear here: (1) we build approximate wavefunctions from hydrogenlike orbitals, and (2) we use the variational principle to systematically improve them. The reduced effective charge $Z \approx 1.7$ is our first quantitative encounter with **shielding**, which the next pages develop into a full picture of multi-electron atoms.
:::
