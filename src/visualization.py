import matplotlib.pyplot as plt
import seaborn as sns
# Configurar o tamanho do gráfico
plt.figure(figsize=(15, 8))
# Gerar boxplots para variáveis relevantes
variaveis_relevantes = ["posse_de_bola", "precisao_passes", "chutes", "chutes_no_alvo"]
for i, coluna in enumerate(variaveis_relevantes, 1):
    plt.subplot(2, 2, i)
    sns.boxplot(y=dados_limpos[coluna])
    plt.title(f"Boxplot: {coluna}")
    plt.tight_layout()
plt.show()
# Plotar os dados no espaço dos dois primeiros componentes principais
plt.figure(figsize=(10, 8))
sns.scatterplot(x=pca_df["PC1"], y=pca_df["PC2"], hue=dados_limpos["Cluster"], palette="viridis", alpha=0.7)
plt.title("Projeção dos Dados no Espaço Reduzido (PC1 vs PC2)")
plt.xlabel("Componente Principal 1 (PC1)")
plt.ylabel("Componente Principal 2 (PC2)")
plt.grid(True)
plt.show()
# Criar histogramas para variáveis relevantes divididas por cluster
plt.figure(figsize=(20, 15))
for i, variavel in enumerate(variaveis_relevantes, 1):
    plt.subplot(3, 2, i)
    for cluster in clusters:
        subset = dados_limpos[dados_limpos["Cluster"] == cluster]
        plt.hist(subset[variavel], bins=15, alpha=0.6, label=f'Cluster {cluster}', edgecolor='black')
    plt.title(f'Histograma: {variavel}')
    plt.xlabel(variavel)
    plt.ylabel('Frequência')
    plt.legend()
plt.tight_layout()
plt.show()
# Gráficos de barras comparando métricas médias por cluster
caracteristicas_medias.T.plot(kind="bar", figsize=(14, 8), legend=True)
plt.title("Comparação de Métricas Médias por Cluster")
plt.xlabel("Métricas")
plt.ylabel("Média")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
