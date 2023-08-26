def metade(preco):
    metade = preco/2
    return f'{metade:.2f}'

def dobro(preco):
    dobro = preco*2
    return f'{dobro:.2f}'

def aumentar(preco, porcentagem):
    valoraumento = porcentagem / 100
    return preco * (1 + valoraumento)

def diminuir(preco, porcentagem):
    valordesconto = porcentagem / 100
    return preco * (1 - valordesconto)