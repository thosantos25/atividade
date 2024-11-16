import os
os.system("cls || clear") # Limpa o terminal

# Definindo o login e a senha corretos
login_correto = "usuario123"
senha_correta = "senhaSegura"

# Número máximo de tentativas
max_tentativas = 3
tentativas = 0

# Iniciar o loop para pedir o login e a senha até que estejam corretos ou até atingir o limite de tentativas
while tentativas < max_tentativas:
    # Solicitar o login e a senha do usuário
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    
    # Verificar se o login e a senha estão corretos
    if login == login_correto and senha == senha_correta:
        print("Login e senha corretos! Acesso permitido.")
        break  # Sai do loop, já que o login e a senha estão corretos
    else:
        tentativas += 1
        if tentativas < max_tentativas:
            print(f"Login ou senha incorretos. Você tem {max_tentativas - tentativas} tentativas restantes.")
        else:
            print("Número de tentativas excedido. Acesso bloqueado.")
            exit()  # Finaliza o programa

