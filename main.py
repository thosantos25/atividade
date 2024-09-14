#Funçao mostrar menu usuario
def mostrar_menu():
    print("Menu de Opçãoes: ")
    print(" 1 - Cadastar Usuário: ")
    print(" 2 - Listar Todos Usuário do Cadastrados")
    print(" 3 - Sair")
    
#Função para cadastro do usuarios
def cadastra_usuario(usuarios):
    nome = input("digite o nome do usuário: ") #declarando variavel para receber o nome
    idade = input("digite a idade do usuário")#declarando variavel para receber idade
    email= input("digite seu E-mail")#declatando variavel para receber email
     
     usuarios = {"nome":nome, "idade":idade, "email":email} #usuario cadastrado
     usuarios.append(usuarios) #adicionado usuario cadastrado no final da lista
     print("Usuário Cadastrado com Sucesso")  #mostra mensagem de concluido
     
     def listar_usuarios(usuarios):
         if len(usuarios) == 0:
             print("Nenhum Uriario Cadastrado") #Logice se
                                                #mostra na tela
                                                #SENAO
 else
   print("Mostar Lista de Usuarios")
              #Estrutura de Repetição
  for i, usuarios in enumerate(usuario, start=1):
                  print(f"Usuário: ", {i}) #Mostar na tela posição de cadastro
                  print(f"nome : {usuarios[nome]} ")
                  print(f"idade : {usuarios[idade]} ")
                  print(f"email : {usuarios[email]} ")
 
 
              
             