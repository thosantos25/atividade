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

while True:
        print("\nMenu:")
        print("1 - Listar todos os usuários")
        print("2 - Adicionar um novo usuário")
        print("3 - Remover um usuário")
        print("4 - Buscar usuário pelo nome")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")

# Processamento
        if opcao == "1":
            # Lógica para listar todos os usuários
            pass
        elif opcao == "2":
            # Lógica para adicionar um novo usuário
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