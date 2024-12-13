## The hydrogen molecule ion

:::{admonition} What you need to know
:class: note

-  We construct trial wavefunction of the molecule from atomic orbitals.
- Applying variational method we find the two MOs to have distinct spatial profiles with one increasing probability of electron between the two nuclei and the other depleating. 
- These MOs are called bonding and anibonding orbitals. They lower and raise eneryg of molecule relative to two separated atoms. 
:::

### Constructing MOs from AOs

:::{figure-md} markdown-fig
<img src="./images/Starting_aos.png" alt="electro" class="bg-primary mb-1" width="400px">

AOs centered on each H atom in $H^{+}_2$ molecule
:::

- The electronic Schrodinger equation for H$_2^+$ can be solved exactly because the equation contains only one particle. However, the  involved math is very complicated and here we take another simpler but  approximate approach. This method will reveal all the important features of chemical bond. An approximate (trial) wavefunction is written as (real functions):

$${\psi_\pm(\vec{r}_1) = c_11s_A(\vec{r}_1) \pm c_21s_B(\vec{r}_1)}$$

- where $1s_A$ and $1s_B$ are hydrogen atom wavefunctions centered at nucleus A 
and B, respectively, and $c_1$ and $c_2$ are constants. This function is
essentially a linear combination of the atomic orbitals (LCAO molecular
orbitals). 
- Because the two protons are identical, we must have $c_1 = c_2 \equiv c$ (also $c > 0$).

- The $\pm$ notation indicates that two different wavefunctions can be 
constructed, one with + sign and the other with $-$ sign. Normalization of the wavefunction requires:

$${\int{\psi_\pm^*\psi_\pm d\tau} = 1}$$



### Overlap integral

In the following, we consider the wavefunction with a ``+'' sign and evaluate the normalization integral ($S$ = overlap integral, which depends on $R$):


$$1 = c^2\int{(1s_A + 1s_B)(1s_A + 1s_B)d \tau}= \\ c^2\int{1s_A^2d \tau} = 1 + c^2{\int{1s_B^2d}\tau}$$

$$+ c^2{\int{1s_A1s_Bd\tau}}{= S}+ c^2{\int{1s_B1s_Ad\tau}}{= S}= c^2(2 + 2S)$$


This can be rewritten as:

$${1 = c^2(2 + 2S) \Rightarrow c = \frac{1}{\sqrt{2 + 2S}}}$$

and the complete ``+'' wavefunction is then:

$${\psi_+ \equiv \psi_g = \frac{1}{\sqrt{2(1 + S)}}(1s_A + 1s_B)}$$

In exactly the same way, we can get the $-$ wavefunction:

$${\psi_- \equiv \psi_u = \frac{1}{\sqrt{2(1 - S)}}(1s_A - 1s_B)}$$



Note that the antibonding orbital has \underline{zero} electron density between the nuclei.

### Bonding vs antibonding orbitals

:::{figure-md} markdown-fig
<img src="./images/b_vs_u.png" alt="electro" class="bg-primary mb-1" width="800px">

Bonding vs anti-bonding wavefunctions (Molecular Orbitals). Show are wavefunctions and probability densities (squares of wavefunctions)
:::

- The main feature of a chemical bond is the increased electron  density between the nuclei. This identifies the + wavefunction as a  **bonding orbital** and $-$ as an **antibonding orbital**.


- When a molecule has a center of symmetry (here at the half-way between the 
nuclei), the wavefunction may or may not change sign when it is inverted
through the center of symmetry. If the origin is placed at the center of 
symmetry then we can assign symmetry labels $g$ and $u$ to the wavefunctions.
If $\psi(x, y, z) = \psi(-x, -y, -z)$ then the symmetry label is
$g$ (even parity) and for $\psi(x, y, z) = -\psi(-x, -y, -z)$ we have $u$ label
(odd parity). 
-  According to this notation the $g$ symmetry orbital is the 
bonding orbital and the $u$ symmetry corresponds to the antibonding orbital.
Later we will see that this is {reversed} for $\pi$-orbitals!

- The overlap integral $S(R)$ can be evaluated analytically (derivation not shown):

$${S(R) = e^{-R}\left( 1 + R + \frac{R^3}{3}\right)}$$

- Note that when $R = 0$ (i.e. the nuclei overlap), $S(0) = 1$ (just a check to see that the expression is reasonable).


## Energy of the hydrogen molecule ion


- Using a linear combination of atomic orbitals, it is possible to calculate the best values, in terms of energy, for the coefficients $c_1$ and $c_2$. Remember that this linear combination can only provide an approximate solution to the $H_2^+$ Schr\"odinger equation. The variational principle provides a systematic way to calculate the energy when $R$ (the distance between the nuclei) is fixed:

$${E = \frac{\int\psi_g^*\hat{H}_e\psi_gd\tau}{\int\psi_g^*\psi_gd\tau} = 
\frac{\int (c_11s_A + c_21s_B)\hat{H}_e(c_11s_A + c_21s_B)d\tau}
{\int (c_11s_A + c_21s_B)^2d\tau}} \\ {= \frac{c_1^2H_{AA} + 2c_1c_2H_{AB} + c_2^2H_{BB}}
{c_1^2 {S_{AA}}{= 1} + 2c_1c_2 {S_{AB}}{= S} + c_2^2 {S_{BB}}{= 1}}
}$$


- where $H_{AA}$, $H_{AB}$, $H_{BB}$, $S_{AA}$, $S_{AB}$ and $S_{BB}$ have been 
used to denote the integrals occurring in variational treatment of the problem. The integrals $H_{AA}$ and $H_{BB}$ are called the Coulomb integrals (sometimes generally termed as matrix elements). 

- This interaction is attractive and therefore its numerical value must be negative. Note that by symmetry $H_{AA} = H_{BB}$. The integral $H_{AB}$ is called the resonance integral and also by symmetry $H_{AB} = H_{BA}$.

### Variational solution 

- To minimize the energy expectation value  with respect to $c_1$ and $c_2$, we have to calculate the partial derivatives of energy with respect to these parameters:


$${E\times (c_1^2 + 2c_1c_2S + c_2^2) = c_1^2H_{AA} + 2c_1c_2H_{AB} + c_2^2H_{BB}}$$

- Both sides can be differentiated with respect to $c_1$ to give:

$${E\times (2c_1 + 2c_2S) + \frac{\partial E}{\partial c_1}\times (c_1^2 + 2c_1c_2S + c_2^2) = 2c_1H_{AA} + 2c_2H_{AB}}$$

- In similar way, differentiation with respect to $c_2$ gives:

$${E\times (2c_2 + 2c_1S) + \frac{\partial E}{\partial c_2}\times (c_1^2 + 2c_1c_2S + c_2^2) = 2c_2H_{BB} + 2c_1H_{AB}}$$

- At the minimum energy (for $c_1$ and $c_2$), the partial derivatives must be zero:

$${c_1(H_{AA} - E) + c_2(H_{AB} - SE) = 0}$$
$${c_2(H_{BB} - E) + c_1(H_{AB} - SE) = 0}$$

- In matrix notation this is (a generalized matrix eigenvalue problem):

$${\begin{pmatrix}H_{AA} - E & H_{AB} - SE\\
H_{AB} - SE & H_{BB} - E\\
\end{pmatrix}\begin{pmatrix} c_1\\ c_2\\\end{pmatrix} = 0}$$

- From linear algebra, we know that a non-trivial solution exists only if:

$${\begin{vmatrix}H_{AA} - E & H_{AB} - SE\\
H_{AB} - SE & H_{BB} - E\\
\end{vmatrix} = 0}$$


### Energies of bonding and antibonding

- It can be shown that $H_{AA} = H_{BB} = E_{1s} + J(R)$, where $E_{1s}$ is the energy of a single hydrogen atom and $J(R)$ is a function of internuclear distance $R$:

$${J(R) = e^{-2R}\left( 1 + \frac{1}{R}\right)}$$

- Furthermore, $H_{AB} = H_{BA} = E_{1s}S(R) + K(R)$, where $K(R)$ is also a function of $R$:

$${K(R) = \frac{S(R)}{R} - e^{-R}\left( 1 + R\right)}$$

- If these expressions are substituted into the previous secular determinant, we get:

$${\begin{vmatrix}E_{1s} + J - E & E_{1s}S + K - SE\\
E_{1s}S + K - SE & E_{1s} + J - E\\
\end{vmatrix} = (E_{1s} + J - E)^2 - (E_{1s}S + K - SE)^2 = 0}$$

- This equation has two roots:

$${E_g(R) = E_{1s} + \frac{J(R) + K(R)}{1 + S(R)}}$$

$${E_u(R) = E_{1s} + \frac{J(R) - K(R)}{1 - S(R)}}$$

:::{figure-md} markdown-fig
<img src="./images/Energies.png" alt="electro" class="bg-primary mb-1" width="600px">

Energies of bonding and antibonding orbitals
:::

- Since energy is a relative quantity, it can be expressed relative to separated
nuclei:

$${\Delta E_g(R) = E_g(R) - E_{1s} = \frac{J(R) + K(R)}{1 + S(R)}}$$

$${\Delta E_u(R) = E_u(R) - E_{1s} = \frac{J(R) - K(R)}{1 - S(R)}}$$




### Comparison of MO energies with experiments 

- These values can be compared with experimental results. The calculated 
ground state equilibrium bond length is 132 pm whereas the experimental value is 106 pm. The binding energy is 170 kJ mol$^{-1}$ whereas the experimental value is 258 kJ  mol$^{-1}$. 
- The excited state (labeled with $u$) leads to repulsive behavior at all bond lengths $R$ (i.e. antibonding). Because the $u$ state lies higher in energy than the $g$ state, the $u$ state is an excited state of H$_2^+$.
- This calculation can be made more accurate by adding more than two terms to
the linear combination. This procedure would also yield more excited state 
solutions. These would correspond $u$/$g$ combinations of $2s$, $2p_x$,
$2p_y$, $2p_z$ etc. orbitals.

### MO diagrams

- It is a common practice to represent the molecular orbitals by molecular 
orbital (MO) diagrams. The formation of bonding and antibonding orbitals can be visualized as follows:

:::{figure-md} markdown-fig
<img src="./images/h2plus_diag.png" alt="electro" class="bg-primary mb-1" width="400px">

Molecular Orbital diagram
:::

- $\sigma$ orbitals When two $s$ or $p_z$ orbitals interact,
a $\sigma$ molecular orbital is formed. The notation $\sigma$ specifies
the amount of angular momentum about the molecular axis (for $\sigma$, $\lambda = 0$ with $L_z = \pm\lambda\hbar$). In many-electron systems, both bonding and antibonding $\sigma$  orbitals can each hold a maximum of two electrons. Antibonding orbitals are often  denoted by *.

:::{figure-md} markdown-fig
<img src="./images/MO_variety.png" alt="electro" class="bg-primary mb-1" width="800px">

MOs for homonuclear molecules have distinct symmetry
:::

- $\pi$ orbitals. When two $p_{x,y}$ orbitals interact, a $\pi$ molecular orbital forms. $\pi$-orbitals are doubly degenerate: $\pi_{+1}$ and $\pi_{-1}$ (or alternatively $\pi_x$ and $\pi_y$), where the $+1/-1$ refer to the eigenvalue of the $L_z$ operator ($\lambda = \pm1$). In many-electron systems a bonding $\pi$-orbital can therefore hold a maximum of 4 electrons (i.e. both $\pi_{+1}$ and $\pi_{-1}$ each can hold two electrons). The same holds for the antibonding $\pi$ orbitals. Note that only the atomic orbitals of the same symmetry mix to form molecular orbitals (for example, $p_z - p_z$, $p_x -  p_x$ and $p_y - p_y$). When atomic $d$ orbitals mix to form molecular orbitals, $\sigma (\lambda = 0)$, $\pi (\lambda = \pm 1)$ and $\delta (\lambda = \pm 2)$ MOs form. 

- Excited state energies of $H_2^+$ resulting from a calculation employing an extended basis set (e.g. more terms in the LCAO) are shown on the left below. The MO energy diagram, which includes the higher energy molecular orbitals, is shown on the right hand side. Note that the energy order of the MOs depends on the molecule.

:::{figure-md} markdown-fig
<img src="./images/MO_summary.png" alt="electro" class="bg-primary mb-1" width="400px">

Mo diagram of homonuclear molecules follows similiar pattern with alternating bonding and anti-bonding MOs. 
:::

## Molecular orbital description of hydrogen molecule


### Setting up Hamiltonian 

![](images/H2mol-fig1.png)




$${H = -\frac{\hbar^2}{2m_e}\left( \Delta_1 + \Delta_2\right)
+ \frac{e^2}{4\pi\epsilon_0}\left(\frac{1}{R} + \frac{1}{r_{12}} - \frac{1}{r_{A1}} 
- \frac{1}{r_{A2}} - \frac{1}{r_{B1}} - \frac{1}{r_{B2}}\right)}$$


- The main difficulty in the molecular Hamiltonian is the $1/r_{12}$
term, which connects the two electrons to each other. This means that a simple  product wavefunction is not sufficient. No known analytic solutions have been  found to the electronic Schr\"odinger equation of $H_2$. 
- For this reason, we will attempt to solve the problem approximately by using the LCAO-MO approach that we  used previously. For example, the ground state for H$_2$ is obtained by placing  two electrons with opposite spins on the $1\sigma_g$ orbital. This assumes that
the wavefunction is expressed as antisymmetrized product (e.g. a Slater determinant).

### Constructing MOs for hydrogen molecule

- According to the Pauli principle, two electrons with opposite spins can be assigned to a given spatial orbital. As a first approximation, we assume that the molecular orbitals in $H_2$ remain the same as in $H_2^+$. Hence we can say that both electrons occupy the $1\sigma_g$ orbital (the ground state) and the electronic configuration is denoted by ($1\sigma_g$)$^2$. This is a similar notation  that we used previously for atoms (for example, He atom is ($1s$)$^2$).


- The molecular orbital for electron 1 in $1\sigma_g$ molecular orbital is:

$${1\sigma_g(1) = \frac{1}{\sqrt{2(1 + S)}}(1s_A(1) + 1s_B(1))}$$


- Previously we found that the total wavefunction must be antisymmetric with respect to change in electron indices. This can be achieved by using the  Slater determinant:

$${\psi_{MO}^{(1\sigma_g)^2} = \frac{1}{\sqrt{2}}\begin{vmatrix}
1\sigma_g(1)\alpha (1) & 1\sigma_g(1)\beta (1)\\
1\sigma_g(2)\alpha (2) & 1\sigma_g(2)\beta (2)\\
\end{vmatrix}}$$

- where $\alpha$ and $\beta$ denote the electron spin. The Slater determinant can be expanded as follows:

$${\psi_{MO}^{(1\sigma_g)^2} = \frac{1}{\sqrt{2}} 
 (1\sigma_g(1)1\sigma_g(2)\alpha (1)\beta (2) 
- 1\sigma_g(1)1\sigma_g(2)\beta (1)\alpha (2))}
{= \frac{1}{2\sqrt{2}(1 + S_{AB})}(1s_A(1) + 1s_B(1))(1s_A(2) + 1s_B(2))
(\alpha (1)\beta (2) - \alpha (2)\beta (1))}$$

- Note that this wavefunction is only approximate and is definitely not an  eigenfunction of the H$_2$ electronic Hamiltonian. Thus we must calculate the  electronic energy by taking an expectation value of this wavefunction with the Hamiltonian (the actual calculation not shown):

$${E(R) = 2E_{1s} + \frac{e^2}{4\pi\epsilon_0 R} 
- \textnormal{integrals}}$$


- where $E_{1s}$ is the electronic energy of one hydrogen atom. The second term  represents the Coulomb repulsion between the two positively charged nuclei and the last term (``integrals'') contains a series of integrals describing the  interactions of various charge distributions with one another (see P. W.  Atkins, Molecular Quantum Mechanics, Oxford University Press). With this approach, the minimum energy is reached at $R$ = 84 pm (experimental 74.1 pm)
and dissociation energy $D_e$ = 255 kJ $mol^{-1}$ (experimental 458 kJ 
$mol^{-1}$).

### Improving upon simple MO approximation

![](images/H2mol-fig2.png)

- This simple approach is not very accurate but it demonstrates that the method  works. To improve the accuracy, ionic and covalent terms should be considered
separately:

$${{1s_A(1)1s_A(2)}_{\textnormal{Ionic (H$^-$ + H$^+$)}}
+ {[1s_A(1)1s_B(2) + 1s_A(2)1s_B(1)]}_{\textnormal{Covalent (H + H)}}
+ {1s_B(1)1s_B(2)}_{\textnormal{Ionic (H$^+$ + H$^-$)}}}$$

Both covalent and ionic terms can be introduced into the wavefunction with their 
own variational parameters $c_1$ and $c_2$:

$${\psi = c_1\psi_{\textnormal{covalent}} + c_2\psi_{\textnormal{ionic}}}$$

$${\psi_{\textnormal{covalent}} = 1s_A(1)1s_B(2) + 1s_A(2)1s_B(1)}$$

$${\psi_{\textnormal{ionic}} = 1s_A(1)1s_A(2) + 1s_B(1)1s_B(2)}$$


Note that the variational constants $c_1$ and $c_2$ depend on the 
internuclear distance $R$. Minimization of the energy expectation value with 
respect to these constants gives $R_e$ = 74.9 pm (experiment 74.1 pm) and $D_e$
= 386 kJ $mol^{-1}$ (experiment 458 kJ $mol^{-1}$). Further improvement could 
be achieved by adding higher atomic orbitals into the wavefunction. The 
previously discussed Hartree-Fock method provides an efficient way for
solving the problem. Recall that this method is only approximate as it ignores 
the electron-electron correlation effects completely. The full treatment 
requires use of configuration interaction methods, which can yield essentially 
exact results: $D_e$ = 36117.8 $cm^{-1}$ (CI) vs. $36117.3\pm1.0\, cm^{-1}$ 
(exp) and $R_e$ = 74.140 pm vs. 74.139 pm (exp).

### Term symbols for diatomic molecules

In diatomic (and linear) molecules, the quantization axis is chosen along the 
molecule. When spin-orbit interaction is negligible, this allows us to define 
the total orbital and spin angular momenta about the molecular axis:

$${\Lambda = \left|\lambda_1 + \lambda_2 + ...\right|}$$

where $\lambda_i = 0$ for a $\sigma$ orbital, $\lambda_i = \pm 1$ for a $\pi$ orbital, 
$\lambda_i = \pm 2$ for a $\delta$ orbital, etc. The value of $\Lambda$ is
expressed using the following capital Greek letters (just like we had $s$, $p$, $d$ for 
atoms):

| $\Lambda$ | = | 0        | 1     | 2        | 3      | ... |
|-----------|---|----------|-------|----------|--------|-----|
| Symbol    | = | $\Sigma$ | $\Pi$ | $\Delta$ | $\Phi$ | ... |


- The state multiplicity is given by $2S + 1$ where $S$ is the sum of the electron spins in the molecule. The term symbol for a diatomic molecule is represented by:

$${^{2S+1}\Lambda}$$

