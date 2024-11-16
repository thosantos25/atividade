import os 
os.system("cls || clear")
# limpa o terminal

"""Refatore: 
    1 - Crie um função para verificar se está aprovado.
    - Conidere média maior ou igual a 7,0 para aprovação
    - caso contrário, reprovado
        
    2 - Use um lista para armazenar notas.
    """

# Inicializando variáveis.
notas = [] # Lista 
QUANTIDADE_NOTAS = 4

def calcular_media(notas, quantidade_notas):
        media = sum(notas) / quantidade_notas
        return media

def verificar_aprovacao(media):
        if QUANTIDADE_NOTAS >= 7:
                resultado = "Reprovado"
        else:
                resultado = "Aprovado"
        return resultado

# ENTRADA
for i in range(QUANTIDADE_NOTAS):
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
# Processamento
media = calcular_media(notas, QUANTIDADE_NOTAS)
resultado = verificar_aprovacao(media)

# Saída 
print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")