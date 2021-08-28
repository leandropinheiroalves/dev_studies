"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

valor = int(input('Digite um número: '))

if valor > 0:
    print('O valor digitado é positivo.')
elif valor == 0:
    print('O valor digitado é neutro.')
else:
    print('O valor digitado é negativo.')