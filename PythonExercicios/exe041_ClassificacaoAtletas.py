from datetime import date

maiorIdade = 18
anoNascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anoNascimento

print('O atleta tem {} anos'.format(idade))

if (idade <= 0):
    print('Por gentileza informar um ano válido.')
elif (idade <= 9):
    print('Classificação: MIRIM')
elif (idade <= 14):
    print('Classificação: INFANTIL')
elif (idade <= 19):
    print('Classificação: JUNIOR')
elif (idade <= 25):
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')