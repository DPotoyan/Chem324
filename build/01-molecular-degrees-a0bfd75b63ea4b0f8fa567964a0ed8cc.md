

# Molecular Degrees of Freedom

:::{note} **What you need to know**

Having found that the energy of bound systems is quantized, our next goal is to investigate the different manifestations of this quantization and the ways of probing it in experiments via spectroscopy. Using simple, exactly solvable toy systems, we will study the specifics of quantization of the different **degrees of freedom (DOF)** found in molecules. The degrees of freedom of a molecule fall into **translational, rotational, vibrational and electronic motion.**

- **Particle in a box.** (quantization of translational DOF)
- **Harmonic oscillator** (quantization of vibrational DOF)
- **Rigid rotor.**  (quantization of rotational DOF)
:::

###  Energies of molecules

Molecules consisting of N nuclei and n electrons are described by wave functions that depend on 3(n+N) variables in 3D space. These coordinates, or degrees of freedom (DOF), are usefully broken down into different kinds of motion classified as translational, rotational, vibrational and electronic. Because molecules are microscopic objects, we expect all of these energies to be quantized. The relative spacings, however, differ significantly because of the boundary conditions that restrict the motions of these DOFs. This is why different kinds of spectroscopy exist for probing the specific degrees of freedom in molecules.

$$E= \epsilon_{trans}+ \epsilon_{rot}+ \epsilon_{vib}+\epsilon_{elec}$$


:::{figure} ./images/Levels1.gif
:label: fig-molecular-degrees-of-freedom-1
:alt: mol deg freed
:width: 500px

Energy levels associated with the different degrees of freedom in molecules.
:::




### 3N Nuclear degrees of freedom 

- The *Born-Oppenheimer approximation* allows us to separate the nuclear and electronic degrees of freedom. The nuclear Hamiltonian for $N$ nuclei can now be written in such a way that the electronic part appears as a potential term:

$${\hat{H} = \sum\limits_{i=1}^{N} -\frac{\hbar^2}{2m_i}\nabla_{R_i}^2 + E(R_1, R_2, ..., R_N)}$$


:::{figure} ./images/mol-DOF.jpg
:label: fig-molecular-degrees-of-freedom-2
:alt: mol deg freed
:width: 500px

The different degrees of freedom in molecules: translational, rotational and vibrational motion.
:::


- In the absence of external electric or magnetic fields, the potential term $E$ depends only on the relative positions of the nuclei, as shown above, and not on the overall position of the molecule or its orientation in space. The above Hamiltonian $H$ can often be approximately written as a sum of the following terms:

$${\hat{H} = \hat{H}_{tr} + \hat{H}_{rot} + \hat{H}_{vib}}$$

where $H_{tr}$ is the translational, $H_{rot}$ the rotational, and $H_{vib}$ the vibrational Hamiltonian. The translational and rotational terms have no potential part, but the vibrational part contains the potential $E$, which depends on the distances between the nuclei.

> In some cases the different degrees of freedom become coupled and one cannot use the following separation technique. Separation of $H$ means that we can write the wavefunction as a product:

$${\psi = \psi_{tr}\psi_{rot}\psi_{vib}}$$

### Separation of degrees of freedom

The resulting three Schrödinger equations are then:

$${\hat{H}_{tr}\psi_{tr} = E_{tr}\psi_{tr}}$$

$${\hat{H}_{rot}\psi_{rot} = E_{rot}\psi_{rot}}$$

$${\hat{H}_{vib}\psi_{vib} = E_{vib}\psi_{vib}}$$

- The translational part is not interesting, since there is no external potential or boundary condition that could lead to quantization (i.e., it produces a continuous spectrum).
  
- On the other hand, the rotational part is subject to a cyclic boundary condition and the vibrational part to the potential $E$, so we expect these to produce quantization, which can be probed by spectroscopic methods.

- The original number of variables in the Hamiltonian is $3\times N$ (i.e. the $x,y,z$ coordinates for each nucleus). We can neglect the translational motion, and we are left with $3N - 3$ coordinates.
  
- To account for molecular rotation, three variables are required, or only two variables for a linear molecule. Therefore the vibrational part must have either $3N - 6$ variables for a non-linear molecule or $3N - 5$ variables for a linear molecule. These are referred to as *vibrational degrees of freedom* or *internal coordinates*.


