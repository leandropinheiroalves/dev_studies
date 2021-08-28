"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário  escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
"""
numero = 93
conversor = ['BINÁRIO', 'OCTAL', 'HEXADECIMAL']
print('''[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
escolha = int(input('Digite um número de 1 a 3: '))
if escolha == 1:
    print(f'O número {numero} convertido em BINÁRIO é igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O número {numero} convertido em OCTAL é igual a {oct(numero)[2:]}')
elif escolha == 3:
    print(f'O número {numero} convertido em HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')



