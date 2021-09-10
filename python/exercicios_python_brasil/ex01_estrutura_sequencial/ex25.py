"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    * "Telefonou para a vítima?"
    * "Esteve no local do crime?"
    * "Mora perto da vítima?"
    * "Devia para a vítima?"
    * "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a
2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""

resposta_1 = input('Telefonou para a vítima? ')
resposta_2 = input('Esteve no local do crime? ')
resposta_3 = input('Mora perto da vítima? ')
resposta_4 = input('Devia para a vítima? ')
resposta_5 = input('Já trabalhou com a vítima? ')
contagem = 0

if resposta_1 in 'Ss':
    contagem += 1

if resposta_2 in 'Ss':
    contagem += 1

if resposta_3 in 'Ss':
    contagem += 1

if resposta_4 in 'Ss':
    contagem += 1

if resposta_5 in 'Ss':
    contagem += 1

if contagem == 2:
    resultado = 'Suspeito'
elif contagem in (3, 4):
    resultado = 'Cúmplice'
elif contagem == 5:
    resultado = 'Assassino'
else:
    resultado = 'Inocente'

print(contagem, resultado)