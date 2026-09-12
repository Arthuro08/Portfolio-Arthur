---
title: Solução - Erro Msg 208 Objeto Inválido SQL Server
tipo: troubleshooting
area: banco de dados relacional
tags: [troubleshooting, sql-server, tsql, erro-208, go, batches]
data_criacao: 2026-09-11
---

# 🛠️ Resolução de Erro: Msg 208 - Nome de objeto inválido no SQL Server

## 📌 Sintoma do Problema
Ao tentar executar um script contendo comandos DDL (`CREATE OR ALTER FUNCTION`, `CREATE PROCEDURE` ou `CREATE VIEW`) seguido de consultas `SELECT`, o SQL Server Management Studio (SSMS) ou o Azure Data Studio retorna o erro:

```text
Msg 208, Level 16, State 1, Line 10
Nome de objeto 'NomeDaTabela' inválido.
```

Mesmo que a tabela exista e esteja criada dentro do banco de dados do projeto.

---

## 🔍 Causa Raiz
O erro ocorre por dois fatores interligados:

1. **Ausência do comando delimitador de lotes (`GO`):**
   - O comando `USE NomeDoBanco` altera a base de dados ativa da sessão, mas sem um `GO` logo em seguida, o SQL Server tenta compilar o lote todo sob o contexto do banco de dados que estava selecionado no momento da conexão (geralmente o banco de sistema **`master`**).
   - No banco `master`, as tabelas do projeto não existem.
2. **Execução Seletiva de Trechos:**
   - Se o desenvolvedor selecionar apenas as linhas do `SELECT` e apertar F5, o comando `USE` não é enviado para o servidor, fazendo com que a consulta rode no banco padrão ativo na interface do editor.
3. **Regra de Compilação de DDL:**
   - Instruções como `CREATE FUNCTION` e `CREATE PROCEDURE` exigem ser a **primeira instrução de um lote (*batch*)**. Sem o `GO` antes e depois de sua declaração, ocorre erro de compilação.

---

## ✅ Solução Definitiva
Inserir os delimitadores `GO` separando explicitamente cada bloco de execução:

```sql
USE Concessionaria
GO -- 1. Separa a troca de contexto de banco

CREATE OR ALTER FUNCTION set_desconto_geral(@valor decimal(10,2), @desconto decimal(10,2))
RETURNS DECIMAL(10,2)
BEGIN
    RETURN @valor - @desconto
END
GO -- 2. Encerra a compilação da função

-- 3. Agora a consulta roda em seu próprio lote no banco correto:
SELECT mar.Nome, mod.Nome, dbo.set_desconto_geral(car.Valor, 15000.00) 
FROM Marca mar
JOIN Modelo mod ON mod.FK_ID_Marca = mar.ID_Marca
JOIN Carro car ON car.FK_ID_Modelo = mod.ID_Modelo;
```

---

## 🔗 Projetos Relacionados
- [[Database - Concessionaria]]
- [[Microsoft SQL Server]]

