# 🐼 Análise Exploratória de Dados com Pandas em Python

## 📌 Sobre o Projeto
Este projeto demonstra os primeiros passos em Ciência e Análise de Dados utilizando a linguagem Python e a consagrada biblioteca Pandas. O script realiza a carga e a leitura de uma planilha em formato Excel (`.xlsx`), executando técnicas fundamentais de análise exploratória (EDA) para inspecionar as primeiras linhas do conjunto de dados, verificar os tipos primitivos e valores ausentes de cada coluna e gerar um resumo estatístico descritivo das variáveis quantitativas.

## 🚀 Funcionalidades
- **Carga de Dados Tabulares:** Leitura automatizada de planilhas eletrônicas estruturadas (`.xlsx`) transformando-as em um `DataFrame`.
- **Inspeção Amostral (`head`):** Visualização das primeiras linhas para compreensão da disposição dos atributos e registros.
- **Auditoria de Estrutura e Tipos (`info`):** Exibição do esquema da tabela, contagem de registros não-nulos e verificação do consumo de memória e tipos de dados de cada coluna.
- **Estatística Descritiva (`describe`):** Geração de sumário com contagem, média, desvio padrão, valores mínimos, máximos e quartis (25%, 50% - mediana, e 75%).

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** Python 3
- **Bibliotecas Utilizadas:**
  - `pandas`: Manipulação, tratamento e análise estruturada de dados tabulares em memória.
  - `openpyxl`: Engine de leitura e integração para arquivos no formato `.xlsx`.

## 🧠 Conceitos Aplicados
- **Análise Exploratória de Dados (EDA):** Técnicas iniciais para entender o comportamento das distribuições e a qualidade das informações contidas na fonte de dados.
- **Estruturas de Dados Bidimensionais (DataFrames):** Operação sobre abstrações de tabelas com índices de linhas e colunas nomeadas.
- **Estatística Descritiva:** Extração de medidas de tendência central e de dispersão para suporte a tomadas de decisão.

## 📂 Estrutura do Projeto
```text
pandas/
│
├── analise.py      # Script Python contendo os comandos de carga e análise exploratória
└── planilha.xlsx   # Arquivo de dados em formato de planilha Excel
```

## ▶️ Como Executar

### 1. Pré-requisitos
- Python 3.8+ instalado.
- Instalação do Pandas e do leitor de arquivos Excel:
  ```bash
  pip install pandas openpyxl
  ```

### 2. Execução
No terminal, execute o script a partir da raiz do repositório ou ajuste o caminho do arquivo `planilha.xlsx`:
```bash
python solucoes_em_python/pandas/analise.py
```
*(Ou entre na pasta `solucoes_em_python/pandas/` e ajuste o caminho da planilha para `./planilha.xlsx`)*

