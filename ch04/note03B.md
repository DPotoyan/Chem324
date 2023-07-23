## Vibrational spectra of diatomic molecules 

- Earlier when we have discussed the harmonic oscillator problem and we briefly mentioned that it can be used to approximate atom - atom interaction energy (*potential energy curve*) near the equilibrium bond length. 

- Harmonic potential would not allow for molecular dissociation and therefore it is clear that it would not be a realistic model when we are far away from the equilibrium geometry. The harmonic potential is given by:

$${E(R) = \frac{1}{2}k(R - R_e)^2}$$

-  $k$ is called the *force constant*, $R_e$ is the *equilibrium bond length*, and $R$ is the distance between the two atoms. The actual potential energy curve can be obtained from theoretical calculations or to some degree from spectroscopic experiments. 

- This curve has usually complicated form and hence it is difficult to solve the nuclear Schrodinger equation exactly for this potential. One way to see the emergence of the harmonic approximation is to look at *Taylor series expansion*:

$${E(R) = E(R_e) + \left(\frac{dE}{dR}\right)_{R = R_e}(R - R_e) + \frac{1}{2}\left(\frac{d^2E}{dR^2}\right)_{R = R_e}(R - R_e)^2 + ...}$$

Note that at the minimum we get $E(R) = E(R_e)$. 


$${E_v = \left(v + \frac{1}{2}\right)h\nu\textnormal{ with }v = 0, 1, 2,...}$$

- The $v$ is the vibrational quantum number, the vibrational frequency $\nu = \frac{1}{2\pi}\sqrt{k/\mu}$ and $\mu$ is the reduced mass of the diatomic molecule. Note that $v$ and $\nu$ look very similar but have different meaning! This can be expressed in wavenumber units as:

$${\tilde{E}_v = \frac{E_v}{hc} = \tilde{\nu}\left(v + \frac{1}{2}\right)}$$

> A typical value for vibrational frequency would be around 500 - 4000 $cm^{-1}$. Small values are associated with weak bonds whereas strong bonds have larger vibrational frequencies.


### Selection rules

Not all diatomic molecules have vibrational absorption spectrum. To see this, we have to calculate the electric dipole transition moment. Previously we found that the dipole moment depends on the internuclear distance. To proceed, we expand $\mu_0^{(e)}$ in a Taylor series about $R = R_e$:

$${\mu_0^{(e)}(R) = \mu_e + \left(\frac{\partial\mu}{\partial R}\right)_{R = R_e}(R - R_e) + \frac{1}{2}\left(\frac{\partial^2\mu}{\partial R^2}\right)_{R = R_e}(R - R_e)^2 + ...}$$


Next we integrate over the vibrational degrees of freedom and obtain:

$${\hspace*{-1cm}\int\psi^*_{v''}\mu_0\psi_{v'}dR = \mu_e\int\psi^*_{v''}\psi_{v'}dR + \left(\frac{\partial\mu}{\partial R}\right)_{R = R_e}\int\psi_{v''}^*(R - R_e)\psi_{v'}dR\hspace*{0.1cm}}
{ + \frac{1}{2}\left(\frac{\partial^2\mu}{\partial R^2}\right)_{R = R_e}\int\psi_{v''}^*(R - R_e)^2\psi_{v'}dR + ...}$$

- The first term above is zero since the vibrational eigenfunctions are orthogonal. The second term is nonzero if the dipole moment depends on the internuclear distance $R$. Therefore we conclude that the selection rule for pure vibrational transition is that the dipole moment must change as a function of $R$. 
- All homonuclear diatomic molecules (e.g., $H_2$, $O_2$, etc.) have zero dipole moment, which cannot change as a function of $R$. Hence these molecules do not show vibrational spectra. 
- In general, all molecules that have dipole moment have vibrational spectra as change in $R$ also results in change of dipole moment. We still have the integral present in the second term. 
- For harmonic oscillator wavefunctions, this integral is zero unless $v'' = v'\pm 1$ . This provides an additional selection rule, which says that the vibrational quantum number may either decrease or increase by one.


### Overtone transitions

The higher order terms are small but they give rise to overtone transitions with $\Delta v = \pm 2, \pm 3, ...$ with rapidly decreasing intensities.


For harmonic oscillator, the Boltzmann distribution  gives the statistical weight for the $v$ level:

$${f_v = \frac{e^{-(v + 1/2)h\nu/(k_BT)}}{\sum\limits_{v=0}^\infty e^{-(v+1/2)h\nu/(k_BT)}}}
{= \frac{e^{-vh\nu/(k_BT)}}{\sum\limits_{v=0}^\infty e^{-vh\nu/(k_BT)}}}$$

Note that the degeneracy factor is identically one because there is no degeneracy in one dimensional harmonic oscillator. To proceed, we recall geometric series:

$${\sum\limits_{v=0}^\infty x^v = \frac{1}{1 - x}\textnormal{ with }x < 1}$$

The denominator now gives:

$${\sum\limits_{v=0}^\infty e^{-vh\nu/(k_BT)} = \frac{1}{1 - e^{-h\nu/(k_BT)}}}$$

Further simplifying we obtain:

$${f_v = \left(1 - e^{-h\nu/(k_BT)}\right)e^{-vh\nu/(k_BT)}}$$

For example, for $H^{35}Cl$ the thermal population of the first vibrational level $v = 1$ is very small ($9\times$ $10^{-7}$) and therefore the excited vibrational levels do not contribute to the (IR) spectrum.


