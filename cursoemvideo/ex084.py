"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    * Quantas pessoas foram cadastradas.
    * Uma listagem com as pessoas mais pesadas.
    * Uma listagem com as pessoas mais leves.
"""
temporaria = []  # Criando lista temporaria
lista = []  # Criando lista principal
pesado = leve = 0  # Criando variáveis pesado e leve
while True:  # Criando laço de repetição infinito
    temporaria.append(str(input('Nome: ')))  # Recebendo nome e armazenando na lista temporária
    temporaria.append(int(input('Peso: ')))  # Recebendo peso e armazenando na lista temporária
    if len(lista) == 0:  # Se a lista principal estiver vazia
        pesado = leve = temporaria[1]  # Variáveis pesado e leve receberam o valor do peso armazenado na lista temp.
    else:  # Senão
        if temporaria[1] > pesado:  # Se o valor do peso da lista temporária for maior que o da variável peso
            pesado = temporaria[1]  # Variável peso receberá o valor de peso da lista temporária
        if temporaria[1] < leve:  # Se o valor do peso da lista temporária for menor que o da variável leve
            leve = temporaria[1]  # Variável peso receberá o valor de peso da lista temporária
    lista.append(temporaria[:])  # Lista principal recebe os valores nome e peso da lista temporária
    temporaria.clear()  # Remove todos os valores da lista temporária
    escolha = str(input('Deseja continuar?[S/N] '))  # Cria variável escolha e recebe um valor digitado pelo usuário
    if escolha in 'Nn':  # Se o valor de escolha estiver em 'Nn'
        break  # Encerra o laço de repetição infinito
print()  # Quebra de linha
print(f'Pessoas cadastradas: {len(lista)}')  # Retorna o número de pessoas cadastradas
print(f'O maior peso foi de {pesado}Kg. Peso de ', end='')  # Retorna o maior peso e evita quebra de linha
for i in lista:  # Cria iteração para cada valor na lista principal
    if i[1] == pesado:  # Se o valor do peso da lista principal for igual o valor de pesado
        print(f'[{i[0]}] ', end='')  # Retorna o valor do nome correspondente ao mais pesado
print()  # Quebra de linha
print(f'O menor peso foi de {leve}Kg. Peso de ', end='')  ## Retorna o menor peso e evita quebra de linha
for i in lista:  # Cria iteração para cada valor na lista principal
    if i[1] == leve:  # Se o valor do peso da lista principal for igual o valor de leve
        print(f'[{i[0]}] ', end='')  # Retorna o valor do nome correspondente ao mais leve
print()  # Quebra de linha
