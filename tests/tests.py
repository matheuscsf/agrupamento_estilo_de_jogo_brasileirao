from sklearn.metrics import silhouette_score
# Verificar a presença de valores ausentes
valores_ausentes = dados.isnull().sum()
print(valores_ausentes)
# Verificar as dimensões do dataset após a limpeza
dimensoes_apos_limpeza = dados_limpos.shape
print(dimensoes_apos_limpeza)
# Confirmar se ainda há valores ausentes nas colunas mencionadas
valores_ausentes_apos_limpeza = dados_limpos[["posse_de_bola", "precisao_passes"]].isnull().sum()
print(valores_ausentes_apos_limpeza)
# Verificar os tipos de dados após a conversão
tipos_dados_apos_conversao = dados_limpos.dtypes
print(tipos_dados_apos_conversao)
# Confirmar as primeiras linhas das colunas convertidas
amostra_dados_convertidos = dados_limpos[["posse_de_bola", "precisao_passes"]].head()
print(amostra_dados_convertidos)
# Calcular a pontuação silhouette
silhouette_avg = silhouette_score(dados_normalizados, clusters)
print(f"Média do coeficiente silhouette: {silhouette_avg}")
# Verificar a distribuição dos clusters no espaço dos componentes principais
plt.figure(figsize=(10, 8))
sns.scatterplot(x=pca_df["PC1"], y=pca_df["PC2"], hue=dados_limpos["Cluster"], palette="viridis", alpha=0.7)
plt.title("Projeção dos Dados no Espaço Reduzido (PC1 vs PC2)")
plt.xlabel("Componente Principal 1 (PC1)")
plt.ylabel("Componente Principal 2 (PC2)")
plt.grid(True)
plt.show()