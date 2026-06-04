import random
import time
import os
from datetime import datetime

ascii = """
  __  __    _  _____ _   _ __  __    _    _   _ ___    _    
 |  \/  |  / \|_   _| | | |  \/  |  / \  | \ | |_ _|  / \   
 | |\/| | / _ \ | | | |_| | |\/| | / _ \ |  \| || |  / _ \  
 | |  | |/ ___ \| | |  _  | |  | |/ ___ \| |\  || | / ___ \ 
 |_|  |_/_/   \_\_| |_| |_|_|  |_/_/   \_\_| \_|___/_/   \_|
____________________________________________________________                                                                                
"""

def qtdrodadas(pontuacao):
    try:
        rodadas = int(input("Insira a quantidade de rodadas a serem jogadas: "))
        if rodadas == 0:
            print("Número inválido. Não pode ser 0. Tente novamente")
            time.sleep(1)
        elif rodadas < 0:
            print("Número inválido. Não pode ser número negativo. Tente novamente")
            time.sleep(1)
        else:
            for cont in range(3, 0, -1):
                print(f"Começando em {cont}")
                time.sleep(1)
        for i in range(rodadas):
            pontuacao += jogo()
        salvar(pontuacao)
    except ValueError:
        print("Número inválido. Tente novamente")
        time.sleep(1)

def salvar(pontuacao):
    with open('solucoes_em_python/mathmania/pontuacao_logs.txt', 'a') as pontuacaototal:
        dataAtual = datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M:%S")
        pontuacaototal.write(f'[{dataFormatada}] Pontuacao: {pontuacao}\n')

def jogo():
    os.system('cls')
    expressao = ""
    result = 0
    qtd = random.randint(2,4)
    for i in range(qtd):
        num = random.randint(1,100)
        result += num
        if i == qtd-1:
            expressao += f"{num}"
        else:
            expressao += f"{num} + "
    
    print(expressao)
    scan = int(input("\nDigite o resultado: "))
    if scan == result:
        print("\nParabéns, você acertou! 5 pontos")
        time.sleep(2)
        return 5
    else:
        print(f"\nVocê errou! O resultado era {result}. 0 pontos")
        time.sleep(2)
        return 0

while(True):
    os.system('cls')
    pontuacao = 0
    print(ascii)
    print("MENU\n")
    print("1 - Começar jogo")
    print("0 - Sair\n")
    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
    if opcao < 0 or opcao > 1:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
    else:
        match(opcao):
            case 1:
                qtdrodadas(pontuacao)
            case 0:
                print("Saindo do jogo...")
                time.sleep(1)
                break
    