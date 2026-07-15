---
kernelspec:
  name: python3
  display_name: Python 3
---

# Dipole Moments and Ionic Bonding

:::{note} **What you will learn**

- The **electric dipole moment** is computed as an expectation value of the dipole operator and measures the asymmetry of the charge distribution in a molecule.
- When bonded atoms differ in electronegativity, the molecular orbitals become unevenly distributed, producing partial ionic character and a permanent dipole.
- An **ionic bond** is held together by Coulomb attraction at long range, balanced by Pauli repulsion at short range, leading to a simple analytic model of the binding curve.
- Weak **intermolecular forces** (dipole-dipole, dipole-induced-dipole, and dispersion) all scale as $1/R^6$ and combine with Pauli repulsion to give the **Lennard-Jones** potential.
:::

### The electric dipole moment

The classical electric dipole moment $\vec{\mu}$ with charges $Q_i$ is defined as:

$${\vec{\mu} = \sum_{i=1}^{N}Q_i\vec{r_i}}$$

where $N$ is the number of charges, $Q_i$ are the charge magnitudes, and $\vec{r_i}$ are their position vectors. Both the dipole moment $\vec{\mu}$ and $\vec{r_i}$ are vectors. Often only the magnitude of the dipole moment is used. The dipole moment has SI units of C m (Coulomb times meter).

To calculate the dipole moment of a molecule, we calculate the expectation value of the electric dipole moment operator:

$$
{\vec{\hat{\mu}} = (\hat{\mu}_x, \hat{\mu}_y, \hat{\mu}_z)}
$$

$$
{\hat{\mu}_x = \sum_{i = 1}^{N} Q_ix_i,~~\hat{\mu}_y = \sum_{i = 1}^{N} Q_iy_i,~~\hat{\mu}_z = \sum_{i = 1}^{N} Q_iz_i}
$$

$$
{\left< \vec{\hat{\mu}}\right> = \int\psi^*\vec{\hat{\mu}}\psi d\tau}
$$

Here $x_i$, $y_i$, and $z_i$ represent the coordinates of particle $i$, and the integrations are over the $3N$-dimensional space with volume element $d\tau$.

### Ionic versus covalent bonds

When atoms with nearly the same electronegativity form bonds, the molecular orbitals are distributed evenly over the two atoms and a covalent bond forms. If the atoms have somewhat different electronegativities, the molecular orbitals are unevenly distributed and an ionic bond forms. In a pure ionic bond, atomic orbitals do not overlap at all and the stabilization is due only to the electrostatic attraction between the charges. Note that neither pure ionic nor pure covalent bonds exist.

:::{tip} **Example: lithium fluoride (LiF)**

The ionization energy of Li is 5.4 eV and the electron affinity of F is 3.5 eV (a difference of 1.9 eV). These two values are sufficiently close to each other, and therefore we expect ionic bonding to occur.

This can be compared, for example, with the C-H bond, where the difference between electron affinities and ionization energies is greater than 10 eV. Alternatively, one can compare the electronegativities of the atoms to see whether ionic or covalent bonding is expected to dominate.
:::

### The ionic binding curve

At long distances, the two charges in an ionic compound (A$^+$ and B$^-$) are bound by the Coulomb attraction ($Q_i$ are the total charges of the ions):

$${E(R) = \frac{Q_1Q_2}{4\pi\epsilon_0R}}$$

When the ions approach close enough that the doubly filled atomic orbitals begin to overlap, strong repulsion occurs because molecular orbitals form with both bonding and antibonding orbitals filled ("antibonding orbitals are more repulsive than bonding orbitals are attractive"). This is also called the **Pauli repulsion**. To account for this repulsive behavior at short distances, an empirical exponential repulsion term is usually added:

:::{important} **Model ionic binding curve**

$${E(R) = \frac{Q_1Q_2}{4\pi\epsilon_0R} + be^{-aR}}$$
:::

where the energy is expressed relative to the dissociated ions. The repulsive term is important only at short distances, and even at the equilibrium distance $R_e$ the Coulomb term gives a good approximation for the binding energy. Further refinement can be obtained by including terms representing attraction between induced dipoles and instantaneous charge fluctuations (van der Waals).

This equation applies to dissociation into separated ions. However, due to an avoided crossing between the ionic and covalent states, dissociation actually occurs into separated neutral atoms.

The dissociation energy into neutral atoms from an ionic state is given by:

$${D_e(\textnormal{MX} \to \textnormal{M} + \textnormal{X}) =
D_e(\textnormal{MX} \to \textnormal{M}^+ + \textnormal{X}^-) - 
E_{ea}(\textnormal{X})}$$

where M denotes the metal and X the non-metal, $D_e$(MX $\to$ M $+$ X) is the dissociation energy into atoms, $D_e$(MX $\to$ M$^+$ + X$^-$) is the dissociation energy into ions, $E_i$(M) is the ionization energy of the metal atom, and $E_{ea}$(X) is the electron affinity of the non-metal atom.

For heteronuclear diatomic molecules, the molecular orbitals form from non-equivalent atomic orbitals. For example, in the HF molecule the H($1s$) and F($2p_z$) orbitals form bonding and antibonding orbitals. By using the variational principle, the orbitals are obtained as:

$${E = -18.8 \textnormal{ eV: } 
1\sigma = 0.19 \times 1s(\textnormal{H}) + 0.98 \times 2p_z(\textnormal{F})}$$

$${E^* = -13.4 \textnormal{ eV: } 
1\sigma^* = 0.98 \times 1s(\textnormal{H}) - 0.19 \times 2p_z(\textnormal{F})}$$

The symmetry and energetics of the atomic orbitals determine which atomic orbitals mix to form molecular orbitals. Note that the $u/g$ labels can no longer be used for heteronuclear molecules.

### Intermolecular forces

Consider two atoms or molecules that do not form chemical bonds. As they approach each other, a small binding (van der Waals, vdW) occurs first, followed by strong repulsion (Pauli repulsion) at shorter distances. The repulsion follows from the overlap of the doubly occupied orbitals discussed earlier. The small vdW binding contributes to physical processes like freezing and boiling. At large distances, the interaction energy approaches zero.

The energy unit in pair potentials is often K (Kelvin; multiplication by the Boltzmann constant gives energy). Distances are commonly expressed in angstroms (Å) or Bohr (atomic units).

### Dipole-dipole interaction

The dipole-dipole interaction between two freely rotating dipoles (molecules with dipole moments) averages to zero. However, because their mutual potential energy depends on relative orientation, the molecules do not in fact rotate completely freely, even in the gas phase. The lower energy orientations are marginally favored, so there is a nonzero average interaction between the dipoles. This interaction has the form (the **Keesom interaction**):

$${\left< V(R) \right>_{dd} = -\frac{2}{3kT}\left( \frac{\mu_A\mu_B}{4\pi\epsilon_0} 
\right)^2 \times \frac{1}{R^6}}$$

where $k$ is the Boltzmann constant, $T$ is the temperature (K), $\mu_A$ and $\mu_B$ are the dipole moments of the molecules, $\epsilon_0$ is the vacuum permittivity, and $R$ is the distance between the molecules. The angular brackets denote thermal averaging. As the temperature increases, this interaction becomes less important; the interaction is negative (attractive).

### Dipole-induced dipole interaction

If molecule A has a permanent dipole moment $\mu_A$, it creates an electric field that polarizes the electron cloud of molecule B. This creates an induced dipole moment proportional to $\alpha_B\mu_A$, where $\alpha_B$ is the (averaged) polarizability of molecule B. The dipole-induced-dipole attractive energy can be shown to be (including the effect both ways):

$${\left< V(R)\right>_{ind} = -4\frac{\alpha_B\mu_A^2 + \alpha_A\mu_B^2}
{(4\pi\epsilon_0)^2}\frac{1}{R^6}}$$

### Dispersion forces

This attractive force has its origin in electron correlation. A simple model (the "Drude oscillator") considers correlated displacements of electrons in the two atoms or molecules, which generate instantaneous dipoles and an attractive interaction. This interaction occurs even between molecules with no permanent dipole or charge. The exact expression is complicated, but to a good approximation:

$${\left< V(R)_{disp}\right> = -\frac{3}{2}\left(\frac{E_AE_B}{E_A + E_B}\right)
\frac{\alpha_A\alpha_B}{(4\pi\epsilon_0)^2}\frac{1}{R^6}}$$

The above three terms add to give the total attractive energy between molecules A and B. This interaction depends strongly on the interacting species, but it is typically a few meV around 5 Å separation.

### The Lennard-Jones potential

It is common to express the interaction energy between two atoms or molecules using the Lennard-Jones form (or 6-12 form):

:::{important} **Lennard-Jones potential**

$${V(R) = 4\epsilon\left[\left(\frac{\sigma}{R}\right)^{12} - 
\left(\frac{\sigma}{R}\right)^6\right]}$$
:::

The first term (left) represents the Pauli repulsion and the second term (right) represents the van der Waals binding discussed previously. The interaction energy is often called the potential energy because, in molecular dynamics simulations (nuclear dynamics), it represents the potential energy. The depth of the well is $\epsilon$, which occurs at distance $R_e = 2^{1/6}\sigma$. These parameters may be obtained from experiment or theory. Typical values for $\epsilon$ and $\sigma$ for different atom and molecule pairs are given below (rotationally averaged).

|            | $\epsilon$ [K] | $\sigma$ [Å] | Freezing pt. [K] | Boiling pt. [K] |
|------------|----------------|----------------|-----------------|-----------------|
| $Ar$       | 120            | 3.41           | 84.0            | 87.3            |
| $Xe$       | 221            | 4.10           | 161.3           | 165.1           |
| $H_2$      | 37             | 2.93           | 13.8            | 20.3            |
| $N_2$      | 95.1           | 3.70           | 63.3            | 77.4            |
| $O_2$      | 118            | 3.58           | 54.8            | 90.2            |
| $Cl_2$     | 256            | 4.40           | 172.2           | 239.1           |
| $CO_2$     | 197            | 4.30           | 216.6           | 194.7           |
| $CH_4$     | 148            | 3.82           | 89              | 111.7           |
| $C_6 H_6$  | 243            | 8.60           | 278.7           | 353.2           |

Note the loose correlation between $\epsilon$ and the freezing and boiling temperatures.

### Problems

::::{admonition} **Problem 1: Bond order and stability**
:class: note

Using the molecular orbital filling diagram, write the ground-state electron configuration of $O_2$ and determine its bond order. Predict whether $O_2$ is diamagnetic or paramagnetic, and explain how the MO picture accounts for this property.

:::{admonition} **Solution:**
:class: dropdown solution

$O_2$ has 16 electrons. Filling the MOs in order of increasing energy gives the configuration $(1\sigma_g)^2(1\sigma_u)^2(2\sigma_g)^2(2\sigma_u)^2(3\sigma_g)^2(1\pi_u)^4(1\pi_g)^2$.

The bond order is

$$\text{BO} = \frac{1}{2}\left(N_{\text{bonding}} - N_{\text{antibonding}}\right) = \frac{1}{2}(10 - 6) = 2.$$

The two highest-energy electrons occupy the doubly degenerate $1\pi_g$ antibonding orbitals. By Hund's rule they occupy separate orbitals with parallel spins, leaving two unpaired electrons. Therefore $O_2$ is **paramagnetic**, a result that the simple Lewis structure fails to predict but that the MO picture explains naturally.
:::
::::

::::{admonition} **Problem 2: Overlap integral check**
:class: note

The overlap integral for two hydrogen 1s orbitals is $S(R) = e^{-R}\left(1 + R + \frac{R^3}{3}\right)$ in atomic units, as given in the $H_2^+$ lecture. Verify the limiting value of $S$ as $R \to 0$ and explain physically why $S$ decreases as $R$ increases.

:::{admonition} **Solution:**
:class: dropdown solution

At $R = 0$ the two orbitals coincide, so $S(0) = e^{0}(1 + 0 + 0) = 1$, which simply states that a normalized orbital overlaps perfectly with itself.

As $R$ grows, the exponential factor $e^{-R}$ dominates and drives $S \to 0$. Physically, the two 1s orbitals decay exponentially away from their nuclei, so the region where both have appreciable amplitude shrinks as the nuclei separate. Less shared amplitude means a smaller overlap integral, which is why bonding (which depends on overlap) weakens at large internuclear distance.
:::
::::

::::{admonition} **Problem 3: Huckel energy of the allyl radical**
:class: note

Set up the Huckel secular determinant for the allyl system (three $p$ orbitals on a chain of three carbons). Show that the orbital energies are $E = \alpha + \sqrt{2}\,\beta$, $\alpha$, and $\alpha - \sqrt{2}\,\beta$.

:::{admonition} **Solution:**
:class: dropdown solution

Numbering the carbons 1-2-3, the secular determinant in terms of $x = (\alpha - E)/\beta$ is

$$\begin{vmatrix} x & 1 & 0 \\ 1 & x & 1 \\ 0 & 1 & x \end{vmatrix} = 0.$$

Expanding gives $x(x^2 - 1) - 1\cdot(x - 0) = x^3 - 2x = 0$, so $x(x^2 - 2) = 0$ with roots $x = 0$ and $x = \pm\sqrt{2}$.

Converting back with $E = \alpha - x\beta$ gives the three orbital energies

$$E = \alpha + \sqrt{2}\,\beta, \quad E = \alpha, \quad E = \alpha - \sqrt{2}\,\beta,$$

with the nonbonding level at exactly $\alpha$.
:::
::::

::::{admonition} **Problem 4: Dipole moment of a diatomic**
:class: note

A diatomic molecule has a measured dipole moment of $1.08$ D and an internuclear separation of $127$ pm. Estimate the partial charge $\delta$ (in units of the elementary charge $e$) on each atom, and compare it with a fully ionic model. (Use $1$ D $= 3.336 \times 10^{-30}$ C m and $e = 1.602 \times 10^{-19}$ C.)

::::

::::{admonition} **Problem 5: Lennard-Jones minimum**
:class: note

Starting from the Lennard-Jones potential $V(R) = 4\epsilon\left[(\sigma/R)^{12} - (\sigma/R)^6\right]$, show that the minimum occurs at $R_e = 2^{1/6}\sigma$ and that the depth of the well there is exactly $-\epsilon$.

::::

::::{admonition} **Problem 6: Ionic versus covalent character**
:class: note

The ionization energy of sodium is $5.14$ eV and the electron affinity of chlorine is $3.62$ eV. Using the reasoning applied to LiF in the lecture, argue whether NaCl is expected to be predominantly ionic or covalent, and identify what additional energetic contribution makes the ionic molecule bound despite the unfavorable electron-transfer balance.

::::

:::{seealso} Chapter demos
Run this chapter's interactive Python demos: [H2+ molecular ion](../demos/17-demo-h2plus.md) · [Benzene by PySCF](../demos/18-demo-benzene.md)
:::
