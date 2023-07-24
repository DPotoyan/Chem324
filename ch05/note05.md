## Spin

- Experiment of Stern and Herlach provdies estblaishes the existance of spin for electrons. Contrary to the suggestive name, the spin is an intrinsic magnetic momentum which is permanently attached to a subatomic particle and has nothing to do with "spinning" or motion. Spins is an intrinsic property just like mass and charge. 
- Particles with half-integer spins, such as 1/2, 3/2, 5/2, are known as fermions, while those particles with integer spins, such as 0, 1, 2, are known as bosons . The two families of particles obey different rules. Fermions obey the Pauli exclusion principle:  there cannot be two identical fermions simultaneously having the same quantum numbers, e.g, having the same position, velocity and spin direction. In contrast, bosons  have no such restriction, so they may "bunch together" even if in identical states.

- *Normal Zeeman effect*: splitting of singlet states with spin zero in the magnetic field is due to electron's angular momentum can be understood classically. 
- *Anomalous Zeeman effect*: Is a more general case of electron spin and angular mometnum both contributing to splitting of energy levels.



### Rotating charge generates mangetic moment

Charged electron moving on a circle of radius has an angular momentum $\vec{L}=\vec{r} \times \vec{p}$ which generates a magnetic moment given by:
$$
\mu_L = -\frac{e}{2m_e}\vec{L}
$$

![](./images/magnetic.jpg)

In an external magnetic field magnetic moment interacts with the field with a potential energy given as a scalar product of two vectors: 
$$
U = -\vec{\mu_L}\cdot\vec{B} = \frac{e}{2m_e}\vec{L}\cdot \vec{B}
$$


### Effect of magnetic field on atoms

The expressionof energy of mangeitc moment in the extenal magnetic field  $U = -\vec{\mu_L}\cdot\vec{B}$ implies that the magnetic field has an ordering effect which ias acheived via an exertion of a force:

$$
F_z=-\frac{\partial U}{\partial z}
$$


![](./images/spin3.gif)



### Mangetic field modifies the hamiltonian

In a constant magnetic field the hydrogen atom's Hamiltonian willl be supplemetned with a new term    accounting for the interaction of electron's magnetic moment with the magnetic field  (e.g needs to not be in an s orbital with l=0). Picking the mangetic field along direction z  we can write the hamiltonain as: 



$$
\hat{H} = \hat{H}_0 + \hat{H}_{mag}+ \frac{e}{2m_e} B \hat{L}_z
$$



Since $[\hat{L}_z, \hat{H}_0]=0$ we have 

- $\hat{L}_z\mid n,l, m_l\rangle = \hbar m_l \mid n,l, m_l\rangle$ 
- $\hat{H}_0\mid n,l, m_l\rangle =E_n\mid n,l, m_l\rangle$




$$
E=E_n +\hbar m \frac{e}{2m_e} B=E_n+m\beta_B B
$$


Where we have introduce the Boh'r magneton $\beta_B = \frac{\hbar e}{2 m_e}$. The energy expression predicts removal of degeneracy with respect to $m_l$ generating splitting energy levels into $2l+1$ lines. For instance the 2p level of hydrogen atom will split into 3 levels $-\beta_B B, 0,+\beta_B$






### The  Zeeman effect 

When an external magnetic field is applied, sharp spectral lines like the $n=3\rightarrow 2$ transition of hydrogen split into multiple closely spaced lines. First observed by Pieter Zeeman, this splitting is attributed to the interaction between the magnetic field and the magnetic dipole moment associated with the orbital angular momentum. In the absence of the magnetic field, the hydrogen energies depend only upon the principal quantum number n , and the emissions occur at a single wavelength.


### Stern-Herlach experiment



<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/jDxUaBYINeQ" frameborder="0" allowfullscreen>
</iframe>
</html>



### Spin as a tiny magnet



We come to view *spin* of subatomic particles in a same way as we view mass and charge. Spin is an intrinsic property of a particle manifested in having permanent magnetic moment. A particle with spin can interact with magnetic fields just like particles with charge can interact with electric fields. This is why spin is pictorially depcited as tiny manget. 




![](./images/Spin1.jpg)



### Spin-Orbit coupling

Having two source of mangeitc fields in atoms one due to orbtial momentum and another due to spin there arises a possibility that these microscopic magnets can interact. And such a possibility is indeed realized and known under name of spin-orbit coupling. 

![](./images/spin-orbit1.png)

![](./images/spin-orbit2.png)





### Term symbols

Becsue of spint orbit coupling the energy levels are no longer diescribed by $l$ and $s$ separetely. This is why one introduces term sybols to describe new states with total spin multiplicity $(2S+1)$ and anuglar momentum $L$ and total angular momentum $J=L+S$. The word total will take more meaning when we discuss multi electorn atoms where angular moenta are summed. 
$$
^{(2S+1)}L_J
$$




### "Anomalous" Zeeman Effect


While the Zeeman effect in some atoms (e.g., hydrogen) showed the expected equally-spaced triplet, in other atoms the magnetic field split the lines into four, six, or even more lines and some triplets showed wider spacings than expected. These deviations were labeled the "anomalous Zeeman effect" and were very puzzling to early researchers. The explanation of these different patterns of splitting gave additional insight into the effects of electron spin. With the inclusion of electron spin in the total angular momentum, the other types of multiplets formed part of a consistent picture. So what has been historically called the "anomalous" Zeeman effect is really the normal Zeeman effect when electron spin is included.

![](./images/Zeeman.png)





### Electron spin

The Schr\"odinger equation does not account for electron spin. The concept of electron spin originates from Dirac's relativistic equation. However, it can be included in the Schr\"odinger equation as an extra quantum number ($s$). Furthermore, it appears to follow the general laws of angular momentum.


The spin angular momentum vector $\vec{S}$ has a magnitude: $|\vec{S}| = S = \sqrt{s(s+1)}\hbar$ where $s$ is the spin quantum number ($\frac{1}{2}$). A crude way of thinking about the origin of the spin angular momentum is to consider the magnetic moment to arise from the internal spinning motion of the electron about its own axis. However, this is not exactly true because electrons have internal structure that we have ignored here.


To summarize the behavior of electron spin angular momentum:

$${S^2 = s(s+1)\hbar^2 = \frac{3}{4}\hbar^2\textnormal{ (since }s = \frac{1}{2}\textnormal{)}}$$

$${S_z = m_s\hbar\textnormal{ with }m_s = \pm\frac{1}{2}\textnormal{ (}+\frac{1}{2} = \textnormal{``spin up''; }-\frac{1}{2}
= \textnormal{``spin down'')}}$$

The corresponding operators are denoted by $\hat{S}_z$ and $\hat{S}^2$. How about the eigenfunctions?


The eigenfunctions are denoted by $\alpha$ and $\beta$ and we don't write down their specific forms. The following relations apply for these eigenfunctions:



$${\hat{S}^2\alpha\equiv \hat{S}^2|\alpha\rangle = \frac{1}{2}\left(\frac{1}{2} + 1\right)\hbar^2\alpha = \frac{3}{4}\hbar^2\alpha\equiv\frac{3}{4}\hbar^2|\alpha\rangle}$$

\aeqn{10.47}{\hat{S}^2\beta\equiv \hat{S}^2|\beta\rangle = \frac{1}{2}\left(\frac{1}{2} + 1\right)\hbar^2\beta = \frac{3}{4}\hbar^2\beta\equiv\frac{3}{4}\hbar^2|\beta\rangle}

$${\hat{S}_z\alpha\equiv \hat{S}_z|\alpha\rangle = +\frac{1}{2}\hbar\alpha\equiv +\frac{1}{2}\hbar |\alpha\rangle}$$

$${\hat{S}_z\beta\equiv \hat{S}_z|\beta\rangle = -\frac{1}{2}\hbar\beta\equiv -\frac{1}{2}\hbar |\beta\rangle}$$

Note that all the following operators commute: $\hat{H}$, $\hat{L}^2$, $\hat{L}_z$, $\hat{S}^2$, and $\hat{S}_z$. This means that they all can be specified simultaneously. The spin eigenfunctions are taken to be orthonormal:

$${\int\alpha^*\alpha d\sigma\equiv\langle\alpha|\alpha\rangle = \int\beta^*\beta d\sigma\equiv\langle\beta|\beta\rangle = 1}$$

$${\int\alpha^*\beta d\sigma\equiv\langle\alpha|\beta\rangle = \int\beta^*\alpha d\sigma\equiv\langle\beta|\alpha\rangle = 0}$$

where the integrations are over variables that the spin eigenfunctions depend on. Note that we have not specified the actual forms these eigenfunctions. We have only stated that they follow from the rules of angular momentum. A complete wavefunction for a hydrogen like atom must specify also the spin part. The total wavefunction is then a product of the spatial wavefunction and the spin part.


Note that analogously, the $\hat{S}_x$ and $\hat{S}_y$ operators can be defined. These do not commute with $\hat{S}_z$. Because electrons have spin angular momentum, the unpaired electrons in silver atoms (Stern-Gerlach experiment) produce an overall magnetic moment (``the two two spots of silver atoms''). The spin magnetic moment is proportional to its spin angular momentum (compare with Eq. (\ref{eq10.36})):

$${\vec{\hat{\mu}}_S = -\frac{g_ee}{2m_e}\vec{\hat{S}}}$$

where $g_e$ is the free electron $g$-factor (2.002322 from quantum electrodynamics). The $z$-component of the spin magnetic moment is ($z$ is the quantiziation axis):

$${\hat{\mu}_z = -\frac{g_ee}{2m_e}\hat{S}_z}$$

Since $S_z$ is given by \ref{eq10.45}, we have:

$${\mu_z = -\frac{g_ee\hbar}{2m_e}m_s = -g_e\mu_Bm_s}$$

Thus the total energy for a spin in an external magnetic field is:

$${E = g_e\mu_Bm_sB}$$

where $B$ is the magnetic field strength (in Tesla).


By combining the contributions from the hydrogenlike atom Hamiltonian and the orbital
and electron Zeeman terms, we have the total Hamiltonian:

$${\hat{H} = \hat{H}_0 + \frac{eB}{2m_e}\hat{L}_z + \frac{g_eeB}{2m_e}\hat{S}_z = \hat{H}_0 + \frac{eB}{2m_e}\left(\hat{L}_z + g_e\hat{S}_z\right)}$$

The eigenvalues of this operator are (derivation not shown):

$${E_{n,m_l,m_s} = -\frac{m_ee^4Z^2}{2(2\pi\epsilon_0)^2\hbar n^2} + \frac{eB\hbar}{2m_e}\left(m_l + g_em_s\right)}$$


### Summary of spim and angular momentum

Spin emerges naturally once one accounts for relativistic effect, as was originally shown by Paul Dirac. Except for special cases relativisti effects however are not too significant to include in quantum mechanics therefore we incoprorate spin as an additional degree of freedom which has not been accounted for but which is knwon to exist!

| *Angular momentum* (eigenfunctions and eigenvalues)          | *Spin momentum* (eigenfunctions and eigenvalues)             |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| $\hat{L}=\hat{r}\times \hat{p}$<br>$\hat{L}_z = -i\hbar \Big (x\frac{\partial}{\partial y}-y\frac{\partial}{\partial x} \Big)$ | $\hat{S}$<br>$\hat{S}_z$                                     |
| $l=0,1,2,3,...$<br>$m_l=-l...0...l$                          | $s=1/2$ <br> $m_s=-1/2,1/2$                                  |
| $\mid l,m_l\rangle=Y_{l, m_l}$                               | $\mid s,m_s\rangle=\alpha,\beta$<br>$\mid 1/2,+ 1/2\rangle=\alpha$ <br>$\mid 1/2,- 1/2\rangle=\beta$ |
| $L=\hbar\sqrt{l(l+1)}$<br>$L_z=\hbar m$                      | $S=\hbar\sqrt{s(s+1)}=\hbar\sqrt{3/4}$<br>$S_z=\hbar m_s= \pm \hbar/2$ |
| $\mu_L=- g_l \frac{e}{2m_e}L$<br>$g_l=1$                     | $\mu_S = g_s \frac{e}{2m_e}S$ <br> $g_s \approx 2$           |
|                                                              |                                                              |
