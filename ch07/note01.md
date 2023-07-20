## Helium atom


The Schrodinger equation for helium atom is already extremely complicated from the mathematical point of view. No analytic solutions to this equation has been found. However, with certain approximations, useful results can be obtained. The Hamiltonian for He atom can be written as:

$${\hat{H} = \underbrace{-\frac{\hbar^2}{2m_e}\left(\Delta_1 + \Delta_2\right)}_{\textnormal{Kinetic energy}} 
\underbrace{- \frac{1}{4\pi\epsilon_0}\left(\frac{Ze^2}{r_1} + \frac{Ze^2}{r_2} \overbrace{- \frac{e^2}{r_{12}}}^{\textnormal{Tough!!}}\right)}_{\textnormal{Potential energy}}}$$

where $\Delta_1$ is the Laplacian for the coordinates of electron 1, $\Delta_2$ for electron 2, $r_1$ is the distance of electron 1 from the nucleus, $r_2$ is the distance of electron 2 from the nucleus and $r_{12}$ is the distance between electrons 1 and 2. For He atom $Z = 2$.


### Approximation

Ignore the ``Tough'' term containing $r_{12}$. In this case the Hamiltonian consists of a sum of two hydrogenlike atoms:



$${\hat{H} = \hat{H}_1 + \hat{H}_2}$$

$${\hat{H}_1 = -\frac{\hbar^2}{2m_e}\Delta_1 - \frac{Ze^2}{4\pi\epsilon_0r_1}}$$

$${\hat{H}_2 = -\frac{\hbar^2}{2m_e}\Delta_2 - \frac{Ze^2}{4\pi\epsilon_0r_2}}$$


Because the Hamiltonian is a sum of two independent parts, the Schr\"odinger equation separates into two (each hydrogelike atom equation):

$${\hat{H}_1\psi(r_1) = E_1\psi(r_1)}$$
$${\hat{H}_2\psi(r_2) = E_2\psi(r_2)}$$

The total energy is a sum of $E_1$ and $E_2$ and the total wavefunction is a product of $\psi(r_1)$ and $\psi(r_2)$. Based on our previous wavefunction table for hydrogenlike atoms, we have:

$${E = E_1 + E_2 = -RZ^2\left(\frac{1}{n_1^2} + \frac{1}{n_2^2}\right)}$$

$${\psi(r_1)\psi(r_2) = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_1/a_0}\frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_2/a_0} 
= \frac{1}{\pi}\left(\frac{Z}{a_0}\right)^3e^{-Z(r_1 + r_2)/a_0}}
$$



- For a ground state He atom both electron reside on the lowest energy orbital and therefore the total wavefunction is $\psi(r_1,r_2) = \psi(r_1)\psi(r_2) = \psi(1)\psi(2) = 1s(1)1s(2)$. The energy obtained from this approximation is not sufficiently accurate (missing electron -- electron repulsion) but the wavefunction can be used for qualitative analysis. The variational principle Eq. (\ref{eq10.58}) gives a systematic way to asses how good our approximation is. The exact ground state energy has been found (very extensive analytic \& numerical calculations) as -79.0 eV. By using the approximate wavefunction, we can calculate the expectation value for energy. This yields -74.8 eV and thus the error in energy for this wavefunction is -5.2 eV. Note that the approximate value is, in accordance with the variational principle, higher than the true energy.

### A better approximation

- We can take the wavefunction from the previous step and use the nuclear charge $Z$ as a variational parameter. The variational principle states that minimization of the energy expectation value with respect to $Z$ should approach the true value from above (but obviously will not reach it). 
- By judging the energy, we can say that this new wavefunction is better than the previous wavefunction. The obtained value of $Z$ is less than the true $Z$ (= 2). This can be understood in terms of electrons shielding the nucleus from each other and hence giving a reduced nuclear charge. If the wavefunction in Eq. (\ref{eq10.68}) is used in calculating the energy expectation value, we get:

$${E = \langle\psi |\hat{H}|\psi\rangle = ... = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}}$$



In order to minimize energy we should differentiate it with respect to $Z$ and set it to zero (extremum point; here it is clear that this point is a minimum):

$${\frac{dE}{dZ} = \left(2Z - \frac{27}{8}\right)\frac{e^2}{4\pi\epsilon_0a_0} = 0}$$


- The above equation gives $Z = 27/16 \approx 1.7$ and $E \approx -77.5$ eV (previous -74.8 eV and exact -79.0 eV). This result could be improved by adding more terms and variables into
the trial wavefunction. For example, higher hydrogenlike atom orbitals with appropriate variational coefficients would yield a much better result.

- Another type of approximate method is based on \underline{perturbation theory}, which would typically assume that the electron --     electron repulsion is treated as an additional (small) perturbation to case 1) above.





