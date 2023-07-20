## The hydrogen molecule ion


The electronic Schr\"odinger equation for H$_2^+$ can be solved exactly because the equation contains only one particle. However, the  involved math is very complicated and here we take another simpler but  approximate approach. This method will reveal all the important features of chemical bond. An approximate (trial) wavefunction is written as (real functions):

$${\psi_\pm(\vec{r}_1) = c_11s_A(\vec{r}_1) \pm c_21s_B(\vec{r}_1)}$$

where $1s_A$ and $1s_B$ are hydrogen atom wavefunctions centered at nucleus A 
and B, respectively, and $c_1$ and $c_2$ are constants. This function is
essentially a linear combination of the atomic orbitals (LCAO molecular
orbitals). Because the two protons are identical, we must have $c_1 = c_2 \equiv c$ (also $c > 0$).
The $\pm$ notation in Eq. (\ref{eq11.7}) indicates that two different wavefunctions can be 
constructed, one with ``+'' sign and the other with ``$-$'' sign. Normalization of the wavefunction requires:

$${\int{\psi_\pm^*\psi_\pm d\tau} = 1}$$



In the following, we consider the wavefunction with a ``+'' sign and evaluate the normalization integral ($S$ = overlap integral, which depends on $R$):


$$1 = c^2\int{(1s_A + 1s_B)(1s_A + 1s_B)d \tau}= \\ c^2\int{1s_A^2d \tau} = 1 + c^2{\int{1s_B^2d}\tau}$$

$$+ c^2{\int{1s_A1s_Bd\tau}}{= S}+ c^2{\int{1s_B1s_Ad\tau}}{= S}= c^2(2 + 2S)$$


This can be rewritten as:

$${1 = c^2(2 + 2S) \Rightarrow c = \frac{1}{\sqrt{2 + 2S}}}$$

and the complete ``+'' wavefunction is then:

$${\psi_+ \equiv \psi_g = \frac{1}{\sqrt{2(1 + S)}}(1s_A + 1s_B)}$$

In exactly the same way, we can get the ``$-$'' wavefunction:

$${\psi_- \equiv \psi_u = \frac{1}{\sqrt{2(1 - S)}}(1s_A - 1s_B)}$$



Note that the antibonding orbital has \underline{zero} electron density between the nuclei.

Recall that the square of the wavefunction gives the electron density. In the left hand side figure (the ``+'' wavefunction), the electron density is amplified between the nuclei whereas in the ``$-$'' wavefunction the opposite happens. \textit{The main feature of a chemical bond is the increased electron  density between the nuclei.} This identifies the ``+'' wavefunction as
a \underline{bonding orbital} and ``$-$'' as an \underline{antibonding orbital}.


- When a molecule has a center of symmetry (here at the half-way between the 
nuclei), the wavefunction may or may not change sign when it is inverted
through the center of symmetry. If the origin is placed at the center of 
symmetry then we can assign symmetry labels $g$ and $u$ to the wavefunctions.
If $\psi(x, y, z) = \psi(-x, -y, -z)$ then the symmetry label is
$g$ (even parity) and for $\psi(x, y, z) = -\psi(-x, -y, -z)$ we have $u$ label
(odd parity). 
-  According to this notation the $g$ symmetry orbital is the 
bonding orbital and the $u$ symmetry corresponds to the antibonding orbital.
Later we will see that this is \underline{reversed} for $\pi$-orbitals!


- The overlap integral $S(R)$ can be evaluated analytically (derivation not shown):

$${S(R) = e^{-R}\left( 1 + R + \frac{R^3}{3}\right)}$$

> Note that when $R = 0$ (i.e. the nuclei overlap), $S(0) = 1$ (just a check to see that the expression is reasonable).


