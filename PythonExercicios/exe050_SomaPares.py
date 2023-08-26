somaPares = 0;
qtdPares = 0;
for numeros in range(0, 6):
    valorInserido = int(input('Informe um número: '))
    if valorInserido % 2 == 0:
        qtdPares += 1
        somaPares += valorInserido
print('Foram informados {} número(s) par(es) e a soma do(s) valor(es) par(es) disponibilizado foi igual a: {}'.format(qtdPares, somaPares))