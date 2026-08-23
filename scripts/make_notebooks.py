"""Generate runnable Colab notebooks from demo pages and student projects.

Since the 2026-08 migration, marimo lives only in prose pages (chNN/, math/02,
math/05, overview.md, demos/06-python-calculator.md). Everything under demos/
and projects/ is static {code-cell} markdown delivered to students as Colab
notebooks.

- demos/*.md    -> notebooks/appendix-<slug>.ipynb, plus an "Open in Colab"
                   badge kept under the page H1 (these are website pages)
- projects/*.md -> notebooks/project-<NN-slug>.ipynb, no badge injected; the
                   badges live on projects/00-computational-projects.md, which
                   is the page students actually read

Any page that is still marimo-only (demos/06) is skipped and has its badge
removed. Rerun after editing any demo page or project.
"""
import re, glob, os, subprocess, tempfile

DEMO_PAGES = sorted(glob.glob("demos/[0-9]*.md"))
PROJECT_PAGES = sorted(glob.glob("projects/0[1-9]-*.md"))
PYSCF_PAGES = {"demos/11-demo-hartree-fock.md", "demos/13-demo-benzene.md"}
MARIMO_BLOCK = re.compile(r"```\{marimo-config\}.*?```\n|```\{marimo\}.*?```\n", re.S)
BADGE_LINE = re.compile(r"\n?\[!\[Open in Colab\]\([^)]*\)\]\([^)]*\)\n", re.M)
COLAB = "https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks"


def notebook_name(page):
    base = os.path.basename(page)[:-3]
    if page.startswith("projects/"):
        return f"project-{base}.ipynb"
    slug = re.sub(r"^\d\d-", "", base)
    return f"appendix-{slug}.ipynb"


def to_ipynb(body, nb):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(body)
        tmp = f.name
    r = subprocess.run(["uvx", "jupytext", "--to", "ipynb", tmp, "-o", f"notebooks/{nb}"],
                       capture_output=True, text=True)
    os.unlink(tmp)
    assert r.returncode == 0, (nb, r.stderr[-300:])


made, skipped = [], []

for page in DEMO_PAGES:
    src = open(page).read()
    src_clean = BADGE_LINE.sub("\n", src)              # manage badge idempotently
    body, _ = MARIMO_BLOCK.subn("", src_clean)
    if body.count("```{code-cell}") < 2:               # marimo-only page
        skipped.append(page)
        if src_clean != src:
            open(page, "w").write(src_clean)
        continue
    if page in PYSCF_PAGES:
        body = re.sub(r"(^# .*\n)",
                      r"\1\n```{code-cell} python\n%pip install -q pyscf py3Dmol\n```\n",
                      body, count=1, flags=re.M)
    nb = notebook_name(page)
    to_ipynb(body, nb)
    badge = f"[![Open in Colab](../assets/colab-badge.svg)]({COLAB}/{nb})\n"
    open(page, "w").write(re.sub(r"(^# .*\n)", r"\1\n" + badge, src_clean, count=1, flags=re.M))
    made.append(nb)

for page in PROJECT_PAGES:
    nb = notebook_name(page)
    to_ipynb(open(page).read(), nb)
    made.append(nb)

print(f"generated {len(made)} notebooks")
for nb in made:
    print(f"  {nb}")
if skipped:
    print(f"marimo-only, skipped: {skipped}")
