"""Crisp stills for the Appendix A decks (slides/math), dpi 200, saved into math/images/.
Run from the repo root:  .venv/bin/python scripts/make_math_figures.py
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = "math/images"
TEAL, CARDINAL, BLACK, GRAY = "#107895", "#C8102E", "#111111", "#6c757d"
plt.rcParams.update({"font.size": 12, "axes.spines.top": False, "axes.spines.right": False})

# ---------------------------------------------------------------- secant lines -> tangent
f = lambda x: x**2
x0 = 1.0; x = np.linspace(-0.5, 2.5, 400)
fig, ax = plt.subplots(figsize=(6.4, 4.8))
ax.plot(x, f(x), color=BLACK, lw=2.4, label=r"$f(x) = x^2$")
for h, col in zip([1.0, 0.5, 0.2], ["#e67e22", "#8e44ad", TEAL]):
    slope = (f(x0 + h) - f(x0)) / h
    ax.plot(x, f(x0) + slope * (x - x0), "--", color=col, lw=1.8, label=f"secant, h = {h} (slope {slope:.1f})")
    ax.plot([x0, x0 + h], [f(x0), f(x0 + h)], "o", color=col, ms=6)
ax.plot(x, f(x0) + 2 * (x - x0), color=CARDINAL, lw=2.6, label="tangent (slope 2)")
ax.plot(x0, f(x0), "o", color=BLACK, ms=7)
ax.set_xlim(-0.5, 2.5); ax.set_ylim(-1, 6); ax.set_xlabel("x"); ax.set_ylabel("f(x)")
ax.legend(fontsize=10, loc="upper left", frameon=False)
ax.set_title("Secant lines pivot into the tangent as h shrinks", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/secant_tangent.png", dpi=200)

# ---------------------------------------------------------------- Riemann sums
a, b = 0, 2; xs = np.linspace(a, b, 400)
fig, axes = plt.subplots(1, 3, figsize=(11, 3.8), sharey=True)
for ax, n in zip(axes, [4, 8, 32]):
    edges = np.linspace(a, b, n + 1); mids = 0.5 * (edges[:-1] + edges[1:]); dx = (b - a) / n
    ax.bar(mids, f(mids), width=dx, align="center", color=TEAL, edgecolor="white", alpha=0.75)
    ax.plot(xs, f(xs), color=BLACK, lw=2.2)
    ax.set_title(f"n = {n},   sum = {np.sum(f(mids) * dx):.3f}", fontsize=12)
    ax.set_xlabel("x")
axes[0].set_ylabel("f(x)")
fig.suptitle("Riemann sums approach the exact area 8/3 = 2.667", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/riemann_sums.png", dpi=200)

# ---------------------------------------------------------------- even / odd symmetry
xx = np.linspace(-2.5, 2.5, 500)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.8))
for ax, g, name in [(a1, np.exp(-xx**2), r"even: $e^{-x^2}$, area = 2 $\times$ right half"), (a2, xx * np.exp(-xx**2), r"odd: $x\,e^{-x^2}$, area = 0")]:
    ax.plot(xx, g, color=BLACK, lw=2.2)
    ax.fill_between(xx, g, where=xx >= 0, color=TEAL, alpha=0.35)
    ax.fill_between(xx, g, where=xx < 0, color=CARDINAL if ax is a2 else TEAL, alpha=0.35)
    ax.axhline(0, color=GRAY, lw=0.8); ax.axvline(0, color=GRAY, lw=0.8)
    ax.set_title(name, fontsize=12, color=BLACK); ax.set_xlabel("x"); ax.set_yticks([])
fig.tight_layout(); fig.savefig(f"{OUT}/even_odd.png", dpi=200)

# ---------------------------------------------------------------- unit circle + waves
theta = np.deg2rad(50); t = np.linspace(0, 2 * np.pi, 400)
fig, (c1, c2) = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw={"width_ratios": [1, 1.4]})
c1.plot(np.cos(t), np.sin(t), color=BLACK, lw=1.6)
c1.plot([0, np.cos(theta)], [0, np.sin(theta)], color=BLACK, lw=2)
c1.plot([np.cos(theta), np.cos(theta)], [0, np.sin(theta)], color=TEAL, lw=3, label=r"$\sin\theta$")
c1.plot([0, np.cos(theta)], [0, 0], color=CARDINAL, lw=3, label=r"$\cos\theta$")
c1.plot(np.cos(theta), np.sin(theta), "o", color=BLACK, ms=7)
arc = np.linspace(0, theta, 50); c1.plot(0.3 * np.cos(arc), 0.3 * np.sin(arc), color=GRAY, lw=1.2); c1.text(0.36, 0.1, r"$\theta$", fontsize=13)
c1.annotate(r"$(\cos\theta,\ \sin\theta)$", (np.cos(theta), np.sin(theta)), textcoords="offset points", xytext=(8, 8), fontsize=12)
c1.axhline(0, color=GRAY, lw=0.6); c1.axvline(0, color=GRAY, lw=0.6)
c1.set_aspect("equal"); c1.set_xlim(-1.3, 1.5); c1.set_ylim(-1.3, 1.3); c1.legend(loc="lower left", fontsize=11, frameon=False)
c1.set_title("A point on the unit circle", fontsize=13, fontweight="bold", color=BLACK)
c2.plot(t, np.cos(t), color=CARDINAL, lw=2.4, label=r"$\cos\theta$"); c2.plot(t, np.sin(t), color=TEAL, lw=2.4, label=r"$\sin\theta$")
c2.axhline(0, color=GRAY, lw=0.6)
c2.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]); c2.set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
c2.set_xlabel(r"$\theta$ (radians)"); c2.legend(fontsize=11, loc="upper right", frameon=False)
c2.set_title("Its two coordinates, a quarter turn apart", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/unit_circle.png", dpi=200)

# ---------------------------------------------------------------- Cartesian vs polar
z = 2 + 1.5j; r, phi = np.abs(z), np.angle(z)
fig, ax = plt.subplots(figsize=(5.6, 5.0))
ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=BLACK, lw=2.4))
arc = np.linspace(0, phi, 60); ax.plot(0.6 * np.cos(arc), 0.6 * np.sin(arc), color=CARDINAL, lw=1.8)
ax.plot([0, z.real], [z.imag, z.imag], "--", color=GRAY, lw=1); ax.plot([z.real, z.real], [0, z.imag], "--", color=GRAY, lw=1)
ax.text(z.real + 0.1, z.imag + 0.1, r"$z = 2 + 1.5i = 2.5\,e^{i\phi}$", fontsize=13)
ax.text(0.7, 0.15, r"$\phi$", color=CARDINAL, fontsize=15)
ax.text(z.real / 2, -0.28, r"$x = r\cos\phi$", color=GRAY, fontsize=11, ha="center")
ax.text(z.real + 0.06, z.imag / 2, r"$y = r\sin\phi$", color=GRAY, fontsize=11)
ax.text(0.75, 1.05, r"$r$", color=BLACK, fontsize=15)
ax.axhline(0, color=BLACK, lw=0.8); ax.axvline(0, color=BLACK, lw=0.8)
ax.set_xlim(-0.6, 3.2); ax.set_ylim(-0.6, 2.4); ax.set_aspect("equal"); ax.set_xlabel("Real"); ax.set_ylabel("Imaginary")
ax.set_title("One number, two descriptions: (x, y) or (r, φ)", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/polar_form.png", dpi=200)

# ---------------------------------------------------------------- multiplying by i
z0 = 1.6 + 0.6j; pts = [z0, 1j * z0, -z0, -1j * z0]
labels = [r"$z$", r"$iz$", r"$i^2 z = -z$", r"$i^3 z = -iz$"]; cols = ["#e67e22", TEAL, "#1f3a93", CARDINAL]
fig, ax = plt.subplots(figsize=(5.4, 5.4))
th = np.linspace(0, 2 * np.pi, 200); R = abs(z0); ax.plot(R * np.cos(th), R * np.sin(th), "--", color=GRAY, lw=1)
for w, lab, c in zip(pts, labels, cols):
    ax.annotate("", xy=(w.real, w.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=c, lw=2.6))
    ax.text(w.real * 1.18, w.imag * 1.18, lab, color=c, fontsize=14, ha="center", va="center")
ax.axhline(0, color=BLACK, lw=0.7); ax.axvline(0, color=BLACK, lw=0.7)
ax.set_xlim(-2.4, 2.4); ax.set_ylim(-2.4, 2.4); ax.set_aspect("equal"); ax.set_xlabel("Real"); ax.set_ylabel("Imaginary")
ax.set_title("Multiplying by i is a quarter turn", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/rotation_by_i.png", dpi=200)
print("done")
