"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%  de desconto.
"""
produto = float(input('Digite o valor do produto: '))
desconto = produto * 0.05
produto_com_desconto = produto - desconto
print(f'O valor do produto com desconto de 5% é R$\033[31m{produto_com_desconto:.2f}\033[m, você economizou R$\033[35m{desconto:.2f}.\033[m')
