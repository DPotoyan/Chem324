"""Generate runnable Colab notebooks from demo/tutorial pages.

For every page with enough static {code-cell} content, produce
notebooks/<name>.ipynb (jupytext) with marimo cells stripped, and keep an
"Open in Colab" badge under the page H1. Marimo-only pages get no notebook
(their launcher is the molab button). Rerun after editing demo pages.
"""
import re, glob, os, subprocess, tempfile, json

PAGES = sorted(glob.glob("ch0*/[0-9][0-9]-demo-*.md")) + sorted(glob.glob("demos/0*.md"))
PYSCF_PAGES = {"ch07/05-demo-hartree-fock.md", "ch08/08-demo-benzene.md"}
MARIMO_BLOCK = re.compile(r"```\{marimo-config\}.*?```\n|```\{marimo\}.*?```\n", re.S)
BADGE_LINE = re.compile(r"\n?\[!\[Open in Colab\]\([^)]*\)\]\([^)]*\)\n", re.M)

def notebook_name(page):
    base = os.path.basename(page)
    slug = re.sub(r"^\d\d-", "", base)[:-3]
    if page.startswith("demos/"):
        return f"appendix-{slug}.ipynb"
    return f"{slug}.ipynb"

made, skipped = [], []
for page in PAGES:
    src = open(page).read()
    src_clean = BADGE_LINE.sub("\n", src)          # manage badge idempotently
    body, _ = MARIMO_BLOCK.subn("", src_clean)
    n_code = body.count("```{code-cell}")
    if n_code < 2:
        skipped.append(page)
        if src_clean != src:
            open(page, "w").write(src_clean)       # remove badge from marimo-only page
        continue
    if "{marimo}" in src:
        note = ("\n:::{note}\nThis notebook carries the static code of the page; "
                "the interactive slider demos live on the course website.\n:::\n")
        body = re.sub(r"(^# .*\n)", r"\1" + note, body, count=1, flags=re.M)
    if page in PYSCF_PAGES:
        body = re.sub(r"(^# .*\n)", r"\1\n```{code-cell} python\n%pip install -q pyscf py3Dmol\n```\n",
                      body, count=1, flags=re.M)
    nb = notebook_name(page)
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(body); tmp = f.name
    r = subprocess.run(["uvx", "jupytext", "--to", "ipynb", tmp, "-o", f"notebooks/{nb}"],
                       capture_output=True, text=True)
    os.unlink(tmp)
    assert r.returncode == 0, (page, r.stderr[-200:])
    badge = (f"[![Open in Colab](../assets/colab-badge.svg)]"
             f"(https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/{nb})\n")
    t = re.sub(r"(^# .*\n)", r"\1\n" + badge, src_clean, count=1, flags=re.M)
    open(page, "w").write(t)
    made.append(nb)

print(f"generated {len(made)}; marimo-only skipped: {skipped}")
