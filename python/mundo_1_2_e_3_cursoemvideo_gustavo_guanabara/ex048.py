# EXERCÍCIO 48
"""
Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

# PROGRAMA PRINCIPAL
soma = contagem = 0  # Variáveis soma e contagem recebem 0
for i in range(1, 501):  # Loop de iteração de 1 a 500
    if i % 3 == 0 and i % 2 != 0:  # SE o número for ímpar e multiplo de três
        contagem += 1  # Incrementa valor de contagem em 1
        soma += i  # Incrementa valor de soma com o número
print(f'A soma total dos números foi {soma} e tiveram {contagem} valores somados.') # Imprime resultado
