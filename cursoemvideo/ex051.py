"""
Desenvolva um programa que leia o primeiro termo e a razão de um PA (Progressão Aritimética). No final, mostre os 10 primeiros termos dessa progressão.
"""
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
for i in range(1, 11):
    print(termo, end=' → ')
    termo += razao
print('FIM')
