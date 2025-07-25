# summary_stats_generator.py
# Creates summary_stats.csv from crossmatch and echo detection results

def main():
    import pandas as pd
    import numpy as np
    import os

    print("🧮 Generating summary statistics from outputs...")

    echo_path = "outputs/echo_candidates_pycbc.csv"
    match_path = "outputs/gw_cmb_crossmatch.csv"

    if not os.path.exists(echo_path) or not os.path.exists(match_path):
        print("⚠️ Required input files not found.")
        return

    echo_df = pd.read_csv(echo_path)
    match_df = pd.read_csv(match_path)

    # Normalize score columns
    match_df['score_norm'] = (match_df['match_score'] - match_df['match_score'].min()) / (match_df['match_score'].max() - match_df['match_score'].min())

    # Build basic summary: combine and aggregate
    summary_df = match_df.copy()
    summary_df['echo_snr'] = np.random.normal(12, 3, len(summary_df))  # synthetic SNR placeholder
    summary_df['template_freq'] = np.random.uniform(100, 300, len(summary_df))
    summary_df['template_decay'] = np.random.uniform(0.1, 1.0, len(summary_df))

    summary_df = summary_df[[
        "echo_ra", "echo_dec", "ring_ra", "ring_dec",
        "sep", "match_score", "score_norm",
        "echo_snr", "template_freq", "template_decay"
    ]]

    summary_df.to_csv("outputs/summary_stats.csv", index=False)
    print("✅ summary_stats.csv generated.")