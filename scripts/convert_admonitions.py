#!/usr/bin/env python3
"""Convert generic `:::{admonition}` + `:class:` into MyST named directives.

note/important/tip/warning/... -> named directive (distinct color).
dropdown-only "Solution"/"Answer" -> collapsible violet `solution` card.
Handles whitespace- AND comma-separated class lists.

Usage: python3 convert_admonitions.py FILE.md [FILE.md ...]
"""
from __future__ import annotations
import re, sys
from pathlib import Path

KINDS = {"note","important","tip","warning","caution","danger","hint","seealso","attention","error"}

def convert(text: str) -> tuple[str, int]:
    lines = text.split("\n"); out=[]; i=0; n=len(lines); changed=0
    while i < n:
        m = re.match(r"^(\s*):::\{admonition\}\s*(.*)$", lines[i])
        if m and i+1 < n and ":class:" in lines[i+1]:
            indent, title = m.group(1), m.group(2).strip()
            raw = lines[i+1].split(":class:")[1]
            classes = [c for c in re.split(r"[,\s]+", raw.strip()) if c]
            kind = next((c for c in classes if c in KINDS), None)
            dropdown = "dropdown" in classes
            is_solution = kind is None and re.search(r"(solution|answer)", title, re.I)
            if kind:
                out.append(f"{indent}:::{{{kind}}} {title}".rstrip())
                if dropdown:
                    out.append(f"{indent}:class: dropdown")
            elif is_solution:
                out.append(f"{indent}:::{{admonition}} {title}".rstrip())
                out.append(f"{indent}:class: dropdown solution")
            else:
                out.append(lines[i]); out.append(lines[i+1]); i += 2; continue
            changed += 1; i += 2; continue
        out.append(lines[i]); i += 1
    return "\n".join(out), changed

if __name__ == "__main__":
    tot = 0
    for p in map(Path, sys.argv[1:]):
        new, c = convert(p.read_text(encoding="utf-8"))
        p.write_text(new, encoding="utf-8")
        print(f"{p.name}: {c} admonitions -> named directives")
        tot += c
    print("TOTAL:", tot)
