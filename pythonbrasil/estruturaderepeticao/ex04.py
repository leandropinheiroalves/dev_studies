"""Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

pais_a = 80_000
taxa_crescimento_a = 1.03
pais_b = 200_000
taxa_crescimento_b = 1.015
anos = 0

print(f'Ano: {anos} / População do País A: {pais_a}  População do País B: {pais_b}')
while pais_a < pais_b:
    anos += 1
    pais_a *= taxa_crescimento_a
    pais_b *= taxa_crescimento_b
    print(f'Ano: {anos} / População do País A: {int(pais_a)}  População do País B: {int(pais_b)}')

print(f'Serão necessários {anos} anos para que a população do País A ultrapasse o País B.')
