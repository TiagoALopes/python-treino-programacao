print('='*14, end='')
print('LOJA DO PAPAI', end='')
print('='*14)
precoCompra = float(input('Preço das compras: R$'))
mensagemPadraoCompra = 'Sua compra de R${:.2f} vai custar R${:.2f} no final' 
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')

opcao = int(input('Qual é a opção? '))

if (opcao == 1):
    print(mensagemPadraoCompra.format(precoCompra, (precoCompra * 0.90)))
elif (opcao == 2):
    print(mensagemPadraoCompra.format(precoCompra, (precoCompra * 0.95)))
elif (opcao == 3):
    print(mensagemPadraoCompra.format(precoCompra, precoCompra))
elif (opcao == 4):
    parcelas = int(input('Quantas parcelas?'))
    valorCompraJuros = precoCompra * 0.2
    print('Sua compra será parceladas em {}x de R${:.2f} COM JUROS'.format(parcelas, valorCompraJuros))
    print(mensagemPadraoCompra.format(precoCompra, (precoCompra + valorCompraJuros)))
else:
    print('Por gentileza, selecionar uma opção listada acima!')