"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
lista = []  # Criando lista
for i in range(0, 5):  # Criando laço de repetição com 5 repetições
    numero = int(input('Digite um valor: '))  # Recebendo um número
    if i == 0:  # Se for a primeira repetição do laço
        lista.append(numero)  # Adiciona o número na lista
        print('Valor adicionado na lista.')  # Retorna que o número foi adicionado a lista
    elif numero > lista[-1]:  # Se numero for maior do que o último número da lista
        lista.append(numero)  # Adiciona o número no final da lista
        print('Valor adicionado no final da lista.')  #Retorna que o número foi adicionado no final da lista
    else:  # Se não
        posicao = 0  # Criando váriavel de posição
        while posicao < len(lista):  # Cria um laço de repetição enquanto a posição for menor que a quantidade da lista
            if numero <= lista[posicao]:  # Se o número for menor do que o valor da lista na posição verificada
                lista.insert(posicao, numero)  # Adiciona o número na posição
                print(f'Valor adicionado na posição {posicao + 1} da lista.')  # Retorna posição que o número foi add
                break  # Para o laço de repetição while
            posicao += 1  # Aumenta a posição
print(f'Números digitados em ordem crescente: {lista}')  # Retorna a lista digitada em ordem crescente
