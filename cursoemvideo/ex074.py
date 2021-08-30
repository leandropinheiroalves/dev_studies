"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
numeros = (randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000), randint(0, 1000))
menor = maior = 0
for i in range(0, 5):
    if i == 0:
        menor = maior = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print(f'Valores sorteados: {numeros}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
# Alternativas para maior e menor usando max/min (tira a necessidade de usar if/else nesse caso)
# print(f'O maior valor sorteado foi {max(numeros)}')
# print(f'O menor valor sorteado foi {min(numeros)}')
