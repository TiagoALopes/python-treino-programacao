from time import sleep

opcao = 99998
primeiro = 0
segundo = 0

while opcao != 5:
    sleep(3)
    print('\n' + '-'*20, end='')
    print('Menu de Opções', end='')
    print('-'*20)
    if opcao == 99998:
        primeiro = float(input('Primeiro Valor: '))
        segundo = float(input('Segundo Valor: '))
    opcao = int(input(('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair
Opção desejada: ''')))
    if (opcao == 1):
        print('\nA Soma de {} + {} = {}'.format(primeiro, segundo, (primeiro + segundo)))
    elif (opcao == 2):
        print('\nO Produto de {} + {} = {}'.format(primeiro, segundo, (primeiro * segundo)))
    elif (opcao == 3):
        if (primeiro > segundo):
            print('\nO Maior número entre {} e {} é {}'.format(primeiro, segundo, primeiro))
        else:
            print('\nO Maior número entre {} e {} é {}'.format(primeiro, segundo, segundo))
    elif opcao == 4:
        primeiro = float(input('Primeiro Valor: '))
        segundo = float(input('Segundo Valor: '))
    elif opcao == 5:
        print('Até Logo...')
    else:
        print('\nPor gentileza informar um valor válido!')