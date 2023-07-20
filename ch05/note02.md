 ## Spectrum of hydrogenlike atoms


 Equation of hydroen atom energy can be expressed in units ($m^{-1}$; usually $cm^{-1}$ is used):

$${\tilde{E}_n = \frac{E_n}{hc} = \frac{E_n}{2\pi\hbar c} = -\overbrace{\frac{m_ee^4}{4\pi c(4\pi\epsilon_0)^2\hbar^3}}^{\equiv R}
\times\frac{Z^2}{n^2}\textnormal{ }}$$


where $R$ is the [Rydberg constant](http://en.wikipedia.org/wiki/Rydberg_constant) and we have assumed that the nucleus has an infinite mass. To be exact, the Rydberg constant depends on the nuclear mass, but this difference is very small. For example, $R_H = 1.096 775 856 \times 10^7$ $m^{-1} = 1.096 775 856 \times 10^5$ $cm^{-1}$, $R_D = 1.097 074 275 \times 10^5$ $cm^{-1}$, and $R_\infty = 1.097 373 153 4 \times 10^5$ $cm^{-1}$. The latter value is for a nucleus with an infinite mass (i.e., $\mu = m_e$).


Eq of H atom energy can be used to calculate the differences in the energy levels:

$$\Delta\tilde{v}_{n_1,n_2} = \tilde{E}_{n_2} - \tilde{E}_{n_1} = -\frac{R_HZ^2}{n_2^2} + \frac{R_HZ^2}{n_1^2} = R_HZ^2\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$$


In the previous figure, the [Lyman series](http://en.wikipedia.org/wiki/Lyman_series) is obtained with $n_1 = 1$, [Balmer series](http://en.wikipedia.org/wiki/Balmer_series) with $n_1 = 2$, and [Paschen series](http://en.wikipedia.org/wiki/Hydrogen_spectral_series) with $n_1 = 3$. The ionization energy (i.e., when the electron is detached from the atom; see previous figure) is given by:

$${E_i = R_HZ^2\left(\frac{1}{1^2} - \frac{1}{\infty}\right)}$$

For a ground state hydrogen atom (i.e., $n = 1$), the above equation gives a value of 109678 cm$^{-1}$ = 13.6057 eV. Note that the larger the nuclear charge $Z$ is, the larger the binding energy is.


Recall that the wavefunctions for hydrogenlike atoms are $R_{nl}(r)Y_l^m(\theta,\phi)$ with $l < n$. For the first shell we have only one wavefunction: $R_{10}(r)Y_0^0(\theta,\phi)$. This state is usually labeled as $1s$, where 1 indicates the [shell number](http://en.wikipedia.org/wiki/Electron_shell) ($n$) and $s$ corresponds to orbital angular momentum $l$ being zero. For $n = 2$, we have several possibilities: $l = 0$ or $l = 1$. The former is labeled as $2s$. The latter is $2p$ state and consists of three degenerate states: (for example, $2p_x$, $2p_y$, $2p_z$ or $2p_{+1}$, $2p_0$, $2p_{-1}$). In the latter notation the values for $m$ have been indicated as subscripts. Previously, we have seen that:





$${m = -l, -l+1, ..., 0, ..., l-1, l}$$


For historical reasons, the following letters are used to express the value of $l$:

$${\phantom{\textnormal{symbo}}l = 0, 1, 2, 3, ...}{\textnormal{symbol} = s, p, d, f, ...}$$

To summarize the quantum numbers in hydrogenlike atoms:

$${n = 1, 2, 3, ...}$$
$${l = 0, 1, 2, ..., n-1}$$
$${m = 0, \pm 1, \pm 2,...,\pm l}$$

For a given value of $n$, the level is $n^2$ times degenerate. There is one more quantum number that has not been discussed yet: [Spin quantum number](http://en.wikipedia.org/wiki/Spin_quantum_number) For one-electron systems this can have values $\pm\frac{1}{2}$ (will be discussed in more detail later). In absence of magnetic fields the spin levels are degenerate and therefore the total degeneracy of the levels is $2n^2$.


The total wavefunction for a hydrogenlike atom is ($m$ is usually denoted by $m_l$):

}



$${\psi_{n,l,m_l}(r,\theta,\phi) = N_{nl}R_{nl}(r)Y_l^{m_l}(\theta,\phi)}$$

$${N_{nl} = \sqrt{\left(\frac{2Z}{na_0}\right)^3\frac{(n - l - 1)!}{2n\left[(n + l)!\right]}}}$$

$$R_{nl}(r) = \rho^le^{-\rho/2}{L_{n-l-1}^{2l+1}(\rho)}$$

### Table of Wavefunctions in cartesian coordinates




| $n$ | $l$ | $m$     | Wavefunction expressed in $\sigma= \frac{zr}{a_0}$                                                                                                                          |
|-----|-----|---------|------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | 0   | 0       | $\psi_{1s} = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-\sigma}$                                                            |
| 2   | 0   | 0       | $\psi_{2s} = \frac{1}{4\sqrt{2\pi}}\left(\frac{Z}{a_0}\right)^{3/2}(2 - \sigma)e^{-\sigma/2}$                                            |
| 2   | 1   | 0       | $\psi_{2p_z} = \frac{1}{4\sqrt{2\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma e^{-\sigma/2}	\textnormal{cos}(\theta)$                        |
| 2   | 1   | $\pm 1$ | $\psi_{2p_x} = \frac{1}{4\sqrt{2\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma e^{-\sigma/2}\textnormal{sin}(\theta)\textnormal{cos}(\phi)$ |
|     |     |         | $\psi_{2p_y} = \frac{1}{4\sqrt{2\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma e^{-\sigma/2}\textnormal{sin}(\theta)\textnormal{sin}(\phi)$ |
| 3   | 0   | 0       | $\psi_{3s} = \frac{1}{81\sqrt{3\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\left(27 - 18\sigma + 2\sigma^2\right)e^{-\sigma/3}$                                                      |
| 3   | 1   | 0       | $\psi_{3p_z} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\left(6 - \sigma\right)\sigma e^{-\sigma/3}	extnormal{cos}(\theta)$                               |
| 3   | 1   | $\pm 1$ | $\psi_{3p_x} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\left(6 - \sigma\right)\sigma  e^{-\sigma/3}\textnormal{sin}(\theta)\textnormal{cos}(\phi)$       |
|     |     |         | $\psi_{3p_y} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\left(6 - \sigma\right)\sigma    $                                                                 |
| 3   | 2   | 0       | $\psi_{3d_{z^2}} = \frac{1}{81\sqrt{6\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2e^{-\sigma/3}\left(3\textnormal{cos}^2(\theta) - 1\right)$                                  |
| 3   | 2   | $\pm 1$ | $\psi_{3d_{xz}} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2  e^{-\sigma/3}\textnormal{sin}(\theta)\textnormal{cos}(\theta)\textnormal{cos}(\phi)$ |
|     |     |         | $\psi_{3d_{yz}} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2  $                                                                                     |
| 3   | 2   | $\pm 2$ | $\psi_{3d_{x^2-y^2}} = \frac{1}{81\sqrt{3\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2  e^{-\sigma/3}\textnormal{sin}^2(\theta)\textnormal{cos}(2\phi)$                       |
|     |     |         | $\psi_{3d_{xy}} = \frac{1}{81\sqrt{3\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2$                                                                                             |



### Exaples of Laguerre polynomials


| $L_0^k(x)$ | $1$                                                                        |
|------------|----------------------------------------------------------------------------|
| $L_1^k(x)$ | $k-x+1$                                                                    |
| $L_2^k(x)$ | $\frac{1}{2} \left(k^2+3 k+x^2-2 (k+2) x+2\right)$                         |
| $L_3^k(x)$ | $\frac{1}{6} \left(k^3+6 k^2+11 k-x^3+3 (k+3) x^2-3 (k+2)(k+3) x+6\right)$ |
| $L_4^k(x)$ | $\frac{1}{24} (x^4-4 (k+4) x^3+6 (k+3) (k+4) x^2-4 k(k (k+9)+26) x$        |
|            | $-96 x+k (k+5) (k (k+5)+10)+24)$                                           |


