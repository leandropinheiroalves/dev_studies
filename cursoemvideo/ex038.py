"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    * O primeiro valor é maior
    * O segundo valor é maior
    * Não existe valor maior, os dois são iguais
"""
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
if numero_1 > numero_2:
    print('O primeiro valor é maior.')
elif numero_1 < numero_2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
