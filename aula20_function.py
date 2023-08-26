#Toda passagem de parametros no Python é por referência - Fazer questões: de 96 ~ 100.
#Método com empacotamento.
def contador(* num):
    """" O Método abaixo realiza a contagem das posições dos campos recebidos.
    :param num: Recebe a lista de valores a serem contadas
    """
    print(f'Recebi os número: {num} e são ao todos {len(num)}')
    for contador, item in enumerate(num):
        print(f'A posição {contador+1} é {item} ')
    print('FIM!!!\n')

help(contador)

#parametros Opcionail
def somar(a, b, c=0):
    soma = a + b + c
    print(f'A soma do valor é {soma}')

somar(1, 5)
somar(a=1, b=5, c=0)

#Método com lista de valores
def dobra(list):
    posicao = 0
    for posicao, valor in enumerate(list):
        list[posicao] = valor*2

def dobra2(listaposicao):
    posicao = 0
    while posicao < len(listaposicao):
        listaposicao[posicao] *= 2
        posicao += 1


contador(1, 2, 3, 5)
contador( 3, 5)
contador(1, 2,)
contador(3)
contador(5)
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

dobra2(valores)
print(valores)
