from datetime import date

maiorIdade = 18
anoNascimento = int(input('Ano de nascimento: '))
idade = date.today().year - anoNascimento
anoAlistamento = anoNascimento + 18
print('Quem nasceu em {} tem {} anos em {}'.format(anoNascimento, idade, date.today().year))

if (idade > maiorIdade):
    print('Você já deveria ter se alistado há {} anos'.format((idade - maiorIdade)))
    print('Seu alistamento foi em {}'.format(anoAlistamento))
else:
    print('Seu alistamento será em {}'.format(anoAlistamento))