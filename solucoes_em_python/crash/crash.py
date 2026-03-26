import random
import os
import time
import msvcrt


def jogo(carteira, valor):
    parada = random.randint(1,10)

    for cont in range(11):
        os.system("cls")
        print(cont)

        inicio = time.time()

        while time.time() - inicio < 2:
            if msvcrt.kbhit(): 
                tecla = msvcrt.getch().decode()

                if tecla == chr(32): 
                    ganho = valor * cont
                    print(f"\nVocê sacou em {cont}x!")
                    print(f"Ganhou R${ganho:.2f}")
                    input("\nPressione qualquer tecla para continuar")
                    return carteira + ganho

        if parada == cont:
            print("CRASH!")
            carteira -= valor
            input("\nPressione qualquer tecla para tentar novamente")
            return carteira

carteira = 1000.00

while True:
    os.system("cls")
    print("===== JOGO CRASH =====")
    print(f"\nVocê possui R${carteira:.2f} no bolso")
    try:
        valor = float(input("\n\nInsira um valor para apostar: "))
        
        input(f"\nVALOR ESCOLHIDO: R${valor:.2f} Aperte qualquer tecla para jogar")
        carteira = jogo(carteira, valor)
    except ValueError:
        pass
    


