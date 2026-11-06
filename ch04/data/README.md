# Measured spectra for Lecture 4.5

Trimmed by `scripts/make_ch04_spectra_data.py` from the PIPER teaching-dataset repository
(<https://github.com/singletS/datasets-gh>, commit `2853b668`). PIPER is run by Steve Singleton, Coe College.
Absorbances are as recorded. Every CSV has a two-line `#` header.

| file | source | contents |
| :-- | :-- | :-- |
| `hcl_band.csv` | J. Gutow, University of Wisconsin-Oshkosh | HCl fundamental, thinned to 0.1 cm^-1 bins, each bin keeping its largest value |
| `hcl_zoom.csv` | same | R(2), R(3) at full sampling |
| `hcl_survey.csv` | same | 1800 to 6100 cm^-1, thinned to 1 cm^-1 bins |
| `co_fine.csv` | POGIL-PCL meeting, UT Austin, January 2018 | CO at 0.25 cm^-1 |
| `co_coarse.csv` | same | CO at 2 cm^-1 |

The HCl scan: 20 Torr, 10 cm cell, 0.125 cm^-1 resolution. It also contains DCl, the HCl overtone, and small inverted
features from CO2 and water in the room air.

**Licence: not stated.** The repository has no license file and the PIPER site gives no reuse terms; the datasets are
described as being "for use with curriculum materials". Confirm with the authors before relying on this.
