tuplaLanche = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
parada = ''

while parada != 99:
    x = int(input('Digite um Número para ver seu valor por extenso entre [0 a 10]:'))
    if(x < 0 or x > 10):
        print('\nPor gentileza, informar um valor entre [1 a 10].')
    else:
        print(f'\nO número por extenso é: {tuplaLanche[x]}')
    print('Pressione [ X ] caso dejese encerrar o aplicativo.')