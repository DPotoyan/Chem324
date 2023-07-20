## Atomic terms and selection rules


In the previous table, column \#7 (``level'') denotes a term symbol for the given atom. This term symbol contains information about the total orbital and spin angular momenta
as well as the total angular momentum (i.e., $J = L + S$). This is expressed as follows:

$${^{2S+1}L_J}$$

where $S$ is the total spin defined in Eq. (\ref{eq10.103}), $L$ is the total angular momentum of Eq. (\ref{eq10.99}), and $J$ is the total angular momentum Eq. (\ref{eq10.106}). Both $2S+1$ and $J$ are expressed as numbers and for $L$ we use a letter: S for $L = 0$, P for $L = 1$, D for $L = 2$, etc. $2S+1$ is referred to as spin
multiplicity (1 = singlet, 2 = doublet, 3 = triplet, ...). The term symbol specifies the ground state electronic
configuration exactly. Note that column \#6 (``electron configuration'') in the table, is
much longer and it ignores the exact configuration of electron spins. Note that only the valence
electrons contribute to the term symbol.


**EXample** What is the atomic term symbol for He atom in its ground state?

**Solution** The electron configuration in He is 1s$^2$ (i.e., two electrons on 1s orbital with opposite
spins). First we use Eq. (\ref{eq10.103}) to obtain $S$. We have two possibilities: $S = 1$ (triplet) or $S = 0$
(singlet). However, since we are interested in the ground state, both electrons are on 1s
orbital and hence they must have opposite spins giving a singlet state. Thus $S = 0$
and $2S + 1 = 1$. Since both electrons reside on s-orbital, $l_1 = l_2 = 0$ and $L = 0$ by Eq. (\ref{eq10.99}).
Eq. (\ref{eq10.104}) now gives $J = L + S = 0 + 0 = 0$. The term symbol is therefore $^1$S$_0$.



**Example** What are the lowest lying state term symbols for a carbon atom?\\

**Solution** The electronic configuration for ground state C is 1s$^2$2s$^2$2p$^2$. To get the possible lowest
lying states, we only consider the two $p$-electrons. From Eq. (\ref{eq10.103}) we get: $S = \frac{1}{2} + \frac{1}{2} = 1$ or $S = 0$. The first case corresponds to triplet and the last singlet state. The total orbital angular momentum quantum numbers are given by Eq. (\ref{eq10.99}): $L = 2,1,0$, which correspond to D, P and S terms, respectively. Again, because the electrons must have opposite spins when the go on the same orbital, some $S$ and $L$ combinations are not possible. Consider the following scenarios:\\

1. $L = 2$ (D term): One of the states ($M_L = -2$) must correspond to configuration, where both electrons occupy a $p$-orbital having $m_l = -1$. Note that the electrons must go on the above orbital with opposite spins and therefore
the triplet state, where the electrons could be parallel, is not allowed:

Thus we conclude that for $L = 2$, only the singlet state (i.e., $^1$D) is possible.

1. $L = 1$ (P term): The three eigen states correspond to:

In principle, all these configurations could also be written for the singlet state but it requires a more complicated consideration to see that this is \textit{not allowed} (see below).

1. $L = 0$ (S term): For this term we can only have $M_L = 0$, which corresponds to:

Again, it is not possible to have triplet state because the spins would have to be parallel on the same orbital. Hence only $^1$S exists.

We conclude that the following terms are possible: $^1$D, $^3$P and $^1$S. As we will see below, the Hund's rules predict that the $^3$P term will be the ground state (i.e., the lowest energy). The total angular momentum quantum number $J$ for this state may have the following values: $J = L + S = 2, 1$, or $0$. Due to spin-orbit coupling, these states have different energies and the Hund’s rules predict that the $J = 0$ state lies lowest in energy. Therefore the $^3$P$_0$ state is the ground state of C atom.


The above method is fast and convenient but does not always work and is not able to show that $^1$P does not exist. In the following (for carbon) we will list each possible electron configuration (microstate), label them according to their $M_L$ and $M_S$ numbers, count how many times each ($M_L$,$M_S$) combination appears and decompose this information into term symbols. The total number of possible microstates $N$ is given by:

$${N = \frac{(2(2l+1))!}{n!(2(2l+1) - n)!}}$$

where $n$ is the number of electrons and $l$ is the orbital angular momentum quantum number (e.g., 1 for $p$ orbitals, 2 for $d$, etc.). Next we need to count how many states of each $M_L$ and $M_S$ we have:


The total number of ($M_L$,$M_S$) combinations appearing above are counted in the following table and its decomposition into term symbols is demonstrated (note that $^1$P does not exist).

**Exercise** Carry out the above procedure for oxygen atom (4 electrons distributed on $2p$ orbitals). What are resulting the atomic term symbols?


### Hund's (partly empirical) rules are:

- The term arising from the ground configuration with the maximum multiplicity ($2S + 1$) lies lowest in energy.
\item For levels with the same multiplicity, the one with the maximum value of $L$ lies lowest in energy.
- For levels with the same $S$ and $L$ (but different $J$), the lowest energy state depends on the extent to which the subshell is filled:
    - If the subshell is less than half-filled, the state with the smallest value of $J$ is the lowest in energy.
    - If the subshell is more than half-filled, the state with the largest value of $J$ is the lowest in energy.


### Spin-orbit interaction

- This relativistic effect can be incorporated into non-relativistic quantum mechanics by including the following term into the Hamiltonian:

$${\hat{H}_{SO} = A\vec{\hat{L}}\cdot \vec{\hat{S}}}$$


where $A$ is the spin-orbit coupling constant and $L$ and $S$ are the orbital and spin angular momentum operators, respectively. The total angular momentum $J$ commutes with both $\hat{H}$ and $\hat{H}_{SO}$ and therefore it can be specified simultaneously with energy. We say that the corresponding quantum number $J$ remains good even when spin-orbit interaction is included whereas $L$ and $S$ do not. The operator dot product $\hat{L}\cdot \hat{S}$ can be evaluated and expressed in terms of the corresponding quantum numbers:

$${\vec{\hat{L}}\cdot\vec{\hat{S}}\left|\psi_{L,S,J}\right> = \frac{1}{2}\left[J(J+1)-L(L+1)-S(S+1)\right]\left|\psi_{L,S,J}\right>}$$

For example in alkali atoms ($S = 1/2, L = 1$), the spin-orbit interaction breaks the degeneracy of the excited $^2$P state ($^2$S$_{1/2}$ is the ground state):

### Atomic spectra and selection rules


The following selection rules for photon absorption or emission in one-electron atoms can be derived by considering the symmetries of the initial and final state wavefunctions (orbitals):

$${\Delta n = \textnormal{unrestricted},\,\, \Delta l = \pm 1,\,\, \Delta m_l = +1, 0, -1}$$

where $\Delta n$ is the change in the principal quantum number, $\Delta l$ is the change in orbital angular momentum quantum number and $\Delta m_l$ is the change in projection of $l$. Qualitatively, the selection rules can
be understood by conservation of angular momentum. Photons are spin 1 particles with $m_l = +1$ (left-circularly polarized light) or $m_l = -1$ (right-circularly polarized light). When a photon interacts with an atom, the angular momentum in it may chance only by $+1$ or $-1$; just like in the selection rules above.

### Nature of light matter interaction

- Note that light is electromagnetic radiation and, as such, it has both electric and magnetic components. The oscillating electric field component is used in driving transitions in optical
spectroscopy (UV/VIS, fluorescence, IR) whereas the magnetic component is used in magnetic resonance spectroscopy (NMR, EPR/ESR). 
- Photon emission from an atom (e.g., fluorescence) is rather difficult to understand with the quantum mechanical machinery that we have developed so far.
- The plain Schrodinger equation would predict that excited states in atoms would have infinite lifetime in vacuum. However, this is not observed in practice and atoms/molecules return to ground state by emitting a photon. This transition is caused by fluctuations of electric field in vacuum (see your physics lecture notes).

### Selection rules

In many-electron atoms the selection rules can be written as follows:

1.  $\Delta L = 0, \pm 1$ except that transition from $L = 0$ to $L = 0$ does not occur.
2. $\Delta l = \pm 1$ for the electron that is being excited (or is responsible for fluorescence).
3. $\Delta J = 0, \pm 1$ except that transition from $J = 0$ to $J = 0$ does not occur.
4. $\Delta S = 0$. The electron spin does not change in optical transition. The exact opposite holds for magnetic resonance spectroscopy, which deals with changes in spin states.

> In some exceptional cases, these rules may be violated but the resulting transitions will be extremely weak (``forbidden transitions''). Because of the last rule, some excited triplet states may have very long lifetime because the transition to the ground singlet state is forbidden (metastable states).

