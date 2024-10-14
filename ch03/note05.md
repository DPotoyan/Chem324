## P3 Eigenvalues

:::{admonition} What you need to know
:class: note


- Learning the abstract mathematical formalism brings simplicity, unity and clairty to the relationships in quantum mechanisms. On the example of simple and familiar 2D-3D vectors we will illustrate the concepts of **basis set**  and  **linear superpositions**.  
- We will then show how **Dirac notation** can liberate  one from coordinate representations and explicit intergrals which may obscure the underlying physics. 
- With an abstract formalism we are able to fully appreciate the strange nature of quantum states which exist in a superoposition of states! We will touch upon  **Schrödinger's cat** and the **double slit experiments** to illustrate the strange nature of quantum states. 
:::

### Reminer: Eigenfuncton-eigenvalue problem

**For operators**

$${\hat{A}\psi_i(x,y,z) = A_n\psi_i(x,y,z)}$$

- This is an eigenvalue problem solution of which yields $n = 1,2,3,...$ number of eigenfunctions $\psi_i$ and the eigenvalues $E_i$. Depending on boundary conditions there could be finite or infinite number of solutions. 

:::{note} **Example: find eigenvalues and eigenfunctions of momentum operator** 
:class: note

What are the eigenfunctions and eigenvalues of an operator $\hat{A} = d/dx$
:::

:::{note} **Solution**
:class: dropdown

Finding eigenfunctions/eigenvalue of differnetial operators analytically involves solving differnetial equations

$${\frac{d}{dx}f = kf(x) \Rightarrow \frac{df(x)}{f(x)} = kdx}$$ 
$$\ln(f) = kx + c$$ 
$${f_k = e^ce^{kx} = c'e^{kx}}$$
:::

**For operators written in matrix form**

- In applied numerical work operators are converted into matrices and one solves eigenvalue-eigenfunction problem of finding eigenvectors $v$ and eigenvalues $\lambda$. 
- For matri with $N$ dimensions there may be at most $N$ eigenvalues!

$$Av = \lambda v$$

:::{note} **Example: finding eigenvalues of a matrix** 
:class: note

$$\begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}\begin{pmatrix}
v_1 \\
v_2
\end{pmatrix} = \lambda \begin{pmatrix}
v_1 \\
v_2
\end{pmatrix}$$
::: 

::::{admonition}

```python
import numpy as np

# Define the matrix
matrix = np.array([[1, 2], [2, 4]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Display the eigenvalues and eigenvectors
eigenvalues, eigenvectors
```
::::







### Eigenfunctions of Hermitian operators form complete basis set

The three crucial consequences of Hermitian property of operators  

$$\langle \phi \mid \hat{H} \mid \psi \rangle = \langle \psi \mid \hat{H}\mid \phi \rangle^*$$

- Eigenvalues  are real: 

$$\hat{H} \mid \psi_n \rangle=E_n \mid \psi_n \rangle$$

$$E_n=E^*_n$$

- Eigenfunctions are orthogonal (and can also be normalized)

$$\langle \psi_n \mid  \psi_m\rangle=\delta_{nm}$$

- Eigenfunctions form a complete basis set! 

$$\mid f\rangle = \sum_i c_i \mid \psi_i \rangle$$

- The last two properties imply that eigenfunctions of Hermitian opeartors  play the same role for functions as the unit vectors for  vectors.  That is a function can be expressed in terms of the eigenfunctions of an opearators which can act on the function.

### Wave function as a linear superoposition of eigenfunctions

This is where we see the power and beautfy of Dirac notation. Reagardless of how the function $f$ looks like, We can always express it in terms of the energy eigenfucntions or the position eigenfunctions or any other complete set of functions.

- Express $f(x)$ function in terms of eigenfunctions of $\hat{H} \mid n\rangle=E_n \mid n \rangle$. 

  - In Dirac notation: $f=\sum_n c_n \mid n\rangle$ 
  - In explicit notation: $f(x) = \sum_n c_n \Big(\frac{2}{L}\Big )^{1/2} sin \Big (\frac{n\pi x}{L} \Big )$

  
- How do we find the coefficients $c_n$? Thanks to orthogonality of eigenfunctions any coeficient $k$, just like component of a vector can be found by projecting our function (vectors) on eigenfunction $k$ (unit basis vector $k$). 

  - In Dirac notation: $c_k = \braket{k \mid f}$

  - In explicit notation: $c_k = \Big(\frac{2}{L}\Big )^{1/2} \int sin \Big (\frac{k\pi x}{L} \Big )f(x) dx$

    
- Thus any wave function in quantum mechanics say $f(x)=x^2$ on $[0,L]$ for particle in a 1D Box, can be expanded in terms of eigenfunctions of operators by plugging the function in above expression and finding the coefficeients which are what define the expansion. This is a mahematical fact. The next question is what is the physical signficance and meaning for the coefficeints and expansion. 



### Quantum states as linear superposition. 

Schrodinger equation as a linear differential equation admits as a general solution ithe linear superposition of eigenfunctions. This is a mathematical fact.<br>What is the physical meaning of solutions written as linear superpositions of eigenfunctions of some operator ? 

$$\hat{A}\mid \phi_n \rangle = A_n \mid \phi_n \rangle$$

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$



- Absolue values of coeficients $\mid c_n \mid^2$ are equal to probabilities $p_n$ of finding system in a state $n$ described by eigenvalue $A_n$ and eigenfunction $\mid \phi_n \rangle$ of the operator $\hat{A}$.

$$p_n=\mid c_n \mid^2$$

Probabilites sum to one.

$$\sum_n \mid c_n \mid^2 =\sum_n p_n=1$$

  

### Averages are probability weighted sums of eigenvalues.

- Superposition is a legitimate stae in which quantum objects can exist. For instance an atom can be in a superposition of ground and next excited states with 50% probabilities. Such a state is descibred by a normalized ket. 

$$\mid \psi \rangle=c_1 \mid 1 \rangle+c_2 \mid 2\rangle$$ 

$$\langle \psi \mid \psi \rangle = \Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1\mid 1\rangle + c_2 \mid 2\rangle\Big] =\\ = \mid c_1 \mid^2 \langle 1 \mid 1 \rangle+(c^*_1 c_2\langle 1 \mid 2 \rangle+c_1 c^*_2\langle 2 \mid 1 \rangle)+\mid c_2\mid^2   = c_1^2+c^2_2=p_1+p_2=1$$

- The meaning of expectation becomes more transparent as an average over all eigenvalues obtained in the experiment. 

 $$\langle E\rangle= \langle \psi \mid \hat{H}\mid \psi \rangle = \Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1\hat{H}\mid 1\rangle + c_2 \hat{H}\mid 2\rangle\Big] =\Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1E_1\mid 1\rangle + c_2 E_2\mid 2\rangle\Big] = \\ = c_1^2E_1+c^2_2 E_2=p_1E_1+p_2 E_2$$


:::{admonition} **Example**  
:class: note

Particle in a box is described as a supperopistion of 1-st and 5-th states. 
- Write down the wavefunction in terms of Hamiltonian operators eigenfunctions.
- Compute the average energy
:::

:::{admonition} **Solution**  
:class: dropdown

$$\psi(x)=\frac{1}{\sqrt{2}}\cdot \Big(\frac{2}{L} \Big )^{1/2}sin\frac{\pi x}{L}+\frac{1}{\sqrt{2}}\cdot \Big(\frac{2}{L} \Big )^{1/2}sin\frac{5\pi x}{L}$$ 

This means that when we measure  energy we are going to obtain only two values $E_1$ and $E_5$ with equal probabilities $p_1=p_2=(1/\sqrt{2})^2$. 

The average of energy will be given by

$$\langle E \rangle =p_1 E_1+p_2 E_2 = \frac{1}{2}\frac{1^2 h^2}{8mL^2}+\frac{1}{2}\frac{5^2 h^2}{8mL^2}$$
:::



:::{admonition} **Example**  
:class: note

Consider a particle in a quantum state $\psi$ that is a superposition of two eigenfunctions $\phi_1$ and $\phi_2$, with energy eigenvalues $E_1$ and $E_2$ of operator $\hat{H}$  ($E_1 \ne E_2$):

$$\psi = c_1\phi_1 + c_2\phi_2$$

- If one attempts to measure energy of such state, what will be the outcome? 
- What will be the average energy and the standard deviation in energy?
:::

:::{admonition} **Solution**  
:class: dropdown

Since $\psi$ is normalized and $\phi_1$ and $\phi_2$ are orthogonal, we have $\left|c_1\right|^2 + \left|c_2\right|^2 = 1$. The probability of measuring $E_1$ is $\left|c_1\right|^2$ and $E_2$ is $\left|c_2\right|^2$. The average energy is given by:


$$\left<\hat{H}\right> = \left<\psi\left|\hat{H}\right|\psi\right> = \left|c_1\right|^2\left<\phi_1\left|\hat{H}\right|\phi_1\right> + c_1^*c_2\left<\phi_1\left|\hat{H}\right|\phi_2\right> + c_2^*c_1\left<\phi_2\left|\hat{H}\right|\phi_1\right>$$
$$ + \left|c_2\right|^2\left<\phi_2\left|\hat{H}\right|\phi_2\right> = \left|c_1\right|^2E_1 + c_1^*c_2E_2\underbrace{\left<\phi_1\left|\phi_2\right.\right>}_{= 0} + c_2^*c_1E_1\underbrace{\left<\phi_2\left|\phi_1\right.\right>}_{= 0} + \left|c_2\right|^2E_2$$
$$= \left|c_1\right|^2E_1 + \left|c_2\right|^2E_2$$


 The standard deviation is given by : $\sigma_{\hat{H}} = \sqrt{\left<\hat{H}^2\right> - \left<\hat{H}\right>^2}$. We have already calculated $\left<\hat{H}\right>$ above and need to calculate $\left<\hat{H}^2\right>$ (use the eigenvalue equation and orthogonality):

$$\left<\hat{H}^2\right> = \left<\psi\left|\hat{H}^2\right|\psi\right> = \left<\psi\left|\hat{H}\right|E_1c_1\phi_1 + E_2c_2\phi_2\right> = \left<c_1\phi_1 + c_2\phi_2\left|E_1^2c_1\phi_1 + E_2^2c_2\phi_2\right.\right>$$
$$ = \left|c_1\right|^2E_1^2 + \left|c_2\right|^2E_2^2 \Rightarrow \sigma_{\hat{H}} = \sqrt{\left|c_1\right|^2E_1^2 + \left|c_2\right|^2E_2^2 - \left(\left|c_1\right|^2E_1 + \left|c_2\right|^2E_2\right)^2}$$

:::



### Quantum states as linear superposition of mutually exclusive states.

It is important to emphasize that postulates of quantum mechanics that in an experimetn we always obtain one of the eigenvalues in other words the system described by a superoposition "collapses" to one of the eigenfunctions. The idea of a quantum system randomly collapsing into distinct and mutuallye esclusive states has trubled many physicsis, who were at the frontiers of development of quantum mechanics. 

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$

- Act of an exeperimentation interferes with superposition state collapsing it to a particular eigenfunction with probability $\mid c_n \mid^2$

  $$\mid \psi \rangle \rightarrow \mid \phi_n \rangle$$

- Orthogonality of eigenfunctions implies mutual exclusivity of system being in state 1 vs state 2 

  $$\langle \phi_1 \mid \phi_2 \rangle=0$$


- The [Copenhagen interpretation](https://en.wikipedia.org/wiki/Copenhagen_interpretation#cite_note-Siddiqui2017-1) is an expression of the meaning of [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics) that was largely devised from 1925 to 1927 by [Niels Bohr](https://en.wikipedia.org/wiki/Niels_Bohr) and [Werner Heisenberg](https://en.wikipedia.org/wiki/Werner_Heisenberg). It is one of the oldest of numerous proposed [interpretations of quantum mechanics](https://en.wikipedia.org/wiki/Interpretations_of_quantum_mechanics), and remains one of the most commonly taught.

- According to the Copenhagen interpretation, physical systems generally do not have definite properties prior to being measured, and quantum mechanics can only predict the probability distribution of a given measurement's possible results. 
- The act of measurement affects the system, causing the set of probabilities to reduce to only one of the possible values immediately after the measurement. This feature is known as [wave function collapse](https://en.wikipedia.org/wiki/Wave_function_collapse)."



### Quantum superopsition of atom. 

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


### Double slit Experiment

<html>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Xmq_FJd1oUQ" frameborder="0" allowfullscreen>
</iframe>
</html>



