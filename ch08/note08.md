## Dipole moments and ionic bonding


The classical electric dipole moment $\mu$ with charges $Q_i$ is defined:

$${\vec{\mu} = \sum_{i=1}^{N}Q_i\vec{r_i}}$$

where $N$ is the number of charges, $Q_i$ are the charge magnitudes and $\vec{r_i}$ are their position vectors. Note that both the dipole moment $\vec{\mu}$ and  $\vec{r_i}$ are vectors. Often only the magnitude of the dipole moment is used. 
Dipole moment has SI units of C m (Coulomb $\times$ meter).


To calculate the dipole moment of a molecule, we must calculate the expectation value
for the electric dipole moment operator:

$$
{\vec{\hat{\mu}} = (\hat{\mu}_x, \hat{\mu}_y, \hat{\mu}_z)}
{\hat{\mu}_x = \sum_{i = 1}^{N} Q_ix_i,~~\hat{\mu}_y = \sum_{i = 1}^{N} Q_iy_i,~~\hat{\mu}_z = \sum_{i = 1}^{N} Q_iz_i}
{\left< \vec{\hat{\mu}}\right> = \int\psi^*\vec{\hat{\mu}}\psi d\tau}$$

Here $x_i$, $y_i$ and $z_i$ represent the coordinates of particle $i$ and 
integrations are over the $3N$ dimensional space with a volume element denoted
by $d\tau$.


When atoms with nearly the same electronegativity form bonds, the molecular 
orbitals are distributed evenly over the two atoms and a covalent bond forms. 
If the atoms have somewhat different electronegativities, the molecular
orbitals are unevenly distributed and an ionic bond forms. In a 
pure ionic bond, atomic orbitals do not exhibit any overlap and the 
stabilization is only due to the electrostatic attraction between the charges.
Note that neither \underline{pure} ionic or covalent bonds exist.

**Example** Lithium fluoride (LiF). The ionization energy of Li is 5.4 eV
and the electron affinity of F is 3.5 eV (difference 1.9 eV). These two values are 
sufficiently close to each other and therefore we expect ionic bonding to occur.



This can be compared, for example, with C--H bond, where the difference between
electron affinities and ionization energies are greater than 10 eV. 
Alternatively, one can compare the electronegativities of the atoms to see, if  ionic or covalent bonding is expected to dominate.


At long distances, the two charges in an ionic compound (i.e. A$^+$ -- B$^-$) 
are bound by the Coulomb attraction ($Q_i$ are the total charges of the ions):

$${E(R) = \frac{Q_1Q_2}{4\pi\epsilon_0R}}$$


When the ions approach close enough so that the doubly filled atomic orbitals 
begin to overlap, strong repulsion occurs because molecular orbitals form
with both bonding and antibonding orbitals filled (``antibonding 
orbitals are more repulsive than the bonding orbitals are attractive''). This
is also called the \textit{Pauli repulsion}. To account for this repulsive behavior at 
the short distances, an empirical exponential repulsion term is usually added to the equation.

$${E(R) = \frac{Q_1Q_2}{4\pi\epsilon_0R} + be^{-aR}}$$

where the energy is expressed relative to the dissociated ions. Note that the 
repulsive term is important only at short distances and even at the equilibrium
distance $R_e$ the Coulomb term gives a good approximation for the binding 
energy. Further refinement of this expression can be obtained by including 
terms representing attraction between the induced dipoles and ``instantaneous 
charge fluctuations'' (van der Waals).


The equatio applies to dissociation into separated ions. However, due to 
an avoided crossing between the ionic and covalent states, the dissociation 
occurs into separated neutral atoms. An example of this behavior is shown below.



The dissociation energy into neutral atoms from an ionic state is given by:

$${D_e(\textnormal{MX} \to \textnormal{M} + \textnormal{X}) =
D_e(\textnormal{MX} \to \textnormal{M}^+ + \textnormal{X}^-) - 
E_{ea}(\textnormal{X})}$$

where M denotes metal and X non-metal, $D_e$(MX $\to$ M $+$ X) is the dissociation
energy into atoms, $D_e$(MX $\to$ M$^+$ + X$^-$) is the dissociation energy into 
ions, $E_i$(M) is the ionization energy of metal atom, and $E_{ea}$(X) is the electron
affinity of the non-metal atom.


Note that for heteronuclar diatomic molecules, the molecular orbitals form with non-equivalent atomic orbitals. For example, in HF molecule the H($1s$) and F($2p_z$) form bonding and antibonding orbitals:



By using the variational principle, it is possible to obtain the orbitals as:

$${E = -18.8 {eV: } 
1\sigma_g = 0.19 \times 1s({H}) + 0.98 \times 2p_z({F})}$$

$${E^* = -13.4 {eV: } 
1\sigma_u^* = 0.98 \times 1s({H}) - 0.19 \times 2p_z({F})}$$

The symmetry and energetics of the atomic orbitals determine which atomic orbitals mix to form molecular orbitals. Note that $u/g$ labels cannot be used anymore.


