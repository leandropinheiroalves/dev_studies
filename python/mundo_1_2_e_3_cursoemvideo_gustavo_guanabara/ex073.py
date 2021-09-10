"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação
Depois mostre:
    * Apenas os 5 primeiros colocados.
    * Os Últimos 4 colocados da tabela.
    * Uma lista com os time em ordem alfabética.
    * Em que posição na tabela está o time da Chapecoense.
"""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético', 'Botafogo', 'Atlético_PR', 'Bahia', 'São Paulo', 'Fluminense',
         'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Lista de times do campeonato: {times}')
print(f'Top 5 da tabela: {times[:5]}')
print(f'Últimos 4 da tabela: {times[-4:]}')
print(f'Tabela em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está em {times.index("Chapecoense") + 1}° na tabela')
