"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu programa deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
lista = []  # Criando  lista
expressao = str(input('Digite uma expressão com parênteses: '))  # Recebendo a expressão digitada
for caracter in expressao:  # Criando laço de repetição, repetindo para cada caractere na expressão
    if caracter == '(':  # Se o caracter for um parêntese aberto
        lista.append(caracter)  # Adiciona um parêntese aberto na lista
    elif caracter == ')':  # Se o caracter for um parêntese fechado
        if '(' in lista:  # Se tiver algum parêntese aberto na lista
            lista.pop()  # Remove o ultimo valor da lista
        else:  # Senão
            lista.append(')')  # Adiciona um parêntese fechado na lista
if len(lista) == 0:  # Se a lista estiver sem valores
    print('Sua expressão está correta!')  # Retorna expressão correta
else:  # Senão
    print('Sua expressão está errada!')  # Retorna expressão errada
