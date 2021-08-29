"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
maior = menor = 0
for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° Pessoa: '))
    if i == 1:
        maior = menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O menor peso informado foi {menor}Kg e o maior foi {maior}Kg')
