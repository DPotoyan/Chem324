---
kernelspec:
  name: python3
  display_name: Python 3
---

# Application: Hopfield Neural Networks

:::{note} **What you will learn**

- **A Hopfield network as linear algebra in action.** Neurons are a state vector $\mathbf{s}$, connections are a weight matrix $W$, and updates are matrix-vector products.
- **The update rule.** Each neuron flips its state based on the sign of the weighted sum of its inputs, $h_i = (W\mathbf{s})_i$.
- **Energy minimization.** The network evolves to minimize an energy function $E = -\tfrac{1}{2}\mathbf{s}^T W \mathbf{s}$, settling into a stored pattern.
- **Associative memory.** This is how the network recalls a complete pattern from noisy or partial input.
:::

A **Hopfield network** is a type of recurrent neural network where all neurons are connected to each other. It is commonly used for **associative memory**: storing and recalling patterns. The network evolves to a stable state, recalling a stored pattern when given noisy or incomplete input. We can understand its behavior using matrix and vector operations.

### Components of a Hopfield network

1. **Neurons (States)**:
   Each neuron has a binary state, either $1$ (active) or $-1$ (inactive). The state of all neurons is represented by a vector $\mathbf{s}$. For a network of 3 neurons, the state vector might be:

   $$
   \mathbf{s} = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}
   $$

2. **Weights (Connections)**:
   Neurons are connected by weights, represented by a symmetric matrix $W$. For a 3-neuron network, the weight matrix might look like:

   $$
   W = \begin{pmatrix}
   0 & w_{12} & w_{13} \\
   w_{21} & 0 & w_{23} \\
   w_{31} & w_{32} & 0
   \end{pmatrix}
   $$

   The diagonal elements are zero because a neuron does not connect to itself.

3. **Update Rule**:
   To update the state of neuron $i$, we calculate the weighted sum of inputs from all other neurons:

   $$
   h_i = \sum_{j} w_{ij} s_j = (W \mathbf{s})_i
   $$

   If $h_i > 0$, the neuron becomes active ($s_i = 1$). If $h_i < 0$, the neuron becomes inactive ($s_i = -1$).

### Example: A simple Hopfield network

Let us consider a 3-neuron Hopfield network with the following weight matrix:

$$
W = \begin{pmatrix}
0 & 1 & -1 \\
1 & 0 & 1 \\
-1 & 1 & 0
\end{pmatrix}
$$

**Initial State**

Assume the initial state of the network is:

$$
\mathbf{s} = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}
$$

**Update Neurons**

We update each neuron based on the weighted inputs:

1. **Neuron 1**:
   The input to neuron 1 is:

   $$
   h_1 = W_{11}s_1 + W_{12}s_2 + W_{13}s_3 = 0 \cdot 1 + 1 \cdot (-1) + (-1) \cdot 1 = -2
   $$

   Since $h_1 < 0$, the new state of neuron 1 is $s_1 = -1$.

2. **Neuron 2**:
   The input to neuron 2 is:

   $$
   h_2 = W_{21}s_1 + W_{22}s_2 + W_{23}s_3 = 1 \cdot 1 + 0 \cdot (-1) + 1 \cdot 1 = 2
   $$

   Since $h_2 > 0$, the new state of neuron 2 is $s_2 = 1$.

3. **Neuron 3**:
   The input to neuron 3 is:

   $$
   h_3 = W_{31}s_1 + W_{32}s_2 + W_{33}s_3 = (-1) \cdot 1 + 1 \cdot (-1) + 0 \cdot 1 = -2
   $$

   Since $h_3 < 0$, the new state of neuron 3 is $s_3 = -1$.

**New State**

After one round of updates, the new state of the network is:

$$
\mathbf{s} = \begin{pmatrix} -1 \\ 1 \\ -1 \end{pmatrix}
$$

### Storing patterns and energy

A Hopfield network stores specific patterns by adjusting the weights, and it evolves to minimize its **energy**. The energy of the network is defined as:

$$
E = -\frac{1}{2} \sum_{i,j} w_{ij} s_i s_j = -\frac{1}{2} \mathbf{s}^T W \mathbf{s}
$$

As the network updates, it reduces its energy until it reaches a stable state, which corresponds to one of the stored patterns.

### Summary

- **Neurons** are represented by a state vector $\mathbf{s}$.
- **Weights** between neurons are represented by a matrix $W$.
- Neurons update their states based on the weighted sum of inputs, which is a matrix-vector multiplication.
- The network evolves to stable patterns by minimizing its energy function.

This is a basic introduction to the Hopfield network using matrix and vector operations.
</content>
