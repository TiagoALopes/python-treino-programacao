media = 0
somaIdade = 0
idadeMaisVelho = 0
nomeMaisVelho = ''
qtdMulheresMenores = 0

for pessoa in range(1, 5):
    print('-'*5, end='')
    print('{}° PESSOA'.format(pessoa), end='')
    print('-'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper
    somaIdade += idade
    if idade > idadeMaisVelho and sexo == 'M':
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    elif sexo == 'F' and idade < 20:
        qtdMulheresMenores += 1
        
media = somaIdade / 4
print('\nA média de idade dos grupo é de {:.1f}'.format(media))
if idadeMaisVelho != 0:
    print('O Homem mais velho tem {} anos e se chama {}.'.format(idadeMaisVelho, nomeMaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(qtdMulheresMenores))