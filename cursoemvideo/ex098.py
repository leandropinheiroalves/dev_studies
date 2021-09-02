"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
    a) De 1 até 10, de 1 em 1.
    b) De 10 até 0, de 2 em 2.
    c) Uma contagem personalizada.
"""
from time import sleep  # Importando função sleep do módulo time


def contador(inicio, fim, passo=1):  # Criando função contador com parâmetros inicio, fim e passo
    print('=' * 40)  # Retorna espaçamento
    if passo < 0:  # Se passo for negativo
        passo *= -1  # Valor de passo fica positivo
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')  # Retorna o cabeçalho
    fim += 1  # Iteração de fim
    if inicio > fim:  # Se o inicio for maior que o fim
        passo *= -1  # Valor de passo fica negativo
        fim -= 2  # Decremento de fim
    for i in range(inicio, fim, passo):  # Loop de iteração numa sequência de inicio, fim com variação passo
        print(i, end=' ')  # Retorna os valores sem quebra de linha
        sleep(0.5)  # Temporizador
    print('FIM!')  # Retorna Fim


contador(1, 10, 1)  # Executando contador com valores 1, 10 e 1
contador(10, 0, 2)  # Executando contador com valores 10, 0 e 2
print('=' * 40)  # Retorna espaçamento
print('Contagem personalizada.')  # Retornando cabeçalho
a = int(input('Início: '))  # Recebendo valor para inicio
b = int(input('Fim: '))  # Recebendo valor para fim
c = int(input('Passo: '))  # Recebendo valor para passo
contador(a, b, c)  # Executando contador com valores informados pelo usuário
