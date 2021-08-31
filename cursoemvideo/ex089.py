"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
principal = []  # Cria lista principal
while True:  # Loop infinito
    nome = str(input('Nome do aluno: '))  # Variável que recebe o nome do aluno
    nota1 = int(input('Primeira nota: '))  # Variável que recebe 1° nota do aluno
    nota2 = int(input('Segunda nota: '))  # Variável que recebe 2° nota do aluno
    media = (nota1 + nota2) / 2  # Variável que calcula a média das notas
    principal.append([nome, [nota1, nota2], media])  # Adiciona os nomes, notas e medias na lista principal
    escolha = ' '  # Variável de escolha
    while escolha not in 'SsNn':  # Loop de iteração enquanto variável escolha não estiver em 'SsNn'
        escolha = str(input('Deseja Continuar?[S/N]: '))  # Recebe o valor da escolha
    if escolha in 'Nn':  # Se o valor de escolha estiver em 'Nn'
        break  # Encerra o loop infinito
print('=' * 30)  # Retorna 30 iguais em uma linha, para melhor estética
print(f'Índice {"Nome":<16} Média')  # Retorna índice, nome e média.
print('=' * 30)  # Retorna 30 iguais em uma linha, para melhor estética
for i, l in enumerate(principal):  # Loop de iteração em cada valor da lista principal
    print(f'{i:<6} {l[0]:<16} {l[2]:>5}')  # Retorna os valores de índice, nome e média.
print('=' * 30)  # Retorna 30 iguais em uma linha, para melhor estética
while True:  # Loop infinito
    aluno = int(input('Digite o índice do aluno para ver suas notas ou 999 para sair: '))  # Variável recebe valor
    while aluno != 999:  # Loop de iteração enquanto valor de aluno não for 999
        if aluno > len(principal) - 1:  # Se o valor de aluno for maior que o número de índices
            aluno = int(input('Índice inválido. Digite outro índice ou 999 para sair: '))  # Variável recebe novo valor
        else:  # Senão
            print(f'As notas de {principal[aluno][0]} foram {principal[aluno][1]}')  # Retorna as notas do aluno
            break  # Encerra o segundo loop
    if aluno == 999:  # Se o valor de aluno for igual a 999
        print('Programa encerrado.')  # Retorna mensagem de encerramento
        break  # Encerra o loop infinito
