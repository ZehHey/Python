def metade(n=0, v=True):
    res = n / 2
    if v:
        return moeda(res)
    else:
        return res


def dobro(n=0, v=True):
    res = n * 2
    if v:
        return moeda(res)
    else:
        return res


def aumentar(n=0, t=0, v=True):
    res = n + (n / 100 * t)
    if v:
        return moeda(res)
    else:
        return res


def diminuir(n=0, t=0, v=True):
    res = n - (n / 100 * t)
    if v:
        return moeda(res)
    else:
        return res


def moeda(n=0, m='R$'):
    return f'{m}{n:4.2f}'.replace('.', ',')


def resumo(n=0, a=10, r=5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço:\t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{r}% de redução: \t{diminuir(n, r)}')
    print('-' * 30)
