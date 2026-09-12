---
title: Database - Authentication
tipo: projeto
area: seguranca & banco de dados
tecnologias: [Python, Microsoft SQL Server, pyodbc]
status: concluído
tags: [projeto, python, sql, autenticacao, seguranca, cli, logs, auditoria]
data_criacao: 2026-09-11
repositorio: "sistemas_com_sql/database authentication"
---

# 🔐 Database - Sistema de Autenticação & Auditoria

## 📌 Visão Geral
Aplicação de autenticação, login e gestão de acessos desenvolvida em [[Python]] com integração nativa ao [[Microsoft SQL Server]]. O sistema opera através de uma interface interativa de terminal (CLI), permitindo o cadastro de usuários com rigorosas validações de senha, autenticação segura e um módulo administrativo restrito protegido por credencial mestre.

Adicionalmente, cada evento de cadastro gera um registro de auditoria com carimbo temporal no arquivo de log local (`logs/logs.txt`).

---

## 🚀 Principais Módulos
- **Cadastro de Usuários (`cadastrar()`):**
  - Validação de tamanho de nome de usuário (máximo 20 caracteres).
  - Consulta ao banco para impedir usernames duplicados.
  - Validação de tamanho de senha (entre 8 e 20 caracteres) e confirmação obrigatória de senha digitada.
- **Login e Autenticação (`login()`):**
  - Validação direta das credenciais contra os registros da tabela `Usuario`.
- **Painel Administrativo (`adm()`):**
  - Acesso restrito via senha mestre (`ADMSENHA = '08032007'`).
  - Listagem completa dos usuários cadastrados (`admlistar()`).
  - Remoção de usuários por identificador único (`admremover()`).
- **Auditoria de Eventos:**
  - Gravação automática de logs com data e hora: `[08/09/2026 21:40:12] Cadastro de Usuario: Arthur`.

---

## 🗄️ Estrutura do Banco de Dados
```sql
CREATE DATABASE Users_Sistema
GO
USE Users_Sistema

CREATE TABLE Usuario(
    ID_Usuario int PRIMARY KEY IDENTITY(1,1) NOT NULL,
    Username varchar(20) NOT NULL,
    Senha VARCHAR(20) NOT NULL
);
```

---

## 🛡️ Aspectos de Segurança & Arquitetura
- **Prevenção a SQL Injection:** Utilização de queries parametrizadas (`cursor.execute(sql, (param1, param2))`), delegando ao driver `pyodbc` o escape seguro de caracteres.
- **Persistência em Arquivo:** Uso do modo de abertura `'a'` (*append*) garantindo que os novos logs não sobrescrevam o histórico anterior.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Python]], [[Microsoft SQL Server]]
- **Conceitos:** [[DDL vs DML vs DQL]], [[Integridade Referencial e Constraints]]
- **Guias Técnicos:** [[Guia - Conexao Python e SQL Server via pyodbc]]
- **Evolução:** [[Roadmap & Backlog]]

