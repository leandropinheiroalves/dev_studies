"""Faça um programa que peça dois números, base e expoente, calcule e
mostre o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem."""

base = int(input('Digite o valor da base: '))
expoente = int(input('Digite o valor do expoente: '))

for i in range(1, expoente):
    if i == 1:
        resultado = base * base
    else:
        resultado *= base

print(f'O resultado de {base} elevado a {expoente} é: {resultado}')
