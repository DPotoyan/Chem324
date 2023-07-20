## Pauli exclusion principle

Our previous wavefunction for He atom did not include electron spin. For two electrons, the spin functions can be written as products:

$${\alpha(1)\alpha(2)\textnormal{, }\beta(1)\alpha(2)\textnormal{, }\alpha(1)\beta(2)\textnormal{ or  }\beta(1)\beta(2)}$$

where, for example, $\alpha(1)$ indicates that electron 1 has spin $\alpha$. Electrons are indistinguishable and therefore it makes no sense to try to use the two middle terms alone but combine them as:




$${\alpha(1)\alpha(2)\textnormal{ (symmetric if 1 and 2 are exchanged)}}$$

$${\beta(1)\beta(2)\textnormal{ (symmetric)}}$$

$${\frac{1}{\sqrt{2}}\left(\alpha(1)\beta(2) + \alpha(2)\beta(1)\right)\textnormal{ (symmetric)}}$$

$${\frac{1}{\sqrt{2}}\left(\alpha(1)\beta(2) - \alpha(2)\beta(1)\right)\textnormal{ (antisymmetric)}}$$


- In 1926 Pauli showed that the wavefunction must be antisymmetric with respect to exchange of the electron indices. This applies also for systems with more than two electrons. An outcome of this principle is that no two electrons can have exactly the same quantum numbers: $n$, $l$, $m_l$, $s$, $m_s$. In non-relativistic quantum mechanics this is a postulate.


In order to construct a complete wavefunction for He atom, we need to tag on the spin part to the wavefunction

$${\psi = 1s(1)1s(2)\times\frac{1}{\sqrt{2}}\left(\alpha(1)\beta(2) - \alpha(2)\beta(1)\right)}$$

A generalization of this result for many-electron systems was proposed by Slater in 1929:

$${\hspace*{-0.4cm}
\psi(r_1,...,r_n) = \frac{1}{\sqrt{n!}}
\begin{vmatrix}
1s(1)\alpha(1) & 1s(1)\beta(1) & 2s(1)\alpha(1) & ... \\
1s(2)\alpha(2) & 1s(2)\beta(2) & 2s(2)\alpha(2) & ... \\
1s(3)\alpha(3) & ... & ... & ...\\
... & ... & ... & ...\\
\end{vmatrix}
}$$


$${
\psi(r_1,r_2) = \frac{1}{\sqrt{2}}\begin{vmatrix}
1s(1)\alpha(1) & 1s(1)\beta(1)\\
1s(2)\alpha(2) & 1s(2)\beta(2)\\
\end{vmatrix}
}$$


- The Slater determinant automatically ensures that the total wavefunction is antisymmetric. Note that from the mathematical point of view the antisymmetry requirement restricts the allowed solutions to the Schr\"odinger equation. The lowest energy solutions are typically symmetric and the antisymmetric states correspond to higher energy. 
- However, one must be careful with terminology here because only the antisymmetric states exist for electrons (Fermions) and as such they are the lowest energy (ground state) solutions for them. Particles that have symmetric wavefunctions are called Bosons (for example, $^4$He atoms).


- In general, particles with half-integral spin ($s = \frac{1}{2}, \frac{3}{2}, ...$) are Fermions (Fermi-Dirac statistics) and particles with integral spin ($s = 0, 1, 2, ...$) are Bosons (Bose-Einstein statistics). Note that electron spin enters the Hamiltonian only when external fields are present or when \underline{spin-orbit} interaction is included (will be discussed later).

**example** Show that the Slater determinant in Eq. (\ref{eq10.78}) for the ground state helium atom is an eigenfunction of the total spin operator $\hat{S}_{z,tot} = \hat{S}_{z_1} + \hat{S}_{z_2}$, where 1 and 2 refer to the two electrons.

**solution**  First we recall how $\hat{S}_z$ operates on electron spin as follows (Eqs. (\ref{eq10.48}) and (\ref{eq10.49})):

$$\hat{S}_z|\alpha\rangle = +\frac{\hbar}{2}|\alpha\rangle\textnormal{ and }\hat{S}_z|\beta\rangle = -\frac{\hbar}{2}|\beta\rangle$$

Next, we expand the Slater determinant in Eq. (\ref{eq10.78}):

$$\psi = \overbrace{1s(1)1s(2)}^{\textnormal{symmetric}}\times\overbrace{\frac{1}{\sqrt{2}}\left(\alpha(1)\beta(2) - \alpha(2)\beta(1)\right)}^{\textnormal{antisymmetric}}$$

Operate on this by $\hat{S}_{z_1}$ and $\hat{S}_{z_2}$. They operate only on the spin-part and on the corresponding electron only:



$$\hat{S}_{z_1}|\psi\rangle = |1s(1)1s(2)\rangle\times\frac{1}{\sqrt{2}}\left(\frac{\hbar}{2}|\alpha(1)\beta(2)\rangle + \frac{\hbar}{2}|\beta(1)\alpha(2)\rangle\right)$$

$$\hat{S}_{z_2}|\psi\rangle = |1s(1)1s(2)\rangle\times\frac{1}{\sqrt{2}}\left(-\frac{\hbar}{2}|\alpha(1)\beta(2)\rangle - \frac{\hbar}{2}|\beta(1)\alpha(2)\rangle\right)$$

$$\Rightarrow\textnormal{ }\hat{S}_{z,tot}|\psi\rangle = \left(\hat{S}_{z_1} + \hat{S}_{z_2}\right)|\psi\rangle = \hat{S}_{z_1}|\psi\rangle + \hat{S}_{z_2}|\psi\rangle = 0$$


Note that the two terms are equal in magnitude but have opposite signs and they cancel. Thus the eigenvalue of the $z$-component of the total spin is zero. It can also be shown that $S^2 = 0$. This kind of electronic configuration is called a \textit{singlet state} (i.e. the two electrons have opposite spins).


Previously we had both electrons on $1s$ orbital with opposite spins. If the electrons reside on two different orbitals, for example, $1s$ and $2s$, we would have an excited helium atom. Such state can be created experimentally by a suitable high-energy process (laser induced break-down etc.). The spatial part of the wavefunction is $\psi = 1s(1)2s(2)$. It could as well be $\psi = 2s(1)1s(2)$ as we cannot distinguish the electrons from each other. Obviously we must form a linear combination of these so that both electrons appear identical (two possibilities):

$${\psi_{sym} = \frac{1}{\sqrt{2}}\left(1s(1)2s(2) + 1s(2)2s(1)\right)\textnormal{ (symmetric)}}$$

$${\psi_{asym} = \frac{1}{\sqrt{2}}\left(1s(1)2s(2) - 1s(2)2s(1)\right)\textnormal{ (antisymmetric)}}$$



> Note that these two states may have different energies.


Next, we consider adding the spin part to these wavefunctions. Because the electrons are on two different orbitals, we have the following four possibilities:

$$
\left.\begin{matrix}
\phi_1 = \alpha(1)\alpha(2)\textnormal{ (symmetric)}\\
\phi_2 = \beta(1)\beta(2)\textnormal{ (symmetric)}\\
\phi_3 = \frac{1}{\sqrt{2}}\left(\alpha(1)\beta(2) + \beta(1)\alpha(2)\right)\textnormal{ (symmetric)}\\
\end{matrix}\right\rbrace\textnormal{ Triplet state}
$$

$$
\left.\phi_4 = \frac{1}{\sqrt{2}}\left(\alpha(1)\beta(2) - \beta(1)\alpha(2)\right)\right\rbrace\textnormal{ Singlet state}
$$

Before we can combine the spatial and spin wavefunctions, we must consider the symmetries of these functions. Remember that the total wavefunction must be antisymmetric. Thus the allowed combinations are: symmetric (spatial) $\times$ antisymmetric (spin) or antisymmetric (spatial) $\times$ symmetric (spin). The total wavefunction for the triplet state is therefore:

$${\psi_1 = \frac{1}{\sqrt{2}}\left(1s(1)2s(2) - 2s(1)1s(2)\right)\alpha(1)\alpha(2)}$$

$${\psi_2 = \frac{1}{2}\left(1s(1)2s(2) - 2s(1)1s(2)\right)\left(\alpha(1)\beta(2) + \beta(1)\alpha(2)\right)}$$

$${\psi_3 = \frac{1}{\sqrt{2}}\left(1s(1)2s(2) - 2s(1)1s(2)\right)\beta(1)\beta(2)}$$


For the singlet state we have:

$${\psi_4 = \frac{1}{2}\left(1s(1)2s(2) + 2s(1)1s(2)\right)\left(\alpha(1)\beta(2) - \alpha(2)\beta(1)\right)}$$

- Singlet and triplet states have been named after the number of spin degenerate levels they posses. The total spin $\hat{S}^2$ and $\hat{S}_z$ operators for these states yield:

$${
\textnormal{Triplet: }\left\lbrace\begin{matrix}
\hat{S}_z|\psi_1\rangle = +\hbar|\psi_1\rangle\textnormal{, }\hat{S}_z|\psi_2\rangle = 0|\psi_2\rangle\textnormal{, }\hat{S}_z|\psi_3\rangle = -\hbar|\psi_3\rangle\\
\hat{S}^2|\psi_i\rangle = 2\hbar^2|\psi_i\rangle\textnormal{ where }i=1,2,3.\\
\end{matrix}\right.
}$$

$${
\textnormal{Singlet: }\left\lbrace\begin{matrix}
\hat{S}_z|\psi_4\rangle = 0|\psi_4\rangle\\
\hat{S}^2|\psi_4\rangle = 0|\psi_4\rangle\\
\end{matrix}\right.
}$$


For helium atom the singlet/triplet consideration is only relevant for the excited states but for atoms with more electrons this may have to be considered in order to determine the ground state. 
When more electrons are added, the wavefunction becomes more complicated. For example, the Slater determinant for Li can be written as:

$${\psi = \frac{1}{\sqrt{6}}
\begin{vmatrix}
1s(1)\alpha(1) & 1s(1)\beta(1) & 2s(1)\alpha(1)\\
1s(2)\alpha(2) & 1s(2)\beta(2) & 2s(2)\alpha(2)\\
1s(3)\alpha(3) & 1s(3)\beta(3) & 2s(3)\alpha(3)\\
\end{vmatrix}
}$$

> Note that the last column could have been labeled as $\beta$ as well (degeneracy).





