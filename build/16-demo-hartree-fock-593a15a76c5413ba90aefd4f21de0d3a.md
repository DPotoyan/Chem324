---
kernelspec:
  name: python3
  display_name: Python 3
---

# Demo: Hartree-Fock with PySCF

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/appendix-demo-hartree-fock.ipynb)



This notebook runs an actual Hartree-Fock (self-consistent field) calculation on atoms using the [PySCF](https://pyscf.org/) quantum chemistry package, and visualizes the resulting orbitals. It complements the Hartree-Fock lecture page, where the theory (Slater determinant, Fock operator, SCF cycle) is developed.

This demo uses the following libraries (already installed for the site build; on your own machine, `pip install pyscf py3Dmol plotly`):

* [PySCF](https://pyscf.org/) for the quantum chemistry
* [py3DMol](https://3dmol.csb.pitt.edu/) for visualizing the molecule
* [plotly](https://plotly.com/python/) and kaleido for plotting

## Hartree-Fock energies and orbitals of alkali-metal atoms

The function below builds an atom in a minimal STO-3G basis, runs a restricted open-shell Hartree-Fock calculation, extracts the molecular-orbital energies, and writes a cube file for the highest occupied molecular orbital (HOMO) so it can be visualized with py3Dmol.

```{code-cell} python
import py3Dmol
from pyscf import gto, scf
from pyscf.tools import cubegen

# Function to calculate orbitals and energies for a given atom
def calculate_orbitals_energies(atom_symbol):
    """
    Calculate the orbitals and energies for a given atom using PySCF.

    Parameters:
    atom_symbol (str): Symbol of the atom (e.g., 'He', 'Li').

    Returns:
    dict: A dictionary containing the total energy, MO coefficients, and MO energies.
    """
    # Define the atom and basis set
    mol = gto.Mole()
    mol.atom = [(atom_symbol, (0, 0, 0))]  # Specify the atom and its position
    mol.basis = 'sto-3g'  # Basis set

    mol.spin = 1  # 2S = 1, since Li, Na, K has 1 unpaired electron

    mol.build()

    # Perform Hartree-Fock calculation
    mf = scf.RHF(mol)  # Restricted Hartree-Fock
    total_energy = mf.kernel()  # Calculate the total electronic energy

    # Extract molecular orbital coefficients and energies
    mo_coefficients = mf.mo_coeff  # MO coefficients
    mo_energies = mf.mo_energy  # MO energies

    # Determine the HOMO (highest occupied molecular orbital) energy
    num_electrons = mol.nelectron  # Total number of electrons in the system
    homo_index = num_electrons // 2 - 1  # HOMO index for closed-shell systems (0-indexed)
    homo_energy = mo_energies[homo_index] if homo_index >= 0 else None

    # Generate the cube file for the HOMO
    if homo_index >= 0:
        cube_filename = f"{atom_symbol}_HOMO.cube"
        cubegen.orbital(mol, cube_filename, mf.mo_coeff[:, homo_index])
        print(f"HOMO cube file saved as: {cube_filename}")

        # Visualize the cube file using py3Dmol
        cube_view = py3Dmol.view(width=400, height=400)
        with open(cube_filename, 'r') as file:
            cube_data = file.read()
        cube_view.addVolumetricData(cube_data, "cube", {'isoval': -0.03, 'color': "red", 'opacity': 0.85})
        cube_view.addVolumetricData(cube_data, "cube", {'isoval': 0.03, 'color': "blue", 'opacity': 0.85})
        cube_view.addModel(mol.tostring(format="xyz"), 'xyz')
        cube_view.setStyle({'stick': {}, "sphere": {"radius": 0.4}})
        cube_view.setBackgroundColor('0xeeeeee')
        cube_view.show()

    results = {
        'atom': atom_symbol,
        'total_energy': total_energy,
        'mo_coefficients': mo_coefficients,
        'mo_energies': mo_energies,
        'homo_energy': homo_energy
    }

    return results
```

Now loop over a couple of alkali-metal atoms, run the calculation, and print the total Hartree-Fock energy, the orbital energies, and the HOMO energy for each.

```{code-cell} python
# List of atoms to calculate
atoms = ['Li', 'Na']

# Store the results for each atom
results_dict = {}

# Loop over each atom and calculate orbitals and energies
for atom in atoms:
    results = calculate_orbitals_energies(atom)
    results_dict[atom] = results

    print(f"Results for {atom} atom:")
    print("Total Energy (Hartree):", results['total_energy'])
    print("Molecular Orbital Energies (Hartree):", results['mo_energies'])
    print("HOMO energy (Hartree):", results['homo_energy'])
    print("\n")
```
