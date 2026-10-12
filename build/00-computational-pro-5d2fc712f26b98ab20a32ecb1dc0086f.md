# Computational Projects

:::{note} **How projects work**

- Each project is a [Google Colab](https://colab.research.google.com) notebook: a full Python environment that runs in the cloud, with NumPy, SciPy, Matplotlib, and Plotly already installed. Nothing to install on your own machine.
- Click **Open in Colab** to launch the project, then immediately use **File > Save a copy in Drive**. That copy is yours, it saves automatically as you work, and you can close the tab and come back to it any time.
- Work through the guided sections, then complete the **Your turn** tasks at the bottom. The parameter cells are meant to be edited: change a value, rerun the cells below it, and see what moves.
- Cells run in the order you run them, so before you finish, use **Runtime > Restart and run all**. That reruns the whole notebook cleanly from top to bottom and catches anything that only worked because of an out-of-order edit.
- **To submit**: after the restart-and-run-all check, use **File > Download > Download .ipynb** and upload that file to Canvas. It carries your code and your output together.
- To run a project locally instead, download the `.ipynb` and open it in Jupyter, or start from [the course repository](https://github.com/DPotoyan/Chem324/tree/master/projects).
:::

### Project 1: Waves, Normal Modes and Interference

Combine normal modes, model musical beats, and build 2D ripple interference patterns from two spherical wave sources.

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/project-01-waves-challenge.ipynb)

**Covers**: Chapter 2 (waves, superposition, normal modes). **Skills**: numpy arrays, meshgrid, subplots, 2D image plots.

### Project 2: Particle in a Box

Explore energies, wavefunctions, and degeneracies of the 1D and 3D particle in a box, then compute uncertainty products and the classical limit with `sympy` and `numpy`.

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/project-02-particle-in-a-box.ipynb)

**Covers**: Chapter 3 (particle in a box, operators and expectation values). **Skills**: varying parameters and replotting, symbolic integration, degeneracy counting.

### Project 3: Quantum Waves

Compute expectation values and the uncertainty relation for particle in a box states, follow a superposition in time, and meet the Fourier transform route to momentum space.

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/project-03-quantum-waves-challenge.ipynb)

**Covers**: Chapter 3 (wavefunctions, expectation values, time dependence, Fourier transforms). **Skills**: numerical derivatives and integrals, FFT.

### Project 4: Atomic Orbitals

Verify orthonormality of radial functions and spherical harmonics numerically, then build the real p and d orbitals chemists know, plus s-p hybrids, as linear combinations.

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/project-04-atomic-orbitals-challenge.ipynb)

**Covers**: Chapter 5 (hydrogen atom, orbitals). **Skills**: special functions, 3D surface plots, linear combinations of wavefunctions.
