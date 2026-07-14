# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "numpy",
#     "matplotlib",
#     "scipy",
# ]
#
# [tool.marimo.runtime]
# auto_instantiate = true
# on_cell_change = "autorun"
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", app_title="Project 4: Atomic Orbitals")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Project 4: Atomic Orbitals

    **Prerequisites**

    - The [hydrogen wavefunctions demo](https://dpotoyan.github.io/Chem324/demo-hydrogen-wavefunctions)
      and the [spherical harmonics demo](https://dpotoyan.github.io/Chem324/demo-spherical-harmonics):
      the plotting functions there are your starting points.

    **How to submit**: add your code below each problem, then File > Download the `.py`
    file and upload it to Canvas. Download your work at the end of every session.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.special import sph_harm_y, genlaguerre, factorial

    return factorial, genlaguerre, np, plt, sph_harm_y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Provided: the radial function

    $$R_{nl}(r) = \sqrt{\Big(\frac{2}{n a_0}\Big)^3 \frac{(n-l-1)!}{2n\,(n+l)!}}\;
    e^{-r/n a_0} \Big(\frac{2r}{n a_0}\Big)^{l} L^{2l+1}_{n-l-1}\Big(\frac{2r}{n a_0}\Big)$$

    with $a_0 = 1$ (Hartree atomic units). Note for the angular part: scipy's
    `sph_harm_y(l, m, theta, phi)` takes the **polar** angle $\theta$ first and the
    **azimuthal** angle $\phi$ second.
    """)
    return


@app.cell
def _(factorial, genlaguerre, np):
    def radial(r, n=1, l=0):
        """Normalized hydrogen radial function R_nl(r) in units of a0 = 1."""
        pre = np.sqrt((2 / n) ** 3 * factorial(n - l - 1) / (2 * n * factorial(n + l)))
        p = 2 * r / n
        return pre * np.exp(-p / 2) * p**l * genlaguerre(n - l - 1, 2 * l + 1)(p)

    return (radial,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Problem 1: Radial part of atomic orbitals

    - Using a few radial functions of the H atom, show that they are normalized and
      orthogonal (numerical integrals with `np.trapezoid`; remember the volume element
      $r^2\,dr$).
    - Compute and plot the probability of finding the electron within the first Bohr
      radius as a function of the quantum number $n$.
    - Compute $\langle 1/r \rangle$ numerically as a function of $n$ and compare with
      the analytical expression from the book.
    """)
    return


@app.cell
def _():
    # TODO Problem 1: radial integrals with np.trapezoid(f, r)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Problem 2: Angular part of atomic orbitals

    $$Y_{l}^{m}(\theta,\phi) = \sqrt{\frac{2l+1}{4\pi}\frac{(l-m)!}{(l+m)!}}\;
    P_{l}^{m}(\cos\theta)\, e^{i m \phi}$$

    - Show that spherical harmonics are normalized and orthogonal (the angular volume
      element is $\sin\theta \, d\theta \, d\phi$).
    - Modify the plotting function from the demo to use **real** combinations of
      $Y_l^m$ and reproduce the three $p$ orbitals and all five $d$ orbitals familiar
      to chemists.
    - Visualize a linear combination of one $s$ and one $p_z$ orbital with equal weights.
    - Visualize a linear combination of $s$, $p_x$ and $p_y$ orbitals with equal weights.
    - Visualize a linear combination of $s$ and all three $p$ orbitals with equal weights.
    """)
    return


@app.cell
def _():
    # TODO Problem 2: real orbitals from Y_l^m, e.g. p_x ~ (Y_1^-1 - Y_1^1) / sqrt(2)
    return


if __name__ == "__main__":
    app.run()
