import random
import time
import os
from datetime import datetime

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
    scan = int(input("\nDigite o resultado:"))
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
    print("---- MATHMANIA - VERSÃO BETA ----\n")
    rodadas = int(input("Insira a quantidade de rodadas a serem jogadas: "))
    for cont in range(3):
        print(f"Começando em {cont+1}")
        time.sleep(1)
    for i in range(rodadas):
        pontuacao += jogo()
    
    with open('solucoes_em_python/mathmania/pontuacao_logs.txt', 'a') as pontuacaototal:
        dataAtual = datetime.now()
        dataFormatada = dataAtual.strftime("%d/%m/%Y %H:%M:%S")
        pontuacaototal.write(f'[{dataFormatada}] Pontuacao: {pontuacao}\n')
    