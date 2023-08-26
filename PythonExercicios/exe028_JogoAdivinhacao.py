from random import randint
from time import sleep

numeroInserido = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
numeroPensado = randint(0,5)
if(numeroInserido == numeroPensado):
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(numeroPensado, numeroInserido))