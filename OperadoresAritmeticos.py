n1 = float(input('Insira um Valor: '))
n2 = float(input('Insira outro Valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
potencia = pow(n1,n2)
raizQuadrada = n1**(1/2)
print('Soma é {}, o produto é {}, a divisão é {}'.format(soma, multiplicacao, divisao), end=',') #\n quebrar a linha
print(' Potência: {}'.format(potencia), end=',')
print(' Raiz Quadrada 1° número: {}'.format(raizQuadrada))

#print(81**(1/2)) #Raiz Quadrada
#print() #Raiz Quadrada
#print(127**(1/3)) #Raiz Cúbico
