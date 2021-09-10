"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Considere US$1,00 = R$3,27
"""
dinheiro_carteira = float(input('Digite quantos reais você possui na carteira: '))
dolares = dinheiro_carteira / 3.27
print(f'É possível comprar US$ \033[3;31m{dolares:.2f}\033[m dolares com R$ \033[36m{dinheiro_carteira}\033[m reais.')