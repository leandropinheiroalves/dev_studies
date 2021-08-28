"""Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que
o usuário informe um valor válido."""

nota = float(input('Digite uma nota de 0 a 10: '))

while nota not in range(11):
    print('O valor digitado é inválido, digite uma nota de 0 a 10.')
    nota = float(input('Digite uma nota de 0 a 10: '))

print(f'A nota digitada foi {nota}.')