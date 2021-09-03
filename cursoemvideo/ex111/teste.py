"""
Crie um pacote chamado utilidadesCeV que tenha dois pacotes internos chamados moeda e dado.
Tranfira todos as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
"""
# Programa Principal
from cursoemvideo.ex111.utilidadescev import moeda
p = float(input('Digite o preço: R$'))
moeda.resumo(p)
