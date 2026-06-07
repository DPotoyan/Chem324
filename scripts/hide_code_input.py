#!/usr/bin/env python3
"""Add `:tags: [hide-input]` to every ```{code-cell}``` block that lacks tags,
so the code collapses (toggle) while its output (figure) stays visible.
Use on LECTURE .md files, not demo notebooks. Usage: FILE.md ..."""
import re, sys
from pathlib import Path
def tag(path):
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    out=[]; n=0
    for i,l in enumerate(lines):
        out.append(l)
        if re.match(r"^```\{code-cell\}", l):
            nxt = lines[i+1] if i+1 < len(lines) else ""
            if not nxt.strip().startswith(":tags:"):
                out.append(":tags: [hide-input]"); n+=1
    Path(path).write_text("\n".join(out), encoding="utf-8")
    return n
for p in sys.argv[1:]:
    print(f"{Path(p).name}: tagged {tag(p)} code cells hide-input")
