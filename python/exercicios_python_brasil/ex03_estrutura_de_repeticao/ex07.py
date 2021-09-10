"""Faça um programa que leia 5 números e informe o maior número."""

for contagem in range(1, 6):
    numero = int(input('Digite um número: '))
    if contagem == 1:
        maior = numero
    else:
        if numero > maior:
            maior = numero

print(maior)