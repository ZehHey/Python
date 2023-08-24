# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial

def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    """
    cont = 1
    for c in range(n, 0, -1):
        cont *= c
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
    return cont


print(f'{fatorial(5, True)}')
help(fatorial)
