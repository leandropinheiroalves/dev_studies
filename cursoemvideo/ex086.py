"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Cria uma lista com 3 listas dentro, cada lista com três valores 0
for linha in range(0, 3):  # Cria iteração para cada linha
    for coluna in range(0, 3):  # Cria iteração para cada coluna
        matriz[linha][coluna] = int(input(f'Digite um valor para o local [{linha}, {coluna}]: '))  # Recebe o valor conforme linha e coluna
print()  # Quebra de  linha
for linha in range(0, 3):  # Cria iteração para cada linha
    for coluna in range(0, 3):  # Cria iteração para cada coluna
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # Retorna os valores da matriz conforme linha e coluna
    print()  # Quebra de linha
