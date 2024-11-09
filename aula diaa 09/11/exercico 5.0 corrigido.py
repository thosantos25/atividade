import os
os.system("cls | clear")

# Funções
def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    resultado_media = soma / 2
    return resultado_media

def mostrar_resultado(media_informanda):
    if media < 7:
        resposta = "Reprovado"
    else:
        resposta = "Aprovado "
    return resposta        

# Entrada
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

# Processamento
media = calcular_media(primeira_nota, segunda_nota)
resultado  = mostrar_resultado(media)

# Saída
print(f"Média: {media}")
print(f"Situação do Aluno: {resultado}")