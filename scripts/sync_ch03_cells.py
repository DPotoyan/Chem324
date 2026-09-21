"""Copy each animation/still from scripts/make_ch03_animations.py into the lecture pages.

A page cell opts in with a marker as its first code line:

    ```{code-cell} python
    :tags: [hide-input]
    # synced: phase_clock
    ...anything here is replaced...
    ```

The function body (dedented, minus `return`/`savefig`/`print` lines) is pasted after a
standard import header; animations end with `HTML(ani.to_jshtml())`, stills with
`plt.show()`. Run from the repo root:  .venv/bin/python scripts/sync_ch03_cells.py
"""
import importlib.util, inspect, re, sys, textwrap

PAGES = ["ch03/01-schrodinger-equation.md"]
HEADER = (
    "import numpy as np\n"
    "import matplotlib.pyplot as plt\n"
    "from matplotlib.animation import FuncAnimation\n"
    "from IPython.display import HTML\n\n"
    'TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"\n'
)

spec = importlib.util.spec_from_file_location("ch03anim", "scripts/make_ch03_animations.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def cell_for(name):
    src = inspect.getsource(mod.REGISTRY[name]).split("\n")
    body = textwrap.dedent("\n".join(src[2:]))          # drop '@register' and 'def name():'
    keep = [l for l in body.splitlines()
            if not l.strip().startswith(("return ", "fig.savefig(", "print("))]
    still = "FuncAnimation(" not in body
    footer = "plt.show()\n" if still else "plt.close(fig)\nHTML(ani.to_jshtml())\n"
    return HEADER + "\n".join(keep).rstrip() + "\n" + footer


pat = re.compile(r"(```\{code-cell\} python\n:tags: \[hide-input\]\n# synced: (\w+)\n)(.*?)(```)", re.S)
for page in PAGES:
    text = open(page).read()
    names = []

    def repl(m):
        names.append(m.group(2))
        return m.group(1) + cell_for(m.group(2)) + m.group(4)

    new = pat.sub(repl, text)
    open(page, "w").write(new)
    print(f"{page}: synced {len(names)} cells: {', '.join(names)}")
