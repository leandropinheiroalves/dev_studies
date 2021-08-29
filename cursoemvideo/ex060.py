"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
"""
numero = int(input('Digite um número para saber o seu fatorial: '))
fatorial = numero
resultado = 1
print(f'{numero}! =', end=' ')
while fatorial > 0:
    print(f'{fatorial} ', end='')
    print('x ' if fatorial > 1 else '= ', end='')
    resultado *= fatorial
    fatorial -= 1
print(resultado)
