"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
    * Quantas pessoas foram cadastradas
    * A média de idade do grupo.
    * Uma lista com todas as mulheres
    * Uma lista com todas as pessoas com idade acima da média
"""
cadastro = dict()  # Criando dicionário
lista = list()  # Criando lista
mulheres = list()  # Criando lista para mulheres
acima_media = list()  # Criando lista para pessoas acima da idade média
contador = soma_idades = 0  # Criando variáveis
while True:  # Loop infinito
    cadastro['nome'] = str(input('Digite um nome: '))  # Recebendo valor na chave 'nome'
    contador += 1  # Incrementando contador
    cadastro['sexo'] = str(input('Digite um sexo [M/F]: '))  # Recebendo valor na chave 'sexo'
    while cadastro['sexo'] not in 'MmFf':  # Loop de iteração enquanto valor de 'sexo' não estiver em 'MmFf'
        cadastro['sexo'] = str(input('Valor inválido. Digite apenas M ou F: '))  # Recebendo novo valor na chave 'sexo'
    cadastro['idade'] = int(input('Digite a idade: '))  # Recebendo valor na chave 'idade'
    lista.append(cadastro.copy())  # Copiando itens do dict para lista
    escolha = str(input('Deseja continuar [S/N]? '))  # Recebendo valor de escolha
    while escolha not in 'SsNn':  # Loop de iteração enquanto valor de escolha não estiver em 'SsNn'
        escolha = str(input('Valor inválido. Digite S ou N: '))  # Recebendo no valor de escolha
    if escolha in 'Nn':  # Se valor de escolha estiver em 'Nn'
        break  # Encerra o loop infinito
for v in lista:  # Loop de iteração para cada valor da lista
    soma_idades += v['idade']  # Incrementando soma_idades com as idades
media = soma_idades / contador   # Calculando média das idades
for v in lista:  # Loop de iteração para  cada valor da lista
    if v['idade'] > media:  # Se valor da chave 'idade' for maior que a média
        acima_media.append(v)  # Adiciona os valores na lista acima_media
    if v['sexo'] in 'fF':  # Se o valor da chave 'sexo' estiver em 'fF'
        mulheres.append(v['nome'])  # Adiciona os valores da chave 'nome' na lista mulheres
print()  # Quebra de linha
print(f'Foram cadastradas {contador} pessoas.')  # Retorna quantas pessoas foram cadastradas
print(f'A média de idades é de {media:.2f} anos.')  # Retorna a média das idades cadastradas
print('As mulheres cadastradas foram: ', end='')  # Retorna mensagem das mulheres cadastradas
for m in mulheres:  # Loop de iteração dos valores da lista mulheres
    print(f'{m}', end=' ')  # Retorna o nome das mulheres na mesma linha do print anterior
print()  # Quebra de linha
print('Lista das pessoas que estão acima da idade média: ')  # Retorna mensagem das pessoas acima da média
for p in acima_media:  # Loop de iteração nos valores da lista acima_media
    print(f'    * Nome: {p["nome"]}, sexo: {p["sexo"]}, idade: {p["idade"]}')  # Retorna os valores da lista acima_media
print('=======FINALIZADO=======')  # Retorna mensagem de fim
