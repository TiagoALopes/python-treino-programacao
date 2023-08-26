from uteis.numeros import moeda

continua = True
while continua:
    try:
        p = float(input('Digite o preço: R$'))
        continua = False
        print(f'A metade de R${p:.2f} é {moeda.metade(p)}')
        print(f'O dobro de R${p:.2f} é {moeda.dobro(p)}')
        print(f'Aumentando 10%, temos {moeda.aumentar(p, 10):.2f}')
        print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13):.2f}')
        if continua:
            break
    except(Exception):
        print('Por gentileza informar um valor válido.')
    
