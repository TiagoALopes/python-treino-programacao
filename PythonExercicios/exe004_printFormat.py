valorRecebido = input('Digite Algo:')
print('O tipo primitivo desse valor é: ', type(valorRecebido))
print('É numero? {}'.format(valorRecebido.isnumeric()))
print('É alfabético? {}'.format(valorRecebido.isalpha()))
print('É alfabético e numérico? {}'.format(valorRecebido.isalnum()))
print('Só tem espaços? {}'.format(valorRecebido.isspace()))
print('Possui só letrar maiusculas? {}'.format(valorRecebido.isupper()))
print('Possui só letrar minusculas? {}'.format(valorRecebido.islower()))
print('Está capitalizada? {}'.format(valorRecebido.istitle())) #Python