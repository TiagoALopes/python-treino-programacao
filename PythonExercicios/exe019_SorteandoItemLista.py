from random import randint, choice
primeiroAluno = input('Digite o primeiro aluno: ')
segundoAluno = input('Digite o segundo aluno: ')
terceiroAluno = input('Digite o terceiro aluno: ')
quartoAluno = input('Digite o quarto aluno: ')

lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
valor = randint(0, 3)
escolhido = choice(lista)

print('O aluno escolhido foi: {}'.format(lista[valor]))
print('O aluno escolhido foi: {}'.format(escolhido))