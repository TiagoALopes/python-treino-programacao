print('Por gentileza, inserir o ano de nascimento das sete pessoas?\n')
pessoa = []
maiorPeso = 0
menorPeso = 999

for c in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))

    if peso > maiorPeso:
        maiorPeso = peso
    
    if peso < menorPeso:
        menorPeso = peso

print('\nO maior peso lido foi de {:.1f}Kg'.format(maiorPeso))
print('O menor peso lido foi de {:.1f}Kg'.format(menorPeso))