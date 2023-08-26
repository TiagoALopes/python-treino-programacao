real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real/4.97
euro = real/5.40
print('Com R$ {:.2f} você consegue comprar: U$ {:.2f} e € {:.2f}'.format(real , dolar, euro))