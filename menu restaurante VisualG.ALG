Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/08/2024
Var
// Se��o de Declara��es das vari�veis 
opcao: inteiro
prato: caracter
preco: real

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
 escreval("=== MENU ===")


  escreval("1 - Picanha - R$ 25,00")

   escreval("2 - Lasanha - R$ 20,00")

    escreval("3 - Strognof - 18,00")

     escreval("4 - Bife Acebolado - R$ 15,00")

      escreval("5 P�o com ovo - R$ 5,00")

       escreval("Digite a op��o desejada: ")
        leia(opcao)

       escolha opcao
              caso 1
               prato <- "Picanha"
               preco <- 25.00
              caso 2
               prato <- "Lasanha"
               preco <- 20.00
              caso 3
               prato <- "Strogonf"
               preco <- 18.00
              caso 4
               prato <- "Bife Acebolado"
               preco <- 15.00
              caso 5
               prato <- "P�o com ovo"
               preco <- 5.00
       outrocaso
              escreval("Op��o inv�lida, ")
       fimescolha
         escreval("Prato: ", prato)
         escreval("Pre�o: ", preco)

  


Fimalgoritmo