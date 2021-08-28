"""Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
a quantidades de latas de tinta a serem compradas e o preço total."""

tamanho_da_area = float(input('Informe o valor em metros quadrados da área a ser pintada: '))
metros_por_litro = 3
metros_por_lata = metros_por_litro * 18
latas_de_tinta = tamanho_da_area // 54

if tamanho_da_area % 54 != 0:
    latas_de_tinta += 1
preco_total = latas_de_tinta * 80

print(f'Para uma área de {tamanho_da_area} m² seraõ necessárias {latas_de_tinta} latas de tinta com valor total de R$ {preco_total}.')