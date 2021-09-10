"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
nome = str(input('Digite o nome completo: '))  # Recebendo um nome completo
lista = nome.split()  # Transformando o nome completo em uma lista
print(f'Primeiro nome é: {lista[0]}')  # Retornando o primeiro valor da lista
print(f'Último nome é: {lista[-1]}')  # Retornando o último valor da lista

# # Solução Guanabara:
# n = str(input('Digite seu nome completo: ')).strip()
# nome = n.split()
# print('Muito prazer em te conhecer!')
# print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu último nome é {}'.format(nome[len(nome)-1]))
