"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são de maiores.
"""
from datetime import date
maiores = menores = 0
for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i}° Pessoa: '))
    idade = date.today().year - ano
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print(f'''Pessoas maiores de idade: {maiores}
Pessoas menores de idade: {menores}''')
