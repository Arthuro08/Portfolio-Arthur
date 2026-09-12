---
title: Solução - Git Fatal Index Smaller Than Expected
tipo: troubleshooting
area: controle de versao & git
tags: [troubleshooting, git, fatal, index, onedrive, corrupcao]
data_criacao: 2026-09-11
---

# 🛠️ Resolução de Erro: `fatal: index file smaller than expected` no Git

## 📌 Sintoma do Problema
Ao tentar rodar `git status`, `git add` ou abrir a aba de Source Control no Visual Studio Code, o Git aborta com a mensagem:

```text
fatal: .git/index: index file smaller than expected
```

---

## 🔍 Causa Raiz
O arquivo `.git/index` é a **área de staging** binária do Git, onde ficam cacheadas as mudanças preparadas para o próximo commit. Esse arquivo corrompe e é truncado para **0 bytes** quando:
1. **Sincronização em Nuvem (OneDrive / Google Drive / Dropbox):** O repositório está dentro de uma pasta sincronizada (ex: `OneDrive\Documentos\Portfolio-Arthur`). Quando o Git tenta regravar o `.git/index` e o OneDrive tenta sincronizá-lo simultaneamente, ocorre conflito de I/O e o arquivo é zerado.
2. **Queda de Energia ou Encerramento Abrupto:** O VS Code ou o terminal é fechado exatamente no milissegundo em que o Git estava escrevendo no index.

---

## ✅ Como Resolver sem Perder Nenhum Código
O histórico de commits e os arquivos reais do repositório ficam salvos em `.git/objects/` e continuam 100% intactos. Apenas o índice intermediário foi afetado.

### Passo a Passo no Terminal (PowerShell / Bash):

1. **Remova o arquivo corrompido de índice:**
   ```powershell
   Remove-Item .git\index
   ```
   *(Ou no Linux/macOS / Git Bash: `rm .git/index`)*

2. **Reconstrua o índice a partir do último commit (`HEAD`):**
   ```bash
   git reset
   ```

3. **Verifique se o Git voltou a funcionar:**
   ```bash
   git status
   ```

O Git recriará um novo arquivo `.git/index` saudável e o VS Code voltará a listar suas alterações normalmente.

