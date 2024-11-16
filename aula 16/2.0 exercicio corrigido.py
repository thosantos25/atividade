import os 
os.system("cls || clear")
# limpa o terminal

# Inicializando variáveis.
notas = 0 
QUANTIDADE_NOTAS = 4
# ENTRADA
for i in range(QUANTIDADE_NOTAS):
    notas += float(input("Digite uma nota: "))

# Processamento
media = notas / QUANTIDADE_NOTAS

# Saída 
print(f"Média: {media}")