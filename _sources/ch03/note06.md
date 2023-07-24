## Time dependence


### Time dependence of a wave function

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
