"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = str(input('Digite um nome completo: ')).upper()
print('SILVA' in nome)

# Solução Guanabara:
# nome = str(input('Qual é seu nome completo? ')).strip()
# print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
