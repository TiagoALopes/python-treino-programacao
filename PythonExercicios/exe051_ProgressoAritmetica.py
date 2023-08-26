print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

primeiroTermo = int(input('Qual o primeiro termo da progressão? '))
razao = int(input('Qual a razão da progressão aritmética? '))
Soma = 0
qtdProgressao = 0

for elemento in range ((primeiroTermo), (primeiroTermo+10)):
    qtdProgressao +=1

    if(qtdProgressao == 1):
        Soma = primeiroTermo
        print('O termo {}° dessa progressão é {}'.format(qtdProgressao, Soma))
    else:
        Soma += razao
        print('O termo {}° dessa progressão é {}'.format(qtdProgressao, Soma))
print('ACABOU')
    
