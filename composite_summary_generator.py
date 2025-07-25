# MEN Engine: Composite Summary Generator

def main():
    import pandas as pd
    import json
    import os

    summary_file = "summary_stats.csv"
    pca_file = "pca_clustered_stats.csv"

    if not os.path.exists(summary_file):
        raise FileNotFoundError("Missing input: summary_stats.csv")
    if not os.path.exists(pca_file):
        raise FileNotFoundError("Missing input: pca_clustered_stats.csv")

    summary_df = pd.read_csv(summary_file)
    pca_df = pd.read_csv(pca_file)

    merged_df = pd.concat([summary_df, pca_df[['PCA1', 'PCA2', 'Cluster']]], axis=1)
    merged_df.to_csv("composite_summary.csv", index=False)

    json_summary = merged_df.to_dict(orient="records")
    with open("composite_summary.json", "w") as f:
        json.dump(json_summary, f, indent=2)

    print("✅ Composite summary generated")