#!/usr/bin/env python3
"""Add a unique `:label: fig-<slug>-<n>` to every `:::{figure}` that lacks one,
so figures can be auto-numbered and cross-referenced.

The slug is derived from the file name (NN-slug.md -> slug). Pass files explicitly.

Usage: python3 label_figures.py FILE.md [FILE.md ...]
"""
from __future__ import annotations
import re, sys
from pathlib import Path

def label(path: Path) -> int:
    slug = re.sub(r'^\d+-', '', path.stem)
    lines = path.read_text(encoding="utf-8").split("\n")
    out=[]; n=0
    for i, l in enumerate(lines):
        out.append(l)
        m = re.match(r"^(\s*):::\{figure\}\s+\S", l)
        if m and not (i+1 < len(lines) and ":label:" in lines[i+1]):
            n += 1
            out.append(f"{m.group(1)}:label: fig-{slug}-{n}")
    if n:
        path.write_text("\n".join(out), encoding="utf-8")
    return n

if __name__ == "__main__":
    for p in map(Path, sys.argv[1:]):
        print(f"{p.name}: {label(p)} figures labeled")
