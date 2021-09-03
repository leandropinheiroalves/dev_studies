# EXERCÍCIO 103
"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
    → O nome de um jogador
    → E quantos gols ele marcou.
O programa deverá ser capaza de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


# DEFININDO FUNÇÃO
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


# PROGRAMA PRINCIPAL
n = str(input('Digite o nome do jogador: '))
g = str(input('Digite o número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
