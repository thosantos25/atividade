# Limpa o terminal.
import os
os.system("cls || clear")

"""

Solicite ao usuário 4 notas mostre as notas ao final.
"""
QUANTIDADE_DE_NOTAS = 4
lista_notas = [] #lista

def calcular_media(primeira_nota, segunda_nota, terceira_nota, quarta_nota):
    soma = primeira_nota + segunda_nota + terceira_nota + quarta_nota
    resultado_media = soma / 4
    return resultado_media

# Entrada

#for i in range(QUANTIDADE_DE_NOTAS): # Laço de repetição
#    nota = float(input("Digite uma nota: "))
#    lista_notas.append(nota)


primeira_nota = float(input("Digite primeira nota: "))
segunda_nota = float(input("Digite primeira nota: "))
terceira_nota = float(input("Digite primeira nota: "))
quarta_nota = float(input("Digite primeira nota: "))

# Processamento
media = calcular_media (primeira_nota, segunda_nota, terceira_nota, quarta_nota)

# Saída
#for nota in lista_notas: # Foreach
    #print(f"Nota: {nota}")

print(f"Média: {media}")

#print(f"Nota: {primeira_nota}")
#print(f"Nota:{segunda_nota}")
#print(f"Nota: {terceira_nota}")
#print(f"Nota: {quarta_nota}")