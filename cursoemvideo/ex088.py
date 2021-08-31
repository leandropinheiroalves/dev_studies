"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sorter 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint  # Importando função randint do módulo random
jogo = []  # Lista com o valor de cada jogo
principal = []  # Lista principal para armazenar todos os jogos
quantidade = int(input('Quantos jogos: '))  # Variável que recebe a quantidade de jogos a serem feitos
for i in range(1, quantidade+1):  # Loop com iteração conforme valor da variável quantidade
    contador = 0  # Contador
    while True:  # Loop infinito
        numero = randint(1, 60)  # Variável que recebe um número aleatório de 1 a 60
        if numero not in jogo:  # Se o número não estiver na lista jogo
            jogo.append(numero)  # Adiciona o número na lista jogo
            contador += 1  # Incrementa o contador em 1
        if contador >= 6:  # Se o contador for maior ou igual a 6
            break  # Encerra o loop infinito
    jogo.sort()  # Organiza a lista jogo em ordem crescente
    principal.append(jogo[:])  # Adiciona uma cópia dos valores da lista jogo para a lista principal
    jogo.clear()  # Limpa a lista jogo
for i, l in enumerate(principal):  # Loop com iteração em cada valor da lista principal
    print(f'Jogo {i+1}: {l}')  # Retorna o índice e o valor de cada jogo na lista principal
