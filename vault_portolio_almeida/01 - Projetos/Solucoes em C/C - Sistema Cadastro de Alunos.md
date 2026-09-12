---
title: C - Sistema Cadastro de Alunos
tipo: projeto
area: algoritmos & baixo nivel
tecnologias: [Linguagem C, GCC]
status: concluído
tags: [projeto, c, struct, ponteiros, arrays, terminal, academico]
data_criacao: 2026-09-11
repositorio: "solucoes_em_c/sistema cadastro de alunos"
---

# 📚 C - Sistema de Cadastro de Alunos

## 📌 Visão Geral
Aplicação desenvolvida em [[Linguagem C]] voltada para o gerenciamento acadêmico de turmas de até 100 alunos. O sistema roda diretamente no terminal através de um menu interativo, permitindo cadastrar novos alunos, listar registros com notas parciais e médias, realizar buscas lineares por matrícula e computar estatísticas da turma (média geral, aluno destaque e percentual de aprovação).

---

## 🏗️ Estruturas de Dados e Modelagem em Memória
O projeto define a estrutura heterogênea `registro_aluno` utilizando `typedef`:

```c
typedef struct {
    char nome[50];
    int matricula;
    double nota1, nota2, media;
} registro_aluno;
```

---

## ⚙️ Principais Funcionalidades
1. **Cadastro (`cadastrar()`):**
   - Leitura de nome com espaços via máscara `scanf(" %49[^\n]", aluno[*qtd].nome)`.
   - Validação de matrícula existente para impedir duplicidades.
   - Validação de intervalo das notas (0 a 10).
   - Bloqueio automático caso o vetor atinja 100 registros.
2. **Listagem (`listar()`):**
   - Varredura de todos os alunos cadastrados exibindo nome, matrícula e média.
3. **Busca (`buscar()`):**
   - Localização instantânea por matrícula via busca linear.
4. **Média da Turma (`media_turma()`):**
   - Somatório cumulativo das médias dividido pela quantidade total de alunos.
5. **Maior Média (`maior_media()`):**
   - Identificação do aluno com a maior média aritmética da turma.
6. **Percentual de Aprovação (`percentual_aprovacao()`):**
   - Cálculo da proporção de estudantes com média $\ge 6.0$ (definido pela constante `#define APROVACAO 6`).

---

## 💡 Destaques de Engenharia & [[Estruturas e Ponteiros em C]]
- **Passagem de Parâmetro por Referência:** Uso do ponteiro `int *qtd` para manipular diretamente o contador de registros alocados sem depender de variáveis globais.
- **Proteção de Estouro de Buffer:** Uso de limitadores de caracteres na leitura de strings para evitar *buffer overflow*.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Linguagem C]]
- **Conceitos:** [[Estruturas e Ponteiros em C]]
- **Evolução:** [[Roadmap & Backlog]]

