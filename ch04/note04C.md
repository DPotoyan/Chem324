## Rotational spectra of diatomic molecules

\otext
We assume that the molecule is a rigid rotor, which means that the molecular geometry does not change during molecular rotation. We have solved this problem already 

$${E_r = \frac{\hbar^2}{2I}J(J+1)\textnormal{ with }J=0,1,2...\textnormal{ and }M=-J,...,0,...J}$$

- The $I$ is the moment of inertia for the molecule (see Eq. (\ref{eq9.128})). Since the energy does not depend on $M$, each rotational level is $2J + 1$ fold degenerate.


- Energies are typically expressed in wavenumber units ($cm^{-1}$ although the basic SI unit is $m^{-1}$) by dividing $E$ by $hc$. The use of wavenumber units is denoted by including a tilde sign above the variable (e.g., $\tilde{\nu}$). The rotational energies expressed in wavenumbers are given by:

$${\tilde{E}_r(J) = \frac{E_r}{hc} = \frac{J(J+1)h}{8\pi^2Ic} = J(J+1)\tilde{B}}$$

where the *rotational constant* is given by:

$${\tilde{B} = \frac{h}{8\pi^2Ic}}$$

where $c$ is the speed of light. The rotational constant defines the rotational energy levels for a rigid diatomic molecule.


When the molecule is in electronic state $e$ and vibrational state $v$, the total wavefunction is written as $\psi = \psi_e\psi_v\psi_{J,M}$. The \textit{transition moment} between two different rotational levels $J,M$ and $J',M'$:

$${\int\int\int\psi_e^*\psi_v^*\psi_{J',M'}\hat{\mu}\psi_e\psi_v\psi_{J,M}d\tau_ed\tau_{rot}d\tau_{vib}}$$

where $\hat{\mu}$ is the transition dipole operator (see Eq. (\ref{eq11.80})) and only the rotational wavefunction has change. The electronic part gives the permanent dipole moment:

$${\mu_0^{(e)} = \int\psi_e^*\hat{\mu}\psi_ed\tau_e}$$

Therefore we can reduce the last equation to:

$${\int\int\psi_v^*\psi^*_{J',M'}\mu_0^{(e)}\psi_v\psi_{J,M}d\tau_{rot}d\tau_{vib}}$$

The vibrational part just gives the dipole moment for the molecule in vibrational state $v$ and we can write:

$${\int\psi_{J',M'}^*\mu_0\psi_{J,M}d\tau_{rot}}$$

- The rotational transition can only occur if this integral has a non-zero value. Clearly $\mu_0$ must be non-zero for the transition to occur, which means that the molecule must have a permanent dipole moment for the rotational transition to occur. 

- For example, homonuclear diatomic molecules like $H_2$ and $O_2$ will not show pure rotational spectra. Heteronuclear molecules show pure rotational spectra.


Using the known properties for spherical harmonics, one can show the following selection rule:

$${\Delta J = J' - J = \pm 1\textnormal{ and }\Delta M = M' - M = 0, \pm 1}$$

Since photons have one unit of angular momentum, the above rule can be understood in terms of angular momentum transfer. The transition frequencies between the rotational levels are given by ($J = 0,1,2,...$):

$${\tilde{\nu} = \tilde{E}_r(J + 1) - \tilde{E}_r(J) = \left((J+1)(J+2) - J(J+1)\right)\tilde{B} = 2\tilde{B}(J+1)}$$

The successive line positions in the rotational spectrum are given by $2\tilde{B}, 4\tilde{B}, 6\tilde{B},...$. Note that molecules with different atomic isotopes have different moments of inertia and hence different positions for the rotational lines.


In reality molecules are not rigid rotors and one must consider the coupling between $H_{rot}$ and $H_{vib}$. Classically thinking, with increasing rotational motion, the chemical bond stretches due to centrifugal forces, which increases the moment of inertia, and consequently, the rotational energy levels come closer together. It can be shown that this can be accounted for by including an additional term in Eq. (\ref{eqn5.33}):

$${\tilde{E}_r(J) = \tilde{B}J(J+1) - \tilde{D}J^2(J+1)^2}$$

where $\tilde{D}$ is the *centrifugal distortion constant* ($cm^{-1}$). Note that both $\tilde{B}$ and $\tilde{D}$ are positive.


When the centrifugal distortion is taken into account, the rotational transition frequencies are given by:

$${\tilde{\nu} = \tilde{E}_r(J+1) - \tilde{E}_r(J) = 2\tilde{B}(J+1) - 4\tilde{D}(J+1)^3\textnormal{ where }J=0,1,2,...}$$

**Example** Measurement of pure rotational spectrum of H$^{35}$Cl molecule gave the following positions for the absorption lines:

$$\tilde{\nu} = \left(20.794\textnormal{cm}^{-1}\right)\left(J+1\right) - \left(0.000164\textnormal{cm}^{-1}\right)\left(J+1\right)^3$$

What is the equilibrium bond length and what is the value of the centrifugal distortion constant?

**Solution** We first write the expression for $\tilde{B}$ and then use the definition of the moment of inertia $I$:

$$\tilde{B} = \frac{h}{8\pi^2cI} = \frac{h}{8\pi^2c\mu R_0^2}$$

where $\mu$ is the reduced mass for the molecule and $R_0$ is the equilibrium bond length. Solving for $R_0$ gives:

$$R_0 = \sqrt{\frac{h}{8\pi^2c\mu\tilde{B}}} = 129\textnormal{ pm}$$


The centrifugal distortion constant can obtained by comparing the above equation with Eq. (\ref{eqn5.40}):

$$\tilde{D} = 4.1\times 10^{-5}\textnormal{ cm}^{-1}$$


Another factor that affects the line intensities in a rotational spectrum is related to the thermal population of the rotational levels. Thermal populations of the rotational levels is given by the Boltzmann distribution (for a collection of molecules):

$${f_J = \frac{g_Je^{-hc\tilde{E}_r(J) / (k_B T)}}{\sum\limits_{J'}g_{J'}e^{-hc\tilde{E}_r(J') / (k_B T)}} = \frac{g_Je^{-hc\tilde{E}_r(J) / (k_B T)}}{q}}$$

- The  $q$ is called the *partition function* and $g_J = 2J + 1$ corresponds to the degeneracy count of state $J$. A useful comparison of thermal energy is given by $kT$ and if the energy of a state is much higher than this, it will not be thermally populated. 
- one expects the intensities to first increase as a function of the initial state $J$, reach a maximum, and then decrease because the thermal populations decrease. In an absorption experiment, one can see the thermal populations of the initial rotational levels.

> Note: For systems, where the rotational degrees of freedom may exchange identical nuclei, an additional complication arises from the symmetry requirement for the nuclear wavefunction. Recall that bosons must have symmetric wavefunctions and fermions antisymmetric. We will not discuss this in more detail here.

