# 🛠️ Diretório `src/`

Este diretório contém o **código-fonte principal** do projeto, organizado em módulos para facilitar o desenvolvimento, manutenção e reutilização.

---

## 🗂️ Estrutura

Os arquivos neste diretório estão organizados por funcionalidade:

```plaintext
src/
├── data_preparation.py       # Funções para limpeza e transformação dos dados
├── clustering.py             # Implementação do algoritmo de clustering
└── visualization.py          # Funções para criação de gráficos e visualizações 
```

---

## 📝 Descrição dos Arquivos

data_preparation.py
- Contém funções para:
  - Limpeza e normalização dos dados.
  - Tratamento de valores ausentes.
  - Geração de novas variáveis para análise.

clustering.py
- Implementa o algoritmo K-means para agrupamento.
- Inclui funções para calcular métricas como inércia e silhouette.
- Aplica técnicas como PCA para redução de dimensionalidade.

visualization.py
- Gera gráficos para interpretação dos resultados:
  - Diagramas de dispersão.
  - Heatmaps.
  - Gráficos de barras e radar.

utils.py
- Funções auxiliares que suportam o projeto, como:
- Leitura e escrita de arquivos.
- Configuração de parâmetros.
- Logs para depuração.

---

## 📋 Notas Importantes

- Reutilização: Estruture os módulos de forma que sejam reutilizáveis em outros projetos.
- Documentação: Certifique-se de que todas as funções possuem docstrings explicativas.
- Testes: Scripts no diretório tests/ devem validar o funcionamento correto dos módulos.
