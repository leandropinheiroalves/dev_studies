'''https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true'''

numero = int(input())
strings = []
par = ''
impar = ''
lista = []
for i in range(numero):
    strings.append(input())
for palavra in strings:
    for indice, letra in enumerate(palavra):
        if indice % 2 == 0 or indice == 0:
            par = par + letra
        else:
            impar = impar + letra
            
    lista.append((par, impar))
    par = ''
    impar = ''
        
for p, i in lista:
    print(p, i)
