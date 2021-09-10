"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint  # Importando função randint do módulo random
from time import sleep  # Importando função sleep do módulo time
from operator import itemgetter  # Importando função itemgetter do módulo operator
jogadas = dict()  # Criando um dicionário para as jogadas
ordem = list()  # Criando uma lista para o ranking final
for i in range(1, 5):  # Loop de 4 iterações
    jogadas[f'jogador{i}'] = randint(1, 6)  # Adiciona a chave jogador e um valor aleatório de 1 a 6
for j, n in jogadas.items():  # Loop de iteração para cada item no dicionário jogadas
    print(f'{j} tirou {n} no dado.')  # Retorna o número tirado no dado pelo jogador
    # sleep(1)  # Temporizador de 1 segundo
ordem = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
# Adiciona os itens do dicionário jogadas na lista ordem organizados pelo valor em ordem decrescente

print()  # Quebra de linha
print(f'{" RANKING DE JOGADORES ":=^34}')  # Retorna um cabeçalho para o programa
for j, n in enumerate(ordem):  # Loop de iteração com índice de cada valor da lista ordem
    print(f'Em {j + 1}° lugar ficou o {n[0]} com {n[1]}')  # Retorna em que posição cada jogador ficou
    # sleep(1)  # Temporizador de 1 segundo
