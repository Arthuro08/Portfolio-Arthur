---
title: Python - Análise com Pandas
tipo: projeto
area: ciencia de dados & analytics
tecnologias: [Python, Pandas, openpyxl]
status: concluído
tags: [projeto, python, pandas, eda, analise-de-dados, excel]
data_criacao: 2026-09-11
repositorio: "solucoes_em_python/pandas"
---

# 🐼 Python - Análise Exploratória com Pandas

## 📌 Visão Geral
Projeto prático demonstrando o uso de [[Python]] e da biblioteca [[Pandas]] para ingestão, auditoria estrutural e análise exploratória de dados tabulares (EDA) provenientes de arquivos de planilhas eletrônicas (`planilha.xlsx`).

---

## 🚀 Pipeline de Análise Desenvolvido
O script `analise.py` executa os três pilares essenciais da inspeção exploratória:

```python
import pandas as pd

# 1. Leitura e parsing do arquivo Excel
df = pd.read_excel("solucoes_em_python/pandas/planilha.xlsx")

# 2. Inspeção das primeiras linhas do DataFrame
print("\n", df.head())

# 3. Diagnóstico de tipos de dados, memória e valores nulos
print("\n\n", df.info())

# 4. Estatística descritiva (média, desvio padrão, min, quartis, max)
print("\n", df.describe())
```

---

## 🧠 Métricas Estatísticas Avaliadas
- **Contagem (`count`):** Quantidade de registros não-nulos em cada variável.
- **Tendência Central (`mean`, `50%` - mediana):** Identificação do ponto médio dos dados.
- **Dispersão (`std`):** Variabilidade e desvio padrão das medições.
- **Valores Extremos (`min`, `max`):** Detecção rápida de limites e potenciais outliers.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Python]], [[Pandas]]
- **Conceitos:** [[Analise Exploratoria de Dados (EDA)]]
- **Evolução:** [[Roadmap & Backlog]]

