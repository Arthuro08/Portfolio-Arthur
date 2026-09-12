---
title: C - Validador de Calendário
tipo: projeto
area: algoritmos & baixo nivel
tecnologias: [Linguagem C, GCC]
status: concluído
tags: [projeto, c, calendario, logica-booleana, datas, validacao]
data_criacao: 2026-09-11
repositorio: "solucoes_em_c/calendario"
---

# 📅 C - Validador e Incrementador de Calendário

## 📌 Visão Geral
Solução em [[Linguagem C]] focada na validação rigorosa de datas do calendário gregoriano e no cálculo determinístico do dia seguinte. O programa recebe três inteiros representando dia (`x`), mês (`y`) e ano (`z`), avalia a consistência temporal das informações e gera como saída a data seguinte formatada (`D.M.A`) ou a mensagem `Invalid`.

---

## 🔍 Regras Lógicas de Validação
- **Limites Universais:** Dia entre 1 e 31, mês entre 1 e 12, ano $\ge 0$.
- **Meses de 30 Dias:** Abril (4), Junho (6), Setembro (9) e Novembro (11) não podem ter dia $> 30$.
- **Fevereiro:** Tratado com teto de 28 dias (`x > 28 && y == 2`).

---

## ⚙️ Algoritmo de Incremento do Dia Seguinte
Quando a data passa nas checagens:
1. Incrementa o dia (`x = x + 1`).
2. Se o dia estourar o limite mensal (ex: dia 32 em qualquer mês ou dia 29 em fevereiro):
   - O dia é resetado para `1`.
   - O mês é incrementado (`y = y + 1`).
3. Se o mês estourar 12 (transição de 31 de dezembro):
   - O mês é resetado para `1`.
   - O ano é incrementado (`z = z + 1`).

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Linguagem C]]
- **Evolução:** [[Roadmap & Backlog]]

