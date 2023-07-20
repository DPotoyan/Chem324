## BO approximation

Because nuclei are much heavier than electrons, the Schrodinger equation can be approximately separated into the nuclear and the electron parts. Thus the electronic Schr\"odinger equation for a molecule can be solved separately at each fixed nuclear configuration. This is called the Born-Oppenheimer approximation.


In the following, we will consider the simplest molecule $H_2^+$, which contains only one electron. This simple system will demonstrate the basic concepts in chemical bonding. The Schr\"odinger equation for H$_2^+$ is:

$${H\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B) = E\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B)}$$

where $\vec{r}_1$ is the vector locating the (only) electron and $\vec{R}_A$ and $\vec{R}_B$
are the positions of the two protons. The Hamiltonian for H$_2^+$ is:

$${\hat{H} = -\frac{\hbar^2}{2M}(\Delta_A + \Delta_B) - \frac{\hbar^2}{2m_e}\Delta_e+ \frac{e^2}{4\pi\epsilon_0}\left(\frac{1}{R} - \frac{1}{r_{1A}} - \frac{1}{r_{1B}}\right)}$$

where $M$ is the proton mass, $m_e$ is the electron mass, $r_{1A}$ is the distance between the electron and nucleus A, $r_{1B}$ is the distance between the electron and nucleus B and $R$ is the A - B distance.


Note that the Hamiltonian includes also the quantum mechanical kinetic energy for the protons. As such the wavefunction depends on $\vec{r}_1$, $\vec{R}_A$ and $\vec{R}_B$. Because the nuclear mass $M$ is much larger than the electron mass $m_e$, the wavefunction can be separated (Born-Oppenheimer approximation):

$${\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B) = \psi_e(\vec{r}_1, R)\psi_n(\vec{R}_A, \vec{R}_B)}$$

where $\psi_e$ is the electronic wavefunction that depends on the distance $R$ between the nuclei and $\psi_n$ is the nuclear wavefunction depending on $\vec{R}_A$ and $\vec{R}_B$. It can be shown that the nuclear part can be often be separated into vibrational, rotational and translational parts. The electronic Schr\"odinger equation can now be written as:

$${\hat{H}_e\psi_e = E_e\psi_e}$$

Note that Eq. (\ref{eq11.4}) depends parametrically on $R$ (``one equation for each value of $R$''). The \textit{electronic Hamiltonian} is:

$${\hat{H}_e = -\frac{\hbar^2}{2m_e}\Delta_e + \frac{e^2}{4\pi\epsilon_0}
\left(\frac{1}{R} - \frac{1}{|r_1 - R_A|} - \frac{1}{|r_1 - R_B|}\right)}$$

Because $R$ is a parameter, both $E_e$ and $\psi_e$ are functions of $R$.

