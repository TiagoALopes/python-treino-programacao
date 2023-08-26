dados = dict()
dados = { 'nome': 'Pedro', 'idade': 25 }
dados['sexo'] = 'M'

print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])

del dados['sexo']
print(dados)

print(dados.values())
print(dados.keys())
print(dados.items())

for k, v in dados.items():
    print(f'{k} dele(a) é {v}')