notaUm = float(input('Primeira nota: '))
notaDois = float(input('Segunda nota: '))
media = (notaUm + notaDois) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(notaUm, notaDois, media))

if (media >= 7):
    print('O aluno está APROVADO')
elif (media >= 5 and media < 7):
    print('O aluno está RECUPERAÇÃO')
else:
    print('O aluno está REPROVADO')