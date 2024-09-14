import os

os.system("cls || clear")
resposta = ""
#Entrada.
idade = int(input("Digite sua idade: "))

#Processamento.
# se idade < 18 entao
# senao
#fimse
if idade < 18:
    resposta = "Menoridade"
else:
    reposta = ' Maioridade'
# Saída.
print(f"Resultado: {resposta}")
print("=== FIM ===")
