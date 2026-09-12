---
title: Análise Exploratória de Dados (EDA)
tipo: conceito
area: ciencia de dados
tecnologia_principal: Pandas
tags: [conceito, eda, data-science, estatistica, pandas, analise]
data_criacao: 2026-09-11
---

# 📊 Análise Exploratória de Dados (Exploratory Data Analysis - EDA)

A **Análise Exploratória de Dados (EDA)** é a etapa primordial em qualquer projeto de ciência ou análise de dados. Seu objetivo é compreender as distribuições das variáveis, detectar anomalias, auditar valores nulos e formular hipóteses antes de qualquer modelagem preditiva ou tomada de decisão.

---

## 🔍 As Três Dimensões da Inspeção Inicial

### 1. Visualização Estrutural Amostral
- **Comando:** `df.head(n)` ou `df.tail(n)`
- **Objetivo:** Inspecionar nomes de colunas, formatação de dados e conformidade das primeiras e últimas linhas.

### 2. Auditoria Técnica do Dataset
- **Comando:** `df.info()`
- **Objetivo:** Verificar a quantidade total de linhas, contagem de registros preenchidos (`non-null count`), tipo de cada coluna (`int64`, `float64`, `object`, `datetime64`) e pegada de memória RAM consumida pelo DataFrame.

### 3. Síntese Estatística Descritiva
- **Comando:** `df.describe()`
- **Métricas Extraídas:**
  - `count`: Frequência de amostras válidas.
  - `mean`: Média aritmética (tendência central sensível a extremos).
  - `std`: Desvio padrão (dispersão dos dados em torno da média).
  - `min` e `max`: Amplitude total.
  - `25%`, `50%` (mediana), `75%`: Quartis indicando a dispersão interquartílica.

---

## 🔗 Projetos Relacionados
- [[Python - Analise com Pandas]]
- [[Database - Concessionaria]]

