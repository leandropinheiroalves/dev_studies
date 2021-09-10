"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
numero = int(input('Digite um número de 0 a 9999: '))
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = ((numero % 1000) % 100) // 10
unidade = ((numero % 1000) % 100) % 10
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

# # Solução Guanabara:
# num = int(input('Informe um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(u))
# print('Dezena: {}'.format(d))
# print('Centena: {}'.format(c))
# print('Milhar: {}'.format(m))