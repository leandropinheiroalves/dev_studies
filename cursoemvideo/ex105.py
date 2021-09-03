"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
    * Quantidade de notas
    * A maior nota
    * A menor nota
    * A média da turma
    * A situação(opcional)
Adicione também as docstrings de função.
"""


def notas(*n, sit=False):
    """
    → Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n) / len(n)
    if sit:
        if turma['média'] >= 7:
            turma['situação'] = 'BOA'
        elif turma['média'] >= 5:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'
    return turma


# PROGRAMA PRINCIPAL
resp = notas(9, 10, 5.5, 2.5, 8.5, sit=True)
print(resp)
