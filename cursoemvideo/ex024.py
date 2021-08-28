"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
cidade = input('Digite o nome de uma cidade: ').upper()
lista = cidade.split()
print('SANTO' in lista[0])

# Solução Guanabara:
# cid = str(input('Em que cidade você nasceu? '))
# print(cid[:5].upper() == 'Santo')
