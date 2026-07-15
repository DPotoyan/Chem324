# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "numpy",
#     "matplotlib",
# ]
#
# [tool.marimo.runtime]
# auto_instantiate = true
# on_cell_change = "autorun"
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", app_title="Project 1: Waves and Interference")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Project 1: Waves, Normal Modes and Interference

    **Prerequisites**

    - The [waves demo](https://dpotoyan.github.io/Chem324/demo-visualizing-waves): you can
      adapt its examples to solve most of these challenges.
    - The [Python and NumPy tutorials](https://dpotoyan.github.io/Chem324/python-basics)
      if you want a refresher on the basics.

    **How to submit**: work through the problems below, adding as many cells as you need.
    When done, use File > Download to save this notebook as a `.py` file and upload it to
    Canvas. Download your work at the end of every session; it is your safety copy.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    return np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Problem 1: Combining normal modes

    - Recreate figures 2.4, 2.6 and 2.7 of the book using linear combinations of normal
      modes of a vibrating string.
    - Recreate figure 2.4 for the case of combining 2D standing waves of a membrane.
    """)
    return


@app.cell
def _():
    # TODO Problem 1: build normal modes sin(n pi x / L) and combine them
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Problem 2: Beats and music

    Music is interesting because instruments mix changing frequencies. When two sounds
    with nearby frequencies interfere, you hear **beats**. Model the two sounds as a
    superposition (keeping only the temporal parts):

    $$s_1 + s_2 = A \sin(2 \pi \nu_1 t + \phi_1) + A \sin(2 \pi \nu_2 t + \phi_2)$$

    Steps:

    - Create time points with `t = np.arange(0, 2, 0.01)`.
    - Set $A = 1$, $\nu_1 = 10$, $\nu_2 = 11.5$, $\phi_1 = \phi_2 = 0$.
    - Compute $s_1 = A \cos(2\pi\nu_1 t + \phi_1)$ and $s_2 = A \cos(2\pi\nu_2 t + \phi_2)$.
    - Plot $s_1$, $s_2$, and $s_1 + s_2$ as three vertically stacked subplots.
    - Make the phase shift interactive with a `mo.ui.slider` and describe what it does.
    - Write a brief report of your observations in a markdown cell.
    """)
    return


@app.cell
def _():
    # TODO Problem 2: beats. Tip: fig, axes = plt.subplots(nrows=3, sharex=True)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Problem 3: Interference of spherical waves

    Disturb two points of a quiet lake and you get ripple interference, like in
    [this video](https://www.youtube.com/watch?v=ovZkFMuxZNc). Recreate the effect
    computationally: two sine waves $w_1 = \sin(k r_1)$ and $w_2 = \sin(k r_2)$ radiate
    from two centers in a 2D plane; their sum shows interference that depends on the
    separation of the centers. Complete the starter code below.
    """)
    return


@app.cell
def _(np):
    wavelength = 5.0
    k = 2 * np.pi / wavelength

    separation = 50.0      # separation of centers in cm
    side = 100.0           # side of the square region in cm
    points = 500           # grid points along each side

    # positions of the two wave centers
    x1, y1 = side / 2 + separation / 2, side / 2
    x2, y2 = side / 2 - separation / 2, side / 2

    # TODO: create 1D arrays with np.linspace, then X, Y = np.meshgrid(...)
    # TODO: r1 = np.sqrt((X - x1)**2 + (Y - y1)**2), same for r2
    # TODO: sum_waves = np.sin(k * r1) + np.sin(k * r2)
    # TODO: plt.imshow(sum_waves); explore different separations and wavelengths
    # optional: wrap it in a function and drive separation with mo.ui.slider
    return


if __name__ == "__main__":
    app.run()
