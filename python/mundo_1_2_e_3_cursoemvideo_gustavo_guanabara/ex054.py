# EXERCÍCIO 54
"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são de maiores.
"""

# PROGRAMA PRINCIPAL
from datetime import date  # Importando função date do módulo datetime

maiores = menores = 0  # Criando variáveis maiores e menores

for i in range(1, 8):  # Loop de iteração de 1 a 7
    ano = int(input(f'Digite o ano de nascimento da {i}° Pessoa: '))  # Recebe ano de nascimento
    idade = date.today().year - ano  # Calcula e recebe a idade

    if idade < 18:  # SE idade  for menor que 18
        menores += 1  # Incrementa a contagem de menores

    else:  # SENÃO
        maiores += 1  # Incrementa a contagem de maiores

print(f'Pessoas maiores de idade: {maiores}')  # Imprime quantidade de maiores de idade
print(f'Pessoas menores de idade: {menores}')  # Imprime quantidade de menores de idade

