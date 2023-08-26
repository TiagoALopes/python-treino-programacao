# A = B faz ligação das listas em Python.
# A = B[:] - Cria uma cópia de B p/ A sem ligar uma lista com a outra.

listaLanche = list(range(4, 11))
listaLanche2 = [8,2,5,684,856,216412]
listaLanche.append(listaLanche2[:])

print(listaLanche)

listaLanche2.sort()
print(listaLanche2)

listaLanche2.pop()
listaLanche2.append(20)

listaLanche2.sort(reverse=True)
print(listaLanche2)

listaLanche2.remove(20) #Remove a primeira ocorrência de um número e remove!
print(listaLanche2)

print(f'{len(listaLanche)}')

for item in listaLanche:
    print(item, end='')

for chave, valores in enumerate(listaLanche):
    print(f'Na posição {chave}... valor: {valores}')
print('Cheguei ao final da lista!')

valores = list()
for cont in range(0,4):
    valores.append(int(input('Digite um valor: ')))