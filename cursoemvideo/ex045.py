# EXERCÍCIO 45
"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

# PROGRAMA PRINCIPAL
from random import choice  # Importando função choice do módulo random
print('[1] PEDRA \n[2] PAPEL \n[3] TESOURA')  # Imprime escolhas
escolha = int(input('Digite uma opção: '))  # Recebe valor da escolha
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']  # Cria lista com pedra, papel e tesoura
computador = choice(opcoes)  # Variável computador recebe um dos valores da lista aleatóriamente
if escolha == 1 and computador == 'PEDRA':  # SE usuario e computador escolherem pedra
    print('Empate, os dois escolherem PEDRA')  # Imprime empate
elif escolha == 1 and computador == 'PAPEL':  # MAIS SE usuario escolhe pedra e computador papel
    print('Você perdeu. Você escolheu PEDRA e o computador escolheu PAPEL.')  # Imprime derrota
elif escolha == 1 and computador == 'TESOURA':  # MAIS SE usuario escolhe pedra e computador tesoura
    print('Você venceu. O computador escolheu TESOURA e você PEDRA.')  # Imprime vitória
elif escolha == 2 and computador == 'PEDRA':  # MAIS SE usuario escolhe papel e computador pedra
    print('Você venceu. Você escolheu PAPEL e o computador escolheu PEDRA.')  # Imprime vitória
elif escolha == 2 and computador == 'PAPEL':  # MAIS SE usuario e computador escolherem papel
    print('Empate, os dois escolherem PAPEL')  # Imprime empate
elif escolha == 2 and computador == 'TESOURA':  # MAIS SE usuario escolhe papel e computador tesoura
    print('Você perdeu. Você escolheu PAPEL e o computador escolheu TESOURA.')  # Imprime derrota
elif escolha == 3 and computador == 'PEDRA':  # MAIS SE usuario escolhe tesoura e computador pedra
    print('Você perdeu. Você escolheu TESOURA e o computador escolheu PEDRA.')  # Imprime derrota
elif escolha == 3 and computador == 'PAPEL':  # MAIS SE usuario escolhe tesoura e computador papel
    print('Você venceu. Você escolheu TESOURA e o computador escolheu PAPEL.')  # Imprime vitória
elif escolha == 3 and computador == 'TESOURA':  # MAIS SE usuario escolhe tesoura e computador tesoura
    print('Empate, os dois escolherem TESOURA')  # Imprime empate
else:  # SENÃO
    print('Ouve algum erro. Tente novamente.')  # Imprime erro
