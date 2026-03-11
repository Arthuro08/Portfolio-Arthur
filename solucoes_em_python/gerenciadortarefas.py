import os

tarefas = []

def adicionar():
   tarefa = str(input("Digite a tarefa: "))
   tarefas.append(tarefa)
   print("Tarefa adicionada com sucesso!")
   input("Pressione qualquer tecla para continuar...")

def listar():
    if len(tarefas) == 0:
        print("Não há tarefas registradas!")
    else:
        tamlista = len(tarefas)
        for i in range(tamlista):
            print(i+1,"-", tarefas[i])
    input("Pressione qualquer tecla para continuar...")

def remover():
    remove = int(input("Digite o número da tarefa a ser removida: "))
    tarefas.pop(remove - 1)
    print("Tarefa removida com sucesso!")
    input("\nPressione qualquer tecla para continuar...")

def salvar():
    i = 0
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            i=i+1
            arquivo.write(str(i) + " - " + tarefa + "\n")
    print("Lista de tarefas salva com sucesso!")
    input("\nPressione qualquer tecla para continuar...")

def carregar():
    try:
        tarefas.clear()
        with open("tarefas.txt", "r") as arquivo:
            for tarefa in arquivo:
                tarefas.append(tarefa.strip())
    except FileNotFoundError:
        pass

while True:
    os.system("cls")
    print("===== GERENCIADOR DE TAREFAS =====")
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Carregar lista")
    print("5 - Salvar lista de tarefas")
    print("0 - Sair\n")
    num = int(input("Escolha uma opção: "))
    match num:
        case 1:
            adicionar()
        case 2:
            listar()
        case 3:
            remover()
        case 4:
            carregar()
        case 5:
            salvar()
        case 0:
            decisao = input("Deseja salvar a lista de tarefas antes de sair? (S ou N): ").upper()
            if decisao == "S":
                salvar()
                print("Encerrando sistema...")
                break
            elif decisao != "N":
                print("Tente novamente!")
            else:
                print("Encerrando sistema...")
                break
        case _:
            print("Opção inválida, tente novamente")
