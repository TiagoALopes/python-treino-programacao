from random import random, randint
from math import sqrt, ceil
import emoji

numAleatorio = random();
print(numAleatorio)
numAleatorioInt = randint(1, 100);
print(numAleatorioInt)
##print(emoji.emojize('Olá Mundo :sunglasses:'))
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A Raiz quadarada é: {:.2f}'.format(raiz))