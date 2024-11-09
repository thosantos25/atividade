import os
os.system("cls || clear")

print("=== SENAI ===")
#Processamento

def par_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")
        
#Entrada de dados

print("== Solicitando dados ==")
numero = int(input("Digite um número: "))

# Chamada a função
par_impar(numero)