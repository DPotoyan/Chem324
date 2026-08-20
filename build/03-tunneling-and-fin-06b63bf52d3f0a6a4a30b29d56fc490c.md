---
kernelspec:
  name: python3
  display_name: Python 3
---

# Tunneling and the Finite Square Well

:::{admonition} **What you need to know**

- **Tunneling** is the signature quantum effect: a particle has a non-zero probability of being found in regions where $E < V$, which no classical particle could ever visit.
- The **finite depth box** is a more realistic model than the infinite potential well, as it allows for quantum tunneling, where the particle has a non-zero probability of being found outside the well.
- The potential energy is zero in the central region and finite outside. The time-independent Schrödinger equation is solved in three regions, with a different form of wavefunction in each. Bound states are possible due to confinement of the particle, but the energy levels are determined by matching the wavefunction and its derivative at the boundaries, leading to transcendental equations.
- Unlike the infinite well, the number of bound states is finite, and the wavefunctions extend slightly outside the well, illustrating the quantum tunneling effect.
- Understanding the **boundary conditions** and the **behavior of the wavefunctions** in each region is key to solving this problem.
:::

**Acknowledgement**
> These Jupyter notebooks are based on the excellent paper in [J. Chem. Educ. 2019, 96, 8, 1663-1670](https://doi.org/10.1021/acs.jchemed.9b00195).

## Quantum objects can go where no classical particles are allowed!


:::{figure} ./images/tunnel1.png
:label: fig-characteristics-of-wavefunctions-1
:alt: pib1
:width: 800px

1. Nordheim square barrier for electron tunneling from bound states into the continuum.
2. Nitrogen inversion in ammonia by tunneling through the barrier (proposed by George Uhlenbeck in 1932).
3. Esaki tunnel diode: electrons and holes tunnel across a heavily doped p-n junction only about 10 nm wide.
:::

<div style="text-align: center;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Yg0LT3n4mYY?si=yIxDAvxxFRzQ8z1J" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

### Qualitative trends in wavefunction behavior


:::{figure} ./images/gen_psi2.png
:label: fig-characteristics-of-wavefunctions-2
:alt: pib1
:width: 400px

A stepped potential and the expected behavior of the wavefunction.
:::



:::{figure} ./images/gen_psi1.png
:label: fig-characteristics-of-wavefunctions-3
:alt: pib1
:width: 400px

From the signs of the terms in the Schrödinger equation, we can predict qualitatively how the wavefunction will behave.
:::

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from scipy import optimize

# constants for an electron in a well measured in eV and Angstroms
hbar = 1.05457180013e-34   # J s
melec = 9.10938356e-31     # electron mass, kg
eVtoJ = 1.60217662e-19     # J per eV
AngstromtoMeter = 1e-10
val = np.sqrt(2.0*melec*eVtoJ)*AngstromtoMeter/(2.0*hbar)  # sqrt(2m)/(2 hbar) with L in Angstrom, E in eV

def potential(x, Vo, L):
    Vx=np.zeros(len(x))
    for i in range(len(x)):
        if x[i]<=-L/2 or x[i]>=L/2:
            Vx[i]=Vo
        

    return Vx

L=10
Vo=5

fig, ax=plt.subplots()

#create and plot the potential
x = np.linspace(-L, L, 1000)
Vx = potential(x, Vo, L)
ax.plot(x,Vx, label='Potential $V_0$')

ax.set_ylim(-.1,Vo*1.4)
ax.set_xlim(-L,L)
ax.set_xlabel(r'$x$ (Angstroms)', fontsize=14)
ax.set_ylabel(r'Energy (eV)', fontsize=14);

#label the three regions of the potential
ax.annotate('Region I',xy=(-3*L/4,Vo*1.1), ha='center')
ax.annotate('Region II',xy=(0,Vo*1.1), ha='center')
ax.annotate('Region III',xy=(3*L/4,Vo*1.1), ha='center')

#generic plot, label interms of width L and depth Vo
ax.set_yticks([0, Vo])
ax.set_yticklabels(['0','$V_0$'])
ax.set_xticks([-L/2, L/2])
ax.set_xticklabels(['$-L/2$','$L/2$'])

#highlight the classically forbidden region in gray
ax.bar(-3*L/4, Vo, width=L/2, color='gray', alpha=0.5)
ax.bar(3*L/4, Vo, width=L/2, color='gray', alpha=0.5)
ax.bar(0, -0.1, width=2*L, color='gray', alpha=0.5)

patch = mpatches.Patch(color='gray', label='Classically forbidden region')
handles, labels = ax.get_legend_handles_labels()
handles.append(patch)
ax.legend(handles=handles, loc=2);

plt.show()
```

### Solutions inside square well

Inside the finite square well, the region $-L/2 \le x \le L/2$, the potential $V(x)=0$ so the Schrödinger equation,

$$
\frac{-\hbar^2}{2m}\frac{d^2\psi(x)}{d{x}^2}+V(x)\psi(x) =E\psi(x)
$$ 


$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{d{x}^2}=E\psi(x)
\quad\Longrightarrow\quad
\frac{d^2\psi(x)}{d{x}^2}=-\frac{2mE}{\hbar^2}\psi(x)
=-k^2\psi(x), \qquad k^2 = \frac{2mE}{\hbar^2}
$$ 


- Solutions to this equation have an oscillatory form:

$$
\psi(x)=A_1e^{ikx}+B_1e^{-ikx}\\
       =A\sin(kx)+B\cos(kx)
$$ 

### Solutions outside the well

In the regions where $x < -L/2$ and $x > L/2$, the potential is $V(x) = V_0$. The time-independent Schrödinger equation for these regions can be written as:

$$
-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} + V_0\psi(x) = E\psi(x),
$$



$$
\frac{d^2\psi(x)}{dx^2} = \frac{2m(V_0 - E)}{\hbar^2} \psi(x) = \beta^2 \psi(x), \qquad \beta^2 = \frac{2m(V_0 - E)}{\hbar^2}
$$

**What happens when $E < V_0$?**

- When the particle's energy is less than the potential outside the well $(E < V_0)$, the coefficient $\beta^2$ is **positive**, so $\beta$ is real. Compare the two regions: inside the well $\psi'' = -k^2\psi$ (curvature toward the axis, oscillation), while outside $\psi'' = +\beta^2\psi$ (curvature away from the axis, exponentials $e^{\pm\beta x}$).
- The physically acceptable solution outside is the **decaying exponential** (an evanescent wave). The wavefunction therefore dies off exponentially as the particle penetrates into the classically forbidden regions, but it is not zero there: that is tunneling.

### Profile of the full wavefunction

Our potential well consists of three regions, and the particle has an energy less than the potential, i.e. $E<V_0$. So that the wavefunction can be normalized, we make the following choices to ensure that $\psi(x)\rightarrow 0$ as $x\rightarrow\pm\infty$. We also choose the trigonometric form of the wavefunction inside the well; recall that this is to make the math easier.

$$
\text{Region I:  }  V(x) = V_0 ~~~~~~~~~~~~~~~~ x \leq-\frac{L}{2} ~~~~~ \psi_{I} = A e^{\beta  x} \\
\text{Region II: }  V(x) = 0 ~~~ -\frac{L}{2} \leq x \leq\frac{L}{2} ~~~~~~~ \psi_{II} = B \cos(k x) + C \sin(k x)\\
\text{Region III:}  V(x) = V_0 ~~~~~~~~~~~~~~  x \geq \frac{L}{2}  ~~~~~~~ \psi_{III} = D e^{-\beta x}
$$

**Why do we check for continuity?**

- $\psi^{'}$ needs to be continuous to guarantee the existence of $\psi^{''}$, whose existence is required from the first postulate.  

- $\large{\frac{d^2}{dx^2}}$ is a component of the kinetic energy operator. If the wavefunction does not have a well-defined second derivative, then the kinetic energy would be undefined, which is not possible.

### Boundary conditions

The wavefunction is the combination of all three components, so we make sure that the wavefunction and its first derivative are continuous at each boundary. We apply the following boundary conditions to achieve this:

$$
\psi_{I}\left(-\frac{L}{2}\right) = \psi_{II}\left(-\frac{L}{2}\right)  \text{  and  } 
\psi_{II}\left(\frac{L}{2}\right) = \psi_{III}\left(\frac{L}{2}\right).
$$

$$
\psi^{'}_{I}\left(-\frac{L}{2}\right) = \psi^{'}_{II}\left(-\frac{L}{2}\right)  \text{  and  }
\psi^{'}_{II}\left(\frac{L}{2}\right) = \psi^{'}_{III}\left(\frac{L}{2}\right)
$$

Note that there are two conditions at each boundary, so we end up with two sets of two simultaneous equations.

### Even and odd solutions

Finally, our potential is symmetric about $x=0$, so the wavefunction is either a maximum or zero at $x=0$ so that the probability distribution is symmetric about $x=0$. We call these even when $\psi(x)=\psi(-x)$ and odd when $\psi(x)=-\psi(-x)$.

**Even solutions:**

$$
x \leq-\frac{L}{2}: ~~~ \psi_{I}(x) = A e^{\beta  x} \\
-\frac{L}{2} \leq x \leq\frac{L}{2}: ~~~ \psi_{II}(x) = B \cos(k x) \\
x \geq \frac{L}{2}: ~~~ \psi_{III}(x) = D e^{-\beta x}
$$



- These are called **even solutions** because the function $\cos(kx)$ is even, i.e. it is symmetric about $x=0$. However, they correspond to the odd values of $n$.


- After imposing the boundary conditions we reach the following relation:

$$
\beta = k\tan\left(k\frac{L}{2}\right)\Rightarrow \sqrt{V_o-E} = \sqrt{E}\tan\left(\frac{L\sqrt{2mE}}{2\hbar}\right)
$$(fsw_even_states_equ)

**Odd solutions:**

$$
x \leq-\frac{L}{2}:  ~~~ \psi_{I}(x) = -A e^{\beta  x} \\
-\frac{L}{2} \leq x \leq\frac{L}{2}:  ~~~ \psi_{II}(x) = C \sin(k x) \\
x \geq \frac{L}{2}:  ~~~ \psi_{III}(x) = D e^{-\beta x}
$$

- These are called **odd solutions** because the function $\sin(kx)$ is odd, i.e. it is anti-symmetric about $x=0$. However, they correspond to the even values of $n$. This is a bit confusing, I know, but the labeling of $n$ is arbitrary; the sine and cosine solutions themselves are determined by the physics.

- After imposing the boundary conditions we reach the following relation:

$$
\beta = -\frac{k}{\tan\left(k\frac{L}{2}\right)} \Rightarrow  \sqrt{V_o-E} = -\frac{\sqrt{E}}{\tan\left(\frac{L\sqrt{2mE}}{2\hbar}\right)}
$$(fsw_odd_states_equ)

- Unfortunately, we cannot find the allowed energies analytically. Instead, we have to choose either a graphical or a numerical method.
- What does that mean? We can graph the left- and right-hand sides of each equation separately as a function of energy $E$ and look for the intersection points, which correspond to the allowed energy values (the energy eigenvalues).
- Below you can adjust the well depth $V_0$ and the width $L$ and watch both the graphical solution and the resulting energy levels respond live.

## Finding the energy eigenvalues graphically 

```{code-cell} python
:tags: [hide-input]
#a better (tidier!!) way of finding the energy eigen values in the finite square well. 

#define the equations we wish to find the roots of
#one for even wavefuntions and one for odd wavefunctions.

def f_even(E,Vo,L):
    return(np.sqrt(Vo-E)-np.sqrt(E)*np.tan(L*np.sqrt(E)*val))
def f_odd(E,Vo,L):
    return(np.sqrt(Vo-E)+np.sqrt(E)/np.tan(L*np.sqrt(E)*val))

#function to find the roots of the above equations.
#default step size of 0.04 is sufficient given the well 
#parameters being used in the rest of the notebook. 

def find_state_energies(Vo,L,step=0.01):  
    
    sol = np.array([],dtype=float) #all solutions
    E = np.arange(step,Vo,step) #array of energies
    even=True 
    
    #iterate over the array of energies and look for positions where the sign of the function changes 
    #These are the roots of the function. 
    for i in range(len(E)-1):
        if even==True:
            if f_even(E[i], Vo, L)*f_even(E[i+1], Vo, L)<0: #have we bracketed a zero?                                                           
                sol=np.append(sol,optimize.brentq(f_even,E[i],E[i+1],args=(Vo, L)) ) 
                even=False
        if even==False:
            if f_odd(E[i], Vo, L)*f_odd(E[i+1], Vo, L)<0:
                sol=np.append(sol,optimize.brentq(f_odd,E[i],E[i+1],args=(Vo, L)))
                even=True  
    #return the energies of the states and the number of states
    return sol, len(sol)

#eng, nstates = sqWellSol(5, 10) 
#print(eng, nstates)
#print(e_eng)
```

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
      "scipy",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
from scipy import optimize
```

```{marimo} python
:hide-code: true

val_m = np.sqrt(2.0 * 9.10938356e-31 * 1.60217662e-19) * 1e-10 / (2.0 * 1.05457180013e-34)

def f_even_m(E, Vo, L):
    return np.sqrt(Vo - E) - np.sqrt(E) * np.tan(L * np.sqrt(E) * val_m)

def f_odd_m(E, Vo, L):
    return np.sqrt(Vo - E) + np.sqrt(E) / np.tan(L * np.sqrt(E) * val_m)

def find_states_m(Vo, L, step=0.01):
    sol = []
    E_scan = np.arange(step, Vo, step)
    even = True
    for i in range(len(E_scan) - 1):
        if even and f_even_m(E_scan[i], Vo, L) * f_even_m(E_scan[i + 1], Vo, L) < 0:
            sol.append(optimize.brentq(f_even_m, E_scan[i], E_scan[i + 1], args=(Vo, L)))
            even = False
        if not even and f_odd_m(E_scan[i], Vo, L) * f_odd_m(E_scan[i + 1], Vo, L) < 0:
            sol.append(optimize.brentq(f_odd_m, E_scan[i], E_scan[i + 1], args=(Vo, L)))
            even = True
    return np.array(sol)

def En_box_m(n, L):
    h_planck = 6.62607e-34
    return n**2 * h_planck**2 / (8 * 9.1093837e-31 * (L * 1e-10)**2 * 1.6e-19)
```

```{marimo} python
:hide-code: true

Vo1 = mo.ui.slider(0.5, 10.0, step=0.5, value=5.0, show_value=True, label="well depth V0 (eV)")
L1 = mo.ui.slider(2.0, 17.0, step=0.5, value=10.0, show_value=True, label="well width L (Angstrom)")
mo.hstack([Vo1, L1], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

_Vo, _L = Vo1.value, L1.value
_fig, _axes = plt.subplots(1, 2, figsize=(11, 5), gridspec_kw={"width_ratios": [2, 1]})

_E = np.linspace(0.001, _Vo * 0.999, 4000)
_lhs = np.sqrt(_Vo - _E)
_ev = np.sqrt(_E) * np.tan(_L * np.sqrt(_E) * val_m)
_od = -np.sqrt(_E) / np.tan(_L * np.sqrt(_E) * val_m)
_ev[np.abs(_ev) > 4 * np.sqrt(_Vo)] = np.nan
_od[np.abs(_od) > 4 * np.sqrt(_Vo)] = np.nan

_axes[0].plot(_E, _lhs, color="#3d81f6", lw=2, label=r"$\sqrt{V_0-E}$")
_axes[0].plot(_E, _ev, color="#d81b60", ls="-.", lw=1.8, label="even states")
_axes[0].plot(_E, _od, color="#004d40", ls="--", lw=1.8, label="odd states")
_energies = find_states_m(_Vo, _L)
_axes[0].scatter(_energies, np.sqrt(_Vo - _energies), zorder=5, color="black")
_axes[0].set_xlim(0, _Vo)
_axes[0].set_ylim(0, np.sqrt(_Vo) * 1.15)
_axes[0].set_xlabel("E (eV)")
_axes[0].set_ylabel(r"(eV$^{1/2}$)")
_axes[0].legend(loc="upper right", fontsize=9)
_axes[0].set_title(f"Graphical solution: {len(_energies)} bound state(s)")

_x = np.linspace(-15, 15, 400)
_axes[1].plot(_x, np.where(np.abs(_x) >= _L / 2, _Vo, 0.0), color="#3d81f6", lw=1.5)
for _n, _en in enumerate(_energies, start=1):
    _c = "#d81b60" if _n % 2 else "#004d40"
    _axes[1].hlines(_en, -_L / 2, _L / 2, color=_c, ls="--", lw=1.8)
    _axes[1].text(_L / 2 + 0.7, _en, f"$E_{_n}$ = {_en:.2f} eV", fontsize=9, color=_c, va="center")
_axes[1].set_ylim(0, _Vo * 1.15)
_axes[1].set_ylabel(r"$E_n$ (eV)")
_axes[1].set_xticks([])
_axes[1].set_title("Energy levels in the well")
plt.tight_layout()
plt.gcf()
```

Here are some questions to think about:

* **Q1:** How does changing the width affect the number and energy of the states?
* **Q2:** How does changing the potential affect the number and energy of the states?
* **Q3:** Is the ground state described by an even or an odd wavefunction?
* **Q4:** What is the minimum number of states?
* **Q5:** Do the energy levels follow the same pattern as the infinite square well, i.e. $E_n=E_1n^2$?

### Plots of the wavefunctions and probability densities

- Now that we know the energy eigenvalues, we can use them to find expressions for the wavefunctions and probability densities. This may help you understand some of the choices we made up to this point. Take a look at the figure and consider again the choice of wavefunction in regions I and III, and why we split the wavefunction into odd and even functions inside the well.

```{code-cell} python
:tags: [hide-input]
#set the potential depth and width
Vo=5
L=10

#find the energies of the states for the given Vo and L
E_vals, nstates = find_state_energies(Vo, L)

fig, ax = plt.subplots(1,2, figsize=(12,9))

#create x values for each of region I, II & III
X_lef = np.linspace(-L, -L/2.0, 900,endpoint=True)
X_mid = np.linspace(-L/2.0, L/2.0, 900,endpoint=True)
X_rig = np.linspace(L/2.0, L, 900,endpoint=True)

#set some figure parameters
ax[0].axis([-L,L,0.0,1.2*Vo])
ax[0].set_xlabel(r'$X$ (Angstroms)')
ax[0].set_ylabel(r'$\psi(x)$')

# Define the maximum amplitude of the wavefunction
if (nstates > 1):
    amp = np.sqrt((E_vals[1]-E_vals[0])/1.5)
else:
    amp = np.sqrt((Vo-E_vals[0])/1.5)
    
# Plot the wavefunctions
for n in range(1,nstates+1):
    ax[0].hlines(E_vals[n-1], -L, L, linewidth=1.8, linestyle='--', color="black")
    k = 2.0*np.sqrt(E_vals[n-1])*val
    a0 = 2.0*np.sqrt(Vo-E_vals[n-1])*val
    # Plotting odd wavefunction
    if (n%2==0):
        ax[0].plot(X_lef,E_vals[n-1]-amp*np.exp(a0*L/2.0)*np.sin(k*L/2.0)*np.exp(a0*X_lef), color="red", label="", linewidth=2.8)
        ax[0].plot(X_mid,E_vals[n-1]+amp*np.sin(k*X_mid), color="red", label="", linewidth=2.8)
        ax[0].plot(X_rig,E_vals[n-1]+amp*np.exp(a0*L/2.0)*np.sin(k*L/2.0)*np.exp(-a0*X_rig), color="red", label="", linewidth=2.8)
    # Plot even wavefunction
    else:
        ax[0].plot(X_lef,E_vals[n-1]+amp*np.exp(a0*L/2.0)*np.cos(k*L/2.0)*np.exp(a0*X_lef), color="red", label="", linewidth=2.8)
        ax[0].plot(X_mid,E_vals[n-1]+amp*np.cos(k*X_mid), color="red", label="", linewidth=2.8)
        ax[0].plot(X_rig,E_vals[n-1]+amp*np.exp(a0*L/2.0)*np.cos(k*L/2.0)*np.exp(-a0*X_rig), color="red", label="", linewidth=2.8)

#create the potential
x = np.linspace(-L,L,1000)
Vx = potential(x, Vo, L)
ax[0].plot(x,Vx, color='blue',linewidth=1.5)

#create a legend
handles, labels = ax[0].get_legend_handles_labels()
line = Line2D([0], [0], label='Wavefunction $\psi(x)$', color='red', linestyle='-')
handles.append(line)
line = Line2D([0], [0], label='Energy Level $E_n$', color='black', linestyle='--')
handles.append(line)
line = Line2D([0], [0], label='Potential $V_0$', color='blue', linestyle='-')
handles.append(line)
ax[0].legend(handles=handles, loc=2);

#start plotting the probability densities
#axis properties for probability densities
ax[1].axis([-L,L,0.0,1.2*Vo])
ax[1].set_xlabel(r'$x$ (Angstroms)')
ax[1].set_ylabel(r'$|\psi(x)|^2$')

#Label the potential
str1="$V_o = %.3f$ eV"%(Vo)
ax[1].text(1.1*L, 1.02*Vo, str1, fontsize=14, color="blue")

# Defining the maximum amplitude of the probability density
if (nstates > 1):
    amp = (E_vals[1]-E_vals[0])/1.5
else:
    amp = (Vo-E_vals[0])/1.5

# Plot the probability densities
for n in range(1,nstates+1):
    ax[1].hlines(E_vals[n-1], -L, L, linewidth=1.8, linestyle='--', color="black")
    str1="$n = "+str(n)+r"$, $E_"+str(n)+r" = %.3f$ eV"%(E_vals[n-1])
    ax[1].text(1.1*L, E_vals[n-1]+0.01*Vo, str1, fontsize=12, color="red")
    k = 2.0*np.sqrt(E_vals[n-1])*val
    a0 = 2.0*np.sqrt(Vo-E_vals[n-1])*val
    # Plot odd probability densities
    if (n%2==0):
        Y_lef = E_vals[n-1]+amp*(np.exp(a0*L/2.0)*np.sin(k*L/2.0)*np.exp(a0*X_lef))**2
        ax[1].plot(X_lef,Y_lef, color="red", linewidth=2.8)
        ax[1].fill_between(X_lef, E_vals[n-1], Y_lef, color="green", alpha=0.7)
        ax[1].plot(X_mid,E_vals[n-1]+amp*(np.sin(k*X_mid))**2, color="red", label="", linewidth=2.8)
        Y_rig = E_vals[n-1]+amp*(np.exp(a0*L/2.0)*np.sin(k*L/2.0)*np.exp(-a0*X_rig))**2
        ax[1].plot(X_rig,Y_rig, color="red", linewidth=2.8)
        ax[1].fill_between(X_rig, E_vals[n-1], Y_rig, color="green", alpha=0.7)
    # Plot even probability densities
    else:
        Y_lef = E_vals[n-1]+amp*(np.exp(a0*L/2.0)*np.cos(k*L/2.0)*np.exp(a0*X_lef))**2
        ax[1].plot(X_lef,Y_lef, color="red", linewidth=2.8)
        ax[1].fill_between(X_lef, E_vals[n-1], Y_lef, color="green", alpha=0.7)
        ax[1].plot(X_mid,E_vals[n-1]+amp*(np.cos(k*X_mid))**2, color="red", label="", linewidth=2.8)
        Y_rig = E_vals[n-1]+amp*(np.exp(a0*L/2.0)*np.cos(k*L/2.0)*np.exp(-a0*X_rig))**2
        ax[1].plot(X_rig,Y_rig, color="red", linewidth=2.8)
        ax[1].fill_between(X_rig, E_vals[n-1], Y_rig, color="green", alpha=0.7)


#create a legend
handles, labels = ax[1].get_legend_handles_labels()
line = Line2D([0], [0], label='Probability Density $|\psi(x)|^2$', color='red', linestyle='-')
handles.append(line)
line = Line2D([0], [0], label='Energy Level $E_n$', color='black', linestyle='--')
handles.append(line)
line = Line2D([0], [0], label='Potential $V_0$', color='blue', linestyle='-')
handles.append(line)
patch = mpatches.Patch(color='green', alpha=0.7, label='Probability of being in \nclassically forbidden region')
handles.append(patch)
ax[1].legend(handles=handles, loc=2);

ax[1].plot(x,Vx, color='blue',linewidth=1.5)

plt.show()

plt.show()


#figstring = 'Figure 2.6.'+str(fig_no)+': label.'
#fig_no+=1
#display(Markdown(figstring))
```

- From these plots we can explain some of the behaviour of the energy levels as $L$ and $V_0$ are changed.

- The first thing to note from the diagram above is that the wavefunctions extend outside the potential; they enter what is sometimes called the classically forbidden region.
- As with the potential step, the quantum description of the particle allows it to tunnel into a region where the potential is larger than the energy of the particle. This is indicated by the shaded green area in the probability density plot. Note that this area gets larger as $V_0-E$ approaches zero.

### Tunneling of particle in the box

- **The tunneling probability** corresponds to the area outside the box that has non-zero probability density. In the graphical representation, those areas are shaded green. Integrating over those areas gives the probability that the particle tunnels outside the classically allowed region.

$$ 
P\left(-\frac{L}{2}>x>\frac{L}{2}\right)= \frac{\text{The area of the probability density that is shaded green}}{\text{The total area of the probability density}}\\
=\large{\frac{\int^{\frac{-L}{2}}_{-\infty} |\psi(x)|^2\ dx +\int^{+\infty}_{\frac{L}{2}} |\psi(x)|^2\ dx }{\int_{-\infty}^{+\infty} |\psi(x)|^2\ dx }}
$$

- We can calculate $P(-L/2>x>L/2)$, i.e. the size of the shaded green area as a percentage of the total area:

```{code-cell} python
:tags: [hide-input]
print ("\nThe tunneling probabilities are:")
for n in range(1,nstates+1):
    k = 2.0*np.sqrt(E_vals[n-1])*val
    a0 = 2.0*np.sqrt(Vo-E_vals[n-1])*val
    # For odd solution
    if (n%2==0):
        C = 1.0
        D = np.exp(a0*L/2.0)*np.sin(k*L/2.0)*C
        prob = D*D*2.0*k*np.exp(-a0*L)/(C*C*a0*(k*L-np.sin(k*L))+D*D*2.0*k*np.exp(-a0*L))
    # For even solution
    else:
        B = 1.0
        D = np.exp(a0*L/2.0)*np.cos(k*L/2.0)*B
        prob = D*D*2.0*k*np.exp(-a0*L)/(B*B*a0*(k*L+np.sin(k*L))+D*D*2.0*k*np.exp(-a0*L))
    print("  State #%3d tunneling probability = %5.2f%%" % (n,100*prob))
```



### A comparison between the energies of an infinite and a finite square well

These values confirm what we have already deduced: the closer the state is to the top of the potential, the more easily it spreads outside the well. How does this affect the energy levels? Lower in the potential, the wavelength of the wavefunction is more closely tied to the width of the well than it is higher up. Compare the infinite and finite square wells of the same width below.

```{marimo} python
:hide-code: true

Vo2 = mo.ui.slider(0.5, 10.0, step=0.5, value=5.0, show_value=True, label="well depth V0 (eV)")
L2 = mo.ui.slider(2.0, 17.0, step=0.5, value=10.0, show_value=True, label="well width L (Angstrom)")
mo.hstack([Vo2, L2], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

_Vo2, _L2 = Vo2.value, L2.value
_fig2, _ax2 = plt.subplots(1, 2, figsize=(9, 5), sharey=True)

_n2 = 1
while En_box_m(_n2, _L2) < _Vo2:
    _c2 = "#d81b60" if _n2 % 2 else "#004d40"
    _axline = _ax2[0].hlines(En_box_m(_n2, _L2), -1, 1, color=_c2, ls="--", lw=1.8)
    _ax2[0].text(1.1, En_box_m(_n2, _L2), f"n={_n2}: {En_box_m(_n2, _L2):.2f} eV", fontsize=9, color=_c2, va="center")
    _n2 += 1
_ax2[0].set_title("Infinite well (same width)")
_ax2[0].set_ylabel(r"$E_n$ (eV)")
_ax2[0].set_xticks([])
_ax2[0].set_xlim(-1, 3.2)

_ens2 = find_states_m(_Vo2, _L2)
for _k2, _e2 in enumerate(_ens2, start=1):
    _c2 = "#d81b60" if _k2 % 2 else "#004d40"
    _ax2[1].hlines(_e2, -1, 1, color=_c2, ls="--", lw=1.8)
    _ax2[1].text(1.1, _e2, f"n={_k2}: {_e2:.2f} eV", fontsize=9, color=_c2, va="center")
_ax2[1].hlines(_Vo2, -1, 1, color="#3d81f6", lw=2.5)
_ax2[1].text(1.1, _Vo2, f"$V_0$ = {_Vo2:.1f} eV", fontsize=10, color="#3d81f6", va="center")
_ax2[1].set_title("Finite well")
_ax2[1].set_xticks([])
_ax2[1].set_xlim(-1, 3.2)
_ax2[1].set_ylim(0, _Vo2 * 1.2)
plt.tight_layout()
plt.gcf()
```

- Notice that at energies closer to zero, the infinite and finite energies are closer together. As the energy of the state approaches the top of the finite potential, it is smaller in the finite well than in the infinite well. Why? The higher-energy states allow the wavefunction in the finite square well to spread out, so the wavelength is longer in the finite well than in the infinite well. A longer wavelength corresponds to a smaller wavenumber $k$, and hence a lower energy.
