# MEN Engine: PCA + Clustering Visualizer Module

def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA
    from sklearn.cluster import DBSCAN
    from sklearn.preprocessing import StandardScaler
    import seaborn as sns
    import os

    data_file = "summary_stats.csv"
    if not os.path.exists(data_file):
        raise FileNotFoundError("Missing input: summary_stats.csv")

    df = pd.read_csv(data_file)
    features = df.select_dtypes(include=[np.number])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    df['PCA1'] = X_pca[:, 0]
    df['PCA2'] = X_pca[:, 1]

    db = DBSCAN(eps=0.5, min_samples=3).fit(X_pca)
    df['Cluster'] = db.labels_

    df.to_csv("pca_clustered_stats.csv", index=False)

    plt.figure(figsize=(10, 7))
    palette = sns.color_palette("hsv", len(set(df['Cluster'])))
    sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette=palette, legend='full')
    plt.title("PCA Projection with DBSCAN Clusters")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend(title="Cluster")
    plt.tight_layout()
    plt.savefig("pca_clustering_plot.png", dpi=300)

    print("✅ PCA clustering complete")