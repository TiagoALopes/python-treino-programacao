#Realizar o desafio do 101 ~ 106 - (Feito o 105).
def contador(* num):
    """" O Método abaixo realiza a contagem das posições dos campos recebidos.
    :param num: Recebe a lista de valores a serem contadas
    """
    #Em Python variável globais redefinidas é gerado um escopo local sem alterar o global
    a = 8
    print(f'Valor de A Local: {a}')
    #Caso queira usar o A Global precisa usar a palavra reservada abaixo:
    global b
    print(f'Valor de B global dentro de uma método: {b}\n')
    
    print(f'Recebi os número: {num} e são ao todos {len(num)}')
    for contador, item in enumerate(num):
        print(f'A posição {contador+1} é {item} ')
    print('FIM!!!\n')

def conversaoParaInteiro(entrada):
    try:
        return float(entrada)
    except:
        print('informar um valor Inteiro.')
        return 0


n = conversaoParaInteiro(input('Por gentileza informar um número: '))
print(f'O valor convertido é: {n}')

help(contador)

#parametros Opcionail
def somar(a=0, b=0, c=0):
    return a + b + c

a = 5
print(f'Valor de A global: {a}')
b = 6
print(f'Valor de B global: {6}')
contador(1, 2, 3, 5)

soma = somar(1, 5)
soma = somar(a=1, b=5, c=0)
soma = somar(a=1, b=5, c=0)

