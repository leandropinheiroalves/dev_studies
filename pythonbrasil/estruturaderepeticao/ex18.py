"""Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores."""

numero = menor = maior = soma = contador= 0
resposta = 'S'
while resposta == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N] ')).upper()

print(f'Soma dos valores: {soma}, maior número: {maior}, menor número {menor}')