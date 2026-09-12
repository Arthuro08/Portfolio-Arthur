---
title: Guia - Conexão Python e SQL Server via pyodbc
tipo: troubleshooting
area: integracao & backend
tags: [troubleshooting, guia, python, sql-server, pyodbc, odbc]
data_criacao: 2026-09-11
---

# 🔌 Guia Prático: Conectando Python ao Microsoft SQL Server com pyodbc

## 📌 Contexto
Para integrar aplicações [[Python]] (como scripts CLI de autenticação e servidores [[Flask]]) ao [[Microsoft SQL Server]], a biblioteca mais robusta e padrão de mercado é o **`pyodbc`**, que se comunica através dos drivers ODBC do sistema operacional.

---

## 🛠️ Padrão de Connection String Resiliente

```python
import pyodbc

# Configuração com Autenticação do Windows (Trusted Connection)
config = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=NOME_DO_SEU_SERVIDOR;'  # Ex: DESKTOP-MLFI9DN ou localhost\SQLEXPRESS
    'Database=NOME_DO_BANCO;'       # Ex: Users_Sistema ou Ficha_Medica
    'Trusted_Connection=yes;'
)

cursor = config.cursor()
```

---

## 🚨 Principais Pontos de Atenção & Erros Comuns

1. **Esquecer de comitar (`config.commit()`):**
   - O `pyodbc` opera com transações abertas por padrão. Se você rodar um `INSERT`, `UPDATE` ou `DELETE` e não chamar `config.commit()`, os dados **não serão persistidos** no banco!
2. **Consultas Parametrizadas obrigatórias:**
   - Nunca use interpolação de strings (`f"SELECT * FROM Users WHERE nome = '{user}'"`) pois abre brecha para SQL Injection. Use sempre o placeholder `?`:
     ```python
     cursor.execute("SELECT * FROM Usuario WHERE Username = ?", (user,))
     ```
3. **Driver não encontrado:**
   - Se `{SQL Server}` não funcionar em máquinas mais recentes, instale o driver oficial da Microsoft e use: `Driver={ODBC Driver 17 for SQL Server};` ou `Driver={ODBC Driver 18 for SQL Server};TrustServerCertificate=yes;`.

---

## 🔗 Projetos Relacionados
- [[Database - Authentication]]
- [[Database - Ficha Medica]]
- [[Microsoft SQL Server]]
- [[Python]]

