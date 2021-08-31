"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
nome = str(input('Digite um nome completo: ')).upper()
# Recebendo o nome da cidade e deixando tudo em maiúsculo

print('SILVA' in nome)
# Verificando se dentro da string existe 'SILVA'
# Retornando True ou False

# Solução Guanabara:
# nome = str(input('Qual é seu nome completo? ')).strip()
# print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
