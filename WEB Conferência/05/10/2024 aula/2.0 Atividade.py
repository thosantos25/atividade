# Limpa o terminal.
import os
os.system("cls || clear")


# Criar um fila com três elmentos>
fila = ["Banana", "Maçã", "Pera"]
print("Fila: ", fila)

# Adiciona uim elemento ao final da fila.
fila.append("Uva")
print("Adicionando um elemento: ", fila)

# Remove o primeiro elemento adicionado á fila.
fila.pop(0)
print("Removendo um elemento: ", fila)
