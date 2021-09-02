"""
Aprimore o exercício 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""
jogador = dict()  # Criando dicionário para os dados do jogador
time = list()  # Criando lista para o time
lista = list()  # Criando uma lista
contador = 0  # Criando contador
while True:  # Loop infinito
    jogador.clear()  # Limpando itens do dicionário jogador
    lista.clear()  # Limpando valores da lista
    jogador['nome'] = str(input('Digite o nome do jogador: '))  # Recebendo valor e adicionando na chave 'nome' do dict
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))  # Variável recebendo valor
    if partidas <= 0:  # Se as partidas forem menores que 0
        print(f'{jogador["nome"]} não jogou nenhuma partida.')  # Retorna que o jogador não jogou
        jogador.clear()  # Limpando itens do dicionário jogador
    else:  # Se o valor de partidas for maior do que 0
        for p in range(1, partidas + 1):  # Loop iteração por partidas jogadas
            lista.append(int(input(f'   Quantos gols na {p}° partida? ')))  # Recebendo os gols e adicionando na lista
        jogador['gols'] = lista[:]  # Copiando os valores da lista para a chave 'gols' do dict
        jogador['total'] = sum(lista)  # Somando os valores da lista e adionando na chave 'total' do dict
        contador += 1  # Iteração do contador
        time.append(jogador.copy())  # Copia os itens do dicionário jogador para a lista time
    escolha = str(input('Deseja continuar[S/N]? '))  # Variável que recebe valor de escolha
    while escolha not in 'SsNn':  # Loop de iteração enquando valor de escolha não estiver em 'SsNn'
        escolha = str(input('Valor inválido. Digite S ou N: '))  # Recebe novo valor de escolha
    if escolha in 'nN':  # Se o valor da escolha estiver em 'Nn'
        print('=' * 36)  # Retorna 36 iguais na linha para melhor legibilidade
        print(f'Índice {"Nome":<12}{"Gols":<12}{"Total":<12}')  # Retorna cabeçalho
        print('=' * 36)  # Retorna 36 iguais na linha para melhor legibilidade
        for i, j in enumerate(time):  # Loop de iteração com índices e valores da lista time
            print(f'{i:>6} {j["nome"]:<12}{str(j["gols"]):<12}{j["total"]:<12}')  # Retorna índice, nome, gols e total
        print('=' * 36)  # Retorna 36 iguais na linha para melhor legibilidade
        break  # Encerra o loop infinito
while True:  # Loop infinito
    indice = int(input('Mostrar dados de qual jogador? [999 encerra] '))  # Variável recebendo o índice
    if indice == 999:  # Se o valor do indice for igual 999
        break  # Encerra o loop infinito
    while indice > len(time) - 1:  # Se o valor do indice for maior que a quantidade de jogadores
        indice = int(input('Índice inválido. Digite novamente: [999 encerra] '))  # Recebe novo valor de indice
    print('=' * 36)  # Retorna 36 iguais na linha para melhor legibilidade
    print(f' *** Levantamento do jogador {time[indice]["nome"]}:')  # Retorna qual jogador será o levantamento
    for j, g in enumerate(time[indice]['gols']):  # Loop de iteração com indices e valores dos gols
        print(f'   No {j+1}° jogo fez {g} gols.')  # Retorna os gols feitos por jogo
    print('=' * 36)  # Retorna 36 iguais na linha para melhor legibilidade
