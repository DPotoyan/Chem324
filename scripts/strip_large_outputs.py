#!/usr/bin/env python3
"""Remove oversized code-cell outputs (animations/jshtml/interactive widgets)
from executed notebooks, keeping small static figures. Keeps notebooks lean
while preserving the clean static images. Usage: FILE.ipynb ... [--max BYTES]"""
import json, sys
from pathlib import Path
MAX = 800_000
args=[a for a in sys.argv[1:]]
if "--max" in args:
    i=args.index("--max"); MAX=int(args[i+1]); del args[i:i+2]
for p in map(Path, args):
    nb=json.loads(p.read_text()); stripped=0; kept=0
    for c in nb.get("cells",[]):
        if c.get("cell_type")!="code": continue
        newouts=[]
        for o in c.get("outputs",[]):
            sz=len(json.dumps(o))
            if sz>MAX:
                stripped+=1
            else:
                newouts.append(o); 
        if any('image' in str(o.get('data',{})) for o in newouts): kept+=1
        c["outputs"]=newouts
    p.write_text(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
    print(f"{p.name}: stripped {stripped} oversized output(s); {kept} cells keep a figure; size now {p.stat().st_size/1e6:.2f}MB")
