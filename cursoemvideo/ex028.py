"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import choice

lista_numeros = [0, 1, 2, 3, 4, 5]
numero_usuario = int(input('Digite um número de 0 a 5: '))
numero_computador = choice(lista_numeros)
if numero_computador == numero_usuario:
    print('Você venceu!')
else:
    print('Você perdeu!')
print(f'Número escolhido pelo computado: {numero_computador}')
print(f'Número escolhido pelo usuário: {numero_usuario}')

# Solução Guanabara:
# from random import randint
# computador = randint(0, 5) # Faz o computador "PENSAR"
# print('-=-' * 20)
# print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
# print('-=-' * 20)
# jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
# if jogador == computador:
#     print('PARABÉNS! Você conseguiu me vencer!')
# else:
#     print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
