"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma  pausa de 1 seundo entre eles.
"""
from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('BUM!')
