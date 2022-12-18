
from cryptography.fernet import Fernet

def gerar_key(): 
    key = Fernet.generate_key()
    with open("chave.key" , "wb") as key_file:
        key_file.write(key)


def carregar_key():
    arq = open("chave.key" , "rb")
    key = arq.read()
    arq.close()
    return key


key = carregar_key()
fer = Fernet(key)

def visu():
    with open('senhas.txt' , 'r') as f:
        for li in f.readlines():
            data = li.rstrip()
            usuario , senha = data.split("|")
            print("Usuario: " , usuario , "| Senha: " , fer.decrypt(senha.encode()).decode())

def add():
    usuario = input('Seu nome -- ')
    novaSenha = input('Sua nova senha -- ')

    #With fechara automaticamente depois que o processo seja feito, ira abrir ler e adicionar no final do arquvio TXT
    with open('senhas.txt' , 'a') as f:
        f.write(usuario + ' | ' + fer.encrypt(novaSenha.encode()).decode() + '\n')


escolha = input('Oque voce deseja - (Visu | Add ) sua senha ?? -- Fechar programa - ( q ) ').lower()


if escolha == 'q':
    quit()


if escolha == 'visu':
    visu()
elif escolha == 'add':
    add()
else:
    print('Escolha invalida !')