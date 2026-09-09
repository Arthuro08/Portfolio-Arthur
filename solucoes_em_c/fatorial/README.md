# 🔢 Cálculo de Fatorial em C

## 📌 Sobre o Projeto
Este projeto é uma solução em linguagem C desenvolvida para realizar o cálculo do fatorial de números inteiros positivos. O algoritmo foi elaborado para processar múltiplas consultas sequenciais no terminal, utilizando uma estratégia de controle de fluxo contínuo com parada controlada por valor sentinela (`-1`).

## 🚀 Funcionalidades
- **Cálculo do Fatorial:** Determinação do produto $n! = n \times (n-1) \times \dots \times 1$ de forma iterativa.
- **Processamento Contínuo:** Capacidade de receber sucessivos números na mesma sessão de execução.
- **Encerramento por Sentinela:** Finalização graciosa do programa ao receber o número `-1`.
- **Tratamento de Base:** Inicialização do acumulador em `1`, garantindo resultado correto para $0! = 1$ e $1! = 1$.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** C
- **Compilador:** GCC (ou compatível)
- **Bibliotecas Padrão Utilizadas:**
  - `<stdio.h>`: Funções de entrada e saída (`printf`, `scanf`).
  - `<stdlib.h>`: Funções de controle e tipos utilitários.

## 🧠 Conceitos Aplicados
- **Laço com Condição de Parada Dupla (`while`):** Avaliação simultânea do sucesso da leitura (`scanf`) e checagem de valor sentinela (`n != -1`).
- **Laço Iterativo de Acumulação (`for`):** Multiplicação cumulativa progressiva dos fatores a partir de `x = 2` até `n`.
- **Variáveis Acumuladoras:** Reinicialização periódica de `fat = 1` a cada nova iteração do laço externo.

## 📂 Estrutura do Projeto
- `fatorial.c`: Código-fonte com o laço de leitura, cálculo iterativo e impressão dos fatoriais.

## ▶️ Como Executar

### 1. Pré-requisitos
- Compilador GCC instalado.

### 2. Compilação
Abra o terminal na pasta do projeto e execute:
```bash
gcc fatorial.c -o fatorial
```

### 3. Execução
- **No Windows:**
  ```powershell
  .\fatorial.exe
  ```
- **No Linux/macOS:**
  ```bash
  ./fatorial
  ```

### 4. Exemplo de Uso
```text
Entrada:
5
Resultado: 120

Entrada:
3
Resultado: 6

Entrada:
-1
(Programa finalizado)
```