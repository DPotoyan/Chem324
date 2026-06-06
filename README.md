# Chem 3240 — Quantum Mechanics for Chemistry

Lecture notes (website) + per-lecture slides for Chem 3240.

- **Website:** [MyST-MD / Jupyter Book v2](https://mystmd.org) — config in `myst.yml`.
- **Slides:** [Quarto](https://quarto.org) reveal.js / PDF — sources in `slides/`.

This is the v2 rebuild of the old Jupyter Book v1 course (`../Chem324`).
**Status: pilot — Chapter 1 migrated.**

## Quickstart

```bash
export PATH="$HOME/Library/Python/3.9/bin:$PATH"

# Live website preview (http://localhost:3000)
myst start

# Static site build
myst build --html

# Build a lecture's slide deck
cd slides/ch01
quarto render 01-why-quantum-mechanics.qmd --to revealjs   # -> self-contained .html
quarto render 01-why-quantum-mechanics.qmd --to beamer     # -> PDF (needs LaTeX)
```

See [CLAUDE.md](CLAUDE.md) for conventions and the chapter-migration checklist.
