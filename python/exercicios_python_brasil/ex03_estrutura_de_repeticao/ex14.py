"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
de números pares e a quantidade de números impares."""

impar = par = 0
for _ in range(1, 11):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print()
print(f'Quantidade de números pares digitada: {par}')
print(f'Quantidade de números impares digitada: {impar}')
