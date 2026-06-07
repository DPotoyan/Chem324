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

## Intermolecular forces 


Consider two atoms or molecules that do not form chemical bonds. When they approach each other, a small binding (van der Waals; vdW) occurs first and after that strong  repulsion (Pauli repulsion). The repulsion follows from the overlap of the doubly  occupied orbitals as discussed earlier. The small vdW binding contributes to physical  processes like freezing and boiling. At large distances, the interaction energy  approaches zero. For example, a ``pair potential'' might look like:


- Note that the energy unit above is K (Kelvin; i.e. multiplication by the Boltzmann constant gives energy). Very often \AA ngstr\"oms (\AA) or Bohr (atomic units; a.u.) are used for units of distance.


### Dipole - dipole interaction.

 The dipole -- dipole interaction between two
freely rotating dipoles (i.e., molecules with dipole moments) is zero. However, because their mutual potential energy depends on their relative orientation, the molecules do not in fact rotate completely freely, even in gas phase. The lower energy orientations are marginally favored, so there is a nonzero average interaction between the dipoles. It can be shown that this interaction has the form (\textit{the Keesom interaction}):

$${\left< V(R) \right>_{dd} = -\frac{2}{3kT}\left( \frac{\mu_A\mu_B}{4\pi\epsilon_0} 
\right)^2 \times \frac{1}{R^6}}$$

where $k$ is the Boltzmann constant, $T$ is the temperature (K), $\mu_A$ and $\mu_B$ 
are dipole moments of the molecules, $\epsilon_0$ is the vacuum permittivity and $R$
is the distance between the molecules. The angular brackets denote thermal averaging 
(statistical mechanics). Note that as the temperature increases, this interaction 
becomes less important and that the interaction is negative (attractive).


### Dipole-induced dipole interaction

 If molecule A has a permanent dipole
moment $\mu_A$, it creates an electric field that polarizes the electron cloud
on molecule B. This creates an induced dipole moment proportional to $\alpha_B\mu_A$,
where $\alpha_B$ is called the (averaged) polarizability of molecule B. The dipole 
- induced dipole attractive energy can be shown to be (including the effect both ways):

$${\left< V(R)\right>_{ind} = -4\frac{\alpha_B\mu_A^2 + \alpha_A\mu_B^2}
{(4\pi\epsilon_0)^2}\frac{1}{R^6}}
$$



### Dispersion forces

 This attractive force has its origins
in the concept of electron correlation. A simple model (``Drude oscillator'') 
considers correlated displacements of electrons in the two atoms / molecules,
which generate instantaneous dipoles and attractive interaction. Of course, this is 
model not entirely correct because this process does not involve real time (i.e.
only quantum mechanical motion). This interaction occurs even between molecules with no 
permanent dipole or charge.

The exact form for the expression is very complicated, but to a good approximation:

$${\left< V(R)_{disp}\right> = -\frac{3}{2}\left(\frac{E_AE_B}{E_A + E_B}\right)
\frac{\alpha_A\alpha_B}{(4\pi\epsilon_0)^2}\frac{1}{R^6}}$$


The above three terms add to give the total attractive energy between molecules A and B. This interaction depends strongly on the interacting atoms/molecules but it is typically few meV around 5 \AA{} separation.


It is common to express the interaction energy between two atoms / molecules by 
using the Lennard-Jones form (or *6-12 form*):

$${V(R) = 4\epsilon\left[\left(\frac{\sigma}{R}\right)^{12} - 
\left(\frac{\sigma}{R}\right)^6\right]}$$


The first term (left) represents the Pauli repulsion and the second term (right) 
represents the van der Waals binding discussed previously. Note that the interaction 
energy is often called the potential energy because in molecular dynamics 
simulations (nuclear dynamics), this represents the potential energy. The magnitude 
of binding in this potential is $\epsilon$, which occurs at distance $R_e = 2^{1/6}\sigma$. These parameters may be obtained from experiments or theory. Typical values for $\epsilon$ and $\sigma$ in different atom / molecule pairs are given below
(rotationally averaged).

|            | $\epsilon$ [K] | $\sigma$ $[\AA]$ | Freezing pt.[K] | Boiling pt. [K] |
|------------|----------------|----------------|-----------------|-----------------|
| $Ar$         | 120            | 3.41           | 84.0            | 87.3            |
| $Xe$         | 221            | 4.10           | 161.3           | 165.1           |
| $H_2$      | 37             | 2.93           | 13.8            | 20.3            |
| $N_2$      | 95.1           | 3.70           | 63.3            | 77.4            |
| $O_2$      | 118            | 3.58           | 54.8            | 90.2            |
| $Cl_2$     | 256            | 4.40           | 172.2           | 239.1           |
| $CO_2$     | 197            | 4.30           | 216.6           | 194.7           |
| $CH_4$     | 148            | 3.82           | 89              | 111.7           |
| $C_6 H_6$ | 243            | 8.60           | 278.7           | 353.2           |


Note the loose correlation between $\epsilon$ and the freezing/boiling temperatures.



