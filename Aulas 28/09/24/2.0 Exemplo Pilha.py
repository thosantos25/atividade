#Limpa o Terminal
import os

os.system("cls || clear")

#Escrinta do Algaritimo.

stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print("Elementos inseridos na satack foram")
print(stack)

print("Excluir elementos da stack")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("Stack atual")
print(stack)