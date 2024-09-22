import os

# Limpa o  terminal.
os.system("cls || clear")

lista_nomes= []

# Solicitando dados
for i in range(4):
    nome = input("Digite seu um nome: ")
    lista_nomes.append(nome)

#For Each ou PARA no portugol.
for cada_nomes in lista_nomes:
    print(cada_nomes)