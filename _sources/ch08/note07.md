## Huckel molecular orbital theory


Molecules with extensive $\pi$ bonding systems, such as benzene,
are not described very well by the valence bond theory because the
$\pi$ electrons are delocalized over the whole molecule. $\sigma$ and $\pi$ 
bonds are demonstrated below for ethylene ($C_2H_4$ with $sp^2$ carbons):


Note that we have chosen $z$-axis along the internuclear axis. Because both $\sigma$ and $\pi$ bonding occurs between the two carbon atoms, we say that this is a double bond. Note that the hybrid orbitals here also explain the geometry. For triple bonds, one $\sigma$ and two $\pi$ bonds are formed.




- Huckel molecular orbital theory assumes that the $\pi$ electrons, which are  responsible for the special properties of conjugated and aromatic 
hydrocarbons, do not interact with one another and the total wavefunction is 
just a product of the one-electron molecular orbitals. The $\pi$ molecular 
orbital of the two carbons in $C_2H_4$ can be written approximately as:

$${\psi = c_1\phi_1 + c_2\phi_2}$$

where $\phi_1$ and $\phi_2$ are the $2p_y$ atomic orbitals for carbon 1 and 2, 
respectively. By using the variational principle (see Eq. (\ref{eq11.24})) gives 
the following secular determinant:

$${\begin{vmatrix} H_{11} - ES_{11} & H_{12} - ES_{12}\\
H_{21} - ES_{21} & H_{22} - ES_{22}\\ \end{vmatrix} = 0 \textnormal{ with }
H_{ij} = \int\phi_i^*H\phi_jd\tau \textnormal{ and } S_{ij} = \int\phi_i^*\phi_jd\tau}$$

In H\"uckel theory, the secular equation is simplified by assuming:

1. All the overlap integrals $S_{ij}$ are set to zero unless $i = j$, when 
$S_{ii} = 1$.
2. All diagonal matrix elements $H_{ii}$ are set to a constant denoted by
$\alpha$.
3. The resonance integrals $H_{ij}$ ($i \ne j$) are set to zero except for 
those on the neighboring atoms, which are set equal to a constant ($\beta$). Note that 
the indices here also identify atoms because the atomic orbitals are centered on atoms.

$${\begin{vmatrix}\alpha - E & \beta\\
\beta & \alpha - E\\ \end{vmatrix} = 0}$$


In Huckel theory, the Coulomb integral $\alpha$ and the resonance integral 
$\beta$ are regarded as empirical parameters. They can be obtained, for 
example, from experimental data. Thus, in the Huckel theory it is not 
necessary to specify the Hamiltonian operator!
Expansion of the determinant in Eq. (\ref{eq11.66}) leads to a quadratic 
equation for $E$. The solutions are found to be $E = \alpha \pm \beta$.
In general, it can be shown that $\beta < 0$, which implies that the lowest orbital energy
is $E_1 = \alpha + \beta$. There are two $\pi$ electrons and therefore the
total energy is $E_{tot} = 2E_1 = 2\alpha + 2\beta$. Do not confuse $\alpha$ and $\beta$ here with electron spin.


The wavefunctions (i.e. the coefficients $c_1$ and $c_2$ 
can be obtained by substituting the two values of $E$ into the original linear 
equations:

$${c_1(\alpha - E) + c_2\beta = 0}$$

$${c_1\beta + c_2(\alpha - E) = 0}$$

For the lowest energy orbital ($E_1 = \alpha + \beta$), we get (including normalization):

$${\psi_1 = \frac{1}{\sqrt{2}}(\phi_1 + \phi_2) \hspace{0.5cm}(\textnormal{i.e.}~c_1 = c_2 = \frac{1}{\sqrt{2}})}$$

and for the highest energy orbital ($E_2 = \alpha - \beta$) (including normalization):

$${\psi_2 = \frac{1}{\sqrt{2}}(\phi_1 - \phi_2) \hspace{0.5cm}(\textnormal{i.e.}~c_1 = \frac{1}{\sqrt{2}}, c_2 = -\frac{1}{\sqrt{2}})}$$



These orbitals resemble the H$_2^+$ LCAO MOs discussed previously.
This also gives us an estimate for one of the excited states where one electron
is promoted from the bonding to the antibonding orbital. The excitation energy is found to be $2|\beta|$, which allows for, for example, estimation of $\beta$
from UV/VIS absorption spectroscopy.

| HOMO orbital | = The highest occupied molecular orbital. |
|--------------|-------------------------------------------|
| LUMO orbital | = The lowest unoccupied molecular orbital. |


**Example** Calculate the $\pi$ electronic energy for 1,3-butadiene 
($CH_2=CHCH=CH_2$) by using the Huckel theory.

**Solution** First we have to write the secular determinant using the 
rules given earlier. In order to do this, it is convenient to number the 
carbon atoms in the molecule:


$$\overset{1}{\textnormal{CH}_2} = \overset{2}{\textnormal{CH}} 
- \overset{3}{\textnormal{CH}} = \overset{4}{\textnormal{CH}_2}$$


In this case there are two scenarios that should be considered:


1. A localized solution where the $\pi$ electrons are shared either with atoms 1 and 2 or 3 and 4. This would imply that the $\beta$ parameter should not be written between nuclei 2 and 3.
2.  A delocalized solution where the $\pi$ electrons are delocalized over all four carbons. This would imply that the $\beta$ parameters should be written between nuclei 2 and 3.



Here it turns out that scenario 2) gives a lower energy solution and we will 
study that in more detail. In general, however, both cases should be considered. The 
energy difference between 1) and 2) is called the \textit{resonance stabilization 
energy}. The secular determinant is:

$${\begin{matrix} 1\\2\\3\\4\\
\end{matrix}\begin{vmatrix}
\alpha - E & \beta & 0 & 0\\
\beta & \alpha - E & \beta & 0\\
0 & \beta & \alpha - E & \beta\\
0 & 0 & \beta & \alpha - E\\
\end{vmatrix}
= 0}$$




To simplify notation, we divide each row by $\beta$ and denote $x = (\alpha - E) / \beta$:

$${\begin{vmatrix}
x & 1 & 0 & 0\\
1 & x & 1 & 0\\
0 & 1 & x & 1\\
0 & 0 & 1 & x\\
\end{vmatrix} = 0}$$


Expansion of this determinant gives $x^4 - 3x^2 + 1 = 0$. There are four solutions $x = \pm 0.618$ and $x = \pm 1.618$. Thus there are four possible orbital energy levels:

$$
{E_1 = \alpha + 1.618\beta \hspace{0.5cm}\textnormal{(lowest energy)}} \\
{E_2 = \alpha + 0.618\beta} \\
{E_3 = \alpha - 0.618\beta} \\
{E_4 = \alpha - 1.618\beta \hspace{0.5cm}\textnormal{(highest energy)}}$$

There are four $\pi$ electrons, which occupy the two lowest energy 
orbitals. This gives the total $\pi$ electronic energy for the molecule:

$${E_\pi = 2(\alpha + 1.618\beta) + 2(\alpha + 0.618\beta)
= 4\alpha + 4.472\beta}$$

and the lowest excitation energy is $1.236|\beta|$.


The four Huckel MO wavefunctions are (calculations not shown):

$${\psi_1 = 0.372\phi_1 + 0.602\phi_2 + 0.602\phi_3 + 0.372\phi_4}
{\psi_2 = 0.602\phi_1 + 0.372\phi_2 - 0.372\phi_3 - 0.602\phi_4}
{\psi_3 = 0.602\phi_1 - 0.372\phi_2 - 0.372\phi_3 + 0.602\phi_4}
{\psi_4 = 0.372\phi_1 - 0.602\phi_2 + 0.602\phi_3 - 0.372\phi_4}$$


**Example** Apply the H\"uckel method for benzene molecule.

**Solution**The secular determinant for benzene is (electrons delocalized):

$${
\begin{vmatrix}
\alpha - E & \beta      &     0      & 0          & 0          & \beta\\
\beta      & \alpha - E & \beta      & 0          & 0          & 0\\
0          & \beta      & \alpha - E & \beta      & 0          & 0\\
0          & 0          & \beta      & \alpha - E & \beta      & 0\\
0          & 0          & 0          & \beta      & \alpha - E & \beta\\
\beta      & 0          & 0          & 0          & \beta      & \alpha - E\\
\end{vmatrix}
= 0
}$$

The solutions are (where the six $\pi$ electrons should be placed):

$$
{E_1 = \alpha + 2\beta~~\textnormal{(lowest energy)}} \\
{E_2 = E_3 = \alpha + \beta} \\
{E_4 = E_5 = \alpha - \beta} \\
{E_6 = \alpha - 2\beta~~\textnormal{(highest energy)}}$$
