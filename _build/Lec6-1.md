---
redirect_from:
  - "/lec6-1"
title: '6.1 Perturbation Theory'
prev_page:
  url: /Lec6-0
  title: '6.0 Approximation methods of QM'
next_page:
  url: /Lec6-2
  title: '6.2 Variation Method'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Outline for Lecture 6.0:  "Perturbation Method"



- Pertrubation theory is applicable when the given problem differs by some exacctly solvable model by a small amount. 

  

  

  

## Time independent perturbation theory



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






### Perturbation theory: It's just like Taylor expansions! 



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



### 1st order correction to Eigenvalues/Eigenfunctions



$$
\hat{H}^0\mid n^1\rangle +\hat{H^1}\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle
$$



Using this orthogonality we now multiplu  first order pertrubation equation by $\langle n^0 \mid$


$$
\langle n^0 \mid \hat{H}^0\mid n^1\rangle +\langle n^0 \mid  \hat{H^1}\mid n^0\rangle = E^0_n\langle n^0 \mid n^1 \rangle+E^1_n \langle n^0 \mid n^0 \rangle
$$



First term on left is zero by using hermitian property of the hamiltonian and orthogonality

 

$$
\langle n^0 \mid \hat{H}^0\mid n^1\rangle = \langle n^1 \mid \hat{H}^0\mid n^0\rangle^* = E^0_n \langle n^1 \mid n^0\rangle^* = 0
$$



The first terms on the right is zero becasue of rothogonality which results in the most important expression of pertrubation theory 1st order correction to energy: 


$$
E^1_n =\langle n^0 \mid \hat{H}^1\mid n^0 \rangle
$$






- Note that this give *first order correction* to the energy $E_n=E^0_n+E^1_n$

- Note that this is different from expectation expression. Here eigenfunctions of $\hat{H}^0$ sandwich the the pertrubation hamitlonian $\hat{H}^1$ . The two hamitlonians in general do not have to share eigenfunctions!

   


### 2nd order correction to Eigenvalues/Eigenfunctions






## Applications




### Example-1: magnetic field





### Example-2: electric field





### Exaple-3 unharmonic oscillator






