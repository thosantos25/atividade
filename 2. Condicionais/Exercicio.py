import os

os.system("cls || clear")

resultado = 0

#Entrada.
primeiro_numero = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada (+ - / *): ")
segundo_numero = float(input("Digite o segundo número: "))

#Processamento.
if operacao == "+":
    resultado == primeiro_numero + segundo_numero
elif operacao == "-":
    resultado = primeiro_numero - segundo_numero
elif operacao == "*":
    resultado == primeiro_numero * segundo_numero
elif operacao == "/":
    resultado = primeiro_numero / segundo_numero
else:                 
    print("Opção inválida.")
        
#Saída
print(f"Resultado: {resultado}")
