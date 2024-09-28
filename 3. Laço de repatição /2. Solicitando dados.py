import os

os.system("cls || clear")

# Entrada de dados.
numero = int(input("digite um número: "))

for i in range(1,6):
    print(f"{numero} x {i} = {numero * i}")