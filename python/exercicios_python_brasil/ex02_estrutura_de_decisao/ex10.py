"""Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso."""

turno_estudado = str(input('Digite em qual turno você estuda: [M-Matutino/V-Vespertino/N-Noturno] ')).upper()

if turno_estudado[0] == 'M':
    print('Bom dia!')
elif turno_estudado[0] == 'V':
    print('Boa Tarde!')
elif turno_estudado[0] == 'N':
    print('Boa Noite!')
else:
    print('Turno inválido.')