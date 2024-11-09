import os

# Função sem retorno
def logo_senai():
    os.system("cls || clear")
    print("=== SENAI ===")

# Função com retorno
def notas_do_aluno(media_do_aluno):
    if notas_do_aluno > 7:
        media_do_aluno = "Aluno tirou nota maior que 7 aprovado"
    if notas_do_aluno < 7:
        media_do_aluno = "Aluno tirou nota menor que 7 reprovado"
    else:
        media_do_aluno = notas_do_aluno / 2
        media_do_aluno = "Média do aluno"

    return media_do_aluno

# Entrada.
logo_senai()
notas_do_aluno = float(input("Digite primeira nota: "))
notas_do_aluno = float(input("Digite primeira nota: "))
media_do_aluno = float(input("Digite o valor da media escolar: "))
#Processamento
resultado = media_do_aluno(notas_do_aluno)

#Saída 
print(f"A média{notas_do_aluno}: ")
