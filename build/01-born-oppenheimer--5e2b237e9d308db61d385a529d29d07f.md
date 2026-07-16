---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Born-Oppenheimer Approximation

:::{note} **What you will learn**

- **The Born-Oppenheimer (BO) approximation.** Because nuclei are much heavier than electrons, the Schrodinger equation can be approximately separated into a nuclear part and an electronic part. The electronic Schrodinger equation for a molecule can then be solved at each fixed nuclear configuration.
- **From atoms to molecules.** The BO approximation lets us extend the multi-electron treatment of atoms to molecules.
- **Molecular orbitals (MOs).** Single-electron wavefunctions of molecules are called molecular orbitals.
- **Nuclear geometry as a parameter.** The geometry of a molecule, for example the bond length $R$ of $H_2$, is held fixed when determining the molecular orbitals. For different values of $R$ one obtains different energies and different MOs.
:::

### The simplest molecule

:::{figure} ./images/h2plus_mol.png
:alt: Coordinates of the hydrogen molecule ion
:width: 300px

Fig. 1 Coordinates used to describe the $H_2^+$ molecule.
:::

In the following, we will consider the simplest molecule $H_2^+$, which contains only one electron. This simple system demonstrates the basic concepts of chemical bonding. The Schrodinger equation for $H_2^+$ is:

$${H\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B) = E\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B)}$$

where $\vec{r}_1$ is the vector locating the (only) electron and $\vec{R}_A$ and $\vec{R}_B$ are the positions of the two protons. The Hamiltonian for $H_2^+$ is:

$${\hat{H} = -\frac{\hbar^2}{2M}(\Delta_A + \Delta_B) - \frac{\hbar^2}{2m_e}\Delta_e+ \frac{e^2}{4\pi\epsilon_0}\left(\frac{1}{R} - \frac{1}{r_{1A}} - \frac{1}{r_{1B}}\right)}$$

where $M$ is the proton mass, $m_e$ is the electron mass, $r_{1A}$ is the distance between the electron and nucleus A, $r_{1B}$ is the distance between the electron and nucleus B, and $R$ is the A to B distance.

Note that the Hamiltonian also includes the quantum mechanical kinetic energy of the protons. As such, the wavefunction depends on $\vec{r}_1$, $\vec{R}_A$, and $\vec{R}_B$.

### The Born-Oppenheimer approximation

:::{figure} ./images/Born.jpg
:alt: Max Born
:width: 200px

Fig. 2 Max Born.
:::

:::{figure} ./images/BO.jpeg
:alt: Robert J. Oppenheimer
:width: 200px

Fig. 3 Robert J. Oppenheimer.
:::

Because the nuclear mass $M$ is much larger than the electron mass $m_e$, the wavefunction can be separated (the Born-Oppenheimer approximation):

$${\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B) = \psi_e(\vec{r}_1, R)\psi_n(\vec{R}_A, \vec{R}_B)}$$

where $\psi_e$ is the electronic wavefunction that depends on the distance $R$ between the nuclei and $\psi_n$ is the nuclear wavefunction depending on $\vec{R}_A$ and $\vec{R}_B$. It can be shown that the nuclear part can often be further separated into vibrational, rotational, and translational parts. The electronic Schrodinger equation can now be written as:

:::{important} **The electronic Schrodinger equation**

$${\hat{H}_e\psi_e = E_e\psi_e}$$

$${\hat{H}_e = -\frac{\hbar^2}{2m_e}\Delta_e + \frac{e^2}{4\pi\epsilon_0}
\left(\frac{1}{R} - \frac{1}{|r_1 - R_A|} - \frac{1}{|r_1 - R_B|}\right)}$$

This equation depends parametrically on $R$: there is one equation for each value of $R$.
:::

Because $R$ is a parameter, both $E_e$ and $\psi_e$ are functions of $R$. Solving the electronic problem at a sequence of fixed nuclear geometries traces out the potential energy surface on which the nuclei move, which is the central idea that makes molecular electronic structure tractable.
