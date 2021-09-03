"""
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com o tamanho adaptável.
Ex:
escreva('Olá, Mundo!')
Saída:
------------
Olá, Mundo!
------------
"""


def escreva(mensagem):  # Criando função escreva com parâmetro mensagem
    tamanho = len(mensagem) + 4  # Váriavel com o tamanho da mensagem + 4
    print('=' * tamanho)  # Imprime na tela sinais de igual conforme o valor da variável tamanho
    print(f'  {mensagem}')  # Imprime na tela a mensagem
    print('=' * tamanho)  # Imprime na tela sinais de igual conforme o valor da variável tamanho


# Programa Principal
escreva('Gustavo Guanabara')  # Executando função com mensagem = 'Gustavo Guanabara'
escreva('Curso de Python no Youtube')  # Executando função com mensagem = 'Curso de Python no Youtube'
escreva('CeV')  # Executando função com mensagem = 'CeV'
