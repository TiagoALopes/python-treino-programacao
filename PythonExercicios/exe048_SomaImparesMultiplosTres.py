soma = 0
qtdMultiplos = 0
for multiplos in range(3, 501, 3):
    if multiplos % 2 != 0:
        qtdMultiplos += 1
        soma += multiplos
print('A soma de todos os {} múltiplos de 3 impares no range de 1 até 500 é {}'.format(qtdMultiplos, soma))