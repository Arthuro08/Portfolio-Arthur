---
title: Estruturas e Ponteiros em C
tipo: conceito
area: baixo nivel & memoria
tecnologia_principal: Linguagem C
tags: [conceito, c, struct, ponteiros, memoria, referencia]
data_criacao: 2026-09-11
---

# 🧠 Estruturas de Dados e Ponteiros em C

O domínio de `struct` e ponteiros é essencial para construir sistemas organizados e com eficiência de memória em [[Linguagem C]].

---

## 🏗️ 1. Estruturas Heterogêneas (`struct`)
Permitem agregar tipos primitivos variados (números inteiros, reais, strings) sob um mesmo tipo de dado customizado.

```c
typedef struct {
    char nome[50];
    int matricula;
    double nota1, nota2, media;
} registro_aluno;
```

---

## 📍 2. Ponteiros e Passagem por Referência
Por padrão, a passagem de parâmetros em C ocorre **por valor** (uma cópia é entregue à função). Ao passar o endereço de memória de uma variável usando o operador `&`, a função recebe um **ponteiro** (`*`) e pode alterar o valor original.

### Exemplo em [[C - Sistema Cadastro de Alunos]]:
```c
void cadastrar(registro_aluno aluno[], int *qtd) {
    // aluno[] já é um ponteiro implícito para o primeiro elemento
    // *qtd acessa diretamente o valor do contador na main()
    aluno[*qtd].matricula = 1234;
    (*qtd)++; // Incrementa a variável original
}
```

---

## 🛡️ Boas Práticas de Manipulação de Strings
- Evitar `gets()` devido ao risco crítico de *buffer overflow*.
- Usar `scanf(" %49[^\n]", variavel)` para ler strings contendo espaços delimitando com segurança o número máximo de bytes.

