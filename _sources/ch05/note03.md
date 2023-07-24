## Probability densities for hydrogenlike atoms


A wavefunction for a one-electron system is called an orbital. For an atomic system such as H (hydrogen atom), it is called an [atomic](http://en.wikipedia.org/wiki/Atomic_orbital).


The orbital plots demonstrated the shapes of the orbitals but this does not tell us anything about the radial extent (i.e., how far the orbital reaches).


### Key takeaways


-  As the value of $Z$ is increased, the radial extent decreases. This indicates that for higher nuclear charge, the electrons will reside closer to the nucleus.
- The radial functions have $n - l - 1$ zero values (``nodes'') between distances from zero to infinity.
- The existence of the nodes makes the wavefunctions orthogonal. For example, $\psi_{1s}$ and $\psi_{2s}$ in hydrogenlike atoms are orthogonal.
\end{itemize}


### Visualization

When visualizing the radial probabilities, it is possible to do directly plot the square of the radial wavefunction ($R_{nl}^2$) or the radial probability density ($P_{nl}$):

$${P_{nl}(r) = r^2N_{nl}^2R_{nl}^2(r)}$$

According to this expression, the most probable radius for an electron on hydrogen atom $1s$ orbital is $a_0$ (the Bohr radius). Previous figures showed examples of $R_{nl}$ and $P_{nl}$. Probability densities are useful, for example, in understanding charge distributions in atoms and molecules.


As the principal quantum number $n$ increases, the electron moves out to greater distances from the nucleus. The average distance for an electron in a given orbital (with quantum numbers $n$ and $l$) is given by (this is \textit{not} the expectation value):

$${\langle r\rangle_{nl} = \int_0^\infty r\times P_{nl}(r)dr}{= \frac{n^2a_0}{Z}\lbrace 1 + \frac{1}{2}\lbrack  1 - \frac{l(l+1)}{n^2}\rbrack\rbrace}$$

Note that the expectation value of $r$ and the most probable value for $r$ are not equal. The expectation value can be thought of like *an average* and the most probable value like a *maximum value*.


The probability density (including the angular variables) for the electron in a hydrogenlike atom is given by:

$${\psi^*_{nlm}(r,\theta,\phi)\psi_{nlm}(r,\theta,\phi) = |N_{nl}R_{nl}(r)Y_l^m(\theta,\phi)|^2}$$

This function depends on three variables and is difficult to plot directly. Previously, we have seen that it is convenient to plot contour levels, which contain the electron with, for example, 90\% probability.

For degenerate states with $l > 0$, we have an additional degree of freedom in choosing how to represent the orbitals. In fact, any linear combination of given $3l$ orthogonal eigenfunctions corresponding to a degenerate set with orbital angular momentum $l$, is also a solution to the Schr\"odinger equation.


Two commonly used representations are the Cartesian form, which are real valued functions and have been, in the case of $l = 1$, denoted by $p_x$, $p_y$ and $p_z$, and the eigenfunctions of the angular momentum ($L^2$ and $L_z$), which are complex valued and are denoted by $p_{-1}$, $p_0$ and $p_{+1}$. The relation between the representations is:



$${p_x = -\frac{1}{\sqrt{2}}\left( p_{+1} - p_{-1}\right)\propto \textnormal{sin}(\theta)\textnormal{cos}(\phi)\propto x}
{p_y = \frac{i}{\sqrt{2}}\left( p_{+1} + p_{-1}\right)\propto \textnormal{sin}(\theta)\textnormal{sin}(\phi)\propto y}
{p_z = p_0}$$

Note by combining $p_x$, $p_y$ and $p_z$, the lobe of the orbital can be made to point at any direction. For $d$-orbitals, we have five degenerate levels:

$${d_{x^2 - y^2} = \frac{1}{\sqrt{2}} \left(d_{+2} + d_{-2}\right)\textnormal{, }d_{xy} = -\frac{i}{\sqrt{2}}\left( d_{+2} - d_{-2}\right)}
{d_{xz} = -\frac{1}{\sqrt{2}}\left( d_{+1} - d_{-1}\right)\textnormal{, }d_{yz} = \frac{i}{\sqrt{2}}\left( d_{+1} + d_{-1}\right)}
{d_{z^2} = d_0}$$
