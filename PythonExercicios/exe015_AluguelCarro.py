diasAlugado = int(input('Quantos dias alugados? '))
kmRodados = int(input('Quantos Km rodados? '))
valorApagar = (60 * diasAlugado) + (0.15 * kmRodados)
print('O Total a pagar é de R$ {:.2f}'.format(valorApagar))