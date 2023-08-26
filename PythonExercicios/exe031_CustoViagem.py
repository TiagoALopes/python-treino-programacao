distanciaTrajeto = float(input('Qual é a distância da sua viagem? '))
viagemCurta = 200
valorViagem = 0

if (distanciaTrajeto <= viagemCurta):
    valorViagem = 0.50
    precoViagemCurta = valorViagem * distanciaTrajeto
    print('Você está prestes a começar uma viagem de {}'.format(distanciaTrajeto))
    print('E o preço da sua passagem será de R${:.2f}'.format(precoViagemCurta))
else:
    valorViagem = 0.45
    precoViagemCurta = valorViagem * distanciaTrajeto
    print('Você está prestes a começar uma viagem de {}'.format(distanciaTrajeto))
    print('E o preço da sua passagem será de R${:.2f}'.format(precoViagemCurta))
    


