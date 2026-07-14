# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "marimo",
#     "numpy",
#     "matplotlib",
#     "plotly",
#     "sympy",
# ]
#
# [tool.marimo.runtime]
# auto_instantiate = true
# on_cell_change = "autorun"
# ///

import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", app_title="Project: Particle in a Box")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Project 1: Particle in a Box

    This notebook is your first computational project. Work through the guided
    sections, then complete the three tasks at the bottom. Every cell reruns
    automatically when anything it depends on changes, so play with the sliders
    freely: you cannot break anything.

    **How to submit**: when you are done, use File > Download to save this
    notebook as a `.py` file and upload it to Canvas.
    """)
    return


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go

    return go, np, plt


@app.cell
def _(np):
    h, m = 1, 1  # atomic-style units
    hbar = h / (2 * np.pi)

    def Epib1d(n=1, L=1):
        """Energy of the 1D particle-in-a-box state n in a box of length L."""
        return (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)

    def psi(x, n=1, L=1):
        """Normalized 1D particle-in-a-box wavefunction evaluated at x."""
        return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

    def psi3d(x, y, z, nx=1, ny=1, nz=1, lx=1, ly=1, lz=1):
        """Normalized 3D box wavefunction as a product of 1D solutions."""
        return psi(x, nx, lx) * psi(y, ny, ly) * psi(z, nz, lz)

    def E3d(nx, ny, nz, lx, ly, lz):
        """Energy of the 3D box state (nx, ny, nz)."""
        return Epib1d(nx, lx) + Epib1d(ny, ly) + Epib1d(nz, lz)

    return E3d, Epib1d, hbar, psi, psi3d


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. The 1D box, interactively

    Drag the sliders: energies scale as $n^2 / L^2$, and the probability density
    $\psi_n^2(x)$ develops $n - 1$ nodes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    box_L = mo.ui.slider(0.5, 2.0, step=0.1, value=1.0, show_value=True, label="box length L")
    n_pick = mo.ui.slider(1, 10, step=1, value=3, show_value=True, label="quantum number n")
    mo.hstack([box_L, n_pick], justify="start", gap=2)
    return box_L, n_pick


@app.cell(hide_code=True)
def _(Epib1d, box_L, n_pick, np, plt, psi):
    fig1d, (ax_lev, ax_psi) = plt.subplots(figsize=(9, 4.5), ncols=2)

    for n_i in range(1, n_pick.value + 1):
        E_i = Epib1d(n_i, box_L.value)
        ax_lev.hlines(E_i, 0.5, 1.5, colors="steelblue", linewidth=2)
        ax_lev.text(1.6, E_i, f"n={n_i}, E={E_i:.2f}", verticalalignment="center", fontsize=9)
    ax_lev.set_xlim(0, 3)
    ax_lev.set_ylim(0, Epib1d(n_pick.value + 1, box_L.value))
    ax_lev.set_ylabel("energy")
    ax_lev.set_title("energy levels", fontsize=11)
    ax_lev.axes.get_xaxis().set_visible(False)

    x_grid = np.linspace(0, box_L.value, 1000)
    ax_psi.fill_between(x_grid, psi(x_grid, n_pick.value, box_L.value) ** 2, color="seagreen", alpha=0.8)
    ax_psi.axvline(0, color="red", lw=3)
    ax_psi.axvline(box_L.value, color="red", lw=3)
    ax_psi.set_xlim(-0.1, box_L.value + 0.1)
    ax_psi.set_ylim(0, 4)
    ax_psi.set_xlabel("x")
    ax_psi.set_ylabel(r"$\psi_n^2(x)$")
    ax_psi.set_title(f"probability density, n={n_pick.value}", fontsize=11)

    fig1d.tight_layout()
    fig1d
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. The 3D box

    The wavefunction is a product $\psi_{n_x}(x)\,\psi_{n_y}(y)\,\psi_{n_z}(z)$.
    The isosurfaces below show the wavefunction at values $\pm A$: blue and red
    lobes are separated by nodal planes, exactly like atomic orbitals. Rotate the
    figure with your mouse.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    nx_pick = mo.ui.slider(1, 4, step=1, value=2, show_value=True, label="nx")
    ny_pick = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="ny")
    nz_pick = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="nz")
    mo.hstack([nx_pick, ny_pick, nz_pick], justify="start", gap=2)
    return nx_pick, ny_pick, nz_pick


@app.cell(hide_code=True)
def _(go, np, nx_pick, ny_pick, nz_pick, psi3d):
    box3 = 10.0
    grid3 = np.linspace(0, box3, 48)
    X3, Y3, Z3 = np.meshgrid(grid3, grid3, grid3, indexing="ij")
    psi_vals = psi3d(X3, Y3, Z3, nx_pick.value, ny_pick.value, nz_pick.value, box3, box3, box3)
    amp = 0.5 * np.abs(psi_vals).max()

    fig3d = go.Figure(
        data=go.Isosurface(
            x=X3.flatten(),
            y=Y3.flatten(),
            z=Z3.flatten(),
            value=psi_vals.flatten(),
            colorscale="RdBu",
            isomin=-amp,
            isomax=amp,
            surface_count=2,
            showscale=False,
            caps=dict(x_show=False, y_show=False, z_show=False),
        )
    )
    fig3d.update_layout(
        scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="z", aspectmode="data"),
        width=700,
        height=480,
        title_text=f"wavefunction isosurfaces at +/- A, state ({nx_pick.value}, {ny_pick.value}, {nz_pick.value})",
    )
    fig3d
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Energy ladders and degeneracy

    Each Cartesian direction contributes its own ladder of levels. When the box
    is a perfect cube the ladders coincide and states such as $(2,1,1)$,
    $(1,2,1)$, $(1,1,2)$ are **degenerate**. Stretch one side and watch the
    ladders (and the degeneracy) split.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    lx_a = mo.ui.slider(0.5, 2.0, step=0.25, value=1.0, show_value=True, label="box side lx")
    ly_a = mo.ui.slider(0.5, 2.0, step=0.25, value=1.0, show_value=True, label="box side ly")
    lz_a = mo.ui.slider(0.5, 2.0, step=0.25, value=1.0, show_value=True, label="box side lz")
    mo.hstack([lx_a, ly_a, lz_a], justify="start", gap=2)
    return lx_a, ly_a, lz_a


@app.cell(hide_code=True)
def _(Epib1d, lx_a, ly_a, lz_a, plt):
    n_ladder = 6
    fig_lad, ax_lad = plt.subplots(figsize=(7, 4.5))
    for (side, x0, x1, color, name) in [
        (lx_a.value, 0.6, 1.0, "steelblue", "x"),
        (ly_a.value, 1.1, 1.5, "seagreen", "y"),
        (lz_a.value, 1.6, 2.0, "goldenrod", "z"),
    ]:
        for n_j in range(1, n_ladder + 1):
            ax_lad.hlines(Epib1d(n_j, side), x0, x1, colors=color, linewidth=2)
        ax_lad.text((x0 + x1) / 2, -1.5, name, ha="center")
    ax_lad.set_xlim(0.5, 2.1)
    ax_lad.set_ylim(-3, Epib1d(n_ladder, min(lx_a.value, ly_a.value, lz_a.value)) * 1.05)
    ax_lad.set_ylabel("energy")
    ax_lad.set_title("1D level ladders for each direction", fontsize=11)
    ax_lad.axes.get_xaxis().set_visible(False)
    fig_lad.tight_layout()
    fig_lad
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Symbolic quantum mechanics with sympy

    Let the computer carry out the operator algebra for $\langle p^2 \rangle$.
    First the wavefunction:
    """)
    return


@app.cell
def _():
    from sympy import symbols, sqrt, sin, pi, diff, integrate, simplify

    x, L, n, hbar_s = symbols("x L n hbar", real=True, positive=True)

    psi_n = sqrt(2 / L) * sin(n * pi * x / L)
    psi_n
    return L, diff, hbar_s, integrate, n, psi_n, simplify, x


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Apply the operator $\hat{p}^2 = -\hbar^2 \, d^2/dx^2$:
    """)
    return


@app.cell
def _(diff, hbar_s, psi_n, x):
    op_psi = -hbar_s**2 * diff(psi_n, x, x)
    op_psi
    return (op_psi,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Sandwich it between wavefunctions and integrate over the box:
    """)
    return


@app.cell
def _(L, integrate, op_psi, psi_n, simplify, x):
    p2_expect = simplify(integrate(psi_n * op_psi, (x, 0, L)))
    p2_expect
    return (p2_expect,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Check: $\langle p^2 \rangle / 2m$ reproduces the energy $E_n$, as it must for
    a state with zero potential energy.

    ---

    ## Your turn

    Complete the three tasks below in the empty cells. Add as many cells as you
    like (click + below any cell).

    **Task 1: Uncertainty product.** Using the sympy symbols already defined,
    compute $\langle x \rangle$ and $\langle x^2 \rangle$ for state $n$, then
    form $\Delta x \, \Delta p = \sqrt{\langle x^2\rangle - \langle x\rangle^2}
    \cdot \sqrt{\langle p^2 \rangle}$. Verify that the ground state respects
    $\Delta x \, \Delta p \ge \hbar / 2$ and report how the product grows with
    $n$.
    """)
    return


@app.cell
def _():
    # TODO Task 1: compute <x> and <x2> with sympy.integrate, then the
    # uncertainty product for n = 1, 2, 3 (use .subs(n, value) and simplify)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Task 2: Classical limit.** Compute the probability of finding the particle
    in the middle third of the box, $P_n = \int_{L/3}^{2L/3} \psi_n^2 \, dx$,
    and plot $P_n$ for $n = 1$ to $20$. What value does it approach, and why is
    that the classical answer?
    """)
    return


@app.cell
def _():
    # TODO Task 2: integrate psi(x, n, L)**2 numerically (np.trapezoid) or
    # symbolically, collect P_n for n = 1..20, and plot P_n vs n
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Task 3: Degeneracy count.** For a cubic box, use `E3d` to list the six
    lowest distinct energies and the states $(n_x, n_y, n_z)$ that share each of
    them. Then stretch one side by 10 percent and report which degeneracies
    survive.
    """)
    return


@app.cell
def _():
    # TODO Task 3: loop nx, ny, nz over 1..4, group states by E3d value
    # (round to 6 decimals), and print the degeneracy table for both boxes
    return


if __name__ == "__main__":
    app.run()
