# Limpa o terminal.
import os
os.system("cls || clear")

fila = []

# Adicionando elementos na fila a partir da entrada do usuário.
for i in range(3):
    texto = input("Digite um string: ")
    fila.append(texto)
print(fila) # Saída: [str1, str2, str3]

# Removendo o elemnto mais antigo da fila
primeiro_elemento = fila.pop(0)
print(primeiro_elemento) # Saída: str1
print(fila) # Saída: [str2, str3]
