"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit."""

celsius = float(input('Informe a temperatura em graus Celsius: '))
fahrenheit = (celsius *9 / 5) + 32

print(f'{celsius} graus Celsius equivalem a: {fahrenheit} graus Fahrenheit')
