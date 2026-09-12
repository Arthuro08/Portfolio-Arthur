---
title: Database - Concessionária
tipo: projeto
area: banco de dados
tecnologias: [Microsoft SQL Server, T-SQL, Power BI]
status: concluído
tags: [projeto, sql, tsql, modelagem, procedures, functions, power-bi, analytics]
data_criacao: 2026-09-11
repositorio: "sistemas_com_sql/database concessionaria"
---

# 🚗 Database - Concessionária de Veículos

## 📌 Visão Geral
Projeto completo de engenharia de dados automotivos, abrangendo desde a modelagem relacional de entidades (marcas, modelos, veículos em estoque e histórico de vendas) até a implementação em [[Microsoft SQL Server]] (T-SQL) e a construção de um painel interativo de Business Intelligence no [[Power BI]].

O sistema foi desenhado para controlar o ciclo de vida comercial da concessionária, prevenindo vendas duplicadas e fornecendo rotinas automatizadas para cálculo de métricas e suporte a tomadas de decisão executiva.

---

## 🏗️ Modelagem Relacional & Arquitetura
A estrutura segue estritamente a normalização relacional com relacionamentos em cascata:

```text
[[Marca]] (1) ──< (N) [[Modelo]] (1) ──< (N) [[Carro]] (1) ──< (1) [[Venda]]
```

### Entidades e Dicionário de Dados
- **`Marca`:** Identificador (`ID_Marca`), nome da fabricante (`Nome` UNIQUE) e país de origem (`Pais`).
- **`Modelo`:** Identificador (`ID_Modelo`), nome comercial (`Nome` UNIQUE), categoria (`Categoria`: SUV, Sedan, Hatch) e chave estrangeira para Marca.
- **`Carro`:** Identificador (`ID_Carro`), `Placa` (char 7 UNIQUE), `Ano`, `Cor`, `Valor` (decimal) e `Quilometragem`.
- **`Venda`:** Identificador (`ID_Venda`), `Data_Venda`, `Valor_Venda` e `FK_ID_Carro` com restrição `UNIQUE` (cada carro só pode ser vendido uma única vez).

---

## ⚙️ Regras de Negócio & [[Integridade Referencial e Constraints]]
- **Restrições de Verificação (`CHECK`):**
  - `CHCK_Carro_Valor`: `Valor >= 0`
  - `CHCK_Carro_Quilometragem`: `Quilometragem >= 0`
  - `CHCK_Venda_Valor_Venda`: `Valor_Venda >= 0`
- **Restrições de Unicidade (`UNIQUE`):**
  - Nomes de marcas e modelos únicos.
  - Placas automotivas únicas.
  - Vínculo 1:1 na venda através de `UQ_Venda_FK_ID_Carro`.

---

## 🛠️ Objetos de Banco & Rotinas Programáveis ([[Stored Procedures e Functions]])
- **View `Consolidado_Tabela`:** Reúne em uma única estrutura desnormalizada os dados de vendas, valor comercializado, ano, quilometragem, modelo e marca.
- **Stored Procedure `sp_num_vendas`:** Consolida e agrupa a quantidade de vendas efetuadas por fabricante.
- **Stored Procedure `sp_media_preco`:** Recebe `@marca` e `@modelo` como parâmetros e calcula o ticket médio histórico das vendas, validando previamente se o modelo existe na base.
- **User-Defined Function `set_desconto_geral`:** Função escalar que calcula o valor líquido subtraindo o desconto aplicado:
  ```sql
  CREATE OR ALTER FUNCTION set_desconto_geral(@valor decimal(10,2), @desconto decimal(10,2))
  RETURNS DECIMAL(10,2)
  BEGIN
      RETURN @valor - @desconto
  END
  ```

---

## 📊 Dashboard em [[Power BI]]
- Faturamento mensal e receita total acumulada.
- Ticket médio por veículo vendido.
- Distribuição de vendas por categoria (SUV, Sedan e Hatch) e por montadora.
- Análise de portfólio remanescente em estoque.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Microsoft SQL Server]], [[Power BI]]
- **Conceitos:** [[DDL vs DML vs DQL]], [[Integridade Referencial e Constraints]], [[Stored Procedures e Functions]]
- **Evolução:** [[Roadmap & Backlog]]
- **Casos de Suporte:** [[Solucao - Erro Msg 208 Objeto Invalido SQL Server]]

