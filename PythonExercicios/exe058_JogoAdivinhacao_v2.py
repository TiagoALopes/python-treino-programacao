from random import randint
from time import sleep

numeroPensado = randint(0,10)
numeroInserido = -1
qtdTentativa = 0

while numeroInserido != numeroPensado:
    numeroInserido = int(input('Em que número eu pensei? '))
    qtdTentativa += 1
    print('PROCESSANDO...')
    sleep(0.5)
    if(numeroInserido == numeroPensado):
        print('Parabéns Você acertou! Eu pensei no número {}, você precisou de {} tentativas!'.format(numeroPensado, qtdTentativa))
    else:
        print('Este não é o número que pensei! tente novamente...')