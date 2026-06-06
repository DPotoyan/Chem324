#!/usr/bin/env python3
"""Strip saved outputs + execution counts from .ipynb files (like nbstripout, no deps).

Usage:
    python3 strip_notebooks.py [--dry-run] PATH [PATH ...]

PATH may be a directory (recursed) or individual .ipynb files. Skips checkpoints.
Clears code-cell `outputs` and `execution_count`, and notebook-level kernel
counters; leaves all source, markdown, attachments, and metadata intact.
"""
from __future__ import annotations
import json, os, sys, glob


def gather(paths):
    out = []
    for p in paths:
        if os.path.isdir(p):
            out += glob.glob(os.path.join(p, "**", "*.ipynb"), recursive=True)
        elif p.endswith(".ipynb"):
            out.append(p)
    return [f for f in out if ".ipynb_checkpoints" not in f and "/.git/" not in f]


def strip(path) -> tuple[int, int, bool]:
    before = os.path.getsize(path)
    nb = json.load(open(path, encoding="utf-8"))
    changed = False
    for c in nb.get("cells", []):
        if c.get("cell_type") == "code":
            if c.get("outputs"):
                c["outputs"] = []; changed = True
            if c.get("execution_count") is not None:
                c["execution_count"] = None; changed = True
    if changed:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(nb, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
    return before, os.path.getsize(path), changed


def main(argv):
    dry = "--dry-run" in argv
    files = gather([a for a in argv if a != "--dry-run"])
    tot_b = tot_a = 0
    for f in sorted(files):
        b = os.path.getsize(f)
        if dry:
            a = b
            print(f"   {b/1e6:7.2f} MB  {f}")
        else:
            b, a, ch = strip(f)
            tag = "stripped" if ch else "clean"
            print(f"   {b/1e6:7.2f} -> {a/1e6:6.2f} MB  [{tag}]  {f}")
        tot_b += b; tot_a += a
    print(f"\n{len(files)} notebooks   {tot_b/1e6:.1f} MB -> {tot_a/1e6:.1f} MB"
          f"   (reclaimed {(tot_b-tot_a)/1e6:.1f} MB)")


if __name__ == "__main__":
    main(sys.argv[1:])
