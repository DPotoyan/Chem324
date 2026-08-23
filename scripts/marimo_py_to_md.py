"""One-time migration: marimo project .py -> jupytext MyST markdown.

Projects moved from molab to Colab, so their source format moves from marimo
`.py` apps to the same `{code-cell}` markdown the rest of the book uses.
scripts/make_notebooks.py then turns these into notebooks/ artifacts.

- drops the `# /// script` header, `import marimo`, `app = marimo.App(...)`
  and the `if __name__ == "__main__"` footer
- `mo.md(r"...")` cells become plain markdown
- every other cell becomes a ```{code-cell} python block, minus the marimo
  `return (...)` plumbing and `import marimo as mo`
- mo.ui widgets are NOT auto-translated; they are reported so you can replace
  them with explicit parameter cells by hand

Run: python3 scripts/marimo_py_to_md.py projects/03-foo.py [more.py ...]
"""
import re, sys, os, textwrap

FRONTMATTER = "---\nkernelspec:\n  name: python3\n  display_name: Python 3\n---\n"
CELL = re.compile(r"^@app\.cell(?:\([^)]*\))?\s*\ndef _\([^)]*\):\n(.*?)(?=^@app\.cell|^if __name__)",
                  re.S | re.M)
MO_MD = re.compile(r'^mo\.md\(\s*r?"""\n?(.*?)\n?\s*"""\s*,?\s*\)$', re.S)


def convert(path):
    src = open(path).read()
    out, widgets = [], []

    for m in CELL.finditer(src):
        body = textwrap.dedent(m.group(1)).strip("\n")

        # strip marimo's trailing return plumbing
        body = re.sub(r"\n?^return(?: \(.*?\)| .*)?$", "", body, flags=re.M).strip("\n")
        body = "\n".join(ln for ln in body.splitlines()
                         if ln.strip() not in ("import marimo as mo", "import marimo"))
        body = body.strip("\n")
        if not body:
            continue

        md = MO_MD.match(body)
        if md:
            out.append(textwrap.dedent(md.group(1)).strip("\n"))
        else:
            if "mo.ui" in body or "mo.hstack" in body or "mo.vstack" in body:
                widgets.append(body.splitlines()[0][:70])
            out.append("```{code-cell} python\n" + body + "\n```")

    dest = os.path.splitext(path)[0] + ".md"
    open(dest, "w").write(FRONTMATTER + "\n" + "\n\n".join(out) + "\n")
    note = f"  <-- {len(widgets)} widget cell(s) need hand conversion" if widgets else ""
    print(f"{path} -> {dest}: {len(out)} cells{note}")
    for w in widgets:
        print(f"      {w}")


for p in sys.argv[1:]:
    convert(p)
