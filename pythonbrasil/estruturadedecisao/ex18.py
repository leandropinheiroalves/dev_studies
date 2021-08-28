"""Faça um Programa que peça uma data no formato dd/mm/aaaa e
determine se a mesma é uma data válida."""

data = str(input('Digite uma data usando o formato dd/mm/aaaa para saber se ela é válida: '))
data_dia = int(data[:2])
data_mes = int(data[3:5])
data_ano = int(data[6:])

if data_ano % 4 == 0: #determinar se o ano é bissexto
    if data_ano % 100 == 0:
        if data_ano % 400 == 0:
            ano_bissexto = True
        else:
            ano_bissexto = False
    else:
        ano_bissexto = True
else:
    ano_bissexto = False

if data_dia < 0 or data_dia > 30: # verificando se os dias estão abaixo de 0 ou acima de 30
    if data_mes in (1, 3, 5, 7, 8, 10, 12) and data_dia == 31:
        dia = True # se o dia estiver acima de trinta mas for um dos meses com 31 dias, o mes é valido
    else:
        dia = False
else:
    dia = True

if data_dia > 28 and data_mes == 2: # se tiver mais de 28 dias em fevereiro
    if ano_bissexto == True and  data_dia == 29: # se o dia for 29 em fevereiro e o ano for bissexto a data é valida
        dia = True
    else:
        dia = False

if data_mes < 0 or data_mes > 12:
    mes = False
else:
    mes = True

if mes == True and dia == True:
    print(f'A data {data} é uma data válida')
else:
    print(f'A data {data} não é uma data válida.')