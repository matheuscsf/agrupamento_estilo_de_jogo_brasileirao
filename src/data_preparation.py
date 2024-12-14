# Carregar o dataset
dados = pd.read_csv('campeonato-brasileiro-estatisticas-full.csv')
# Exibir informações gerais sobre o dataset
informacoes_gerais = dados.info()
# Verificar a presença de valores ausentes
valores_ausentes = dados.isnull().sum()
# Remover as linhas com valores ausentes nas colunas "posse_de_bola" e "precisao_passes"
dados_limpos = dados.dropna(subset=["posse_de_bola", "precisao_passes"])
dados_limpos
# Converter colunas de porcentagens (em texto) para valores numéricos
dados_limpos["posse_de_bola"] = dados_limpos["posse_de_bola"].str.replace('%', '').astype(float)
dados_limpos["precisao_passes"] = dados_limpos["precisao_passes"].str.replace('%', '').astype(float)
# Inicializar o escalador e aplicar a normalização
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
dados_normalizados = scaler.fit_transform(dados_limpos[colunas_para_normalizar])