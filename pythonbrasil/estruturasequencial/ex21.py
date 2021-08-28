"""Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    * Exemplo 1: Para sacar a quantia de 256 reais,
      o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    * Exemplo 2: Para sacar a quantia de 399 reais,
      o programa fornece três notas de 100, uma nota de 50,
      quatro notas de 10, uma nota de 5 e quatro notas de 1."""
import math

saque = int(input('Digite o valor a ser sacado: '))
notas_100 = math.floor(saque / 100)
notas_50 = math.floor((saque % 100) / 50)
notas_10 = math.floor(((saque % 100) % 50) / 10)
notas_5 = math.floor((((saque % 100) % 50) % 10) / 5)
notas_1 = saque % 5

if 10 <= saque <= 600:
    print(f'Valor a ser sacado: {saque}')
    print(f'''    Quantidade de notas de R$ 100 : {notas_100} notas
    Quantidade de notas de R$ 50  : {notas_50} notas
    Quantidade de notas de R$ 10  : {notas_10} notas
    Quantidade de notas de R$ 5   : {notas_5} notas
    Quantidade de notas de R$ 1   : {notas_1} notas
    ''')
else:
    print('ERRO! O valor a ser sacado precisa ser entre 10 e 600.')


