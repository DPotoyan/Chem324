# HW 6: Particle in a Box

### Table of useful integrals

| **Indefinite integra**l                                      | **Definite integral over $[0, L]$**                          |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| $$\int\sin (nx) cos(mx)dx=0$$    (for any n and m)           | $$\int^{L}_0\sin ( \frac{n\pi x}{L}) cos( \frac{n\pi x}{L})dx=0$$ |
| $$ \int  sin^2 (kx)dx=\frac{x}{2}-\frac{sin(2kx)}{4k}$$      | $$ \int^L_0  sin^2 \big(  \frac{n\pi x}{L}\big)dx=\frac{L}{2}$$ |
| $$ \int x\cdot sin^2 (kx)dx=\frac{a^2}{4}$$                  | $$ \int^L_0 x\cdot sin^2 \big(  \frac{n\pi x}{L}\big)dx=\frac{L^2}{4}$$ |
| $$\int x^2 \cdot sin^2 (kx)dx=\frac{x^3}{6}-\Big(\frac{x^2}{4k}-\frac{1}{8k^3} \Big)sin(2kx)-\frac{xcos(2kx)}{4k^2}$$ | $$ \int^L_0 x^2 \cdot sin^2 \big(  \frac{n\pi x}{L}\big)dx= \big( \frac{L}{2\pi n}\big)^3 \big (\frac{4 \pi^3 n^3}{3}-2n\pi \big )$$ |
| (Optional exercise for the fearless souls) Give it a try and see if you can obtain these expressions by carrying out integrations explicitly.  One approach is to use [Euler's relation](https://en.wikipedia.org/wiki/Euler%27s_formula) with [integration by parts](https://en.wikipedia.org/wiki/Integration_by_parts). |                                                              |

### Q-1 

Using the table of integrals above along with  lecture notes/book calculate the following quantities for the particle in a box  described by the following wave-function $\psi_n(x)=\Big(\frac{2}{L} \Big)^{1/2} sin \Big(\frac{n\pi x}{L}\Big)$. 

- $\langle x \rangle$, $\langle x^2 \rangle$, $\sigma_x$
- $\langle p \rangle$, $\langle p^2 \rangle$, $\sigma_p$

- $$E=\langle K \rangle$$ 
- $$\Delta E_n=E_{n+1}-E_{n}$$       (Energy spacing between levels n and n+1)

### Q-2 

Particle in a box (PIB) system is a useful toy model  for learning about the behaviour of electrons bound in atoms and molecules. Using the  average quantities computed above comment on the meaning of the following variations between two extreme limits

- Changing the box size $L$ from $[0, \infty]$

- Changing the quantization number $n$ from $[1, \infty]$ 

  


### Q-3 

_To solve this problem read carefully the end of chapter 3.5._ 

Particle in a box can also be a useful toy model for estimating excitation energies conugated molecules like butediene $$CH_2=CH-CH=CH_2$$. By taking $L$ to be the length of the linear chain and filling up energy levels by each pair of  $\pi$ electrons (e.g 2 in level $E_1$ and 2 in $E_2$ for butediene) one can compute transitions from highest occupied state to the next unoccupied state. For butadiene it will be $$h\nu = E_3-E_2$$ 

- Follow example in the book to find length of molecule L and the excitation wavelength for the following molecule with 6 $\pi$ electrons: $$CH_2=CH-CH=CH-CH=CH_2$$ 


### Q-4 

Normalize the discrete and continuous functions thereby making them proper probability distributions.

- $p=[25, 30, 20, 40, 50, 25]$  (number of times you getting values 1-6 when throwing a rigged die)
- $p(x)=e^{-2x}$               over a range of $[0,\infty]$ 
- $p(x) = sin(n\pi x/L)$ over a range of [0, L]
- $p(x)=10$                   over range of $[0,2]$ 
- $p(x)=e^{-x^2}$               over range of $[-\infty, \infty]$ (Read Appendix B and especially the part about gaussian distribution)

### Q-5 

In 2D and 3D particle in a box it is possible to have degenerate energy levels becasue of the symmetry of box.  What are the possible degeneracies of the first four energy levels of a partcile in 3D box with 

- $a=b=2c$

- $a=0.99b=2c $
