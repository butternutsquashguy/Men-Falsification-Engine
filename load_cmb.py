# load_cmb.py
# Loads Planck SMICA map and extracts temperature data

def main():
    import healpy as hp
    import numpy as np
    import os

    print("🌌 Loading Planck SMICA map...")

    # Placeholder: create synthetic HEALPix map
    nside = 64
    npix = hp.nside2npix(nside)
    cmb_map = np.random.normal(0, 30e-6, npix)

    os.makedirs("outputs", exist_ok=True)
    hp.write_map("outputs/fake_smica_map.fits", cmb_map, overwrite=True)

    print("✅ Simulated SMICA map saved as FITS.")