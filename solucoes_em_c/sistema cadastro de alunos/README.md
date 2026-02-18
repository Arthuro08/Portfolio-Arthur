# 📚 Sistema de Cadastro de Alunos em C

## 📌 Sobre o Projeto

Este projeto é um sistema simples de cadastro de alunos desenvolvido em linguagem C.  
Ele permite armazenar até 100 alunos e realizar operações básicas como cadastro, listagem, busca e cálculos estatísticos.

O objetivo principal é praticar e consolidar fundamentos da linguagem C, organização de código e lógica de programação.

---

## ⚙️ Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

1 - Cadastrar aluno  
2 - Listar alunos cadastrados  
3 - Buscar aluno por matrícula  
4 - Mostrar média geral da turma  
5 - Mostrar aluno com maior média  
6 - Mostrar percentual de aprovação  
0 - Sair  

---

## 🧠 Regras de Negócio

- O sistema permite cadastrar até **100 alunos**.
- A média do aluno é calculada automaticamente a partir de duas notas.
- A média mínima para aprovação é definida pela constante:

```c
#define APROVACAO 6
```

- O sistema impede cálculos quando não há alunos cadastrados.
- Caso o limite de 100 alunos seja atingido, o cadastro é bloqueado.

---

## 🏗 Estrutura do Código

O projeto utiliza:

- `struct` para representar os dados do aluno
- Vetor fixo para armazenamento
- Ponteiros para controle da quantidade de registros
- Funções separadas para cada funcionalidade
- Menu interativo com `switch-case`