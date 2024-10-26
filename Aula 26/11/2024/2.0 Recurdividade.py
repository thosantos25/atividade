# Implemente um algoritimo que, usando recursividade,
# receba um número como parâmetro e some todos números
# de zero até o número informado. 

import os
import time
os.system("cls || clear")

def somar_numero(numero): 
    if numero == 0:
         return 0
    else: 
         print(f"{numero} + {numero -1}")
         return numero + somar_numero(numero -1)
numero = int(input("Digite um número para soma: "))    
print(f"Soma: {somar_numero(numero)}")