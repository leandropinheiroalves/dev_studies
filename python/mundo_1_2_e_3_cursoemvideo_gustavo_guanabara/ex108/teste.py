"""
Adapte o código do desafiro 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
com um valor monetário formatado.
"""
# Programa Principal
from cursoemvideo.ex108 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
