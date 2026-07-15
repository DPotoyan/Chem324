"""Convert a demo page's static {code-cell} blocks to marimo cells.

- collects imports from all code cells into one hidden marimo imports cell
- converts each {code-cell} to a {marimo} cell (page config gets echo: true)
- replaces trailing plt.show() with plt.gcf()
Run: python3 scripts/marimoify.py <page.md> <dep1,dep2,...>
"""
import re, sys

page, deps = sys.argv[1], sys.argv[2].split(",")
t = open(page).read()

code_cell = re.compile(r"^```\{code-cell\} python\n(?::tags:[^\n]*\n\n?)?(.*?)^```$\n", re.S | re.M)
imports = []
def convert(m):
    body = m.group(1)
    lines = []
    for ln in body.splitlines():
        if re.match(r"\s*[%!]", ln):
            continue
        if re.match(r"\s*(import |from \S+ import )", ln):
            if ln.strip() not in imports:
                imports.append(ln.strip())
        else:
            lines.append(ln)
    body = "\n".join(lines).strip("\n")
    if not body:
        return ""
    body = re.sub(r"^plt\.show\(\)\s*$", "plt.gcf()", body, flags=re.M)
    return "```{marimo} python\n" + body + "\n```\n"

t = code_cell.sub(convert, t)

# merge imports into existing hidden imports cell, or create one
existing = re.search(r"(```\{marimo\} python\n:hide-code: true\n\n)((?:import |from )[^\n]*\n(?:(?:import |from )[^\n]*\n)*)(```\n)", t)
if existing:
    have = set(l.strip() for l in existing.group(2).splitlines())
    add = [i for i in imports if i not in have]
    if add:
        t = t.replace(existing.group(0), existing.group(1) + existing.group(2) + "\n".join(add) + "\n" + existing.group(3), 1)
else:
    block = "```{marimo} python\n:hide-code: true\n\nimport marimo as mo\n" + "\n".join(imports) + "\n```\n\n"
    cfg = re.search(r"```\{marimo-config\}.*?```\n", t, re.S)
    if cfg:
        t = t.replace(cfg.group(0), cfg.group(0) + "\n" + block, 1)
    else:
        deps_toml = "".join(f'      "{d}",\n' for d in deps)
        cfg_block = ("```{marimo-config}\n---\necho: true\npyproject: |\n"
                     "  requires-python = \">=3.10\"\n  dependencies = [\n" + deps_toml + "  ]\n---\n```\n\n")
        t = re.sub(r"(^# .*\n(?:\n\[!\[Open in Colab\][^\n]*\n)?)", r"\1\n" + cfg_block + block, t, count=1, flags=re.M)

# ensure page config has echo: true
t = re.sub(r"(```\{marimo-config\}\n---\n)(?!echo)", r"\1echo: true\n", t, count=1)
open(page, "w").write(t)
print(f"{page}: converted, {len(imports)} imports collected")
