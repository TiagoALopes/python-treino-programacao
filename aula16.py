#Tuplas é uma coleção ordenada e imutável. Permite membros duplicados e tipos diferentes (Parecido com comportamento de Vetor)
#Póssivel apagar a tupla toda del().

tuplaLanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #Tupla Forma 1
conjuntoLanche = set() #Conjunto Forma.

tuplaLanche2 = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
tuplaLanche3 = tuplaLanche + tuplaLanche2 #Possível unir as tuplas

#listaLanche = [] #Lista - Forma 1
#listaLanche = list() #Lista - Forma 2

#dicionarioLanche = {} #Dicionário - Forma 1
#dicionarioLanche = dict() #Dicionário - Forma 2

conjuntoLanche.add('Refrigerante')
print(conjuntoLanche)

print(tuplaLanche3.count('Suco')) #Possível contar a qtd de  vezes que aparece o elemento
print(tuplaLanche3.index('Suco')) #Possível descobrir a posição que está determinado valor

print(tuplaLanche3) #Possível unir as tuplas
print(len(tuplaLanche)) #qtdTupla.
print(sorted(tuplaLanche)) #Ordenado.

print('\nOpção 1')
for comida in range(0,len(tuplaLanche)):
    print(f'Eu vou comer {tuplaLanche[comida]} e posição: {comida}')

print('\nOpção 2')
for pos, comida in enumerate(tuplaLanche):
    print(f'Eu vou comer {comida} e posição: {pos}')

print('\nOpção 3')
for comida in tuplaLanche:
    print(comida, end=' ')

print('\n')

print(f'\n{tuplaLanche2}')
print(tuplaLanche2[3])
print(tuplaLanche2[-2])
print(tuplaLanche2[1:3])
print(tuplaLanche2[0:])
print(tuplaLanche2[:2])
print(tuplaLanche[-1::-1])

