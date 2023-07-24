## Commutability and precision of measurement


We have seen previously that operators may not always commute (i.e., $[A, B] \ne 0$). An example of such operator pair is position $\hat{x}$ and momentum $\hat{p}_x$:

$${\hat{p}_x\hat{x}\psi(x) = \hat{p}_x\left(x\psi(x)\right) = \left(\frac{\hbar}{i}\frac{d}{dx}\right)\left(x\psi(x)\right) = \frac{\hbar x}{i}\frac{d\psi(x)}{dx} + \frac{\hbar}{i}\psi(x)}$$

$${\hat{x}\hat{p}_x\psi(x) = x\left(\frac{\hbar}{i}\frac{d\psi(x)}{dx}\right)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right]\psi(x) = \left(\hat{p}_x\hat{x} - \hat{x}\hat{p}_x\right)\psi(x) = \frac{\hbar}{i}\psi(x)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right] = \frac{\hbar}{i}}$$

In contrast, the kinetic energy operator and the momentum operators commute:

$${\left[\hat{T},\hat{p}_x\right] = \left[\frac{\hat{p}_x^2}{2m},\hat{p}_x\right] = \frac{p_x^3}{2m} - \frac{p_x^3}{2m} = 0}$$

We had the uncertainty principle for the position and momentum operators:

$$\Delta x\Delta p_x \ge \frac{\hbar}{2}$$


In general, it turns out that for operators $\hat{A}$ and $\hat{B}$ that do not commute, the [uncertainty principle](http://en.wikipedia.org/wiki/Uncertainty_principle) applies in the following form:

$${\Delta A\Delta B \ge \frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right|}$$


**Example**  obtain the position/momentum uncertainty principle 

**Solution** Denote $\hat{A} = \hat{x}$ and $\hat{B} = \hat{p}_x$. 


$$\frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right| = \frac{1}{2}\left|\left<\left[\hat{x},\hat{p}_x\right]\right>\right| = \frac{1}{2}\left|\left<\frac{\hbar}{i}\right>\right|
= \frac{1}{2}\left|\left<\psi\left|\frac{\hbar}{i}\right|\psi\right>\right| = \frac{1}{2}\left|\frac{\hbar}{i}\underbrace{\left<\psi\left|\psi\right.\right>}_{=1}\right| = \frac{\hbar}{2}$$

$$\Rightarrow \Delta x\Delta p_x \ge \frac{\hbar}{2}$$



**Example** Show that if all eigenfunctions of operators $\hat{A}$ and $\hat{B}$ are identical, $\hat{A}$ and $\hat{B}$ commute with each other.

**Solution** Denote the eigenvalues of $\hat{A}$ and $\hat{B}$ by $a_i$ and $b_i$ and the common eigenfunctions by $\psi_i$. For both operators we have then:

$$\hat{A}\psi_i = a_i\psi_i\textnormal{ and }\hat{B}\psi_i = b_i\psi_i$$


By using these two equations and expressing the general wavefunction $\psi$ as a linear combination of the eigenfunctions, the commutator can be evaluated as:

$$\hat{A}\hat{B}\psi = \hat{A}\left(\hat{B}\psi\right) = \hat{A}\overbrace{\left(\hat{B}\sum\limits_{i=1}^{\infty}c_i\psi_i\right)}^{\textnormal{complete basis}}
= \hat{A}\overbrace{\left(\sum\limits_{i=1}^{\infty}c_i\hat{B}\psi_i\right)}^{\hat{B}\textnormal{ linear}} = \hat{A}\overbrace{\left(\sum\limits_{i=1}^{\infty}c_ib_i\psi_i\right)}^{\textnormal{eigenfunction of }\hat{B}}$$
$$= \overbrace{\sum\limits_{i=1}^{\infty}c_ib_i\hat{A}\psi_i}^{\hat{A}\textnormal{ linear}} = \overbrace{\sum\limits_{i=1}^{\infty}c_ib_ia_i\psi_i}^{\textnormal{eigenfunction of }\hat{A}} = \overbrace{\sum\limits_{i=1}^{\infty}c_ia_ib_i\psi_i}^{a_i\textnormal{ and }b_i\textnormal{ are constants}} = \sum\limits_{i=1}^{\infty}c_ia_i\hat{B}\psi_i$$
$$= \hat{B}\sum\limits_{i=1}^{\infty}c_ia_i\psi_i = \hat{B}\sum\limits_{i=1}^{\infty}c_i\hat{A}\psi_i = \hat{B}\hat{A}\sum\limits_{i=1}^{\infty}c_i\psi_i = \hat{B}\hat{A}\psi$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = 0$$


Note that the commutation relation must apply to all well-behaved functions and not just for some given subset of functions!


