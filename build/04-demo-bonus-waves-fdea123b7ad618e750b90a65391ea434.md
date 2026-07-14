---
kernelspec:
  name: python3
  display_name: Python 3
---

# DEMO: Bonus challenge

**Waves, normal modes and interference** 

**Prerequisites**
- Go over the [demo notebook on waves](https://dpotoyan.github.io/Chem324/ch02/demo_waves.html). You can copy paste and modify examples there to solve most challenges

- Go over the [python, numpy and matploltib](https://dpotoyan.github.io/Chem324/demos/intro2py.html) basics to be more comfortable with the code.  

**How to complete the work**
- Run the cell below to import all necessary libraries.
- Add code below each problem. 
- Run the code in Google Collab then download the file either as *.ipynb or *py file.
- Submit your file to Canvas.
- Do not forget that Google Collab deletes files if you do not save them iin your Google Drive.

```{code-cell} python
import numpy as np  
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive
import scipy  
from scipy.constants import physical_constants, hbar, h, c, k, m_e, Rydberg, e, N_A

%matplotlib inline
%config InlineBackend.figure_format='retina'
```

### Problem 1: Combining normal modes 

- Recreate figures 2.4, 2.6 and 2.7 in the book using the example of normal modes.

- Recreate fig 2.4 but for the case of combining the 2D standing waves! 

### Problem 2: Beats and music

The study of music provides many examples of the superposition of waves and the constructive and destructive interference that occurs. Very few examples of music being performed consist of a single source playing a single frequency for an extended period of time. You will probably agree that a single frequency of sound for an extended period might be boring to the point of irritation, similar to the unwanted drone of an aircraft engine or a loud fan. Music is pleasant and interesting due to mixing the changing frequencies of various instruments and voices. An interesting phenomenon that occurs due to the constructive and destructive interference of two or more frequencies of sound is the phenomenon of beats. If two sounds differ in frequencies, the sound waves can be modeled as superposition of two waves $s_1+s_2$ (showing only the temporal parts)

$$s_1+s_2 = A sin(2 \pi  \nu_1  t + \phi_1)+A sin(2 \pi  \nu_2  t + \phi_2)$$

You can use the trig identities for sum of sines and cosines to appreacite what the difference in frequencies does to the music $\phi_1-\phi_2$. But for this exercise we are going to take computational route. Below are the steps to help you explore the effect of frequency shift in producing beats! 

- Create range of time points via **t = np.arange(0, 2, 0.01)**. 
- Set $A=1$, $\nu_1=10$, $\nu_2=11.5$, $\phi_1=\phi_2=0$.
- Compute $s_1 = A cos(2 \pi  \nu_1  t + \phi_1)$
- Compute $s_2 = A cos(2 \pi  \nu_2  t + \phi_2$)
- Make a plots $s_1$ and $s_2$ and $plot s1+s2$ separately. Take a look at cookbook example and try making three subplots stacked vertically. 
- Create interactive widet to explore the effect of a phase shift!
- Write a brief report about your observations

### Problem 3 Interference of spherical waves

One place you must have seen wave intereference is when you disturb two points of water in a quiet lake. See this video for instance: [Water Wave interference](https://www.youtube.com/watch?v=ovZkFMuxZNc). 
<br>
Below we are going to create this effect computationally. The mathematics is simple you create two sin waves in 2D space 
- $w_1=sin(k r_1)$ and 
- $w_2=sin(k r_2)$ 

at different locations of 2D space. Then you combine these waves and observe intereference as a function of separation of wave centers $r_1$ and $r_2$ Below you will find the partial code along with description of what you need to do to complete the exercise. You should see some pretty intereference patterns. 

```{code-cell} python

wavelength = 5.0

k = 2*np.pi/wavelength

separation = 50.0      # Separation of centers in cm
side = 100.0           # Side of the square in cm
points = 500           # Number of grid points along each side
spacing = side/points  # Spacing of points in cm

# Calculate the positions of the centers of our spherical waves.

x1 = side/2 + separation/2
y1 = side/2

x2 = side/2 - separation/2
y2 = side/2

#  Create a 1D np.linspace method create two 1D numpy arrays for xx and yy dividing each side by points given above.

# Use np.meshgrid turn xx and yy into  500 by 500 2D arrays of x and y. Check out examples in PythonCookbook and PythonIntro sections

#  Compute distance r1 = np.sqrt((x-x1)**2+(y-y1)**2)
#  Compute distance r2 = np.sqrt((x-x2)**2+(y-y2)**2)

#  Plug dsitances into linear combination of sine waves X
#  sum_waves = np.sin(k*r1)+np.sin(k*r2)

#  Make a 2D plot via plt.imshow(sum_waves)

#  Make plots in different jupyter cells for exploring differen values of separation and wavelengths

# (optional) make the above code into a function and create an interactive  widget for exploring the separation 
```
