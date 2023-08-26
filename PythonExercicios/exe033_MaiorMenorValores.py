primeiroValor = int(input('Primeiro Valor: '))
segundoValor = int(input('Segundo Valor: '))
terceiroValor = int(input('Terceiro Valor: '))

menor = primeiroValor
maior = primeiroValor

if (segundoValor < primeiroValor and segundoValor<terceiroValor):
    menor = segundoValor
elif(terceiroValor < primeiroValor and terceiroValor< segundoValor):
        menor = terceiroValor
if (segundoValor > primeiroValor and segundoValor > terceiroValor):
    maior = segundoValor
elif(terceiroValor > primeiroValor and terceiroValor > segundoValor):
        maior = terceiroValor

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
