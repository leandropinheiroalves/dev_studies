# EXERCÍCIO 60
"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
"""

# PROGRAMA PRINCIPAL
numero = int(input('Digite um número para saber o seu fatorial: '))  # Recebe um número
fatorial = numero  # Variável fatorial igual valor de numero
resultado = 1  # Variável resultado igual 1

print(f'{numero}! =', end=' ')  # Imprime o número informado sem quebra de linha
while fatorial > 0:  # Loop ENQUANTO valor de fatorial for maior que 0
    print(f'{fatorial} ', end='')  # Imprime o fatorial sem quebra de linha
    print('x ' if fatorial > 1 else '= ', end='')  # Imprime as separações dos números
    resultado *= fatorial  # Incremento do resultado
    fatorial -= 1  # Decremento do fatorial

print(resultado)  # Imprime resultado
