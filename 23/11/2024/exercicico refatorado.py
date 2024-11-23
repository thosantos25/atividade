# Limpa o terminal.
import os
os.system("cls || clear")

# Função

def calcular_media(notas):
    return sum(notas) / len(notas)

lista_notas = [] # Lista

# Entrada
while True:
    nota = float(input("Digite um nota: "))
    if nota <0:
        break
    else:
        lista_notas.append(nota)

# Processamento
media = calcular_media(lista_notas)

# Saída
for nota in lista_notas: # Foreach
    print(f"Nota: {nota}")

print(f"Média: {media}")