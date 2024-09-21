import os

# Limpa o Terminal.
os.system ("cls || clear")

QUANTIDADE_DE_NOTAS = 4


# Função.
def logo_senai():
    os.system ("cls || clear")
    print("=== SENAI ===")

def calcular_media(lista_notas):
# Processamento.    

    soma = sum / QUANTIDADE_DE_NOTAS
    media = soma / QUANTIDADE_DE_NOTAS
    return media

# Entrada.
# Vetor / Lista.
lista_de_notas = []

for i in range(QUANTIDADE_DE_NOTAS):
    logo_senai()# Função sem retorno.
    nota = float(input(f"Digite a{i+1}ª nota: "))
    lista_de_notas.append(nota)

media = calcular_media(lista_de_notas)# Função com retorno.

# Saída.
logo_senai()# FUnção sem retorno.
for cada_nota in  lista_de_notas:
    print(f"Nota : {cada_nota}")

print(f"Média: {media}")