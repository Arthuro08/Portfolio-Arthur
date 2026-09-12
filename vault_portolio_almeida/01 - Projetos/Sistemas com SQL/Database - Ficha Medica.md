---
title: Database - Ficha Médica
tipo: projeto
area: full stack & banco de dados
tecnologias: [Python, Flask, Microsoft SQL Server, pyodbc, HTML5]
status: concluído
tags: [projeto, python, flask, sql, tsql, web, saude, transacoes]
data_criacao: 2026-09-11
repositorio: "sistemas_com_sql/database ficha medica"
---

# 🏥 Database - Ficha Médica Hospitalar

## 📌 Visão Geral
Sistema integrado de gestão de prontuários médicos ambulatoriais e hospitalares. O projeto une a modelagem relacional completa do histórico clínico de pacientes à implementação de uma aplicação web com o microframework [[Flask]] em [[Python]], permitindo o preenchimento de cadastros através de formulários no navegador com persistência atômica no [[Microsoft SQL Server]].

O projeto conta com documentação completa em PDF com memorial descritivo desde a fase conceitual até a homologação.

---

## 🏗️ Modelagem e Estrutura Relacional
A modelagem organiza os registros clínicos em 5 tabelas correlacionadas por chaves estrangeiras:

- **`Paciente`:** `num_paciente` (PK Identity), `nome_paciente`, `data_nasc`, `sexo`, `convenio`, `est_civil`, `RG` (UNIQUE).
- **`Endereco`:** `cod_endereco` (PK Identity), `endereco`, `fk_paciente` (FK).
- **`Telefone`:** `cod_telefone` (PK Identity), `telefone`, `fk_paciente` (FK).
- **`Consulta`:** `num_consulta` (PK Identity), `data_consulta`, `medico`, `diagnostico`, `fk_paciente` (FK).
- **`Exame`:** `num_exame` (PK Identity), `nome`, `data_exame`, `fk_consulta` (FK).

---

## 💡 Destaque Técnico: Cláusula `OUTPUT INSERTED`
Um dos pontos arquiteturais mais elegantes deste projeto foi o uso da cláusula T-SQL `OUTPUT INSERTED` no momento da inserção pelo [[Flask]]. 

Ao inserir o paciente, o sistema recupera imediatamente a chave primária recém-criada sem necessidade de executar queries secundárias de consulta ou depender de variáveis de escopo como `SCOPE_IDENTITY()`:

```python
cursor.execute(
    "INSERT INTO Paciente(nome_paciente, data_nasc, sexo, convenio, est_civil, RG) "
    "OUTPUT INSERTED.num_paciente VALUES (?, ?, ?, ?, ?, ?)",
    (nome_paciente, data_nasc, sexo, convenio, estado_civil, rg)
)
num_paciente = cursor.fetchone()[0]

# O ID recuperado é utilizado diretamente nas tabelas dependentes:
cursor.execute("INSERT INTO Endereco(endereco, fk_paciente) VALUES(?, ?)", (endereco, num_paciente))
cursor.execute("INSERT INTO Telefone(telefone, fk_paciente) VALUES(?, ?)", (telefone, num_paciente))
```

---

## ⚙️ Regras de Integridade e Validações
- **Unicidade de Pacientes:** O sistema verifica previamente se o RG já está cadastrado no banco antes de iniciar o fluxo transacional.
- **Atomicidade Transacional:** Todos os registros vinculados (endereço, telefone, consulta e exames) são confirmados em conjunto através de `config.commit()`.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Python]], [[Flask]], [[Microsoft SQL Server]]
- **Conceitos:** [[Integridade Referencial e Constraints]], [[DDL vs DML vs DQL]], [[Consumo de APIs REST e Assincronismo]]
- **Guias Técnicos:** [[Guia - Conexao Python e SQL Server via pyodbc]]
- **Evolução:** [[Roadmap & Backlog]]

