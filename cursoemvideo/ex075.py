"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    * Quantas vezes apareceu o valor 9.
    * Em que posição foi digitado o primeiro valor 3.
    * Quais foram os números pares.
"""
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))
numero_4 = int(input('Digite o quarto número: '))
tupla = (numero_1, numero_2, numero_3, numero_4)
print(f'Números digitados {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O primeiro valor 3 digitado está na {tupla.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')
