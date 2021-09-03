# EXERCÍCIO 102
"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e o outro chamado show,
que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


# DEFININDO FUNÇÃO
def fatorial(numero, show=False):  # Criando função fatorial com valor de parâmetro show opcional
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """  # Docstring sobre funcionamento da função fatorial
    resultado = 1  # Cria variável resultado
    print('=' * 50)  # Imprime na tela o espaçamento
    if not show:  # Se o valor de show for False
        for i in range(1, numero + 1):  # Loop de iteração
            resultado *= i  # Incremento da variável resultado
        return resultado  # Função retorna o resultado
    elif show:  # Mais se show for True
        for i in range(numero, 0, -1):  # Loop de iteração com ordem decrescente do numero até zero
            print(f'{i}', end='')  # Imprime na tela os números sem quebra de linha
            if i > 1:  # Se o número for menor que um
                print(' x ', end='')  # Imprime na tela ' x ' entre os números sem quebra de linha
            else:  # Senão
                print(' = ', end='')  # Imprime na tela ' = ' sem quebra de linha
            resultado *= i # Incremento da variável resultado
        return resultado  # Função retorna o resultado


# PROGRAMA PRINCIPAL
print(fatorial(5, show=True))  # Imprimindo na tela o resultado da execução da função fatorial com show = True
print(fatorial(5))  # Imprimindo na tela o resultado da execução da função fatorial sem informar valor de show
