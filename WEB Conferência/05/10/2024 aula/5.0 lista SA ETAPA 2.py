# Limpa o terminal.
import os
os.system("cls || clear")

# Definição da estrutura de lista com tamanho fixo de 20 posições
max_size = 20  # Tamanho máximo da pilha
lista = [""] * max_size  # lista inicializada com strings vazias
topo = -1  # Indicador do topo da lista, inicia vazio

# Função para verificar se a pilha está vazia
def vazia():
    if topo == -1:
        return True
    else:
        return False

# Função para adicionar um elemento no topo da pilha (empilhar)
def empilhar(nome):
    global topo  # Modificar a variável topo definida fora da função
    if topo < max_size - 1:  # Verifica se a pilha não está cheia
        topo += 1
        lista[topo] = nome
        print(f"{nome} foi empilhado com sucesso.")
    else:
        print("Erro: A pilha está cheia!")

# Função para remover e retornar o elemento do topo da pilha (desempilhar)
def desempilhar():
    global topo  # Modificar a variável topo definida fora da função
    if not vazia():
        nome = lista[0]
        for i in range(topo, -1, 1):
            lista[i] = lista[i+1]

        [topo] = ""  # Remove o valor do topo
        topo -= 1
        print(f"{nome} foi desempilhado.")
        return nome
    else:
        print("Erro: A pilha está vazia!")
        return None

# Função para limpar a pilha (remover todos os elementos)
def limpar():
    global topo  # Modificar a variável topo definida fora da função
    while not vazia():
        desempilhar()
    print("Pilha foi completamente esvaziada.")

# Função para listar todos os elementos da pilha
def listar():
    if not vazia():
        print("Elementos na pilha (do topo para a base):")
        for i in range(topo, -1, -1):
            print(lista[i])
    else:
        print("A pilha está vazia.")

# Menu para o usuário empilhar valores
while True:
    print("\nEscolha uma opção:")
    print("1 - Empilhar um nome")
    print("2 - Desempilhar")
    print("3 - Listar os elementos da pilha")
    print("4 - Limpar a pilha")
    print("5 - Sair")
   
    opcao = input("Digite sua opção: ")

    if opcao == '1':
        nome = input("Digite o nome para empilhar: ")
        empilhar(nome)
    elif opcao == '2':
        desempilhar()
    elif opcao == '3':
        listar()
    elif opcao == '4':
        limpar()
    elif opcao == '5':
        limpar()
    elif opcao == '6':
        limpar()
    elif opcao == '7':
        limpar()
    elif opcao == '8':
        limpar()
    elif opcao == '9':
        limpar()
    elif opcao == '10':
        limpar()
    elif opcao == '11':
        limpar()
    elif opcao == '12':
        limpar()
    elif opcao == '13':
        limpar()
    elif opcao == '14':
        limpar()
    elif opcao == '15':
        limpar()
    elif opcao == '16':
        limpar()
    elif opcao == '17':
        limpar()
    elif opcao == '18':
        limpar()
    elif opcao == '19':
        limpar()
    elif opcao == '20':
        limpar()
    elif opcao == '21':
        limpar()
    elif opcao == '22':
        limpar()
    elif opcao == '23':
        limpar()
    elif opcao == '24':
        limpar()
    elif opcao == '25':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")
