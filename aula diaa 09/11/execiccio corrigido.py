import os

# Limpa o Terminal.
os.system ("cls || clear")

# Entrada

quantidade_macas = int(input("Digite a quantidade de maçãs: "))

# Processamento

if quantidade_macas < 12:
    preco_final = quantidade_macas * 1.30
else:
    preco_final = quantidade_macas * 1

# Saída
print(f"Preço final: {preco_final}")