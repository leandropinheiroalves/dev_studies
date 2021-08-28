"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
import random
escolha = int(input('''[1] PEDRA
[2] PAPEL
[3] TESOURA
Digite uma opção: '''))
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(opcoes)
if escolha == 1 and computador == 'PEDRA':
    print('Empate, os dois escolherem PEDRA')
elif escolha == 1 and computador == 'PAPEL':
    print('O computador venceu. Você escolheu PEDRA e o computador escolheu PAPEL.')
elif escolha == 1 and computador == 'TESOURA':
    print('Você venceu. O computador escolheu TESOURA e você PEDRA.')
elif escolha == 2 and computador == 'PEDRA':
    print('Você venceu. Você escolheu PAPEL e o computador escolheu PEDRA.')
elif escolha == 2 and computador == 'PAPEL':
    print('Empate, os dois escolherem PAPEL')
elif escolha == 2 and computador == 'TESOURA':
    print('O computador venceu. Você escolheu PAPEL e o computador escolheu TESOURA.')
elif escolha == 3 and computador == 'PEDRA':
    print('O computador venceu. Você escolheu TESOURA e o computador escolheu PEDRA.')
elif escolha == 3 and computador == 'PAPEL':
    print('Você venceu. Você escolheu TESOURA e o computador escolheu PAPEL.')
elif escolha == 3 and computador == 'TESOURA':
    print('Empate, os dois escolherem TESOURA')
else:
    print('Ouve algum erro. Tente novamente.')