import json
import os
from datetime import datetime, date 

USERS_FILE="usuarios.json"

def carregar_usuarios():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    return {}

def salvar_usuarios(usuarios):
    with open(USERS_FILE, 'w') as file:
        json.dump(usuarios, file, indent=4)

def calcular_idade():
    nascimento = input("Forneça sua data de nascimento no formato 'dd/mm/aaaa': ")
    hoje = date.today()
    date_format = '%d/%m/%Y'  
    try:
        nascimento_convertido = datetime.strptime(nascimento, date_format).date() 
        idade = hoje.year - nascimento_convertido.year - ((hoje.month, hoje.day) < (nascimento_convertido.month, nascimento_convertido.day))
        return idade
    except ValueError:
        print("Formato de data inválido. Por favor, use o formato 'dd/mm/aaaa'.")
        return None

def cadastrar_usuario():
    usuarios=carregar_usuarios()
    nome= input("forneça o seu nome:")
    idade=calcular_idade()
    email=input("forneça o seu email no formato 'usuario@dominio.com':")

    if email in usuarios:
        print("email ja cadastrado!")
        return
    
    senha=input("digite uma senha:")

    usuarios[email]={"nome":nome,
                    "idade":idade,
                    "senha":senha}
    
    salvar_usuarios(usuarios)

def login():
        usuarios=carregar_usuarios()
        email=input("digite seu email:")
        senha=input("digite sua senha")
        if email in usuarios and usuarios[email]['senha'] == senha:
            print(f"bem vindo,{usuarios[email]['nome']}!")
        else:
            print("email ou senha incorretos. Tente novamente!")
    
def menu():
        print("digite 1 para cadastrar usuario")
        print("digite 2 para fazer login")
        print("digite 3 para sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            login()
        elif opcao == '3':
            exit()
        else:
            print("Opção inválida, tente novamente.")

menu()






