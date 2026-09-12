---
title: Python - Jogo Crash
tipo: projeto
area: jogos & tempo real
tecnologias: [Python, msvcrt]
status: concluído
tags: [projeto, python, crash, jogos, tempo-real, terminal, apostas]
data_criacao: 2026-09-11
repositorio: "solucoes_em_python/crash"
---

# 🎮 Python - Jogo Crash no Terminal

## 📌 Visão Geral
Simulação interativa do popular jogo de apostas "Crash", desenvolvida em [[Python]] para terminal. O jogador define uma aposta a partir de sua carteira virtual (iniciando com R$ 1.000,00) e observa o multiplicador subir segundo a segundo. O desafio consiste em sacar os ganhos pressionando a barra de **espaço** antes que ocorra o momento imprevisível de parada ("CRASH").

---

## 🚀 Mecânicas do Jogo
- **Carteira Dinâmica:** Os lucros (aposta $\times$ multiplicador) e prejuízos são somados ou subtraídos do saldo do usuário.
- **Multiplicador Temporizado:** Contador de 0x a 10x com pausa calculada via delta de tempo (`time.time()`).
- **Ponto de Crash Aleatório:** Sorteio via `random.randint(1, 10)` definindo o limiar em que a rodada é perdida.
- **Saque Assíncrono:** Captura da barra de espaço sem exigir o acionamento da tecla `Enter`.

---

## 💡 Destaque de Engenharia: Polling de Teclado
Para permitir que o jogador tome uma ação no teclado enquanto o laço de contagem continua rodando em primeiro plano, o script utiliza a biblioteca nativa do Windows `msvcrt`:

```python
if msvcrt.kbhit(): 
    tecla = msvcrt.getch().decode()
    if tecla == chr(32): # Barra de Espaço
        ganho = valor * cont
        return carteira + ganho
```

---

## 🔗 Links e Notas Relacionadas
- **Tecnologias:** [[Python]]
- **Casos de Suporte:** [[Tecnica - Captura Nao-Bloqueante de Teclado no Windows com msvcrt]]
- **Evolução:** [[Roadmap & Backlog]]

