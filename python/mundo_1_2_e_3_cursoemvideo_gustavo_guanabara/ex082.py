"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
No final, mostre o conteúdo das três listas geradas.
"""
lista = []                                              # Criando lista principal
pares = []                                              # Criando lista de números pares
impares = []                                            # Criando lista de números ímpares
while True:                                             # Criando laço de repetição infinito
    lista.append(int(input('Digite um valor: ')))       # Recebendo e adicionando valor na lista
    escolha = ' '                                       # Criando variável escolha
    while escolha not in 'SsNn':                        # Criando laço de rep. enquanto resposta não estiver em 'SsNn'
        escolha = str(input('Quer continuar?[S/N] '))   # Recebendo o valor de escolha
    if escolha in 'Nn':                                 # Se a escolha estiver em 'Nn'
        break                                           # Encerra o laço de repetição
for numero in lista:                                    # Criando laço de rep. que se repetira para cada número na lista
    if numero % 2 == 0:                                 # Se o resto da divisão do número por 2 for igual a 0
        pares.append(numero)                            # Adiciona o valor na lista dos pares
    else:                                               # Se o resto da divisão do número por 2 for diferente de 0
        impares.append(numero)                          # Adiciona o valor na lista dos ímpares
print()                                                 # Quebra de linha
print(f'Lista completa de valores digitados: {lista}')  # Retorna a lista principal
print(f'Lista de valores pares: {pares}')               # Retorna a lista dos números pares
print(f'Lista de valores ímpares: {impares}')           # Retorna a lista dos números ímpares
