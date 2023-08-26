peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)
classificacao = ''

if (imc <= 18.5):
    classificacao = 'ABAIXO'
elif (imc >= 18.6 and imc <= 24.9):
    classificacao = 'IDEAL'
elif (imc >= 25.0 and imc <= 29.9):
    classificacao = 'LEVEMENTE ACIMA'
elif (imc >= 30.0 and imc <= 34.9):
    classificacao = 'OBESIDADE GRAU I'
elif (imc >= 35.0 and imc <= 39.9):
    classificacao = 'OBESIDADE GRAU II (SEVERA)'
elif (imc >= 39.9):
    classificacao = 'OBESIDADE GRAU III (MÓRBIDA)'

print('O IMC dessa pessoa é de {:.1f}'.format(imc))
print('Você está {} DO PESO normal'.format(classificacao))