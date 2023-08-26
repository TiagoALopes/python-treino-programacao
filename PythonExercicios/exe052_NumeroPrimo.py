numero = int(input('Digite um número: '))
qtdMultiplos = 0

for c in range(1, numero+1):
    if numero % c == 0:
        print('\33[34m', end = '')
        qtdMultiplos += 1
    else:
        print('\33[m', end = '')
    print('{} '.format(c), end = '')

if qtdMultiplos == 2:
    print('O número {} foi divisível por {} números'.format(numero, qtdMultiplos))
    print('Por isso é PRIMO!')
else:
    print('O número {} foi divisível por {} números'.format(numero, qtdMultiplos))
    print('por isso NÃO É PRIMO!')