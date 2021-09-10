# EXERCÍCIO 40
"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    → Média abaixo de 5.0: REPROVADO
    → Média entre 5.0 e 6.9: RECUPERAÇÃO
    → Média 7.0 ou superior: APROVADO
"""

# PROGRAMA PRINCIPAL
nota_1 = float(input('Digite a primeira nota: '))  # Recebendo primeira nota
nota_2 = float(input('Digite a segunda nota: '))  # Recebendo segunda nota
media = (nota_1 + nota_2) / 2  # Calculando média
if 7 <= media <= 10:  # SE a média for maior ou igual a 7 E menor ou igual a 10
    print(f'APROVADO! Sua média foi {media:.1f}.')  # Imprime mensagem aprovado e valor da média
elif 7 > media >= 5:  # MAIS SE a média for menor que 7 E maior ou igual a 5
    print(f'RECUPERAÇÃO! Sua média foi {media:.1f}.')  # Imprime mensagem recuperação e valor da média
elif 0 <= media < 5:  # SE a média for maior ou igual a 0 E menor que 5
    print(f'REPROVADO! Sua média foi {media:.1f}')  # Imprime mensagem reprovado e valor da média
else:  #SENÃO
    print('Ouve algum erro. Tente novamente.')  # Imprime mensagem de erro
