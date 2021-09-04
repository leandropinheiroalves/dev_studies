# EXERCÍCIO 55
"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

# PROGRAMA PRINCIPAL
maior = menor = 0  # Criando variáveis maior e menor

for i in range(1, 6):  # Loop iterável de 1 a 5
    peso = float(input(f'Digite o peso da {i}° Pessoa: '))  # Recebe o peso

    if i == 1:  # SE for o primeiro peso informado
        maior = menor = peso  # Variáveis maior e menor recebem o valor do peso

    if peso > maior:  # SE o valor do peso for maior que o valor de maior
        maior = peso  # Variável maior recebe o valor do peso

    if peso < menor:  # SE o valor do peso for maior que o valor de maior
        menor = peso  # Variável menor recebe o valor do peso

print(f'O menor peso informado foi {menor}Kg e o maior foi {maior}Kg')
# ↑ Imprime o menor e o maior peso
