# EXERCÍCIO 46
"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma  pausa de 1 seundo entre eles.
"""

# PROGRAMA PRINCIPAL
from time import sleep  # Importando função sleep do módulo time
for i in range(10, -1, -1):  # Criando loop com contagem regressiva de 10 a 0
    print(i, end=' ')  # Imprime numero da contagem sem quebra de linha
    sleep(1)  # Temporizador
print('BUM!')  # Imprime BUM! no final da contagem
