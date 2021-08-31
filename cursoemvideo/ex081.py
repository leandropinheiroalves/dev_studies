"""
Crie um programa que vai ler vários números a colocar em uma lista.
Depois disso, mostre:
    * Quantos números foram digitados.
    * A lista de valores, ordenada de forma decrescente.
    * Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []  # Criando lista
contador = 0  # Criando variável contador
while True:  # Criando laço de repetição infinito
    numero = int(input('Digite um valor: '))  # Recebendo um número
    lista.append(numero)  # Adicionando o número na lista
    contador += 1  # Aumentando o contador em 1
    escolha = ' '  # Criando váriavel escolha
    while escolha not in 'SsNn':  # Criando laço de repetição enquanto a escolha não estiver em 'SsNn'
        escolha = str(input('Deseja continuar?[S/N] '))  # Recebendo valor de escolha
    if escolha in 'nN':  # Se a escolha estiver em 'nN'
        break  # Encerra o laço de repetição
lista.sort(reverse=True)  # Reorganiza a lista em ordem decrescente
print()  # Quebra de linha
print(f'Você digitou {contador} valores.')  # Retorna quantos valores foram digitados
print(f'Lista de valores em ordem decrescente: {lista}')  # Retorna a lista de valores em ordem decrescente
if 5 in lista:  # Se o número 5 estiver na lista
    print('O valor 5 faz parte da lista!')  # Retorna que o 5 está na lista
else:  # Se o número 5 não estiver na lista
    print('O valor 5 não está na lista.')  # Retorna que o 5 não está na lista
