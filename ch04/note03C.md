## Beyond harmonic oscillator

As discussed previously, the harmonic oscillator model is expected to work well near the equilibrium bond length and does not allow for dissociation of molecules. As the potential function is usually unknown, we attempt to account for the deviation from the harmonic behavior by adding higher order polynomial terms $\tilde{E}_v$:

$${\tilde{E}_v = \tilde{\nu}_e(v + \frac{1}{2}) - \tilde{\nu}_ex_e(v + \frac{1}{2})^2 + \tilde{\nu}_ey_e(v + \frac{1}{2})^3}$$

where $\tilde{\nu}_e$ is the vibrational wavenumber, $x_e$ and $y_e$ are anharmonicity constants, and $v$ is the vibrational quantum number. Usually the third term is ignored and we can write the vibrational transition frequencies as ($v\rightarrow v+1$):

$${\tilde{\nu}(v) = \tilde{E}_{v+1} - \tilde{E}_v = \tilde{\nu}_e - 2\tilde{\nu}_ex_e(v+1)}$$

As we will see soon that by adding the 2nd order polynomial term to the eigenvalues, we actually imply the use of a potential function that allows for dissociation. 

### On dissociation energy

- One has to distinguish between two kinds of dissociation energies: *equilibrium dissociation energy* $D_e$ and *spectroscopic dissociation energy* $D_0$. 

- $D_e$ is measured from the bottom of the potential to the dissociation limit whereas $D_0$ is measured from the lowest vibrational level to the dissociation limit. The meaning of these two quantities is demonstrated below.

The ground vibrational level energy is given by:

$${\tilde{E}_0 = \frac{\tilde{\nu}_e}{2} - \frac{\tilde{\nu}_ex_e}{4} + \frac{\tilde{\nu}_ey_e}{8}}$$

And therefore the difference between $D_0$ and $D_e$ is:

$${\tilde{D}_e - \tilde{D}_0 = \tilde{E}_0}$$


When starting from the lowest vibrational level ($v = 0$), the observed absorption frequencies for $v' = 1,2,3...$ are given by:

$${\tilde{\nu}(v') = \tilde{E}_{v'} - \tilde{E}_0 = \tilde{\nu}_ev' - \tilde{\nu}_ex_ev'(v'+1)}$$

Note that sometimes the frequency $\nu$ may be expressed as angular frequency $\omega$. The relationship between the two is just a constant factor:
$\omega = 2\pi\nu$. To convert these to energy, one must use either $E = h\nu$ or $E = \hbar\omega$.

### Morse potential

We added a second order term (3rd order ignored) to the expression for $\tilde{E}_v$ in harmonic oscillator expression but what kind of potential would this correspond to? It can be shown that this potential is the Morse potential:

$${V(R) = \tilde{D}_e\left(1 - \exp\left(-\alpha(R - R_e)\right)\right)^2}$$

where $D_e$ is the equilibrium dissociation energy and $\alpha$ is a parameter related to the anharmonicity in the potential.

This allows for a diatomic molecule to dissociate and therefore it is more realistic than the harmonic function. Solution of the Schr\"odinger equation using the Morse function gives the following expression for the vibrational energy levels:

$${\tilde{E}_v = \alpha\sqrt{\frac{\hbar \tilde{D}_e}{\pi c\mu}}\left(v + \frac{1}{2}\right) - \frac{\hbar\alpha^2}{4\pi c\mu}\left(v + \frac{1}{2}\right)^2}$$

By comparing this with 

$${\tilde{\nu}_e = \alpha\sqrt{\frac{\hbar \tilde{D}_e}{\pi c\mu}}}$$

$${\tilde{\nu}_ex_e = \frac{\hbar\alpha^2}{4\pi c\mu}}$$

Solving for $\tilde{D}_e$ gives:

$${\tilde{D}_e = \frac{\tilde{\nu}_e}{4x_e}}$$

Note that the actual potential energy curve most likely deviates from the Morse potential and therefore the above expressions are only approximate.

### Birge-Sponer plot

The Birge-Sponer plot can be used to estimate the dissociation energy $D_0$ by using the following sum:

$${D_0 = \sum\limits_{v = 0}\tilde{\nu}(v) \approx \int\tilde{\nu}(v)dv}$$

$D_0$ therefore represents the area under linear function $\tilde{\nu}(v)$. By using the mid-point numerical integration scheme, one should prepare the $x$-axis as $v+1/2$ and the $y$-axis as $\tilde{\nu}(v)$. The integration can be carried out with a simple python code. 
