"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do  jogo.
"""
from random import randint
contagem = 0
while True:
    numero = int(input('Digite um número: '))
    escolha = str(input('Par ou Ímpar? [P/I]')).upper()
    computador = randint(0, 10)
    total = computador + numero
    if escolha == 'P' and total % 2 == 0:
        contagem += 1
        print(f'Você VENCEU!')
        print(f'Você jogou {numero} e o computador {computador}. Total {total} que É PAR!')
    elif escolha == 'P' and total % 2 != 0:
        print('Você PERDEU!')
        print(f'Você jogou {numero} e o computador {computador}. Total {total} que É ÍMPAR!')
        break
    elif escolha == 'I' and total % 2 != 0:
        contagem += 1
        print(f'Você VENCEU!')
        print(f'Você jogou {numero} e o computador {computador}. Total {total} que É ÍMPAR!')
    elif escolha == 'I' and total % 2 == 0:
        print('Você PERDEU!')
        print(f'Você jogou {numero} e o computador {computador}. Total {total} que É PAR!')
        break
print(f'O Jogo acabou. Você venceu {contagem} vezes consecutivas.')

