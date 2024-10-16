## P3 Eigenvalues

:::{admonition} **What you need to know**
:class: note


- Learning the abstract mathematical formalism brings simplicity, unity and clairty to the relationships in quantum mechanisms. 
- Concepts of **basis set, orthogonality, linear superpositions**  underly logic of quantum mechanics. 
- **Dirac notation** liberates you from explicit and awkward looking coordinate representations which may obscure the underlying picture. 
- **Schrödinger's cat** and the **double slit experiments** are explained using quantum superpsoition of orthognal states. 
:::

### Reminer: Eigenfuncton-eigenvalue problem


$${\hat{A}\psi_n = A_n\psi_n}$$

- This is an eigenvalue problem solution of which yields $n = 1,2,3,...$ number of eigenfunctions $\psi_n$ and the eigenvalues $E_i$. Depending on boundary conditions there could be finite or infinite number of solutions. 

:::{admonition} **Example: find eigenvalues and eigenfunctions of momentum operator** 
:class: note

What are the eigenfunctions and eigenvalues of an operator $\hat{p_x} = -i\hbar d/dx$
:::

:::{admonition}  **Solution**
:class: dropdown

$$\hat{p} f = p f $$

$$-i\hbar \frac{df}{dx} = p$$

Lets use the only trick we knowwhen solving ODEs $f=e^{kx}$

$$-i\hbar k = p\rightarrow k=\frac{ip}{\hbar}$$

$$f = e^{ipx/\hbar}$$

- Periodic plane waves are the eigenfunctions of momentum!

:::

**For operators written in matrix form**

- In applied numerical work operators are converted into matrices and one solves eigenvalue-eigenfunction problem of finding eigenvectors $v$ and eigenvalues $\lambda$. 
- For matri with $N$ dimensions there may be at most $N$ eigenvalues!

$$Av = \lambda v$$

:::{admonition} **Example: finding eigenvalues of a matrix** 
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

````{admonition} **Solving eignefunction eigenvalue problems numerically**
:class: note, dropdown

```python
import numpy as np

# Define the matrix
matrix = np.array([ [1, 2], 
                    [2, 4]   ] )

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Display the eigenvalues and eigenvectors
eigenvalues, eigenvectors
```

````



### Eigenfunctions of Hermitian operators form complete basis set


::::{grid}
:gutter: 2

:::{grid-item-card} Integral Notation

$\int \phi^* \hat{H}\psi dx = \int \psi (\hat{H}\phi)^*dx$

:::

:::{grid-item-card} Dirac Notation

$\langle \phi \mid \hat{H} \mid \psi \rangle = \langle \psi \mid \hat{H}\mid \phi \rangle^*$

:::

::::

The three crucial consequences of Hermitian property of operators:

- **Eigenvalues are real**: 

$$\hat{H} \mid \psi_n \rangle=E_n \mid \psi_n \rangle$$

$$E_n=E^*_n$$

- **Eigenfunctions are orthogonal** 

$$\langle \psi_n \mid  \psi_m\rangle=\delta_{nm}$$

- **Eigenfunctions form a complete basis set!**

$$\mid f\rangle = \sum_i c_i \mid \psi_i \rangle$$

- The last two properties imply that eigenfunctions of Hermitian opeartors  play the same role for functions as the unit vectors for  vectors.  
- Thus a wavefunction can be expressed in terms of the eigenfunctions of an opearators which can act on the function.

### Wave function as a linear superoposition of eigenfunctions

- We can express wavefunctions $\mid \psi \rangle$ describign states of quantum object in terms of superpsoition of **any eigenfunctions of Hermtian operators** be in energy momentum, position or other operators. 

$$\hat{A}\mid \phi_n \rangle = A_n \mid \phi_n \rangle$$

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$

- Here is an example of expressiing wavefunction for particle in a box in terms fo energy eigenfuntions. 

::::{grid}
:gutter: 2

:::{grid-item-card} Integral Notation

$$\psi=\sum_n c_n \mid n\rangle$$

$$c_n = \braket{n \mid \psi}$$

:::

:::{grid-item-card} Dirac Notation

$$\psi(x) = \sum_n c_n \Big(\frac{2}{L}\Big )^{1/2} sin \Big (\frac{n\pi x}{L} \Big )$$

$$c_k = \Big(\frac{2}{L}\Big )^{1/2} \int sin \Big (\frac{k\pi x}{L} \Big )\psi(x) dx$$
:::

::::


### Probabilistic meaning of linear superposition

:::{admonition} **Coefficients describe probability of observing distinct states**

- Wavefunction can be written as linear superposition of eigenfunctions any QM operator $\hat{A}$.

$$|\psi\rangle  = \sum_n c_n |\phi_n\rangle $$

- Absolue values of coeficients $\mid c_n \mid^2$ are equal to probabilities $p_n$ of finding system in a state $n$ described by eigenvalue $A_n$ and eigenfunction $\mid \phi_n \rangle$ of the operator $\hat{A}$.

$$p_n=\mid c_n \mid^2$$

$$\sum_n \mid c_n \mid^2 =\sum_n p_n=1$$


### Averages are probability weighted sums of eigenvalues.

- Quantum objects an exist in any supersposition states. For instance an atom can be in a superposition of ground and next excited states with 50% probabilities. 

- From normalization condition imposed on wavfunction we see the true meaning of coeficients in linear superopositions

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

- This means that when we measure  energy we are going to obtain only two values $E_1$ and $E_5$ with equal probabilities $p_1=p_2=(1/\sqrt{2})^2$. The average of energy will be given by

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

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$

- In an experimetn one always obtain one of the eigenvalues (see Postulates) corresponding to $\phi_n$

- In other words the system described by a **wavefunction of superoposition "collapses" to one of the eigenfunctions** when experiment is carried out. 

  $$\mid \psi \rangle \rightarrow \mid \phi_n \rangle$$

- In experiments on only observes different eigenvalues with probability given by squared coefficients: $\mid c_n \mid^2$

- The idea of a quantum system randomly collapsing into distinct and mutuallye esclusive states has trubled many physicsis, who were at the frontiers of development of quantum mechanics. 

- **Orthogonal of eigenfunctions** means **mutually exclusive** states. E.g system can only be in either state 1 or 2 but not both.

  $$\langle \phi_1 \mid \phi_2 \rangle=0$$


### Copenhagen Interpretation

- The [Copenhagen interpretation](https://en.wikipedia.org/wiki/Copenhagen_interpretation#cite_note-Siddiqui2017-1) is an expression of the meaning of [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics) that was largely devised from 1925 to 1927 by [Niels Bohr](https://en.wikipedia.org/wiki/Niels_Bohr) and [Werner Heisenberg](https://en.wikipedia.org/wiki/Werner_Heisenberg). It is one of the oldest of numerous proposed [interpretations of quantum mechanics](https://en.wikipedia.org/wiki/Interpretations_of_quantum_mechanics), and remains one of the most commonly taught.

- According to the Copenhagen interpretation, physical systems generally do not have definite properties prior to being measured, and quantum mechanics can only predict the probability distribution of a given measurement's possible results. 
- The act of measurement affects the system, causing the set of probabilities to reduce to only one of the possible values immediately after the measurement. This feature is known as [wave function collapse](https://en.wikipedia.org/wiki/Wave_function_collapse)."



### Quantum superopsition of atom. 

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/7B1llCxVdkE" frameborder="0" allowfullscreen>
</iframe>
</html>


### Schordinger's cat

- Schrödinger created a thought experiment to illustrate bizarre nature of quantum superpositions, in which a quantum system such as an atom or photon can exist as a combination of multiple states corresponding to different possible outcomes. 

- The thought Experiment puts cat in a box with a single radioactive atom whose state dictates weather it decays thereby breaking the poisonous chamber in the box that kills the cat or does not decay and cat stays alive. So Schrodinger argued kitty must be thought of simultaneously dead and alive until experiment is done and cat is found in one of the two states. 

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/UjaAxUO6-Uw" frameborder="0" allowfullscreen>
</iframe>
</html>


### Double slit Experiment

<html>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Xmq_FJd1oUQ" frameborder="0" allowfullscreen>
</iframe>
</html>



