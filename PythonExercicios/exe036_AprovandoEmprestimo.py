valorCasa = float(input('Valor da casa: R$'))
salarioComprador = float(input('Salário do comprador: R$'))
anosFinanciamento = int(input('Quantos anos de financiamento?: '))
limiteOrcamento = salarioComprador * 0.3
valorPrestacao = valorCasa / (anosFinanciamento * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valorCasa, anosFinanciamento, valorPrestacao))
if(valorPrestacao <= limiteOrcamento):
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')