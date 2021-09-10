"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import choice  # Importando função choice do módulo random

lista_numeros = [0, 1, 2, 3, 4, 5]  # Criando lista com números de 1 a 5
usuario = int(input('Digite um número de 0 a 5: '))  # Recebendo um número do usuario
computador = choice(lista_numeros)  # Recebendo numero aleatório escolhido pelo computador
if computador == usuario:  # Se o numero do usuário for igual ao do computador o usuário vence
    print('Você venceu!')  # Retorna a mensagem de vitória do usuário
else:  # Se o numero do usuário for diferente do computador o usuário perde
    print('Você perdeu!')  # Retorna a mensagem de derrota do usuário
print(f'Número escolhido pelo usuário: {usuario}')  # Retorna o número escolhido pelo usuário
print(f'Número escolhido pelo computador: {computador}')  # Retorna o número escolhido pelo computador


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
