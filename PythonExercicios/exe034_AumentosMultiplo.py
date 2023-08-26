salario = float(input('Qual é o salário do funcionário? R$'))
SalarioMinino = 1250

if (salario <= SalarioMinino):
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,(salario * 1.15)))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,(salario * 1.10)))