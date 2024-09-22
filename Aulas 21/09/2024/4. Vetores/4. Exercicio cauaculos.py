import os

# Limpa o Terminal.
os.system ("cls || clear")

# Funções.
def calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2):
    
    soma = QUANTIDADE_DE_NÚMERO1 + QUANTIDADE_DE_NÚMERO2
    
    return soma

def calcular_subtracao(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2):
    
    subtracao = QUANTIDADE_DE_NÚMERO1 - QUANTIDADE_DE_NÚMERO2
    
    return subtracao

def calcular_multiplicacao(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2):    
  
    multiplicacao = QUANTIDADE_DE_NÚMERO1 * QUANTIDADE_DE_NÚMERO2
    
    return multiplicacao

def calcular_divisao(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2):
    
    divisao = QUANTIDADE_DE_NÚMERO1 / QUANTIDADE_DE_NÚMERO2
    
    return divisao


QUANTIDADE_DE_NÚMERO1 = int(input("Dgite o primeiro número: "))

QUANTIDADE_DE_NÚMERO2 = int(input("Dgite o primeiro número: "))

# Entrada
soma = calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)

#Processamento
soma = calcular_soma(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)
subtracao = calcular_subtracao(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)
multiplicacao = calcular_multiplicacao(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)
divisao = calcular_divisao(QUANTIDADE_DE_NÚMERO1, QUANTIDADE_DE_NÚMERO2)

# Saída.
print(f"Soma: {soma}")
print(f"Subtraçao: {subtracao}")
print(f"multiplicacao: {multiplicacao}")
print(f"divisão: {divisao}")