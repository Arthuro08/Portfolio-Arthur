---
title: Técnica - Captura Não-Bloqueante de Teclado no Windows com msvcrt
tipo: troubleshooting
area: terminal & tempo real
tags: [troubleshooting, python, msvcrt, terminal, jogos, nao-bloqueante]
data_criacao: 2026-09-11
---

# 🎮 Técnica: Captura Não-Bloqueante de Teclado no Windows com msvcrt

## 📌 O Desafio Técnico
Ao desenvolver jogos de console em [[Python]] como o [[Python - Jogo Crash]], o uso da função padrão `input()` trava a execução do script até que o usuário digite algo e aperte `Enter`. No entanto, em um jogo com multiplicador dinâmico em tempo real, o contador precisa continuar subindo a cada segundo enquanto o sistema "escuta" se uma tecla de saque foi pressionada.

---

## ⚡ A Solução com `msvcrt` (C Runtime Library do Windows)
O módulo nativo `msvcrt` disponibiliza duas funções fundamentais:
- `msvcrt.kbhit()`: Retorna `True` se houver alguma tecla pressionada esperando no buffer, **sem bloquear** o laço de repetição.
- `msvcrt.getch()`: Lê um único caractere diretamente do buffer do console, sem ecoar na tela e sem exigir `Enter`.

### Padrão de Implementação:
```python
import msvcrt
import time

inicio = time.time()

# Espera até 2 segundos por ciclo sem travar:
while time.time() - inicio < 2:
    if msvcrt.kbhit():
        tecla = msvcrt.getch().decode()
        if tecla == chr(32): # Código ASCII 32 = Barra de Espaço
            print("Saque realizado com sucesso!")
            break
```

---

## ⚠️ Limitações & Considerações
- O módulo `msvcrt` é exclusivo do ecossistema Microsoft Windows.
- Para rodar a mesma lógica no Linux ou macOS, utiliza-se a biblioteca `curses` ou a manipulação de terminais POSIX com `termios` e `tty`.

---

## 🔗 Projetos Relacionados
- [[Python - Jogo Crash]]
- [[Python]]

