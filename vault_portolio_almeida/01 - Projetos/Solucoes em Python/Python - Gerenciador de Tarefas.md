---
title: Python - Gerenciador de Tarefas
tipo: projeto
area: produtividade & persistencia
tecnologias: [Python]
status: concluído
tags: [projeto, python, crud, tarefas, todo, persistencia, terminal]
data_criacao: 2026-09-11
repositorio: "solucoes_em_python/task manager"
---

# ✅ Python - Gerenciador de Tarefas (To-Do List)

## 📌 Visão Geral
Aplicação de gerenciamento de tarefas e afazeres desenvolvida em [[Python]] com interface via terminal e persistência em arquivo de texto plano (`tarefas.txt`). Permite ao usuário manter controle de seus compromissos, organizando a lista em memória e sincronizando com disco sob demanda.

---

## 🚀 Funcionalidades
- **Adicionar Tarefa (`adicionar()`):** Adiciona uma nova string à lista em memória (`tarefas.append(tarefa)`).
- **Listar Tarefas (`listar()`):** Itera sobre a lista exibindo índices numéricos amigáveis ($1, 2, 3 \dots$).
- **Remover Tarefa (`remover()`):** Remove o item selecionado pelo índice fornecido através de `tarefas.pop(remove - 1)`.
- **Salvar em Arquivo (`salvar()`):** Grava os itens formatados e numerados no arquivo de texto:
  ```python
  with open("tarefas.txt", "w") as arquivo:
      for tarefa in tarefas:
          arquivo.write(str(i) + " - " + tarefa + "\n")
  ```
- **Carregar do Arquivo (`carregar()`):** Importa as tarefas gravadas no arquivo para a lista ativa do sistema.

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Python]]
- **Evolução:** [[Roadmap & Backlog]]

