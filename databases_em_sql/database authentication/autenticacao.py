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
        time.sleep(1)
        user(log_user)

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

def user(nome_user):
    while True:
        os.system('cls')
        print('\n==== ACESSO DO USUÁRIO ====\n')
        print('1 - Ver dados da conta')
        print('2 - Alterar senha')
        print('3 - Alterar nome de usuário')
        print('4 - Deletar conta')
        print('0 - Log-out')
        try:
            opcao = int(input(f'Olá, {nome_user}. Escolha uma das opções acima: '))
        except ValueError:
            print('ERRO: Insira uma opção válida!')
            continue
        match opcao:
            case 1:
                userdados(nome_user)
            case 2:
                useralterarsenha(nome_user)
            case 3:
                nome_user = useralterarusername(nome_user)
            case 4:
                ops = userdeletar(nome_user)
                if ops == 1:
                    break
            case 0:
                break

def userdados(nome_user):
    print("\n======= DADOS DA CONTA =======\n")
    cursor.execute('SELECT * FROM Usuario WHERE Username = ?', (nome_user,))
    row = cursor.fetchone()
    print(f'Usuário: {row.Username}')
    print(f'ID: {row.ID_Usuario}')
    input('\nAperte qualquer tecla para continuar...')

def useralterarsenha(nome_user):
    alterarsenha = input('\nEscolha uma nova senha: ')
    confirm_alterarsenha = input('Confirme essa nova senha:')
    if alterarsenha != confirm_alterarsenha:
        print('\nERRO: A confirmação de senha falhou.')
        input('\nAperte qualquer tecla para continuar...')
        return
    else:
        cursor.execute('UPDATE Usuario SET Senha = ? WHERE Username = ?', (alterarsenha, nome_user))
        config.commit()
        print('A alteração de senha foi um sucesso!')
        input('\nAperte qualquer tecla para continuar...')

def useralterarusername(nome_user):
    novo_username = input('\nDigite o novo nome de usuário da sua conta: ')
    if len(novo_username) <= 20:
        cursor.execute('UPDATE Usuario SET Username = ? WHERE Username = ?', (novo_username, nome_user))
        config.commit()
        print('Nome de usuário alterado com sucesso!')
        input('\nAperte qualquer tecla para continuar')
        return novo_username
    else:
        print('ERRO: O nome de usuário não deve exceder 20 caracteres')
        input('\nAperte qualquer tecla para continuar...')
        return nome_user

def userdeletar(nome_user):
    operacao = 0
    confirm_deletar = input('\nDeseja mesmo deletar sua conta? Essa é uma ação sem volta. Digite S para continuar / Digite qualquer outra tecla para cancelar: ').lower()
    if confirm_deletar == 's':
        cursor.execute('DELETE FROM Usuario WHERE Username = ?', (nome_user,))
        config.commit()
        operacao = 1
        print('Sua conta foi deletada do sistema permanentemente.')
        input('Aperte qualquer tecla para continuar')
        return operacao
    else:
        print('Operação cancelada.')
        time.sleep(1)
        return operacao

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
