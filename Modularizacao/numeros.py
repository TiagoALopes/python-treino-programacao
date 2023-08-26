#Conceito de Pacotes Python iguais a de bibliotecas do Java.
from uteis.numeros import __init__operacoes
#from uteis import fatorial, dobro -- NÃO RECOMENDADO.
from math import sqrt

num = int(input('Digite um valor: '))
fat = __init__operacoes.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {__init__operacoes.dobro(num)}')
print(f'A raiz quadrada de {num} é {sqrt(num)}')