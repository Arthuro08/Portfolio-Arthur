# 🎮 Jogo Crash em Python

## 📌 Sobre o Projeto

Este projeto é uma simulação simples do popular jogo "Crash", desenvolvido em Python para execução no terminal.

O objetivo é apostar um valor e tentar sacar antes que o jogo "quebre" (crash). Quanto mais você espera, maior o multiplicador — mas o risco também aumenta.

O projeto foi criado para praticar lógica de programação, interação com teclado em tempo real e controle de tempo.

---

## ⚙️ Funcionalidades

- Sistema de carteira (saldo do jogador)
- Apostas com valores personalizados
- Multiplicador crescente em tempo real
- Possibilidade de sacar pressionando **ESPAÇO**
- Evento aleatório de **CRASH**
- Loop contínuo de jogo

---

## 🧠 Regras do Jogo

- O jogador começa com **R$1000.00**
- A cada rodada:
  - Você escolhe o valor da aposta
  - O multiplicador começa em **0x** e aumenta
- Pressione **ESPAÇO** para sacar:
  - Ganho = valor apostado × multiplicador atual
- Se o jogo "crashar" antes:
  - Você perde o valor apostado
- O jogo continua até o usuário encerrar manualmente

---

## 🏗 Estrutura do Código

O projeto utiliza:

- `random` → para gerar o momento do crash  
- `time` → controle de tempo e delay  
- `os` → limpeza do terminal  
- `msvcrt` → captura de teclado em tempo real (Windows)  

- Função principal:
  - `jogo(carteira, valor)` → executa uma rodada

- Loop principal:
  - Controle de saldo
  - Entrada de apostas
  - Execução contínua do jogo

---

## ▶️ Como Executar

1. Certifique-se de estar no **Windows** (uso de `msvcrt`)
2. Execute o arquivo:

```bash
python crash.py
