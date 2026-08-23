"""Convert a page's {marimo} cells back to static {code-cell} blocks.

Inverse of scripts/marimoify.py. Used to move demo/tutorial pages off marimo
so they can be delivered as Colab notebooks; marimo now lives only in prose
pages (chNN/, math/02, math/05, overview.md, demos/06-python-calculator.md).

- deletes the {marimo-config} block
- {marimo} python -> {code-cell} python, :hide-code: true -> :tags: [hide-input]
- drops `import marimo as mo` and marimo-only plumbing
- restores trailing plt.gcf() to plt.show()
- ensures the page frontmatter carries a kernelspec

Run: python3 scripts/demarimoify.py <page.md> [<page.md> ...]
"""
import re, sys

FRONTMATTER = "---\nkernelspec:\n  name: python3\n  display_name: Python 3\n---\n"


def convert(path):
    t = open(path).read()
    orig = t

    # 1. drop the marimo page config
    t = re.sub(r"```\{marimo-config\}\n---\n.*?\n---\n```\n\n?", "", t, flags=re.S)

    # 2. each marimo cell -> code-cell
    cell = re.compile(
        r"^```\{marimo\} python\n"
        r"((?::(?:hide-code|editor):[^\n]*\n)*)"   # option lines
        r"\n?"
        r"(.*?)"
        r"^```\n",
        re.S | re.M,
    )

    def one(m):
        opts, body = m.group(1), m.group(2)
        hide = "hide-code" in opts

        lines = [ln for ln in body.splitlines()
                 if ln.strip() not in ("import marimo as mo", "import marimo")]
        body = "\n".join(lines).strip("\n")
        if not body:
            return ""                                  # cell was marimo plumbing only

        body = re.sub(r"^plt\.gcf\(\)\s*$", "plt.show()", body, flags=re.M)

        head = "```{code-cell} python\n"
        if hide:
            head += ":tags: [hide-input]\n"
        head += "\n" if hide else ""
        return head + body + "\n```\n"

    t, n = cell.subn(one, t)

    # 3. collapse blank-line runs left behind by removed blocks
    t = re.sub(r"\n{4,}", "\n\n\n", t)

    # 4. guarantee a kernelspec so --execute and jupytext both work
    if not t.startswith("---\n"):
        t = FRONTMATTER + "\n" + t
    elif "kernelspec" not in t.split("---")[1]:
        t = t.replace("---\n", "---\nkernelspec:\n  name: python3\n  display_name: Python 3\n", 1)

    if t != orig:
        open(path, "w").write(t)
    leftover = len(re.findall(r"\bmo\.", t))
    flag = f"  <-- {leftover} mo.* refs still present" if leftover else ""
    print(f"{path}: {n} cells converted{flag}")


for p in sys.argv[1:]:
    convert(p)
