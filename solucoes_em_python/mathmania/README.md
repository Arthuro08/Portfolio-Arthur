# 🧮 MathMania - Jogo de Desafio Matemático em Python

## 📌 Sobre o Projeto
O MathMania é um jogo interativo desenvolvido em Python para execução no terminal, cujo objetivo é testar e aprimorar a agilidade de cálculo mental do usuário. O sistema gera expressões matemáticas dinâmicas e pseudoaleatórias compostas por múltiplos termos e operadores. A cada acerto, o jogador acumula pontos e, ao término de cada série de rodadas, a pontuação final é persistida em um arquivo de log acompanhada de carimbo de data e hora.

## 🚀 Funcionalidades
- **Geração Dinâmica de Expressões:** Montagem aleatória de expressões com 2 a 4 operandos numéricos entre 1 e 100.
- **Operações Diversificadas:** Suporte a adição (`+`), subtração (`-`) e multiplicação (`x`).
- **Configuração de Partida:** O usuário define quantas rodadas deseja disputar na sessão.
- **Contagem Regressiva e Interface Limpa:** Banner estilizado em ASCII art e contagem regressiva animada antes do início da bateria de contas.
- **Sistema de Pontuação:** Bonificação de 5 pontos por resposta correta e feedback imediato em caso de erro informando a resposta exata.
- **Registro Histórico (Logs):** Gravação automática da pontuação com carimbo temporal no arquivo `pontuacao_logs.txt`.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** Python 3
- **Módulos Nativos Utilizados:**
  - `random`: Sorteio de quantidades de operandos (`randint`), seleção de valores numéricos e escolha de operadores (`choice`).
  - `datetime`: Captura da data e horário exatos (`datetime.now()`) para auditoria das pontuações.
  - `time`: Controle de temporização (`sleep`) e ritmo entre as rodadas e menus.
  - `os`: Limpeza do console (`os.system('cls')`).

## 🧠 Conceitos Aplicados
- **Lógica e Aritmética Computacional:** Avaliação sequencial e encadeada de expressões numéricas em tempo de execução.
- **Tratamento de Exceções e Entradas:** Validação defensiva com blocos `try / except (ValueError)` para impedir quebras com caracteres inválidos, valores nulos ou números negativos.
- **Estrutura de Seleção Moderna (`match-case`):** Controle das opções de menu adotando a sintaxe de pattern matching do Python 3.10+.
- **Persistência e Manipulação de Arquivos:** Uso de gerenciadores de contexto (`with open(...)`) no modo append (`'a'`) para salvamento seguro dos logs.

## 📂 Estrutura do Projeto
```text
mathmania/
│
├── mathmania.py            # Código-fonte principal com a mecânica do jogo, gerador de contas e menus
└── pontuacao_logs.txt      # Histórico de partidas com data, hora e total de pontos conquistados
```

## ▶️ Como Executar

### 1. Pré-requisitos
- Python 3.10+ instalado (devido ao uso de `match-case`).

### 2. Execução
Abra o terminal no diretório do projeto e execute:
```bash
python mathmania.py
```

### 3. Exemplo de Histórico Gerado (`pontuacao_logs.txt`)
```text
[03/06/2026 14:32:15] Pontuacao: 20
[03/06/2026 14:35:42] Pontuacao: 15
```