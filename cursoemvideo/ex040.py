"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    *Média abaixo de 5.0: REPROVADO
    *Média entre 5.0 e 6.9: RECUPERAÇÃO
    *Média 7.0 ou superior: APROVADO
"""
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
if 7 <= media <= 10:
    print(f'APROVADO! Sua média foi {media:.1f}.')
elif 7 > media >= 5:
    print(f'RECUPERAÇÃO! Sua média foi {media:.1f}.')
elif 0 < media < 5:
    print(f'REPROVADO! Sua média foi {media:.1f}')
else:
    print('Ouve algum erro. Tente novamente.')
