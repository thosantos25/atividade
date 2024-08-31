Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/08/2024
Var
// Seção de Declarações das variáveis 
opcao: inteiro
prato: caracter
preco: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
 escreval("=== MENU ===")


  escreval("1 - Picanha - R$ 25,00")

   escreval("2 - Lasanha - R$ 20,00")

    escreval("3 - Strognof - 18,00")

     escreval("4 - Bife Acebolado - R$ 15,00")

      escreval("5 Pão com ovo - R$ 5,00")

       escreval("Digite a opção desejada: ")
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
               prato <- "Pão com ovo"
               preco <- 5.00
       outrocaso
              escreval("Opção inválida, ")
       fimescolha
         escreval("Prato: ", prato)
         escreval("Preço: ", preco)

  


Fimalgoritmo