## Orbital angular momentum of the hydrogen atom


In hydrogenlike atoms degeneracy implies that the angular momentum is non-zero. If the quantum numbers $l$ and $m$ are known, it is possible to calculate $L^2$ and $L_z$ directly based on Eqs. (\ref{eq9.161}) and (\ref{eq9.163}):

$${L^2 = l(l+1)\hbar^2\textnormal{ (or formally }L = \sqrt{l(l+1)}\hbar\textnormal{)}}$$

$${L_z = m\hbar\textnormal{ where }m = -l,...,0,...,+l}$$

Without external electric or magnetic fields and electron spin, the energy of hydrogen atom is independent of quantum number $m$. The Lorentz force law (see your physics course lecture notes) gives the interaction of a charged particle with an electromagnetic field (for a classical particle):

$${\vec{F} = q\left( \vec{E} + \vec{v}\times \vec{B}\right)}$$

where vector $\vec{F}$ is the force experienced by the charged particle, $q$ is the particle charge, $\vec{E}$ is the electric field vector, $\vec{v}$ is the particle velocity vector and $\vec{B}$ is the magnetic field vector. Even though the above expression strictly applies to the classical case, it suggests that the presence of external magnetic or electric fields should somehow affect the electron orbit in hydrogenlike atoms.


\underline{The effect of electric field.} The effect of electric field is to mix the orbitals of the same symmetry along the direction of the applied field. This is called the Stark effect. By assuming that the electric field is time-independent, the quantum mechanical operator is proportional to position vector $\vec{r}$ that is in the direction of the applied field. Thus the Hamiltonian, including the
hydrogenlike atomic part and the external field, is (direction chosen along the $z$-axis below):

$${\hat{H}_{tot} = \hat{H}_{atom} + e\epsilon \hat{z}\textnormal{ (the general form: }e\vec{\epsilon}\cdot\vec{r}\textnormal{)}}$$

where $\epsilon$ is the electric field strength (N C$^{-1}$ or V m$^{-1}$) and $e$ is the electron charge. Consider, for example, $2s$ and three degenerate $2p$ orbitals. The $p_x$ and $p_y$ orbitals are unaffected by the field but the $2s$ and $2p_z$ orbitals are mixed by the field:


The low energy state has the electron wavefunction distorted towards the positively charged pole above. 


Because $2p_x$ and $2p_y$ are not affected by the field, this means that the degeneracy of the $2p$ orbitals is broken. Also $2s$ and $2p_z$ are no longer pure states and experience shift in energy. This shift can be observed by spectroscopic measurements.


### The effect of magnetic field.

A moving charge will also interact with an external magnetic field. When an electron is in a state with $l > 0$, it can be thought to be in quantum mechanical circular motion around the nucleus and generate its own magnetic field. Note that this motion is not classical but here we are just trying to obtain a wire frame model based on classical interpretation. The electron has now a magnetic moment given by (see your physics lecture notes):

$${\vec{\mu} = \gamma_e\vec{L}}$$

where $\gamma_e$ is the magnetogyric ratio of the electron ($-\frac{e}{2m_e}$). We choose the external magnetic field to lie along the $z$-axis and therefore it is important to consider the $z$ component of $\vec{\mu}$:

$${\mu_z = -\left(\frac{e}{2m_e}\right)L_z = -\left(\frac{e\hbar}{2m_e}\right)m \equiv -\mu_B m}$$

where $\mu_B$ is the Bohr magneton as defined above. The interaction between a magnetic moment and an external magnetic field is given by (classical expression):

$${E = -\vec{\mu}\cdot\vec{B} = -|\vec{\mu}||\vec{B}|\cos(\alpha)}$$

where $\alpha$ is the angle between the two magnetic field vectors. This gives the energy for a bar magnet in presence of an external magnetic field:


In quantum mechanics, a magnetic moment (here corresponding to a $p$-electron) may only take specific orientations. In classical mechanics any orientation is allowed. When the external magnetic field is oriented along $z$-axis, Eq. (\ref{eq10.40}) reads:

$${E = -\mu_z B = \frac{eB}{2m_e}L_z}$$

where the $z$-axis is often called the \underline{quantization axis}. The eigenvalues of $\hat{L}_z$ essentially give the possible orientations of the magnetic moment with respect to the external field. For example, consider an electron on $2p$ orbital in a hydrogenlike atom. The electron may reside on any of $2p_{+1}$, $2p_0$ or $2p_{-1}$ orbitals (degenerate without the field). For these orbitals $L_z$ may take the following values ($+\hbar, 0, -\hbar$):

$${\hat{L}_z|p_{+1}\rangle = +1\times\hbar|p_{+1}\rangle\textnormal{, }\hat{L}_z|p_0\rangle = 0\times\hbar|p_{0}\rangle\textnormal{, }\hat{L}_z|p_{-1}\rangle = -1\times\hbar|p_{-1}\rangle}$$


The relative orientations with respect to the external magnetic field are shown on the left side of the figure.


The total quantum mechanical Hamiltonian for a hydrogenlike atom in a magnetic field can now be written as:

$${\hat{H} = \hat{H}_0 + \frac{eB}{2m_e}\hat{L}_z}$$

where $\hat{H}_0$ denotes the Hamiltonian in absence of the magnetic field. The eigenvalues for Eq. (\ref{eq10.42}) are (derivation not shown):

$${E_{nlm} = -\frac{m_ee^4Z^2}{2(4\pi\epsilon_0)^2n^2\hbar^2} + \mu_BmB}$$

where $n = 1, 2, ...$; $l = 0, 1, ..., n - 1$; and $m = -l, ..., 0, ..., +l$. In the presence of magnetic field, the $(2l + 1)$ degenerate levels have been split (i.e., the degeneracy is lifted). This is called the orbital Zeeman effect.

