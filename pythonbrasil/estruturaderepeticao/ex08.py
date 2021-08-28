"""Faça um programa que leia 5 números e informe a soma e a média dos números."""

for contagem in range(1, 6):
    numero = float(input('Digite um número: '))
    if contagem == 1:
        soma = numero
    else:
        soma += numero
        media = soma / contagem

print(f'A soma total dos números é: {soma}')
print(f'A média dos números é: {media}')
