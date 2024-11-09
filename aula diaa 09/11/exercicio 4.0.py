# Limpa o terminal
import os 
os.system("cls || clear")
def logo_senai():
    print("=== SENAI ===")
# Processamento
def preco_inflacionado(numero):
    if numero <100/1.1:
        resultado = "Número inflacionado"
    if numero >=100/1.2:
        resultado = "Numero infalcionado menor ou igual a cem"
    
    return resultado

# Entrada de dados
logo_senai()
numero = int(input("Digite um número: "))

# Chamando a função
resposta = preco_inflacionado(numero)

logo_senai()
print(f"O número: {numero} é {resposta}.")