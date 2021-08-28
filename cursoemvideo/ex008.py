"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

metros = float(input('Digite um valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'O valor digitado em centímetros é: \033[31m{centimetros} cm\033[m')
print(f'O valor digitado em milímetros é: \033[35m{milimetros} mm')