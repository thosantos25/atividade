import os 
os.system("cls || clear") # LImpa terminal

# Inicializando variáveis
while True:
    nota = float(input("Digite uma nota: "))

    #procesamneto
    if nota >= 0 or nota <=10:
        # Saída
        print(F"Nota: {nota}")
        break