primeiroSegmento = float(input('Primeiro Segmento: '))
segundoSegmento = float(input('Segundo Segmento: '))
terceiroSegmento = float(input('Terceiro Segmento: '))
tipoTriangulo = ''

if ((primeiroSegmento < segundoSegmento + terceiroSegmento)
    and (segundoSegmento < primeiroSegmento + terceiroSegmento)
    and (terceiroSegmento < primeiroSegmento + segundoSegmento)):

    if (primeiroSegmento == segundoSegmento and primeiroSegmento == terceiroSegmento):
        tipoTriangulo = 'EQUILÁTERO'
    elif (primeiroSegmento != segundoSegmento and primeiroSegmento != terceiroSegmento):
        tipoTriangulo = 'ESCALENO'
    elif (primeiroSegmento == segundoSegmento or primeiroSegmento == terceiroSegmento or segundoSegmento == terceiroSegmento):
        tipoTriangulo = 'ISÓSCELES'
    else:
        tipoTriangulo = 'NÃO IDENTIFICADO'

    print('Os segmentos acima PODEM FORMAR triângulo {}!'.format(tipoTriangulo))
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')