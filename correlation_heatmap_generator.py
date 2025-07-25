# MEN Engine: Extended Correlation Heatmap Generator

def main():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import os

    data_file = "summary_stats.csv"
    if not os.path.exists(data_file):
        raise FileNotFoundError("Missing input: summary_stats.csv")

    df = pd.read_csv(data_file)
    numeric_df = df.select_dtypes(include=[np.number])

    pearson_corr = numeric_df.corr(method='pearson')
    spearman_corr = numeric_df.corr(method='spearman')

    plt.figure(figsize=(10, 8))
    sns.heatmap(pearson_corr, annot=True, cmap="coolwarm", fmt=".2f", square=True)
    plt.title("Pearson Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("pearson_correlation_heatmap.png", dpi=300)
    plt.close()

    plt.figure(figsize=(10, 8))
    sns.heatmap(spearman_corr, annot=True, cmap="coolwarm", fmt=".2f", square=True)
    plt.title("Spearman Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("spearman_correlation_heatmap.png", dpi=300)
    plt.close()

    print("✅ Correlation heatmaps generated")