from random import randint

componentesJogo = ['PEDRA', 'PAPEL', 'TESOURA']
escolhaCOM = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL      
[ 2 ] TESOURA
''')
escolhaJogador = int(input('Qual é a sua jogada? '))

if (escolhaJogador < 0 or escolhaJogador > 2):
    print('Por gentileza, informar uma opção válida!')
elif(escolhaJogador == 0 and escolhaCOM == 2):
    print('Jogador VENCEU PEDRA derrota a TESOURA do Computador')
elif(escolhaJogador == 1 and escolhaCOM == 0):
    print('Jogador VENCEU PAPEL derrota a PEDRA do Computador')
elif(escolhaJogador == 2 and escolhaCOM == 1):
    print('Jogador VENCEU TESOURA derrota O PAPEL do Computador')
elif(escolhaJogador == 0 and escolhaCOM == 1):
    print('Computador VENCEU PAPEL derrota A PEDRA do Jogador')
elif(escolhaJogador == 1 and escolhaCOM == 2):
    print('Computador VENCEU TESOURA derrota O PAPEL do Jogador')
elif(escolhaJogador == 2 and escolhaCOM == 0):
    print('Computador VENCEU PEDRA derrota A TESOURA do Jogador')
else:
    print('Empatamos! Você escolheu: {} e eu escolhi: {}'.format((componentesJogo[escolhaJogador]), (componentesJogo[escolhaCOM])))


