from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
# Configurar o modelo K-means
kmeans = KMeans(n_clusters=3, random_state=42)
# Ajustar o modelo e prever os clusters
clusters = kmeans.fit_predict(dados_normalizados)
# Adicionar os clusters ao DataFrame original
dados_limpos["Cluster"] = clusters
# Calcular a pontuação silhouette
silhouette_avg = silhouette_score(dados_normalizados, clusters)
print(f"Média do coeficiente silhouette: {silhouette_avg}")
# Gráfico de dispersão no espaço dos componentes principais
plt.figure(figsize=(10, 8))
sns.scatterplot(x=pca_df["PC1"], y=pca_df["PC2"], hue=dados_limpos["Cluster"], palette="viridis", alpha=0.7)
plt.title("Projeção dos Dados no Espaço Reduzido (PC1 vs PC2)")
plt.xlabel("Componente Principal 1 (PC1)")
plt.ylabel("Componente Principal 2 (PC2)")
plt.grid(True)
plt.show()
# Analisar características médias por cluster
caracteristicas_medias = dados_limpos.groupby("Cluster")[colunas_para_normalizar].mean()
print(caracteristicas_medias)
