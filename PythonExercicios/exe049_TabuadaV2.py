valor = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for multi in range(0,11):
    print('{} X {:2} = {}'.format(valor, multi, (valor*multi)))
print('-' * 12)