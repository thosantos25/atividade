# Equipe
# Leandro carvalho, Sergio Almeida e Thalisson Oliveira
# Limpa o terminal
import os
os.system("cls | clear")


# Funções
def buscar_usuario_por_nome(nome, usuarios):
    for i, usuarios in enumerate(usuarios):
        if usuarios["nome"].lower() == nome.lower():  # Ignora diferenciação de maiúsculas/minúsculas
            print(f"Usuário encontrado: Nome = {usuarios['nome']}, Idade = {usuarios['idade']}")
            return i
    print("Usuário não encontrado.")
    return -1

def menu_principal():
    
    usuarios = [
        {"nome": "João", "idade": 25},
        {"nome": "Maria", "idade": 30},
        {"nome": "Pedro", "idade": 22},
        # Outros usuários
    ]

# Entrada

print("""\nMenu:
            1 - Listar todos os usuários
            2 - Adicionar um novo usuário
            3 - Remover um usuário
            4 - Buscar usuário pelo nome
            5 - Sair""")
usuarios = [
        {"nome": "João", "idade": 25},
        {"nome": "Maria", "idade": 30},
        {"nome": "Pedro", "idade": 22},
        # Outros usuários
    ]


while True:

    opcao = input("Escolha uma opção: \n")
    print("\n")

# Processamento
    if opcao == "1":
            # Lógica para listar todos os usuários
            input("Digite o número para listar usuários: ")
            usuarios.append
            pass
    elif opcao == "2":
            # Lógica para adicionar um novo usuário
            input("Digite um usuário para o cadastro: ")
            usuarios.append
            pass
    elif opcao == "3":
            # Lógica para remover um usuário
            pass
    elif opcao == "4":
            nome = input("Digite o nome do usuário a ser buscado: ")
            buscar_usuario_por_nome(nome, usuarios) # type: ignore

# Saída 

    elif opcao == "5":
        print("Saindo do sistema.")
    break
else:
    print("Opção inválida. Tente novamente.")