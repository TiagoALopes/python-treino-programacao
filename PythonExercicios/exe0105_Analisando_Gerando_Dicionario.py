def novoDicionario():
    novoDicionario = {'total': '', 'maior': 0, 'menor': 0,'média': 0}
    return novoDicionario
        
def notas(*notasrecebidas, sit = False):
    """
    -> Funcao responsável por analisar as notas recebidas e a situacao do aluno de acordo com a validação acadêmica da escola.
    :param notasrecebidas: um ou mais notas do aluno. (Aceita Várias)
    :param sit: Valor opcional, indicando se deve ou não exibir a situacao do aluno.
    :return: dicionário com várias informacoes sobre a situacao da turma.
    """
    dicionarioNotas = novoDicionario()

    totalNotas = 0
    somaNotas = 0
    maiorNota = 0
    menorNota = 999
    media = 0

    for nota in notasrecebidas:
        totalNotas += 1
        somaNotas += nota

        if nota > maiorNota:
            maiorNota = nota

        if nota < menorNota:
            menorNota = nota

    media = somaNotas/totalNotas

    dicionarioNotas['total'] = totalNotas
    dicionarioNotas['maior'] = maiorNota
    dicionarioNotas['menor'] = menorNota
    dicionarioNotas['média'] = media

    if sit:
        if media >= 7:
            dicionarioNotas['situacao'] = 'BOA'
        elif media >= 5 and media < 7:
            dicionarioNotas['situacao'] = 'CUIDADO COM A RECUPERAÇÃO'
        else:
            dicionarioNotas['situacao'] = 'CUIDADO COM A REPROVAÇÃO'

    return dicionarioNotas

#Programa Principal.
resp = notas(3.5, 2.5, 6, 2.5)
print(resp)
help(notas)