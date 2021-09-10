# EXERCÍCIO 33
"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

# PROGRAMA PRINCIPAL
numero_1 = int(input('Digite o primeiro número: '))  # Recebendo primeiro número
numero_2 = int(input('Digite o segundo número: '))  # Recebendo segundo número
numero_3 = int(input('Digite o terceiro número: '))  # Recebendo terceiro número
menor = maior = numero_1  # Variáveis menor e maior recebendo o valor do primeiro número
if numero_2 > numero_1 and numero_2 > numero_3:  # SE n2 for maior que n1 E n2 for maior que n3
    maior = numero_2  # Variável maior recebe n2
if numero_3 > numero_1 and numero_3 > numero_2:  # SE n3 for maior que n1 E n3 for maior que n2
    maior = numero_3  # Variável maior recebe n3
if numero_2 < numero_1 and numero_2 < numero_3:  # SE n2 for menor que n1 E n2 for menor que n3
    menor = numero_2  # Variável menor recebe n2
if numero_3 < numero_1 and numero_3 < numero_2:  # SE n3 for menor que n1 E n3 for menor que n2
    menor = numero_3  # Variável menor recebe n3
print(f'O maior número digitado foi {maior}')  # Imprime na tela o maior número
print(f'O menor número digitado foi {menor}')  # Imprime na tela o menor número

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
