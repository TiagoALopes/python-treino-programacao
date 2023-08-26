frase = input('Digite uma Frase: ').upper().strip()
fraseSeparada = frase.split()
frasejunto = ''.join(fraseSeparada)
nomeInvertido = ''

for letra in range (len(frasejunto) -1 , -1, -1):
    nomeInvertido += frasejunto[letra]

print('O inverso de {} é {}'.format(frase, nomeInvertido))

if frasejunto == nomeInvertido:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')


