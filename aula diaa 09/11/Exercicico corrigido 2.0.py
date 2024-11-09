import os

# Limpa o Terminal.
os.system ("cls || clear")

# Entrada
valor = int(input("Digite um número: "))

# Processamento
desconto = valor * 0.1
valor_com_desconto = valor - desconto

# Saída
print(F"Valor com desconto: {valor_com_desconto}")
