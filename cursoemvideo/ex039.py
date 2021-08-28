"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    * Se ele ainda vai se alistar ao serviço militar
    * Se é a hora de se alistar
    * Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
alistamento = ano + 18
if 0 < idade < 18:
    tempo = 18 - idade
    print(f'''Você nasceu em {ano} e está com {idade} anos.
Faltam {tempo} anos para o seu alistamento.
Seu alistamento será em {alistamento}.''')
elif idade == 18:
    print(f'''Você nasceu em {ano} e está com {idade} anos.
Você tem que se alistar nesse ano.''')
elif idade > 18:
    print(f'''Você nasceu em {ano} e está com {idade} anos.
Você deveria ter se alistado a {idade - 18} anos.
Seu alistamento foi em {alistamento}.''')
else:
    print('Ouve algum erro. Tente novamente.')
