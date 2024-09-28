#Limpa o Terminal
import os

os.system("cls || clear")

lista = []
while True:
    print("""\nMenu de opções
1 - Adicionar um livro a lista
2 - Visualizar lista de livros
3 - Remover um livro da lista
4 - Sair do programa""")
    
    x = int(input("Digite a ação tomada: \n"))
    print("\n")
    if x == 1:
        y = input("\nDigite o livro que deseja adicionar na lista: ")
        lista.append(y)
    elif x == 2:
        if lista == []:
            print("A lista de livros está vazia\n")
        for livros in lista:
            print(livros)
    elif x == 3:
        cont = 1
        for livros in lista:
            print(f"{cont} - {livros}")
            cont += 1
        y = int(input("\nDigite o número do livro acima que deseja remover: "))
        lista.pop((y-1))
    elif x == 4:
        print("Programa encerrado...") 
        break