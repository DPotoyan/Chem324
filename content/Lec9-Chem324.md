

## Outline for Lecture 3.3: Matheamtical Foundations of Quantum Mechanics

- The objective of this section to provide a gentle and mathematically friendly introduction  to the abstract mathematical formalism of quantum mechanics which include three topics of fundmental importance for quantum mechanics:

  1. **Linear vector spaces.**

  2. **Dirac notation.**

  3. **Functional spaces.**

- Learning the abstract formalism brings simplicity, unity and clairty to the relationships in quantum mechanisms. On the example of simple and familiar 2D-3D vectors we will illustrate the concepts of **basis set**  and  **linear superpositions.**  We then will show how **Dirac notation** can liberate  one from coordinate representations and explicit  intergrals which can often obscure  the underlying mathematical and physical facts. 
- With an abstract formalism we are able to fully appreciate the strange nature of quantum states which exist in a superoposition state! The metaphor of **Schrodinger's cat** is introduced to illustrate the stragneness of quantum phenomena on macroscopic scales. 



## Video "Vectors, what are they?"

Let's remind ourselves of some basics first. 1B3B has an excellent lecture series on linear algebra with stunning visual examples. I highly reccomend watching video 1 now and video 2 at the end of this chapter. 

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/fNk_zzaMoSs" frameborder="0" allowfullscreen>
</iframe>
</html>






## Vectors in 2D/3D

- Vector is just an ordered collection of numbers, e.g:

  -  $$a=(-2,8) \,\,\,$$ *A 2D vector*

  -  $$b=(1.34,4.23,5.98) \,\,\,$$  *A 3D vector* 

  -  $$c=(1,-2,4i,3+2i) \,\,\,$$  *A 4D vector with complex components.* 

  - $$f=(1,2,3,4,5,6 ...\infty)\,\,\,$$ *A infinite dimensional vector with integers as components.* 



### Dirac notation

Here, anticipating their immense usefulenss,  we introduce Dirac notation for vectors and functions. At this point let us just get used to this new and fancy looking notation:

|                 Dirac notation for vectors:                  |                 Dirac notation for functions                 |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| **Ket:** $$\mid a \rangle =(a_1,a_2,..) \,\,\,\,\,$$ <br>Example: $$\mid a \rangle =(1, 2i)$$ | **Ket:** $$\mid \psi\rangle=\psi$$<br> Example: $$\mid \psi \rangle=ix^2$$ |
| **Bra:**$$\langle a \mid = \begin{pmatrix}a_1\\a_2\\  ...\\\end{pmatrix}$$ <br> $$\mid a \rangle =\begin{pmatrix}1\\-2i\\\end{pmatrix}$$ | **Bra:** $$\langle \psi \mid=\psi^*$$<br>  $$\langle \psi \mid-ix^2$$ |
|        $$\langle a \mid b \rangle = \sum_i a_i b_i$$         | $$\langle \phi \mid \psi \rangle = \int  \phi(x)^* \psi(x) dx$$ |
| $$\langle a \mid a \rangle = \sum_i a^2_i$$<br> $$\langle a \mid a \rangle=(1)(1)+(2i)(-2i)=5$$ | $$\langle \psi \mid \psi \rangle = \int \mid \psi(x) \mid^2 dx$$<br> $$\langle \psi \mid \psi \rangle = \int^L_0 (ix^2)(-ix^2) dx=\frac{L^5}{5}$$ |




### Representation of vectors

Notation for vectors can be different depending on the context. Below we list the different representation of the same vector.

  - $$\vec{a}=2\vec{e_i}+3\vec{e_j}$$  
  - $$\mid a\rangle = 2\mid e_i\rangle+3 \mid e_j\rangle$$  
  - $$a=(2,3)$$    
  - $$a= \begin{pmatrix}
    2\\
    3\\
    \end{pmatrix}$$ 

In classical physics vectors are attached to a coordinate system with unit vectors ($\vec{e_i}$) and are drawn with an arrow to emphasize that vector has directionality in addition to magnitude. Below is an example of unit vectors in cartesian space where each vector is aligned alogn x, y and z axes. 

$$e_1 = (1, 0, 0)\,\,\, e_2=(0,1,0), e_3=(0,0,1)$$

Vectors are just an array of numbers, however, and the components of vector can refer to quantities for which direction is less relevant e.g (age, height and weight) of a person, a populations of all countires listed in array, a stock prices over last teny years, etc. 

  - $$Person = (22, 1.75, 80)$$   

  - $$Population  =(3.0, 40.0, 2.0 ...)$$ 

  - $$Stock = (1.4, 3.6, 8.5, ...)$$  



### Vector operations 

What defines vectors is the opeartions on them. Let us take a simple 2D vector as an exmaple: 

$$\mid a\rangle=a_1\mid e_1\rangle+a_2\mid e_2\rangle$$

**1. Addition or subtraction** with another vector $\mid b\rangle=\mid  e_1\rangle\pm\mid e_2\rangle$

  - $$ a+b=\begin{pmatrix}
    2\\
    3\\
    \end{pmatrix}+\begin{pmatrix}
    1\\
    1\\
    \end{pmatrix}=\begin{pmatrix}
    3\\
    4\\
    \end{pmatrix}$$

  - $$\mid a\rangle \pm \mid b\rangle=(a_1\pm b_1)\mid e_1\rangle+(a_2 b_2)\mid e_2\rangle$$

    

**2. Mulitiplication** by a  scalar  $\alpha=10$

  - $$\alpha \cdot a=10\begin{pmatrix}
    2\\
    3\\
    \end{pmatrix}=\begin{pmatrix}
    20\\
    30\\
    \end{pmatrix}$$

  - $$\alpha \mid a\rangle=\alpha a_1\mid e_1\rangle+ \alpha a_2\mid e_2\rangle$$

    

**3. Dot product** with another vector $\mid b\rangle$

  - $$a\cdot b=(2,3)\begin{pmatrix}
    1\\
    1\\
    \end{pmatrix}=2 \cdot 1+3\cdot 1=5$$
  - $$\langle a \mid b\rangle=a_1b_1+a_2b_2$$



###  Projection, orthogonality and norm

- Dot product  $\langle a\mid b \rangle$ shows the projection of vector a on b, e.g how much a and b have in comon with each other in terms of direction in space.  If the projection is zero, vectors are called orthogonal.  Example of the orthogonal vectors are unit vectors of cartesian coordinate system: 

  - $$\langle e_i \mid e_j \rangle =\delta_{ij}$$  
  - $$(1,0)\begin{pmatrix}
    0\\
    1\\
    \end{pmatrix}=a\cdot 0+0\cdot 1=0$$

   Where denote orthogonality and normalization with a convneient Kornecker symbol: $\delta_{ij}=0$  when $i\neq j$ and 1 when $i=j$ 

  

- Norm of a vector $\mid a\mid$ quantifies the length or magnitude of vector and is defined via square root of dot product of vectors with itself:
	
	- $$\langle a \mid a\rangle= a_1^2+a_2^2$$
	
	- $$\mid a \mid =\sqrt{a_1^2+a_2^2}$$
	

When the norm is on $\mid a \mid=1$, vector is called normalized. To normalize a vector is to dividethe vector by its norm. $\mid E_1\rangle = (4,0,0,0)$ is not normalized since $\langle E_1\mid E_1\rangle = 4$ hence we dividie by norm and obtain a normalized vector $\mid e_1\rangle=\frac{1}{4}\mid E_1\rangle=(1,0,0,0)$. And now $\langle e_1 \mid  e_1\rangle=1$


### Basis set and linear independence. 

**1. Every N dimensional vector can be uniquely represented as a linear combination of N orthogonal vectors.** And vice versa if a vector can be represented by N orthogonal vectors it means that the vector is N-dimensional. The set of unit vectors in terms of which an arbitrary N-dimensional vectords is expressed is called **basis set.** 

  

  - $$\mid v\rangle = \sum^{i=N}_{i=1} \mid e_i\rangle$$
  - $$a= \begin{pmatrix}
    2\\
    3\\
    \end{pmatrix} = 2\begin{pmatrix}
    1\\
    0\\
    \end{pmatrix}+3 \begin{pmatrix}
    0\\
    1\\
    \end{pmatrix}$$
  - $$a= \begin{pmatrix}
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
    \end{pmatrix}$$
    
    

**2. Orthognal unit vectors are linearly independent.** This means that no member of unit vectors can be expressed in terms of the others.  Linear indepence is exprsessed mathematically by having coefficients of the linear combination of 3D (4D, ND, etc) vectors to zero $\alpha_1=\alpha_2=\alpha_3=0$ as the only way to satify zero vector equality: 

  $$\alpha_1 \mid e_1\rangle +\alpha_1 \mid e_2\rangle+\alpha_3 \mid e_3\rangle=0$$   

The converse, when one of the coefificent $\alpha_i$can be non-zero immeaditely implies linear depenence,  because one can divide by that coeficient $\alpha_i$ and express the unit vector $\mid e_i\rangle$ in terms of the others.

## Video "Linear combinations, span, and basis vectors"

Now watch the second video from 1B3B on linear combinations and basis vectors. 

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/k7RM-ot2NWY" frameborder="0" allowfullscreen>
</iframe>
</html>

## Decomposition of functions into orthogonal components

- Writing a vector in terms of its orthogonal unit vectors is a powerful mathematical technique which permeates much of quantum mechanics. The role of finite dimensional vectors in QM play the  infinite dimensional functions. In analogy with vectors which can live in 2D, 3D or ND spaces, the inifinite dimensional space of functions is in quantum mathematics is known as **Hilbert space.** Named after famous mathematician David Hilbert. We will not go too much in depth about functional spaces other than listing some powerful analogies with simple vectors.   

|                           Vectors                            |                          Functions                           |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| Orthonrmal units:<br> $\langle x\mid y \rangle = \sum^{i=N}_{i=1} x_i y_i=\delta_{xy}$ | Orthonormal units: <br>$\langle \phi_i \mid \phi_j \rangle = \int^{+\infty}_{-\infty} \phi_i(x) \phi_j(x)dx=\delta_{ij}$ |
| Linear superposition: <br>$$\mid A \rangle = A_x \mid x\rangle+A_y\mid y\rangle$$ | Linear superposition: <br/>$$\mid f\rangle = c_1 \mid\phi_1\rangle+c_2\mid\phi_2\rangle$$ |
| Coefficients are projections: <br/>$$\langle e_x\mid A\rangle=A_x \langle x\mid x \rangle +A_y \langle x\mid y \rangle=A_x  $$ | Coefficients are projections: <br/>$$\langle \phi_1\mid A\rangle=c_1 \langle \phi_1\mid\phi_1 \rangle +c_2 \langle \phi_1\mid\phi_2 \rangle=c_1$$ |

In the first column we decompose a vectors in terms of two orthogonal components $A_i$ or projections of vector $A$ along the orthonormal vectors $x$ and $y$.  In the second column similiar decomposition where the dot product, due to iniften dimensions and continous variation is given by an integral!



### Eigenfunctions of Hermitian operators are complete basis set


The three crucial consequences of Hermitian property of operators  $\langle \phi \mid \hat{H} \mid \psi \rangle = \langle \psi \mid \hat{H}\mid \phi \rangle^*$ 

- Eigenvalues of  are real: $E_n=E^*_n$ for $H \mid \psi_n \rangle=E_n \mid \psi_n \rangle$

- Eigenfunctions are orthogonal: $$\langle \psi_n \mid  \psi_m\rangle=\delta_{nm}$$

- Eigenfunctions form complete basis set! $\mid f\rangle = \sum_i c_i \mid \psi_i \rangle$

The last two properties imply that eigenfunctions of Hermitian opeartors can play the same role for wavefunctions  as the unit vectors for  vectors.  That is a wave function can be expressed in terms of the eigenfunctions of an opearators which can act on the function.



### Wave function as a linear superoposition of eigenfunctions

This is where we see the power and beautfy of Dirac notation. That is, reagardless of how the function f looks like, weather we want to express it in terms of energy eigenfucntions or position eigenfunctions, the key expressions are identical to the vector case! 



- Express $f(x)$ function in terms of eigenfunctions of $\hat{H} \mid n\rangle=E_n \mid n \rangle$. 

  - In Dirac notation: $$f=\sum_n c_n \mid n\rangle$$  
  - In explicit notation: $$f(x) = \sum_n c_n \Big(\frac{2}{L}\Big )^{1/2} sin \Big (\frac{n\pi x}{L} \Big )$$

  

- What about coefficients $c_n$? They are what define the expansion. Thanks to orthogonality of eigenfunctions any coeficient $k$, just like component of a vector can be found by projecting our function (vectors) on eigenfunction $k$ (unit basis vector $k$). 

  - In Dirac notation: $$c_k = \langle k \mid f \rangle$$

  - In explicit notation: $$c_k = \Big(\frac{2}{L}\Big )^{1/2} \int sin \Big (\frac{k\pi x}{L} \Big )f(x) dx$$

    

Thus any wave function in quantum mechanics say $f(x)=x^2$ on $[0,L]$ for particle in a 1D Box, can be expanded in terms of eigenfunctions of operators by plugging the function in above expression and finding the coefficeients which are what define the expansion. This is a mahematical fact. The next question is what is the physical signficance and meaning for the coefficeints and expansion. 



## Quantum states as linear superpositions of mutually exclusive states. 

