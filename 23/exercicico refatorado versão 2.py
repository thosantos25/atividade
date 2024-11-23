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

def maior_nota(notas):
      return sum(notas / len(notas))

def maior_nota(notas):
      return min(notas)

def ordem_crescente(notas):
      return notas.sort()

def ordem_decescente(notas):
      return notas.short(reversed=True)

QUANTIDADE_DE_NOTAS = [4]
lista_notas = [] 
lista_ordem_crescente = []
lista_ordem_decrescente = []  

# Entrada
for i in range(QUANTIDADE_DE_NOTAS):
    while True:
            nota = float(input("Digite a {i+ª} nota: "))
            if nota >= 0 and nota <= 10:
                lista_notas.append(nota)
                break
            else:
                continue
    
# Processamento
media = calcular_media(lista_notas)

# Saída
for nota in lista_notas: # Foreach
        print(f"Nota: {nota}")

print(f"Média: {media}")