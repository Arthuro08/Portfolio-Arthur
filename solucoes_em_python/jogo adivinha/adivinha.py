import random
import json

recorde = 0
nivelrecorde = None

def jogar(dif):
    i = 0
    num = random.randint(1, dif)
    while True:
        try:
            palpite = int(input(f"Eu pensei em um número de 1 a {dif}. Descubra qual é: "))
        except ValueError:
            print("Digite um número inteiro válido.")
            continue
        i = i + 1
        if palpite == num:
            print("Parabéns! Esse é o número que eu pensei.")
            print(f"Você acertou em {i} tentativas")
            input("\nPressione ENTER para voltar ao menu...")
            return i

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

def recordes(nivelrecorde, recorde):
    try:
        with open("recordes.txt", "r") as arquivo:
            datarecordes = json.load(arquivo)
    except FileNotFoundError:
        datarecordes = {"Júnior": None, "Pleno": None, "Sênior": None}

    if datarecordes[nivelrecorde] is None or recorde < datarecordes[nivelrecorde]:
        print(f"Novo recorde para o nível {nivelrecorde}!")
        datarecordes[nivelrecorde] = recorde
        with open("recordes.txt", "w") as arquivo:
            json.dump(datarecordes, arquivo)

while True:
    print("===== ADIVINHE O NÚMERO =====")
    print("\n1 - Nível júnior")
    print("2 - Nível pleno")
    print("3 - Nível sênior")
    print("0 - Sair\n")
    try:
        dificuldade = int(input("Selecione a dificuldade (de 1 a 3): "))
    except ValueError:
        print("Digite uma opção válida.")
        continue
    match dificuldade:
        case 1:
            dif = 50
            nivelrecorde = "Júnior"
            recorde = jogar(dif)
            recordes(nivelrecorde, recorde)
        case 2:
            dif = 100
            nivelrecorde = "Pleno"
            recorde = jogar(dif)
            recordes(nivelrecorde, recorde)
        case 3:
            dif = 500
            nivelrecorde = "Sênior"
            recorde = jogar(dif)
            recordes(nivelrecorde, recorde)
        case 0:
            print("Encerrando por hoje...")
            break
        case _:
            print("Tente novamente")

