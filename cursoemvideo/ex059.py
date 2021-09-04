# EXERCÍCIO 59
"""
Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

# PROGRAMA PRINCIPAL
numero_1 = int(input('Digite o primeiro número: '))  # Recebe primeiro número
numero_2 = int(input('Digite o segundo número: '))  # Recebe segundo número
escolha = 0  # Criando variável escolha

while True:  # Loop infinito
    print('''[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números  \n[5] sair do programa''')
    # ↑ Imprime as escolhas dispóniveis
    escolha = int(input('Digite uma das opções: '))  # Recebe escolha

    if escolha == 1:  # SE a escolha for 1
        soma = numero_1 + numero_2  # Calcula a soma
        print(f'{numero_1} + {numero_2} = {soma}')  # Imprime o resultado da soma

    elif escolha == 2:  # MAIS SE a escolha for 2
        multiplicar = numero_1 * numero_2  # Calcula a multiplicação
        print(f'{numero_1} x {numero_2} = {multiplicar}')  # Imprime o resultado da multiplicação

    elif escolha == 3:  # MAIS SE a escolha for 3
        if numero_2 > numero_1:  # SE o segundo número for maior que o primeiro
            print(f'O maior número entre {numero_1} e {numero_2} é o {numero_2}')
            # ↑ Imprime que o segundo número é maior

        elif numero_2 < numero_1:  # MAIS SE o segundo número for menor que o primeiro
            print(f'O maior número entre {numero_1} e {numero_2} é o {numero_1}')
            # ↑ Imprime que o primeiro número é maior

        elif numero_2 == numero_1:  # MAIS SE os números forem iguais
            print(f'Os dois números informados são iguais.')  # Imprime igualdade do números

    elif escolha == 4:  # MAIS  SE a escolha for 4
        numero_1 = int(input('Digite novamente o primeiro número: '))  # Recebe novo primeiro número
        numero_2 = int(input('Digite novamente o segundo número: '))  # Recebe novo segundo número

    elif escolha == 5:  # MAIS  SE a escolha for 5
        print('Programa foi encerrado.')  # Imprime encerramento do programa
        break  # Encerra o loop infinito

    else:  # SENÃO
        print('Opção inválida tente novamente')  # Imprime erro
