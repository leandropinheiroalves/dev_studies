"""
Melhore o exercício 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
termo = int(input('Digite o valor do primeiro termo: '))
razao = int(input('Digite o valor da razao: '))
contador = mais = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador < total:
        print(f'{termo}', end=' → ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
