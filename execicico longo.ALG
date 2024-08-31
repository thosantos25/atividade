Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/08/2024
Var
// Seção de Declarações das variáveis 
   nome: caracter
   idade: inteiro
   n1: real
   n2: real
   n3: real
   soma: real
   media: real
   resultado: caracter
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
 escreva("Digite seu o nome do Aluno(a): ")
  leia(nome)
    escreval("Digite a idade do Aluno: ")
     leia(idade)
     escreval("Digite a primeira nota do Aluno: ")
      leia(n1)
       escreval("Digite a segunda nota do Aluno: ")
        leia(n2)
         escreval("Digite a terceira nota do Aluno: ")
          leia(n3)

          media <- (n1 + n2 + n3) /3
          se media >=7 entao
          escreval("Aprovado")
          senao
          escreval("Reprovado")
            fimse

           

         
   

Fimalgoritmo