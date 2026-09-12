---
title: Integridade Referencial e Constraints
tipo: conceito
area: modelagem e banco de dados
tags: [conceito, sql, integridade, constraints, fk, pk, unique, check]
data_criacao: 2026-09-11
---

# 🛡️ Integridade Referencial & Constraints em SQL

As restrições de integridade (*Constraints*) garantem a precisão, confiabilidade e consistência dos dados armazenados em um banco de dados relacional.

---

## 📋 Categorias de Restrições

1. **`PRIMARY KEY` (Chave Primária):**
   - Identifica exclusivamente cada registro da tabela.
   - Não aceita valores nulos (`NOT NULL`) e impõe unicidade implícita.

2. **`FOREIGN KEY` (Chave Estrangeira):**
   - Estabelece uma relação de dependência entre duas tabelas.
   - Impede a inserção de registros "órfãos" e protege contra exclusões acidentais que quebrariam a integridade dos dados filhos.

3. **`UNIQUE` (Unicidade):**
   - Garante que todos os valores em uma coluna (ou tupla de colunas) sejam distintos.
   - Diferente da PK, permite valores nulos (uma única ocorrência de `NULL` no SQL Server).
   - Exemplo prático em [[Database - Concessionaria]]: aplicada na `FK_ID_Carro` da tabela `Venda` para garantir que um veículo só seja vendido uma única vez.

4. **`CHECK` (Validação de Domínio):**
   - Impõe uma condição lógica booleana sobre os dados aceitos na coluna.
   - Exemplo em [[Database - Concessionaria]]: `CHECK (Valor >= 0)` e `CHECK (Quilometragem >= 0)`.

5. **`NOT NULL`:**
   - Obriga o preenchimento da coluna em qualquer instrução de `INSERT`.

---

## 🔗 Projetos Aplicados
- [[Database - Concessionaria]]
- [[Database - Ficha Medica]]
- [[Database - Futebol BR]]

