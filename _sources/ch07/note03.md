##  Angular momentum of many-electron atoms

In many-electron atoms, each electron has both orbital and spin angular momenta. First, for simplicity, consider only the \textit{total} orbital angular momentum operator:

$${\hat{L} = \sum\limits_{i=1}^{N} \hat{l}_i}$$

where $N$ is the number of electrons and $\hat{l}_i$ is the angular momentum operator for electron $i$. The projection operator along the $z$-axis is then given by:

$${\hat{L}_z = \sum\limits_{i=1}^{N} \hat{l}_{z,i}}$$


$${M_L = \sum\limits_{i=1}^{N}m_i}$$

Vector model for adding 3 angular momenta:

- $\vec{L}$ = Total orbital angular momentum.
- $\vec{l}_1, \vec{l}_2, \vec{l}_3$ = individual angular momenta.


- $\hat{L}, \hat{l}_i$ are operators; $L, l_i$ are the corresponding quantum numbers.
- We assume a light atom and thus neglect the spin-orbit coupling.

### Total orbital angular momentum in a many-electron atom.


Consider an atom with two electrons each with orbital angular momentum $l_1$ and $l_2$, respectively. The maximum total angular momentum is obtained when the two angular momenta vectors are parallel: $L = l_1 + l_2$. When they point in opposite directions, we have: $L = l_1 - l_2$.


Hence the total angular momentum quantum number $L$ can take values (``Glebsch-Gordan series''):

$${L = l_1 + l_2, l_1 + l_2 - 1, ..., \left|l_1 - l_2\right|}$$

where $l_1$ and $l_2$ are the angular momentum quantum numbers for electrons 1 and 2, respectively. For example, if we have two electrons on $p$-orbitals, the above gives: $L = 2, 1$ or $0$. Furthermore, for $L = 2$, we can have $M_L = +2, +1, 0, -1, -2$; for $L = 1$, $M_L = +1, 0, -1$; and $L = 0$, $M_L = 0$. It is instructive to check that we actually have the same number of states in both representations (i.e., the uncoupled vs. the coupled representation). In the uncoupled representation: $3^2 = 9$ states (3 $p$-orbitals and 2 electrons) and in the coupled 5 + 3 + 1 = 9.


- Usually closed shell inner core electrons are not included in the consideration as they don't contribute to the end result.


### Total spin angular momentum in many-electron atom.


The total spin angular momentum operator for a many-electron atom is given by:

$${\hat{S} = \sum\limits_{i=1}^{N}\hat{s}_i}$$

and the $z$-component of the total spin angular momentum operator is defined as:

$${\hat{S}_z = \sum\limits_{i=1}^{N}\hat{s}_{z,i}}$$

Here $\hat{s}_i$ and $\hat{s}_{z,i}$ refer to spin angular momenta of the individual electrons. In similar fashion to (\ref{eq10.98}), total quantum number $M_S$ can be written:

$${M_S = \sum\limits_{i=1}^{N} m_{s,i}}$$

This value can range from $-S$ to $S$ and the total quantum number $S$ is given by:

$${S = s_1 + s_2, s_1 + s_2 - 1, ..., \left|s_1 - s_2\right|}$$

For example, for two electrons, $S = 1$ (``triplet state'') or $S = 0$ (``singlet state'').


### The total angular momentum (combined orbital and spin).

The total angular momentum operator$\hat{J}$, is as a vector sum of $\hat{L}$ and $\hat{S}$:

$${\vec{\hat{J}} = \vec{\hat{L}} + \vec{\hat{S}}}$$

$${\hat{J}_z = \hat{L}_z + \hat{S}_z}$$

The total quantum number $J$ is given by:

$${J = L + S, L + S - 1, ..., \left|L - S\right|}$$

with the corresponding total magnetic quantum number $M_J$ as:

$${M_J = M_L + M_S}$$


The previous coupling scheme is called the $LS$ coupling or Russell-Saunders coupling. This approach is only approximate when spin-orbit coupling is included in the Hamiltonian. Spin-orbit interaction arises from relativistic effects and its origin is not considered here. Instead, it should be simply thought to couple the orbital and spin angular momenta to each other with some given magnitude (``spin-orbit coupling constant''). Note that the spin-orbit effect is larger for heavier atoms. For these atoms the $LS$ coupling scheme begins to break down and only $J$ remains a good quantum number. This means that, for example, one can no longer speak about singlet and triplet electronic states. The $LS$ coupling scheme works reasonably well for the first two rows in the periodic table.


