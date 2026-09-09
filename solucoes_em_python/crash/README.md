# 🎮 Jogo Crash em Python

## 📌 Sobre o Projeto
Este projeto é uma simulação interativa via terminal do jogo "Crash", popular modalidade de apostas onde um multiplicador sobe progressivamente com o tempo. O jogador aposta um valor de sua carteira virtual e deve sacar pressionando a tecla de espaço antes que ocorra o "CRASH" repentino (gerado aleatoriamente). Quanto maior o tempo de espera, maior o multiplicador e o lucro, mas maior é o risco de perder todo o montante apostado na rodada.

## 🚀 Funcionalidades
- **Gestão de Carteira:** O jogador inicia com uma banca de R$ 1.000,00 que é atualizada dinamicamente com os ganhos e perdas.
- **Entrada de Apostas:** Permite apostar qualquer quantia com tratamento de exceções contra entradas não numéricas.
- **Multiplicador em Tempo Real:** Contador progressivo exibido no console com intervalo temporizado entre os níveis.
- **Mecânica de Saque Instantâneo:** Captura assíncrona do teclado (barra de **ESPAÇO**) sem travar o loop de contagem.
- **Ponto de Crash Aleatório:** O encerramento da rodada é determinado probabilisticamente a cada nova partida.

## 🛠️ Tecnologias, Ferramentas e Bibliotecas
- **Linguagem:** Python 3 (ambiente Windows devido ao `msvcrt`)
- **Módulos Nativos Utilizados:**
  - `msvcrt`: Captura não bloqueante de eventos do teclado (`kbhit` e `getch`) para o sistema Windows.
  - `random`: Sorteio do momento exato do crash (`randint`).
  - `time`: Medição do tempo decorrido (`time.time()`) para controle de cada segundo do multiplicador.
  - `os`: Limpeza do console (`os.system("cls")`) proporcionando uma interface limpa.

## 🧠 Conceitos Aplicados
- **Interatividade em Tempo Real:** Leitura de tecla sem necessidade de pressionar Enter, através de polling com `msvcrt.kbhit()`.
- **Laços Aninhados e Temporização:** Combinação de laços `for` (progresso do multiplicador) e `while` baseado em delta de tempo para amostragem de frames.
- **Tratamento de Exceções (`try / except`):** Proteção do fluxo principal contra erros de conversão com `ValueError`.
- **Escopo e Retorno de Funções:** Atualização do saldo da carteira como valor de retorno da função `jogo()`.

## 📂 Estrutura do Projeto
- `crash.py`: Código-fonte principal com a lógica da partida, captura de teclado e menu interativo.

## ▶️ Como Executar

### 1. Pré-requisitos
- Sistema Operacional **Windows** (necessário para suporte à biblioteca nativa `msvcrt`).
- Python 3.8+ instalado.

### 2. Execução
Abra o prompt de comando ou PowerShell na pasta do projeto e execute:
```bash
python crash.py
```

### 3. Como Jogar
1. Digite o valor que deseja apostar e aperte `Enter`.
2. Pressione qualquer tecla para iniciar a contagem.
3. Observe o multiplicador subir e aperte a barra de **ESPAÇO** no momento que desejar sacar seus lucros antes do crash!
