---
kernelspec:
  name: python3
  display_name: Python 3
---

# DEMO: HF calculations on small organic molecules by PySCF

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/appendix-demo-benzene.ipynb)





* This demo uses the following libraries (already installed for the site build; on your own machine, `pip install pyscf py3Dmol plotly`)
  * [PySCF](https://pyscf.org/) (for the quantum chemistry)
  * [py3DMol](https://3dmol.csb.pitt.edu/) for visualizing the molecule
  * [plotly](https://plotly.com/python/) and kaleido for plotting

```{code-cell} python
from pyscf import gto   # Used to define a molecule
from pyscf import scf   # Used to perform HF calculations
from pyscf import mp    # Used to perform Møller–Plesset PT calculations
from pyscf import cc    # Used to perfrom Coupled Cluster calculations
from pyscf import mcscf # Used to perform multireference calculations
```

### Overview of Basis sets used in calculations

#### Minimal & small
- **`sto-3g`** – very small, qualitative (what you already used).
- **`sto-6g`** – still minimal, but better approximation to Slater orbitals; improved E(R) shape.

#### Split-valence Pople sets
- **`3-21g`** – first split-valence; cheap, decent improvement over STOs.
- **`6-31g`** – classic workhorse; much better bond length and well depth for H₂.

### With polarization
- **`6-31g*`** or **`6-31g(d)`** – adds d-functions on heavy atoms (not needed for H₂).
- **`6-31g**`** or **`6-31g(d,p)`** – adds p-functions on H; recommended for H₂ to improve curvature and accuracy.

#### Correlation-consistent (Dunning) sets
- **`cc-pVDZ`** – correlation-consistent double-ζ; very good HF curve.
- **`cc-pVTZ`** – triple-ζ; near basis-set limit for HF on H₂.
- **`aug-cc-pVDZ`** – includes diffuse functions; useful for exploring dissociation tail / anionic behavior.

### Diatomics

```{code-cell} python
import numpy as np
import matplotlib.pyplot as plt
from pyscf import gto, scf, tools

def compute_h2_bond_curve(distances, basis='sto-3g'):
    """
    Computes the total energy of H2 molecule at various bond distances.
    
    Parameters:
    - distances (array-like): List of H-H bond distances to calculate energy.
    - basis (str): Basis set for the calculation.
    
    Returns:
    - energies (list): Total electronic energies for each bond distance.
    - mo_energies_list (list of lists): Molecular orbital energies for each distance.
    - mo_coeffs_list (list of arrays): Molecular orbital coefficients for each distance.
    """
    energies = []
    mo_energies_list = []
    mo_coeffs_list = []

    for r in distances:
        mol = gto.Mole()
        mol.atom = f'H 0 0 0; H 0 0 {r}'
        mol.basis = basis
        mol.spin = 0  # Singlet state
        mol.build()
        
        # Perform Hartree-Fock calculation
        mf = scf.RHF(mol)
        total_energy = mf.kernel()
        
        # Store results
        energies.append(total_energy)
        mo_energies_list.append(mf.mo_energy)
        mo_coeffs_list.append(mf.mo_coeff)
        
        print(f"Bond distance: {r:.2f} Å, Total Energy: {total_energy:.6f} Hartree")
    
    return energies, mo_energies_list, mo_coeffs_list

def plot_bond_curve(distances, energies):
    """
    Plots the bond energy curve of H2 molecule.
    
    Parameters:
    - distances (array-like): H-H bond distances.
    - energies (list): Total electronic energies for each bond distance.
    """
    plt.figure(figsize=(8, 5))
    plt.plot(distances, energies, marker='o', label='Total Energy (HF)')
    plt.xlabel('H-H Bond Distance (Å)')
    plt.ylabel('Total Energy (Hartree)')
    plt.title('Bond Curve for H2 (HF/STO-3G)')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_molecular_orbitals(distances, mo_energies_list):
    """
    Plots the molecular orbital energies as a function of bond distance.
    
    Parameters:
    - distances (array-like): H-H bond distances.
    - mo_energies_list (list of lists): Molecular orbital energies for each distance.
    """
    plt.figure(figsize=(8, 5))
    for i in range(len(mo_energies_list[0])):  # Number of orbitals
        orbital_energies = [mo_energies[i] for mo_energies in mo_energies_list]
        plt.plot(distances, orbital_energies, marker='o', label=f'MO {i+1}')
    
    plt.xlabel('H-H Bond Distance (Å)')
    plt.ylabel('Molecular Orbital Energy (Hartree)')
    plt.title('Molecular Orbital Energies for H2 (HF/STO-3G)')
    plt.grid(True)
    plt.legend()
    plt.show()
```

```{code-cell} python
# Define bond distances (in Ångstroms)
distances = np.linspace(0.5, 3.0, 20)  # From 0.5 to 3.0 Å

# Run the bond curve calculation
energies, mo_energies_list, mo_coeffs_list = compute_h2_bond_curve(distances)

# Plot the bond curve
plot_bond_curve(distances, energies)

# Plot the molecular orbital energies as a function of bond distance
plot_molecular_orbitals(distances, mo_energies_list)
```

```{code-cell} python
import numpy as np
from pyscf import gto, scf, tools
import py3Dmol  # For 3D visualization of orbitals

def visualize_h2_mo_cubes(bond_distance=0.74, basis='sto-3g', mo_index=0, output_cube_file='mo.cube'):
    """
    Generate and visualize cube files for molecular orbitals of H2.
    
    Parameters:
    - bond_distance (float): H-H bond distance (in Ångstroms).
    - basis (str): Basis set for the calculation (e.g., 'sto-3g', '6-31g').
    - mo_index (int): Index of the molecular orbital to visualize (0-indexed).
    - output_cube_file (str): The name of the cube file to save.
    """
    # 1. Build the H2 molecule
    mol = gto.Mole()
    mol.atom = f'H 0 0 0; H 0 0 {bond_distance}'
    mol.basis = basis
    mol.spin = 0  # Singlet state
    mol.build()

    # 2. Perform Hartree-Fock calculation
    mf = scf.RHF(mol)
    mf.kernel()

    # 3. Generate cube file for the specified molecular orbital (MO)
    print(f"Generating cube file for MO {mo_index + 1} (0-indexed as {mo_index})")
    tools.cubegen.orbital(mol, output_cube_file, mf.mo_coeff[:, mo_index], nx=80, ny=80, nz=80)

    # 4. Visualize the molecular orbital using py3Dmol
    print(f"Visualizing cube file: {output_cube_file}")
    cube_view = py3Dmol.view(width=400, height=400)
    with open(output_cube_file, 'r') as cube_file:
        cube_data = cube_file.read()
        
    # Add isosurfaces for positive and negative parts of the orbital
    cube_view.addVolumetricData(cube_data, "cube", {'isoval': -0.03, 'color': "red", 'opacity': 0.85})
    cube_view.addVolumetricData(cube_data, "cube", {'isoval': 0.03, 'color': "blue", 'opacity': 0.85})
    
    # Add the molecular structure as well
    cube_view.addModel(mol.tostring(format="xyz"), 'xyz')
    cube_view.setStyle({'stick': {}, 'sphere': {'radius': 0.4}})
    cube_view.setBackgroundColor('0xeeeeee')
    cube_view.show()
```

```{code-cell} python
# Set the bond distance, basis, and the index of the molecular orbital to visualize
visualize_h2_mo_cubes(bond_distance=0.74, basis='sto-3g', mo_index=1, output_cube_file='mo_1.cube')  # MO 1
```

### Build and Visualize Benzene

```{code-cell} python
mol_xyz = """H      1.2194     -0.1652      2.1600
  C      0.6825     -0.0924      1.2087
  C     -0.7075     -0.0352      1.1973
  H     -1.2644     -0.0630      2.1393
  C     -1.3898      0.0572     -0.0114
  H     -2.4836      0.1021     -0.0204
  C     -0.6824      0.0925     -1.2088
  H     -1.2194      0.1652     -2.1599
  C      0.7075      0.0352     -1.1973
  H      1.2641      0.0628     -2.1395
  C      1.3899     -0.0572      0.0114
  H      2.4836     -0.1022      0.0205"""

mol = gto.M(atom=mol_xyz, basis="sto3g", verbose=3)
```

```{code-cell} python
import py3Dmol

xyz_view = py3Dmol.view(width=400,height=400)
xyz_view.addModel(mol.tostring(format="xyz"),'xyz')
xyz_view.setStyle({'stick':{}, "sphere":{"radius":0.4}})
xyz_view.setBackgroundColor('0xeeeeee')
xyz_view.show()

#
# Use your mouse to interact with the molecule!
#
```

### Run calculations

```{code-cell} python
# Run HF and save the results
mf = scf.RHF(mol).run()

# In Jupyter notebooks you can hover over methods to see docstrings or you can print the docstrings out!
#print(mf.__doc__)
```

### Visualize Results

```{code-cell} python
import plotly.express as px

# Plot the MO Occupations
fig = px.line(y=mf.mo_occ, markers=True, title="Molecular Orbital (MO) Occupations")
fig.update_layout(xaxis_title="Orbital Index (0-Based)", yaxis_title="MO Occupation")
fig.show()
```

```{code-cell} python
# Plot the MO Energies (i.e. eigenvalues of the Fock matrix)
fig = px.line(y=mf.mo_energy, markers=True, title="Molecular Orbital (MO) Energies")
fig.update_layout(xaxis_title="Orbital Index (0-Based)", yaxis_title="MO Energies")
fig.show()
```

```{code-cell} python
from pyscf.tools import cubegen

cubegen.orbital(mol, 'mo.cube', mf.mo_coeff[:,18]); # 42 electrons so 21 occupied orbitals

cube_view = py3Dmol.view(width=400,height=400)
cube_view.addVolumetricData(open("mo.cube").read(), "cube", {'isoval': -0.03, 'color': "red", 'opacity': 0.85})
cube_view.addVolumetricData(open("mo.cube").read(), "cube", {'isoval': 0.03, 'color': "blue", 'opacity': 0.85})
cube_view.addModel(mol.tostring(format="xyz"),'xyz')
cube_view.setStyle({'stick':{}, "sphere":{"radius":0.4}})
cube_view.setBackgroundColor('0xeeeeee')
cube_view.show()

#
# Use your mouse to interact with the molecule!
#
```

| Region   | Orbital indices | Type               | Comment                   |
| -------- | --------------- | ------------------ | ------------------------- |
| Very low | 0–5             | C 1s core          | Flat band, strongly bound |
| Middle   | 6–20            | σ bonding          | σ-framework in the ring   |
| Gap      | ~21             | Highest occupied π | Aromatic HOMO             |
| High     | 22–35           | π*/σ*              | Virtual MOs               |

### Short Survey of more acurate methods

```{code-cell} python
from pyscf import gto, scf, dft, mp, cc, fci
import py3Dmol
import plotly.express as px
```

```{code-cell} python
# Experimental geometry of gas-phase water
# Ref: https://cccbdb.nist.gov/expgeom2x.asp
mol_xyz = """O        0.0000   0.0000   0.1173
             H        0.0000   0.7572	 -0.4692
             H        0.0000  -0.7572	 -0.4692"""
mol = gto.M(
    atom=mol_xyz, 
    basis="6-31g", 
    verbose=4,
    charge=0,      # 0 by default
    spin=0,        # 0 by default, defined as (n_up - n_down)
    symmetry=True, # False by default
)
```

```{code-cell} python
xyz_view = py3Dmol.view(width=400,height=400)
xyz_view.addModel(mol.tostring(format="xyz"),'xyz')
xyz_view.setStyle({'stick':{}, "sphere":{"radius":0.4}})
xyz_view.setBackgroundColor('0xeeeeee')
xyz_view.show()
```

#### [Hartree-Fock](https://en.wikipedia.org/wiki/Hartree%E2%80%93Fock_method)

* Hatree-Fock (HF) is the starting point of the most of quantum chemistry
* We variationally optimize the orbitals for a single [Slater determinint](https://en.wikipedia.org/wiki/Slater_determinant)
* Working in the basis of atom-centered basis function we solve the [Roothaan-Hall](https://en.wikipedia.org/wiki/Roothaan_equations) equations

<!-- $\textbf{FC} = \textbf{SC} \epsilon$

* $\textbf{F}$ is the Fock matrix
* $\textbf{C}$ is the molecular orbital coefficient matrix
* $\textbf{S}$ is the atomic orbital overlap matrix
* $\epsilon$ is the vector of molecular orbital energies -->

See the PySCF [user guide](https://pyscf.org/user/scf.html) and [examples](https://github.com/pyscf/pyscf/tree/master/examples/scf) for more info.

```{code-cell} python
mymf = scf.RHF(mol).run()
```

#### [Density Functional Theory](https://en.wikipedia.org/wiki/Density_functional_theory)

* In Density Functional Theory (DFT), the electron density of a reference noninteracting system is used to represent the density of the true interacting system.
* The formulation resembles HF with a different effective Fock potential.
* This effective potential depends on the density functional approximation which is chosen by the user.
* PySCF gives users the access to a large number of functionals through the [libxc](https://tddft.org/programs/libxc/) and [xcfun](https://github.com/dftlibs/xcfun) libraries.

See the PySCF [user guide](https://pyscf.org/user/dft.html) and [examples](https://github.com/pyscf/pyscf/tree/master/examples/dft) for more info.

#### [Møller–Plesset perturbation theory](https://en.wikipedia.org/wiki/M%C3%B8ller%E2%80%93Plesset_perturbation_theory)

* Perturbative corrections to the Hartree-Fock approximation.

See the PySCF [user guide](https://pyscf.org/user/mp.html) and [examples](https://github.com/pyscf/pyscf/tree/master/examples/mp) for more info.

```{code-cell} python
mymp2 = mp.MP2(mymf).run()
```

#### [Coupled Cluster](https://en.wikipedia.org/wiki/Coupled_cluster)

* Perturbative method that improves on the Hartree-Fock approximation.
* Coupled Cluster Singles and Doubles (CCSD) includes single and double excitation on top of the HF wave function.
* Accuracy can be improved by including triples perturbatively (CCSD(T)).
* Non-variational, but size extensive description of ground states. For excited states, see EOM-CCSD.

See the PySCF [user guide](https://pyscf.org/user/cc.html) and [examples](https://github.com/pyscf/pyscf/tree/master/examples/cc) for more info.

```{code-cell} python
mycc = cc.CCSD(mymf).run()
```

```{code-cell} python
e_ccsd_t = mycc.ccsd_t()
```

#### [Full Configuration Interaction](https://en.wikipedia.org/wiki/Full_configuration_interaction)

* Full configuration interaction (FCI) is exact for a given choice of basis set.
* Cost grows exponentially with the size of the system.
* Also known as exact diagonalization.

See the [PySCF examples](https://github.com/pyscf/pyscf/tree/master/examples/fci) for more details.

```{code-cell} python
myfci = fci.FCI(mymf)
myfci.kernel();
```

### Analysis

Important data is saved to the PySCF method objects, making it easy to analyze and visualize!

```{code-cell} python
# Collect data
methods = ["HF", "MP2", "CCSD", "CCSD(T)", "FCI"]
energies = [mymf.e_tot, mymp2.e_tot, mycc.e_tot, mycc.e_tot + e_ccsd_t, myfci.e_tot]

# Plotting
fig = px.line(x=methods, y=energies, title="Comparison of QC methods", markers=True)
fig.update_layout(xaxis_title="Method", yaxis_title="Energy (Ha)")
fig.update_traces(marker_size=12)
fig.show() # It's interactive!
```
