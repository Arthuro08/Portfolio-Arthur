---
title: Database - Futebol Brasileiro
tipo: projeto
area: banco de dados
tecnologias: [Microsoft SQL Server, T-SQL, Power BI]
status: concluído
tags: [projeto, sql, tsql, analytics, futebol, joins, procedures, power-bi]
data_criacao: 2026-09-11
repositorio: "sistemas_com_sql/database futebol"
---

# ⚽ Database - Futebol Brasileiro Analytics

## 📌 Visão Geral
Projeto prático desenvolvido para explorar o ecossistema relacional do [[Microsoft SQL Server]] e a construção de relatórios analíticos no [[Power BI]]. A modelagem estrutura dados de Federações Estaduais, Clubes e Jogadores, funcionando como um laboratório completo de T-SQL para operações de álgebra relacional, funções escalares/matemáticas, manipulação de strings e desenvolvimento de Stored Procedures parametrizadas.

---

## 🏗️ Modelagem Relacional
A arquitetura relaciona entidades em uma hierarquia de duas etapas:

```text
[[Federacao]] (1) ──< (N) [[Clube]] (1) ──< (N) [[Jogador]]
```

- **`Federacao`:** `ID_Federacao` (PK), `Nome`, `Sigla`, `Estado`.
- **`Clube`:** `ID_Clube` (PK), `Nome`, `Cidade`, `FK_ID_Federacao` (FK).
- **`Jogador`:** `ID_Jogador` (PK), `Nome`, `Posicao`, `DataNascimento`, `FK_ID_Clube` (FK).

---

## 🔍 Laboratório de Consultas e Álgebra Relacional
O projeto serviu de campo de provas para os comportamentos práticos de junções em SQL:

- **Diferenças entre `INNER JOIN`, `LEFT JOIN` e `RIGHT JOIN`:**
  - Foi cadastrado o clube *Santos* sem jogadores vinculados para testar o comportamento do `LEFT JOIN`. No resultado, o Santos é exibido normalmente, e as colunas de dados do jogador retornam com valores `NULL`.
- **Agrupamentos com `GROUP BY` e `HAVING`:**
  - Agrupamento de atletas por posição com cláusula de corte (`HAVING COUNT(*) > 5`).
- **Funções Matemáticas e de String Nativas:**
  - `POWER(2, 3)` (exponenciação), `SQRT(49)` (raiz quadrada), `ABS(-13)` (módulo).
  - `LOWER(Sigla)` e `UPPER(Nome)` para padronização tipográfica.

---

## ⚙️ Stored Procedures Implementadas
O script `database_futebolbr.sql` contém quatro variações de procedures:
1. `sp_procedure_simples`: Demonstra declaração de variáveis locais (`DECLARE`), atribuição manual (`SET`) e saída via `PRINT`.
2. `sp_procedure_pk_jogador`: Resgate e mapeamento de campos do banco diretamente em variáveis de escopo.
3. `sp_parametro(@id_jogador int)`: Procedimento com parâmetro de entrada para filtragem dinâmica.
4. `sp_muitos_parametros(@id_jogador int, @clube varchar(255))`: Procedimento com múltiplos parâmetros combinando operadores lógicos e `LEFT JOIN`.

---

## 📊 Dashboard em [[Power BI]]
O arquivo `Dashboard_Federacoes.pbix` oferece visualizações gerenciais com a distribuição geográfica dos clubes, idade dos atletas e volume de jogadores por federação estadual (SP, RJ, MG, RS).

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Microsoft SQL Server]], [[Power BI]]
- **Conceitos:** [[DDL vs DML vs DQL]], [[Stored Procedures e Functions]], [[Integridade Referencial e Constraints]]
- **Evolução:** [[Roadmap & Backlog]]

