"""Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
    * A mensagem "Aprovado", se a média for maior ou igual a 7,
    com a respectiva média alcançada;
    * A mensagem "Reprovado", se a média for menor do que 7,
    com a respectiva média alcançada;
    * A mensagem "Aprovado com Distinção", se a média for igual a 10."""

nota_1 = float(input('Digite a sua primeira nota parcial: '))
nota_2 = float(input('Digite a sua segunda nota parcial: '))
nota_3 = float(input('Digite a sua terceira nota parcial: '))
media = (nota_1 + nota_2 + nota_3) / 3

if media == 10:
    print(f'Aprovado com distinção, sua média foi {media:.1f}.')
elif 10 > media >= 7:
    print(f'Aprovado, sua média foi {media:.1f}')
else:
    print(f'Reprovado, sua média foi {media:.1f}')