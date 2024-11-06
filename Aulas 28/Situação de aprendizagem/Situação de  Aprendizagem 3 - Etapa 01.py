# Limpa o Terminal.
import os

os.system(" cls || clear")

# Entrada de Dados.

int(input("Digite quantidade de usuários que deseja cadastrar: \n"))
print("\n")

# Menu de cadastro.

print("""\nMenu de Opções
      1 - Cadastrar Novo Usuário
      2 - Listar todos os usuários cadastrados
      3 - Sair do sistema""")

quantidadedeusuarios = []
while True:
    
    x = int(input("Digite uma ação a ser tomada: \n"))
    print("\n")
    if x == 1:
        y = input("\nDigite um usuário que você deseja cadastrar na lista: ")
        quantidadedeusuarios.append(y)
    elif x == 3:
        cont = 0
        for usuários in quantidadedeusuarios:
            print(f"{cont} - {quantidadedeusuarios}")
            y = int(input("\nDigite o número de usuários que deseja adicionar na lista: "))
            quantidadedeusuarios.pop((y-1))
    elif  x == 4:
        input("Digite uma ação a ser tomada para sair do programa:")
        print("Programa encerrado...")
        break