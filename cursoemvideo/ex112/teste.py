"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários.
"""

# Programa Principal
from cursoemvideo.ex112.utilidadescev import moeda
from cursoemvideo.ex112.utilidadescev import dado
p = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
