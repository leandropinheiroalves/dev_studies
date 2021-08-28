"""Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    * 326 = 3 centenas, 2 dezenas e 6 unidades
    * 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101,
    311, 111, 25, 20, 10, 21, 11, 1, 7 e 16"""
import math

numero = int(input('Informe um número: '))
centenas = math.floor(numero / 100)
dezenas = math.floor((numero % 100) / 10)
unidades = math.floor((numero % 100) % 10)

if centenas == 1:
    if dezenas > 0 and unidades > 0:
        espacamento_centenas = ' centena, '
        if dezenas == 1:
            espacamento_dezenas = ' dezena e '
        elif dezenas > 1:
            espacamento_dezenas = ' dezenas e '
    elif (dezenas > 0 and unidades == 0):
        espacamento_centenas = ' centena e '
        if dezenas == 1:
            espacamento_dezenas = ' dezena'
        elif dezenas > 1:
            espacamento_dezenas = ' dezenas'
    elif (dezenas == 0 and unidades > 0):
        espacamento_dezenas = ''
        dezenas = ''
        espacamento_centenas = ' centena e '
    else:
        espacamento_centenas = ' centena'
        espacamento_dezenas = dezenas = ''
elif centenas == 0:
    centenas = espacamento_centenas = ''
    if dezenas > 0 and unidades > 0:
        if dezenas == 1:
            espacamento_dezenas = ' dezena e '
        elif dezenas > 1:
            espacamento_dezenas = ' dezenas e '
    elif (dezenas > 0 and unidades == 0):
        if dezenas == 1:
            espacamento_dezenas = ' dezena'
        elif dezenas > 1:
            espacamento_dezenas = ' dezenas'
    elif (dezenas == 0 and unidades > 0):
        espacamento_dezenas = ''
        dezenas = ''
else:
    if dezenas > 0 and unidades > 0:
        espacamento_centenas = ' centenas, '
        if dezenas == 1:
            espacamento_dezenas = ' dezena e '
        elif dezenas > 1:
            espacamento_dezenas = ' dezenas e '
    elif (dezenas > 0 and unidades == 0):
        espacamento_centenas = ' centenas e '
        if dezenas == 1:
            espacamento_dezenas = ' dezena'
        elif dezenas > 1:
            espacamento_dezenas = ' dezenas'
    elif (dezenas == 0 and unidades > 0):
        espacamento_dezenas = ''
        dezenas = ''
        espacamento_centenas = ' centenas e '
    else:
        espacamento_centenas = ' centenas'
        espacamento_dezenas = dezenas = ''

if unidades == 0:
    espacamento_unidades = unidades = ''
elif unidades == 1:
    espacamento_unidades = ' unidade'
else:
    espacamento_unidades = ' unidades'

if numero > 1000:
    print('Erro, o número informado precisa ser menor que 1000.')
else:
    print(f'{numero} = {centenas}{espacamento_centenas}{dezenas}{espacamento_dezenas}{unidades}{espacamento_unidades}')
