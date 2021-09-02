"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep  # Importando função sleep do módulo import


def maior(*numeros):  # Criando função maior com parâmetros variáveis
    print('=' * 40)  # Retorna espaçamento
    print('Analisando valores.')  # Retorna cabeçalho
    maior = 0  # Criando váriável maior com valor 0
    for i in numeros:  # Loop de iteração em cada número na tupla numeros
        print(i, end=' ')  # Retorna os números sem quebra de linha
        sleep(0.5)  # Temporizador
        if i > maior:  # Se o número for maior do que o valor de maior
            maior = i  # Variável maior recebe o valor no número
    print(f'Ao todo foram informados {len(numeros)} valores.')  # Retorna quantos números foram informados
    print(f'O maior valor informado foi {maior}.')  # Retorna o maior valor informado


maior(2, 9, 4, 5, 7, 1)  # Executando função maior com valores 2, 9, 4, 5, 7 e 1
maior(4, 7, 0)  # Executando função maior com valores 4, 7 e 0
maior(1, 2)  # Executando função maior com valores 1 e 2
maior(6)  # Executando função maior com valor 6
maior()  # Executando função maior sem valores
