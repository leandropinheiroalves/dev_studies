"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
cidade = input('Digite o nome de uma cidade: ').upper()
# Recebendo o nome da cidade e deixando tudo em maiúsculo

lista = cidade.split()
# Criando uma lista com o nome da cidade e eliminando os espaços no inicio e no fim

print('SANTO' == lista[0])
# Verificando se o primeiro nome da cidade é 'SANTO'
# Retornando True ou False

# Solução Guanabara:
# cid = str(input('Em que cidade você nasceu? '))
# print(cid[:5].upper() == 'Santo')
