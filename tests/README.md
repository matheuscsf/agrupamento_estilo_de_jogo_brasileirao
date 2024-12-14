# 🧪 Diretório `tests/`

Este diretório contém os **scripts de teste** do projeto, desenvolvidos para garantir a qualidade e a confiabilidade dos módulos implementados no diretório `src/`.

---

## 🗂️ Estrutura

A estrutura dos arquivos de teste segue a mesma organização dos módulos em `src/`:

```plaintext
tests/
├── test_data_preparation.py   # Testes para as funções de preparação de dados
├── test_clustering.py         # Testes para o algoritmo de clustering
├── test_visualization.py      # Testes para as funções de visualização
└── conftest.py                # Configurações e fixtures para testes (opcional)
```

---

## 📝 Descrição dos Arquivos

test_data_preparation.py
- Valida as funções de limpeza e transformação dos dados.
- Testa cenários como:
  - Dados com valores ausentes.
  - Formatos inconsistentes.
  - Normalização de variáveis.

test_clustering.py
- Testa a implementação do algoritmo K-means.
- Avalia a consistência dos resultados para diferentes conjuntos de dados.
- Verifica o cálculo de métricas como inércia e silhouette.
  
test_visualization.py
- Garante que as funções de visualização geram gráficos sem erros.
- Testa os parâmetros de entrada para cada tipo de gráfico.

conftest.py (opcional)
- Define fixtures reutilizáveis para inicializar dados ou estados comuns entre os testes.
