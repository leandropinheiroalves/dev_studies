"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o  nome do jogador e quantas partidas ele jogou. Depois vai ler a  quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()  # Criando dicionário para os dados do jogador
lista = list()  # Criando uma lista
jogador['nome'] = str(input('Digite o nome do jogador: '))  # Recebendo valor e adicionando na chave 'nome' do dict
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))  # Variável recebendo valor
if partidas > 0:  # Se o valor de partidas for maior do que 0
    for p in range(1, partidas + 1):  # Loop iteração por partidas jogadas
        lista.append(int(input(f'Quantos gols na {p}° partida? ')))  # Recebendo os gols e adicionando na lista
    jogador['gols'] = lista[:]  # Copiando os valores da lista para a chave 'gols' do dict
    jogador['total'] = sum(lista)  # Somando os valores da lista e adionando na chave 'total' do dict
    print()  # Quebra de linha
    print(jogador)  # Retorna o dict jogador
    print()  # Quebra de linha
    for k, v in jogador.items():  # Loop de iteração nos items do dict
        print(f'{k.capitalize()}: {v}')  # Retorna chave e valor do dict
    print()  # Quebra de linha
    print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')  # Retorna o número de partidas jogadas
    for i, p in enumerate(jogador['gols']):  # Loop de iteração nos valores da chave 'gols' do dict
        print(f'   Na {i + 1}° partida fez {p} gols.')  # Retorna o número de gols feitos por partida
    print(f'Ele fez no total {jogador["total"]} gols no campeonato.')  # Retorna o total de gols feitos no campeonato
else:  # Senão
    print(f'{jogador["nome"]} não jogou nenhuma parida.')  # Retorna que o jogador não jogou
