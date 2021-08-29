"""
Crie um programa que leia dois valores e mostre um menu na tela:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
escolha = 0
while True:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    escolha = int(input('Digite uma das opções: '))
    if escolha == 1:
        soma = numero_1 + numero_2
        print(f'{numero_1} + {numero_2} = {soma}')
    elif escolha == 2:
        multiplicar = numero_1 * numero_2
        print(f'{numero_1} x {numero_2} = {multiplicar}')
    elif escolha == 3:
        if numero_2 > numero_1:
            print(f'O maior número entre {numero_1} e {numero_2} é o {numero_2}')
        elif numero_2 < numero_1:
            print(f'O maior número entre {numero_1} e {numero_2} é o {numero_1}')
        elif numero_2 == numero_1:
            print(f'Os dois números informados são iguais.')
    elif escolha == 4:
        numero_1 = int(input('Digite novamente o primeiro número: '))
        numero_2 = int(input('Digite novamente o segundo número: '))
    elif escolha == 5:
        print('Programa foi encerrado.')
        break
    else:
        print('Opção inválida tente novamente')
