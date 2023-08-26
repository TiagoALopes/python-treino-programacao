from random import randint

pare = False
vitorias = 0

print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR ') 
print('=-' * 30)

while not(pare):
    numeroJogador = int(input('Diga um valor: '))
    numeroComputador = randint(0,20)
    resultado = numeroJogador + numeroComputador
    opcaoEscolhida = input('Par ou Ímpar? [P/I]: ').upper()
    if opcaoEscolhida != 'P' and opcaoEscolhida != 'I':
        print('Opção inválida, por gentileza escolher Par ou Ímpar? [P/I]')
    else:
        if(resultado % 2 == 0 and opcaoEscolhida == 'P'):
            print(f'Você me venceu! Escolhi {numeroComputador} e você {numeroJogador}! DEU PAR')
            vitorias += 1
        elif(resultado % 2 == 0 and opcaoEscolhida == 'I'):
            pare = True
            print('GAME OVER!')
            print(f'Você jogou {numeroJogador} e o computador {numeroComputador}! Total deu: {resultado} Você conseguiu me vencer {vitorias} vez')
            break