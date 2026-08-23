# Computational projects

Student project notebooks for Chem 3240. Each project is authored here as a
`{code-cell}` markdown file; `scripts/make_notebooks.py` turns it into
`notebooks/project-<name>.ipynb`, which is what the Colab badges open.

| project | open |
|---|---|
| Project 1: Waves, Normal Modes and Interference | [![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/project-01-waves-challenge.ipynb) |
| Project 2: Particle in a Box | [![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/project-02-particle-in-a-box.ipynb) |
| Project 3: Quantum Waves | [![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/project-03-quantum-waves-challenge.ipynb) |
| Project 4: Atomic Orbitals | [![Open in Colab](../assets/colab-badge.svg)](https://colab.research.google.com/github/DPotoyan/Chem324/blob/master/notebooks/project-04-atomic-orbitals-challenge.ipynb) |

Students open a badge, do **File > Save a copy in Drive**, work, then run
**Runtime > Restart and run all** before downloading the `.ipynb` for Canvas.

After editing any project source, regenerate the notebooks:

```bash
python3 scripts/make_notebooks.py
```

To preview a project locally:

```bash
uvx jupytext --to ipynb projects/01-waves-challenge.md -o /tmp/p1.ipynb && jupyter lab /tmp/p1.ipynb
```
