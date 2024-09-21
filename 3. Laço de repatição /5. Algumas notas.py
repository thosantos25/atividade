import os

# Limpa o  terminal.
os.system("cls || clear")

#nota1 = float(input("Digite uma nota: "))
#nota2 = float(input("Digite uma nota: "))
#nota3 = float(input("Digite uma nota: "))
#nota4 = float(input("Digite uma nota: "))
#nota5 = float(input("Digite uma nota: "))

while True:
    nota = float(input("Digite uma nota: "))

    if nota < 0:
        break