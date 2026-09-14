---
title: ML - NayarIA Previsão de Custos de Carro
tipo: projeto
area: inteligencia artificial & machine learning
tecnologias: [Python, Scikit-Learn, Pandas, Machine Learning]
status: em desenvolvimento / pessoal
tags: [projeto, python, machine-learning, scikit-learn, regressao, automotivo, eda, etl]
data_criacao: 2026-09-13
repositorio_externo: "https://github.com/Arthuro08/NayarIA---Previsao-de-Custos-de-Carro"
---

# 🤖 ML - NayarIA: Previsão de Custos e Precificação de Carros

## 📌 Visão Geral
O **NayarIA** é um projeto pessoal de Machine Learning e Inteligência Artificial desenvolvido em [[Python]] com a biblioteca [[Scikit-Learn]]. O objetivo do sistema é criar modelos preditivos supervisionados capazes de estimar o valor de venda e precificação de veículos a partir de atributos históricos e técnicos (como montadora, modelo, ano de fabricação e quilometragem rodada).

O projeto é uma evolução direta dos dados modelados originalmente no projeto [[Database - Concessionaria]], criando uma conexão real entre Engenharia de Dados (SQL Server / ETL) e Aprendizado de Máquina.

---

## 🛠️ Pipeline de Machine Learning & Engenharia de Dados
O script `nayaria.py` estrutura o fluxo clássico de Ciência de Dados:

1. **Ingestão de Dados:** Carga da base de veículos via `pandas.read_csv('concessionaria.csv')`.
2. **ETL & Tratamento Categórico (One-Hot Encoding):**
   - Conversão de variáveis categóricas textuais (`Nome` do modelo e `Marca`) em representação numérica binária utilizando `pd.get_dummies()`:
     ```python
     dataset_traduzido = pd.get_dummies(dataset, columns=['Nome', 'Marca'], dtype=int)
     ```
3. **Separação de Features e Target:**
   - Variáveis preditoras (`X` / *pistas*): remoção do alvo (`Valor_Venda`) e de datas.
   - Variável alvo (`y` / *resultado*): `Valor_Venda`.
4. **Particionamento de Dados (Holdout):**
   - Divisão em conjuntos de treino e teste via `train_test_split(test_size=0.2)`.
5. **Modelagem Preditiva:**
   - Aplicação de algoritmos de Regressão Linear e Árvores de Decisão (`DecisionTreeRegressor` / `LinearRegression`).

---

## 🔗 Links e Notas Relacionadas
- **Repositório Oficial no GitHub:** [Arthuro08/NayarIA---Previsao-de-Custos-de-Carro](https://github.com/Arthuro08/NayarIA---Previsao-de-Custos-de-Carro)
- **Base Relacional de Origem:** [[Database - Concessionaria]]
- **Tecnologias:** [[Python]], [[Pandas]], [[Scikit-Learn]]
- **Conceitos:** [[Analise Exploratoria de Dados (EDA)]]

