---
title: Stored Procedures e Functions
tipo: conceito
area: banco de dados relacional
tecnologia_principal: Microsoft SQL Server
tags: [conceito, sql, procedures, functions, tsql, modularizacao]
data_criacao: 2026-09-11
---

# ⚙️ Stored Procedures vs User-Defined Functions (UDF)

Em T-SQL no [[Microsoft SQL Server]], tanto Procedures quanto Functions permitem encapsular blocos de código reaproveitáveis no servidor, mas possuem papéis e restrições técnicas distintas.

---

## 🥊 Principais Diferenças

| Característica | User-Defined Function (UDF) | Stored Procedure |
| :--- | :--- | :--- |
| **Retorno Obrigatório** | Sim, retorna um valor escalar ou tabela | Não obrigatório (pode retornar 0 ou mais) |
| **Uso dentro de `SELECT`** | **Sim!** Pode ser chamada em `SELECT`, `WHERE`, `JOIN` | **Não.** Deve ser chamada isoladamente com `EXEC` |
| **Comandos de Modificação (DML)** | Não pode alterar o estado do banco (`INSERT`/`UPDATE` proibidos) | Pode executar livremente comandos DDL, DML e transações |
| **Controle Transacional** | Não permite `BEGIN TRAN` ou `COMMIT` | Permite gerenciar transações completas |

---

## 💡 Exemplos no Portfólio

### 1. Function Escalar (em [[Database - Concessionaria]])
```sql
CREATE OR ALTER FUNCTION set_desconto_geral(@valor decimal(10,2), @desconto decimal(10,2))
RETURNS DECIMAL(10,2)
BEGIN
    RETURN @valor - @desconto
END

-- Utilização direta na projeção da consulta:
SELECT Nome, dbo.set_desconto_geral(Valor, 5000.00) FROM Carro;
```

### 2. Stored Procedure com Parâmetros (em [[Database - Futebol BR]])
```sql
CREATE OR ALTER PROCEDURE sp_muitos_parametros(@id_jogador int, @clube varchar(255)) AS
BEGIN
    SELECT * from Jogador j 
    LEFT JOIN Clube c on j.FK_ID_Clube = ID_Clube 
    WHERE j.ID_Jogador <= @id_jogador AND c.Nome = @clube
END
GO

EXEC sp_muitos_parametros 10, 'Palmeiras';
```

