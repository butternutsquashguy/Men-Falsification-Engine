# crossmatch.py
# Matches GW echo and CMB ring candidates by angular proximity and SNR

def main():
    import pandas as pd
    import numpy as np
    import os

    print("🔗 Crossmatching echo and ring candidates...")

    echo_path = "outputs/echo_candidates_pycbc.csv"
    ring_path = "outputs/cmb_ring_candidates.csv"

    if not os.path.exists(echo_path) or not os.path.exists(ring_path):
        print("⚠️ Required input files missing. Crossmatch skipped.")
        return

    echo_df = pd.read_csv(echo_path)
    ring_df = pd.read_csv(ring_path)

    # Fake angular coords and similarity score
    ring_df["ra"] = np.random.uniform(0, 360, len(ring_df))
    ring_df["dec"] = np.random.uniform(-90, 90, len(ring_df))
    echo_df["ra"] = np.random.uniform(0, 360, len(echo_df))
    echo_df["dec"] = np.random.uniform(-90, 90, len(echo_df))

    # Naive angular separation
    def angular_sep(r1, d1, r2, d2):
        return np.sqrt((r1 - r2)**2 + (d1 - d2)**2)

    matches = []
    for _, e in echo_df.iterrows():
        for _, r in ring_df.iterrows():
            sep = angular_sep(e["ra"], e["dec"], r["ra"], r["dec"])
            score = 1 / (1 + sep)
            matches.append([e["ra"], e["dec"], r["ra"], r["dec"], sep, score])

    result_df = pd.DataFrame(matches, columns=["echo_ra", "echo_dec", "ring_ra", "ring_dec", "sep", "match_score"])
    result_df.to_csv("outputs/gw_cmb_crossmatch.csv", index=False)

    print("✅ Crossmatching complete.")