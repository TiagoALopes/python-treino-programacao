print('Digite um número para ', end = '')
valor = int(input('calcular seu Fatorial: '))
print('Calculando {}! '.format(valor), end = '')
aux = valor
fatorial = 1
valorFatorial = ""

while aux >= 0:
    fatorial *= aux
    aux += -1
print('= {} = {}'.format(fatorial, fatorial))