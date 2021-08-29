"""
Melhore o jogo do exercício 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint

numero_usuario = int(input('Digite um número de 0 a 10: '))
numero_computador = randint(0, 10)
palpites = 1
while numero_computador != numero_usuario:
    palpites += 1
    numero_usuario = int(input(f'Errou! Digite um número novamente: '))
print(f'Você venceu! O computador escolheu {numero_computador}. Você precisou de {palpites} tentativas para acertar.')
