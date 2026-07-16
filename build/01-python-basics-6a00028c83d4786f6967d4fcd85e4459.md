---
kernelspec:
  name: python3
  display_name: Python 3
---

# Python Basics

[![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/appendix-python-basics.ipynb)






```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = []
---
```

```{image} images/py-popular2.png
:class: bg-primary mb-1
:width: 400px
:align: center
```

**What is so special about python**

- Python code is very intutive and human readable. It allows you to express very powerful ideas in very few lines of code while being very readable. 
- Python is a high-level, dynamically-typed, multiparadigm programming language. 
- What makes python special for STEM fields is its vast ecosystem of scientific libraries (numpy,  pandas, scipy, matplotlib).
  
> Some of you may already know Python and that's great! You can sit back and relax and can skim through this notebook. For the rest of you, this section will serve as a quick crash course of python programming language and some of its most essential scientific libraries. This module will cover everything we will need for this course.

Let's start with an example/appetizer

```{code-cell} python
menu = ["h2o", "ch4", "nh3", 'XeF4', 'c2H4', 'NaCl'] 

for item in menu:
    print(item)
```

```{code-cell} python
for item in menu:
    
    if item == "NaCl":   
        
        print("sodium chlrodie in the list!")
        
    else:
        
        print("no sodium ions")
```

While these are silly examples for illustration, with the same simplicity of code you can do fairly sophisticated calculations. Do not worry if some of these commands seem unfamiliar, we are going to explain them later on. 

### Python versions

Just like any piece of code python is constantly evolving with new improvements and additions. Currently most of scientific packages and libraries are based python3 (we will be using python 3.7+). If you have installed Python on your computer you can check your Python version at the command line by running `python --version`.

### Comments
A “comment” is a part of code that is not run. It is a way to
write notes about what your code is doing at certain points. This is helpful
when you, or someone else, looks at the code later, so they know what it is
doing. To make a comment in Python, precede the comment with a #.

```{code-cell} python
# Comments can be on their own line like this
print("Hi")
print("World") # A comment can also be at the end of a line
```

### Whitespace
In programming, white space refers to all of the space in your document that is not filled with code.  Examples of whitespace are spaces, tabs (indents), and newlines (when you press enter and go to the next line). Python is very particular about white space and how you use it, specifically the use of indentations and newlines.
- **Newlines:** Python uses newline characters to separate logical lines of code. A logical line of code consists of a "command" in code. It is considered good Python style, or _Pythonic_ , to separate logical lines with newlines, although other methods exist.
- **Indentation:** Tab characters, or indentation, are used to indicate code blocks in Python. These will be seen later in the tutorial with for loops, while loops, if statements, and other structures. For now, the take-home message is to follow the indentation pattern of the example and avoid unnecessary indentation.

```{code-cell} python
print("Hello") # This is a logical line that assigns the value 16 to x
print("World") # This is another logical line, on the next line, that prints the value of x
```

```{code-cell} python
:tags: [raises-exception]

print("Hello")     # This line is not indented, so it is fine
    print("World") # Unnecessary indentation, this code will not work
```

**Exercise:** Remove unnecessary indentation in the broken code above and execute it again.

### Basic data types

Python has a variety of data types for managing different kinds of data

- numbers
- strings
- lists
- dictionaries
- sets
- tuples 

Some of these are _point types_ such as simple numbers often used for basic arithmetic operations. Others are of _container kind_ which contain sequences of numbers often used as vectors and matrices.  

## Numbers

Numbers are an important data type for us which we use to do all sorts of computations. It is important to know that the numbers in Python can be:
- **Integers:** -2, -1, 0, 1, 2
- **Floats:** -0.001, 4.56, 3.14
- **Complex numbers:** 1.2+2.5j, 2j, 3+1j

Let us begin creating some numeric data and assigning variable names:

```{code-cell} python
x = 3    # variable called x
```

```{code-cell} python
print(x) # print contents of x
```

```{code-cell} python
x        # Works the same for single line but for multiple lines you need print. See below
```

```{code-cell} python
print(x + 18)   # Addition
print(x - 1)   # Subtraction
print(x * 2)   # Multiplication
print(x ** 2)  # Exponentiation
```

```{code-cell} python
x=2.3
type(x) #let's find out what kind of number is this
```

**Exercise:** change the number type to float and complex number and execute the above cells again

```{code-cell} python
x, y, z = 1, 2, 5 # multiple assignments can be done with one line!
print(x)
print(y)
print(z)
```

```{code-cell} python
x + y, x * z  # Multiple operations can be done with one line also, separated by a comma!
```

#### Complex numbers are handled just as easily

```{code-cell} python
z1 = 10+2j
z2 = 3-1j
```

```{code-cell} python
# extract real and imaginary parts as well as the conjugate
z1.real, z1.imag, z1.conjugate()
```

```{code-cell} python
z1_abs = z1 * z1.conjugate()
print(z1_abs)
```

```{code-cell} python
z1_abs**0.5
```

## Booleans

Booleans are key type in any computer language they allow determining true or false statements and constructing logical set of operations

```{code-cell} python
x=True
y=False
z=True
```

```{code-cell} python
x == z  # == (equals), != (not equal), > (greater than), < (less than) comparison operators and return True or False.
```

```{code-cell} python
y=2.3
y>2
```

```{code-cell} python
y<2
```

```{code-cell} python
y==2.3
```

```{code-cell} python
y!=-234
```

## Strings

```{code-cell} python
hello = 'hello'   # String literals can use single quotes
x = "world blah blah"   # or double quotes; it does not matter.
type(x)
```

```{code-cell} python
world = 'world'
hw = hello + ' ' + world  # String concatenation with the + operator
print(hw)  # prints "hello world"
```

String objects have a bunch of useful methods; for example:

```{code-cell} python
s = "hello"
print(s.capitalize())  # Capitalize a string; prints "Hello"
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"
print(s.center(7))     # Center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another;
                               # prints "he(ell)(ell)o"
print('  world '.strip())   # Strip leading and trailing whitespace; prints "world"
print('-'.join(' A B C '))
print(''.join(' A B C '))
print('A B C'.split())
```

```{marimo} python
:editor: true

element = "Helium"
symbol = element[:2]
f"{element} -> {symbol}, {len(element)} letters"
```

## Containers

Python includes several built-in container types: **lists, dictionaries, sets, and tuples.** Lists will be the most useful for our objectives in this course so we only cover lists.

Strings, lists and tuples are *sequences*. They can be *indexed* and *sliced* in the same way.

Tuples and strings are “immutable” (which basically means we can’t change individual elements within the tuple, and we cannot change individual characters within a string) whereas lists are “mutable” (*.i.e* we can change elements in a list.)

Sequences share the following operations

* `a[i]` returns i-th element of `a`
* `a[i:j]` returns elements i up to j-1
* `len(a)` returns number of elements in sequence
* `min(a)` returns smallest value in sequence
* `max(a)` returns largest value in sequence
* `x in a` returns `True` if `x` is element in `a`
* `a + b` concatenates `a` and `b`
* `n * a` creates `n` copies of sequence `a`

### Lists

![](images/list.png)

A list is a generic container for holding any Python type, be it a string, numbers, other lists, or a mix of everything.

```{code-cell} python
xs = [3, 1, 2,5,6,'blah']   # Create a list
print(xs[4])
```

```{code-cell} python
xs[2] = 'foo'    # Lists can contain elements of different types
print(xs)
```

```{code-cell} python
xs.append(145) # Add a new element to the end of the list
print(xs)  
```

```{code-cell} python
#x = xs.pop()     # Remove and return the last element of the list
#print(x, xs) 
#help(x)
```

As usual, you can find all the gory details about lists in the [documentation](https://docs.python.org/2/tutorial/datastructures.html#more-on-lists).

### Slicing

In addition to accessing list elements one at a time, Python provides concise syntax to access sublists; this is known as slicing:

![](images/sliceList.jpg)

```{code-cell} python
nums = range(0,55,3) # range(i,j,k) is a built-in function that creates a list of integers from i to j with a stride k
nums = list(nums)     # make a list
print(nums)
nums[0:3]
```

![](images/list_slice.png)

### Loops

Loops alow you to go over the elements of containers and act on them given specific instructions. You can loop over the elements of a list like this:

```{code-cell} python
animals = ['cat', 'dog', 'monkey', 'lion']

for animal in animals:
    print(animal)
```

### List comprehensions:

When programming, frequently we want to transform one type of data into another. As a simple example, consider the following code that computes square numbers:

```{code-cell} python
nums = [0, 1, 2, 3, 4,5]
squares = []

for x in nums:
    squares.append(x ** 3)
squares
```

You can make this code simpler using a special trick of lists called list comprehension:

```{code-cell} python
nums = [0, 1, 2, 3, 4, 5]

squares = [5*x + x ** 2 for x in nums]  # This is a list comprehension

squares
```

List comprehensions can also contain conditions:

```{code-cell} python
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
even_squares
```

#### The range() command

A special type of list is frequently required (often together with `for-loops`) and therefor a command exists to generate that list: the `range(n)` command generates integers starting from 0 and going up to *but not including* n. Here are a few examples:

```{code-cell} python
list(range(3))
```

```{code-cell} python
list(range(10))
```

This command is often used with for loops. For example, to print the numbers 0<sup>2</sup>,1<sup>2</sup>,2<sup>2</sup>,3<sup>2</sup>,…,10<sup>2</sup>, the following program can be used:

```{code-cell} python
for i in range(11):
    print(i ** 2)
```

The range command takes an optional parameter for the beginning of the integer sequence (start) and another optional parameter for the step size. This is often written as `range([start],stop,[step])` where the arguments in square brackets (*i.e.* start and step) are optional. Here are some examples:

```{code-cell} python
list(range(3, 10))  
```

```{code-cell} python
list(range(3, 10, 2))
```

Why are we calling `list(range())`?

In Python 3, `range()` generates the numbers on demand. When you use `range()` in a for loop, this is more efficient, because it doesn't take up memory with a list of numbers. Passing it to `list()` forces it to generate all of its numbers, so we can see what it does.

To get the same efficient behaviour in Python 2, use `xrange()` instead of `range()`.

```{marimo} python
:editor: true

evens = [n for n in range(20) if n % 2 == 0]
evens[2:6]   # try different slices or conditions
```

### Control Flow and the if-then-else statement

The `if statement` allows you to execute a block of code optionally, if certain conditions are met. An expression which evaluates to True or False, called the *conditional statement*, must be in the parentheses following the `if` keyword.

```{code-cell} python
x = 5

if( x + 3 > 11):
    print("I entered the conditional block!")
    print("I am also part of the conditional block.")
    
print('''Since I am not indented, I am not in the 
    conditional block and execute every time.''')
```

The `if statement` can be followed with optional blocks of code that will be executed if another condition, or no condition, is met. The default code block when no condition is met is an `else statement`. Each `if statement` can also be followed by zero or more `elif statements`. These are used to chain together `if statements` with different conditions. Try changing x to trigger the different conditions below.

```{code-cell} python
x = 9

if( x == 9):
    print("x equals 9")
elif(x < 9):
    print("x is less than 9")
elif(x > 9 and x < 20):
    print("x is between 9 and 20")
else:
    print("x is greater than 20")
```

**While loop**

The <span>`while`</span> keyword allows to repeat an operation while a condition is true. Suppose we’d like to know for how many years we have to keep 100 pounds on a savings account to reach 200 pounds simply due to annual payment of interest at a rate of 5%. Here is a program to compute that this will take 15 years:

```{code-cell} python
mymoney = 100         # in GBP
rate = 1.05           # 5% interest
years = 0
while mymoney < 200:  # repeat until 20 pounds reached
    mymoney = mymoney * rate
    years = years + 1
print('We need', years, 'years to reach', mymoney, 'pounds.')
```

### Dictionaries

Dictionaries are *unordered* sets of *key-value pairs*.

An empty dictionary can be created using curly braces:

``
my_empty_dict = {}
``

```{code-cell} python
polymer_properties = {'monomer': 'ch2', 
                      'mass': 120, 
                      'melting temperature': '25 C',
                      'degree of polymerization': 24}
```

```{code-cell} python
weather = {}
```

```{code-cell} python
weather['today'] = '22 deg C'    # 'today' is the keyword
```

```{code-cell} python
weather['yesterday'] = '19 deg C'
```

```{code-cell} python
:tags: [raises-exception]

print(weather['todady'])
print(weather['random day'])
```

`d.keys()` returns a list of all keys:

We can retrieve values by using the keyword as the index:

```{code-cell} python
weather['today']
```

Other ways of populating a dictionary if the data is known at creation time are:

```{code-cell} python
d3 = dict(a=1, b=2, c=3)
d3
```

The function `dict()` creates an empty dictionary.

Other useful dictionary methods include `values()`, `items()` and `get()`. You can use `in` to check for the presence of values.

```{code-cell} python
d3.values()
```

```{code-cell} python
d3.items()
```

```{marimo} python
:editor: true

masses = {"H": 1.008, "He": 4.003, "Li": 6.94}
masses["C"] = 12.011   # add more elements
sorted(masses.items())
```

## Functions

Python functions are defined using the `def` keyword. For example let us write a polynomial function 

$$f(x)=3.0x^3 + x^2 + 10x+1.0$$

```{code-cell} python
def sq_func(x):  
    ''' Always document the kinds of inout and output you expect from a function
    x:    float number
    f(x): float number '''
    
    return 3.0*x**3 + x**2 + 10*x+1.0
```

```{code-cell} python
def list_explorer(X, i):
    '''
    X: is a non empty list
    i: is an integer
    '''

    print(f'element {i} of my list is', X[i])
```

```{code-cell} python
y = sq_func(3)
y
```

```{code-cell} python
import numpy as np

def add_trig2(x, y):   # defined function of variable x and y
    
    return np.sin(x)**2 + np.cos(y)**2
```

```{code-cell} python
z = add_trig2(4, 4)

z
```

### Positional and optional arguments

Sometimes we like to specify default values for funciton variables. E.g in science context this will be physical parameters, like the stiffness constant and quilibrium length of a spring. Note that the positional argument must always come first followed by any number of optional arguments.

```{code-cell} python
def harm_osc(x, k=1, x0=0):
    '''x: is a float number
       k: float number
       x0: float number'''

    return k * (x-x0) ** 2
```

```{code-cell} python
print(harm_osc(2))

print(harm_osc(2,10))

print(harm_osc(2,k=10))

print(harm_osc(2,k=10,x0=0.5))
```

```{marimo} python
:editor: true

def kinetic_energy(m, v):
    return 0.5 * m * v**2

kinetic_energy(9.109e-31, 2.19e6)   # electron at Bohr speed, joules
```

## Exercises

**1. Predict and explain the following statements**

```
1. 1 and 2
2. 0 and 1
3. 1 or 0
4. not 1 < 2 or 4 > 2
5. not (1 < 2 or 4 > 2)
6. 1 < 2 or 4 > 2
7. not 0 < 1
```

**2. Slice the string s = 'seehemewe' to produce the following substrings:**

```
1. 'see'
2. 'he'
3. 'me'
4. 'we'
5. 'hem'
6. 'meh'
7. 'wee'
```

**3. Predict the results of the following statements**

```    
days = 'Sun Mon Tues Weds Thurs Fri Sat'

1. print(days[days.index('M'):])
2. print(days[days.index('M'): days.index('Sa')]. rstrip ())
3. print(days [6:3: -1]. lower ()*3)
4. print(days.replace('rs', ''). replace('s ', ' ')[::4])
5. print(' -*- '.join(days.split ()))
```

**4. Predict and explain the outcome of the following statements using the variables**

```
s = 'hello' and a = [4, 10, 2]

1. print(s, sep='-')
2. print(*s, sep='-')
3. print(a)
4. print(*a, sep='')
5. list(range(*a))
```

**5. Core data types of python**

1. Acess and pring the length as well as first, middle and last letters of the string ``dna_string = "ACGCAGG"``

2. Create two lists ``x=[1,2,4,"dog", "xy"]`` and ``y =[3,4,5,"cat", "a"]`` and do ``x+y``. ``XY=x[:3]+y[:3]``. Comment on why ``XY`` looks the way it looks. Any other way to achieve same result? 

3. Create two string variables ``s1="I am"`` and ``s2="  Python Ninja"`` (notice the space). First do s1+sw and comment. Next Capitalize every other element in the string. 

4. Loop over items in lists in 1 by prining the numbers only. 

5. Create two string variables by typing ``mol1 = "CH3"`` and ``mol2= "CH2"``. Using only these two strings and arithmetic operations on strings (+ and/or multiply *) create a third variable that would represent molecule of octane.

**6. Functions**

1. Create a function that computes polynomial $y=ax^n+bx^3+c$ at points $x=−2$, $x=0$, and $x=2.1$ by using $n=1$, $a=b=1$, $c=-6$ as parameters. 

    - Create a list of values for parameter a. Compute values of function at values x = 1 and x=2 and store it in a separate list. 

2. Create a function that calculates mass of hydrocarbon and fraction of carbon atoms.

3. Complete a function started below that calculates the rate of a single-step chemical reaction nA → P using the differential rate law (Rate = k[A]).

```python 

def rate(A0, k=1.0, n=1):
    ''' (concentration(M), k = 1.0, n = 1) → rate (M/s)
    Takes in the concentration of A (M), the rate constant (k), 
    and the order (n) and returns the rate (M/s)
    '''   

```

4. Write and test a function, complete with docstring, that solves the Ideal Gas Law for pressure when provided with volume, temperature, and moles of gas (R = 0.08206 L·atm/mol·K) with the following stipulations.

    - Create one version of the function that takes only positional arguments.

    - Create a second copy of the function that takes only keyword arguments. Try testing this function with positional arguments. Does it still work?

5. Write a function that calculates the distance between the origin and a point in any dimensional space (1D, 2D, 3D, etc…) by allowing the function to take any number of coordinate values (e.g., x, xy, xyz, etc…). Your function should work for the following tests.

```bash
[in]: dist(3)

[out]: 3

[in]: dist(1,1)

[out]: 1.4142135623730951

[in]: dist(3, 2, 1)

[out]: 3.7416573867739413

```

**7. Computating Binomial coefficients**

- Step-1 Write a function that computes binomial coefficients given n and k as input. You can consult [Wikipedia](https://en.wikipedia.org/wiki/Binomial_coefficient)

    ```python
    def C(n,k):
    return
    ```
    
- Step-2 Compare your function with binom function from of scipy. Do help(binom) to learn more

    ```python
    from scipy.special import binom
    ```
    
- Step-3 Make several plots of binomial coefficients C(n,k) as a function of k values for different fixed n.
E.g n =2 n= 8 n=16 n=23 n=64.

    ```python
    from matplotlib.pyplot import plt
    plt.plot(k, C(16,k), '-o')
    ```

**8. Computing palindromes using DNA sequence**
    
1. Given a string representing a base-pair sequence (i.e. containing only the letters
A, G, C and T), determine the fraction of G and C bases in the sequence.
(Hint: strings have a count method, returning the number of occurrences of a
substring.)
2. Using only string methods, devise a way to determine if a nucleotide sequence
is a palindrome in the sense that it is equal to its own complementary sequence
read backward. For example, the sequence TGGATCCA is palindromic because
its complement is ACCTAGGT, which is the same as the original sequence backward. The complementary base pairs are (A, T) and (C, G).

**9. Credit Card fraud.**

The Luhn algorithm is a simple checksum formula used to validate credit card and bank account numbers. It is designed to prevent common errors in transcribing the number, and detects all single-digit errors and almost all transpositions of two adjacent digits. The algorithm may be written as the following steps. 

    1. Reverse the number.
    2. Treating the number as an array of digits, take the even-indexed digits (where the indexes start at 1 ) and double their values. If a doubled digit results in a number greater than 10, add the two digits (e.g., the digit 6 becomes 12 and hence 1 + 2 = 3).
    3. Sum this modified array.
    4. If the sum of the array modulo 10 is 0 the credit card number is valid.
    
Write a Python program to take a credit card number as a string of digits (possibly in
groups, separated by spaces) and establish if it is valid or not. For example, the string ’4799 2739 8713 6272’ is a valid credit card number, but any number with a single digit in this string changed is not.

**10. Catch a bug**

A Harshad number is an integer that is divisible by the sum of its digits (e.g., 21 is divisible by 2 + 1 = 3 and so is a Harshad number). Correct the following code which should return True or False if n is a Harshad number or not respectively. The code when run on some number ``is_harshad(21)`` gives error. Find the error and fix it.  

```python
def digit_sum(n):

    """ Find the sum of the digits of integer n. """
    s_digits = list(str(n)) dsum = 0
    for s_digit in s_digits:
        dsum += int(s_digit) 

def is_harshad(n):
    return not n % digit_sum(n)
```

**11. The while loop and radioactive decay**

The isotope of $^13C$ has a half-life about 30.2 years. Using a while loop, determine how many half-lives until a 500.0 g sample would have to decay until there is less that 10.00 grams left. To accomplish this, create a counter (counter = 0) and add 1 to it each cycle of a while loop to keep count.

**12. interatomic distances**

The following code generates five atoms at random coordinates in 3D space. Write a Python script that calculates the distance between each pair of atoms and returns the shortest distance. 
> The [itertools](https://docs.python.org/3/library/itertools.html) module might be helpful here but you can do without it. 

```python
from random import randint
atoms = []
for a in range(5):
    x, y, z = randint(0,20), randint(0,20), randint(0,20)
    atoms.append((x,y,z))
```

### Try it live

:::{tip}
This cell runs **in your browser**. Edit the code and press the play button (or Ctrl-Enter). The value of the last line is what gets displayed, so end your experiments with an expression.
:::


```{marimo} python
:editor: true

quantum_pioneers = ["Planck", "Bohr", "Heisenberg", "Schrodinger", "Dirac"]
greetings = [f"{name} says hi" for name in sorted(quantum_pioneers)]
greetings
```
