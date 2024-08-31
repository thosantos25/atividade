Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/08/2024
Var
// Seção de Declarações das variáveis 
  primeiro_numero: real
  segundo_numero: real
  resultado: real
  operacao: caracter

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
   escreva("Digite o primeiro numero: ")
    leia(primeiro_numero)
    
    escreva("Digite o Segundao numero: ")
    leia(segundo_numero)
    escreva("Digite a Operação desejada: ")
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
                escreval("Opção Válida")
fimescolha

escreval("Resultado : ", Resultado)
    

Fimalgoritmo