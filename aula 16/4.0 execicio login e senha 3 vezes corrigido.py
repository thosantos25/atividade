import os
os.system("cls || clear") # Limpa o terminal

# Definindo o login e senha.
login_cadastrado = "marta"
senha_cadastra = "123"
tentativas = 0

# Entrada.
while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    tentativas += 1
    
    # Processamento
    if login == login_cadastrado and senha_cadastra:
        print("Acesso ao sistema!")
        break
    
    if tentativas >= 3:
        print("Permitido  anpenas 3 tentativas!")
        break