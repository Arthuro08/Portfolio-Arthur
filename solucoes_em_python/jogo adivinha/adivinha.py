import random

def jogar(dif):
    i = 0
    num = random.randint(1, dif)
    while True:
        palpite = int(input(f"Eu pensei em um número de 1 a {dif}. Descubra qual é: "))
        i = i + 1
        if palpite == num:
            print("Parabéns! Esse é o número que eu pensei.")
            print(f"Você acertou em {i} tentativas")
            input("\nPressione ENTER para voltar ao menu...")
            break

        elif palpite > num:
            if palpite < num + 10:
                print("Tá quase lá. É um número um pouco menor")
            else:
                print("Muito alto!")

        elif palpite < num:
            if palpite > num - 10:
                print("Tá quase lá. É um número um pouco maior")
            else:
                print("Muito baixo!")

while True:
    print("===== ADIVINHE O NÚMERO =====")
    print("\n1 - Nível júnior")
    print("2 - Nível pleno")
    print("3 - Nível sênior\n")
    dificuldade = int(input("Selecione a dificuldade (de 1 a 3): "))
    match dificuldade:
        case 1:
            dif = 50
            jogar(dif)
        case 2:
            dif = 100
            jogar(dif)
        case 3:
            dif = 500
            jogar(dif)
        case _:
            print("Tente novamente")

