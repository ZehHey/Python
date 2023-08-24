def metade(n):
    res = f'{n / 2:.2f}'
    return res


def dobro(n):
    res = f'{n * 2:.2f}'
    return res


def aumentar(n, t):
    res = f'{n + (n / 100 * t):.2f}'
    return res


def diminuir(n, t):
    res = f'{n - (n / 100 * t):.2f}'
    return res
