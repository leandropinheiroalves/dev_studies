"""
Refaça o Exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    * Equilátero: todos os lados iguais
    * Isósceles: dois lados iguais
    * Escaleno: todos os lados diferentes
"""
reta_1 = float(input('Digite o primeiro valor: '))
reta_2 = float(input('Digite o segundo valor: '))
reta_3 = float(input('Digite o terceiro valor: '))
if reta_1 < (reta_2 + reta_3) and reta_2 < (reta_1 + reta_3) and reta_3 < (reta_2 + reta_1):
    print('Os valores informados formam um triângulo.')
    if reta_1 == reta_2 == reta_3:
        print('O triângulo formado é Equilátero, todos os lados são iguais.')
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:
        print('O triângulo formado é Isósceles, dois lados são iguais.')
    else:
        print('O triângulo formado é Escaleno, todos os lados são diferentes.')
else:
    print('Os valores informados não formam um triângulo.')

