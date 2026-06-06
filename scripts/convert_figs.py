#!/usr/bin/env python3
"""Convert v1 Jupyter-Book `:::{figure-md}` + <img> blocks to native MyST `:::{figure}`."""
import re
import sys
from pathlib import Path

ATTR = lambda name, s: (re.search(rf'{name}\s*=\s*"([^"]*)"', s) or [None, None])[1]

def convert(text: str) -> tuple[str, int]:
    lines = text.split("\n")
    out, i, n = [], 0, len(lines)
    count = 0
    while i < n:
        line = lines[i]
        if re.match(r"^\s*:::\{figure-md\}", line):
            # gather block until the closing standalone ::: line
            j = i + 1
            block = []
            while j < n and lines[j].strip() != ":::":
                block.append(lines[j])
                j += 1
            # j now points at the closing :::
            body = "\n".join(block)
            img = re.search(r"<img\b[^>]*>", body)
            if img:
                tag = img.group(0)
                src = ATTR("src", tag) or ""
                alt = ATTR("alt", tag)
                width = ATTR("width", tag)
                # caption = everything in the block except the <img> line, trimmed of blank edges
                caption_lines = [l for l in block if "<img" not in l]
                while caption_lines and caption_lines[0].strip() == "":
                    caption_lines.pop(0)
                while caption_lines and caption_lines[-1].strip() == "":
                    caption_lines.pop()
                new = [f":::{{figure}} {src}"]
                if alt:
                    new.append(f":alt: {alt}")
                if width:
                    new.append(f":width: {width}")
                new.append("")
                new.extend(caption_lines)
                new.append(":::")
                out.extend(new)
                count += 1
                i = j + 1
                continue
            # no img found: leave block untouched
            out.append(line)
            i += 1
            continue
        out.append(line)
        i += 1
    return "\n".join(out), count

total = 0
for path in map(Path, sys.argv[1:]):
    new, c = convert(path.read_text())
    path.write_text(new)
    print(f"{path.name}: {c} figures converted")
    total += c
print(f"TOTAL: {total}")
