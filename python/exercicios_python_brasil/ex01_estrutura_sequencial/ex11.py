"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
"""

numero_1 = int(input('Informe um número inteiro: '))
numero_2 = int(input('Informe outro número inteiro: '))
numero_3 = float(input('Informe um número inteiro real: '))

a = (numero_1 * 2) * (numero_2 / 2)
b = numero_1 * 2 + numero_3
c = numero_3 ** 3

print(f'''O produto do dobro de {numero_1} com metade de {numero_2} é: {a}.
A soma do triplo de {numero_1} com o {numero_3} é: {b}.
{numero_3} elevado ao cubo é: {c}.
''')