
### Particle in a 3D box

```{admonition} What you need to know
:class: note

- Particle in a box is a toy model of electron/atom/molecule trapped in some region of space $[0,L]$. The positional information of a quantum "particle" is described by a quantum wave function $\psi(x)$ which is obtained by solving Schrodinger equation a simple PDE/ODE or an eigenfunction-eigenvalue problem. 
-  Wave functions are standing waves just like in a guitar on a string problem. With one major difference! Quantum-wave function has a probabilistic meaning and hence has a completely different meaning from a classical notion of a "wave"
```

### What did we learn from 1D PIB model

1. In classical systems  a particle trapped inside a large box can move at any speed within the box and it is no more likely to be found at one position than another. However, when the well becomes very narrow (on the scale of a few nanometers), quantum effects become important. The particle may only occupy certain positive **energy levels**.

2. "Particle"  can never have **zero energy**, meaning that the particle can never "sit still". 

3. "Particle" is more likely to be found at certain positions than at others, depending on its energy level. The particle may never be detected at certain positions, known as **spatial nodes.**

### Quantum PIB in 3D

:::{figure-md} markdown-fig
<img src="https://upload.wikimedia.org/wikipedia/commons/1/13/Infinite_potential_well-en.svg" alt="pib1" class="bg-primary mb-1" width="300px">

Particle in a box subject to infinitely high potential walls
:::

$${\,\,\,\,\, -\frac{\hbar^2}{2m}\Delta\psi(x,y,z) + V(x,y,z)\psi(x,y,z) = E\psi(x,y,z)} \\ 
{\textnormal{OR}\,\,\,\,\,}{-\frac{\hbar^2}{2m}\left(\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2}\right) + V\psi = E\psi}$$

where the solutions $\psi$ must be normalized:

$${\int\limits_{-\infty}^{\infty}\int\limits_{-\infty}^{\infty}\int\limits_{-\infty}^{\infty}\left|\psi(x,y,z)\right|^2dxdydz = 1}$$

Consider a particle in a box with sides of lengths $a$ in $x$, $b$ in $y$ and $c$ in $z$. The potential inside the box is zero and outside the box infinity. Again, the potential term can be treated by boundary conditions (i.e,. infinite potential implies that the wavefunction must be zero there). The above equation can be now written as:


$${-\frac{\hbar^2}{2m}\Delta\psi = E\psi} \\
{\textnormal{with }\psi(a,y,z) = \psi(x,b,z) = \psi(x,y,c) = 0} \\
{\textnormal{and }\psi(0,y,z) = \psi(x,0,z) = \psi(x,y,0) = 0}$$


In general, when the potential term can be expressed as a sum of terms that depend separately only on $x, y$ and $z$, the solutions can be written as a product:

$${\psi(x,y,z) = X(x)Y(y)Z(z)}$$

By substituting and dividing by $X(x)Y(y)Z(z)$, we obtain:

$${-\frac{\hbar^2}{2m}\left[\frac{1}{X(x)}\frac{d^2X(x)}{dx^2} + \frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2} + \frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}\right] = E}$$

The total energy $E$ consists of a sum of three terms, which each depend separately on $x, y$ and $z$. Thus we can write $E = E_x + E_y + E_z$ and separate the equation into three one-dimensional problems:

$${-\frac{\hbar^2}{2m}\left[\frac{1}{X(x)}\frac{d^2X(x)}{dx^2}\right] = E_x\textnormal{ with }X(0) = X(a) = 0}\\
{-\frac{\hbar^2}{2m}\left[\frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2}\right] = E_y\textnormal{ with }Y(0) = Y(b) = 0}\\
{-\frac{\hbar^2}{2m}\left[\frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}\right] = E_z\textnormal{ with }Z(0) = Z(c) = 0}$$



Each line in anbove equations corresponds to one-dimensional particle in a box problem:

$${X(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n_x\pi x}{a}\right)}\\
{Y(y) = \sqrt{\frac{2}{b}}\sin\left(\frac{n_y\pi y}{b}\right)}\\
{Z(z) = \sqrt{\frac{2}{c}}\sin\left(\frac{n_z\pi z}{c}\right)}$$

Thus the three-dimensional wavefunction  is:

$${\psi(x,y,z) = X(x)Y(y)Z(z) = \sqrt{\frac{8}{abc}}\sin\left(\frac{n_x\pi x}{a}\right)\sin\left(\frac{n_y\pi y}{b}\right)\sin\left(\frac{n_z\pi z}{c}\right)}$$

The total energy is given by:

$${E_{n_x,n_y,n_z} = \frac{h^2}{8m}\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2}\right)}$$

Energy is again quantized and when $a = b = c$, we the energy levels can also be degenerate (i.e., the same energy with different values of $n_x, n_y$ and $n_z$).

In most cases, degeneracy in quantum mechanics arises from symmetry. When $a = b = c$, the lowest levels have the following degeneracy factors:

| Quantum Numbers \( n_x, n_y, n_z \) | Energy \( E_{n_x, n_y, n_z} \) | Degeneracy |
|------------------------------------|-------------------------------|------------|
| (1,1,1)                            | \( \frac{3\hbar^2}{2mL^2} \)  | 1          |
| (1,1,2), (1,2,1), (2,1,1)          | \( \frac{6\hbar^2}{2mL^2} \)  | 3          |
| (1,1,3), (1,3,1), (3,1,1)          | \( \frac{11\hbar^2}{2mL^2} \) | 3          |
| (1,2,2), (2,1,2), (2,2,1)          | \( \frac{9\hbar^2}{2mL^2} \)  | 3          |
| (1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1) | \( \frac{14\hbar^2}{2mL^2} \) | 6 |
| (1,3,3), (3,1,3), (3,3,1)          | \( \frac{19\hbar^2}{2mL^2} \) | 3          |
| (2,2,2)                            | \( \frac{12\hbar^2}{2mL^2} \) | 1          |
| (2,2,3), (2,3,2), (3,2,2)          | \( \frac{17\hbar^2}{2mL^2} \) | 3          |
| (2,3,3), (3,2,3), (3,3,2)          | \( \frac{22\hbar^2}{2mL^2} \) | 3          |
| (3,3,3)                            | \( \frac{27\hbar^2}{2mL^2} \) | 1          |
| (1,1,4), (1,4,1), (4,1,1)          | \( \frac{18\hbar^2}{2mL^2} \) | 3          |
| (1,2,4), (1,4,2), (2,1,4), (2,4,1), (4,1,2), (4,2,1) | \( \frac{21\hbar^2}{2mL^2} \) | 6 |
| (1,3,4), (1,4,3), (3,1,4), (3,4,1), (4,1,3), (4,3,1) | \( \frac{26\hbar^2}{2mL^2} \) | 6 |
| (1,4,4), (4,1,4), (4,4,1)          | \( \frac{33\hbar^2}{2mL^2} \) | 3          |
| (2,2,4), (2,4,2), (4,2,2)          | \( \frac{24\hbar^2}{2mL^2} \) | 3          |
| (2,3,4), (2,4,3), (3,2,4), (3,4,2), (4,2,3), (4,3,2) | \( \frac{29\hbar^2}{2mL^2} \) | 6 |
| (2,4,4), (4,2,4), (4,4,2)          | \( \frac{36\hbar^2}{2mL^2} \) | 3          |
| (3,3,4), (3,4,3), (4,3,3)          | \( \frac{34\hbar^2}{2mL^2} \) | 3          |
| (3,4,4), (4,3,4), (4,4,3)          | \( \frac{39\hbar^2}{2mL^2} \) | 3          |
| (4,4,4)                            | \( \frac{48\hbar^2}{2mL^2} \) | 1          |





:::{admonition} Example: 
Consider an electron in superfluid helium ($^4$He) where it forms a solvation cavity with a radius of 18 \AA. Calculate the zero-point energy and the energy difference between the ground and first excited states by approximating the electron by a particle in a 3-dimensional box.
:class: tip, dropdown

**Solution** The zero-point energy can be obtained from the lowest state energy (e.g. $n = 1$) with $a = b = c = 36$ \AA. The first excited state is triply degenerate ($E_{112}, E_{121}$ and $E_{211}$). Use Eq. (\ref{eq9.87}):

$$E_{111} = \frac{h^2}{8m_e}\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2}\right)$$
$$= \frac{(6.626076\times 10^{-34}\textnormal{ Js})^2}{8(9.109390\times 10^{-31}\textnormal{ kg})}\left(\frac{1}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1}{(36\times 10^{-10}\textnormal{ m})^2}\right)$$
$$= 1.39\times10^{-20}\textnormal{ J} = 87.0\textnormal{ meV}$$


$$E_{211} = E_{121} = E_{112} = \frac{(6.626076\times 10^{-34}\textnormal{ Js})^2}{8(9.109390\times 10^{-31}\textnormal{ kg})}$$
$$\times\left(\frac{2^2}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1^2}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1^2}{(36\times 10^{-10}\textnormal{ m})^2}\right)$$
$$= 2.79\times 10^{-20}\textnormal{ J} = 174\textnormal{ meV} \Rightarrow \Delta E = 87\textnormal{ meV}$$
(Experimental value: 105 meV; Phys. Rev. B 41, 6366 (1990))


The solutions in three dimensions are difficult to visualize. Consider a two-dimensional particle in a box problem. In this case $\psi = \psi(x, y)$ and we can visualize the solutions:
:::

### Applications

- Particle in a box model can be used to explain electronic transitions in conjugated molecules.

![](./images/pib1d-1.jpeg)

- Count pi electrons and fill up PIB energy levels.

- Compute transitions to next excited states.

![](./images/pib-applic2.jpeg)
