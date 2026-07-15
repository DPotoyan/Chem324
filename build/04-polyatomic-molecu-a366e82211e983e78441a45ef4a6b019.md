---
kernelspec:
  name: python3
  display_name: Python 3
---

# Electronic Structure of Polyatomic Molecules

:::{note} **What you will learn**

- The MO picture extends across the homonuclear diatomic series, where filling alternating bonding and antibonding orbitals predicts **bond order, bond length, and dissociation energy**.
- The **non-crossing rule:** molecular orbital states of the same symmetry never cross as a function of internuclear distance.
- The **valence bond approach** builds bonds from overlapping atomic orbitals, and it naturally gives rise to **hybrid orbitals** ($sp$, $sp^2$, $sp^3$) that explain molecular geometries.
- Worked examples for $BeH_2$, $BH_3$, $CH_4$, and $H_2O$ connect hybridization to the observed shapes of small molecules.
- Practical numerical quantum chemistry replaces atomic orbitals with **Gaussian basis sets** that allow analytic evaluation of the required integrals.
:::

### Orbitals of homonuclear diatomic molecules

Which atomic orbitals mix to form molecular orbitals, and what are their relative energies? The interactive viewer below can be used to obtain the energy order of molecular orbitals and indicates the atomic orbital limits.

<iframe src="https://al2me6.github.io/evanescence/"
        width="800"
        height="500"
        allowfullscreen>
</iframe>

### The non-crossing rule

States with the same symmetry never cross.

| Bonding orbitals:     | $1\sigma_g$, $2\sigma_g$, $1\pi_u$, etc.       |
|-----------------------|------------------------------------------------|
| Antibonding orbitals: | $1\sigma_u^*$, $2\sigma_u^*$, $1\pi_g^*$, etc. |

:::{figure} images/non-crossing-rule.png
:alt: Non-crossing rule for molecular orbital correlation diagram
:width: 600px

Fig. 1 Correlation diagram illustrating the non-crossing rule: orbitals of the same symmetry avoid each other as the internuclear distance changes.
:::

### Table of molecular orbitals

The orbitals are filled with electrons in order of increasing energy. Note that $\pi$, $\delta$, etc. orbitals can hold a total of 4 electrons. If only one bond is formed, we say that the bond order (BO) is 1. If two bonds form (for example, one $\sigma$ and one $\pi$), the bond order is 2 (a double bond). Molecular orbitals always come in pairs: bonding and antibonding.

| Molecule | Electrons | Configuration                    | Term sym.    | BO  | $R_e$ (Å) | $D_e$ (eV)   |
|----------|------------|----------------------------------|--------------|-----|-------------|--------------|
| $H_2^+$  | 1          | $(1\sigma_g)$                    | $^2\Sigma_g$ | 0.5 | 1.060       | 2.793        |
| $H_2$    | 2          | $(1\sigma_g)^2$                  | $^1\Sigma_g$ | 1.0 | 0.741       | 4.783        |
| $He_2^+$ | 3          | $(1\sigma_g)^2(1\sigma_u)$       | $^2\Sigma_u$ | 0.5 | 1.080       | 2.5          |
| $He_2$   | 4          | $(1\sigma_g)^2(1\sigma_u)^2$     | $^1\Sigma_g$ | 0.0 |             |              |
| $Li_2$   | 6          | $He_2(2\sigma_g)^2$              | $^1\Sigma_g$ | 1.0 | 2.673       | 1.14         |
| $Be_2$   | 8          | $He_2(2\sigma_g)^2(2\sigma_u)^2$ | $^1\Sigma_g$ | 0.0 |             |              |
| $B_2$    | 10         | $Be_2(1\pi_u)^2$                 | $^3\Sigma_g$ | 1.0 | 1.589       | $\approx 3.0$ |
| $C_2$    | 12         | $Be_2(1\pi_u)^4$                 | $^1\Sigma_g$ | 2.0 | 1.242       | 6.36         |
| $N_2^+$  | 13         | $Be_2(1\pi_u)^4(3\sigma_g)$      | $^2\Sigma_g$ | 2.5 | 1.116       | 8.86         |
| $N_2$    | 14         | $Be_2(1\pi_u)^4(3\sigma_g)^2$    | $^1\Sigma_g$ | 3.0 | 1.094       | 9.902        |
| $O_2^+$  | 15         | $N_2(1\pi_g)$                    | $^2\Pi_g$    | 2.5 | 1.123       | 6.77         |
| $O_2$    | 16         | $N_2(1\pi_g)^2$                  | $^3\Sigma_g$ | 2.0 | 1.207       | 5.213        |
| $F_2$    | 18         | $N_2(1\pi_g)^4$                  | $^1\Sigma_g$ | 1.0 | 1.435       | 1.34         |
| $Ne_2$   | 20         | $N_2(1\pi_g)^4(3\sigma_u)^2$     | $^1\Sigma_g$ | 0.0 |             |              |

:::{note} **Reading the table**

- A missing value of $R_e$ means that the molecule is not stable.
- Hund's rules predict that the electron configuration with the largest multiplicity lies lowest in energy when the highest occupied MOs are degenerate.
:::

### The valence bond approach

- The valence bond method is an approximate approach that is useful for understanding the formation of chemical bonds. In particular, concepts like hybrid orbitals follow directly from it.

- The valence bond method is based on the idea that a chemical bond forms when there is non-zero overlap between the atomic orbitals of the participating atoms. The atomic orbitals must therefore have the same symmetry in order to gain overlap.

- Hybrid orbitals are essentially linear combinations of atomic orbitals that belong to a single atom. Note that hybrid orbitals are not meaningful for free atoms, as they only begin to form when other atoms approach. The idea is best illustrated through the following examples.

### Example 1: The $BeH_2$ molecule

- The Be atom has the atomic electron configuration He$2s^2$. The two approaching hydrogens perturb the atomic orbitals, and the two outer-shell electrons reside on the two hybrid orbitals formed (the $z$-axis is along the molecular axis):

:::{figure} images/BeH1.png
:alt: sp hybrid orbital formation in BeH2
:width: 500px

Fig. 2 Formation of $sp$ hybrid orbitals on the Be atom in $BeH_2$.
:::

$${\psi_{sp}^1 = \frac{1}{\sqrt{2}}(2s + 2p_z)}$$

$${\psi_{sp}^2 = \frac{1}{\sqrt{2}}(2s - 2p_z)}$$

The hybrid orbitals further form two molecular $\sigma$ orbitals:

:::{figure} images/BeH2.png
:alt: sigma bonds formed by sp hybrids in BeH2
:width: 500px

Fig. 3 The $sp$ hybrids on Be each form a $\sigma$ bond with a hydrogen 1s orbital.
:::

$${\psi = c_11s_A + c_2\psi_{sp}^1}$$

$${\psi' = c_1'1s_B + c_2'\psi_{sp}^2}$$

:::{figure} images/BeH2-orbs.png
:alt: BeH2 molecular orbitals
:width: 500px

Fig. 4 The resulting linear $\sigma$ framework of $BeH_2$.
:::

- **This form of hybridization is called $sp$.** It means that one $s$ and one $p$ orbital participate in forming the hybrid orbitals. For $sp$ hybrids, linear geometries are favored, and here H-Be-H is indeed linear. Each MO between Be and H contains two shared electrons. Note that the number of initial atomic orbitals and the number of hybrid orbitals formed must be identical: here $s$ and $p$ atomic orbitals give two $sp$ hybrid orbitals. Hybrid orbitals should be orthonormalized.

### Example 2: The $BH_3$ molecule

- All the atoms lie in a plane (a planar structure), and the angles between the H atoms are $120^\circ$. The boron atom has electron configuration $1s^22s^22p$. Three atomic orbitals ($2s$, $2p_z$, $2p_x$) participate in forming three hybrid orbitals:

$${\psi^1_{sp^2} = \frac{1}{\sqrt{3}}2s + \sqrt{\frac{2}{3}}2p_z}$$

$${\psi^2_{sp^2} = \frac{1}{\sqrt{3}}2s - \frac{1}{\sqrt{6}}2p_z 
+ \frac{1}{\sqrt{2}}2p_x}$$

$${\psi^3_{sp^2} = \frac{1}{\sqrt{3}}2s - \frac{1}{\sqrt{6}}2p_z 
- \frac{1}{\sqrt{2}}2p_x}$$

The three orbitals can have the following spatial orientations:

:::{figure} images/BeH3.png
:alt: sp2 hybrid orbitals of BH3
:width: 500px

Fig. 5 The three $sp^2$ hybrid orbitals of $BH_3$ point to the corners of an equilateral triangle.
:::

- Each of these hybrid orbitals forms a $\sigma$ bond with an H atom. This is called $sp^2$ hybridization, because two $p$ orbitals and one $s$ orbital participate in the hybrid.

### Example 3: The $CH_4$ molecule

- The electron configuration of the carbon atom is $1s^22s^22p^2$. The four outer valence electrons should be placed in four $sp^3$ hybrid orbitals:

$${\psi^1_{sp^3} = \frac{1}{2}(2s + 2p_x + 2p_y + 2p_z)}$$

$${\psi^2_{sp^3} = \frac{1}{2}(2s - 2p_x - 2p_y + 2p_z)}$$

$${\psi^3_{sp^3} = \frac{1}{2}(2s + 2p_x - 2p_y - 2p_z)}$$

$${\psi^4_{sp^3} = \frac{1}{2}(2s - 2p_x + 2p_y - 2p_z)}$$

These four hybrid orbitals form $\sigma$ bonds with the four hydrogen atoms.

:::{figure} images/CH4.png
:alt: sp3 hybrid orbitals of methane
:width: 500px

Fig. 6 The four $sp^3$ hybrids of $CH_4$ point to the corners of a tetrahedron.
:::

The $sp^3$ hybridization is directly responsible for the tetrahedral geometry of the $CH_4$ molecule. Note that for other elements with $d$-orbitals, one can also obtain bipyramidal (coordination 5) and octahedral (coordination 6) structures.

### Example 4: The $H_2O$ molecule

- The oxygen is $sp^3$ hybridized, with O atom electron configuration $1s^22s^22p^4$. Two of the four hybrid orbitals are doubly occupied with electrons from the oxygen atom, and the remaining two hybrid orbitals participate in $\sigma$ bonding with the two H atoms. This predicts the bond angle H-O-H to be $109^\circ$ (experimental value $104^\circ$). Thus $H_2O$ has two lone pairs of electrons.

:::{figure} images/watMO1.png
:alt: Water hybrid orbitals
:width: 500px

Fig. 7 The $sp^3$ hybrid framework of the water molecule.
:::

:::{figure} images/watMO2.png
:alt: Water bonding orbitals
:width: 500px

Fig. 8 Bonding and lone-pair orbitals of water.
:::

:::{figure} images/watMO3.png
:alt: Water molecular orbitals
:width: 500px

Fig. 9 The occupied molecular orbitals of water.
:::

:::{figure} images/watMO-diag.png
:alt: Water molecular orbital diagram
:width: 500px

Fig. 10 Molecular orbital diagram for the water molecule.
:::

### Other molecules

<iframe src="https://al2me6.github.io/evanescence/"
        width="800"
        height="500"
        allowfullscreen>
</iframe>

### Numerical calculations

In numerical quantum chemical calculations, basis sets that resemble linear combinations of atomic orbitals are typically used (LCAO-MO-SCF). The atomic orbitals are approximated by a group of Gaussian functions, which allow analytic evaluation of the integrals appearing, for example, in the Hartree-Fock (SCF; HF) method. Note that hydrogenlike atomic orbitals differ from Gaussian functions by the power of $r$ in the exponent. A useful rule for Gaussians: the product of two Gaussian functions is another Gaussian function.
