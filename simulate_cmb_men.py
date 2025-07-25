# simulate_cmb_men.py
# Injects synthetic MEN-like ring imprint into CMB map

def main():
    import healpy as hp
    import numpy as np
    import os

    print("🧪 Simulating MEN imprint in CMB...")

    map_path = "outputs/fake_smica_map.fits"
    if not os.path.exists(map_path):
        print("⚠️ CMB map not found.")
        return

    cmb_map = hp.read_map(map_path)
    npix = len(cmb_map)
    center = npix // 2
    ring_width = 10

    # Inject Gaussian ring
    for offset in range(-ring_width, ring_width + 1):
        cmb_map[(center + offset) % npix] += np.exp(-offset**2 / (2 * 3**2)) * 50e-6

    hp.write_map("outputs/cmb_with_men_imprint.fits", cmb_map, overwrite=True)
    print("✅ MEN imprint simulation complete.")