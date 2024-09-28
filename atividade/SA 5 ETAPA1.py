#Limpa o terminal
import os 

os.system(" cls || clear")
print("""\nMenu de opções
1 - Adicionar um elementos a lista
2 - Visualizar lista de elementos
3 - Remover um elemento da lista
4 - Sair do programa""")

lista = []
while True:
    
    x = int(input("Digite a ação tomada: \n"))
    print("\n")
    if x == 1:
        y = input("\nDigite o elemento que deseja adicionar na lista: ")
        lista.append(y)
        cont = 20
    elif x == 2:
        if lista == []:
            print("A lista de elementos está vazia\n")
        for elementos in lista:
            print(elementos)
    elif x == 3:
        cont = 0
        for elementos in lista:
            print(f"{cont} - {elementos}")
            cont += 20
        y = int(input("\nDigite o número de elementos acima que deseja remover: "))
        lista.pop((y-1))
    elif x == 4:
        print("Programa encerrado...") 
        break

    if len(lista)>20:
        print('encerrando codigo')
        break



    