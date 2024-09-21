import os

# Limpa o Terminal.
os.system ("cls || clear")

# Funções.
def calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2):
    
    soma = QUANTIDADE_DE_NÚMERO1 + QUANTIDADE_DE_NÚMERO2
    subtracao = QUANTIDADE_DE_NÚMERO1 - QUANTIDADE_DE_NÚMERO2
    mutiplicacao = QUANTIDADE_DE_NÚMERO1 * QUANTIDADE_DE_NÚMERO2
    divisao = QUANTIDADE_DE_NÚMERO1 / QUANTIDADE_DE_NÚMERO2
    return soma
    return subtracao
    return mutiplicacao
    return divisao

QUANTIDADE_DE_NÚMERO1 = int(input("Dgite o primeiro número: "))
QUANTIDADE_DE_NÚMERO2 = int(input("Dgite o primeiro número: "))

# Entrada
soma = calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)

#Processamento
soma = calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)
subtracao = calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)
multiplicacao = calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)
divisao = calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)

# Saída.
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"mutiplicacao: {multiplicacao}")
print(f"divisao: {divisao}")