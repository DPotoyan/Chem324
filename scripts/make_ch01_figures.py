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
BLACK = "#111111"
T = 5000
nu = np.linspace(1e12, 2.0e15, 800)
planck = 8 * np.pi * h * nu**3 / c**3 / np.expm1(h * nu / (kB * T))
rj = 8 * np.pi * nu**2 * kB * T / c**3
fig, ax = plt.subplots(figsize=(7.2, 4.8))
ax.plot(nu / 1e14, rj, "--", color=TEAL, lw=3.2, label="Rayleigh-Jeans (classical)")
ax.plot(nu / 1e14, planck, color=CARDINAL, lw=3.6, label="Planck (quantum)")
ax.set_ylim(0, 2.6 * planck.max()); ax.set_xlim(0, 20)
ax.set_xlabel(r"frequency $\nu$ (10$^{14}$ Hz)", fontsize=15, color=BLACK)
ax.set_ylabel(r"energy density $\rho_\nu$", fontsize=15, color=BLACK)
ax.set_yticks([]); ax.tick_params(axis="x", labelsize=13, colors=BLACK)
for sp in ["left", "bottom"]: ax.spines[sp].set_linewidth(1.4)
ax.annotate("ultraviolet catastrophe:\nclassical curve never comes down", xy=(1.95, 2.45 * planck.max()), xytext=(3.4, 2.0 * planck.max()),
            fontsize=13, color=BLACK, arrowprops=dict(arrowstyle="->", color=BLACK, lw=1.4))
ax.annotate("curves agree at\nlow frequency", xy=(1.0, planck[np.argmin(abs(nu / 1e14 - 1.0))]), xytext=(3.2, 1.35 * planck.max()),
            fontsize=13, color=BLACK, arrowprops=dict(arrowstyle="->", color=BLACK, lw=1.4))
ax.text(12, 0.55 * planck.max(), f"T = {T} K", fontsize=14, color=BLACK)
ax.legend(frameon=False, loc="center right", fontsize=13)
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

# ---------------------------------------------------------------- 2b. Planck curve family vs frequency (tab twin of the wavelength plot)
nu_f = np.linspace(1e12, 2.2e15, 1000)
fig, ax = plt.subplots(figsize=(6.8, 4.2))
peaks = []
for i, Ti in enumerate(Ts):
    rho = 8 * np.pi * h * nu_f**3 / c**3 / np.expm1(h * nu_f / (kB * Ti))
    ax.plot(nu_f / 1e14, rho, color=HOT2COLD[i], lw=2.2, label=f"{Ti} K")
    peaks.append((nu_f[np.argmax(rho)] / 1e14, rho.max()))
px, py = zip(*peaks)
ax.plot(px, py, ":", color=GRAY, lw=1.2)
ax.annotate("Wien's law: peak moves to\nhigher frequency as T rises", xy=(px[-1], py[-1]), xytext=(px[-1] + 3.5, py[-1] * 0.95),
            fontsize=9.5, color=GRAY, arrowprops=dict(arrowstyle="->", color=GRAY))
ax.axvspan(c / 750e-9 / 1e14, c / 380e-9 / 1e14, color="gold", alpha=0.15)
ax.text((c / 750e-9 + c / 380e-9) / 2e14, py[-1] * 1.04, "visible", ha="center", fontsize=9, color="darkgoldenrod")
ax.set_xlim(0, 22); ax.set_ylim(0, py[-1] * 1.12); ax.set_yticks([])
ax.set_xlabel(r"frequency $\nu$ (10$^{14}$ Hz)"); ax.set_ylabel(r"energy density $\rho_\nu$")
ax.legend(frameon=False, fontsize=9.5, loc="center right", title="temperature", title_fontsize=9.5)
fig.tight_layout(); fig.savefig(f"{OUT}/planck_curves_nu.png", dpi=200)

# ---------------------------------------------------------------- 2c. counting wave modes in a box (1D)
BLACK = "#111111"
fig, b1 = plt.subplots(figsize=(7.2, 5.0))
L = 1.0; xb = np.linspace(0, L, 400)
for n in [1, 2, 3, 4]:
    y0 = -(n - 1) * 1.5
    b1.plot(xb, y0 + 0.55 * np.sin(n * np.pi * xb / L), color=HOT2COLD[min(n, 4)], lw=2.6)
    b1.plot([0, L], [y0, y0], color="#bbb", lw=0.8)
    b1.text(L + 0.07, y0, rf"$n$ = {n}:   $\lambda = 2L/{n}$", va="center", fontsize=14, color=BLACK)
b1.axvline(0, color=BLACK, lw=2.8); b1.axvline(L, color=BLACK, lw=2.8)
b1.annotate("", xy=(L, 1.0), xytext=(0, 1.0), arrowprops=dict(arrowstyle="<->", color=BLACK, lw=1.4))
b1.text(L / 2, 1.12, "box of size L", ha="center", fontsize=13, color=BLACK)
b1.text(1.0, -6.0, r"waves that fit up to frequency $\nu$:   $N = \dfrac{2L}{\lambda} = \dfrac{2L\,\nu}{c}$", fontsize=13, color=BLACK, ha="center", va="center", bbox=dict(fc="#f6f6f6", ec="#bbb", pad=6))
b1.set_xlim(-0.1, 2.2); b1.set_ylim(-6.7, 1.5); b1.axis("off")
b1.set_title("Only whole half-waves fit between the walls", fontsize=14, fontweight="bold", color=BLACK, pad=14)
fig.tight_layout(); fig.savefig(f"{OUT}/mode_counting.png", dpi=200)

# ---------------------------------------------------------------- 3. wave definitions
BLACK = "#111111"
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={"width_ratios": [1, 1.1]})
x = np.linspace(0, 3, 600); A = 1.0
a1.plot(x, A * np.sin(2 * np.pi * x), color=TEAL, lw=2.6)
a1.axhline(0, color=BLACK, ls="--", lw=1)
# peaks of sin(2 pi x) sit at x = 0.25, 1.25, 2.25
a1.annotate("", xy=(1.25, 1.32), xytext=(0.25, 1.32), arrowprops=dict(arrowstyle="<->", color=BLACK, lw=1.6, shrinkA=0, shrinkB=0))
a1.plot([0.25, 0.25], [1.0, 1.32], color=BLACK, lw=0.8, ls=":"); a1.plot([1.25, 1.25], [1.0, 1.32], color=BLACK, lw=0.8, ls=":")
a1.text(0.75, 1.42, r"wavelength $\lambda$", ha="center", color=BLACK, fontsize=14)
a1.annotate("", xy=(2.25, 1.0), xytext=(2.25, 0.0), arrowprops=dict(arrowstyle="<->", color=BLACK, lw=1.6, shrinkA=0, shrinkB=0))
a1.text(2.33, 0.5, "amplitude", va="center", color=BLACK, fontsize=14)
a1.text(1.36, 1.02, "peak", ha="left", fontsize=13, color=BLACK); a1.text(1.75, -1.2, "trough", ha="center", fontsize=13, color=BLACK)
a1.set_xlim(-0.05, 3.05); a1.set_ylim(-1.45, 1.75); a1.axis("off")
a1.set_title("One wave: wavelength and amplitude", fontsize=15, fontweight="bold", color=BLACK, pad=22)
xs = np.linspace(0, 1, 1200)
for k, (nu_k, col) in enumerate(zip([4, 8, 16], [HOT2COLD[0], HOT2COLD[2], HOT2COLD[4]])):
    y0 = -k * 2.7
    a2.plot(xs, y0 + np.sin(2 * np.pi * nu_k * xs), color=col, lw=2.4)
    a2.text(1.03, y0, rf"$\nu$ = {nu_k} Hz", va="center", fontsize=14, color=BLACK)
    lam_k = 1 / nu_k
    x_peak = 1 / (4 * nu_k) + np.ceil((0.45 - 1 / (4 * nu_k)) * nu_k) / nu_k  # first peak past x = 0.45
    a2.annotate("", xy=(x_peak + lam_k, y0 + 1.22), xytext=(x_peak, y0 + 1.22), arrowprops=dict(arrowstyle="<->", color=BLACK, lw=1.4, shrinkA=0, shrinkB=0))
    a2.plot([x_peak, x_peak], [y0 + 1.0, y0 + 1.22], color=BLACK, lw=0.8, ls=":"); a2.plot([x_peak + lam_k, x_peak + lam_k], [y0 + 1.0, y0 + 1.22], color=BLACK, lw=0.8, ls=":")
    a2.text(x_peak + lam_k / 2, y0 + 1.36, rf"$\lambda_{k+1}$", ha="center", fontsize=13, color=BLACK)
a2.axvline(0, color=BLACK, ls="--", lw=1); a2.axvline(1, color=BLACK, ls="--", lw=1)
a2.annotate("", xy=(1, 2.0), xytext=(0, 2.0), arrowprops=dict(arrowstyle="->", color=BLACK, lw=1.4))
a2.text(0.5, 2.15, "distance the wave travels in 1 second", ha="center", fontsize=13, color=BLACK)
a2.set_xlim(-0.05, 1.36); a2.set_ylim(-6.8, 2.7); a2.axis("off")
a2.set_title("Same speed c: higher frequency, shorter wavelength", fontsize=15, fontweight="bold", color=BLACK, pad=22)
fig.tight_layout(h_pad=1.0); fig.subplots_adjust(top=0.86)
fig.savefig(f"{OUT}/wave_definitions.png", dpi=200)

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

# ---------------------------------------------------------------- 5b. why the classical wave picture fails
fig, d1 = plt.subplots(figsize=(7.6, 4.6))
schematic_axes(d1, "light intensity (brightness)", "electron kinetic energy")
d1.xaxis.label.set_size(16); d1.yaxis.label.set_size(16)
d1.plot([0, 0.9], [0.1, 0.75], "--", color=TEAL, lw=3.2)
d1.text(0.48, 0.72, "KE predicted by\nclassical physics", color=TEAL, fontsize=17, ha="center")
d1.plot([0, 0.9], [0.32, 0.32], color=CARDINAL, lw=3.4)
d1.text(0.45, 0.20, "observed KE", color=CARDINAL, fontsize=17, ha="center")
fig.tight_layout(); fig.savefig(f"{OUT}/photoelectric_classical_fail.png", dpi=200)

# ---------------------------------------------------------------- 5c. wave vs photon stream
fig, (e1, e2) = plt.subplots(2, 1, figsize=(8.5, 4.6), sharex=True)
xw = np.linspace(0, 10, 800)
e1.plot(xw, 0.8 * np.sin(2 * np.pi * 1.2 * xw), color=TEAL, lw=2.4)
e1.set_ylim(-1.6, 1.6); e1.axis("off")
e1.set_title("classical picture: a continuous wave, energy set by its amplitude", fontsize=13, color=BLACK, fontweight="bold")
rng2 = np.random.default_rng(3)
xp = np.linspace(0.4, 9.6, 14) + rng2.uniform(-0.15, 0.15, 14)
yp = rng2.uniform(-0.75, 0.75, 14)
e2.scatter(xp, yp, s=180, color=CARDINAL, alpha=0.9, edgecolors="white")
for xi, yi in zip(xp[::3], yp[::3]):
    e2.text(xi, yi + 0.42, r"$h\nu$", fontsize=12, ha="center", color=CARDINAL)
e2.annotate("", xy=(10.4, 0), xytext=(9.9, 0), arrowprops=dict(arrowstyle="->", color=BLACK, lw=1.6))
e2.set_ylim(-1.6, 1.6); e2.set_xlim(0, 10.6); e2.axis("off")
e2.set_title("Einstein's picture: a stream of packets, each carrying exactly E = hν", fontsize=13, color=BLACK, fontweight="bold")
fig.tight_layout(); fig.savefig(f"{OUT}/photon_stream.png", dpi=200)

# ---------------------------------------------------------------- 6. photoelectric schematics
nu0 = 0.35
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.4))
schematic_axes(a1, "light frequency", "electron kinetic energy")
a1.plot([0, nu0], [0, 0], color=CARDINAL, lw=3.2); a1.plot([nu0, 0.95], [0, 0.8], color=CARDINAL, lw=3.2)
a1.text(nu0 - 0.025, 0.05, r"$\nu_0$", ha="right", color=CARDINAL, fontsize=17)
a1.text(0.56, 0.33, "slope = h", color=GRAY, fontsize=14, rotation=np.degrees(np.arctan2(0.8, 0.6)), transform_rotates_text=True, rotation_mode="anchor")
schematic_axes(a2, "light intensity", "electron kinetic energy")
a2.plot([0, 0.95], [0.55, 0.55], color=CARDINAL, lw=3.2); a2.text(0.5, 0.61, r"$\nu > \nu_0$", ha="center", color=CARDINAL, fontsize=17)
a2.plot([0, 0.95], [0, 0], color=CARDINAL, lw=3.2); a2.text(0.5, 0.06, r"$\nu < \nu_0$", ha="center", color=CARDINAL, fontsize=17)
for ax in (a1, a2):
    ax.xaxis.label.set_size(16); ax.yaxis.label.set_size(16)
fig.tight_layout(); fig.savefig(f"{OUT}/photoelectric_ke.png", dpi=200)

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.4))
schematic_axes(a1, "light frequency", "electron current")
a1.plot([0, nu0, nu0, 0.95], [0, 0, 0.6, 0.6], color=CARDINAL, lw=3.2)
a1.text(nu0 - 0.025, 0.05, r"$\nu_0$", ha="right", color=CARDINAL, fontsize=17)
schematic_axes(a2, "light intensity", "electron current")
a2.plot([0, 0.95], [0, 0.85], color=CARDINAL, lw=3.2); a2.text(0.32, 0.62, r"for $\nu > \nu_0$", color=CARDINAL, fontsize=17)
for ax in (a1, a2):
    ax.xaxis.label.set_size(16); ax.yaxis.label.set_size(16)
fig.tight_layout(); fig.savefig(f"{OUT}/photoelectric_current.png", dpi=200)
