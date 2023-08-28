
## Atomic spectra

```{admonition} What you need to know
:class: note

- Atomic spectroscopy measures frequencies or wavelengths of radiation absorbed or emitted by atoms.
- Spectra of atoms show discrete lines which indicate that atoms absorb or emit only very specific few frequencies
- In other words energies of atoms are quantized.
- Bohr tried to develop theory to explain spectra of atoms by combining classical mechanics with rules of quantization.
- For the simplest H atom Bohr's theory worked perfectly giving a closed formula which explains all spectral lines of H atom.
- Alas for atoms with more than one electron Bohr's theory fails to generalize which prompted scientist to develop a more rigorous theory fo quantum Mechanics
```

![](images/spectra.png)

- When heated or subjected to electrical discharge, atoms emit radiation of characteristic frequencies.  The spectrum from each atom is unique.  These discrete emitted frequencies comprise a stick spectrum such as the one shown above.  

### H atom spectra

![](images/lec1_AtomicSpectrum.png)

- These stick spectra are clearly impossible to describe with classical mechanics.  In 1885, Johann Blamer demonstrated that a subset of the hydrogen atom spectrum (the Balmer series) could be described by the equation

$$v = 8.2202\times10^{14}\left(1-\frac{4}{n^2}\right)$$


where $n=3,4,5,...$.  Later, Johannes Rydberg generalized this formula to account for the entire hydrogen atom spectrum yielding the Rydberg formula

$$\tilde{v} = R_H\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right)$$

where 
- $R_H = 109677.581$ cm$^{-1}$ is the Rydberg constant
- $n_1 = 1,2,3,...$, and $n_2 = n_1+1,n_1+2,...$.  

- While these equations fit the hydrogen atom spectrum nicely, they do not prescribe any physics to the system.  They do not present a model of the hydrogen atom but rather a heuristic equation that fits the data.  Nonetheless, scientists were perplexed by the presence of the integers $n_1$ and $n_2$. 

### Bohr model of H atom

- In 1911, Niels Bohr proposed a model for the hydrogen atom that was able to recapitulate the hydrogen atom spectrum. 
- The model consists of an electron orbiting a proton in circular orbits.  The proton is considered to be fixed in space because it is so much more massive than the electron.  
- Most importantly Bohr had to assume that the electron demonstrates wavelike characteristics and that these waves must have an integer number of modes around the circular orbit.  This equates to

$$\begin{equation}
2\pi r = n\lambda_e \quad n=1,2,3,...
\end{equation}$$

where $\lambda_e$ is the deBroglie wavelength of an electron and can be written as

$$\begin{equation}
\lambda_e = \frac{h}{m_ev}.
\end{equation}$$

Plugging the deBroglie wavelength equation into the circular wave equation yields

$$\begin{equation}
m_evr = \frac{nh}{2\pi} = n\hbar,
\end{equation}$$

where we have introduce $\hbar = \frac{h}{2\pi}$ as a short-hand because it comes up frequently in quantum mechanics. The term on the left-hand side of the last equation, $m_evr$, is the angular momentum of the electron.  Thus Bohr 's model demonstrates a quantization of the angular momentum of the electron.

Bohr posited that for stationary states of the electron the electrostatic force between the proton and electron,

$$\begin{equation}
f = \frac{e^2}{4\pi\varepsilon_0r^2}
\end{equation}$$

where $4\pi\varepsilon_0$ is present to achieve SI units, must be equal to the centrifugal force,

$$\begin{equation}
f = \frac{m_ev^2}{r}
\end{equation}$$

where $m_e$ is the mass and $v$ is the velocity of the electron.  Equating these two forces yields

$$\begin{equation}
\frac{e^2}{4\pi\varepsilon_0r^2} = \frac{m_ev^2}{r}.
\end{equation}$$


The combination of the force balance equation and the quantized angular momentum equation quantizes the values of $r$, the radius of the electron's circular orbit, that can be taken.  To demonstrate this we solve the quantized angular momentum equation for $v$ and plug the result into the force balance equation and solve for $r$:

$$\begin{align}
\frac{e^2}{4\pi\varepsilon_0r^2} &= \frac{m_e\left( \frac{n\hbar}{m_er}\right)^2}{r} \\
\Rightarrow \frac{e^2}{4\pi\varepsilon_0} &= \frac{(n\hbar)^2}{m_er} \\
\Rightarrow e^2m_er &= 4\pi\varepsilon_0(n\hbar)^2 \\
\Rightarrow r &= \frac{4\pi\varepsilon_0(n\hbar)^2}{e^2m_e} \quad n=1,2,3,...
\end{align}$$

The radius of the first Bohr orbit is denoted $a_0 = \frac{4\pi\varepsilon_0\hbar^2}{e^2m_e}$ or units of Bohr.  Allowed values of $r$ as a function of $n$ are plotted below.

### Energy of H atom within Bohr's theory eplains spectral lines from first principles

The energy of the system can is a sum of the Coulomb attraction between the electron and the proton and the kinetic energy of the electron:

$$\begin{equation}
E(r) = \frac{1}{2}m_ev^2 - \frac{e^2}{4\pi\varepsilon_0r}
\end{equation}$$

To determine the energy of an electron that is limited to be in the circular wavelike orbits described above, we must use the force balance relationship.  We do that by substituting $m_ev^2 = \frac{e^2}{4\pi\varepsilon_0r}$ into the energy equation to yield

$$\begin{align}
E(r) &= \frac{1}{2}\frac{e^2}{4\pi\varepsilon_0r} - \frac{e^2}{4\pi\varepsilon_0r} \\
    &= -\frac{1}{2}\frac{e^2}{4\pi\varepsilon_0r} \\
    &= -\frac{1}{2}\frac{e^2}{4\pi\varepsilon_0}\frac{e^2m_e}{4\pi\varepsilon_0(n\hbar)^2} \\
    &= -\frac{m_ee^4}{32\pi^2\varepsilon_0\hbar^2}\frac{1}{n^2} \\
    &= -\frac{m_ee^4}{8\varepsilon_0^2h^2}\frac{1}{n^2} \quad n=1,2,3,...
\end{align}$$

where I plugged in the quantized values for $r$ derived from the for balance relationship.  

Taking differences in energy between two energy levels, $n_1$ and $n_2>n_1$, yields

$$\begin{equation}
\Delta E = \frac{m_ee^4}{8\varepsilon_0^2h^2}\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
\end{equation}$$

Equating this to the frequency (use $E = h\nu$ and $\tilde{\nu} = \frac{\nu}{c}$) of emitted light yields

$$\begin{equation}
\tilde{v} = \frac{m_ee^4}{8\varepsilon_0^2ch^3}\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
\end{equation}$$

We see that this yields an expression for the Rydberg constant in terms of fundamental constants

$$\begin{equation}
R_H = \frac{m_ee^4}{8\varepsilon_0^2ch^3}
\end{equation}$$