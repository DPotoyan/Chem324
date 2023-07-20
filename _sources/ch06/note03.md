## Linear variational method


$$
\phi = \sum_i c_i f_i
$$

- $c_i$ -Variational coefficients
- $f_i$ Trial functions
- Example: $\phi(x) = c_1 sin (2x)+c_2 sin(2x)$


### Minimizing energy by varying linear coefficients

$$
\mid \phi \rangle = \sum_i c_i \mid f_i \rangle
$$

$$
E(c_1,c_2,...c_N) = \frac{\langle \phi \mid \hat{H} \mid \phi \rangle}{\langle\phi \mid \phi \rangle}
$$

$$
E(c_1,c_2,...c_N) = \frac{\sum_i \sum_j c_i c_j\langle f_i \mid \hat{H} \mid f_j \rangle}{\sum_i \sum_j c_i c_j\langle f_i \mid f_j \rangle} = \frac{\sum_i \sum_j H_{ij}}{\sum_i \sum_j c_i c_jS_{ij}}
$$



### It's a linear algebra problem

$$\mid \phi\rangle = c_1\mid f_1\rangle+ c_1\mid f_2\rangle$$

$$E(c_1,c_2) = \langle \phi \mid \hat{H} \mid \phi \rangle $$

Minimizing $E(c_1,c_2)$ with respect to ($c_1$,$c_2$) gives rise 2 linear equations.

$$
c_1(H_{11}-ES_{11})+c_2(H_{11}-ES_{12}) = 0 \newline
c_1(H_{21}-ES_{21})+c_2(H_{21}-ES_{22}) = 0
$$

The set of linear equations has nontrivial solution only when determinant of matrix elements is zero:

$$
\begin{vmatrix}
H_{11}-ES_{11} & H_{12}-ES_{12}  \\
H_{21}-ES_{21} & H_{22}-ES_{22}  \\
\end{vmatrix} = 0
$$



### Determinant for  N trial functions

Variational minimization of coeffients of  N trial functions $(c_1, c_2,...c_N)$ leads to an N by N determinant:

$$
\mid \phi \rangle = \sum_i c_i \mid f_i \rangle
$$

$$
\begin{vmatrix}
H_{11}-ES_{11} & H_{12}-ES_{12}  & \dots & H_{1N}-ES_{1N} \\
H_{21}-ES_{21} & H_{22}-ES_{22}  & \dots & H_{2N}-ES_{2N} \\
H_{31}-ES_{31} & H_{32}-ES_{32}  & \dots & H_{3N}-ES_{3N}  \\
\dots & \dots & \dots & \dots \\
H_{N1}-ES_{11} & H_{N2}-ES_{N2}  & \dots & H_{NN}-ES_{NN}
\end{vmatrix} = 0
$$