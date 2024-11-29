# Equipe
# Leandro carvalho, Sergio Almeida e Thalisson Oliveira
# Limpa o terminal
import os
os.system("cls | clear")

# Estrutura inicial de usuários (lista de dicionários)
usuarios = [
    {"nome": "Jonatas", "idade": 25},
    {"nome": "Carla", "idade": 30},
    {"nome": "Samira", "idade": 22},
]

# Função para buscar usuário pelo nome
def buscar_usuario_por_nome(usuarios, nome_buscado):
    """
    Busca um usuário pelo nome em uma lista de dicionários.
    :param usuarios: Lista contendo os usuários.
    :param nome_buscado: Nome do usuário a ser buscado.
    :return: Índice do usuário ou -1 caso não encontrado.
    """
    for i, usuario in enumerate(usuarios):
        if usuario["nome"].lower() == nome_buscado.lower():
            print(f"Usuário encontrado: Nome: {usuario['nome']}, Idade: {usuario['idade']}")
            return i  # Retorna o índice do usuário encontrado
    print("Usuário não encontrado.")
    return -1  # Retorna -1 se o usuário não for encontrado

# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("1. Listar usuários")
    print("2. Adicionar usuário")
    print("3. Excluir usuário")
    print("4. Buscar usuário pelo nome")
    print("0. Sair")

# Função principal para executar o sistema
def sistema():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nUsuários cadastrados:")
            for i, usuario in enumerate(usuarios):
                print(f"{i + 1}. Nome: {usuario['nome']}, Idade: {usuario['idade']}")

        elif opcao == "2":
            nome = input("Digite o nome do novo usuário: ")
            idade = int(input("Digite a idade do novo usuário: "))
            usuarios.append({"nome": nome, "idade": idade})
            print("Usuário adicionado com sucesso!")

        elif opcao == "3":
            nome = input("Digite o nome do usuário a ser excluído: ")
            indice = buscar_usuario_por_nome(usuarios, nome)
            if indice != -1:
                usuarios.pop(indice)
                print("Usuário excluído com sucesso!")
            else:
                print("Exclusão não realizada. Usuário não encontrado.")

        elif opcao == "4":
            nome = input("Digite o nome do usuário a ser buscado: ")
            buscar_usuario_por_nome(usuarios, nome)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Execução do sistema
sistema()
