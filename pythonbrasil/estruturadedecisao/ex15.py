"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem
um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    * Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
    que o terceiro;
    * Triângulo Equilátero: três lados iguais;
    * Triângulo Isósceles: quaisquer dois lados iguais;
    * Triângulo Escaleno: três lados diferentes;"""
lado_1 = float(input('Digite o primeiro lado do triângulo: '))
lado_2 = float(input('Digite o segundo lado do triângulo: '))
lado_3 = float(input('Digite o terceiro lado do triângulo: '))

if (lado_1 + lado_2) > lado_3 or (lado_1 + lado_3) > lado_2 or (lado_3 + lado_2) > lado_1:
    triangulo = True
else:
    triangulo = False

if lado_1 == lado_2 == lado_3:
    tipo_triangulo = 'Equilátero'
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    tipo_triangulo = 'Isóceles'
else:
    tipo_triangulo = 'Escaleno'

if triangulo == True:
    print(f'Os valores informados formam um triângulo e ele é {tipo_triangulo}.')
else:
    print('Os valores informados não formam um triângulo!')