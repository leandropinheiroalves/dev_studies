"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
lista = []  # Criando lista
while True:  # Criando laço de repetição infinito
    numero = (int(input('Digite um número: ')))  # Recebendo número
    if numero not in lista:  # Se o número informado não estiver na lista
        lista.append(numero)  # Adiciona o número na lista
        print('Valor adicionado!')  # Retorna mensagem de adicionado
    else:  # Se o número estiver na lista
        print('Valores duplicados não serão adicionados.')  # Retorna mensagem de não adicionado
    escolha = ' '  # Criando variável de decisão
    while escolha[0] not in 'SsNn':  # Criando laço de repetição enquanto a decisão não estiver em 'SsNn'
        escolha = str(input('Deseja continuar?[S/N] '))  # Recebendo valor da decisão
    if escolha[0] in 'Nn':  # Se a decisão estiver em 'Nn'
        break  # Encerra o laço de repetição infinito
lista.sort()  # Organiza a lista em ordem crescente
print(f'Os valores únicos digitados em ordem crescente são: {lista}')  # Retorna a lista em ordem crescente
