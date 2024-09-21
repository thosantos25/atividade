import os

# Limpa o  terminal.
os.system("cls || clear")

lista_nomes= []

# Solicitando dados
for i in range(4):
    nome = input(f"Digite o {i+1}º nome: ")
    lista_nomes.append(nome)

#For Each ou PARA no portugol.
for i, cada_nomes in enumerate(lista_nomes, start=1):
    print(f"{i}º nome: {cada_nomes}")