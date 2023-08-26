print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
primeiroSegmento = float(input('Primeiro Segmento: '))
segundoSegmento = float(input('Segundo Segmento: '))
terceiroSegmento = float(input('Terceiro Segmento: '))

if ((primeiroSegmento < segundoSegmento + terceiroSegmento)
    and (segundoSegmento < primeiroSegmento + terceiroSegmento)
    and (terceiroSegmento < primeiroSegmento + segundoSegmento)):
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')