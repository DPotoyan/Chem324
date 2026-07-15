---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Hartree-Fock Method

:::{note} **What you will learn**

- The Schrodinger equation for multi-electron systems cannot be solved exactly because of the electron, electron interaction.
- The **Hartree-Fock** method provides an approximate approach by treating each electron as moving in the **average (mean-field) potential** created by all the others.
- Antisymmetry of the total wavefunction is enforced using a **Slater determinant**, which introduces the **exchange interaction**, a purely quantum effect with no classical analogue.
- The solution is obtained **self-consistently**: the orbitals define the mean field, and the mean field determines the orbitals. This is the **SCF** procedure.
- Hartree-Fock captures exchange exactly but misses **dynamic correlation**, motivating post-Hartree-Fock methods.
:::

## The Wavefunction

The total wavefunction $\Psi(1, 2, \ldots, N)$ is approximated as a single Slater determinant so that it satisfies the Pauli exclusion principle automatically:

:::{important} **Slater determinant ansatz**

$$
\Psi(1, 2, \ldots, N) = \frac{1}{\sqrt{N!}}
\begin{vmatrix}
\psi_1(1) & \psi_2(1) & \cdots & \psi_N(1) \\
\psi_1(2) & \psi_2(2) & \cdots & \psi_N(2) \\
\vdots & \vdots & \ddots & \vdots \\
\psi_1(N) & \psi_2(N) & \cdots & \psi_N(N)
\end{vmatrix}
$$

:::

## The Hartree-Fock Equations

Each molecular orbital (MO) $\psi_i$ satisfies the self-consistent field (SCF) equation:

:::{important} **Hartree-Fock equation**

$$
\hat{F} \psi_i = \varepsilon_i \psi_i
$$

where $\hat{F}$ is the **Fock operator** and $\varepsilon_i$ are the orbital energies.
:::

### The Fock Operator

The Fock operator $\hat{F}$ is the sum of the one-electron Hamiltonian and a mean-field potential:

$$
\hat{F} = \hat{h} + \sum_{j} \left( \hat{J}_j - \hat{K}_j \right)
$$

- $\hat{h}$ contains the kinetic energy and nuclear attraction operators.
- $\hat{J}_j$ is the Coulomb operator (electron, electron repulsion).
- $\hat{K}_j$ is the exchange operator, which arises from the antisymmetry requirement of the wavefunction and has no classical analogue.

## The Self-Consistent Field (SCF) Procedure

The Fock operator depends on the orbitals it is meant to determine, so the equations must be solved iteratively:

1. **Guess** an initial set of molecular orbitals $\psi_i$.
2. **Construct** the Fock operator $\hat{F}$ using the current $\psi_i$.
3. **Solve** the Hartree-Fock equation $\hat{F}\psi_i = \varepsilon_i\psi_i$ to obtain new orbitals $\psi_i$.
4. **Repeat** steps 2 and 3 until convergence, that is, until the orbitals no longer change significantly.

:::{figure} images/HF_iter.png
:alt: SCF iteration loop
:width: 500px

Fig. 1 The self-consistent field cycle. The orbitals define the mean field through the Fock operator, and solving the Fock equation produces updated orbitals; the loop repeats until self-consistency.
:::

## Total Energy of the System

The total electronic energy $E_{HF}$ in the Hartree-Fock approximation is:

:::{important} **Hartree-Fock energy**

$$
E_{HF} = \sum_{i} \langle \psi_i | \hat{h} | \psi_i \rangle + \frac{1}{2} \sum_{i,j} \left( J_{ij} - K_{ij} \right)
$$

- $J_{ij}$ is the Coulomb integral.
- $K_{ij}$ is the exchange integral.
- The factor $\tfrac{1}{2}$ corrects for double counting of the electron, electron interaction.
:::

## Hartree-Fock for the Helium Atom

Helium is the simplest closed-shell atom on which to see the method work. Each $1s$ electron moves in an effective potential, the bare nuclear attraction plus the mean field of the other electron.

:::{figure} images/HF_He.png
:alt: Hartree-Fock applied to helium
:width: 500px

Fig. 2 Hartree-Fock applied to the helium atom: each electron is treated as moving in the average field of the other.
:::

:::{figure} images/V_eff.png
:alt: Effective potential seen by an electron
:width: 500px

Fig. 3 The effective (mean-field) potential felt by one electron is the nuclear attraction screened by the averaged charge cloud of the other electron.
:::

:::{figure} images/HF_slater.png
:alt: Slater determinant for helium
:width: 500px

Fig. 4 The antisymmetrized helium wavefunction written as a Slater determinant of spin-orbitals.
:::

:::{figure} images/HF_orb_e.png
:alt: Hartree-Fock orbital energies
:width: 500px

Fig. 5 Orbital energies obtained from the converged Hartree-Fock calculation.
:::

## Strengths and Limitations

**Strengths**

- **Efficient.** It reduces the intractable multi-electron Schrodinger equation to a set of coupled one-electron equations.
- **Exchange interactions.** It includes the effects of exchange exactly through the Slater determinant.

**Limitations**

- **No dynamic correlation.** Electron, electron correlation is only partially captured, because each electron sees only the *average* field of the others, not their instantaneous positions.
- **Post-Hartree-Fock methods.** More accurate energies require methods such as MP2 or CCSD that add correlation on top of the Hartree-Fock reference.

:::{tip} **Hartree-Fock in one sentence**

Hartree-Fock replaces the impossible many-body problem with a self-consistent set of one-electron problems in which each electron moves in the averaged field of all the others, capturing exchange exactly but correlation only on average. The companion demo notebook runs an actual Hartree-Fock calculation with PySCF.
:::
