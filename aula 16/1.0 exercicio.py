# Limpa o terminal.
import os
os.system("cls || clear")

# Entrada de dados.
numero = int(input("Digite um número: "))

# Processamento.
for i in range (1,16,2):
    if i % 2 == 1:
        print(i)
