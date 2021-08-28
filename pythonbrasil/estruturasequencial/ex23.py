"""Faça um Programa que peça um número e informe se o número é inteiro ou
decimal. Dica: utilize uma função de arredondamento."""
import math
numero = float(input('Digite um número: '))

if numero == round(numero):
    print(f'{int(numero)} é INTEIRO')
else:
    print(f'{numero} é DECIMAL')