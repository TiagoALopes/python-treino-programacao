from random import shuffle
primeiroAluno = input('Digite o primeiro aluno: ')
segundoAluno = input('Digite o segundo aluno: ')
terceiroAluno = input('Digite o terceiro aluno: ')
quartoAluno = input('Digite o quarto aluno: ')
lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
shuffle(lista)
print('A Ordem de apresentação será: {}'.format(lista))
