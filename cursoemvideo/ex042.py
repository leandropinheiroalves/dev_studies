# EXERCÍCIO 42
"""
Refaça o Exercício 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
    → Equilátero: todos os lados iguais
    → Isósceles: dois lados iguais
    → Escaleno: todos os lados diferentes
"""

# PROGRAMA PRINCIPAL
reta_1 = float(input('Digite o primeiro valor: '))  # Recebe primeiro valor
reta_2 = float(input('Digite o segundo valor: '))  # Recebe segundo valor
reta_3 = float(input('Digite o terceiro valor: '))  # Recebe terceiro valor
if reta_1 < (reta_2 + reta_3) and reta_2 < (reta_1 + reta_3) and reta_3 < (reta_2 + reta_1):
    # ↑ SE a primeira reta for menor que a soma da segunda e da terceira reta
    # ↑↑ OU SE a segunda reta for menor que a soma da primeira e da terceira reta
    # ↑↑↑ OU SE a terceira reta for menor que a soma da segunda e da primeira reta
    print('Os valores informados formam um triângulo.')  # Imprime na tela que é um triângulo
    if reta_1 == reta_2 == reta_3:  #  SE as três retas forem iguais
        print('O triângulo formado é Equilátero, todos os lados são iguais.')  # Imprime equilátero
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_2 == reta_3:  # MAIS SE haver dois lados iguais
        print('O triângulo formado é Isósceles, dois lados são iguais.')  # Imprime isósceles
    else:  # SENÃO
        print('O triângulo formado é Escaleno, todos os lados são diferentes.')  # Imprime escaleno
else:  # SENÃO
    print('Os valores informados não formam um triângulo.')  # Imprime na tela que não é um triângulo
