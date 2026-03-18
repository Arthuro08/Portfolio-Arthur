import random
import json
import time
import os

recorde = 0
nivelrecorde = None

def lertempo():
    global acumtotal
    try:
        with open("tempo.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            acumtotal = float(conteudo)
    except (ValueError, FileNotFoundError):
        acumtotal = 0


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
        datarecordes = {
            "Junior": None, 
            "Pleno": None, 
            "Senior": None
        }

    if datarecordes[nivelrecorde] is None or recorde < datarecordes[nivelrecorde]:
        print(f"Novo recorde para o nível {nivelrecorde}!")
        datarecordes[nivelrecorde] = recorde
        with open("recordes.txt", "w", encoding="utf-8") as arquivo:
            json.dump(datarecordes, arquivo, indent=4, ensure_ascii=False)

def viewrecordes():
    try:
        with open("recordes.txt") as arquivo:
            datarecordes = json.load(arquivo)
            print("\n- Recordes:")
            for nivel, recorde in datarecordes.items():
                if recorde == None:
                    recorde = "Não houve registro de"
                print(f"{nivel}: {recorde} tentativas")

    except FileNotFoundError:
        print("Não há nenhum recorde registrado no momento.")
    

def viewtempo():
    global acumtotal
    seg = int(acumtotal)
    dias = seg // 86400
    seg = seg % 86400

    horas = seg // 3600
    seg = seg % 3600

    minutos = seg // 60
    seg = seg % 60
    print("\n- Tempo total jogado:")
    if acumtotal == 0:
        print("Nenhum tempo registrado ainda. Já tentou concluir uma sessão?\n")
    else:
        if dias == 0 and horas == 0 and minutos == 0:
            print(f"{seg} segundos\n")
        elif dias == 0 and horas == 0:
            print(f"{minutos} minutos e {seg} segundos\n")
        elif dias == 0:
            print(f"{horas} horas, {minutos} minutos e {seg} segundos\n")
        else:
            print(f"{dias} dias, {horas} horas, {minutos} minutos e {seg} segundos\n") 
    input("\nPressione ENTER para voltar ao menu...")

def calctempo(tempinicial, tempfinal):
    global acumtotal
    total = tempfinal - tempinicial
    acumtotal = acumtotal + total
    with open("tempo.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(str(acumtotal))
        
tempinicial = time.time()
lertempo()
while True:
    os.system("cls")
    print("===== ADIVINHE O NÚMERO =====")
    print("\n1 - Nível júnior (1 a 50)")
    print("2 - Nível pleno (1 a 100)")
    print("3 - Nível sênior (1 a 500)")
    print("4 - Ver estatísticas")
    print("0 - Sair\n")
    try:
        dificuldade = int(input("Selecione a opção: "))
    except ValueError:
        print("Digite uma opção válida.")
        continue
    match dificuldade:
        case 1:
            dif = 50
            nivelrecorde = "Junior"
            recorde = jogar(dif)
            recordes(nivelrecorde, recorde)
        case 2:
            dif = 100
            nivelrecorde = "Pleno"
            recorde = jogar(dif)
            recordes(nivelrecorde, recorde)
        case 3:
            dif = 500
            nivelrecorde = "Senior"
            recorde = jogar(dif)
            recordes(nivelrecorde, recorde)
        case 4:
            os.system("cls")
            print("===== ESTATÍSTICAS =====")
            viewrecordes()
            viewtempo()
        case 0:
            print("Encerrando por hoje...")
            tempfinal = time.time()
            calctempo(tempinicial, tempfinal)
            break
        case _:
            print("Tente novamente")

