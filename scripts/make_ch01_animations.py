"""Regenerate the chapter 1 animated GIFs used by the slide decks.

The SAME animation is authored as a `{code-cell}` on the lecture page, where it is
displayed with `HTML(ani.to_jshtml())`; this script bakes it once to a GIF for the deck.

Run from the repo root:  .venv/bin/python scripts/make_ch01_animations.py
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Circle

OUT = "ch01/images"
TEAL, CARDINAL, GRAY, PURPLE, GREEN = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#1a7f37"

# ------------------------------------------------------------ de Broglie waves on a ring
R, AMP, LAPS = 1.0, 0.17, 8          # ring radius, wave amplitude, passes summed
th1 = np.linspace(0, 2 * np.pi, 900)          # first pass around the loop
th2 = np.linspace(2 * np.pi, 4 * np.pi, 900)  # second pass around the loop

n_grid = np.linspace(1.5, 6.5, 2000)
laps = np.arange(LAPS)[:, None]
survival = np.abs(np.exp(2j * np.pi * n_grid * laps).sum(axis=0)) / LAPS

n_seq = [2.0] * 4
for target in (3.0, 4.0, 5.0, 6.0):
    n_seq += list(np.linspace(n_seq[-1], target, 11, endpoint=False)) + [target] * 4


def survival_at(n):
    return abs(np.exp(2j * np.pi * n * np.arange(LAPS)).sum()) / LAPS


fig, (ax, bx) = plt.subplots(1, 2, figsize=(8.8, 4.2), gridspec_kw={"width_ratios": [1, 1.15]})

ax.add_patch(Circle((0, 0), R, fill=False, color=GRAY, lw=1.2, ls="--"))
ax.plot(0, 0, "o", color=CARDINAL, ms=9)
(lap1,) = ax.plot([], [], color=PURPLE, lw=2.4, label="1st pass")
(lap2,) = ax.plot([], [], color="#e07b00", lw=2.0, ls="--", label="2nd pass")
(gap,) = ax.plot([], [], color=CARDINAL, lw=3.4, solid_capstyle="butt", zorder=6)
(startdot,) = ax.plot([], [], "o", color=PURPLE, ms=8, mec="white", mew=1.2, zorder=7)
(enddot,) = ax.plot([], [], "o", color="#e07b00", ms=8, mec="white", mew=1.2, zorder=7)
gaplabel = ax.text(0, -1.42, "", fontsize=10.5, color=CARDINAL, ha="center", va="center")
verdict = ax.set_title("", fontsize=12, pad=10)
ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False, fontsize=9)
ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.55); ax.set_aspect("equal"); ax.axis("off")

bx.plot(n_grid, survival, color=TEAL, lw=2.2)
bx.fill_between(n_grid, survival, color=TEAL, alpha=0.10)
(marker,) = bx.plot([], [], "o", color=CARDINAL, ms=9, zorder=5)
vline = bx.axvline(2.0, color=CARDINAL, lw=1.2, ls=":")
bx.set_xlim(1.5, 6.5); bx.set_ylim(-0.03, 1.18)
bx.set_xticks(range(2, 7))
bx.set_xlabel("wavelengths around the orbit,  $n = 2\\pi r / \\lambda$", fontsize=11)
bx.set_ylabel("amplitude left after 8 passes", fontsize=11)
bx.set_title("Only integer $n$ survives", fontsize=12, pad=10)
for s in ("top", "right"):
    bx.spines[s].set_visible(False)

fig.suptitle("A standing wave on a Bohr orbit:  $2\\pi r = n\\lambda = nh/p$", fontsize=13.5, y=0.99)
fig.tight_layout(rect=(0, 0, 1, 0.93))


def update(i):
    n = n_seq[i]
    lap1.set_data((R + AMP * np.sin(n * th1)) * np.cos(th1), (R + AMP * np.sin(n * th1)) * np.sin(th1))
    lap2.set_data((R + AMP * np.sin(n * th2)) * np.cos(th2), (R + AMP * np.sin(n * th2)) * np.sin(th2))
    r0, r1 = R, R + AMP * np.sin(2 * np.pi * n)     # wave value at the start and after one lap
    gap.set_data([r0, r1], [0, 0])
    startdot.set_data([r0], [0])
    enddot.set_data([r1], [0])
    closes = abs(n - round(n)) < 1e-9
    off = abs(n - round(n))
    gaplabel.set_text("the 2nd pass lands on the 1st" if closes else f"the 2nd pass is {off:.2f}$\\lambda$ out of step")
    gaplabel.set_color(GREEN if closes else CARDINAL)
    verdict.set_text(f"$n$ = {n:.2f}   " + ("the wave closes on itself" if closes else "the wave misses itself"))
    verdict.set_color(GREEN if closes else CARDINAL)
    marker.set_data([n], [survival_at(n)])
    vline.set_xdata([n, n])
    return lap1, lap2, gap, startdot, enddot, gaplabel, marker, vline, verdict


ani = FuncAnimation(fig, update, frames=len(n_seq), interval=70, blit=False)
ani.save(f"{OUT}/debroglie_ring.gif", writer=PillowWriter(fps=12), dpi=100)
plt.close(fig)
print(f"wrote {OUT}/debroglie_ring.gif ({len(n_seq)} frames)")

# ------------------------------------------------------------ circular motion kinematics
# Position, velocity, centripetal acceleration and the (fictitious) centrifugal force on a
# circular orbit. Used in the Bohr force-balance section and again for angular momentum.
R2, N_FR, OM = 1.0, 72, 1.0          # radius, frames, angular velocity
SV, SA = 0.62, 0.48                   # arrow scale factors (v and a are drawn to scale)
th_seq = np.linspace(0, 2 * np.pi, N_FR, endpoint=False)

fig2, (cx, dx) = plt.subplots(1, 2, figsize=(10.4, 4.5),
                              gridspec_kw={"width_ratios": [1.15, 1.2]})

cx.add_patch(Circle((0, 0), R2, fill=False, color=GRAY, lw=1.2, ls="--"))
cx.plot(0, 0, "o", color=CARDINAL, ms=11)
cx.text(0.10, -0.22, "nucleus", color=CARDINAL, fontsize=8)
(bead,) = cx.plot([], [], "o", color="k", ms=9, zorder=6)


def arrow(color, ls="-", lw=2.2):
    return cx.annotate("", xy=(0, 0), xytext=(0, 0), zorder=5,
                       arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                       ls=ls, shrinkA=0, shrinkB=0))


a_r, a_v, a_a, a_cf = arrow(GRAY, lw=1.3), arrow(TEAL), arrow(PURPLE), arrow(CARDINAL, "--")
a_r.arrow_patch.set_alpha(0.45)
cx.set_xlim(-1.75, 1.75)
cx.set_ylim(-1.6, 1.6)
cx.set_aspect("equal")
cx.axis("off")
cx.legend(handles=[plt.Line2D([], [], color=GRAY, lw=1.3, alpha=0.45, label=r"$\vec{r}$  position"),
                   plt.Line2D([], [], color=TEAL, lw=2.2, label=r"$\vec{v}$  velocity (tangent)"),
                   plt.Line2D([], [], color=PURPLE, lw=2.2, label=r"$\vec{a}$  centripetal (inward)"),
                   plt.Line2D([], [], color=CARDINAL, lw=2.2, ls="--",
                              label="centrifugal (rotating frame)")],
          loc="lower center", bbox_to_anchor=(0.5, -0.16), fontsize=7.5, frameon=False)

t_full = th_seq / OM
dx.plot(t_full, R2 * np.cos(th_seq), color=GRAY, lw=1.6, label=r"$x = R\cos\omega t$")
dx.plot(t_full, -OM * R2 * np.sin(th_seq), color=TEAL, lw=1.6, label=r"$v_x = -\omega R\sin\omega t$")
dx.plot(t_full, -OM**2 * R2 * np.cos(th_seq), color=PURPLE, lw=1.6,
        label=r"$a_x = -\omega^2 R\cos\omega t$")
sweep = dx.axvline(0, color="k", lw=0.9, alpha=0.45)
(m_x,) = dx.plot([], [], "o", color=GRAY, ms=7)
(m_v,) = dx.plot([], [], "o", color=TEAL, ms=7)
(m_a,) = dx.plot([], [], "o", color=PURPLE, ms=7)
dx.axhline(0, color="k", lw=0.6, alpha=0.3)
dx.set_xlim(0, t_full[-1])
dx.set_ylim(-1.5, 1.9)
dx.set_xlabel("time")
dx.set_yticks([])
dx.legend(loc="upper right", fontsize=7.5, frameon=False, ncol=1)
dx.set_title("each component is simple harmonic motion", fontsize=9)
for s in ("top", "right", "left"):
    dx.spines[s].set_visible(False)

fig2.suptitle("Fig. Circular motion: position, velocity and centripetal acceleration.\n"
              "The magnitudes never change, only the directions.", fontsize=10)
fig2.tight_layout()


def frame2(i):
    th = th_seq[i]
    p = np.array([R2 * np.cos(th), R2 * np.sin(th)])
    rhat, that = p / R2, np.array([-np.sin(th), np.cos(th)])
    bead.set_data([p[0]], [p[1]])
    a_r.xy = p
    a_r.set_position((0, 0))
    a_v.xy = p + SV * OM * R2 * that
    a_v.set_position(p)
    a_a.xy = p - SA * OM**2 * R2 * rhat
    a_a.set_position(p)
    a_cf.xy = p + SA * OM**2 * R2 * rhat
    a_cf.set_position(p)
    sweep.set_xdata([t_full[i], t_full[i]])
    m_x.set_data([t_full[i]], [p[0]])
    m_v.set_data([t_full[i]], [-OM * R2 * np.sin(th)])
    m_a.set_data([t_full[i]], [-OM**2 * R2 * np.cos(th)])
    return bead, a_r, a_v, a_a, a_cf, sweep, m_x, m_v, m_a


ani2 = FuncAnimation(fig2, frame2, frames=N_FR, interval=50, blit=False)
ani2.save(f"{OUT}/circular_motion.gif", writer=PillowWriter(fps=20), dpi=100)
print("wrote circular_motion.gif")

# ---- deck framing of the SAME animation: orbit panel only, square, big arrows.
# The two-panel version above is what the lecture page shows; projected from the back of a
# hall the component plot is unreadable and only the vectors matter, so the deck gets this.
fig3, ex = plt.subplots(figsize=(6.4, 5.6))
ex.add_patch(Circle((0, 0), R2, fill=False, color=GRAY, lw=1.6, ls="--"))
ex.plot(0, 0, "o", color=CARDINAL, ms=15)
ex.text(0.12, -0.26, "nucleus", color=CARDINAL, fontsize=12)
(bead3,) = ex.plot([], [], "o", color="k", ms=13, zorder=6)


def arrow3(color, ls="-", lw=3.4):
    return ex.annotate("", xy=(0, 0), xytext=(0, 0), zorder=5,
                       arrowprops=dict(arrowstyle="-|>,head_width=0.28,head_length=0.55",
                                       color=color, lw=lw, ls=ls, shrinkA=0, shrinkB=0))


b_r, b_v, b_a, b_cf = arrow3(GRAY, lw=2.0), arrow3(TEAL), arrow3(PURPLE), arrow3(CARDINAL, "--")
b_r.arrow_patch.set_alpha(0.5)
ex.set_xlim(-1.8, 1.8)
ex.set_ylim(-1.75, 1.85)
ex.set_aspect("equal")
ex.axis("off")
ex.legend(handles=[plt.Line2D([], [], color=GRAY, lw=2.0, alpha=0.5, label=r"$\vec{r}$  position"),
                   plt.Line2D([], [], color=TEAL, lw=3.4, label=r"$\vec{v}$  velocity"),
                   plt.Line2D([], [], color=PURPLE, lw=3.4, label=r"$\vec{a}$  centripetal"),
                   plt.Line2D([], [], color=CARDINAL, lw=3.4, ls="--",
                              label="centrifugal (rotating frame)")],
          loc="upper center", bbox_to_anchor=(0.5, 1.04), fontsize=12, frameon=False, ncol=2)
fig3.tight_layout()


def frame3(i):
    th = th_seq[i]
    p = np.array([R2 * np.cos(th), R2 * np.sin(th)])
    rhat, that = p / R2, np.array([-np.sin(th), np.cos(th)])
    bead3.set_data([p[0]], [p[1]])
    b_r.xy = p
    b_r.set_position((0, 0))
    b_v.xy = p + SV * OM * R2 * that
    b_v.set_position(p)
    b_a.xy = p - SA * OM**2 * R2 * rhat
    b_a.set_position(p)
    b_cf.xy = p + SA * OM**2 * R2 * rhat
    b_cf.set_position(p)
    return bead3, b_r, b_v, b_a, b_cf


ani3 = FuncAnimation(fig3, frame3, frames=N_FR, interval=50, blit=False)
ani3.save(f"{OUT}/circular_motion_orbit.gif", writer=PillowWriter(fps=20), dpi=100)
print("wrote circular_motion_orbit.gif")
