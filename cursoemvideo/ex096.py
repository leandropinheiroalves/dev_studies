"""
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.
"""


def area(largura, comprimento):  # Criando função area com parâmetros largura e comprimento
    a = largura * comprimento  # Variável que calcula a área
    print(f'A área de um terreno {largura} x {comprimento} é de {a} m².')  # Imprime na tela a área


# Programa Principal
l = float(input('Digite a largura do terreno em metros: '))  # Variável recebendo largura
c = float(input('Digite o comprimento do terreno em metros: '))  # Variável recebendo comprimento
area(l, c)  # Executando função com os valores coletados
