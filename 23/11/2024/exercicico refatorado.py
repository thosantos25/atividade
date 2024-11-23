# Limpa o terminal.
import os
os.system("cls || clear")

#vetor_notas = []
#for i in range (4):
 #   nota = float(input("Digite uma nota: "))
  #  vetor_notas.append(nota)


#for cada_notas in vetor_notas :
 #   print(cada_notas)    

# Função

def calcular_media(notas):
    return sum(notas) / len(notas)

lista_notas = [] # Lista

# Entrada
while True:
    nota = float(input("Digite a {i+ª} nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida!")
        continue
    else:
        lista_notas.append(nota)
        break

# Processamento
media = calcular_media(lista_notas)

# Saída
for nota in lista_notas: # Foreach
        print(f"Nota: {nota}")

print(f"Média: {media}")