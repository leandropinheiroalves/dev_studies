"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
soma = contagem = 0
for i in range(1, 500):
    if i % 3 == 0 and i % 2 != 0:
        contagem += 1
        soma += i
print(f'A soma total dos números foi {soma} e tiveram {contagem} valores somados.')
