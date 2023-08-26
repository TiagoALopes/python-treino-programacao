numero = 9999
contador = 0
soma = 0

while numero > 0:
    print('-' * 30)
    numero = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 12)
    if numero < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    else:
        
        for multi in range(0,11):
            print(f'{numero} X {multi:2} = {(numero*multi)}')