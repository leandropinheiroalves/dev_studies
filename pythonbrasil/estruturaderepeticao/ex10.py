"""Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
"""

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o primeiro número: '))

for numeros in range(numero_1 + 1, numero_2):
    print(numeros, end = ' ')