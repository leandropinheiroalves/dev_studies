"""Faça um Programa que leia três números e mostre o maior e o menor deles."""

numero_1 = float(input('Digite o primeiro número: '))
numero_2 = float(input('Digite o segundo número: '))
numero_3 = float(input('Digite o terceiro número: '))

if numero_1 < numero_2 and numero_1 < numero_3:
    if numero_2 < numero_3:
        print(f'Entre os números {numero_1}, {numero_2} e {numero_3}, o maior deles é {numero_3} e o menor é {numero_1}')
    else:
        print(
            f'Entre os números {numero_1}, {numero_2} e {numero_3}, o maior deles é {numero_2} e o menor é {numero_1}')

if numero_2 < numero_1 and numero_2 < numero_3:
    if numero_1 < numero_3:
        print(f'Entre os números {numero_1}, {numero_2} e {numero_3}, o maior deles é {numero_3} e o menor é {numero_2}')
    else:
        print(f'Entre os números {numero_1}, {numero_2} e {numero_3}, o maior deles é {numero_1} e o menor é {numero_2}')

if numero_3 < numero_2 and numero_3 < numero_1:
    if numero_2 > numero_1:
        print(f'Entre os números {numero_1}, {numero_2} e {numero_3}, o maior deles é {numero_2} e o menor é {numero_3}')
    else:
        print(
            f'Entre os números {numero_1}, {numero_2} e {numero_3}, o maior deles é {numero_1} e o menor é {numero_3}')