Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/08/2024
Var
// Se��o de Declara��es das vari�veis 
  primeiro_numero: real
  segundo_numero: real
  resultado: real
  operacao: caracter

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
   escreva("Digite o primeiro numero: ")
    leia(primeiro_numero)
    
    escreva("Digite o Segundao numero: ")
    leia(segundo_numero)
    escreva("Digite a Opera��o desejada: ")
    leia(operacao)
    
    escolha operacao
            caso "+"
                resultado <- primeiro_numero + segundo_numero
            caso "-"
                resultado <- primeiro_numero - segundo_numero
            caso "*"
                resultado <- primeiro_numero * segundo_numero
            caso "/"
                resultado <- primeiro_numero / segundo_numero
                outrocaso
                escreval("Op��o V�lida")
fimescolha

escreval("Resultado : ", Resultado)
    

Fimalgoritmo