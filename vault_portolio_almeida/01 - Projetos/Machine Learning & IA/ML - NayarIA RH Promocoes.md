---
title: ML - NayarIA RH Promoções
tipo: projeto
area: inteligencia artificial & machine learning
tecnologias: [Python, Scikit-Learn, Pandas, Machine Learning, openpyxl]
status: concluído / pessoal
tags: [projeto, python, machine-learning, scikit-learn, rh, people-analytics, decision-tree, classificacao, eda]
data_criacao: 2026-09-13
repositorio_externo: "https://github.com/Arthuro08/NayarIA---RH"
---

# 👥 ML - NayarIA: Previsão de Promoções de Funcionários (People Analytics)

## 📌 Visão Geral
O **NayarIA - RH** é uma solução de Aprendizado de Máquina supervisionado em [[Python]] focada em People Analytics. O modelo preditivo utiliza Árvores de Decisão para classificar se um colaborador é elegível para promoção com base em métricas de desempenho pré-existentes extraídas de bases de dados do departamento de Recursos Humanos em planilhas Excel (`.xlsx`).

O projeto combina boas práticas de Data Science para evitar vazamento de dados (*data leakage*) e controle de complexidade do modelo para prevenção de *overfitting*.

---

## 🛠️ Pipeline de Machine Learning & Técnicas Aplicadas
- **Ingestão de Dados:** Importação e tratamento de planilhas realistas com [[Pandas]] e `openpyxl`.
- **Separação de Dados (Holdout):** Utilização do `train_test_split` para separar com rigor amostras de treino e de teste, garantindo que o modelo seja avaliado com dados nunca vistos.
- **Controle de Aleatoriedade (`random_state`):** Fixação de semente para assegurar a reprodutibilidade dos experimentos.
- **Modelagem com Árvores de Decisão (`DecisionTreeClassifier`):**
  - Algoritmo supervisionado de classificação interpretável.
  - Controle de hiperparâmetros (como `max_depth`) para evitar sobreajuste (*overfitting*).
- **Avaliação de Performance:** Cálculo e exibição da precisão/acurácia do modelo em tempo de execução.
- **Interface CLI Interativa:** Saídas no terminal com cores indicativas para enriquecer a experiência do usuário.

---

## 🔗 Links e Notas Relacionadas
- **Repositório Oficial no GitHub:** [Arthuro08/NayarIA---RH](https://github.com/Arthuro08/NayarIA---RH)
- **Tecnologias:** [[Python]], [[Scikit-Learn]], [[Pandas]]
- **Conceitos:** [[Analise Exploratoria de Dados (EDA)]]
- **Projeto Irmão:** [[ML - NayarIA Previsao de Custos]]

