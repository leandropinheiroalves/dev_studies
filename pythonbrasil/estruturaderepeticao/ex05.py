"""Altere o programa anterior permitindo ao usuário informar as populações e as
taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""


pais_a = float(input('Digite a população total do primeiro País: '))
taxa_crescimento_a = float(input('Digite a % de taxa de crescimento do primeiro País: ')) / 100 + 1
pais_b = float(input('Digite a população total do primeiro País: '))
taxa_crescimento_b = float(input('Digite a % de taxa de crescimento do segundo País: ')) / 100 + 1
anos = 0

print(f'Ano: {anos} / População do País A: {pais_a}  População do País B: {pais_b}')

while True:
    while pais_a < pais_b:
        anos += 1
        pais_a *= taxa_crescimento_a
        pais_b *= taxa_crescimento_b
        print(f'Ano: {anos} / População do País A: {int(pais_a)}  População do País B: {int(pais_b)}')
    print(f'Serão necessários {anos} anos para que a população do País A ultrapasse o País B.')
    resposta = str(input('Deseja informar novos valores? [S-Sim / N-Não] ')).upper()
    if resposta == 'S':
        pais_a = float(input('Digite a população total do primeiro País: '))
        taxa_crescimento_a = float(input('Digite a % de taxa de crescimento do primeiro País: ')) / 100 + 1
        pais_b = float(input('Digite a população total do primeiro País: '))
        taxa_crescimento_b = float(input('Digite a % de taxa de crescimento do segundo País: ')) / 100 + 1
        anos = 0
    else:
        break
