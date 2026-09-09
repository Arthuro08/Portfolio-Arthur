# ⚽ Futebol Brasileiro - Banco de Dados Relacional & Dashboard Analytics

## 📌 Sobre o Projeto
Este projeto explora a modelagem, implementação e análise de dados do futebol brasileiro utilizando o Microsoft SQL Server (T-SQL) e o Microsoft Power BI. A estrutura relaciona federações estaduais, clubes de futebol e jogadores, servindo como um laboratório completo de SQL: desde comandos básicos de DDL e DML até consultas avançadas com junções externas (`LEFT`/`RIGHT JOIN`), funções agregadoras com `HAVING`, manipulação de texto/matemática e automação com Stored Procedures parametrizadas. 

Os dados alimentam um dashboard executivo no Power BI para visualização da distribuição de atletas e clubes por federação.

## 🚀 Funcionalidades
- **Modelagem Relacional Normalizada:** Entidades bem definidas mapeando Federações (1:N) Clubes (1:N) Jogadores.
- **Consultas Analíticas e Filtros Avançados:**
  - Filtragem por padrões de texto (`LIKE`, `%`), intervalos numéricos (`BETWEEN`) e conjuntos (`IN`).
  - Junções relacionais completas: `INNER JOIN`, `LEFT JOIN` (identificando clubes sem jogadores cadastrados) e `RIGHT JOIN`.
  - Estatísticas de elenco: contagem de jogadores por posição com cláusula `HAVING`, identificação do jogador mais jovem (`MAX`) e mais experiente (`MIN`).
- **Manipulação e Formatação de Dados:**
  - Transformações de strings com `LOWER`, `UPPER` e concatenação de colunas.
  - Funções matemáticas nativas: exponenciação (`POWER`), módulo (`ABS`) e raiz quadrada (`SQRT`).
- **Stored Procedures Dinâmicas:**
  - `sp_procedure_simples`: Demonstração de declaração de variáveis locais e fluxo de impressão (`PRINT`).
  - `sp_procedure_pk_jogador`: Resgate e atribuição de dados relacionais diretamente em variáveis de procedure.
  - `sp_parametro`: Filtragem dinâmica de registros via parâmetro numérico.
  - `sp_muitos_parametros`: Consulta combinada filtrando atletas por limite de ID e clube específico.
- **Visualização com Power BI:**
  - Painel interativo com métricas de clubes por federação e volume de atletas por posição e estado.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **SGBD:** Microsoft SQL Server (T-SQL)
- **Ferramenta de Administração:** SQL Server Management Studio (SSMS) / Azure Data Studio
- **Business Intelligence:** Microsoft Power BI Desktop (`.pbix` e relatório `.pdf`)
- **Modelagem Conceitual e Lógica:** Ferramentas de Diagrama Entidade-Relacionamento (DER)

## 🧠 Conceitos Aplicados
- **Modelagem Relacional:** Chaves primárias (`PK`), chaves estrangeiras (`FK`) e integridade referencial.
- **Álgebra Relacional e Junções SQL:** Aplicação prática das diferenças entre `INNER JOIN`, `LEFT JOIN` e `RIGHT JOIN` (incluindo tratamento de valores `NULL`).
- **Agrupamentos e Agregações:** `GROUP BY`, `COUNT(*)`, `HAVING`, `MIN()`, `MAX()`.
- **DML Avançado:** `INSERT`, `UPDATE`, `DELETE` condicional e `TRUNCATE TABLE`.
- **Programação em Banco de Dados (Procedural T-SQL):** Criação e execução de `STORED PROCEDURES`, escopo de variáveis com `DECLARE`/`SET` e passagem de múltiplos parâmetros.

## 📂 Estrutura do Projeto
```text
database futebol/
│
├── database_futebolbr.sql              # Script SQL unificado (DDL, DML, consultas e procedures)
│
├── modelagem/
│   ├── Modelo Conceitual - Futebol.png # Visão conceitual das entidades Federação, Clube e Jogador
│   └── Modelo Lógico - Futebol.png     # Esquema relacional com tipos de dados e chaves
│
└── dashboard/
    ├── Dashboard_Federacoes.pbix       # Painel interativo do Power BI
    └── Dashboard_Federacoes.pdf        # Relatório analítico exportado em PDF
```

## ▶️ Como Executar

### 1. Configuração do Banco de Dados
1. Abra o **SQL Server Management Studio (SSMS)** ou Azure Data Studio.
2. Abra o arquivo `database_futebolbr.sql`.
3. Execute o bloco de criação do banco (`CREATE DATABASE FEDERACAO_BD`) e as tabelas `Federacao`, `Clube` e `Jogador`.
4. Execute os blocos de `INSERT` para popular os dados das federações (SP, RJ, MG, RS), clubes e jogadores.
5. Navegue pelas seções comentadas do script para testar as consultas, operações matemáticas e Stored Procedures.

### 2. Acesso ao Dashboard (Power BI)
1. Certifique-se de possuir o [Power BI Desktop](https://powerbi.microsoft.com/desktop/) instalado.
2. Abra o arquivo `dashboard/Dashboard_Federacoes.pbix`.
3. Para uma consulta rápida sem o Power BI, abra o arquivo `dashboard/Dashboard_Federacoes.pdf`.

