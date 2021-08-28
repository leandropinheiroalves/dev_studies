"""Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

h =  float(input('Informe uma altura: '))
genero = str(input('Informe o genero da pessoa: [M-Masculino/F-Feminino] ')).upper()

if genero == 'M':
    peso_ideal = (72.7*h) - 58
    print(f'O peso ideal para uma pessoa do sexo Masculino com {h}m de altura é: {peso_ideal}kg')
elif genero == 'F':
    peso_ideal = (62.1*h) - 44.7
    print(f'O peso ideal para uma pessoa do sexo Feminino com {h}m de altura é: {peso_ideal}kg')
else:
    print('O genero informado é inválido!')