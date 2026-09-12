---
title: DDL vs DML vs DQL
tipo: conceito
area: banco de dados relacional
tags: [conceito, sql, ddl, dml, dql, dcl, tcl, teoria]
data_criacao: 2026-09-11
---

# 📚 Sublinguagens SQL: DDL, DML, DQL, DCL e TCL

A linguagem SQL é categorizada em grupos de instruções de acordo com o seu impacto sobre o banco de dados.

---

## 🧱 1. DDL (Data Definition Language)
- **Foco:** Estrutura e esquema dos objetos do banco (esqueleto).
- **Comandos:**
  - `CREATE`: Cria tabelas, databases, views, procedures.
  - `ALTER`: Modifica a estrutura de um objeto (adiciona/remove colunas, constraints).
  - `DROP`: Destrói o objeto por completo.
  - `TRUNCATE TABLE`: Esvazia a tabela desalocando suas páginas de memória (reseta o `IDENTITY`).

---

## 📝 2. DML (Data Manipulation Language)
- **Foco:** Manipulação direta dos registros e linhas armazenadas dentro das tabelas.
- **Comandos:**
  - `INSERT`: Adiciona novas linhas.
  - `UPDATE`: Altera linhas existentes com base em condições.
  - `DELETE`: Exclui linhas específicas com suporte à cláusula `WHERE`.

---

## 🔍 3. DQL (Data Query Language)
- **Foco:** Extração e projeção de dados somente para leitura.
- **Comando:**
  - `SELECT`: Projeta colunas, realiza junções (`JOIN`) e agregações sem modificar os registros.

---

## 🔑 4. DCL (Data Control Language)
- **Foco:** Controle de segurança, usuários e permissões.
- **Comandos:**
  - `GRANT`: Concede permissões de acesso.
  - `REVOKE`: Revoga permissões previamente concedidas.
  - `DENY`: Bloqueia explicitamente um acesso.

---

## 🔄 5. TCL (Transaction Control Language)
- **Foco:** Gerenciamento de transações atômicas (Propriedades ACID).
- **Comandos:**
  - `BEGIN TRAN`: Inicia uma transação.
  - `COMMIT`: Efetiva permanentemente as operações no disco.
  - `ROLLBACK`: Desfaz todas as alterações em caso de falha.

---

## 🥊 Tabela Comparativa: DELETE vs TRUNCATE

| Propriedade | `DELETE` | `TRUNCATE TABLE` |
| :--- | :--- | :--- |
| **Sublinguagem** | DML | DDL |
| **Cláusula WHERE** | Aceita | Não aceita (sempre apaga tudo) |
| **Contador IDENTITY** | Mantém a sequência atual | Reseta para a semente inicial (seed) |
| **Velocidade** | Mais lento (grava linha por linha) | Instantâneo (desaloca páginas de disco) |
| **Triggers** | Dispara triggers de DELETE | Não dispara triggers |
| **Chaves Estrangeiras** | Permite se não houver registros filhos | Falha se a tabela for referenciada por FK |

---

## 🔗 Projetos Relacionados
- [[Database - Concessionaria]]
- [[Database - Futebol BR]]
- [[Database - Ficha Medica]]
- [[Database - Authentication]]

