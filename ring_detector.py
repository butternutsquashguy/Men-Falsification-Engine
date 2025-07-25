# ring_detector.py
# Scans HEALPix map for ring-like structures

def main():
    import healpy as hp
    import numpy as np
    import pandas as pd
    import os

    print("🔍 Scanning CMB map for ring structures...")

    map_path = "outputs/fake_smica_map.fits"
    if not os.path.exists(map_path):
        print(f"⚠️ CMB map not found at {map_path}")
        return

    cmb_map = hp.read_map(map_path)
    nside = hp.get_nside(cmb_map)

    ring_radii = [0.2, 0.4, 0.6]
    ring_scores = []

    for i, radius in enumerate(ring_radii):
        score = np.corrcoef(cmb_map, np.roll(cmb_map, int(radius * 100)))[0, 1]
        ring_scores.append((i, radius, score))

    df = pd.DataFrame(ring_scores, columns=["id", "radius", "pearson_r"])
    df.to_csv("outputs/cmb_ring_candidates.csv", index=False)

    print("✅ CMB ring scan complete. Candidates saved.")