"""
Refaça o exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

termo = int(input('Digite o valor do primeiro termo: '))  # Recebendo primeiro valor
razao = int(input('Digite o valor da razao: '))  # Recebendo segundo valor
contador = 0  # Criando contador
while contador < 10:  # Loop ENQUANTO o contador for menor que 10
    print(f'{termo}', end=' → ')  
    termo += razao
    contador += 1
print('FIM')
