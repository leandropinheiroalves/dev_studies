"""
Crie um programa onde o usuário possa digitar sete valores númericos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista = [[], []]  # Cria uma lista com 2 listas dentro
for i in range(1, 8):  # Cria um laço de repetição com 7 iterações
    numero = int(input(f'Digite {i}° valor: '))  # Cria váriavel numero e recebe um número
    if numero % 2 == 0:  # Se o valor da variável numero for par
        lista[0].append(numero)  # Adiciona o valor da variável numero na primeira lista
    else:  # Se o valor da variável numero for impar
        lista[1].append(numero)  # Adiciona o valor da variável numero na segunda lista
lista[0].sort()  # Organiza a primeira lista em ordem crescente
lista[1].sort()  # Organiza a segunda lista em ordem crescente
print(f'Valores pares em ordem crescente: {lista[0]}')  # Retorna a primeira lista com números pares em ordem cresc.
print(f'Valores ímpares em ordem crescente: {lista[1]}')  # Retorna a primeira lista com números ímpares em ordem cresc.
