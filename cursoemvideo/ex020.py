"""
O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
from random import shuffle

alunos = []
alunos.append(input('Digite o nome do primeiro aluno: '))
alunos.append(input('Digite o nome do segundo aluno: '))
alunos.append(input('Digite o nome do terceiro aluno: '))
alunos.append(input('Digite o nome do quarto aluno: '))
ordem = shuffle(alunos)
print('A ordem de apresentação dos trabalhos é:')
print(alunos)
