## Vibration-rotation spectra of diatomic molecules


Rotational structure can often be observed to accompany vibronic transitions when using sufficiently high spectral resolution. Spectral lines in such spectrum correspond to simultaneous change in both vibrational and rotational quantum numbers. For example, for HCl molecule one can observe the vibrational quantum number to change $v' = v'' \pm 1$ and $J' = J''\pm 1$. The vibration-rotation spectrum of HBr is shown below. Note that the rotational structure can usually only be observed in dilute gas phase samples as molecular rotations tend to be quenched in liquids and solids.

### Selection rules
Because the ground vibrational level ($v'' = 0$) is predominantly populated up to room temperatures, transitions from the excited vibrational states do not contribute to the spectrum at these temperatures. They can contribute when temperature is increased, however. For rotational states many states are thermally populated and therefore the excited rotational states contribute to the spectrum. Note that at close to 0 K one could only observe one rotational transition ($J'' = 0 \rightarrow J' = 1$). Transitions where the rotational quantum number increases by one ($\Delta J  = +1$) are said to belong to the $R$ branch and transitions where the rotational quantum number decreases by belong to the $P$ branch ($\Delta J = -1$). The intensities of the spectral lines reflect the thermal populations on the initial rotational states. The $Q$ branch corresponds to $\Delta J = 0$ but is only allowed in when the molecule has orbital angular momentum (e.g., NO).

### Energies of vibration-rotation levels

The energies of the vibration-rotation levels are approximately given by:

$${\tilde{E}_{vr}= \tilde{E}_v + \tilde{E}_r = \tilde{\nu}_e\left(v + 1\right) - \tilde{v}_ex_e\left(v + \frac{1}{2}\right)^2 + \tilde{B}_vJ(J+1)}$$

where we have included separate rotational constant $B_v$ for each vibrational level $v$. Usually $B_1 < B_0$ etc. The dependence of the rotational constant on the vibrational quantum number can be expressed as:

$${\tilde{B}_v = \tilde{B}_e - \tilde{\alpha}_e\left(v + \frac{1}{2}\right)}$$

where $\tilde{\alpha}_e$ is the *vibration-rotation constant*


Next we consider a fairly common case where the vibrational transition occurs from $v = 0$ to $v = 1$ and consider only rotational transitions that fulfill the selection rule $\Delta J = \pm 1$. In the ground vibrational level the rotational level energies are given by:

$${\tilde{E_{vr}}(v=0,J) = \tilde{\nu}_e/2 - \tilde{v}_ex_e/4 + \tilde{B}_0J(J+1)}$$

When a molecule absorbs light, the vibrational quantum number increases by one. For the $R$ branch the rotational quantum number $J$ also increases by one. Thus we need the energy for this level:

$${\tilde{E}_{vr}(v = 1, J+1) = \frac{3}{2}\tilde{\nu} - \tilde{\nu}_ex_e\left(\frac{3}{2}\right)^2 + \tilde{B}_1(J+1)(J+2)}$$

The energy differences give the positions of the spectral lines for the $R$ branch:

$${\tilde{\nu}_R = \tilde{E}_{vr}(v = 1, J+1) - \tilde{E}_{vr}(v=0,J)}
{= \tilde{\nu}_0 + \tilde{B}_1(J+1)(J+2) - \tilde{B}_0J(J+1)}
{= \tilde{\nu}_0 + 2\tilde{B}_1 + \left(3\tilde{B}_1 - \tilde{B}_0\right)J + \left(\tilde{B}_1 - \tilde{B}_0\right)J^2}
{ = \tilde{\nu}_0 + \left(\tilde{B}_0 + \tilde{B}_1\right)\left(J + 1\right) + \left(\tilde{B}_1 - \tilde{B}_0\right)\left(J + 1\right)^2}$$



$${\tilde{\nu}_0 = \tilde{\nu}_e - 2\tilde{\nu}_ex_e}$$

where $\tilde{\nu}_0$ is the center of the vibration-rotation band. There will be no absorption at $\tilde{\nu}_0$ unless the molecule has a $Q$ branch. If $B_1 = B_0$ these lines are equally spaced.



For the $P$ branch $J \rightarrow J - 1$ and the excite state energy level is given by:

$${\tilde{E}_{vr}(v = 1,J-1) = \frac{3}{2}\tilde{\nu}_e - \tilde{\nu}_ex_e\left(\frac{3}{2}\right)^2 + \tilde{B}_1(J-1)J}$$

The corresponding transitions occur at:


$${\tilde{\nu}_P = \tilde{E}_{vr}(v=1,J-1) - \tilde{E}_{vr}(v=0,J)}
{= \tilde{\nu}_0 + \tilde{B}_1(J - 1)J - \tilde{B}_0J(J+1)}
{= \tilde{\nu}_0 - \left(\tilde{B}_1 + \tilde{B}_0\right)J + \left(\tilde{B}_1 - \tilde{B}_0\right)J^2}$$


To extract $B_0$ and $B_1$ from an experimental spectrum, the following expressions are useful:

$${\tilde{\nu}_R(J-1) - \tilde{\nu}_P(J+1) = 4\tilde{B}_0\left(J + \frac{1}{2}\right)}
{\tilde{\nu}_R(J) - \tilde{\nu}_P(J) = 4\tilde{B}_1\left(J + \frac{1}{2}\right)}$$

where $J$ is the initial state rotational quantum number. To apply these equations one must label the rotational lines according to their $J$ and record the peak positions in wavenumbers. This should be applied to many peak pairs and then obtain the averaged values for $\tilde{B}_0$ and $\tilde{B}_1$.


**Example** Calculate the relative populations of the first five rotational levels of the ground vibrational state of $H^{35}$Cl at 300 K. The ground vibrational state rotational constant $B_0 = 10.44$ cm$^{-1}$.\\

**Solution** The level populations are given by the Boltzmann distribution:

$$\frac{N_J}{N_0} = \left(2J + 1\right)e^{-hcJ(J+1)\tilde{B}_0/(k_BT)}$$

where $N_0$ is the number of molecules in the rotational ground state. First we calculate the factor appearing in the exponent:


$$\frac{hc\tilde{B}_0}{k_BT} = \frac{(6.626\times 10^{-34}\textnormal{ Js})(2.998\times 10^8\textnormal{ m/s})(10.44\textnormal{ cm}^{-1})(10^2\textnormal{ cm/m})}{(1.3806\times 10^{-23}\textnormal{ J K}^{-1})(300\textnormal{ K})}$$
$$ = 5.007\times 10^{-2}$$

Then, for example, for $J = 1$ we get:

$$\frac{N_1}{N_0} = 3e^{-2(5.007\times 10^{-2})} = 2.71$$

The same way one can get the relative populations as: 1.00, 2.71, 3.70, 3.84, 3.31, and 2.45 for $J = 0, 1, 2, 3, 4, 5$. Note that these are relative populations since we did not calculate the partition function $q$.

### Summary

### Spectroscopic applications of Rigid rotor model

The energy spacing between rotational levels assume simple expression predicting integer multiples (J+1) of spectral lines for $J=0,1,2,...$

$$
\Delta E_{J+1,J} = E_{J+1}-E_{J} = B[(J+1)(J+2)-J(J+1)]=2B(J+1)
$$

Often in spectroscopy application wavenumbers are adopted which we indicate by placing tilde on energy:

$$
\tilde{\nu}_{J+1,J} =\frac{1}{\lambda} = \frac{\Delta E}{hc} = 2\tilde{B}(J+1)
$$

Where rotational constant has units of inverse wavelength [cm^{-1}]  $\tilde{B}=\frac{h^2}{8\pi^2 I c}$



### Spectral lines are predicted to be equidistant!

Rigid rotor model makes a very specifci prediction about spectral lines: they are to be equally spaced. In other words difference between adjacent frequency of tranisitons is a constnat number:

$$
\tilde{\nu}_{J+2,J+1}-\tilde{\nu}_{J+1,J}=2\tilde{B}
$$

Thus be measuring this spectral line difference, we can extract structural information about the molecule, e.g. compute the moment of inertia!



### Rotational-virbational transitions

Rotational transitions often accompany the transitions in vibrational levels. The simplest  model for joint vibrational and rotational transitions is a combination of a harmonic oscillator with rigid rotor models:

$$
E_{v,J} = h\nu(n+1/2)+BJ(J+1)
$$

The selection rules for harmonic oscillator and rigid rotor are $\Delta v =\pm 1$ and $\Delta J \pm 1$, respectively. 

![](./images/rovib1.png)



### Ro-vibrational spectra, R, P and Q branches

Often times we are interested in transitions among rotational levels that accompany excitation from ground vibrational state $v=0\rightarrow v=1 $. The transitions with $\Delta J=+1$ and $\Delta J=-1$ appear as two branches in the spectrum known as R and P   branch, respectively. The Q-branch $\Delta J =0$ is predicted to be absent because it is forbidden by the selection rule of the rigid rotor model. 

$$
\tilde{\nu}_{\Delta J=+/-1} = E_{v+1,J\pm1} - E_{v,J} = \tilde{\omega} \pm 2\tilde{B}(J+1)
$$

![](./images/branch.jpg)



### Correction #1 rovibrational coupling

One correction one can make to the rotational-vibrational model is to include the effect of coupling between rotational and vibrational degrees of freedom. When exciting molecules to higher vibrational states, it is reasonable to expect that rotational parameters will be impacted as a result of changes in the average intra-nuclear distance, among other things. This can be accounted for by making rotational constant dependent on vibrational level v. $B\rightarrow B_v$. The v dependence is captured via the following expression showing that rotational constant is a linearly decreasing function of v!

$$
B_v = B_e-\alpha_e(v+1/2)
$$

The expression of energy with these correction would then be:

$$
E_{v,J} = h\nu(v+1/2)+B_vJ(J+1)
$$

$$
\tilde{\nu}_{\Delta J=+1} = \tilde{\omega} + 2\tilde{B_1}+(3\tilde{B_1}-\tilde{B}_0)J+(\tilde{B_1}-\tilde{B}_0)J^2
$$

$$
\tilde{\nu}_{\Delta J=-1} = \tilde{\omega} - (\tilde{B_1}+\tilde{B}_0)J+(\tilde{B_1}-\tilde{B}_0)J^2
$$


### Correction #2 the unharmonicity/unrigdity term

Similiar to the first order correction we introduced for harmonic oscillator in the form of unharmonicity term  we can now also improve rigid rotor model by accounting for the fact that chemical bonds are not trully rigid: 

$$
\tilde{E}_{v,J} =\Big[\omega_e (v+1/2)- x_e\omega_e(v+1/2)^2\Big] + \Big[ BJ(J+1)-DJ^2 (J+1)^2 \Big ]
$$

Where constant D is called the **centrifugal distortion constant.** and is typically a small number $D<<1$

