"""Regenerate the simple schematic figures of chapter 1 as crisp matplotlib PNGs (dpi 200).

Run from the repo root:  .venv/bin/python scripts/make_ch01_figures.py
Outputs go to ch01/images/ and are referenced by the ch01 pages and slides/ch01 decks.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

OUT = "ch01/images"
TEAL, CARDINAL, GRAY = "#107895", "#C8102E", "#6c757d"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})


def schematic_axes(ax, xlabel, ylabel):
    """Bare axes with arrowheads and no ticks, for qualitative plots."""
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    for s in ["top", "right"]: ax.spines[s].set_visible(False)
    ax.spines["left"].set_position(("data", 0)); ax.spines["bottom"].set_position(("data", 0))
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=6)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=6)
    ax.set_xlabel(xlabel, fontsize=11, color=TEAL, style="italic")
    ax.set_ylabel(ylabel, fontsize=11, color=TEAL, style="italic")


# ---------------------------------------------------------------- 1. UV catastrophe
h, c, kB = 6.626e-34, 2.998e8, 1.381e-23
T = 5000
nu = np.linspace(1e12, 2.0e15, 800)
planck = 8 * np.pi * h * nu**3 / c**3 / np.expm1(h * nu / (kB * T))
rj = 8 * np.pi * nu**2 * kB * T / c**3
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.plot(nu / 1e14, rj, "--", color=TEAL, lw=2, label="Rayleigh-Jeans (classical)")
ax.plot(nu / 1e14, planck, color=CARDINAL, lw=2.4, label="Planck (quantum)")
ax.set_ylim(0, 2.6 * planck.max()); ax.set_xlim(0, 20)
ax.set_xlabel(r"frequency $\nu$ (10$^{14}$ Hz)"); ax.set_ylabel(r"energy density $\rho_\nu$")
ax.set_yticks([])
ax.annotate("ultraviolet catastrophe:\nclassical curve never comes down", xy=(1.95, 2.45 * planck.max()), xytext=(3.2, 2.05 * planck.max()),
            fontsize=10, color=TEAL, arrowprops=dict(arrowstyle="->", color=TEAL))
ax.annotate("curves agree at low frequency", xy=(1.0, planck[np.argmin(abs(nu / 1e14 - 1.0))]), xytext=(2.5, 1.5 * planck.max()),
            fontsize=10, color=GRAY, arrowprops=dict(arrowstyle="->", color=GRAY))
ax.text(12, 0.55 * planck.max(), f"T = {T} K", fontsize=10, color=GRAY)
ax.legend(frameon=False, loc="center right", fontsize=10)
fig.tight_layout(); fig.savefig(f"{OUT}/uv_catastrophe.png", dpi=200)

# ---------------------------------------------------------------- 2. Planck curve family
lam = np.linspace(80e-9, 2500e-9, 1000)
Ts = [3000, 4000, 5000, 6000, 7000]
HOT2COLD = ["#c0392b", "#e67e22", "#8e44ad", "#3498db", "#1f3a93"]  # increasing T: red to blue
fig, ax = plt.subplots(figsize=(6.8, 4.2))
peaks = []
for i, Ti in enumerate(Ts):
    rho = 8 * np.pi * h * c / lam**5 / np.expm1(h * c / (lam * kB * Ti))
    col = HOT2COLD[i]
    ax.plot(lam * 1e9, rho, color=col, lw=2.2, label=f"{Ti} K")
    peaks.append((2.898e-3 / Ti * 1e9, rho.max()))
px, py = zip(*peaks)
ax.plot(px, py, ":", color=GRAY, lw=1.2)
ax.annotate("Wien's law: peak moves to\nshorter wavelength as T rises", xy=(px[-1], py[-1]), xytext=(900, py[-1] * 0.95),
            fontsize=9.5, color=GRAY, arrowprops=dict(arrowstyle="->", color=GRAY))
ax.axvspan(380, 750, color="gold", alpha=0.15); ax.text(565, py[-1] * 1.04, "visible", ha="center", fontsize=9, color="darkgoldenrod")
ax.set_xlim(0, 2500); ax.set_ylim(0, py[-1] * 1.12); ax.set_yticks([])
ax.set_xlabel("wavelength (nm)"); ax.set_ylabel(r"energy density $\rho_\lambda$")
ax.legend(frameon=False, fontsize=9.5, loc="center right", title="temperature", title_fontsize=9.5)
fig.tight_layout(); fig.savefig(f"{OUT}/planck_curves.png", dpi=200)

# ---------------------------------------------------------------- 3. wave definitions
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1, 1.1]})
x = np.linspace(0, 3, 600); A = 1.0
a1.plot(x, A * np.sin(2 * np.pi * x), color=TEAL, lw=2.4)
a1.axhline(0, color=GRAY, ls="--", lw=1)
a1.annotate("", xy=(1.25, 1.3), xytext=(0.25, 1.3), arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.5))
a1.text(0.75, 1.4, r"wavelength $\lambda$", ha="center", color=CARDINAL, fontsize=11)
a1.annotate("", xy=(2.25, 1.0), xytext=(2.25, 0.0), arrowprops=dict(arrowstyle="<->", color=CARDINAL, lw=1.5))
a1.text(2.33, 0.5, "amplitude", va="center", color=CARDINAL, fontsize=11)
a1.text(0.25, 1.06, "peak", ha="center", fontsize=10, color="#333"); a1.text(0.75, -1.2, "trough", ha="center", fontsize=10, color="#333")
a1.set_xlim(-0.05, 3.05); a1.set_ylim(-1.45, 1.7); a1.axis("off")
a1.set_title("one wave: wavelength and amplitude", fontsize=11, color="#333")
xs = np.linspace(0, 1, 800)
for k, (nu_k, col) in enumerate(zip([4, 8, 16], [HOT2COLD[0], HOT2COLD[2], HOT2COLD[4]])):
    y0 = -k * 2.6
    a2.plot(xs, y0 + np.sin(2 * np.pi * nu_k * xs), color=col, lw=2.2)
    a2.text(1.03, y0, rf"$\nu$ = {nu_k} Hz", va="center", fontsize=11, color=col)
    lam_k = 1 / nu_k
    a2.annotate("", xy=(0.5 + lam_k, y0 + 1.15), xytext=(0.5, y0 + 1.15), arrowprops=dict(arrowstyle="<->", color=GRAY, lw=1.2))
    a2.text(0.5 + lam_k / 2, y0 + 1.3, rf"$\lambda_{k+1}$", ha="center", fontsize=10, color=GRAY)
a2.axvline(0, color=GRAY, ls="--", lw=1); a2.axvline(1, color=GRAY, ls="--", lw=1)
a2.annotate("", xy=(1, 1.9), xytext=(0, 1.9), arrowprops=dict(arrowstyle="->", color="#333", lw=1.2))
a2.text(0.5, 2.05, "distance the wave travels in 1 second", ha="center", fontsize=10.5, color="#333")
a2.set_xlim(-0.05, 1.32); a2.set_ylim(-6.6, 2.5); a2.axis("off")
a2.set_title("same speed c, higher frequency means shorter wavelength", fontsize=11, color="#333")
fig.tight_layout(); fig.savefig(f"{OUT}/wave_definitions.png", dpi=200)

# ---------------------------------------------------------------- 4. Bohr standing waves
fig, axes = plt.subplots(1, 2, figsize=(9, 4.4))
for ax, n, title in zip(axes, [4, 4.5], ["(a) allowed orbit:  $2\\pi r = n\\lambda$,  n = 4", "(b) forbidden orbit:  $2\\pi r \\neq n\\lambda$,  n = 4.5"]):
    th = np.linspace(0, 2 * np.pi if n == int(n) else 4 * np.pi, 2000)
    R, a = 1.0, 0.16
    ax.add_patch(Circle((0, 0), R, fill=False, color=GRAY, lw=1.2, ls="--"))
    ax.plot((R + a * np.sin(n * th)) * np.cos(th), (R + a * np.sin(n * th)) * np.sin(th), color="#6a3d9a", lw=2.2)
    ax.plot(0, 0, "o", color=CARDINAL, ms=9)
    ax.annotate("", xy=(R * np.cos(0.6), R * np.sin(0.6)), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="#333", lw=1))
    ax.text(0.5 * R * np.cos(0.6) + 0.05, 0.5 * R * np.sin(0.6) - 0.12, "r", fontsize=12, style="italic")
    ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.45, 1.45); ax.set_aspect("equal"); ax.axis("off")
    ax.set_title(title, fontsize=11, color="#333")
axes[0].text(0, -1.38, "the wave closes on itself: constructive interference", ha="center", fontsize=9.5, color=GRAY)
axes[1].text(0, -1.38, "the wave misses itself after each lap: it cancels out", ha="center", fontsize=9.5, color=GRAY)
fig.tight_layout(); fig.savefig(f"{OUT}/bohr_standing_waves.png", dpi=200)

# ---------------------------------------------------------------- 5. Bohr orbits with spectral series
fig, ax = plt.subplots(figsize=(6.4, 6.4))
nmax = 6
radii = {n: 0.9 * n for n in range(1, nmax + 1)}  # schematic spacing, not n^2
for n, r in radii.items():
    ax.add_patch(Circle((0, 0), r, fill=False, color="#bbb", lw=1))
    ang_l = np.deg2rad(215)
    ax.text(r * np.cos(ang_l), r * np.sin(ang_l), f"n = {n}", fontsize=8, color="#555", ha="center", va="center", bbox=dict(fc="white", ec="none", pad=1))
ax.plot(0, 0, "o", color=CARDINAL, ms=8)
series = [(1, "Lyman", "#6a3d9a", 100), (2, "Balmer", CARDINAL, 40), (3, "Paschen", "#e59866", -20)]
for n1, name, col, ang0 in series:
    for k, n2 in enumerate(range(n1 + 1, nmax + 1)):
        ang = np.deg2rad(ang0 - 7 * k)
        p2 = radii[n2] * np.array([np.cos(ang), np.sin(ang)]); p1 = radii[n1] * np.array([np.cos(ang), np.sin(ang)])
        ax.add_patch(FancyArrowPatch(p2, p1, arrowstyle="-|>", mutation_scale=12, color=col, lw=1.6, shrinkA=0, shrinkB=0))
    ang = np.deg2rad(ang0 - 7 * (nmax - n1 - 1) / 2)
    r_lab = radii[nmax] + 0.75
    ax.text(r_lab * np.cos(ang), r_lab * np.sin(ang), f"{name} series\n(to n = {n1})", ha="center", va="center", fontsize=10.5, color=col)
ax.text(0, -radii[nmax] - 0.5, "orbit spacing schematic, not to scale", ha="center", fontsize=8.5, color=GRAY)
ax.set_xlim(-6.4, 6.4); ax.set_ylim(-6.3, 6.4); ax.set_aspect("equal"); ax.axis("off")
fig.tight_layout(); fig.savefig(f"{OUT}/bohr_series_orbits.png", dpi=200)

# ---------------------------------------------------------------- 6. photoelectric schematics
nu0 = 0.35
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
schematic_axes(a1, "light frequency", "electron kinetic energy")
a1.plot([0, nu0], [0, 0], color=CARDINAL, lw=2.6); a1.plot([nu0, 0.95], [0, 0.8], color=CARDINAL, lw=2.6)
a1.text(nu0 - 0.025, 0.05, r"$\nu_0$", ha="right", color=CARDINAL, fontsize=12)
a1.text(0.58, 0.36, "slope = h", color=GRAY, fontsize=10, rotation=np.degrees(np.arctan2(0.8, 0.6)), transform_rotates_text=True, rotation_mode="anchor")
schematic_axes(a2, "light intensity", "electron kinetic energy")
a2.plot([0, 0.95], [0.55, 0.55], color=CARDINAL, lw=2.6); a2.text(0.5, 0.6, r"$\nu > \nu_0$", ha="center", color=CARDINAL, fontsize=12)
a2.plot([0, 0.95], [0, 0], color=CARDINAL, lw=2.6); a2.text(0.5, 0.05, r"$\nu < \nu_0$", ha="center", color=CARDINAL, fontsize=12)
fig.tight_layout(); fig.savefig(f"{OUT}/photoelectric_ke.png", dpi=200)

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
schematic_axes(a1, "light frequency", "electron current")
a1.plot([0, nu0, nu0, 0.95], [0, 0, 0.6, 0.6], color=CARDINAL, lw=2.6)
a1.text(nu0 + 0.03, 0.05, r"$\nu_0$", ha="left", color=CARDINAL, fontsize=12)
schematic_axes(a2, "light intensity", "electron current")
a2.plot([0, 0.95], [0, 0.85], color=CARDINAL, lw=2.6); a2.text(0.3, 0.6, r"for $\nu > \nu_0$", color=CARDINAL, fontsize=12)
fig.tight_layout(); fig.savefig(f"{OUT}/photoelectric_current.png", dpi=200)
print("done")
