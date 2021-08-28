"""A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500."""

t1 = 0
t2 = 1
t3 = t1 + t2
print(t1, t2, t2, end = ' ')
while True:
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(t3, end = ' ')
    if t3 > 500:
        break