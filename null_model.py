# null_model.py
# Shuffles parameters to generate null hypothesis match distribution

def main():
    import pandas as pd
    import numpy as np
    import os

    print("🌀 Generating null distribution...")

    match_path = "outputs/gw_cmb_crossmatch.csv"
    if not os.path.exists(match_path):
        print("⚠️ Crossmatch results missing.")
        return

    df = pd.read_csv(match_path)
    null_scores = []

    for _ in range(1000):
        shuffled = df.copy()
        shuffled["ring_ra"] = np.random.permutation(shuffled["ring_ra"])
        shuffled["ring_dec"] = np.random.permutation(shuffled["ring_dec"])

        shuffled["null_score"] = 1 / (1 + np.sqrt((shuffled["echo_ra"] - shuffled["ring_ra"])**2 +
                                                  (shuffled["echo_dec"] - shuffled["ring_dec"])**2))
        null_scores.extend(shuffled["null_score"].tolist())

    pd.DataFrame({"null_score": null_scores}).to_csv("outputs/null_match_distribution.csv", index=False)
    print("✅ Null model distribution saved.")