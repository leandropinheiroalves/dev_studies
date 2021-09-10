"""Altere o programa anterior para mostrar no final a soma dos números."""

numero_1 = int(input('Digite o primeiro número: '))
numero_2 = int(input('Digite o primeiro número: '))

for numeros in range(numero_1 + 1, numero_2):
    print(numeros, end = ' ')
    if numeros == (numero_1 + 1):
        soma = numeros
    else:
        soma += numeros

print()
print(f'A soma dos números no intervalo de {numero_1} a {numero_2} é: {soma}.')
print(f'OBS: Os números {numero_1} e {numero_2} não estão contidos no intervalo e nem na soma.')