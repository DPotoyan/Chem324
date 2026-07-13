import re, sys, os, glob
from PIL import Image, ImageSequence

ROOT='.'  # run from Chem324
CH_TITLES={
 'ch01':'Chapter 1: Intro to Quantum Mechanics','ch02':'Chapter 2: Waves and the Wave Equation',
 'ch03':'Chapter 3: The Schrodinger Equation','ch04':'Chapter 4: Model Systems',
 'ch05':'Chapter 5: The Hydrogen Atom','ch06':'Chapter 6: Approximation Methods',
 'ch07':'Chapter 7: Multi-Electron Atoms','ch08':'Chapter 8: Molecular Orbital Theory'}

FRONT='''---
title: "Chem 3240: Quantum Mechanics"
subtitle: "Lecture slides, print handout"
author: "Davit Potoyan"
institute: "Department of Chemistry, Iowa State University"
date: today
format:
  beamer:
    theme: moloch
    themeoptions:
      - colortheme=tomorrow
      - progressbar=frametitle
      - sectionpage=progressbar
      - titleformat=regular
    aspectratio: 169
    navigation: empty
    pdf-engine: lualatex
    toc: false
    incremental: false
    slide-level: 2
    include-in-header: header.tex
    fig-align: center
---
'''

def gif_still(relpath, qmd_dir):
    # relpath like ../../ch04/images/foo.gif relative to a slides/<x>/ deck dir
    src=os.path.normpath(os.path.join(qmd_dir, relpath))
    still=src[:-4]+'-still.png'
    if os.path.exists(src) and not os.path.exists(still):
        im=Image.open(src); im.seek(0); im.convert('RGB').save(still)
    return relpath[:-4]+'-still.png'

INKSCAPE='/Applications/Inkscape.app/Contents/MacOS/inkscape'

def svg_pdf(relpath, qmd_dir):
    # beamer/lualatex can't embed SVG without rsvg-convert; pre-convert to PDF
    src=os.path.normpath(os.path.join(qmd_dir, relpath))
    pdf=src[:-4]+'.pdf'
    if os.path.exists(src) and not os.path.exists(pdf):
        import subprocess
        subprocess.run([INKSCAPE, src, '--export-type=pdf',
                        '--export-filename='+pdf], check=True)
    return relpath[:-4]+'.pdf'

def pad_fences(text):
    # pandoc only opens/closes a fenced div at a block boundary, so every
    # ::: fence needs a blank line on both sides (e.g. a ::: {.fragment}
    # directly after a $$ block otherwise leaks through as literal text and
    # breaks the surrounding columns environment in beamer).
    out=[]
    for l in text.split('\n'):
        fence=l.lstrip().startswith(':::')
        if fence and out and out[-1].strip()!='':
            out.append('')
        out.append(l)
        if fence:
            out.append('')
    # collapse runs of blank lines
    res=[]; blank=False
    for l in out:
        if l.strip()=='':
            if blank: continue
            blank=True
        else:
            blank=False
        res.append(l)
    return '\n'.join(res)

def transform(path):
    txt=open(path,encoding='utf-8').read()
    # strip YAML frontmatter
    if txt.startswith('---'):
        txt=txt.split('---',2)[2]
    qmd_dir=os.path.dirname(path)
    out=[]
    for l in txt.split('\n'):
        h=re.match(r'^(#{1,6})\s+(.*)$', l)
        if h:
            title=re.sub(r'\s*\{[^}]*\}\s*$','',h.group(2)).strip()
            out.append('## '+title)   # every deck heading becomes a frame
            continue
        out.append(l)
    body='\n'.join(out)
    # gif -> still png (create still, rewrite ref)
    for m in re.findall(r'\]\(([^)]+\.gif)\)', body):
        body=body.replace('('+m+')', '('+gif_still(m, qmd_dir)+')')
    # svg -> pdf (beamer can't embed svg without rsvg-convert)
    for m in re.findall(r'\]\(([^)]+\.svg)\)', body):
        body=body.replace('('+m+')', '('+svg_pdf(m, qmd_dir)+')')
    # collapse single-line inline fragments ("- ::: {.fragment} text :::"):
    # these aren't valid block fences and leak as literal ::: in print, and
    # incremental reveal is meaningless in a static handout anyway.
    body=re.sub(r':::+ *\{\.fragment\} *(.*?) *:::+', r'\1', body)
    return pad_fences(body.strip())

def build(chapters, outpath):
    parts=[FRONT]
    for ch in chapters:
        parts.append('\n# '+CH_TITLES[ch]+'\n')
        for f in sorted(glob.glob(f'slides/{ch}/*.qmd')):
            parts.append('\n'+transform(f)+'\n')
    open(outpath,'w',encoding='utf-8').write('\n'.join(parts))
    print('wrote', outpath, 'from chapters', chapters)

if __name__=='__main__':
    chapters=sys.argv[1].split(',') if len(sys.argv)>1 else list(CH_TITLES)
    out=sys.argv[2] if len(sys.argv)>2 else 'slides/handout/Chem3240-slides.qmd'
    build(chapters, out)
