"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

from time import sleep  # Importando função sleep do módulo import


def maior(*numeros):  # Criando função maior com parâmetro numero variável
    print('=' * 40)  # Imprime na tela espaçamento
    print('Analisando valores.')  # Imprime na tela um cabeçalho
    resultado = 0  # Cria váriável resultado com valor 0
    for i in numeros:  # Loop de iteração em cada número na tupla numeros
        print(i, end=' ')  # Imprime na tela os números sem quebra de linha
        sleep(0.5)  # Temporizador
        if i > resultado:  # Se o número for maior do que o valor de resultado
            resultado = i  # Variável resultado recebe o valor do número
    print(f'Ao todo foram informados {len(numeros)} valores.')  # Imprime na tela quantos números foram informados
    print(f'O maior valor informado foi {resultado}.')  # Imprime na tela o resultado


maior(2, 9, 4, 5, 7, 1)  # Executando função maior com valores 2, 9, 4, 5, 7 e 1
maior(4, 7, 0)  # Executando função maior com valores 4, 7 e 0
maior(1, 2)  # Executando função maior com valores 1 e 2
maior(6)  # Executando função maior com valor 6
maior()  # Executando função maior sem valores
