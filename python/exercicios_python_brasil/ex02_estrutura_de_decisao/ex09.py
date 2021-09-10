"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))

if numero_1 < numero_2 and numero_1 < numero_3:
    if numero_2 < numero_3:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_3}, {numero_2} e {numero_1}')
    elif numero_2 > numero_3:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_2}, {numero_3} e {numero_1}')
    elif numero_2 == numero_3:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_2}, {numero_3} e {numero_1}')

elif numero_2 < numero_1 and numero_2 < numero_3:
    if numero_1 < numero_3:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_3}, {numero_1} e {numero_2}')
    elif numero_1 > numero_3:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_1}, {numero_3} e {numero_2}')
    elif numero_1 == numero_3:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_1}, {numero_3} e {numero_2}')

elif numero_3 < numero_2 and numero_3 < numero_1:
    if numero_2 < numero_1:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_1}, {numero_2} e {numero_3}')
    elif numero_2 > numero_1:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_2}, {numero_1} e {numero_3}')
    elif numero_1 == numero_2:
        print(f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_2}, {numero_1} e {numero_3}')

elif numero_1 == numero_2 == numero_3:
    print(
        f'A ordem decrescente dos números {numero_1}, {numero_2} e {numero_3} é: {numero_2}, {numero_1} e {numero_3}')

else:
    print('Ouve algum erro, tente novamente.')