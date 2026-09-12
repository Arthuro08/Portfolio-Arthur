---
title: Microsoft SQL Server
tipo: tecnologia
categoria: banco de dados relacional
linguagem_padrao: T-SQL
tags: [tecnologia, sgbd, sql-server, tsql, relacional]
data_criacao: 2026-09-11
---

# 🗄️ Microsoft SQL Server

## 📌 Visão Geral
O **Microsoft SQL Server** é um dos principais Sistemas de Gerenciamento de Bancos de Dados Relacionais (SGBDR) do mercado corporativo. Utiliza a linguagem **T-SQL (Transact-SQL)**, uma extensão do padrão ANSI SQL que adiciona recursos de controle de fluxo, variáveis, declaração de procedimentos (`STORED PROCEDURES`), gatilhos (`TRIGGERS`) e funções definidas pelo usuário (`UDF`).

---

## 🚀 Principais Recursos Utilizados no Portfólio
- **DDL & Schemas:** Tipagem de dados com precisão decimal (`DECIMAL(10,2)`), strings (`VARCHAR`, `CHAR`), datas (`DATE`) e auto-incremento via `IDENTITY(1,1)`.
- **Integridade:** Restrições `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE` e `CHECK`.
- **Cláusula `OUTPUT INSERTED`:** Resgate atômico e determinístico de chaves recém-geradas em inserções transacionais.
- **Views e Stored Procedures:** Encapsulamento de lógicas analíticas complexas e regras de negócio.
- **Separação de Lotes (`GO`):** Delimitação de batches de compilação essenciais para comandos DDL.

---

## 📂 Projetos que Utilizam SQL Server
- [[Database - Concessionaria]]
- [[Database - Ficha Medica]]
- [[Database - Futebol BR]]
- [[Database - Authentication]]

---

## 🔗 Conceitos e Guias Relacionados
- [[DDL vs DML vs DQL]]
- [[Stored Procedures e Functions]]
- [[Integridade Referencial e Constraints]]
- [[Solucao - Erro Msg 208 Objeto Invalido SQL Server]]
- [[Guia - Conexao Python e SQL Server via pyodbc]]

