# EXERCÍCIO 51
"""
Desenvolva um programa que leia o primeiro termo e a razão de um PA (Progressão Aritimética). No final, mostre os 10 primeiros termos dessa progressão.
"""

# PROGRAMA PRINCIPAL
termo = int(input('Digite o primeiro termo da PA: '))  # Recebe valor da PA
razao = int(input('Digite a razão: '))  # Recebe razão

for i in range(1, 11):  # Loop iterável de 1 a 10
    print(termo, end=' → ')  # Imprime os resultados sem quebra de linha
    termo += razao  # Incrementa a variável termo com o valor de razão

print('FIM')  # Imprime FIM
