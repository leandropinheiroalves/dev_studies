"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo."""

numero = int(input('Digite um número inteiro para saber o número de series de Fibonacci: '))
t1 = 0
t2 = 1
t3 = t1 + t2

print(f'{t1} {t2} {t2} ', end = '')
for i in range(numero + 1):
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(f'{t3}', end = ' ')

