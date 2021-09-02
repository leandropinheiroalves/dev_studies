"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
A situação do aluno é Aprovado caso a média for maior que 7, do contrário a situação do aluno será Reprovado.
No final, mostre o conteúdo da estrututa na tela.
"""
aluno = dict()  # Cria um dicionário
aluno['nome'] = str(input('Digite o nome do aluno: '))  # Cria a chave 'nome' no dicionário recebendo nome
aluno['media'] = float(input('Digite a média do aluno: '))  # Cria a chhave 'media' no dicionário recebendo media
if aluno['media'] < 7:  # Se o valor da chave media for menor que 7
    aluno['situação'] = 'Reprovado'  # Dicionário recebe a chave 'situação' com o valor 'Reprovado'
else:  # Senão
    aluno['situação'] = 'Aprovado'  # Dicionário recebe a chave 'situação' com o valor 'Aprovado'
for i, v in aluno.items():  # Loop com iteração para cada item do dicionário aluno
    print(f'{i.capitalize()}: {v}')  # Retorna a chave e o respectivo valor
