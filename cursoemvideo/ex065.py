"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
maior = menor = soma = 0
contador = 0
escolha = 'S'
while escolha == 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    contador += 1
    if contador == 1:
        menor = maior = numero
    else:
        if numero < menor:
            menor = numero
        if numero > maior:
            maior = numero
    escolha = str(input('Deseja continuar? [S/N] ')).upper()
media = soma / contador
print(f'Foram digitados {contador} números e a média deles é {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
