# Limpa  o terminal
import os
os.system ("cls || clear")
# Entada de dados

numero = float(input("Digite um número para saber se é par ou impar: "))
resto = numero % 2

# Saída
if resto == 0:
    print("Número é par")
else:
    print("Número é impar")