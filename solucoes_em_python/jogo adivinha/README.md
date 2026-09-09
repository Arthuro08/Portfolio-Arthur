# 🔢 Jogo de Adivinhação em Python

## 📌 Sobre o Projeto
Este projeto é um jogo de adivinhação de números para console desenvolvido em Python. O jogador deve descobrir um número secreto gerado aleatoriamente pelo computador no menor número de palpites possível. O jogo conta com múltiplos níveis de dificuldade, um sistema de dicas inteligentes que analisa a proximidade do palpite, persistência de recordes individuais por dificuldade em formato JSON e rastreamento acumulado do tempo total que o usuário passou jogando.

## 🚀 Funcionalidades
- **Seleção de Dificuldade:**
  - **Júnior:** Intervalo de 1 a 50.
  - **Pleno:** Intervalo de 1 a 100.
  - **Sênior:** Intervalo de 1 a 500.
- **Dicas Inteligentes:**
  - Avisa se o número secreto é maior ("Muito baixo!") ou menor ("Muito alto!").
  - Alerta especial de proximidade ("Tá quase lá!") quando a distância do palpite para o número é menor que 10.
- **Quadro de Recordes:** Salva e atualiza automaticamente o recorde de menor número de tentativas para cada um dos 3 níveis de dificuldade.
- **Rastreamento de Tempo:** Mede e acumula o tempo gasto em cada partida, exibindo o total acumulado em segundos/minutos.
- **Menu Interativo:** Opções para iniciar partida, consultar recordes, visualizar tempo de jogo e sair.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** Python 3
- **Módulos Nativos Utilizados:**
  - `random`: Geração do número pseudoaleatório através de `randint()`.
  - `json`: Serialização e desserialização dos recordes estruturados no arquivo `recordes.txt`.
  - `time`: Medição precisa de timestamps com `time.time()` para cálculo do tempo jogado.
  - `os`: Limpeza visual do terminal (`cls`).

## 🧠 Conceitos Aplicados
- **Persistência de Dados Estruturados (JSON):** Leitura (`json.load`) e escrita (`json.dump`) de dicionários em arquivo texto garantindo persistência entre sessões.
- **Tratamento de Exceções (`try / except`):** Captura defensiva de `ValueError` na conversão de palpites e `FileNotFoundError` na inicialização de arquivos inexistentes.
- **Dicionários e Chaves Dinâmicas:** Associação das pontuações aos respectivos níveis ("Junior", "Pleno", "Senior").
- **Escopo e Variáveis Globais:** Gerenciamento do estado de tempo acumulado (`acumtotal`) e controle de fluxo com retorno de valores.

## 📂 Estrutura do Projeto
```text
jogo adivinha/
│
├── adivinha.py      # Código-fonte principal com a mecânica do jogo, recordes e menus
├── recordes.txt    # Arquivo de persistência contendo o menor número de tentativas por nível (JSON)
└── tempo.txt       # Arquivo de persistência com o tempo total jogado acumulado em segundos
```

## ▶️ Como Executar

### 1. Pré-requisitos
- Python 3.8+ instalado.

### 2. Execução
No terminal, entre na pasta do projeto e execute:
```bash
python adivinha.py
```

### 3. Como Jogar
1. Escolha a opção `1` para iniciar uma partida.
2. Selecione a dificuldade desejada (Júnior, Pleno ou Sênior).
3. Insira seus palpites guiando-se pelas dicas exibidas pelo sistema até acertar.
4. Consulte seus recordes a qualquer momento através da opção `2` do menu principal.
