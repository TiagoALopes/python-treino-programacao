from math import floor

velocidade = float(input('Qual é a velocidade atual do carro?'))
limiteVelocidade = 80

if (velocidade < limiteVelocidade):
    print('Tenha um bom dia! Dirija com segurança!')
else:
    diferencaKM = float(floor(velocidade - limiteVelocidade)*7)
    print('MULTADO! Você excedeu o limite permitido que é de {}Km/h'.format(limiteVelocidade))
    print('Você deve pagar uma multa de R${:.2f}'.format(diferencaKM))