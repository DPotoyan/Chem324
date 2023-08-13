# QM overview

## From classical to Quantum 

### Blackbody radiation

|Description|Equations|
|-:|:-|
|Energy quantization|$E = nh\nu$|
|Average energy of an oscillating dipole|$\langle E_{\text{osc}} \rangle = \dfrac{h\nu}{e^{h\nu / k_B T} - 1}$|
|Spectral radiation density of blackbody (Planck)|$\rho (\nu, T) \ d\nu = \dfrac{8\pi h \nu^3}{c^3}\dfrac{1}{e^{h\nu / k_B T} - 1} \ d\nu$|
|Spectral radiation density of blackbody (classical)|$\rho (\nu, T) \ d\nu = \dfrac{8\pi h \nu^3}{c^3} k_B T d\nu$|

### Wave-particle duality

|Description|Equations|
|-:|:-|
|Energy of light|$E = h \nu$|
|**Photoelectric effect** <br/> Kinetic energy of ejected photoelectron|$E_k = h \nu - \Phi$|
|de Broglie relation|$p = \dfrac{h}{\lambda}$|
|Kinetic energy|$E_k = \dfrac{1}{2}mv^2 = \dfrac{p^2}{2m}$|

### Atomic spectra of hydrogen and Bohr's model

|Description|Equations|
|-:|:-|
|Hydrogen emission lines <br/> $n_2 > n_1$|$\tilde{\nu} = \dfrac{1}{\lambda} = R_H \left( \dfrac{1}{n_1^2} - \dfrac{1}{n_2^2} \right)$|
|Bohr's radius|$r = \dfrac{4\pi \varepsilon_0 \hbar^2}{m_e e^2}$|
|Energy level in Bohr's model|$E_n = -\dfrac{m_e e^4}{8\varepsilon_0^2 h^2n^2}$|
|Emission of hydrogen atom <br/> $n_2 > n_1$|$\nu = \dfrac{m_e e^4}{8\varepsilon_0^2 h^3} \left( \dfrac{1}{n_1^2} - \dfrac{1}{n_2^2} \right)$|

### Waves

|Description|Equations|
|-:|:-|
|Classical nondispersive wave equation|$\dfrac{\partial \Psi(x, t)}{\partial x^2} = \dfrac{1}{v^2} \dfrac{\partial \Psi(x, t)}{\partial t^2}$|
|Wave number|$k = \dfrac{2\pi}{\lambda}$|
|Frequency|$\nu = \dfrac{1}{T}$|
|Angular frequency|$\omega = \dfrac{2\pi}{T} = 2\pi\nu$|
|Wave speed|$v = \lambda\nu$|
|Euler's formula|$e^{i\theta} = \cos\theta + i\sin\theta$|
|Solution of wave equation|$\begin{aligned}\Psi(x, t) &= A \sin(kx - \omega t + \phi) \\\ &= \mathrm{Re}(Ae^{i(kx-\omega t + \phi')})\end{aligned}$|
|Interfering traveling waves give standing wave|$\begin{aligned}\Psi(x, t) &= A[\sin(kx - \omega t) + \sin(kx + \omega t)] \\\ &= 2A \sin(kx)\cos(\omega t) \\\ &= \psi(x)\cos(\omega t) \end{aligned}$|
|Time-independent Schrodinger equation|$-\dfrac{\hbar^2}{2m}\dfrac{d^2\psi(x)}{dx^2} + V(x)\psi(x) = E\psi(x)$|
|Time-dependent Schrodinger equation|$-\dfrac{\hbar^2}{2m}\dfrac{\partial^2\Psi(x, t)}{\partial x^2} + V(x, t)\Psi(x, t) = i\hbar\Psi(x, t)$|
|Stationary states are standing waves|$\Psi(x, t) = \psi(x) e^{-i(E/\hbar)t}$|
|Normalization|$\Vert f(x) \Vert = \int_D f^* f \ dx = 1$|
|Orthogonality|$\int_D f^* g \ dx = 0$|
|Use quantum mechanics when ...|1. $\lambda_{\text{particle}} \sim L_{\text{problem}}$ <br/> 2. $\Delta E \gtrsim k_bT$ (discrete energy spectrum)|

## Quantum-Mechanical Postulates

1. The state of a quantum-mechanical particle is completely specified by a wave function $\Psi(x, t)$. The probability that the particle will be found at time $t_0$ in a spatial interval of width $dx$ centered at $x_0$ is given by $\Psi^*(x_0, t_0)\Psi(x_0, t_0) dx$
2. For every measurable property of a system, there exists a corresponding operator.
3. In any single measurement of the observable that corresponds to the operator $\hat{A}$, the only values that will ever be measured are the eigenvalues of that operator.
4. If the system is in a state described by the wave function $\Psi(x, t)$, and the value of the observatle $a$ is measured once on each of many identically prepared systems, the average value (expectation value) of all of the measurements is given by
$$
\langle a \rangle = \dfrac{\displaystyle\int_{-\infty}^{\infty} \Psi^* \hat{A} \Psi \ dx}{\displaystyle\int_{-\infty}^{\infty} \Psi^*\Psi \ dx}
$$
5. The evolution in time of a quantum-mechanical system is governed by the time-dependent Schrödinger equation
$$
\hat{H}\Psi(x, t) = i\hbar\dfrac{\partial\Psi(x, t)}{\partial t}
$$

### Operators

|Description|1D|3D|
|-:|:-|:-|
|Position|$\hat{x} = x$|$\mathbf{\hat{x}} = \mathbf{x}$|
|Linear momentum|$\hat{p}_x = -i\hbar \dfrac{d}{dx}$|$\mathbf{\hat{p}} = -i\hbar\mathbf{\nabla}$|
|Kinetic energy|$\hat{T} = \dfrac{\hat{p}_x^2}{2m} = -\dfrac{\hbar^2}{2m}\dfrac{d^2}{dx^2}$|$\mathbf{\hat{T}} = -\dfrac{\hbar^2}{2m}\mathbf{\nabla}^2$|
|Potential energy|$\hat{V} = V(x)$|$\mathbf{\hat{V}} = V(\mathbf{x})$|
|Total energy Hamiltonian|$\hat{H} = \hat{T} + \hat{V} = -\dfrac{\hbar^2}{2m}\dfrac{d^2}{dx^2} + V(x)$|$\mathbf{\hat{H}} = -\dfrac{\hbar^2}{2m}\mathbf{\nabla}^2 + V(\mathbf{x})$|

## Simple Quantum Systems

### Stationary states

|Description|Equations|
|-:|:-|
|Time dependent Schrodinger equation|$\hat{H}\Psi(x, t) = i\hbar\dfrac{\partial\Psi(x, t)}{\partial t}$|
|Time independent Schrodinger equation|$\hat{H}\psi_n(x) = E_n \psi_n(x)$|
|Stationary state wave function|$\Psi(x, t) = \psi(x) T(t)$|
|Time component of wave function|$T(t) = e^{iEt/\hbar}$|
|Probability of finding particle in an interval|$\mathrm{Prob}(x, x+dx) = \vert \Psi(x, t) \vert^2 dx = \vert \psi(x) \vert^2 dx$|
|General solution as linear combination of stationary states|$\psi(x) = \sum\limits_n c_n \phi_n(x)$|
|Expansion coefficients|$c_n = \langle \phi_n \vert \psi \rangle = \int \phi_n^* \psi \ dx$|
|Normalization|$\sum\limits_n c_n = 1$|

### Particle in a 1D box

|Description|Equations|
|-:|:-|
|Time independent Schrodinger equation|$\left[ -\dfrac{\hbar^2}{2m}\dfrac{d^2}{dx^2} + V(x) \right] \psi(x) = E\psi(x)$|
|Wave function <br/> $n = 0, 1, 2, ...$|$\psi_n(x) = \sqrt{\dfrac{2}{L}} \sin\left(\dfrac{n \pi x}{L}\right)$|
|Energy eigenvalues|$E_n = \dfrac{h^2}{8mL^2} n^2 = \dfrac{\hbar^2 \pi^2}{2mL^2}n^2$|

### Particle in a 3D box

|Description|Equations|
|-:|:-|
|Time independent Schrodinger equation|$\left[ -\dfrac{\hbar^2}{2m}\mathbf{\nabla}^2 + V(\mathbf{x}) \right] \psi(\mathbf{x}) = E\psi(\mathbf{x})$|
|Wave function <br/> $n_x = 0, 1, 2, ...$ <br/> $n_y = 0, 1, 2, ...$ <br/> $n_z = 0, 1, 2, ...$|$\begin{aligned}&\psi_{n_x, n_y, n_z}(\mathbf{x}) \\\ =& \psi_{n_x}(x)\psi_{n_y}(y)\psi_{n_z}(z) \\\ =& \sqrt{\dfrac{2}{L_x}}\sqrt{\dfrac{2}{L_y}}\sqrt{\dfrac{2}{L_z}} \sin\left(\dfrac{n_x \pi x}{L_x}\right)\sin\left(\dfrac{n_y \pi y}{L_y}\right)\sin\left(\dfrac{n_z \pi z}{L_z}\right)\end{aligned}$|
|Energy eigenvalues|$E_n = \dfrac{h^2}{8m} \left(\dfrac{n_x^2}{L_x^2} + \dfrac{n_y^2}{L_y^2} + \dfrac{n_z^2}{L_z^2}\right)$|

### Finite potential well

|Description|Equations|
|-:|:-|
|Potential|$V(x) = \begin{cases}0 & x\in [0, L] \\\ V_0 & \mathrm{elsewhere}\end{cases}$|
|Reflection probability|$R = \dfrac{(\sqrt{E} - \sqrt{E - V_0})^2}{(\sqrt{E} + \sqrt{E - V_0})^2}$|
|Transmission probability|$T = \dfrac{4\sqrt{E(E - V_0)}}{(\sqrt{E} - \sqrt{E - V_0})^2}$|

## Commutators and Uncertainty

|Description|Equations|
|-:|:-|
|Commutator|$[A, B] = AB - BA$|
|Condition of commutation|$[A, B] = 0$|
|Standard deviation (uncertainty)|$\begin{aligned}\sigma_A &= \sqrt{\langle (A - \langle A \rangle^2 \rangle)} \\\ &= \sqrt{\langle A^2 \rangle - \langle A \rangle^2}\end{aligned}$|
|Heisenberg uncertainty principle (general)|$\sigma_A \sigma_B \ge \frac{1}{2} \vert\langle[\hat{A}, \hat{B}]\rangle\vert$|
|Heisenberg uncertainty principle (position-momentum)|$\sigma_x \sigma_p \ge \frac{\hbar}{2}$|

## Spectroscopy

### Dimer model

|Description|Equations|
|-:|:-|
|Hamiltonian of dimer|$\mathbf{H}_{\text{dimer}} = \dfrac{\mathbf{p}_1^2}{2m_1} + \dfrac{\mathbf{p}_2^2}{2m_2} + V(\vert \mathbf{x}_1 - \mathbf{x}_2\vert)$|
|Total mass|$M = m_1 + m_2$|
|Reduced mass|$\mu = \dfrac{m_1m_2}{m_1 + m_2}$|
|Position in center of mass (COM) coordinate|$\mathbf{X} = \dfrac{m_1 \mathbf{x}_1 + m_2 \mathbf{x}_2}{M}$|
|Momentum in center of mass (COM) coordinate|$\mathbf{\Pi} = \mathbf{p}_1 + \mathbf{p}_2$|
|Position in relative coordinate|$\mathbf{x} = \mathbf{x}_1 - \mathbf{x}_2 \equiv \mathbf{r}$|
|Momentum in relative coordinate|$\mathbf{p} = \dfrac{m_1 \mathbf{p}_1 + m_2 \mathbf{p}_2}{M}$|
|Hamiltonian of dimer|$\begin{aligned}\mathbf{H}_{\text{dimer}} &= \mathbf{H}\_{\text{free}} + \mathbf{H}\_{\text{int}} \\\ &= \underbrace{\dfrac{\mathbf{\Pi}^2}{2M}}\_{\text{COM coord}} + \underbrace{\dfrac{\mathbf{p}^2}{2\mu} + V(\vert\mathbf{x}\vert)}\_{\text{rel coord}}\end{aligned}$|
|Free particle Hamiltonian|$\mathbf{H}_{\text{free}} = \dfrac{\mathbf{\Pi}^2}{2M}$|
|Internal Hamiltonian|$\mathbf{H}_{\text{int}} = \dfrac{\mathbf{p}^2}{2\mu} + V(\vert\mathbf{x}\vert)$|
|Dimer wave function|$\Psi_{\text{dimer}} = \Phi(\mathbf{X}) \psi(\mathbf{x})$|
|Free particle (COM) wave function|$\Phi(\mathbf{X}) = e^{\pm i\mathbf{\Pi X}/\hbar}$|
|Internal Hamiltonian Schrodinger equation|$\left[ -\dfrac{\hbar^2}{2\mu}\nabla_{\mathbf{x}}^2 + V(\mathbf{r}) \right] \psi(\mathbf{x}) = E\psi(\mathbf{x})$|
|Laplacian in spherical coordinate <br/> $\theta \in [0, \pi]$ <br/> $\phi \in [0, 2\pi]$|$\nabla^2 = \underbrace{\dfrac{1}{r^2}\dfrac{\partial}{\partial r}\left(r^2 \dfrac{\partial}{\partial r}\right)}\_{\text{radial breathing KE, vibration}} + \underbrace{\dfrac{1}{r^2 \sin\theta}\dfrac{\partial}{\partial \theta}\left(\sin\theta\dfrac{\partial}{\partial \theta}\right) + \dfrac{1}{r^2 \sin^2 \theta}\dfrac{\partial^2}{\partial\phi^2}}\_{\text{angular breathing KE, rotation}}$|
|Dimer Hamiltonian|$\hat{H}\_{\text{dimer}} = \hat{H}\_{\text{COM}} + \hat{H}\_{\text{vib}} + \hat{H}\_{\text{rot}}$|
|Dimer total energy (see below)|$E = \dfrac{\Pi^2}{2M} + \hbar\omega_0 (n+\frac{1}{2}) + \dfrac{\hbar^2 l(l+1)}{2I}$|

### Vibration: quantum harmonic oscillator

|Description|Equations|
|-:|:-|
|Vibrational Schrodinger equation|$\left[ -\dfrac{\hbar^2}{2\mu}\dfrac{1}{r^2}\dfrac{\partial}{\partial r}\left(r^2 \dfrac{\partial}{\partial r}\right) + V(r) \right]\psi(\mathbf{x}) = E\psi(\mathbf{x})$|
|Wave function|$\psi(\mathbf{x}) = R(r)Y(\theta, \phi)$|
|Harmonic approximation|$V(r) \approx \frac{1}{2}kr^2$|
|Spring constant|$k = \mu\omega_0^2$|
|Vibrational Schrodinger equation|$\left[ -\dfrac{\hbar^2}{2\mu}\dfrac{1}{r^2}\dfrac{\partial}{\partial r}\left(r^2 \dfrac{\partial}{\partial r}\right) + \dfrac{1}{2}kr^2 \right]\psi(r) = E\psi(r)$|
|Wave function <br/> $n = 0, 1, 2, ...$|$\psi(r) = \dfrac{1}{\sqrt{2^2 n!}}\left(\dfrac{\alpha}{\pi}\right)^{1/4} H_n(\sqrt{\alpha} r) e^{-\alpha r^2 / 2}$|
|Hermite polynomials|$H_n(r) = (-)^n e^{x^2}\left(\dfrac{d^n}{dx^n}\right)e^{-x^2}$|
|Constant|$\alpha = \dfrac{m\omega_0}{\hbar}$|
|Energy eigenvalue <br/> $n = 0, 1, 2, ...$|$E_n = (n + \frac{1}{2})\hbar \omega_0$|
|Transition dipole moment|$\vec{\mu}_{fi} = \dfrac{d\vec{\mu}(x_0)}{dx} \langle \psi_f \vert \hat{x} \vert \psi_i \rangle$|
|Vibrational selection rule|$\Delta n = \pm 1$|

### Rotation: rigid rotor

#### Classical rigid rotor

|Description|Equations|
|-:|:-|
|Angular momentum|$\mathbf{L} = \mathbf{x} \times \mathbf{p} = I\vec{\omega}$|
|Linear velocity|$\vec{v} = R_0 \vec{\omega}$|
|Moment of inertia|$I = mR_0^2$|
|Rotational kinetic energy|$E = \dfrac{1}{2}I\omega^2 = \dfrac{L^2}{2I}$|

#### Quantum rigid rotor

|Description|Equations|
|-:|:-|
|Angular momentum operator|$\hat{\mathbf{L}} = \hat{\mathbf{x}} \times \hat{\mathbf{p}}$|
|z-component of angular momentum operator|$L_x = \dfrac{\hbar}{i}\dfrac{\partial}{\partial\phi}$|
|Magnitude of angular momentum operator|$\hat{\mathbf{L}}^2 = L^2 =  -\hbar^2 \left[ \dfrac{1}{\sin\theta}\dfrac{\partial}{\partial\theta} \left( \sin\theta\dfrac{\partial}{\partial\theta} + \dfrac{1}{\sin^2\theta}\dfrac{\partial^2}{\partial\phi^2} \right) \right]$|
|Components of $\hat{\mathbf{L}}$ does not commute|$[\hat{L}_i, \hat{L}_j] = i\hbar \hat{L}_k$|
|Components of $\hat{\mathbf{L}}$ commute with its magnitude|$[\hat{L}_i, L^2] = 0$|

|Description|Equations|
|-:|:-|
|Rotational Schrodinger equation|$-\dfrac{\hbar^2}{2\mu R_0^2}\left[ \dfrac{1}{r^2 \sin\theta}\dfrac{\partial}{\partial \theta}\left(\sin\theta\dfrac{\partial}{\partial \theta}\right) + \dfrac{1}{r^2 \sin^2 \theta}\dfrac{\partial^2}{\partial\phi^2} \right]Y(\theta, \phi) = EY(\theta, \phi)$|
|Spherical harmonics|$Y_l^m(\theta, \phi) = (-)^m \sqrt{\dfrac{(2l+1)}{4\pi}\dfrac{(l-m)!}{(l+m)!}} P_l^m(\cos\theta) e^{im\phi}$|
|Legendre polynomial|$P_l^m(x) = \dfrac{1}{2^l l!}(1-x^2)^{m/2} \dfrac{d^{(l+m)}}{dx^{(l+m)}}(x^2-1)^l$|
|Energy eigenvalues <br/> $l = 0, 1, 2, ...$|$E_l = \dfrac{\hbar^2}{2I}l(l+1)$|
|Angular momentum eigenvalues <br/> $l = 0, 1, 2, ...$|$L^2 Y = \hbar^2l(l+1) Y$|
|z-component eigenvalues <br/> $m = -l, ..., 0, ..., l$|$L_z Y = \hbar m Y$|
|Transition dipole moment|$\mu_{fi} = \langle \psi_f \vert \mu_z \cos\theta \vert \psi_i \rangle$|
|Rotational selection rule|$\Delta l = \pm 1, \Delta m = 0$|

### Hydrogen atom

|Description|Equations|
|-:|:-|
|Hydrogen atom Schrodinger equation|$\left[ -\dfrac{\hbar}{2m_e}\dfrac{1}{r^2}\dfrac{\partial}{\partial r}\left(r^2 \dfrac{\partial}{\partial r}\right) + \dfrac{\vec{L}}{2m_er^2} - \dfrac{e^2}{r} \right]\psi(x) = E\psi(x)$|
|Effective potential|$V_{\text{eff}} = \dfrac{\hbar l(l+1)}{2mr^2} - \dfrac{e^2}{r}$|
|Wave function <br/> $n = 1, 2, ...$|$\psi_{nlm}(x) = R_{nl}(r)Y_l^m(\theta, \phi)$|
|Energy eigenvalues <br/> $n = 1, 2, ...$|$E_n = -\dfrac{e^2}{2a_0}\dfrac{1}{n^2} = -\dfrac{me^4}{2\hbar^2}\dfrac{1}{n^2} - \dfrac{R_H}{n^2}$|
|Rydberg's constant|$R_H = 2.179 \times 10^{-18} \mathrm{J} = 13.6 \ \mathrm{eV}$|
|Bohr's radius|$a_0 = \dfrac{\hbar^2}{me^2}$|
|Radial probability distribution|$P_{nl}(r) dr = r^2 R^2_{nl}(r) dr$|

## Many Electron and Proton System

### Many electron atom

|Description|Equations|
|-:|:-|
|Helium Schrodinger equation|$\left[ \underbrace{-\dfrac{\hbar^2}{2m}\nabla_1^2}\_{\text{KE of }e^-_1} \overbrace{-\dfrac{\hbar^2}{2m}\nabla_2^2}\^{\text{KE of }e^-_2} \underbrace{-\dfrac{2e^2}{\vert\mathbf{x}_1\vert}}\_{e^-_1\text{-N attraction}} \overbrace{-\dfrac{2e^2}{\vert\mathbf{x}_2\vert}}\^{e^-_2\text{-N attraction}} + \underbrace{\dfrac{e^2}{\vert\mathbf{x}_1 - \mathbf{x}_2\vert}}\_{e^-_1 \text{-} e^-_2 \text{repulsion}} \right] \psi(\mathbf{x}_1, \mathbf{x}_2) = E \psi(\mathbf{x}_1, \mathbf{x}_2)$|
|Orbital approximation|$\psi(\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_n) = \phi(\mathbf{x}_1)\phi(\mathbf{x}_2)\dots\phi(\mathbf{x}_n)$|
|Hartree orbital equations|$\left[ -\dfrac{\hbar^2 \nabla_i^2}{2m} - \dfrac{Ze^2}{\vert\mathbf{x}\vert} + \sum\limits^N_{j=1, j\not= i} \displaystyle\int \dfrac{e^2 \phi_j^*(\mathbf{x}')\phi_j(\mathbf{x}')}{\vert\mathbf{x} - \mathbf{x}' \vert} d^3\mathbf{x}' \right] \phi_i(\mathbf{x}) = \varepsilon_{ii} \phi_i(\mathbf{x})$|

### Spin

|Description|Equations|
|-:|:-|
|Components of $\hat{\mathbf{S}}$ does not commute|$[\hat{S}_i, \hat{S}_j] = i\hbar \hat{S}_k$|
|Components of $\hat{\mathbf{S}}$ commute with its magnitude|$[\hat{S}_i, S^2] = 0$|
|Eigenvalue of $\hat{\mathbf{S}}^2$|$\hat{\mathbf{S}}^2 \leftrightarrow \hbar^2 s(s+1)$|
|Eigenvalue of $\hat{S}_z$|$\hat{S}_z \leftrightarrow \hbar m_s$|

#### Electron spin

|Description|Equations|
|-:|:-|
|Electron spin|$s = \frac{1}{2}$|
|Spin up function|$\alpha(m_s) = \begin{cases} 1 & m_s = +\frac{1}{2} \\\ 0 & m_s = -\frac{1}{2} \end{cases}$|
|Spin down function|$\beta(m_s) = \begin{cases} 0 & m_s = +\frac{1}{2} \\\ 1 & m_s = -\frac{1}{2} \end{cases}$|
|$\alpha$ is eigenfunction of $\hat{S_z}$|$\hat{S_z} \alpha = +\frac{1}{2}\hbar \alpha$|
|$\beta$ is eigenfunction of $\hat{S_z}$|$\hat{S_z} \beta = -\frac{1}{2}\hbar \beta$|
|$\alpha, \beta$ are eigenfunctions of $\hat{S^2}$|$\hat{S^2} \alpha = \hbar^2 s(s+1) \alpha = \frac{3}{4} \hbar^2 \alpha \newline \hat{S^2} \beta = \hbar^2 s(s+1) \beta = \frac{3}{4} \hbar^2 \beta$|
|Normalization|$\sum\limits_{m_s} \alpha^*\alpha = \sum\limits_{m_s} \beta^*\beta = 1$|
|Orthogonality|$\sum\limits_{m_s} \alpha^*\beta = \sum\limits_{m_s} \beta^*\alpha = 0$|

### Identical particles

|Description|Equations|
|-:|:-|
|Spin-spin permutation operator|$P_{ij} \psi(\mathbf{r}_1, \mathbf{r}_2, \dots, \mathbf{r}_i, \dots, \mathbf{r}_j, \dots, \mathbf{r}_N) = \psi(\mathbf{r}_1, \mathbf{r}_2, \dots, \mathbf{r}_j, \dots, \mathbf{r}_i, \dots, \mathbf{r}_N)$|
|Doing nothing|$P_{ij}P_{ij} = 1$|
|Symmetric eigenvalue|$\lambda = 1$|
|Anti-symmetric eigenvalue|$\lambda = -1$|
|Fermions (e.g. electron)|$\frac{1}{2}$-integer spin, anti-symmetric|
|Bosons|integer spin, symmetric|
|Pauli exclusion principle|$\psi(\mathbf{r}_1, \mathbf{r}_2, \dots, \mathbf{r}_i, \dots, \mathbf{r}_i, \dots, \mathbf{r}_N) = - \psi(\mathbf{r}_1, \mathbf{r}_2, \dots, \mathbf{r}_i, \dots, \mathbf{r}_i, \dots, \mathbf{r}_N) = 0$|
|Slater determinant|$\Psi(\mathrm{x}_1, \mathrm{x}_2, \cdots, \mathrm{x}_N) = \dfrac{1}{\sqrt{N!}} \begin{vmatrix}\chi_1(\mathbf{x}_1) & \chi_2(\mathbf{x}_1) & \cdots & \chi_N(\mathbf{x}_1) \\\ \chi_1(\mathbf{x}_2) & \chi_2(\mathbf{x}_2) & \cdots & \chi_N(\mathbf{x}_2) \\\ \vdots & \vdots & \ddots & \vdots \\\ \chi_1(\mathbf{x}_N) & \chi_2(\mathbf{x}_N) & \cdots & \chi_N(\mathbf{x}_N) \end{vmatrix}$|
|Hartree-Fock orbital equations|$\left[ -\dfrac{\hbar^2\nabla^2}{2m} - \dfrac{Ze^2}{\vert\mathbf{x}\vert} \right] \phi_i(\mathbf{r}) + \displaystyle\sum_{j=1}^N \left[ \phi_i(\mathbf{r}) \int \dfrac{e^2 \phi^*_j(\mathbf{r}) \phi_j(\mathbf{r})}{\vert\mathbf{x} - \mathbf{x}'\vert} d^3r' - \phi_j(\mathbf{r}) \int \dfrac{e^2 \phi^*_j(\mathbf{r}) \phi_i(\mathbf{r})}{\vert\mathbf{x} - \mathbf{x}'\vert} d^3r' \right] = \varepsilon_i \phi_i(\mathbf{r})$|
|Molecular orbital by linear combination of atomic orbitals (MO-LCAO)|$\psi(\mathbf{x}) = c_1 \phi_1 (\mathbf{x}) + c_2 \phi_2 (\mathbf{x}) \newline \mathrm{MO} = c_1 (\mathrm{AO}) + c_2 (\mathrm{AO})$|
|Variational principle|$E = \dfrac{\langle \psi \vert H \vert \psi \rangle}{\langle \psi \vert \psi \rangle}$|
