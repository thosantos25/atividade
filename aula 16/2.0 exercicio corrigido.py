import os 
os.system("cls || clear")
# limpa o terminal

# Fefatore este código para uso com uma função.
# Inicializando variáveis.
notas = 0 
QUANTIDADE_NOTAS = 4

def calcular_media(notas, quantidade_notas):
        media = notas / quantidade_notas
        return media

# ENTRADA
for i in range(QUANTIDADE_NOTAS):
        notas += float(input("Digite uma nota: "))

# Processamento
media = calcular_media(notas, QUANTIDADE_NOTAS)

# Saída 
print(f"Média: {media}")
