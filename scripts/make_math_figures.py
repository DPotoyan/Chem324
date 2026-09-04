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

# ---------------------------------------------------------------- partial derivatives as slopes of slices
g = lambda x, y: 4 - x**2 - y**2 / 4
gx = lambda x, y: -2 * x
gy = lambda x, y: -y / 2
x0, y0 = 1.0, 1.0
X, Y = np.meshgrid(np.linspace(-2, 2, 60), np.linspace(-3, 3, 60))
fig = plt.figure(figsize=(7.2, 5.4))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, g(X, Y), color="lightgray", alpha=0.35, linewidth=0)
xs = np.linspace(-2, 2, 100); ys = np.linspace(-3, 3, 100)
ax.plot(xs, np.full_like(xs, y0), g(xs, y0), color=CARDINAL, lw=2.8, label=r"slice $y = 1$: slope is $\partial f/\partial x$")
ax.plot(np.full_like(ys, x0), ys, g(x0, ys), color=TEAL, lw=2.8, label=r"slice $x = 1$: slope is $\partial f/\partial y$")
tx = np.array([x0 - 0.8, x0 + 0.8]); ax.plot(tx, np.full_like(tx, y0), g(x0, y0) + gx(x0, y0) * (tx - x0), "--", color=CARDINAL, lw=1.6)
ty = np.array([y0 - 1.2, y0 + 1.2]); ax.plot(np.full_like(ty, x0), ty, g(x0, y0) + gy(x0, y0) * (ty - y0), "--", color=TEAL, lw=1.6)
ax.scatter([x0], [y0], [g(x0, y0)], color=BLACK, s=45)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("f(x, y)")
ax.view_init(elev=25, azim=-60)
ax.legend(loc="upper left", fontsize=10, frameon=False)
ax.set_title("Slopes of slices, one variable at a time", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/partial_slices.png", dpi=200)

# ---------------------------------------------------------------- phasor addition of two waves
phi = 2 * np.pi / 3; th = np.linspace(0, 4 * np.pi, 500)
pa, pb = 1 + 0j, np.exp(1j * phi); pc = pa + pb
fig, (p1, p2) = plt.subplots(1, 2, figsize=(10.5, 4.2), gridspec_kw={"width_ratios": [1, 1.6]})
p1.annotate("", xy=(pa.real, pa.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=CARDINAL, lw=2.6))
p1.annotate("", xy=(pc.real, pc.imag), xytext=(pa.real, pa.imag), arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.6))
p1.annotate("", xy=(pc.real, pc.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=BLACK, lw=3.2))
p1.text(0.5, -0.2, "1", color=CARDINAL, fontsize=14, ha="center")
p1.text(0.85, 0.6, r"$e^{i\phi}$", color=TEAL, fontsize=14)
p1.text(-0.55, 0.85, r"$1 + e^{i\phi}$", color=BLACK, fontsize=14)
p1.axhline(0, color=GRAY, lw=0.6); p1.axvline(0, color=GRAY, lw=0.6)
p1.set_aspect("equal"); p1.set_xlim(-0.6, 1.6); p1.set_ylim(-0.6, 1.4); p1.set_xlabel("Real"); p1.set_ylabel("Imaginary")
p1.set_title("Phasors add tip to tail", fontsize=13, fontweight="bold", color=BLACK)
p2.plot(th, np.cos(th), color=CARDINAL, lw=1.6, label=r"$\cos\theta$")
p2.plot(th, np.cos(th + phi), color=TEAL, lw=1.6, label=r"$\cos(\theta + \phi)$")
p2.plot(th, np.cos(th) + np.cos(th + phi), color=BLACK, lw=2.8, label="sum")
p2.axhline(0, color=GRAY, lw=0.6)
p2.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi]); p2.set_xticklabels(["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
p2.set_xlabel(r"$\theta$"); p2.set_ylim(-2.3, 2.3); p2.legend(fontsize=11, loc="upper right", ncol=3, frameon=False)
p2.set_title(r"Sum amplitude $2|\cos(\phi/2)|$ = 1.00 for $\phi = 2\pi/3$", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/phasor_sum.png", dpi=200)
print("done (partials, phasors)")

# ---------------------------------------------------------------- Taylor polynomials of sin x
from math import factorial
xt = np.linspace(-2 * np.pi, 2 * np.pi, 600)
fig, ax = plt.subplots(figsize=(7.6, 4.2))
ax.plot(xt, np.sin(xt), color=BLACK, lw=2.6, label=r"$\sin x$")
for order, col in zip([1, 3, 5, 7], [CARDINAL, "#e67e22", TEAL, "#1f3a93"]):
    poly = sum((-1) ** (k // 2) * xt**k / factorial(k) for k in range(1, order + 1, 2))
    ax.plot(xt, poly, "--", color=col, lw=1.8, label="1 derivative" if order == 1 else f"{order} derivatives")
ax.set_ylim(-2.5, 2.5); ax.set_xlabel("x"); ax.axhline(0, color=GRAY, lw=0.6)
ax.set_xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi]); ax.set_xticklabels([r"$-2\pi$", r"$-\pi$", "0", r"$\pi$", r"$2\pi$"])
ax.legend(fontsize=10, loc="lower right", ncol=2, frameon=False)
ax.set_title("More derivatives at 0 predict sin x farther out", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/taylor_sin.png", dpi=200)

# ---------------------------------------------------------------- first derivative: direction
xc = np.linspace(-2.3, 2.3, 500); fc, fpc, fppc = xc**3 - 3 * xc, 3 * xc**2 - 3, 6 * xc
fig, (d1, d2) = plt.subplots(2, 1, figsize=(6.6, 5.8), sharex=True)
d1.plot(xc, fc, color=BLACK, lw=2.6)
d1.fill_between(xc, -6, 6, where=fpc > 0, color=TEAL, alpha=0.12); d1.fill_between(xc, -6, 6, where=fpc < 0, color=CARDINAL, alpha=0.12)
for x_ in (-1, 1):
    d1.plot([x_ - 0.4, x_ + 0.4], [x_**3 - 3 * x_] * 2, color="#1f3a93", lw=2.2); d1.plot(x_, x_**3 - 3 * x_, "o", color="#1f3a93", ms=8)
d1.text(-1, 2.7, "maximum", ha="center", fontsize=11); d1.text(1, -3.5, "minimum", ha="center", fontsize=11)
d1.text(-2.1, 3.7, "rising", color=TEAL, fontsize=11); d1.text(-0.35, 3.7, "falling", color=CARDINAL, fontsize=11); d1.text(1.5, 3.7, "rising", color=TEAL, fontsize=11)
d1.set_ylim(-5, 5); d1.set_ylabel(r"$f = x^3 - 3x$")
d2.plot(xc, fpc, color="#1f3a93", lw=2.6); d2.axhline(0, color=GRAY, lw=0.8); d2.plot([-1, 1], [0, 0], "o", color="#1f3a93", ms=8)
d2.fill_between(xc, 0, fpc, where=fpc > 0, color=TEAL, alpha=0.25); d2.fill_between(xc, 0, fpc, where=fpc < 0, color=CARDINAL, alpha=0.25)
d2.text(-2.15, 3.2, r"$f' > 0$", color=TEAL, fontsize=12); d2.text(0.2, -2.2, r"$f' < 0$", color=CARDINAL, fontsize=12)
d2.set_ylabel(r"$f' = 3x^2 - 3$"); d2.set_xlabel("x")
d1.set_title("Sign of f' gives the direction, zeros give the stationary points", fontsize=12, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/first_derivative.png", dpi=200)

# ---------------------------------------------------------------- second derivative: bending
fig, (e1, e2) = plt.subplots(2, 1, figsize=(6.6, 5.8), sharex=True)
e1.plot(xc, fc, color=BLACK, lw=2.6)
e1.fill_between(xc, -6, 6, where=xc < 0, color=CARDINAL, alpha=0.12); e1.fill_between(xc, -6, 6, where=xc > 0, color=TEAL, alpha=0.12)
e1.plot(0, 0, "s", color="#e67e22", ms=9); e1.text(0.15, 0.5, "inflection", fontsize=11, color="#b7500a")
e1.text(-1.9, 3.7, "bends down (dome)", color=CARDINAL, fontsize=11); e1.text(0.4, 3.7, "bends up (bowl)", color=TEAL, fontsize=11)
e1.plot(-1, 2, "o", color="#1f3a93", ms=8); e1.plot(1, -2, "o", color="#1f3a93", ms=8)
e1.text(-1, 2.7, r"$f'' < 0$: max", ha="center", fontsize=11); e1.text(1, -3.5, r"$f'' > 0$: min", ha="center", fontsize=11)
e1.set_ylim(-5, 5); e1.set_ylabel(r"$f = x^3 - 3x$")
e2.plot(xc, fppc, color="#b7500a", lw=2.6); e2.axhline(0, color=GRAY, lw=0.8); e2.plot(0, 0, "s", color="#e67e22", ms=9)
e2.fill_between(xc, 0, fppc, where=fppc > 0, color=TEAL, alpha=0.25); e2.fill_between(xc, 0, fppc, where=fppc < 0, color=CARDINAL, alpha=0.25)
e2.set_ylabel(r"$f'' = 6x$"); e2.set_xlabel("x")
e1.set_title("Sign of f'' gives the bending, a zero crossing an inflection", fontsize=12, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/second_derivative.png", dpi=200)

# ---------------------------------------------------------------- Gaussian and its derivatives
xg = np.linspace(-3, 3, 500); gg = np.exp(-xg**2); xi = 1 / np.sqrt(2)
fig, ax = plt.subplots(figsize=(7.6, 4.2))
ax.plot(xg, gg, color=BLACK, lw=2.6, label=r"$f = e^{-x^2}$")
ax.plot(xg, -2 * xg * gg, color="#1f3a93", lw=2, label=r"$f' = -2x\,e^{-x^2}$")
ax.plot(xg, (4 * xg**2 - 2) * gg, "--", color=CARDINAL, lw=2, label=r"$f'' = (4x^2 - 2)\,e^{-x^2}$")
ax.axhline(0, color=GRAY, lw=0.6)
for x_ in (-xi, xi):
    ax.axvline(x_, color="#b7500a", lw=1, ls=":"); ax.plot(x_, np.exp(-x_**2), "s", color="#e67e22", ms=8)
ax.plot(0, 1, "o", color="#1f3a93", ms=8)
ax.text(0, 1.1, r"peak: $f' = 0,\ f'' < 0$", ha="center", fontsize=11); ax.text(xi + 0.08, 0.72, r"inflection: $f'' = 0$", fontsize=11, color="#b7500a")
ax.set_ylim(-2.3, 1.45); ax.set_xlabel("x"); ax.legend(fontsize=10, loc="lower right", frameon=False)
ax.set_title("The Gaussian with its first two derivatives", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/gaussian_derivs.png", dpi=200)

# ---------------------------------------------------------------- cosine motion
tt = np.linspace(0, 4 * np.pi, 500)
fig, ax = plt.subplots(figsize=(7.6, 3.8))
ax.plot(tt, np.cos(tt), color=BLACK, lw=2.6, label=r"position $x = \cos t$")
ax.plot(tt, -np.sin(tt), color="#1f3a93", lw=2, label=r"velocity $x' = -\sin t$")
ax.plot(tt, -np.cos(tt), "--", color=CARDINAL, lw=2, label=r"acceleration $x'' = -x$")
ax.axhline(0, color=GRAY, lw=0.6)
ax.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi]); ax.set_xticklabels(["0", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
ax.set_xlabel("t"); ax.set_ylim(-1.9, 1.9); ax.legend(fontsize=10, loc="upper right", ncol=3, frameon=False)
ax.set_title("Acceleration is the mirror image of position", fontsize=13, fontweight="bold", color=BLACK)
fig.tight_layout(); fig.savefig(f"{OUT}/motion_cos.png", dpi=200)
print("done (taylor, derivatives, gaussian, motion)")
