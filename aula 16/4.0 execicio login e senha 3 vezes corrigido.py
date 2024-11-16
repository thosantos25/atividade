import os
os.system("cls || clear") # Limpa o terminal

# Definindo o login e senha.
login_cadastrado = "marta"
senha_cadastra = "123"
tentativas = 0

def verificar_login_e_senha(login, senha, tentativas):
    if login == login_cadastrado and senha == senha_cadastra:
           resultado = True
    else:
          resultado = False
    return resultado


# Entrada.
while True:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        tentativas += 1   
        # Processamento
        if verificar_login_e_senha(login, senha, tentativas):
              print("Acesso ao sistem!")
              break
        if tentativas >= 3:
              print("Permitido apenas 3 tentativas!")
              break