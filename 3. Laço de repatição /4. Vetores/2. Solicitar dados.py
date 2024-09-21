import os

# Limpa o  terminal.
os.system("cls || clear")

# Solicitar dados para o usúario.
#notas = []

#notas[o] = float(input(" Digite um nota: "))
#notas[1] = float(input(" Digite um nota: "))
#notas[2] = float(input(" Digite um nota: "))

# Exibir os dados.
#print(notas[0])
#print(notas[1])
#print(notas[2])

vetor_notas = []
for i in range(3):
    notas = float(input("Digite uma nota: "))
    vetor_notas.append(notas)

# For Each. Ou PARA
for cada_notas in vetor_notas:
    print(cada_notas)
