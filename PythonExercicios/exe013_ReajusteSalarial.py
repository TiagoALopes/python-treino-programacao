valor = float(input('Qual é o salário do funcionário? R$ '))
print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, '.format(valor), end='')
print('passa a receber R$ {:.2f}'.format(valor*1.15), end='')