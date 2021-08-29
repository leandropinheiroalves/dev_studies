"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
numero = int(input('Digite um número: '))
divisao = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisao += 1
if divisao == 2:
    print(f'O número {numero} só foi dividido {divisao} vezes, por isso é primo.')
else:
    print(f'O número {numero} foi dividido {divisao} vezes, por isso não é primo.')
