"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []  # Criando lista
maior = menor = 0  # Criando váriaveis de maior e menor com valor de inicio 0
for numero in range(0, 5):  # Criando laço de repetição com 5 repetições
    lista.append(int(input('Digite um número: ')))  # Recebe um número e adiciona à lista
    if numero == 0:  # Se for a primeira repetição do laço
        maior = menor = lista[numero]  # Variáveis maior e menor recebem o primeiro valor da lista
    else:  # Se não for a primeira repetição do laço
        if lista[numero] > maior:  # Se o número informado for maior que o maior número
            maior = lista[numero]  # O número informado passa a ser o maior número
        if lista[numero] < menor:  # Se o número informado for menor que o menor número
            menor = lista[numero]  # O número informado passa a ser o menor número
print(f'Números digitados: {lista}')  # Retorna a lista
print(f'O maior número foi {maior} nas posições: ', end='')  # Retorna o maior número
for i, a in enumerate(lista):  # Laço de repetição com índices e valores dos itens da lista
    if a == maior:  # Se o valor for igual o maior número
        print(f'{i} ', end='')  # Retorna o índece do maior valor
print()  # Quebra de linha
print(f'O menor número foi {menor} nas posições: ', end='')  # Retorna o maior número
for i, a in enumerate(lista):  # Laço de repetição com índices e valores dos itens da lista
    if a == menor:  # Se o valor for igual o menor número
        print(f'{i} ', end='')  # Retorna o índice do menor valor
print()  # Quebra de linha
