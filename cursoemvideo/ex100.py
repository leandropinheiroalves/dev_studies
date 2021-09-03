"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
soma entre todos os valores PARES sorteados pela função anterior.
"""
from random import randint  # Importando função randint do módulo random
from time import sleep  # Importando função sleep do módulo time


def sorteio(num):  # Criando função sorteio
    print(f'Sorteando 5 valores: ', end='')  # Imprime na tela um cabeçalho
    for i in range(0, 5):  # Loop com 5 iterações
        n = randint(1, 10)  # Váriavel n que recebe um número aleatório
        numeros.append(n)  # Adiciona os valores de n na lista numeros
        print(f'{n} ', end='')  # Imprime na tela os valores aleatórios gerados
        sleep(0.3)  # Temporizador
    print('FIM')  # Imprime na tela mensagem de fim


def somaPar(lst):  # Criando função somaPar
    soma = 0  # Cria variável soma
    for valor in lst:  # Loop de iteração para cada valor da lista
        if valor % 2 == 0:  # Se o valor for par
            soma += valor  # Incrementa o valor da variável soma
    print(f'A soma dos valores pares de {lst} é {soma}')  # Imprime na tela mensagem com resultado da soma


# Program Principal
numeros = list()  # Criando lista
sorteio(numeros)  # Executando a função sorteio na lista numeros
somaPar(numeros)  # Executando a função somaPar na lista numeros
