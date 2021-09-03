# EXERCÍCIO 38
"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    → O primeiro valor é maior
    → O segundo valor é maior
    → Não existe valor maior, os dois são iguais
"""

# PROGRAMA PRINCIPAL
numero_1 = int(input('Digite o primeiro número: '))  # Recebe o primeiro número
numero_2 = int(input('Digite o segundo número: '))  # Recebe o segundo número
if numero_1 > numero_2:  # SE o primeiro número for maior que o segundo
    print('O primeiro valor é maior.')  # Imprime primeiro número é maior
elif numero_1 < numero_2:  # MAIS SE o primeiro número for menor que o segundo
    print('O segundo valor é maior.')  # Imprime segundo número é maior
else:  # SENÃO
    print('Não existe valor maior, os dois são iguais.')  # Imprime que os dois números são iguais
