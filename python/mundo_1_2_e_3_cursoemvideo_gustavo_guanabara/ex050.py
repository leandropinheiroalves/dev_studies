# EXERCÍCIO 50
"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""

# PROGRAMA PRINCIPAL
soma = contagem = 0  # Variáveis soma e contagem recebem 0
for i in range(1, 7):  # Loop de iteração de 1 a 6
    numero = int(input('Digite um número: '))  # Recebe um número
    if numero % 2 == 0:  # SE o número for par
        contagem += 1  # Incremento da contagem em 1
        soma += numero  # Incremento da soma com o número
print(f'Foram digitados {contagem} números pares e a soma deles é {soma}.')  # Imprime o resultado
