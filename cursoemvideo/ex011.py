"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""
import math

largura = float(input('Digite a largura da parede a ser pintada: '))
altura = float(input('Digite a altura da parede a ser pintada: '))
area = largura * altura
tinta = math.ceil(area / 2)
print(f'A área a ser pintada é de \033[2;33m{area:.2f}\033[m m² e serão necessários \033[2;34m{tinta}\033[m litros de tinta para pinta-la.')
