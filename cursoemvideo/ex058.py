# EXERCÍCIO 58
"""
Melhore o jogo do exercício 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

# PROGRAMA PRINCIPAL
from random import randint  # Importando função randint do módulo random

numero_usuario = int(input('Digite um número de 0 a 10: '))
# ↑ Recebe valor de 0 a 10 inserido pelo usuário
numero_computador = randint(0, 10)  # Computador escolhe um número de 0 a 10
palpites = 1  # Variável palpites começa em 1

while numero_computador != numero_usuario:  # ↑ Loop de iteração ENQUANTO numero do usuário diferente do numero do computador
    palpites += 1  # Incremento do palpite
    numero_usuario = int(input(f'Errou! Digite um número novamente: '))  # Recebe outro número

print(f'Você venceu! O computador escolheu {numero_computador}. Você precisou de {palpites} tentativas para acertar.')
# ↑ Imprime vitória e número de palpite necessários.
