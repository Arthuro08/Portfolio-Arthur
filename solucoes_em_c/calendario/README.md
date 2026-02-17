# 📅 Validador e Incrementador de Data em C

## 📌 Descrição

Solução desenvolvida em C com o objetivo de validar uma data informada pelo usuário e calcular o dia seguinte.

O programa recebe três valores inteiros representando:

- Dia
- Mês
- Ano

Caso a data seja inválida, o sistema imprime `Invalid`.  
Caso seja válida, o programa calcula e exibe o dia seguinte no formato: dia.mes.ano

## 🚀 Funcionalidades

- Validação de:
  - Dia inválido
  - Mês inválido
  - Ano negativo
  - Meses com 30 dias
  - Fevereiro (considerando até 28 dias)
  - Cálculo automático do dia seguinte
  - Atualização automática de:
  - Mudança de mês
  - Mudança de ano

---

## 🛠 Tecnologias Utilizadas

- Linguagem C
- Biblioteca padrão `<stdio.h>`
- Biblioteca `<stdlib.h>`

---

## 🧠 Conceitos Aplicados

- Estruturas condicionais (`if / else`)
- Operadores lógicos (`&&`, `||`)
- Validação de entrada
- Manipulação de datas simples
- Controle de fluxo
