import os

# Limpa o Terminal.
os.system ("cls || clear")

# Função.
def logo_senai():
    os.system ("cls || clear")
    print("=== SENAI ===")


# Entrada.
# COSNTANTE.
QUANTIDADE_DE_NOTAS = 4
# Vetor / Lista.
lista_notas = []

for i in range(QUANTIDADE_DE_NOTAS):
    logo_senai()# Função sem retorno.
    nota = float(input(f"Digite a{i+1}ª nota: "))
    lista_notas.append(nota)

# Processamento.
soma = sum(lista_notas)# Função com retorno.
media = soma / QUANTIDADE_DE_NOTAS

# Saída.
logo_senai()
for cada_nota in  lista_notas:
    print(f"Nota : {cada_nota}")

print(f"Média: {media}")