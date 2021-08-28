"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o segundo número: '))
numero_3 = int(input('Digite o terceiro número: '))
menor = maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')

# # Solução Guanabara
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
# # Verificando quem é menor
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
# # Verificando quem é maior
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
# print('O menor valor digitado foi {}'.format(menor))
# print('O maior valor digitado foi {}'.format(maior))
