# EXERCÍCIO 52
"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

# PROGRAMA PRINCIPAL
numero = int(input('Digite um número: '))  # Recebe um número
divisao = 0  # Variável divisão recebe 0

for i in range(1, numero + 1):  # Loop iterável de 1 até o valor da váriavel numero
    if numero % i == 0:  # SE os resto da divisão do numero pelo valor de i for zero
        divisao += 1  # Incremento da variável divisao

if divisao == 2:  # SE valor de divisao for igual a 2
    print(f'O número {numero} só foi dividido {divisao} vezes, por isso é primo.')  # Imprime primo
else:  # SENÃO
    print(f'O número {numero} foi dividido {divisao} vezes, por isso não é primo.')  # Imprime ñ primo
