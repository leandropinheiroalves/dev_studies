"""Faça um programa que calcule o fatorial de um número inteiro fornecido
pelo usuário. Ex.: 5!=5.4.3.2.1=120"""

numero = int(input('Digite um número inteiro para calcular o fatorial dele: '))
contador = numero
fatorial = 1

print(f'Calculando {numero}!: ', end = '')
while contador > 0:
    print(contador, end = ' ')
    print(f'x ' if contador > 1 else '= ',  end = '')
    fatorial *= contador
    contador -= 1
print(fatorial, end= '')