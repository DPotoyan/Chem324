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


