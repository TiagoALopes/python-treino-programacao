sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe seu sexo [M/F]: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Por gentileza, forneça um sexo válido [M/F]: ')