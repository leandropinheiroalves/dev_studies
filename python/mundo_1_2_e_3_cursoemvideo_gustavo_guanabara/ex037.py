# EXERCÍCIO 37
"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário  escolher qual será a base de conversão:
    → 1 para binário
    → 2 para octal
    → 3 para hexadecimal
"""

# PROGRAMA PRINCIPAL
numero = int(input('Digite um número: '))  # Recebendo um valor
conversor = ['BINÁRIO', 'OCTAL', 'HEXADECIMAL']
# ↑ Criando lista com valores 'BINÁRIO', 'OCTAL' e 'HEXADECIMAL'
print('''[1] BINÁRIO \n[2] OCTAL \n[3] HEXADECIMAL''')  # Imprimindo escolhas
escolha = int(input('Digite um número de 1 a 3: '))  # Recebendo escolha
if escolha == 1:  # SE escolha for 1
    print(f'O número {numero} convertido em BINÁRIO é igual a {bin(numero)[2:]}')
    # ↑ Imprime o número em binário
elif escolha == 2:  # MAIS SE escolha for 2
    print(f'O número {numero} convertido em OCTAL é igual a {oct(numero)[2:]}')
    # ↑ Imprime o número em octal
elif escolha == 3:  # MAIS SE escolha for 3
    print(f'O número {numero} convertido em HEXADECIMAL é igual a {hex(numero)[2:]}')
    # ↑ Imprime o número em hexadecimal
else:  # SENÃO
    print('Opção inválida. Tente novamente.')  # Imprime erro
