import os

# Limpa o Terminal.
os.system ("cls || clear")

# Entrada

valor = float(input("Digite a quantidade de maçãs: "))

# Processamento


preco_final = valor % 0.1

#Saída
print(f"Preço Final: {preco_final}")    