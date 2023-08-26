from datetime import date

print('Por gentileza, inserir o ano de nascimento das sete pessoas?')
pessoa = []
qtdPessoasMaiores = 0
maioridade = 21

for c in range(1, 8):
    anoNascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = date.today().year - anoNascimento
    if idade >= maioridade:
        qtdPessoasMaiores += 1
    elif idade < 21:
        pessoa.append(idade)
print('\nAo todo tivemos {} pessoas maiores de idade'.format(qtdPessoasMaiores))
print('E também tivemos {} pessoas menores de idade'.format(len(pessoa)))