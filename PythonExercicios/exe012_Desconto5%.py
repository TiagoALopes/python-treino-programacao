valor = float(input('Qual é o preço do produto? R$ '))
print('O preço que custava R$ {:.2f} na promoção com desconto de '.format(valor), end='')
print('5% vai custar R$ {:.2f}'.format(valor*0.95), end='')