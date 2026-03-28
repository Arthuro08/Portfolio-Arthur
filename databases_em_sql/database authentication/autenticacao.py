import pyodbc
import os
import time

config = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-MLFI9DN;'
    'Database=Users_Sistema;'
    'Trusted_Connection=yes;'
)

ADMSENHA = '08032007'
cursor = config.cursor()

def cadastrar():
    sign_user = input('\nInsira um nome de usuário: ')
    if len(sign_user) > 20:
        print('ERRO: O nome de usuário não deve exceder 20 caracteres')
        input('Aperte qualquer tecla para continuar...')
        return
    
    cursor.execute('SELECT Usuario.Username from Usuario')
    for row in cursor:
        if row.Username == sign_user:
            print('\nERRO: Este nome de usuário já existe. Tente novamente.')
            input('Aperte qualquer tecla para continuar...')
            return
    
    sign_senha = input('Perfeito! Agora crie uma senha: ')
    if len(sign_senha) > 20:
        print('\nERRO: A senha não deve exceder 20 caracteres.')
        input('Aperte qualquer tecla para continuar...')
        return
    if len(sign_senha) < 8:
        print('\nERRO: A senha deve conter pelo menos 8 caracteres')
        input('Aperte qualquer tecla para continuar...')
        return
    confirm_senha = input('Quase lá. Agora confirme a senha: ')
    if sign_senha != confirm_senha:
        print('\nERRO: A confirmação de senha falhou.')
        input('Aperte qualquer tecla para continuar...')
        return
    cursor.execute("INSERT INTO Usuario (Username, Senha) VALUES (?, ?)", (sign_user, sign_senha))
    config.commit()
    print('\nConta efetuada com sucesso!')
    input('\nAperte qualquer tecla para continuar...')

def login():
    log_user = input('\nInsira o nome de usuário: ')
    log_senha = input('Insira a senha: ') 
    cursor.execute('SELECT * FROM Usuario')
    encontrado = False

    for row in cursor:
        if row.Username == log_user and row.Senha == log_senha:
            encontrado = True
            break

    if encontrado:
        print(f'\nAcesso liberado. Seja bem-vindo(a) de volta, {log_user}')
        input('Aperte qualquer tecla para continuar...')
    else:
        print('\nERRO: Usuário ou senha inválidos.')
        input('Aperte qualquer tecla para continuar...')

def adm():
    
    admtentativa_senha = input('Insira a senha de administrador: ')
    if admtentativa_senha == ADMSENHA:
        print('Acesso concedido')
        time.sleep(1)
        while True:
            os.system("cls")
            print('======= ACESSO DO ADMINISTRADOR =======')
            print('\n1 - Listar usuários e senhas')
            print('2 - Deletar usuário')
            print('0 - Voltar ao menu principal')
            try:
                opcaoadm = int(input('Escolha uma opção: '))
            except ValueError:
                print('ERRO: Insira uma opção válida!')
                continue
            
            match opcaoadm:
                case 1:
                    admlistar()
                case 2:
                    admremover()   
                case 0:
                    print('Saindo...')
                    time.sleep(2)
                    return     
    else:
        print('ERRO: Acesso negado. Senha de administrador inválida.')
        input('\nAperte qualquer tecla para continuar...')

def admlistar():
    print('\n==== REGISTRO DE USUÁRIOS NO SISTEMA ====\n')
    cursor.execute('SELECT Usuario.Username, Usuario.Senha FROM Usuario')
    for row in cursor:
        print(f'Usuário: {row.Username} | Senha: {row.Senha}')
    input('\nAperte qualquer tecla para continuar...')

def admremover():
    encontrado = 0
    removeuser = input('\nDigite o usuário a ser removido: ')
    cursor.execute('SELECT * FROM Usuario')
    for row in cursor:
        if row.Username == removeuser:
            encontrado = 1
    if encontrado == 1:
        cursor.execute('DELETE FROM Usuario WHERE Username = ? ', (removeuser,))
        config.commit()
        print('Usuário apagado do banco de dados do sistema com sucesso!')
        input('\nAperte qualquer tecla para continuar...')
    else:
        print('ERRO: Usuário não encontrado no sistema!')
        input('\nAperte qualquer tecla para continuar...')

while True:
    os.system('cls')
    print('======= AUTENTICAÇÃO DE USUÁRIO =======')
    print('\n1 - Efetuar Cadastro')
    print('2 - Efetuar Log-in')
    print('3 - Acesso do administrador')
    print('0 - Sair')

    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('ERRO: Insira uma opção válida!')
        continue

    match opcao:
        case 1:
            cadastrar()
        case 2:
            login()
        case 0:
            cursor.close()
            config.close()
            print('Saindo.')
            time.sleep(1)
            print('Saindo..')
            time.sleep(1)
            print('Saindo...')
            time.sleep(2)
            break
        case 3:
            adm()
        case _:
            print('ERRO: Insira uma opção válida!')
