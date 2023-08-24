def metade(n=0):
    res = f'{n / 2}'
    return res


def dobro(n=0):
    res = f'{n * 2}'
    return res


def aumentar(n=0, t=0):
    res = f'{n + (n / 100 * t)}'
    return res


def diminuir(n=0, t=0):
    res = f'{n - (n / 100 * t)}'
    return res


def moeda(n=0, m='R$'):
    n = float(n)
    return f'{m}{n:.2f}'.replace('.', ',')

