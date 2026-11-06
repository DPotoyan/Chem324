"""Trim the measured infrared spectra of Lecture 4.5 into ch04/data/ (see ch04/data/README.md).

Run from the repo root, only to rebuild the CSVs (they are committed; the 13 MB raw HCl file is not):
    .venv/bin/python scripts/make_ch04_spectra_data.py

The raw files come from the PIPER teaching-dataset repository, pinned to one commit, because its history shows an
earlier HCl file was replaced for a 1 cm^-1 calibration offset. Absorbances are kept as recorded; no baseline is removed
here. Two files are thinned to keep the repo light: within each bin the point farthest from zero is kept, so line heights
survive. It also prints the H35Cl line table pasted into `hcl_gaps` and the page's visible fit cell.
"""
import io
import os
import urllib.parse
import urllib.request

import numpy as np

COMMIT = "2853b668da67f8e8e918f92b9762a054ed0ab821"
RAW = f"https://raw.githubusercontent.com/singletS/datasets-gh/{COMMIT}"
OUT = "ch04/data"
HCL_NOTE = "HCl and DCl gas, 20 Torr, 10 cm cell, FTIR at 0.125 cm^-1. J. Gutow, University of Wisconsin-Oshkosh, via PIPER"
CO_NOTE = "CO gas, FTIR, recorded at the POGIL-PCL meeting, UT Austin, January 2018, via PIPER"


def fetch(path):
    url = f"{RAW}/{urllib.parse.quote(path)}"
    with urllib.request.urlopen(url, timeout=120) as r:
        text = r.read().decode("latin-1")
    a = np.genfromtxt(io.StringIO(text), delimiter=",", skip_header=1, invalid_raise=False)
    a = a[np.isfinite(a).all(axis=1)]
    return a[np.argsort(a[:, 0])]


def window(a, lo, hi):
    return a[(a[:, 0] >= lo) & (a[:, 0] <= hi)]


def thin(a, width):
    """Keep, in each bin of this width, the point farthest from zero, so that peaks keep their height."""
    bins = np.floor((a[:, 0] - a[0, 0]) / width).astype(int)
    edges = np.flatnonzero(np.diff(bins)) + 1
    keep = [seg[np.argmax(np.abs(a[seg, 1]))] for seg in np.split(np.arange(len(a)), edges)]
    return a[keep]


def save(name, a, note, fmt="%.3f,%.4f"):
    path = f"{OUT}/{name}"
    np.savetxt(path, a, fmt=fmt, header=f"{note}\nwavenumber (cm^-1),absorbance")
    print(f"wrote {path}: {len(a)} points, {os.path.getsize(path) / 1024:.0f} KB")


def peak_near(a, guess, half=0.4):
    w = window(a, guess - half, guess + half)
    return w[np.argmax(w[:, 1]), 0]


os.makedirs(OUT, exist_ok=True)
hcl = fetch("hcl-dcl-IR/P Chem HCl_10_13_2025.CSV")
save("hcl_band.csv", thin(window(hcl, 2580, 3120), 0.1), HCL_NOTE + "; thinned to 0.1 cm^-1 bins")
save("hcl_zoom.csv", window(hcl, 2935, 2970), HCL_NOTE)
save("hcl_survey.csv", thin(window(hcl, 1800, 6100), 1.0), HCL_NOTE + "; thinned to 1 cm^-1 bins")
co = fetch("CO_irspectra/CO_0p25.csv")
save("co_fine.csv", window(co, 2000, 2295), CO_NOTE + "; 0.25 cm^-1")
co2 = fetch("CO_irspectra/CO_2p0.csv")
save("co_coarse.csv", window(co2, 2000, 2295), CO_NOTE + "; 2 cm^-1")

# the H35Cl line table: assign each measured peak from the literature constants, then let the fit stand on the data
nu0, B0, B1, D = 2885.98, 10.440, 10.136, 5.3e-4
F = lambda B, J: B * J * (J + 1) - D * (J * (J + 1)) ** 2
m, nu = [], []
for J in range(13, 0, -1):
    m.append(-J); nu.append(peak_near(hcl, nu0 + F(B1, J - 1) - F(B0, J)))
for J in range(0, 12):
    m.append(J + 1); nu.append(peak_near(hcl, nu0 + F(B1, J + 1) - F(B0, J)))
m, nu = np.array(m), np.array(nu)
c3, c2, c1, c0 = np.polyfit(m, nu, 3)
print("m =", m.tolist())
print("nu =", np.round(nu, 2).tolist())
print(f"fit: nu0 = {c0:.2f}, B0 = {(c1 - c2) / 2:.3f}, B1 = {(c1 + c2) / 2:.3f}, D = {-c3 / 4:.2e}")
