

## Outline for Lecture 3.3: Matheamtical Foundations of Quantum Mechanics

- The objective of this section to provide a gentle and mathematically friendly introduction  to the three pillars of the abstract mathematical formalism of quantum mechanics, namely

  1. **Linear vector spaces.**

  2. **Dirac notation.**
  3. **Fourier transforms.**
- Learning the abstract formalism brings simplicity, unity and clairty to the relationships in quantum mechanisms. On the example of simple and familiar 2D-3D vectors we will illustrate the concepts of **basis set** ** and  **linear superpositions.**  We then will show how **Dirac notation** can liberate  one from coordinate representations and explicit  intergrals which can often obscure  the underlying mathematical and physical facts. 
- With an abstract formalism we are able to fully appreciate the strange nature of quantum states which exist in a superoposition state! The metaphor of **Schrodinger's cat** is introduced to illustrate the stragneness of quantum phenomena on macroscopic scales. 



## Video "Vectors, what are they?"

Lets remind ourselves of some basics first. 1B3B has an excellent lecture series on linear algebra with stunning visual examples. I highly reccomend watching videos 1. 

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/fNk_zzaMoSs" frameborder="0" allowfullscreen>
</iframe>
</html>






## Vectors in 2D/3D

- Vector is just an ordered collection of numbers, e.g:

  -   $a=(-2,8) \,\,\,$ *A 2D vector*

  -  $b=(1.34,4.23,5.98) \,\,\,$  *A 3D vector* 

  -  $c=(1,-2,4i,3+2i) \,\,\,$  *A 4D vector with complex components.* 

  - $f=(1,2,3,4,5,6 ...\infty)\,\,\,$ *A infinite dimensional vector with integers as components.* 

    


### Representation of vectors

- Notation for vectors can be different depending on the context. Below we list the different representation of the same vector.

  - $\vec{a}=2\vec{e_i}+3\vec{e_j} $  *Explicit representation in terms of **unit vectors.***
  - $\mid a\rangle = 2\mid e_i\rangle+3 \mid e_j\rangle$ *Same as before but **using Dirac notation.***
  - $a=(2,3)$    *Column array representation*
  - $a= \begin{pmatrix}
    2\\
    3\\
    \end{pmatrix}$ *Row array representation*

In classical physics vectors are attached to a coordinate system with unit vectors ($\vec{e_i}$) and are drawn with an arrow to emphasize that vector has directionality in addition to magnitude. Below is an example of unit vectors in cartesian space where each vector is aligned alogn x, y and z axes. 

- $e_1 = (1, 0, 0)\,\,\, e_2=(0,1,0), e_3=(0,0,1)$

However let us note vectors are just an array of numbers and the components of vector can refer to quantities for which direction is less relevant e.g (age, height and weight) of a person, a populations of all countires listed in array, a stock prices over last teny years, etc. 

- Person = (22, 1.75, 80)   in years, kg, m, kg
- Population  =(3.0, 40.0, 2.0 ...) popultions of countires listed alphabetically in millions.  
- Stock = (1.4, 3.6, 8.5, ...) price tags of an item in $ over years. 



## Vector operations 

What defines vectors is the opeartions on them. Let us take a simple 2D vector as an exmaple: $\mid a\rangle=a_1\mid e_1\rangle+a_2\mid e_2\rangle$ 

- **Addition or subtraction** with another vector $\mid b\rangle=\mid  e_1\rangle\pm\mid e_2\rangle$

  - $ a+b=\begin{pmatrix}
    2\\
    3\\
    \end{pmatrix}+\begin{pmatrix}
    1\\
    1\\
    \end{pmatrix}=\begin{pmatrix}
    3\\
    4\\
    \end{pmatrix}$

  - $\mid a\rangle \pm \mid b\rangle=(a_1\pm b_1)\mid e_1\rangle+(a_2 b_2)\mid e_2\rangle$

    

- **Mulitiplication** by a  scalar  $\alpha=10$

  - $\alpha \cdot a=10\begin{pmatrix}
    2\\
    3\\
    \end{pmatrix}=\begin{pmatrix}
    20\\
    30\\
    \end{pmatrix}$

  - $\alpha \mid a\rangle=\alpha a_1\mid e_1\rangle+ \alpha a_2\mid e_2\rangle$

    

- **Dot product** with another vector $\mid b\rangle$

  - $a\cdot b=(2,3)\begin{pmatrix}
    1\\
    1\\
    \end{pmatrix}=2 \cdot 1+3\cdot 1=5$
  - $\langle a \mid b\rangle=a_1b_1+a_2b_2$



##  Projection, orthogonality and norm

- Dot product  $\langle a\mid b \rangle$ shows the projection of vector a on b, e.g how much a and b have in comon with each other in terms of direction in space.  If the projection is zero, vectors are called orthogonal.  Example of the orthogonal vectors are unit vectors of cartesian coordinate system: 

  - $\langle e_i \mid e_j \rangle =\delta_{ij}$  where $\delta_{ij}=0$ when $i\neq j$ and 1 when $i=j$
  - $(1,0)\begin{pmatrix}
    0\\
    1\\
    \end{pmatrix}=a\cdot 0+0\cdot 1=0$

   In other words orthogonal vectors have nothing in common with each other and *live* in their own dimensions. 

- Norm of a vector $\mid a\mid$ quantifies the length or magnitude of vector and is defined via square root of dot product of vectors with itself:
	
	- $\langle a \mid a\rangle= a_1^2+a_2^2$
- $ \mid a \mid =\sqrt{a_1^2+a_2^2}$
- When the norm is on $\mid a \mid=1$, vector is called normalized. To normalize a vector is to dividethe vector by its norm. $\mid E_1\rangle = (4,0,0,0)$ is not normalized since $\langle E_1\mid E_1\rangle = 4$ hence we dividie by norm and obtain a normalized vector $\mid e_1\rangle=\frac{1}{4}\mid E_1\rangle=(1,0,0,0)$. And now $\langle e_1 \mid  e_1\rangle=1$
  
  
### Basis and linear independence. 

- **Every N dimensional vector can be uniquely represented as a linear combination of N orthogonal vectors.** And vice versa if a vector can be represented by N orthogonal vectors it means that the vector is N-dimensional. The set of unit vectors in terms of which an arbitrary N-dimensional vectords is expressed is called **basis set.** 

  - $\mid v\rangle = \sum^{i=N}_{i=1} \mid e_i\rangle$
  - $a= \begin{pmatrix}
    2\\
    3\\
    \end{pmatrix} = 2\begin{pmatrix}
    1\\
    0\\
    \end{pmatrix}+3 \begin{pmatrix}
    0\\
    1\\
    \end{pmatrix}$
  - $a= \begin{pmatrix}
    -1\\
    5\\ 8\\ \end{pmatrix} = -1\begin{pmatrix}
    1\\
    0\\ 0\\
    \end{pmatrix}+5 \begin{pmatrix}
    0\\
    1\\ 0\\
    \end{pmatrix}+8 \begin{pmatrix}
    0\\
    0\\ 1\\
    \end{pmatrix}$
  - 

- **Orthognal unit vectors are linearly independent.** This means that no member of unit vectors can be expressed in terms of the others.  Linear indepence is exprsessed mathematically by having coefficients of the linear combination of 3D (4D, ND, etc) vectors to zero $\alpha_1=\alpha_2=\alpha_3=0$ as the only way to satify zero vector equality: 

  
  
  $$\alpha_1 \mid e_1\rangle +\alpha_1 \mid e_2\rangle+\alpha_3 \mid e_3\rangle=0$$ 
  
  
  
  The converse, when one of the coefificent $\alpha_i$can be non-zero immeaditely implies linear depenence,  because one can divide by that coeficient $\alpha_i$ and express the unit vector $\mid e_i\rangle$ in terms of the others.
  
## Video "Linear combinations, span, and basis vectors"

Now watch the second video from 1B3B on linear combinations and basis vectors. 

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/k7RM-ot2NWY" frameborder="0" allowfullscreen>
</iframe>
</html>

## Decomposition of functions into orthogonal components

- Writing a vector in terms of its orthogonal unit vectors is a powerful idea which permeates much of quantum mechanics where the role of finite dimensional vectors we have infinite dimensional functions. First let us write the decomposition of a vectors in terms of two orthogonal components $A_i$ or projections of vector $A$ along the orthonormal vectors $x$ and $y$.  



$$\langle x\mid y \rangle = \sum^{i=N}_{i=1} x_i y_i=\delta_{xy}$$ 

$$\mid A \rangle = A_x \mid x\rangle+A_y\mid y\rangle$$

$$\langle e_x\mid A\rangle=A_x \langle x\mid x \rangle +A_y \langle x\mid y \rangle=A_x  $$

$$\langle y\mid A\rangle=A_x \langle y\mid x \rangle +A_y \langle y\mid y \rangle=A_y  $$



- For functions one can carry out similiar decomposition where the dot product, due to iniften dimensions and continous variation is given by an integral! Below we write an example of function of x decomposed in terms of two orthognal functions:

  

  $$ \langle \phi_i \mid \phi_j \rangle = \int^{+\infty}_{-\infty} \phi_i(x) \phi_j(x)dx=\delta_{ij}$$

  $\mid f\rangle = c_1 \mid\phi_1\rangle+c_2\mid\phi_2\rangle$

  $$\langle \phi_1\mid A\rangle=c_1 \langle \phi_1\mid\phi_1 \rangle +c_2 \langle \phi_1\mid\phi_2 \rangle=c_1  $$

  $$\langle \phi_2\mid A\rangle=c_1 \langle \phi_2\mid\phi_1 \rangle +c_2 \langle \phi_2\mid\phi_2 \rangle=c_2  $$



## Hermitian operators provide complete basis set

Eigenfunctions of Hermitian opeartors serve the same role for general wavefunctions  as the unit vectors for general vectors. That is any wave function can be expressed in terms of the eigenfunctions of an opearators which can act on the function.   





 