# 📚 Sistema de Cadastro de Alunos em C

## 📌 Sobre o Projeto
Este projeto é um sistema acadêmico de gerenciamento de estudantes desenvolvido em linguagem C para execução em terminal. A aplicação oferece uma interface interativa baseada em menu para realizar operações de cadastro, consulta, busca individual e análises estatísticas do desempenho da turma (como média geral, identificação do aluno destaque e percentual global de aprovação), com capacidade de armazenamento em memória de até 100 registros.

## 🚀 Funcionalidades
- **Menu Interativo:**
  - `1 - Cadastrar aluno`: Registro de nome, número de matrícula (até 4 dígitos) e duas notas parciais (0 a 10).
  - `2 - Listar alunos cadastrados`: Exibição de todos os alunos com nome, matrícula e média individual.
  - `3 - Buscar aluno por matrícula`: Localização instantânea de um estudante por ID.
  - `4 - Mostrar média geral da turma`: Cálculo da média aritmética combinada de todos os estudantes matriculados.
  - `5 - Mostrar aluno com maior média`: Identificação e destaque do estudante com o melhor desempenho da turma.
  - `6 - Mostrar percentual de aprovação`: Cálculo da taxa percentual de alunos aprovados (média $\ge 6.0$).
  - `0 - Sair`: Encerramento do sistema.
- **Validações e Regras de Negócio:**
  - Bloqueio de matrículas duplicadas.
  - Validação estrita de notas (valores devem pertencer ao intervalo $[0.0, 10.0]$).
  - Limite máximo seguro de 100 alunos.
  - Prevenção de divisão por zero e mensagens de aviso ao tentar calcular métricas com base vazia.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** C
- **Compilador:** GCC (ou compatível)
- **Bibliotecas Padrão Utilizadas:**
  - `<stdio.h>`: Leitura de dados compostos (`scanf` com máscara `[^\n]`), saídas formatadas e controle de menu.
  - `<stdlib.h>`: Funções utilitárias da biblioteca padrão.

## 🧠 Conceitos Aplicados
- **Estruturas de Dados Heterogêneas (`struct` / `typedef`):** Definição do tipo `registro_aluno` encapsulando nome, matrícula, notas e média calculada.
- **Passagem de Parâmetros por Referência (Ponteiros):** Uso de ponteiro `int *qtd` para atualizar o contador global de alunos nas funções.
- **Constantes de Pré-processamento (`#define`):** Definição da constante `APROVACAO 6` para centralizar a regra de corte de notas.
- **Manipulação Segura de Strings:** Leitura de strings com espaço via `scanf(" %49[^\n]", ...)` prevenindo estouro de buffer (*buffer overflow*).
- **Algoritmos de Varredura e Busca:** Busca linear para validação de unicidade de matrícula e determinação do maior elemento em vetor.

## 📂 Estrutura do Projeto
```text
sistema cadastro de alunos/
│
├── sistema_cadastro_alunos.c   # Código-fonte completo (structs, funções e menu principal)
└── output/                     # Diretório de compilação contendo o executável (.exe)
```

## ▶️ Como Executar

### 1. Pré-requisitos
- Compilador GCC instalado.

### 2. Compilação
Abra o terminal na pasta do projeto e execute:
```bash
gcc sistema_cadastro_alunos.c -o sistema_cadastro_alunos
```

### 3. Execução
- **No Windows:**
  ```powershell
  .\sistema_cadastro_alunos.exe
  ```
  *(Ou execute diretamente o binário já compilado na pasta `output/`)*
- **No Linux/macOS:**
  ```bash
  ./sistema_cadastro_alunos
  ```