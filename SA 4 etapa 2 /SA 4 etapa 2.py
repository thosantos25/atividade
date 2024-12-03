# Equipe
# Leandro carvalho, Sergio Almeida e Thalisson Oliveira
# Limpa o terminal
import os
os.system("cls | clear")


# Lista para armazenar os usuários
usuarios = []

# Função para buscar o índice de um usuário pelo nome
def buscar_usuario_por_nome(nome):
    for i, usuario in enumerate(usuarios):
        if usuario["nome"] == nome:
            return i  # Retorna o índice do usuário encontrado
    return -1  # Retorna -1 se não encontrar

# Função para remover um usuário pelo índice
def remover_usuario_por_indice(indice):
    if 0 <= indice < len(usuarios):
        # Remove o usuário deslocando os itens seguintes uma posição para trás
        del usuarios[indice]  # O Python já reordena a lista automaticamente
        print("Usuário removido com sucesso!")
    else:
        print("Índice inválido.")

# Função para remover um usuário pelo nome
def remover_usuario():
    nome = input("Digite o nome do usuário a ser removido: ")
    indice = buscar_usuario_por_nome(nome)
    if indice == -1:
        print("Usuário não encontrado.")
    else:
        remover_usuario_por_indice(indice)

# Função para listar todos os usuários
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("Usuários cadastrados:")
        for i, usuario in enumerate(usuarios):
            print(f"{i + 1}. Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")

# Função para adicionar um novo usuário
def adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    email = input("Digite o email do usuário: ")
    usuarios.append({"nome": nome, "idade": idade, "email": email})
    print("Usuário adicionado com sucesso!")

# Menu principal
def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Remover usuário")
        print("4 - Buscar usário pelo nome")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "4":
            nome = input("Digite o nome do usuário para buscar: ")
            indice = buscar_usuario_por_nome(nome)
            if indice == -1:
                print("Usuário não encontrado.")
            else:
                usuario = usuarios[indice]
                print(f"Usuário encontrado: Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
        elif opcao == "3":
            remover_usuario()
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
