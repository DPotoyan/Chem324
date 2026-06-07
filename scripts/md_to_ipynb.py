#!/usr/bin/env python3
"""Convert a MyST lecture .md (with ```{code-cell}``` blocks) into a Jupyter
notebook whose code cells are tagged `hide-input`. Prose (including MyST
directives like :::{figure} / :::{note}) becomes markdown cells verbatim.

Then execute the notebook once (jupyter nbconvert --execute) so the figure
outputs are stored; the site renders those with the code collapsed.

Usage: python3 md_to_ipynb.py FILE.md [OUT.ipynb]
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

KERNEL = {"name": "python3", "display_name": "Python 3", "language": "python"}

def to_source(s: str):
    s = s.rstrip("\n")
    return s.splitlines(keepends=True) if s else []

def convert(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    # drop YAML frontmatter (kernelspec is set in notebook metadata instead)
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    body = text[m.end():] if m else text
    cells, pos = [], 0
    for cm in re.finditer(r"```\{code-cell\}[^\n]*\n(.*?)\n```", body, re.S):
        md = body[pos:cm.start()].strip("\n")
        if md.strip():
            cells.append({"cell_type": "markdown", "metadata": {}, "source": to_source(md)})
        code = re.sub(r"^:tags:.*\n", "", cm.group(1))
        cells.append({"cell_type": "code", "metadata": {"tags": ["hide-input"]},
                      "execution_count": None, "outputs": [], "source": to_source(code)})
        pos = cm.end()
    tail = body[pos:].strip("\n")
    if tail.strip():
        cells.append({"cell_type": "markdown", "metadata": {}, "source": to_source(tail)})
    return {"cells": cells,
            "metadata": {"kernelspec": KERNEL, "language_info": {"name": "python"}},
            "nbformat": 4, "nbformat_minor": 5}

if __name__ == "__main__":
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".ipynb")
    out.write_text(json.dumps(convert(src), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{src.name} -> {out.name}")
