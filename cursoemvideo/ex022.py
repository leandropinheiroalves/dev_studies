"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
    * O nome com todas as letras maiúsculas
    * O nome com todas as letras minúsculas
    * Quantas letras ao todo (sem contar os espaços)
    * Quantas letras tem o primeiro nome.
"""
nome = input('Digite o seu nome completo: ')
print(f'O nome com todas as letras maiúsculas: {nome.upper()}')
print(f'O nome com todas as letras minúsculas: {nome.lower()}')
lista = nome.split()
print(f'Quantidade total de letras no seu nome: {len("".join(lista))} letras')
print(f'Seu primeiro nome é {lista[0]} e tem {len(lista[0])} letras')

# #
# # # Solução Guanabara:
# nome = str(input('Digite seu nome completo: ')).strip() # usou strip para ignorar espaços no inicio e no final
# print('Analisando seu nome...')
# print('Seu nome em maiúsculas é {}'.format(nome.upper()))
# print('Seu nome em minúsculas é {}'.format(nome.lower()))
# print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) # usou o len para saber o total depois contou a quantidade de espaços e subtraiu o valor
# # print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) # usou o find para achar a primeir posiçao em branco que equivale ao valor de letras da primeira palavra
# separa = nome.split() # criou uma lista
# print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0]))) # usou a primeira posiçao e a quantidade dela que é o primeiro nome
