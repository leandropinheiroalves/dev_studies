# EXERCÍCIO 39
"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    → Se ele ainda vai se alistar ao serviço militar
    → Se é a hora de se alistar
    → Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

# PROGRAMA PRINCIPAL
from datetime import date  # Importando função date do módulo datetime
ano = int(input('Digite o seu ano de nascimento: '))  # Recebendo ano
ano_atual = date.today().year  # Recebendo ano atual
idade = ano_atual - ano  # Calculando idade
alistamento = ano + 18  # Calculando ano do alistamento
if 0 < idade < 18:  # SE a idade for maior do que 0 e menor que 18
    tempo = 18 - idade  # Calculando quantos anos faltam até o alistamento
    print(f'Você nasceu em {ano} e está com {idade} anos.')  # Imprime o ano e a idade
    print(f'Faltam {tempo} anos para o seu alistamento.')  # Imprime tempo que falta até o alistamento
    print(f'→ Seu alistamento será em {alistamento}.')  # Imprime em que ano será seu alistamento
elif idade == 18:  # MAIS SE a idade for igual 18
    print(f'Você nasceu em {ano} e está com {idade} anos.')  # Imprime o ano e a idade
    print('→ Você tem que se alistar nesse ano.')  # Imprime que seu alistamento é nesse ano
elif idade > 18:  # MAIS SE a idade for maior que 18
    print(f'Você nasceu em {ano} e está com {idade} anos.')  # Imprime o ano e a idade
    print(f'Você deveria ter se alistado a {idade - 18} anos.')  # Imprime o atraso do alistamento
    print(f'→ Seu alistamento foi em {alistamento}.')  # Imprime em que ano foi seu alistamento
else:  # SENÃO
    print('Ouve algum erro. Tente novamente.')  # Imprime mensagem de erro
