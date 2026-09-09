# 🧮 Calculadora Científica em C

## 📌 Sobre o Projeto
Este projeto consiste em uma calculadora desenvolvida em linguagem C para execução em terminal. A aplicação permite ao usuário realizar cálculos aritméticos básicos e operações matemáticas avançadas (como exponenciação e radiciação), mantendo a execução contínua através de um laço de repetição e implementando verificações defensivas contra erros matemáticos clássicos (como divisão por zero e raízes de valores negativos).

## 🚀 Funcionalidades
- **Operações Suportadas:**
  - Adição (`+`)
  - Subtração (`-`)
  - Multiplicação (`*`)
  - Divisão (`/`) com bloqueio de divisão por zero
  - Exponenciação (`e`) utilizando a base e o expoente
  - Radiciação (`r`) calculando a raiz quadrada com bloqueio de radicando negativo
- **Tratamento de Exceções e Entradas:**
  - Validação de operadores desconhecidos.
  - Alerta de erro para divisor igual a `0`.
  - Alerta de erro para raízes com valores menores que `0`.
- **Fluxo Contínuo:** Sistema de repetição permitindo realizar múltiplos cálculos em sequência sem reiniciar a aplicação.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** C (padrão C99 / C11)
- **Compilador:** GCC (GNU Compiler Collection) ou qualquer compilador C compatível
- **Bibliotecas Padrão Utilizadas:**
  - `<stdio.h>`: Funções de entrada e saída formatada (`printf`, `scanf`).
  - `<math.h>`: Funções matemáticas especializadas (`pow` para potência e `sqrt` para raiz quadrada).

## 🧠 Conceitos Aplicados
- **Modularização de Funções:** Criação da função `calc()` para isolar as operações matemáticas da lógica de interação com o usuário na `main()`.
- **Estruturas de Decisão:** Uso de `switch-case` para seleção eficiente de operadores e encadeamentos `if / else if` para validações preventivas.
- **Laços de Repetição:** Utilização do laço `do-while` para garantir ao menos uma execução e checar a decisão de continuidade (`S`/`N`).
- **Formatação de Ponto Flutuante:** Leitura e precisão de números reais utilizando o tipo `double` com especificador `%lf` e exibição arredondada em duas casas (`%.2lf`).

## 📂 Estrutura do Projeto
- `calculadora.c`: Código-fonte completo contendo a função de cálculo e o fluxo interativo principal.

## ▶️ Como Executar

### 1. Pré-requisitos
- Compilador GCC instalado (como MinGW no Windows ou build-essential no Linux).

### 2. Compilação
No terminal, navegue até a pasta do projeto e compile o código vinculando a biblioteca matemática (`-lm`):
```bash
gcc calculadora.c -o calculadora -lm
```

### 3. Execução
Execute o binário compilado:
- **No Windows:**
  ```powershell
  .\calculadora.exe
  ```
- **No Linux/macOS:**
  ```bash
  ./calculadora
  ```

### 4. Exemplo de Uso
- Para calcular `10 * 5`: digite `10 * 5`
- Para calcular raiz quadrada de `49`: digite `49 r`
- Ao final, digite `S` para continuar ou `N` para finalizar.