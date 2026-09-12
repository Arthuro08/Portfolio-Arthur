---
title: C - Cálculo de Fatorial
tipo: projeto
area: algoritmos & baixo nivel
tecnologias: [Linguagem C, GCC]
status: concluído
tags: [projeto, c, matematica, lacos, sentinela, fatorial]
data_criacao: 2026-09-11
repositorio: "solucoes_em_c/fatorial"
---

# 🔢 C - Cálculo de Fatorial

## 📌 Visão Geral
Algoritmo desenvolvido em [[Linguagem C]] para computar o produto fatorial $n!$ de números inteiros fornecidos via entrada padrão. O programa possui suporte a múltiplas consultas em sequência utilizando um laço contínuo com condição de encerramento baseada em valor sentinela (`-1`).

---

## ⚙️ Lógica do Algoritmo
- **Leitura Contínua e Sentinela:**
  ```c
  while(scanf("%d", &n) && n != -1){
      fat = 1;
      for(x = 2; x <= n; x++){
          fat = fat * x;
      }
      printf("%d\n", fat);
  }
  ```
- **Acumulador Multiplicativo:** A cada número recebido, a variável `fat` é redefinida para `1`, e o laço `for` realiza as multiplicações iterativas até $n$.
- **Parada:** O envio de `-1` quebra imediatamente o laço sem calcular o fatorial desse valor.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Linguagem C]]
- **Evolução:** [[Roadmap & Backlog]]

