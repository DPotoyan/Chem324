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
