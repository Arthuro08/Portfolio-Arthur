# 🔢 Jogo de Adivinhação em Python

## 📌 Sobre o Projeto

Este projeto é um jogo de adivinhação desenvolvido em Python, onde o jogador deve descobrir um número aleatório dentro de um intervalo definido.

O jogo possui diferentes níveis de dificuldade, sistema de recordes e controle de tempo total jogado, com armazenamento em arquivos.

O objetivo é praticar lógica de programação, manipulação de arquivos e estruturas de controle.

---

## ⚙️ Funcionalidades

- Sistema de níveis de dificuldade (Júnior, Pleno e Sênior)
- Geração de número aleatório a cada partida
- Dicas inteligentes (alto, baixo ou "quase lá")
- Contagem de tentativas
- Sistema de recordes por nível
- Registro de tempo total jogado
- Menu interativo no terminal

---

## 🧠 Regras do Jogo

- Escolha um nível:
  - **Júnior** → número entre 1 e 50  
  - **Pleno** → número entre 1 e 100  
  - **Sênior** → número entre 1 e 500  

- A cada tentativa:
  - O jogo informa se o número é maior ou menor
  - Dicas extras aparecem quando você está próximo

- O objetivo é:
  - Acertar o número com o menor número de tentativas possível

- O sistema salva:
  - 🏆 Melhor número de tentativas por nível  
  - ⏱ Tempo total acumulado de jogo  

---

## 🏗 Estrutura do Código

O projeto utiliza:

- `random` → geração do número aleatório  
- `json` → armazenamento dos recordes  
- `time` → controle de tempo jogado  
- `os` → limpeza do terminal  

### Principais funções:

- `jogar(dif)` → executa uma partida  
- `recordes()` → salva e atualiza recordes  
- `viewrecordes()` → exibe recordes  
- `viewtempo()` → mostra tempo total jogado  
- `calctempo()` → calcula e salva o tempo acumulado  

---

## 💾 Arquivos Gerados

- `recordes.txt` → armazena os melhores resultados por nível  
- `tempo.txt` → guarda o tempo total jogado  

---

## ▶️ Como Executar

1. Execute o arquivo:

```bash
python nome_do_arquivo.py
