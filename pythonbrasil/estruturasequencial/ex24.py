"""Faça um Programa que leia 2 números e em seguida pergunte ao usuário
qual operação ele deseja realizar. O resultado da operação deve
ser acompanhado de uma frase que diga se o número é:
    * par ou ímpar;
    * positivo ou negativo;
    * inteiro ou decimal."""

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o primeiro número: '))
decisao = int(input('Digite um número: 1-SOMA / 2-SUBTRAÇÃO / 3-MULTIPLICAÇÃO / 4-DIVISÃO '))

if decisao == 1:  # soma
    operacao = numero_1 + numero_2
    nome_operacao = 'soma'
elif decisao == 2:  # subtração
    operacao = numero_1 - numero_2
    nome_operacao = 'subtração'
elif decisao == 3:  # multiplicação
    operacao = numero_1 * numero_2
    nome_operacao = 'multiplicação'
elif decisao == 4:  # divisão
    operacao = numero_1 / numero_2
    nome_operacao = 'divisão'
else:
    operacao = 0
    nome_operacao = 0

if operacao == 0:
    par_ou_impar = 'não é par nem impar é NEUTRO'
elif operacao % 2 == 0:
    par_ou_impar = 'é PAR'
else:
    par_ou_impar = 'é IMPAR'

if operacao > 0:
    positivo_ou_negativo = 'é POSITIVO'
elif operacao == 0:
    positivo_ou_negativo = 'não é positivo nem negativo é NEUTRO'
else:
    positivo_ou_negativo = 'é NEGATIVO'

if operacao == round(operacao):
    inteiro_ou_decimal = 'é INTEIRO'
else:
    inteiro_ou_decimal = 'é DECIMAL'

if decisao in (1, 2, 3, 4):
    print(f'O resultado da {nome_operacao} é: {operacao}.')
    print(f'O número {operacao} {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}.')
else:
    print('ERRO! A operção escolhida não existe. [1-SOMA / 2-SUBTRAÇÃO / 3-MULTIPLICAÇÃO / 4-DIVISÃO]')
