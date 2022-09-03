## Outline for Lecture 3.3: Mathematical Foundations of Quantum Mechanics

- The objective of this section is to provide a gentle and mathematically friendly introduction to the abstract mathematical formalism of quantum mechanics. We are going to learn three mathematical topics of fundmental importance for quantum mechanics:

  1. **Linear vector spaces.**
  2. **Dirac notation.**
  3. **Functional spaces.**

- Learning the abstract mathematical formalism brings simplicity, unity and clairty to the relationships in quantum mechanisms. On the example of simple and familiar 2D-3D vectors we will illustrate the concepts of **basis set**  and  **linear superpositions**.  We will then show how **Dirac notation** can liberate  one from coordinate representations and explicit intergrals which may obscure the underlying mathematical and physical meaning. 
- With an abstract formalism we are able to fully appreciate the strange nature of quantum states which exist in a superoposition of states! We will touch upon  **Schrödinger's cat** and the **double slit experiments** to illustrate the strange nature of superimposed states. 

## Video "Vectors, what are they?"

Let's remind ourselves of some basics first. 3B1B has an excellent lecture series on linear algebra with stunning visual examples. I highly reccomend watching video 1 now and video 2 at the end of this chapter. 

<html>
<iframe width="560" height="315" src="https://www.youtube.com/embed/fNk_zzaMoSs" frameborder="0" allowfullscreen>
</iframe>
</html>

## Vectors in 2D/3D

- An example of a vector is an ordered collection of numbers, e.g:
  -  $$a=(-2,8) \,\,\,$$ *A 2D vector.*
  -  $$b=(1.34,4.23,5.98) \,\,\,$$  *A 3D vector.*
  -  $$c=(1,-2,4i,3+2i) \,\,\,$$  *A 4D vector with complex components.*
  - $$f=(1,2,3,4,5,6 ...,\infty)\,\,\,$$ *An infinite-dimensional vector with integers as components.*

### Dirac notation

Here, anticipating their immense usefulenss,  we introduce Dirac notation for vectors and functions. At this point let us just get used to this new and fancy looking notation.

|                 Dirac notation for vectors                   |                 Dirac notation for functions                 |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| **Ket:** $$\mid a \rangle =(a_1,a_2,..) \,\,\,\,\,$$ <br>Example: $$\mid a \rangle =(1, 2i)$$ | **Ket:** $$\mid \psi\rangle=\psi$$<br> Example: $$\mid \psi \rangle=ix^2$$ |
| **Bra:**$$\langle a \mid = \begin{pmatrix}a_1\\a_2\\  ...\\\end{pmatrix}$$ <br> $$\mid a \rangle =\begin{pmatrix}1\\-2i\\\end{pmatrix}$$ | **Bra:** $$\langle \psi \mid=\psi^*$$<br>  $$\langle \psi \mid = -ix^2$$ |
|        $$\langle a \mid b \rangle = \sum_i a_i b_i$$         | $$\langle \phi \mid \psi \rangle = \int  \phi(x)^* \psi(x) dx$$ |
| Example of Bra-Ket product for vectors in terms of components <br>$$\langle a \mid a \rangle = \sum_i a^2_i$$<br> $$\langle a \mid a \rangle=(1)(1)+(2i)(-2i)=5$$ | Example of Bra-Ket product for functions in terms of components<br>$$\langle \psi \mid \psi \rangle = \int \mid \psi(x) \mid^2 dx$$<br> $$\langle \psi \mid \psi \rangle = \int^L_0 (ix^2)(-ix^2) dx=\frac{L^5}{5}$$ |




### Representation of vectors

Notation for vectors can be different depending on the context. Below we list the different representation of the same vector.

  - $$\vec{a}=2\vec{e_i}+3\vec{e_j}$$  
  - $$\mid a\rangle = 2\mid e_i\rangle+3 \mid e_j\rangle$$  
  - $$a=(2,3)$$    
  - $$a= \begin{pmatrix}
    2\\
    3\\
    \end{pmatrix}$$ 

In classical physics vectors are attached to a coordinate system with unit vectors ($\vec{e_i}$) and are drawn with an arrow to emphasize that vector has a direction in addition to magnitude. Below is an example of unit vectors in cartesian space where each vector is aligned alogn x, y and z axes. 

$$e_1 = (1, 0, 0)\,\,\, e_2=(0,1,0), e_3=(0,0,1)$$

However, a vector can be just an array of numbers, and the components of a vector can refer to quantities for which direction is less relevant e.g (age, height and weight) of a person, populations of some countries, stock prices over last ten years, etc. 

  - $$Person = (22, 1.75, 80)$$   

  - $$Population  =(3.0, 40.0, 2.0, ...)$$ 

  - $$Stock = (1.4, 3.6, 8.5, ...)$$  



### Vector operations 

What defines vectors is the operations on them. Let us take a simple 2D vector as an example: 

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

  - $$\mid a\rangle \pm \mid b\rangle=(a_1\pm b_1)\mid e_1\rangle+(a_2\pm b_2)\mid e_2\rangle$$

    

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

- Dot product  $\langle a\mid b \rangle$ quantifies the projection of vector $a$ on $b$ and vice-versa. That is, how much $a$ and $b$ have in common with each other in terms of direction in space.  If the projection is zero we say that the vectors are orthogonal.  Example of the orthogonal vectors are unit vectors of cartesian coordinate system: 

  - $$\langle e_i \mid e_j \rangle =\delta_{ij}$$  
  - $$(1,0)\begin{pmatrix}
    0\\
    1\\
    \end{pmatrix}=1\cdot 0+0\cdot 1=0$$

   Where we denote both orthogonality and normalization with the convenient Kornecker symbol: $\delta_{ij}=0$  when $i\neq j$ and $1$ when $i=j$. 

  

- Norm of a vector $\mid a\mid$ quantifies the length or magnitude of vector. Norm is defined via square root of dot product of vector with itself:
	
	- $$\langle a \mid a\rangle= a_1^2+a_2^2$$
	
	- $$\mid a \mid =\sqrt{a_1^2+a_2^2}$$
	

When the norm is $\mid a \mid=1$, vector is called normalized. To normalize a vector is to divide the vector by its norm. $\mid E_1\rangle = (4,0,0,0)$ is not normalized since $\langle E_1\mid E_1\rangle = 4$ hence we divide by norm and obtain a normalized vector $\mid e_1\rangle=\frac{1}{4}\mid E_1\rangle=(1,0,0,0)$. And now $\langle e_1 \mid  e_1\rangle=1$.


### Basis set and linear independence. 

**1. Every $N$-dimensional vector can be uniquely represented as a linear combination of $N$ orthogonal vectors.** And vice-versa: if a vector can be represented by $N$ orthogonal vectors, it means that the vector is $N$-dimensional. A set of vectors in terms of which an arbitrary $N$-dimensional vector is expressed is called a **basis set.**

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
    
**2. Orthogonal vectors are linearly independent.** This means that no member of a set of vectors can be expressed in terms of the others.  Linear independence is exprsessed mathematically by having coefficients of the linear combination of 3D (4D, ND, etc) vectors to zero $\alpha_1=\alpha_2=\alpha_3=0$ as the only way to satify zero vector equality: 

  $$\alpha_1 \mid e_1\rangle +\alpha_1 \mid e_2\rangle+\alpha_3 \mid e_3\rangle=0$$   

The converse, when one of the coefificent $\alpha_i$can be non-zero immeaditely implies linear depenence,  because one can divide by that coeficient $\alpha_i$ and express the unit vector $\mid e_i\rangle$ in terms of the others.

## Video "Linear combinations, span, and basis vectors"

Now watch the second video from 3B1B on linear combinations and basis vectors. 

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/k7RM-ot2NWY" frameborder="0" allowfullscreen>
</iframe>
</html>

## Decomposition of functions into orthogonal components

- Writing a vector in terms of its orthogonal unit vectors is a powerful mathematical technique which permeates much of quantum mechanics. The role of finite dimensional vectors in QM play the  infinite dimensional functions. In analogy with sequence vectors which can live in 2D, 3D or ND spaces, the inifinite dimensional space of functions in quantum mathematics is known as a **Hilbert space**, named after famous mathematician David Hilbert. We will not go too much in depth about functional spaces other than listing some powerful analogies with simple sequence vectors.   

|                $$\,$$Sequence vectors                 |                          Functions                           |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| Orthonormality of basis unit vectors x and y:<br> $$\langle x\mid y \rangle = \sum^{i=N}_{i=1} x_i y_i=\delta_{xy}$$ | Orthonormality of eigenfunctions of Hermitian operator: <br>$$\langle \phi_i \mid \phi_j \rangle = \int^{+\infty}_{-\infty} \phi_i(x) \phi_j(x)dx=\delta_{ij}$$ |
| Linear superposition: <br>$$\mid A \rangle = A_x \mid x\rangle+A_y\mid y\rangle$$ | Linear superposition: <br/>$$\mid f\rangle = c_1 \mid\phi_1\rangle+c_2\mid\phi_2\rangle$$ |
| Coefficients are expressed via projections onto basis vectors: <br/>$$\langle e_x\mid A\rangle=A_x \langle x\mid x \rangle +A_y \langle x\mid y \rangle=A_x  $$ | Coefficients are expressed via projections onto basis functions: <br/>$$\langle \phi_1\mid \Psi\rangle=c_1 \langle \Psi \mid\phi_1 \rangle +c_2 \langle \Psi \mid\phi_2 \rangle=c_1$$ |

In the first column we decompose a vectors in terms of two orthogonal components $A_i$ or projections of vector $A$ along the orthonormal vectors $x$ and $y$.  In the second column similiar decomposition where the dot product, due to infinite dimension, is given by an integral!

### Eigenfunctions of Hermitian operators are complete basis set

The three crucial consequences of Hermitian property of operators  $\langle \phi \mid \hat{H} \mid \psi \rangle = \langle \psi \mid \hat{H}\mid \phi \rangle^*$ 

- Eigenvalues $\hat{H} \mid \psi_n \rangle=E_n \mid \psi_n \rangle$  are real: 

  $$E_n=E^*_n$$

- Eigenfunctions are orthogonal:

   $$\langle \psi_n \mid  \psi_m\rangle=\delta_{nm}$$

- Eigenfunctions form a complete basis set! 

  $$\mid f\rangle = \sum_i c_i \mid \psi_i \rangle$$

The last two properties imply that eigenfunctions of Hermitian opeartors  play the same role for functions as the unit vectors for  vectors.  That is a function can be expressed in terms of the eigenfunctions of an opearators which can act on the function.

### Wave function as a linear superoposition of eigenfunctions

This is where we see the power and beautfy of Dirac notation. Reagardless of how the function $f$ looks like, weather we want to express it in terms of the energy eigenfucntions or the position eigenfunctions, the key expressions are going to be the same! 



- Express $f(x)$ function in terms of eigenfunctions of $\hat{H} \mid n\rangle=E_n \mid n \rangle$. 

  - In Dirac notation: $$f=\sum_n c_n \mid n\rangle$$  
  - In explicit notation: $$f(x) = \sum_n c_n \Big(\frac{2}{L}\Big )^{1/2} sin \Big (\frac{n\pi x}{L} \Big )$$

  

- What about coefficients $c_n$? They are what define the expansion. Thanks to orthogonality of eigenfunctions any coeficient $k$, just like component of a vector can be found by projecting our function (vectors) on eigenfunction $k$ (unit basis vector $k$). 

  - In Dirac notation: $$c_k = \langle k \ket{f}$$

  - In explicit notation: $$c_k = \Big(\frac{2}{L}\Big )^{1/2} \int sin \Big (\frac{k\pi x}{L} \Big )f(x) dx$$

    

Thus any wave function in quantum mechanics say $f(x)=x^2$ on $[0,L]$ for particle in a 1D Box, can be expanded in terms of eigenfunctions of operators by plugging the function in above expression and finding the coefficeients which are what define the expansion. This is a mahematical fact. The next question is what is the physical signficance and meaning for the coefficeints and expansion. 



## Quantum states as linear superposition. 

Schrodinger equation as a linear differential equation admits as a general solution ithe linear superposition of eigenfunctions. This is a mathematical fact.<br>What is the physical meaning of solutions written as linear superpositions of eigenfunctions of some operator ? 

$$\hat{A}\mid \phi_n \rangle = A_n \mid \phi_n \rangle$$

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$



- **Absolue values of coeficients $\mid c_n \mid^2$ are equal to probabilities $p_n$ of finding system in a state $n$ described by eigenvalue $A_n$ and eigenfunction $\mid \phi_n \rangle$ of the operator $\hat{A}$.** 

  $$p_n=\mid c_n \mid^2$$

- **Probabilites sum to one.**

  **$$\sum_n \mid c_n \mid^2 =\sum_n p_n=1$$.**  

  

### Averages are probability weighted sums of eigenvalues.

- Superposition is a legitimate stae in which objects can exist. For instance an atom can be in a superposition of ground and next excited states with 50% probabilities. Such a state is descibred by a normalized ket. 

  $$\mid \psi \rangle=c_1 \mid 1 \rangle+c_2 \mid 2\rangle $$ 

    $$\langle \psi \mid \psi \rangle = \Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1\mid 1\rangle + c_2 \mid 2\rangle\Big] =\\ = \mid c_1 \mid^2 \langle 1 \mid 1 \rangle+(c^*_1 c_2\langle 1 \mid 2 \rangle+c_1 c^*_2\langle 2 \mid 1 \rangle)+\mid c_2\mid^2   = c_1^2+c^2_2=p_1+p_2=1$$

- The meaning of expectation becomes more transparent as an average over all eigenvalues obtained in the experiment. 

 $$\langle E\rangle= \langle \psi \mid \hat{H}\mid \psi \rangle = \Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1\hat{H}\mid 1\rangle + c_2 \hat{H}\mid 2\rangle\Big] =\Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1E_1\mid 1\rangle + c_2 E_2\mid 2\rangle\Big] = \\ = c_1^2E_1+c^2_2 E_2=p_1E_1+p_2 E_2$$



### Particle in a box example of a superoposition state

Suppose a the particle in a box is in a state of supperopistion of 1-st and 5-th states of eigenfunctions of Hamiltonian: 

$$\psi(x)=\frac{1}{\sqrt{2}}\cdot \Big(\frac{2}{L} \Big )^{1/2}sin\frac{\pi x}{L}+\frac{1}{\sqrt{2}}\cdot \Big(\frac{2}{L} \Big )^{1/2}sin\frac{5\pi x}{L}$$ 

This means that when we measure  energy we are going to obtain only two values $E_1$ and $E_5$ with equal probabilities $p_1=p_2=(1/\sqrt{2})^2$. 

The average of energy will be given by

$$\langle E \rangle =p_1 E_1+p_2 E_2 = \frac{1}{2}\frac{1^2 h^2}{8mL^2}+\frac{1}{2}\frac{5^2 h^2}{8mL^2}$$



### Quantum states as linear superposition of mutually exclusive states.

It is important to emphasize that postulates of quantum mechanics that in an experimetn we always obtain one of the eigenvalues in other words the system described by a superoposition "collapses" to one of the eigenfunctions. The idea of a quantum system randomly collapsing into distinct and mutuallye esclusive states has trubles many physicsis, who were at the frontiers of development of quantum mechanics. 

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$

- Act of an exeperimentation interferes with superposition state collapsing it to a particular eigenfunction with probability $\mid c_n \mid^2$

  $$\mid \psi \rangle \rightarrow \mid \phi_n \rangle$$

- Orthogonality of eigenfunctions implies mutual exclusivity of system being in state 1 vs state 2 

  $$\langle \phi_1 \mid \phi_2 \rangle=0$$

 

### Copenhagen interpretation

"The **Copenhagen interpretation** is an expression of the meaning of [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics) that was largely devised from 1925 to 1927 by [Niels Bohr](https://en.wikipedia.org/wiki/Niels_Bohr) and [Werner Heisenberg](https://en.wikipedia.org/wiki/Werner_Heisenberg). It is one of the oldest of numerous proposed [interpretations of quantum mechanics](https://en.wikipedia.org/wiki/Interpretations_of_quantum_mechanics), and remains one of the most commonly taught.(https://en.wikipedia.org/wiki/Copenhagen_interpretation#cite_note-Siddiqui2017-1)(https://en.wikipedia.org/wiki/Copenhagen_interpretation#cite_note-Wimmel1992-2)

According to the Copenhagen interpretation, physical systems generally do not have definite properties prior to being measured, and quantum mechanics can only predict the probability distribution of a given measurement's possible results. The act of measurement affects the system, causing the set of probabilities to reduce to only one of the possible values immediately after the measurement. This feature is known as [wave function collapse](https://en.wikipedia.org/wiki/Wave_function_collapse)."



### Video of quantum superopsition of atom. 

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/7B1llCxVdkE" frameborder="0" allowfullscreen>
</iframe>
</html>


### Schordinger's cat

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/UjaAxUO6-Uw" frameborder="0" allowfullscreen>
</iframe>
</html>

- Schrödinger created a thought experiment to illustrate bizarre nature of quantum superpositions, in which a quantum system such as an atom or photon can exist as a combination of multiple states corresponding to different possible outcomes. 

- The thought Experiment puts cat in a box with a single radioactive atom whose state dictates weather it decays thereby breaking the poisonous chamber in the box that kills the cat or does not decay and cat stays alive. So Schrodinger argued kitty must be thought of simultaneously dead and alive until experiment is done and cat is found in one of the two states. 

## Time dependence in quantum mechanics

So far we have completely ignored time dependence in our discussions. This is becasuse we have mainly focused on pure eigenfunction states $\psi_n(x,t)$ which show no time dependent behaviour for any quantity. It is easy to see why:

$$\psi_n(x,t) =\psi_n(x) \psi_n(x) e^{-\frac{i}{\hbar}E_n t}$$

When we do any kind of probabilistic calcualtion the time dependence dissapears because all the expressions involve square of wave functions and absolute value of complex temporal phase ends up as unity. 

$$\mid \psi_n(x,t) \mid^2 = \psi_n^*(x)\psi_n(x) e^{-\frac{i}{\hbar}E_n t} e^{+\frac{i}{\hbar}E_n t}=\mid \psi_n(x)\mid^2$$

$$\langle A \rangle = \int \psi_n^*(x)e^{+\frac{i}{\hbar}E_n t} \hat{A} \psi_n(x)e^{-\frac{i}{\hbar}E_n t}dx = \int \psi_n^*(x) \hat{A} \psi_n(x)dx$$

Will we always hae this lucky cancelation of time? The answer is no, when the states are described as linear superpositions time dependence does enter into picture. 



### Time depenendece in superposition states

Let us start with a superposition state of two energy eigenfunctions  at time t=0:

$$\mid \psi(0) \rangle =c_1\mid 1 \rangle + c_2 \mid 2 \rangle$$

What would the state be after some time t? By the virute of speration of variables we add the time dependence as a multiplicative factor for each eigenfunction:

$$\mid \psi(t) \rangle =c_1 e^{-\frac{i}{\hbar}E_1 t}\mid 1 \rangle + c_2 e^{-\frac{i}{\hbar}E_2 t}\mid 2 \rangle= c_1(t)\mid 1\rangle+c_2(t) \mid 2 \rangle$$

Thus we see that the coefficients change over time. This means our state vector moves in functional space spanned by fixed orthogonal eigenfunctions! We can verify that the expression satisfies time-dependent Schrodinger equation by plugging it and getting identity:

$$  i\hbar\frac{\partial}{\partial t}\mid \psi \rangle =\hat{H}\psi(t)\rangle $$

*Left hand side :*

$$i\hbar \Big( -\frac{i}{\hbar}E_1 c_1 e^{-\frac{i}{\hbar}E_1 t}\mid 1\rangle-\frac{i}{\hbar}E_2 c_2 e^{-\frac{i}{\hbar}E_2 t}\mid 2\rangle \Big) = E_1 c_1(t)\mid 1 \rangle +E_2 c_2(t)\mid 2 \rangle$$

*Right hand side:*

$$c_1 e^{-\frac{i}{\hbar}E_1 t}\hat{H}\mid 1 \rangle + c_2 e^{-\frac{i}{\hbar}E_2 t}\hat{H} \mid 2 \rangle = E_1 c_1(t)\mid 1 \rangle +E_2 c_2(t)\mid 2 \rangle $$



### Normalized wave function stays normalized over time

Some quantities, however will be invariant to time evolution. For instance it is reasonable to expect that normalization will not depend on time e.g particle is bound to be somwhere inside box at any moment of time. 

$$\mid \psi(t)\rangle=\sum_n c_n e^{-\frac{i}{\hbar}E_n t}\mid n\rangle$$



*Note how the bra-ket prodcut involves product of two independent sums indexed by n and k. We will be seeing expressions like this often later on.*

$$\langle \psi(t) \mid \psi(t)\rangle = \sum_n \sum_k \langle n\mid c^*_n e^{\frac{i}{\hbar}E_n t}  \cdot  c_k e^{-\frac{i}{\hbar}E_k t}\mid k\rangle = \sum_n \sum_k c^*_n c_ke^{-\frac{i}{\hbar}(E_k-E_n)t}\delta_{kn} =\sum_n \mid c_n \mid^2=1$$



Where the last line used the fact that eigenfunctions $\langle n \mid k\rangle=0$ are orthogonal hence cross terms in the sum where $k\neq n$ are all zero and only diagonal terms $n=k$ survie.

 

## Constants of motion

Quantities which are conserved over time are called **constants of motion**. In  QM we generaly have expectations or averages instead of sharply defined values. The principle of conservation of energy, however, dictates that the average of total energy must be one of the conserved quantities. To find out weather a quantity of interest will depend on time we  take a time derivative of the expectation:

$$\langle A \rangle =\langle \psi \mid A\mid \psi \rangle$$

$$\frac{\partial}{\partial t}\langle A \rangle = \langle \frac{\partial \psi}{\partial t} \mid A\mid \psi \rangle + \langle \psi \mid A\mid  \frac{\partial \psi}{\partial t} \rangle+\langle \psi \mid \frac{\partial \hat{A}}{\partial t}\mid  \psi \rangle$$

Now we making use of time dependent Schrodinger equation $i\hbar \frac{\partial }{\partial t}\mid \psi \rangle=\hat{H}\mid \psi\rangle$ to express time derivatives of bras and kets: 

- $$\langle \frac{\partial \psi}{\partial t}\mid = -\frac{1}{i\hbar} \hat{H}\langle \psi \mid$$

- $$\mid \frac{\partial \psi}{\partial t}\rangle = \frac{1}{i\hbar} \hat{H}\mid \psi \rangle$$

Plugging this into time derivative of expectation we get:

$$\frac{\partial}{\partial t}\langle A \rangle =\frac{1}{i\hbar}\langle \psi \mid \hat{A}\hat{H}\mid \psi \rangle-\frac{1}{i\hbar}\langle \psi \mid \hat{H}\hat{A}\mid \psi \rangle+\langle \psi \mid \frac{\partial \hat{A}}{\partial t}\mid  \psi \rangle = \\ = \frac{1}{i\hbar}\langle \psi \mid [\hat{A},\hat{H}]\mid \psi \rangle+\langle \psi \mid \frac{\partial \hat{A}}{\partial t}\mid  \psi \rangle$$

This imporatat relationship shows that if an operator $\hat{A}$ itself does not depend on time $\frac{\hat{A}}{t}=0$ then the quantites which commute with hamiltonian $[\hat{A},\hat{H}]=0$ will be constants of motion and those that don't $[\hat{A},\hat{H}]\neq0$ will evolve over time!

- Hamiltonian commutes with itself and does not depend on time $\frac{\partial}{\partial t}\langle E\rangle =0$



### Double slit Experiment

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/Xmq_FJd1oUQ" frameborder="0" allowfullscreen>
</iframe>
</html>



