"""
Faça um programa que mostre a tabuada de vários números, um de cada  vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""
contagem = 0
while True:
    numero = int(input('Digite um número: '))
    contagem = 0
    if numero < 0:
        print('Programa encerrado.')
        break
    while contagem < 10:
        contagem += 1
        print(f'{numero} x {contagem} = {numero * contagem}')
