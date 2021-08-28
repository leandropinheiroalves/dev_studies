"""Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros,
que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    a. comprar apenas latas de 18 litros;
    b. comprar apenas galões de 3,6 litros;
    c. misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    considere latas cheias.
"""
import math
# math.ceil() arredonda pra cima
# math.floor() arredonda pra baixo

area_a_ser_pintada = 200
area_a_ser_pintada_com_folga = area_a_ser_pintada * 1.1
metros_por_litro = 6
litros_por_lata = 18
valor_por_lata = 80
litros_por_galao = 3.6
valor_por_galao = 25

# Situação 1 - Comprando apenas Latas de 18 litros
metros_por_lata = litros_por_lata * metros_por_litro
quantidade_de_latas = math.ceil(area_a_ser_pintada_com_folga / metros_por_lata)
valor_total_latas = quantidade_de_latas * valor_por_lata
print(f'Com uma área a ser pintade de {area_a_ser_pintada} m², serão necessárias {quantidade_de_latas} latas de tinta de 18 litros, o valor total é de: R$ {valor_total_latas}')

# Situação 2 - Comprando apenas Galões de 3.6 litros
metros_por_galao = litros_por_galao * metros_por_litro
quantidade_de_galoes = math.ceil(area_a_ser_pintada_com_folga / metros_por_galao)
valor_total_galoes = quantidade_de_galoes * valor_por_galao
print(f'\nCom uma área a ser pintade de {area_a_ser_pintada} m², serão necessárias {quantidade_de_galoes} galões de tinta de 3.6 litros, o valor total é de: R$ {valor_total_galoes}')

# Situação 2 - Comprando latas e galões, de forma que o desperdício de tinta seja menor
quantidade_de_latas = math.floor(area_a_ser_pintada_com_folga / metros_por_lata)
valor_latas = quantidade_de_latas * 80
listros_faltantes = area_a_ser_pintada_com_folga % metros_por_lata
quantidade_de_galoes = math.ceil(listros_faltantes / metros_por_galao)
valor_galoes = quantidade_de_galoes * 25

valor_total = valor_latas + valor_galoes

print(f'''\nCom uma área a ser pintada de {area_a_ser_pintada} m², serão necessários:
{quantidade_de_latas} latas de tinta de 18 litros, no valor de: R$ {valor_latas}
{quantidade_de_galoes} galões de tinta de 3.6 litros, no valor de: R${valor_galoes}
O valor total de latas e galões é de: {valor_total}
''')

