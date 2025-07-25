
[![GitHub Repo](https://img.shields.io/badge/GitHub-MEN--Falsification--Engine-black?logo=github)](https://github.com/butternutsquashguy/MEN-Falsification-Engine)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/butternutsquashguy/MEN-Falsification-Engine/blob/main/index_sequential.ipynb)


# MEN Falsification Engine v3.0 (Upgraded)

This repository contains the full scientific pipeline for testing the hypothesis of **Maximally Entangled Nonspace (MEN)** via gravitational wave (GW) echoes, cosmic microwave background (CMB) residuals, and statistical crossmatching.

---

## 📦 Contents

- `MEN_Falsification_Engine.py` — Full pipeline controller (parallel + notebook-ready)
- `template_generator.py` — Generates parameter-swept echo templates
- `inject_echo.py` — Injects synthetic echoes into simulated GW strain
- `echo_detector_pycbc.py` — FFT-based matched filtering using PyCBC
- `echo_detector_bilby.py` — Bayesian echo inference using Bilby
- `echo_detector_comb.py` — Frequency-domain periodic echo detection
- `load_cmb.py` — Loads (or simulates) Planck SMICA CMB map
- `ring_detector.py` — Scans CMB maps for concentric ring structures
- `ring_classifier_ml.py` — Scores rings via ML (simulated ResNet)
- `crossmatch.py` — Matches GW echo and CMB ring candidates
- `null_model.py` — Generates null distribution for significance testing
- `simulate_cmb_men.py` — Injects synthetic MEN imprint into CMB map
- `chirplet_transform_overlay.py` — Visualizes chirplet-based echo enhancement
- `pca_clustering_visualizer.py` — Projects summary data using PCA + DBSCAN
- `correlation_heatmap_generator.py` — Produces correlation matrix heatmaps
- `composite_summary_generator.py` — Combines stats and scores into JSON/CSV

---

## 🧠 Overview

This system:
- Detects potential GW echo signals across parameter space
- Analyzes CMB maps for ring-like residuals
- Matches signals statistically, generates null distributions
- Supports Colab, Docker, notebook, and CLI execution

---

## 🚀 Quick Start (Colab)

Paste into a Colab cell:

```python
!pip install matplotlib pandas numpy scikit-learn seaborn healpy bilby pycbc

from MEN_Falsification_Engine import main
main()
```

---

## 🐳 Quick Start (Docker)

```bash
docker build -t men_superpipe_full .
docker run -v $(pwd):/app -it men_superpipe_full
```

Windows users: double-click `run_men_engine.bat`

---

## ⚙️ Requirements

- Python 3.10+
- pip packages: `pycbc`, `bilby`, `healpy`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

Optional (for plotting or HPC):  
- `tensorflow`, `corner`, `h5py`, `emcee`

---

## 🧪 Output Files

All outputs are saved to `/outputs`, including:
- Echo candidate lists (`echo_candidates_*.csv`)
- CMB ring candidates (`cmb_ring_candidates.csv`)
- Crossmatches (`gw_cmb_crossmatch.csv`)
- Null distribution (`null_match_distribution.csv`)
- Visualizations (`*.png`)
- Composite summaries (`composite_summary.*`)

---

## 📄 License
This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for full terms.
