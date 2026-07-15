---
kernelspec:
  name: python3
  display_name: Python 3
---

# NumPy

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
  ]
---
```

```{marimo} python
:hide-code: true

import numpy as np
```

**What is numpy?**

- NumPy is the core python library for numerical and scientific computing. 
- A numpy array is a grid of values, all of the same type, and is indexed by nonnegative integers. 
- The array can have any number of dimensions 1D, 2D, 3D, ...
- The shape of an array is a tuple of integers giving the size of the array along each dimension. For example a 1D vector of size 4 is (4,). a matrix of size 2 is (2,2), a matrix with size 2x5 is (2,5) 

- Numpy arrays can be generates either by feeding lists to numpy or on the fly using numpy special methods

**Additional resources to learn numpy**

- [numpy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [RealPython numpy tutorial](https://realpython.com/numpy-tutorial/)

```{code-cell} python
# To use numpy you have to first import it
import numpy as np
print(np.__version__)
```

### Array Creation

### Generating numpy arrays from lists

```{code-cell} python
data=np.array([1,2,3])
data
```

```{code-cell} python
data.shape
```

![](images/numpy1.png)

```{code-cell} python
print(data[0], data[1], data[2])
data[0] = 10                 # Change an element of the array
print(data)
```

```{code-cell} python
b = np.array([[1,2,3],[4,5,6]])   # Create a 2D array
print(b)
```

```{code-cell} python
print(b.shape)                    
print(b[0, 0], b[0, 1], b[1, 0])
```

```{code-cell} python
# Question: what does this do?
np.array( [ x**2 for x in range(100) if x%3==0 ])
```

### Array vs list cration: which is faster?

Jupyter notebooks have a nice built-in method to time how long a line of code takes to execute. In a Jupyter notebook, when a line starts with ```%timeit``` followed by code, the kernel runs the line of code multiple times and outputs an average of the time spent to execute the line of code.

We can use ```%timit``` to compare a mathematical operation on a Python list using a for loop to the same mathematical operation on a NumPy array.

```{code-cell} python
lst = list(range(10000))
%timeit for i, item in enumerate(lst): lst[i] = lst[i]*2
```

```{code-cell} python
nparray = np.arange(0,10000,1)
%timeit 2*nparray
```

With 10,000 integers, the Python list and for loop takes an average of single milliseconds, while the NumPy array completes the same operation in tens of microseconds. This is a speed increase of over 100x by using the NumPy array (1 millisecond = 1000 microseconds).

For larger lists of numbers, the speed increase using NumPy is considerable.

### Generating arrays using special methods

![](images/numpy2.png)

```{code-cell} python
a = np.zeros((5,8))  # Create an array of all zeros
print(a)
```

```{code-cell} python
b = np.ones((1,5))   # Create an array of all ones
print(b) 
```

```{code-cell} python
e = np.random.random((4,4)) # Create an array filled with random values
print(e)
```

```{code-cell} python
x = np.linspace(1,100,10) # create an array between 1 and 100 divided by 10 segments
print(x)
```

```{code-cell} python
y = np.arange(1,100,5) # create an array strting from 1 to 100 in 10 incremenets
print(y)
```

```{code-cell} python
c = np.full((2,2), 7.5) # Create a constant array
print(c)  
```

```{code-cell} python
d = np.eye(5)        # Create a 3x3 identity matrix
print(d) 
```

```{code-cell} python
k = np.tile(d,3)  # repeat the array d 3 times
k
```

### Common array creation methods 

| Function | Description |
| --- | --- |
| ```np.array([list, of, numbers])``` | Array from a list |
| ```np.arange(start, stop, step)``` | Array with know step |
| ```np.linspace(start, stop, num)``` | Creates an array from [start, stop] with num number of steps |
| ```np.logspace(start, stop, num)``` | Same but on log scale |
|```np.zeros((rows, cols))``` | Array of zeros |
| ```np.ones((rows, cols))``` | Array of ones |
| ```np.meshgrid(array1, array2)``` | Two 2D arrays from two 1D arrays  |

### Common array creation methods involving random numbers

| Function | Description | 
|:-------: |:----------- |
|`np.rand()`  | Generates random floats in the range \[0,1) in an even distribution |
|`np.randint()` | Generates random integers from a given range in an even distributionb |
|`np.randn()` | Generates random floats in a normal distribution centered around zero |
|`np.binomial()` | Generates random integers in a binomial distribution; takes a probability ,`p`, and `size` artuments |
|`np.poisson()` | Generates random floats in a Poisson distribution; takes a target mean argument (`p`)  |
|`np.choice()` | Selects random values taken from a 1-D array or range |
|`np.shuffle()` | Randomizes the order of an array |

### Indexing, slicing and shaping arrays

**Slicing:** Similar to Python lists, numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each dimension of the array:

```{code-cell} python
data=np.array([1,2,3])
data[0:3]
```

![](images/numpy_index.png)

```{code-cell} python
data = np.array([[1,3,5], [2,4,6]])
data.T
```

![](images/numpy-matrix-indexing.png)

```{code-cell} python
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
a.shape
```

```{code-cell} python
a.shape
```

```{code-cell} python
a[1,:4]  #
```

```{code-cell} python
a[1,3]
```

```{code-cell} python
a[:,-1] # last column
```

```{code-cell} python
a[-1,:] # last row
```

**Same principles of slicing and shapes applies to the N-dimensional arrays.**

![](images/numpy_3d.png)

```{marimo} python
:editor: true

m = np.arange(1, 26).reshape(5, 5)   # np is already imported on this page
m[1:4, ::2]   # predict the result before running
```

### Vectorized operations with numpy

Basic mathematical functions operate **elementwise on arrays**, and are available both as operator overloads and as functions in the numpy module:

```{code-cell} python
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
```

```{code-cell} python
# Elementwise sum; both produce the array
print(x + y) 
```

```{code-cell} python
# Elementwise difference; both produce the array
print(x - y)  
```

```{code-cell} python
# Elementwise product; both produce the array
print(x * y) 
```

```{code-cell} python
print(x / y) 
```

```{code-cell} python
print(np.sqrt(x)) 
```

```{code-cell} python
1.5*x  # elementwise multiplication!
```

```{code-cell} python
y+3    # elementwise addition. 
```

As last two examples show can also do operations on arrays with unequal shapes! These are powerful operations which follow set of rules called **broadcasting.** See the end for these rules and examples

**To use vector,matrix dot product between A and B use A@B**

```{code-cell} python
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v@w) 
```

```{code-cell} python
# Matrix / vector product; both produce the rank 1 array [29 67]
print(x@v) 
```

```{code-cell} python
# Matrix / matrix product; both produce the rank 2 array
print(x@y) 
```

### Aggregation

Numpy provides many useful functions for performing computations on arrays; one of the most useful is `sum`:

```{code-cell} python
x = np.array([[1,2],[3,4]])
np.sum(x,axis=1)
```

```{code-cell} python
print(np.sum(x))   # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))   # Compute sum of each row; prints "[3 7]"
```

```{code-cell} python
print(x.max())
print(x.min())
```

### Reshaping arrays

```{code-cell} python
x=np.array([1,2,3,4,5,6,7,8,9,10])
```

```{code-cell} python
x=x.reshape(2,5)
x
```

```{code-cell} python
x=x.reshape(5,2)
x
```

```{code-cell} python
# transpose matrix
x.T 
```

```{code-cell} python
# add an empty dimension
y = np.arange(3)

print(y.shape)

z = y[:, np.newaxis]

print(z.shape)
print(z)
```

### Broadcasting rules of numpy arrays

Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array. 

The rules of broadcasting are:

- **Rule 1:** If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
- **Rule 2:** If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
- **Rule 3:** If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

![](images/numpy-matrix-broadcast.png)

**Examples of broadcasting**

```{code-cell} python
data     = np.array([[1,2],[3,4],[5,6]])
ones_row = np.array([1,1])
data.shape, ones_row.shape
```

```{code-cell} python
data
```

```{code-cell} python
ones_row
```

```{code-cell} python
data.shape, ones_row.shape
```

```{code-cell} python
data+ones_row
```

**Let us see both rules in action on another example**

```{code-cell} python
a = np.arange(3).reshape((3, 1))
print(a)
print(a.shape)
```

```{code-cell} python
b = np.arange(3)
print(b)
print(b.shape)
```

Lets predict a+b sum. By first rule the sum of arrays with shapes **(3,1)+(3,)** are broadcast to **(3,1)+(1,3)** then by second rule dimensions one are padded to match the shape **(3,3)+(3,3)**

```{code-cell} python
a+b 
```

**numpy application example**
```
Calculate the sinc function: sin(r)/r.  Use a Cartesian x,y grid
and calculate ``r = sqrt(x**2+y**2)`` with 0 in the center of the grid.
Calculate the function for -15,15 for both x and y.
```

```{marimo} python
:editor: true

counts = np.random.default_rng(11).integers(0, 100, size=(4, 6))
counts.mean(axis=0).round(1)   # try axis=1, .max(), .argsort()
```

### Quick plots: visualizing your arrays

Numbers in an array are hard to read; a picture is not. A handful of matplotlib patterns cover almost everything in this course: a line plot for a function, several curves with a legend, a scatter of points, and a histogram of samples. Import `matplotlib.pyplot` once and reuse it.

```{code-cell} python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
plt.plot(x, np.sin(x))
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("A line plot of an array")
```

For anything beyond a single curve it is cleaner to create `fig` and `ax` objects: `ax` styles the plot, `fig` holds the whole figure. Multiple curves plus a legend:

```{code-cell} python
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(x, np.sin(x), label="sin")
ax.plot(x, np.cos(x), label="cos")
ax.set_xlabel("x")
ax.set_ylabel("value")
ax.legend()
```

Scatter plots show individual points (useful for noisy data), and histograms show how samples are distributed, the picture behind every probability density in quantum mechanics:

```{code-cell} python
rng = np.random.default_rng(0)
noisy = np.sin(x) + 0.15 * rng.standard_normal(x.size)
samples = rng.normal(0.0, 1.0, 1000)

fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].scatter(x, noisy, s=8)
ax[0].set_title("scatter of noisy points")
ax[1].hist(samples, bins=30)
ax[1].set_title("histogram of 1000 samples")
fig.tight_layout()
```

That trio (line, scatter, histogram) is enough to visualize essentially every array you will build in this course. For a wider gallery see the [Matplotlib examples](https://matplotlib.org/stable/gallery/index.html).

### Pandas

You may thinkg of numpy as enhancing functionality of lists for numerical computations. In the same vein you can think of pandas as enahcnign dicitonaires to deal with heteogenuous categorical data. 

Pandas is widely used by data analysts from all disciplines to carry out rapid data cleaning, statistical analysis and plotting. The DataFrame is the ore object of pandas whihc stores observables as columns whith rows indicating measurments or samples. Lets create an example

```{code-cell} python
import pandas as pd
import numpy as np
```

```{code-cell} python
A = pd.DataFrame({'Time': [1,2,3,4,5],
                 'Energy': [10,20,30,40,50]
                 })
```

```{code-cell} python
A
```

```{code-cell} python
A['velocity'] = np.zeros(5)
```

```{code-cell} python
A.columns
```

```{code-cell} python
A.index
```

```{code-cell} python
# acess underlying values as numpy arrays
A['Energy'].values
```

### Exercises

**1. Predict and explain the following statements**

1. Create an array of the numbers ```1```, ```5```, ```19```, ```30```

2. Create an array of the numbers ```-3```, ```15```,```0.001```, ```6.02e23```

3. Create an array of integers between -10 and 10

4. Create an array of 10 equally spaced angles between 0 and $2\pi$

5. Create an array of logarithmically spaced numbers between 1 and 1 million. Hint: remember to pass exponents to the ```np.logspace()``` function.

6. Create an array of 20 random integers between 1 and 10

7. Create an array of 30 random numbers with a normal distribution

8. Predict the outcome of the following operation between two NumPy arrays. Test your your prediction.

    $$ \left[ \begin{array}{cc} 1 & 1 \\ 2 & 2 \end{array} \right] + \left[1 \right] = \,\, ?$$

9. Predict the outcome of the following operation between two NumPy arrays. Test your your prediction.

    $$ \left[ \begin{array}{ccc} 1 & 8 & 9 \\ 8 & 1 & 9 \\ 1 & 8 & 1 \end{array} \right] + \left[  \begin{array}{cc} 1     & 1 \\ 1 & 1 \end{array} \right] = \,\, ? $$

10. Predict the outcome of the following operation between two NumPy arrays. Test your your prediction.

    $$ \left[ \begin{array}{cc} 1 & 8 \\ 3 & 2 \end{array} \right] + 
    \left[ \begin{array}{cc} 1 & 1 \\ 1 & 1 \end{array} \right] = \,\, ?$$
```

**2. Array Manipulation**

1. Create an array ```B``` that contains integers 0 to 24 (including 24) in one row.  Then reshape ```B``` into a 5 row by 5 column array

2. Extract the 2nd row from ```B```.  Store it as a one column array called ```x```.

3. Store the number of elements in array ```x``` in a new variable called ```y```. 

4. Extract the last column of ```B``` and store it in an array called ```z```.  

5. Store a transposed version of ```B``` in an array called ```t```.

**3. Arrray slicing**

1. The 1D NumPy array ```G``` is defined below.  But your code should work with any 1D NumPy array filled with numeric values.

```G = np.array([5, -4.7, 99, 50, 6, -1, 0, 50, -78, 27, 10])```

- Select all of the positive numbers in ```G``` and store them in ```x```.

- Select all the numbers in ```G``` between ```0``` and  ```30``` and store them in ```y```.

- Select all of the numbers in ```G``` that are either less than ```-50``` or greater than ```50``` and store them in ```z```.

2. Generate a one-dimensional array with the following code and index the 5th element of the array.

    ```python
    arr = np.random.randint(0, high=10, size=10)
    ```
    
3. Generate a two-dimensional array with the following code.
    
    ```python
    arr2 = np.random.randint(0, high=10, size=15).reshape(5, 3)
    ```
    
    a. Index the second element of the third column.
    
    b. Slice the array to get the entire third row.
    
    c. Slice the array to access the entire first column.
    
    d. Slice the array to get the last two elements of the first row.

```

**4. random numbers**
    
1. For the following randomly-generated array:
    
    ```python
    arr = np.random.rand(20)
    ```
    
    a. Find the *index* of the largest values in the following array.

    b. Calculate the mean value of the array.
    
    c. Calculate the cumulative sum of the array.

    d. Sort the array.

2. Generate a random array of values from -1 $\rightarrow$ 1 (exclusive) and calculate its median value. Hint: start with an array of values 0 $\rightarrow$ 1 (exclusive) and manipulate it.

3. Generate a random array of integers from 0 $\rightarrow$ 35 (inclusive) and then sort it.

4. Hydrogen nuclei can have a spin of +1/2 and -1/2 and occur in approximately a 1:1 ratio. Simulate the number of +1/2 hydrogen nuclei in a molecule of six hydrogen atoms and plot the distribution. Hint: being that there are two possible outcomes, this can be simulated using a *binomial distribution*. 

**Generating an Combining arrays - Bohr hydrogen atom.**

a. Create an array containing the principle quantum numbers (n) for the first eight orbits of a hydrogen atom  (e.i., 1 $\rightarrow$ 8).
b. Generate a second array containing the energy (J) of each orbit in part A for a Bohr model of a hydrogen atom   using the equation $E = -2.18 \times 10^{-18}J (\frac{1}{n^2} )$
c. Combine the two arrays from parts A and B into a new 8 $\times$ 2 array with the first column containing the principle quantum numbers and the second containing the energies.
d. Compute transition energies as a function of quantum number separation and make a plot

### Try it live

:::{tip}
Edit this cell in your browser and press play. The last line is displayed: experiment with shapes, slicing, and broadcasting.
:::


```{marimo} python
:editor: true

arr = np.arange(12).reshape(3, 4)
row_means = arr.mean(axis=1)
arr - row_means[:, np.newaxis]   # broadcasting in action: try axis=0
```
