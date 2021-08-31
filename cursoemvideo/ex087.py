"""
Aprimore o exercício anterior, mostrando no final:
    * A soma de todos os valores pares digitados.
    * A  soma dos valores da terceira coluna.
    * O maior valor da segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Cria uma lista com 3 listas dentro, cada lista com três valores 0
soma_pares = soma_coluna = maior = 0  # Cria váriaveis
for linha in range(0, 3):  # Cria iteração para cada linha
    for coluna in range(0, 3):  # Cria iteração para cada coluna
        matriz[linha][coluna] = int(input(f'Digite um valor para o local [{linha}, {coluna}]: '))  # Recebe o valor conforme linha e coluna
        if matriz[linha][coluna] % 2 == 0:  # Se valor for par
            soma_pares += matriz[linha][coluna]  # Soma os valores pares
print()  # Quebra de  linha
for linha in range(0, 3):  # Cria iteração para cada linha
    for coluna in range(0, 3):  # Cria iteração para cada coluna
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # Retorna os valores da matriz conforme linha e coluna
    print()  # Quebra de linha
print()  # Quebra de linha
print(f'A soma dos valores pares é: {soma_pares}')  # Retorna a soma dos valores pares
for linha in range(0, 3):  # Cria iteração na linha
    soma_coluna += matriz[linha][2]  # Soma os valores da terceira coluna
print(f'A soma dos valores da terceira coluna é: {soma_coluna}')  # Retorna a soma dos valores da terceira coluna
for coluna in range(0, 3):  # Cria iteração na coluna
    if coluna == 0:  # Se for a primeira coluna
        maior = matriz[1][coluna]  # Variável maior recebe o valor da coluna 1, linha 2
    elif matriz[1][coluna] > maior:  # Se o valor da coluna na linha 2 for maior que a variável maior
        maior = matriz[1][coluna]  # Variável maior recebe o valor da coluna na linha 2
print(f'O maior número da segunda linha é: {maior}')  # Retorna o maior número da segunda linha
