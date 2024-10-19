# Limpa Terminal.
import os
os.system(" cls || clear")

# Embarlha
lista = [1, 3, 12, 8, 2]
lista.pop()
print(lista)

#Apaga
lista = [1, 3, 12, 8, 2]
lista.pop(2)
print(lista)

lista = [1, 3, 12, 8, 2, 2]
print(lista)
lista.remove(2)
print(lista)
print(lista)

lista = [1, 3, 12, 8, 2, 2]
print(lista)
del lista[2]
print(lista)

lista = [1, 2, 12 ,8, 2, 2]
del lista