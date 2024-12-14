# 📂 Diretório `data/`

Este diretório contém os dados utilizados no projeto, organizados de forma a facilitar o fluxo de trabalho entre dados brutos e processados.

---

## 🗂️ Estrutura

A estrutura da pasta `data/` está dividida em:

```plaintext
data/
├── raw/                 # Dados brutos, originais, sem alterações
├── processed/           # Dados tratados, limpos e prontos para análise
```
---

#📁 raw/

- Esta subpasta armazena os arquivos de dados originais.
- Nenhuma modificação deve ser feita nos arquivos dessa pasta.
- Exemplos de arquivos armazenados:
  - dados_campeonato_brasileiro.csv

---

## 📁 processed/

- Contém os dados que passaram por etapas de limpeza e transformação.
- Esses dados estão prontos para serem usados nos notebooks e scripts.
- Exemplos de arquivos armazenados:
  - dados_limpos.csv
 
---

## 📜 Regras de Uso

1. Dados Brutos (raw/):
- Não modifique ou remova os arquivos diretamente.
- Se novos dados forem adicionados, documente o processo.
2. Dados Processados (processed/):
- Apenas scripts no diretório src/ devem gerar ou modificar os arquivos desta subpasta.
- Mantenha a consistência nos formatos de arquivo.
