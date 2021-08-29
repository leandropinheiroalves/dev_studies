"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
soma = contagem = 0
for i in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        contagem += 1
        soma += numero
print(f'Foram digitados {contagem} números pares e a soma deles é {soma}.')
