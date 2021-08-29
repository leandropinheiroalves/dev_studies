"""
Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""
termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razao: '))
contador = 0
while contador < 10:
    print(f'{termo}', end=' → ')
    termo += razao
    contador += 1
print('FIM')
