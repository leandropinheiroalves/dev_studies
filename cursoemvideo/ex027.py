"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""

nome = str(input('Digite o nome completo: '))
lista = nome.split()
print(f'Primeiro nome é: {lista[0]}')
print(f'Último nome é: {lista[-1]}')

# # Solução Guanabara:
# n = str(input('Digite seu nome completo: ')).strip()
# nome = n.split()
# print('Muito prazer em te conhecer!')
# print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[len(nome)-1]))
