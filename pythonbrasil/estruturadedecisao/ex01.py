"""Faça um Programa que peça dois números e imprima o maior deles."""

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

if numero_1 < numero_2:
    print(f'O maior número entre {numero_1} e {numero_2} é o numero {numero_2}')
elif numero_1 > numero_2:
    print(f'O maior número entre {numero_1} e {numero_2} é o numero {numero_1}')
else:
    print('Os números informados são iguais.')

