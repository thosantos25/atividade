import os
import time
os.system("cls || clear")

def contagem_regressiva(numero):
    if numero < 0:
        return
    print(numero)
    time.sleep(2)
    contagem_regressiva(numero - 1) # chamada recursiva.


# Código principal
numero = int(input("Digite um número para contagem regressiva: "))

print("Contagem regressiva...")
contagem_regressiva(5)    # Chamada da função.
print("=== FIM ===")



# Entrada 
# Processamento
# Saída