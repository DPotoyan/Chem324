#!/usr/bin/env python3
"""Convert a prose-heavy lecture .ipynb to MyST markdown.

Markdown cells pass through verbatim; code cells become executable
` ```{code-cell} python ` blocks. Adds a kernelspec front-matter so MyST
treats the page as executable.

Usage: python3 ipynb_to_md.py notebook.ipynb [output.md]
"""
from __future__ import annotations
import json, sys
from pathlib import Path

FRONTMATTER = """---
kernelspec:
  name: python3
  display_name: Python 3
---
"""

def convert(path: Path) -> str:
    nb = json.loads(path.read_text(encoding="utf-8"))
    parts = []
    for c in nb.get("cells", []):
        src = "".join(c.get("source", [])).rstrip("\n")
        if c["cell_type"] == "markdown":
            if src.strip():
                parts.append(src)
        elif c["cell_type"] == "code":
            if src.strip():
                parts.append("```{code-cell} python\n" + src + "\n```")
    return FRONTMATTER + "\n" + "\n\n".join(parts) + "\n"

if __name__ == "__main__":
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".md")
    out.write_text(convert(src), encoding="utf-8")
    print(f"{src.name} -> {out}")
