---
title: Python - MathMania
tipo: projeto
area: jogos & logica
tecnologias: [Python, datetime]
status: concluído
tags: [projeto, python, jogos, matematica, procedural, logs, terminal]
data_criacao: 2026-09-11
repositorio: "solucoes_em_python/mathmania"
---

# 🧮 Python - MathMania (Desafio Mental)

## 📌 Visão Geral
Jogo de agilidade matemática desenvolvido em [[Python]] no qual o jogador é desafiado a resolver expressões aritméticas geradas dinamicamente. O sistema permite configurar a quantidade de rodadas por partida, pontua os acertos e mantém um histórico persistente de pontuações acompanhadas de carimbo de data e hora em `pontuacao_logs.txt`.

---

## 🚀 Mecânicas & Geração Procedural
- **Geração Aleatória de Expressões:**
  - Sorteio de 2 a 4 números inteiros entre 1 e 100.
  - Seleção dinâmica de operadores na lista `['+', '-', 'x']`.
  - Construção da string da expressão e cálculo do resultado acumulado esperado.
- **Sistema de Pontuação:**
  - Cada acerto premia o jogador com 5 pontos.
  - Respostas incorretas mostram imediatamente o resultado correto.
- **Persistência de Logs:**
  - Ao final da série de rodadas, grava a data e o total no log:
    ```text
    [03/06/2026 14:32:15] Pontuacao: 20
    ```

---

## 💡 Destaque de Código
- Uso moderno da estrutura `match-case` (Python 3.10+) no menu principal.
- Tratamento de exceções com `try/except ValueError` para entradas de menu e respostas.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Python]]
- **Evolução:** [[Roadmap & Backlog]]

