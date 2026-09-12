---
title: MOC - Troubleshooting & DevLog
tipo: moc
tags: [moc, devlog, troubleshooting, bugs, licoes-aprendidas]
data_criacao: 2026-09-11
---

# 🛠️ Mapa de Conteúdo: Troubleshooting & DevLog

Este índice reúne documentações técnicas de problemas reais enfrentados durante o desenvolvimento dos projetos, os diagnósticos técnicos efetuados e as soluções consolidadas. É uma seção de alto valor para consulta rápida e para motores de **RAG**.

---

## 📑 Registros de Soluções & Casos Reais

- [[Solucao - Erro Msg 208 Objeto Invalido SQL Server]]
  - **Contexto:** Execução de scripts DDL/DQL com funções e views no SQL Server onde tabelas válidas acusavam "Nome de objeto inválido".
  - **Causa Raiz:** Ausência do delimitador de lote `GO` e contexto da conexão preso ao banco `master`.
  - **Solução:** Isolamento de lotes com `GO` e seleção explícita da database ativa.

- [[Guia - Conexao Python e SQL Server via pyodbc]]
  - **Contexto:** Integração de scripts Python CLI e APIs Flask com bancos de dados relacionais Microsoft SQL Server.
  - **Causa Raiz:** Configurações de drivers ODBC (`{SQL Server}`), instâncias nomeadas e autenticação confiável do Windows (`Trusted_Connection=yes`).
  - **Solução:** Padrão de connection string resiliente e boas práticas com cursores e `commit()`.

- [[Tecnica - Captura Nao-Bloqueante de Teclado no Windows com msvcrt]]
  - **Contexto:** Desenvolvimento de jogos de console em tempo real ([[Python - Jogo Crash]]) sem pausar o laço de execução no `input()`.
  - **Causa Raiz:** A função `input()` bloqueia a thread de execução do interpretador Python.
  - **Solução:** Polling com `msvcrt.kbhit()` e leitura do buffer com `msvcrt.getch()`.

- [[Solucao - Git Fatal Index Smaller Than Expected]]
  - **Contexto:** Erro `fatal: index file smaller than expected` ao tentar rodar `git status` ou abrir o Source Control no VS Code.
  - **Causa Raiz:** Arquivo `.git/index` corrompido ou truncado para 0 bytes devido a conflitos de I/O de sincronização do OneDrive / fechamento abrupto.
  - **Solução:** Remoção do `.git/index` corrompido e reconstrução limpa com `git reset`.


