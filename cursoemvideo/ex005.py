"""
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor = numero - 1
print(f'O sucessor do número \033[1;32m{numero}\033[m é \033[1;33m{sucessor}\033[m e o seu antecessor é \033[1;34m{antecessor}\033[m.')
