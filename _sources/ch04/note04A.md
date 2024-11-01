## Angular momentum  

:::{admonition} What You Need to Know
:class: note

- **Angular momentum** is essential in both classical and quantum mechanics. In classical mechanics, all isolated systems conserve angular momentum (along with energy and linear momentum). This conservation law simplifies calculations for systems such as planetary orbits, rotations of rigid bodies, and many other dynamic systems.
- In **quantum mechanics**, angular momentum is similarly fundamental, especially in understanding atomic structure and other systems with rotational symmetry. 
- Angular momentum in QM is represented by an operator—a vector operator, to be specific, much like the momentum operator. 
- However, unlike the linear momentum operator, the three components of the angular momentum operator **do not commute**.

:::

### L vs p Overview

| Property                  | Linear Momentum              | Angular Momentum             |
|---------------------------|-----------------------------|------------------------------|
| Nature                    | Linear motion in a straight line | Rotational motion around an axis |
| Vector   form            | $\vec{p} = m \cdot \vec{v}$            | $\vec{L} = \vec{p}\times\vec{r}$        |
| Scalar form               | $ \|\vec{p}\| = m \cdot v$            | $ \|\vec{L}\| = I \cdot \omega$        |
| Mass for point particles       | $m$            | $I=mr^2$        |
| Kinetic Energy           | $\frac{p^2}{2m}$            | $\frac{L^2}{2I}$         |
| QM operators              | $\hat{p_x}=-i\hbar\frac{\partial}{\partial x}$           | ${\hat{L_x} = yp_z - zp_y}$           |
| Conservation Principle    | Law of Conservation of Linear Momentum | Law of Conservation of Angular Momentum |
| Conservation Condition    | No net external force acting on a closed system | No net external torque acting on a closed system |


### Classical angular momentum 

:::{figure-md} markdown-fig
<img src="./images/L.png" alt="DeD0" class="bg-primary mb-1" width="300px">

Angular momemntum in classical mechanics is a vector quantity defined by the cross product of position vector and linear momentum. Direction is determined by using the thumb rule. 
:::

- In classical mechanics, the  [angular momentum](http://en.wikipedia.org/wiki/Angular_momentum) is defined via a corss product of position and linear momentum. The cross product is convenient to write using a [determinant](http://en.wikipedia.org/wiki/Determinant):

$${\vec{L} = \vec{r}\times\vec{p} =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k}\\
x & y & z\\
p_x & p_y & p_z\\
\end{vmatrix}= \left(yp_z - zp_y\right)\vec{i} + \left(zp_x - xp_z\right)\vec{j} + \left(xp_y - yp_x\right)\vec{k}}$$


- where $\vec{i}, \vec{j}$ and $\vec{k}$ denote [unit vectors](http://en.wikipedia.org/wiki/Unit_vector) along the $x, y$ and $z$ axes. $p_x$ and $L_x$ are components of linear and angular momentum respectively 

:::{admonition} **The Cartesian components of angular momentum**
:class: important

$${L_x = yp_z - zp_y}$$

$${L_y = zp_x - xp_z}$$

$${L_z = xp_y - yp_x}$$

$${\vec{L}^2 = \vec{L}\cdot\vec{L} = L_x^2 + L_y^2 + L_z^2}$$
:::


### Spherical coordinates

-  **Spherical coordinates** are more convenient for rotational problems. We therefore replace $(x,y,z)$ by $(r, \phi, \theta)$. For instance: when considering rotation with $r=const$ we are able to eliminate one degree of freedom associated with radial direction.

$$\hat{L}^2= L_x^2 + L_y^2 + L_z^2=\hat{L_r}^2+\hat{L_{\phi}}^2+\hat{L_\theta}^2 = \hat{L_{\phi}}^2+\hat{L_\theta}^2$$

:::{figure-md} markdown-fig
<img src="./images/spherical_volume.png" alt="DeD0" class="bg-primary mb-1" width="450px">

Since we are going to work in spherical coordinate system we need to know how operators look in differnet cooridnate systems. This figure shows a rectangular volume element expressed in spherical coordinates. 
:::

**Geometric relations**

$$x={\color{blue} r}{\color{green}sin\theta} {\color{orange} cos\phi}$$
$$y={\color{blue} r}{\color{green} sin\theta}  {\color{orange} cos\phi}$$
$$z={\color{blue} r} {\color{green} cos\theta}$$

**The range of spherical variables**

$$Radius:\,\,\,{\color{blue} 0<{r}<\infty}$$
$$Azimuthal\, angle:{\color{green}\,\,\,0<\phi<2\pi}$$
$$Polar\, angle:\,\,\,{\color{orange} 0<\theta<\pi}$$

**Volume Element**

$$
dV = {\color{blue} r^2} {\color{green}\sin \theta} \, {\color{blue} dr} \, {\color{green}d\theta} \, {\color{orange}d\phi}
$$

**Laplacian**

::::{tab-set} 
:::{tab-item} Cartesian

$$
\nabla^2 = \frac{{\partial^2}}{{\partial x^2}} + \frac{{\partial^2}}{{\partial y^2}} + \frac{{\partial^2}}{{\partial z^2}}
$$

:::

:::{tab-item} Polar
$$
\nabla^2 = {\color{blue}\frac{1}{{ r^2}} \frac{{\partial}}{{\partial r}} \left(r^2 \frac{{\partial}}{{\partial r}}\right) } + \frac{1}{{{\color{blue} r^2} {\color{orange}\sin(\phi)}}} {\color{green}\frac{{\partial}}{{\partial \theta}} \left(\sin(\phi) \frac{{\partial}}{{\partial \theta}}\right)} + {\color{orange}\frac{1}{{{\color{blue} r^2} \sin^2(\phi)}} \frac{{\partial^2}}{{\partial \phi^2}}}
$$
:::
::::




:::{admonition} **Example**
:class: note
Compute volume of cube and sphere using cartesian and spherical cooridnates by integrating volume elements
:::

:::{admonition} **Solution**
:class: note, dropdown

$$\int^a_0\int^b_0\int^c_0 dxdydz=a\cdot b\cdot c$$

$$\int^r_0\int^{2\pi}_0\int^\pi_0 r^2 \sin \theta \, dr \, d\theta \, d\phi=\frac{r^3}{3}\Big|^r_0 \cdot 2\pi \cdot (-cos\theta) \Big|^\pi_0\cdot 2\pi=\frac{4\pi r^3}{3}$$
:::

:::{admonition} **Example**
:class: note

Write down laplacian for a rigid rotor problem $r=const$. Show what equations result when you separate the two angular variables by pluggin in $\psi(r, \theta, \phi)$
:::

:::{admonition} **Solution**
:class: note, dropdown

$$
\nabla^2 =  {\color{blue}\frac{1}{{ r^2}}}\Big[  {\color{green}\frac{1}{\sin(\theta)}}{\color{green}\frac{{\partial}}{{\partial \theta}} \left(\sin(\theta) \frac{{\partial}}{{\partial \theta}}\right)} + {{\color{green}\frac{1}{{ \sin^2(\theta)}}} {\color{orange} \frac{{\partial^2}}{{\partial \phi^2}}}}\Big] = {\color{blue}\frac{1}{r^2}}\nabla^2_{\theta, \phi}
$$
:::


### Quantum angular momentum 

- In quantum mechanics, the classical angular momentum is replaced by the corresponding
quantum mechanical operator.

- In [spherical coordinates](http://en.wikipedia.org/wiki/Spherical_coordinate_system), the angular momentum operators can be written in the following form. The derivations are [quite tedious](https://planetmath.org/derivationofthelaplacianfromrectangulartosphericalcoordinates) involving multiple applications of chain rule but its just a straightforward math procedure. Note that the choice of $z$-axis  here was arbitrary. Sometimes the physical system implies such axis naturally (for example, the direction of an external magnetic field). 


::::{tab-set} 
:::{tab-item} Cartesian

$${\hat{L}_x = -i\hbar\left(y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y}\right)}$$

$${\hat{L}_y = -i\hbar\left(z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z}\right)}$$

$${\hat{L}_z = -i\hbar\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right)}$$

$$\hat{L}^2=\hat{L_x}^2+\hat{L_y}^2+\hat{L_z}^2$$
:::

:::{tab-item} Polar
$${\hat{L}_x = i\hbar\left(\sin(\phi)\frac{\partial}{\partial\theta} + \cot(\theta)\cos(\phi)\frac{\partial}{\partial\phi}\right)}$$

$${\hat{L}_y = i\hbar\left(-\cos(\phi)\frac{\partial}{\partial\theta} + \cot(\theta)\sin(\phi)\frac{\partial}{\partial\phi}\right)}$$

$${\hat{L}_z = -i\hbar\frac{\partial}{\partial\phi}}$$

$${\vec{\hat{L}}^2 = -\hbar^2\underbrace{\left[\frac{1}{\sin(\theta)}\frac{\partial}{\partial\theta}\left(\sin(\theta)\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2(\theta)}\frac{\partial^2}{\partial\phi^2}\right]}_{\equiv \Lambda^2}}$$
:::
::::




### Components of angular momentum do not commute!

- Unlike linear momentum components of angular momentum do not commute! 
- This implies that it is not possible to measure any of the Cartesian angular momentum pairs simultaneously with an infinite precision (the Heisenberg uncertainty relation).

:::{admonition}
:class: important

$$
{\left[\hat{L}_x,\hat{L}_y\right] = i\hbar\hat{L}_z, \left[\hat{L}_y,\hat{L}_z\right] = i\hbar\hat{L}_x,\left[\hat{L}_z,\hat{L}_x\right] = i\hbar\hat{L}_y} \\
{\left[\hat{L}_x,\vec{\hat{L}}^2\right] = \left[\hat{L}_y,\vec{\hat{L}}^2\right] = \left[\hat{L}_z,\vec{\hat{L}}^2\right] = 0}
$$

:::

- Note the cyclical nature of commutations between components


### Eignefunctions and eigenvalues of $L$ and $L_z$

- Since operators of component and angular momentum square commute is possible to find functions that are eigenfunctions of both $\vec{\hat{L}}^2$ and $\hat{L}_z$. 

:::{admonition} Eignefunctions and eigenvalues of angular momentum
:class: imporant 

$${{\hat{L}}^2 Y_l^m(\theta,\phi) = \hbar^2 l(l+1)\cdot Y_l^m(\theta,\phi)}$$

$${\hat{L}_zY^m_l(\theta,\phi) = m\hbar \cdot Y_l^m(\theta,\phi)}$$

- **Eigenfunctions:** $Y_l^m(\theta,\phi) $
- **Angular quantum number:** $l = 0,1,2,3...$ 
- **Magnetic quantum number:** $|m| = 0,1,2,3,...l$
:::

- Note that here $m$ has nothing to do with magnetism but the name originates from the fact that (electron or nuclear) spins follow the same laws of angular momentum. 
- Functions $Y_l^m$ are called [spherical harmonics](http://en.wikipedia.org/wiki/Spherical_harmonics). Examples of spherical harmonics with various values of $l$ and $m$ are given below (with [Condon-Shortley](http://en.wikipedia.org/wiki/Spherical_harmonics\#Condon-Shortley_phase)  [phase convention](http://en.wikipedia.org/wiki/Spherical_harmonics\#Condon-Shortley_phase)

### Spherical harmonics

| $Y_{lm}(\theta, \phi)$ | Expression |
|-----------------------|------------|
| $Y_{00}(\theta, \phi)$ | $\frac{1}{\sqrt{4\pi}}$ |
| $Y_{10}(\theta, \phi)$ | $\sqrt{\frac{3}{4\pi}} \cos(\theta)$ |
| $Y_{1-1}(\theta, \phi)$ | $\sqrt{\frac{3}{4\pi}} \sin(\theta) e^{-i\phi}$ |
| $Y_{20}(\theta, \phi)$ | $\sqrt{\frac{5}{16\pi}} (3\cos^2(\theta) - 1)$ |
| $Y_{2-1}(\theta, \phi)$ | $\sqrt{\frac{15}{4\pi}} \sin(\theta) \cos(\theta) e^{-i\phi}$ |
| $Y_{2-2}(\theta, \phi)$ | $\sqrt{\frac{15}{4\pi}} \sin^2(\theta) e^{-2i\phi}$ |

- The functions $Y_{J,m}(\theta,\phi)$ are spherical harmonics that frequently occur in problems with spherical symmetry as the convenient basis of expansion. Spherical harmonics are important in many theoretical and practical applications, e.g., the representation of multipole electrostatic and electromagnetic fields, computation of [atomic orbital](https://en.wikipedia.org/wiki/Atomic_orbital) [electron configurations](https://en.wikipedia.org/wiki/Electron_configuration), representation of gravitational fields,  MRI imaging for streamline tractography, and the magnetic fields of planetary bodies and stars.

![](./images/sphhar2.png)

- Spherical harmonics consist of a well known special functions called [associated Legendre polynomials](https://en.wikipedia.org/wiki/Associated_Legendre_polynomials) ($\theta$ part) times the complex exponential ($\phi$ part). 
- In physics, [spherical harmonics](https://en.wikipedia.org/wiki/Spherical_harmonics) are defined on the surface of a sphere  form a complete basis set. 
- Spherical harmonics can be used to represent functions defined on the surface of a sphere, just as circular functions (sines and cosines) are used to represent functions on a circle via [Fourier series](https://en.wikipedia.org/wiki/Fourier_series). Like the sines and cosines in the Fourier series, the spherical harmonics may be organized by (spatial) angular frequency. 


**Orthogonality**


$$\langle l', m'| l, m\rangle=\delta_{l,l'}\delta_{m,m'}$$ 

$${\int\limits_0^{\pi}\int\limits_0^{2\pi}Y_{l'}^{m'*}(\theta,\phi)Y_l^m(\theta,\phi)\sin(\theta)d\theta d\phi = \delta_{l,l'}\delta_{m,m'}}$$







