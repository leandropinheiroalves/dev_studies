"""
Faça um programa que leia um número inteiro e mostre na tela os primeiros elementos de uma sequência de Fibonacci.
Ex:
0 → 1 → 1 → 2 → 3 → 5 → 8
"""
sequencia = int(input('Digite um número: '))
n1 = 0
n2 = 1
n3 = n1 + n2
contador = 0
print(f'{n1} → {n2} → {n2} → ', end='')
while contador < sequencia - 3:
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    print(n3, end=' → ')
    contador += 1
print('FIM')
