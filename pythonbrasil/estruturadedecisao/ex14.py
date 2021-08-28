"""Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se
o conceito for D ou E."""

nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
media = (nota_1 + nota_2) / 2

if 9 <= media <= 10:
    conceito = 'A'
elif 7.5 <= media < 9:
    conceito = 'B'
elif 6 <= media < 7.5:
    conceito = 'C'
elif 4 <= media < 6:
    conceito = 'D'
elif 4 >= media > 0:
    conceito = 'E'
else:
    conceito = 'j'

if conceito in 'ABC':
    resultado = 'APROVADO'
elif conceito in 'DE':
    resultado = 'REPROVADO'
else:
    resultado = ''

if resultado == 'APROVADO' or resultado == 'REPROVADO':
    print(f'Você foi {resultado}, seu conceito foi {conceito}, sua média foi {media}, sua primeira nota foi {nota_1} e sua segunda nota foi {nota_2}')
else:
    print('Ouve algum erro, tente novamente.')