## Vibration-rotation spectra of diatomic molecules


:::{admonition} What you need to know
:class: note

- Rotational structure can often be observed to accompany vibrational transitions when using sufficiently high spectral resolution. 
- Spectral lines  correspond to simultaneous change in both vibrational and rotational quantum numbers. For example, for HCl molecule one can observe the vibrational quantum number to change $v' = v'' \pm 1$ and $J' = J''\pm 1$. 
- Note that the rotational structure can usually only be observed in dilute gas phase samples as molecular rotations tend to be quenched in liquids and solids.
:::

:::{admonition} **Selection rules**
:class: important


- Because the ground vibrational level ($v = 0$) is predominantly populated up to room temperatures, transitions from the excited vibrational states do not contribute to the spectrum at these temperatures. They can contribute when temperature is increased, however. 
- For rotational states many states are thermally populated and therefore the excited rotational states contribute to the spectrum. Note that at close to 0 K one could only observe one rotational transition ($J'' = 0 \rightarrow J' = 1$). 
- Transitions where the rotational quantum number increases by one ($\Delta J  = +1$) are said to belong to the $R$ branch and transitions where the rotational quantum number decreases by belong to the $P$ branch ($\Delta J = -1$). The intensities of the spectral lines reflect the thermal populations on the initial rotational states. The $Q$ branch corresponds to $\Delta J = 0$ but is only allowed in when the molecule has orbital angular momentum (e.g., NO).
:::

:::{admonition} **Spectroscopic applications of Rigid rotor model**
:class: important

The energy spacing between rotational levels assume simple expression predicting integer multiples (J+1) of spectral lines for $J=0,1,2,...$

$$
\Delta E_{J+1,J} = E_{J+1}-E_{J} = B[(J+1)(J+2)-J(J+1)]=2B(J+1)
$$

Often in spectroscopy application wavenumbers are adopted which we indicate by placing tilde on energy:

$$
\tilde{\nu}_{J+1,J} =\frac{1}{\lambda} = \frac{\Delta E}{hc} = 2\tilde{B}(J+1)
$$

Where rotational constant has units of inverse wavelength $[cm^{-1}]$ and is exprssed as  $\tilde{B}=\frac{h^2}{8\pi^2 I c}$



**Spectral lines are predicted to be equidistant!**

Rigid rotor model makes a very specifci prediction about spectral lines: they are to be equally spaced. In other words difference between adjacent frequency of tranisitons is a constnat number:

$$
\tilde{\nu}_{J+2,J+1}-\tilde{\nu}_{J+1,J}=2\tilde{B}
$$

Thus be measuring this spectral line difference, we can extract structural information about the molecule, e.g. compute the moment of inertia!

:::

:::{admonition} **Rotational-virbational transitions**
:class: important

Rotational transitions often accompany the transitions in vibrational levels. The simplest  model for joint vibrational and rotational transitions is a combination of a harmonic oscillator with rigid rotor models:

$$
E_{v,J} = h\nu(n+1/2)+BJ(J+1)
$$

The selection rules for harmonic oscillator and rigid rotor are $\Delta v =\pm 1$ and $\Delta J \pm 1$, respectively. 

![](./images/rovib1.png)

**Ro-vibrational spectra, R, P and Q branches**

Often times we are interested in transitions among rotational levels that accompany excitation from ground vibrational state $v=0\rightarrow v=1 $. The transitions with $\Delta J=+1$ and $\Delta J=-1$ appear as two branches in the spectrum known as R and P   branch, respectively. The Q-branch $\Delta J =0$ is predicted to be absent because it is forbidden by the selection rule of the rigid rotor model. 

$$
\tilde{\nu}_{\Delta J=+/-1} = E_{v+1,J\pm1} - E_{v,J} = \tilde{\omega} \pm 2\tilde{B}(J+1)
$$

![](./images/branch.jpg)

:::









:::{admonition} **Correction #1 rovibrational coupling**
:class: important


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
:::


:::{admonition} **Correction #2 the unharmonicity/unrigdity term**
:class: important

Similiar to the first order correction we introduced for harmonic oscillator in the form of unharmonicity term  we can now also improve rigid rotor model by accounting for the fact that chemical bonds are not trully rigid: 

$$
\tilde{E}_{v,J} =\Big[\omega_e (v+1/2)- x_e\omega_e(v+1/2)^2\Big] + \Big[ BJ(J+1)-DJ^2 (J+1)^2 \Big ]
$$

Where constant D is called the **centrifugal distortion constant.** and is typically a small number $D<<1$
:::