# Computational Projects

:::{note} **How projects work**

- Each project is an interactive [marimo](https://marimo.io) notebook that runs in the cloud. Click **Open in molab**: you will first see a read-only preview of the notebook.
- Press the **fork** button to get your own editable, running copy. No installation is needed. **Sign in to molab first** (free) so your copy is saved and you can return to it later; an unsaved fork lives only in the current browser tab.
- Work through the guided sections, then complete the **Your turn** tasks at the bottom of the notebook. Cells rerun automatically when anything they depend on changes, so experiment freely.
- **To submit**: in molab use File, then Download, to save the completed notebook as a `.py` file and upload it to Canvas. Download your work at the end of every session even if you signed in; it is your safety copy.
- If molab is unavailable, the backup link runs the same notebook entirely in your browser, or run it locally with `uv run marimo edit <file>` after downloading it from [the course repository](https://github.com/DPotoyan/Chem324/tree/master/projects).
:::

### Project 1: Particle in a Box

Explore energies, wavefunctions, and degeneracies of the 1D and 3D particle in a box, then compute uncertainty products and the classical limit with `sympy` and `numpy`.

[![Open in molab](images/molab-shield.svg)](https://molab.marimo.io/github/DPotoyan/Chem324/blob/master/projects/01-particle-in-a-box.py)

Backup: [run in your browser (marimo.app)](https://marimo.app/github.com/DPotoyan/Chem324/blob/master/projects/01-particle-in-a-box.py)

**Covers**: Chapter 3 (particle in a box, operators and expectation values). **Skills**: sliders and reactive plots, symbolic integration, degeneracy counting.

### Project 2: Waves, Normal Modes and Interference

Combine normal modes, model musical beats, and build 2D ripple interference patterns from two spherical wave sources.

[![Open in molab](images/molab-shield.svg)](https://molab.marimo.io/github/DPotoyan/Chem324/blob/master/projects/02-waves-challenge.py)

Backup: [run in your browser (marimo.app)](https://marimo.app/github.com/DPotoyan/Chem324/blob/master/projects/02-waves-challenge.py)

**Covers**: Chapter 2 (waves, superposition, normal modes). **Skills**: numpy arrays, meshgrid, subplots, 2D image plots.

### Project 3: Quantum Waves

Compute expectation values and the uncertainty relation for particle in a box states, follow a superposition in time, and meet the Fourier transform route to momentum space.

[![Open in molab](images/molab-shield.svg)](https://molab.marimo.io/github/DPotoyan/Chem324/blob/master/projects/03-quantum-waves-challenge.py)

Backup: [run in your browser (marimo.app)](https://marimo.app/github.com/DPotoyan/Chem324/blob/master/projects/03-quantum-waves-challenge.py)

**Covers**: Chapter 3 (wavefunctions, expectation values, time dependence, Fourier transforms). **Skills**: numerical derivatives and integrals, FFT.

### Project 4: Atomic Orbitals

Verify orthonormality of radial functions and spherical harmonics numerically, then build the real p and d orbitals chemists know, plus s-p hybrids, as linear combinations.

[![Open in molab](images/molab-shield.svg)](https://molab.marimo.io/github/DPotoyan/Chem324/blob/master/projects/04-atomic-orbitals-challenge.py)

Backup: [run in your browser (marimo.app)](https://marimo.app/github.com/DPotoyan/Chem324/blob/master/projects/04-atomic-orbitals-challenge.py)

**Covers**: Chapter 5 (hydrogen atom, orbitals). **Skills**: special functions, 3D surface plots, linear combinations of wavefunctions.
