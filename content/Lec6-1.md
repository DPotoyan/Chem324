## Outline for Lecture 6.0:  "Perturbation Method"



- Pertrubation theory is applicable when the given problem differs by some exacctly solvable model by a small amount. 

- First and second order corrections to energy suffice for solving wide range of problems in quantum mechanics.

  

  

  

## Time independent perturbations



Suppose we have hamiltonian for some exactly solvable problem (particle in a box, harmonic oscilator, etc): $\hat{H}_0$. 


$$
\hat{H}^0 \mid n^0\rangle=E^0_n \mid n^0\rangle
$$



*Note the placing of 0 index: It indicates exactly solvable hamitlonian along with eigenfunctions and eigenvalues. The  $\mid n\rangle $ is the eigenfunction corepsonding to the eigenvalue $E_n$.* <br>Suppse we modify the hamitlonian by adding a "small" pertrubation $\hat{H_1}$ how would the eigenvalues and iegenfunctions change? 


$$
\hat{H}=\hat{H}^0+\lambda \hat{H}^1 
$$



The  $\lambda$ is a covneinence constant factor which turns perturbation on $\lambda=1$ and off $\lambda=0$.  The objective of  perturbation theory is to find solutions of the following equation in terms of the exactly solvable problem plus a little pertrubation:


$$
\hat{H}\mid n\rangle =E_n \mid n\rangle
$$






### It's just like Taylor expansions! 



We assume that eigenvalues and eigenfunctions can be expanded in power series in the parameter $\lambda$ to be set to 1 in the end. 


$$
E_n =E^0_n+\lambda E^1_n+\lambda^2 E^2_n+...
$$

$$
\mid n\rangle = \mid n^0\rangle+\lambda\mid n^1\rangle+\lambda^2\mid n^2\rangle+...
$$



Plugging in thepertrubative expansion of eigneufncitons and eignvalues into schrodinger equation we get:



$$
\Big(\hat{H}^0+\lambda \hat{H}^1 \Big)\Big(\mid n^0\rangle+\lambda\mid n^1\rangle+\lambda^2\mid n^2\rangle \Big)  = \\ =\Big(E^0_n+\lambda E^1_n+\lambda^2 E^2_n \Big) \Big(\mid n^0\rangle+\lambda\mid n^1\rangle+\lambda^2\mid n^2\rangle\Big)
$$





### Petrubation equations of order 0, 1 and 2

Now if we opent he brackets and collecting different orders of $\lambda$ we obtain equations determining 0, 1st and 2nd order perturbations to eigenfunctions/eigenvalues:

 

$$
\hat{H}^0\mid n^0\rangle = E^0_n\mid n^0 \rangle
$$


$$
\hat{H}^0\mid n^1\rangle +\hat{H^1}\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle
$$


$$
\hat{H}^0\mid n^2\rangle +\hat{H^1}\mid n^1\rangle = E^0_n\mid n^2 \rangle+E^1_n\mid n^1+E^2_n\mid n^0 \rangle
$$



- Note how the sum of  upstairs index determines the order of perturbation expansion		
- Note that 0 order is just the exact solution.
- Note that hamitonian only has first order expansion while eigenfunctions and eigenvalues are expanded to infinite terms. Usually going to second order is enough for most problems. 





###  Fixing the normalization

If we have normalization the zero order eigenfunctions will be orthogonal to all higher order ones


$$
\langle n^0 \mid n^0 \rangle=1
$$


$$
\langle n^0\mid n\rangle = \langle n^0\mid n^0\rangle + \lambda\langle n^0\mid n^1\rangle+\lambda^2\langle n^0\mid n^2\rangle=1+0+0+...
$$

$$
\langle n^0 \mid n^{k} \rangle=0\,\,\, k=1,2,..
$$





### 1st order correction 



$$
\hat{H}^0\mid n^1\rangle +\hat{H^1}\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle
$$



Using the orthogonality we now multiply  first order pertrubation equation by $\langle n^0 \mid$



$$
\langle n^0 \mid \hat{H}^0\mid n^1\rangle +\langle n^0 \mid  \hat{H^1}\mid n^0\rangle = E^0_n\langle n^0 \mid n^1 \rangle+E^1_n \langle n^0 \mid n^0 \rangle
$$



First term on left is zero by using hermitian property of the hamiltonian and orthogonality

 

$$
\langle n^0 \mid \hat{H}^0\mid n^1\rangle = \langle n^1 \mid \hat{H}^0\mid n^0\rangle^* = E^0_n \langle n^1 \mid n^0\rangle^* = 0
$$



The first terms on the right is zero becasue of rothogonality. We now have the most important expression of pertrubation theory 1st order correction to energy: 



$$
E^1_n =\langle n^0 \mid \hat{H}^1\mid n^0 \rangle
$$




- Note that this give *first order correction* to the energy $E_n=E^0_n+E^1_n$

- Note that this is different from expectation expression. Here eigenfunctions of $\hat{H}^0$ sandwich the the pertrubation hamitlonian $\hat{H}^1$ . The two hamitlonians in general do not have to share eigenfunctions!

   



### 2nd order correction 

Again we take advantage of orthogonality and now  multiply  second order pertrubation equation by $\langle n^0 \mid$ getting:


$$
E^2_n = \langle n^0 \mid \hat{H}^1 \mid n^1 \rangle
$$


We express unknown first order eigenfunctions $\mid n^1 \rangle$ in terms of known eigenfunctions. This is done by by the virtue of  $\mid k^0\rangle $ forming complete basis set in terms of which one can express any function:



$$
\mid n^1 \rangle = \sum_{k \neq n} c_k \mid k^0 \rangle
$$



with $c_k =\langle k^0 \mid n^1 \rangle$ hence the $k\neq n$ in the sum indicating that $c_n=0$. Next we express coefficients in terms of exact eigenfunctions:

$$
c_k (E^0_n-E^0_k) = \langle k^0 \mid \hat{H}^1 \mid n^0 \rangle =H_{nk} \\ 

\mid n^1\rangle = \sum_{k \neq n} \frac{H_{nk}}{(E^0_n-E^0_k)} \mid n^0 \rangle
$$



Where we have introduced a notation for matrix elements of perturbation hamitlonian $H_{nk}=H_{kn} = \langle k^0 \mid \hat{H}^1 \mid n^0 \rangle$. Plugging the above expansion into second order correction we obtain the key result for 2nd order pertrubation:



$$
E^2_n = \sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}
$$




- Note that this is the  *second order correction* to the energy $E_n=E^0_n+E^1_n+E^2_n$
- The energy in the denominator is the difference between energy of a given state $E_n$ from all other states $E_k$ with k being the summation index.
- For the ground state the second order correction thereofre will always be negative because $\Delta E_{0k}=E_0-E_k<0$. 
- If the matrix elements of $ \hat{H}^1$ are of comparable magnitude the neighbouring levels make larger contributions that distance levels.



## Putting everything together

Using the convenient notaiton for matrix elements of pertrubation hamiltonian we have the qst and second roder perturbations to the energy level $E_n$


$$
E_n = E^0_n+ H_{nn} + \sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}
$$


Writing the correction exlicitely for the ground state


$$
E_0 =E^0_0+ H_{00} + \frac{\mid H_{01}\mid^2}{E^0_0-E^0_1}+\frac{\mid H_{02}\mid^2}{E^0_0-E^0_2}+ ...
$$


## Applications




### Example-1: magnetic field





### Example-2: electric field





### Exaple-3 unharmonic oscillator






