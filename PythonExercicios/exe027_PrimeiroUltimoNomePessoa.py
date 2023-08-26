nomeCompleto = input('Digite seu nome completo: ').strip()
nomeDividido = nomeCompleto.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nomeDividido[0]))
print('Seu último nome é {}'.format(nomeDividido[(len(nomeDividido)-1)]))

