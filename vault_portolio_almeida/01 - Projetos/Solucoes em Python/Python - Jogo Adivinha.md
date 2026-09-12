---
title: Python - Jogo Adivinha
tipo: projeto
area: jogos & logica
tecnologias: [Python, json]
status: concluído
tags: [projeto, python, jogos, adivinhacao, json, persistencia, tempo]
data_criacao: 2026-09-11
repositorio: "solucoes_em_python/jogo adivinha"
---

# 🔢 Python - Jogo de Adivinhação de Números

## 📌 Visão Geral
Jogo de console em [[Python]] onde o jogador tenta descobrir um número secreto sorteado pelo computador no menor número de tentativas possível. Apresenta 3 níveis de dificuldade, um sistema de dicas inteligentes que analisa a proximidade da resposta, persistência de recordes estruturados em formato JSON e contabilização do tempo total acumulado de jogo.

---

## 🚀 Funcionalidades
- **Seleção de Dificuldade:**
  - Júnior: 1 a 50
  - Pleno: 1 a 100
  - Sênior: 1 a 500
- **Dicas Inteligentes:**
  - "Muito alto!" / "Muito baixo!"
  - "Tá quase lá" (quando a diferença entre o palpite e o número sorteado é menor que 10).
- **Persistência de Recordes com JSON:**
  - Armazenamento em `recordes.txt` estruturado em dicionário:
    ```json
    {"Junior": 4, "Pleno": 7, "Senior": 12}
    ```
- **Rastreamento de Tempo Total Jogado:**
  - Acumulação do tempo de partida no arquivo `tempo.txt`.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Python]]
- **Evolução:** [[Roadmap & Backlog]]

