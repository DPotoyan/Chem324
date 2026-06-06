#!/usr/bin/env python3
"""Promote a notebook's first markdown heading to a single '#' H1 so MyST uses it
as the page title (rendered once) instead of duplicating it. Usage: FILE.ipynb ..."""
import json, re, sys
from pathlib import Path
def fix(path):
    nb=json.loads(Path(path).read_text())
    for c in nb.get("cells",[]):
        if c["cell_type"]!="markdown": continue
        src=c["source"] if isinstance(c["source"],list) else c["source"].splitlines(keepends=True)
        for i,line in enumerate(src):
            m=re.match(r"^(#{1,6})(\s+\S)", line)
            if m:
                if len(m.group(1))>1:
                    src[i]="#"+line[len(m.group(1)):]
                    c["source"]=src
                    Path(path).write_text(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
                    return f"{Path(path).name}: '{line.strip()[:35]}' -> H1"
                return f"{Path(path).name}: already H1"
    return f"{Path(path).name}: no heading found"
for p in sys.argv[1:]: print(fix(p))
