import os

os.system("cls || clear") #Limpa o terminal (|| significa ou).

#Entrado.
nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade:")) 
telefone = int(input("Digite seu Telefone:"))
cpf = input("Digite seu CPF: ")
rg = input("Digite seu RG: ")
endereço = input("Digite seu Endereço: ")
sexo = input("Digite seu Sexo(a): ")

#Saída.
print(f"Nome: ", nome)
print(f"Idade: {idade}")
print(f"Telefone: {telefone}")
print(f"CPF: {cpf}")
print(f"RG: {rg}")
print(f"Endereço: {endereço}")
print(f"Sexo: {sexo}")



