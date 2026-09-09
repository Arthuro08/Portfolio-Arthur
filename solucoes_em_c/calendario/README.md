# 📅 Validador e Incrementador de Data em C

## 📌 Sobre o Projeto
Este projeto é um utilitário desenvolvido em linguagem C para validar datas informadas pelo usuário e computar automaticamente a data do dia subsequente. O programa processa uma data informada no formato de números inteiros (dia, mês e ano), avalia regras de calendário gregoriano (como meses com 30 ou 31 dias e o limite padrão de fevereiro) e calcula a transição de virada de mês e de virada de ano.

## 🚀 Funcionalidades
- **Validação de Datas:**
  - Rejeição de valores negativos ou zerados para dia ou mês.
  - Rejeição de anos negativos.
  - Verificação de meses com limite de 30 dias (abril, junho, setembro e novembro).
  - Verificação de meses com limite de 31 dias.
  - Validação estrita para o mês de fevereiro (limite de 28 dias).
- **Cálculo do Dia Seguinte:**
  - Incremento regular do dia quando dentro do mesmo mês.
  - Transição de fim de mês: reinicia o dia para `1` e incrementa o mês.
  - Transição de fim de ano (Reveillon): reinicia dia e mês para `1` e incrementa o ano.
- **Saída Formatada:** Exibição da data calculada no padrão `D.M.A` ou mensagem `Invalid` em caso de incoerência.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** C
- **Compilador:** GCC (ou compatível)
- **Bibliotecas Padrão Utilizadas:**
  - `<stdio.h>`: Entrada e saída de dados no terminal (`printf`, `scanf`).
  - `<stdlib.h>`: Funções utilitárias da biblioteca padrão do C.

## 🧠 Conceitos Aplicados
- **Operadores Lógicos e Condicionais:** Uso intensivo de operadores relacionais e lógicos (`&&`, `||`, `>`, `<`, `==`) para cobertura dos casos de borda do calendário.
- **Controle de Fluxo com Encadeamentos `if / else`:** Tratamento das camadas de validação prioritária antes de executar a lógica de incremento.
- **Aritmética e Atribuição de Variáveis:** Atualização em cascata de dia (`x`), mês (`y`) e ano (`z`).

## 📂 Estrutura do Projeto
- `calendario.c`: Código-fonte com leitura de entrada, árvore de decisões lógicas e impressão da data resultante.

## ▶️ Como Executar

### 1. Pré-requisitos
- Compilador GCC instalado.

### 2. Compilação
Abra o terminal na pasta do projeto e execute:
```bash
gcc calendario.c -o calendario
```

### 3. Execução
- **No Windows:**
  ```powershell
  .\calendario.exe
  ```
- **No Linux/macOS:**
  ```bash
  ./calendario
  ```

### 4. Exemplos de Entrada e Saída
- **Entrada:** `28 2 2024` → **Saída:** `1.3.2024`
- **Entrada:** `31 12 2023` → **Saída:** `1.1.2024`
- **Entrada:** `31 4 2023` → **Saída:** `Invalid` (Abril só possui 30 dias)
