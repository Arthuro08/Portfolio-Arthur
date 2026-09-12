---
title: C - Calculadora Científica
tipo: projeto
area: algoritmos & baixo nivel
tecnologias: [Linguagem C, GCC, math.h]
status: concluído
tags: [projeto, c, matematica, funcoes, terminal, cli]
data_criacao: 2026-09-11
repositorio: "solucoes_em_c/calculadora"
---

# 🧮 C - Calculadora Científica

## 📌 Visão Geral
Utilitário de linha de comando desenvolvido em [[Linguagem C]] com suporte a operações aritméticas fundamentais, exponenciação e radiciação. A aplicação mantém execução contínua através de um laço `do-while` e implementa programação defensiva contra erros matemáticos clássicos (como divisão por zero e cálculo de raiz quadrada de número negativo).

---

## 🚀 Operações Suportadas
- **Adição (`+`):** $x_1 + x_2$
- **Subtração (`-`):** $x_1 - x_2$
- **Multiplicação (`*`):** $x_1 \times x_2$
- **Divisão (`/`):** $x_1 \div x_2$ (com validação prévia de $x_2 \neq 0$)
- **Exponenciação (`e`):** $x_1^{x_2}$ via função `pow()` da biblioteca `<math.h>`
- **Radiciação (`r`):** $\sqrt{x_1}$ via função `sqrt()` da biblioteca `<math.h>` (com validação $x_1 \ge 0$)

---

## 🧠 Arquitetura e Decisões de Código
- **Modularização de Funções:** As operações foram isoladas na função pura `calc()` com retorno de tipo `double`:
  ```c
  double calc(double x1, char operador, double x2){
      switch(operador){
          case '+': return x1 + x2;
          case '-': return x1 - x2;
          case '*': return x1 * x2;
          case '/': return x1 / x2;
          case 'e': return pow(x1, x2);
          case 'r': return sqrt(x1);
          default: return 0;
      }
  }
  ```
- **Controle de Continuidade:** O usuário pode encadear sucessivos cálculos respondendo à solicitação de continuidade (`S`/`N`).

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Linguagem C]]
- **Evolução:** [[Roadmap & Backlog]]

