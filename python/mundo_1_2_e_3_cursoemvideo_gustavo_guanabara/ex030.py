"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
numero = int(input('Digite um número inteiro: '))  # Recebe um número inteiro
if numero % 2 == 0:  # Se o resto da divisão do número por 2 for igual 0 o número é par
    print('O número digitado é PAR!')  # Retorna mensagem de número PAR
else:  # Se o resto da divisão não for 0 o número é ímpar
    print('O número digitado é ÍMPAR!')  # Retorna mensagem de número ÍMPAR

# Solução Guanabara:
# numero = int(input('Me diga um número qualquer: '))
# resultado = numero % 2
# if resultado == 0:
#     print('O número {} é PAR'.format(numero))
# else:
#     print('O número {} é ÍMPAR'.format(numero))
