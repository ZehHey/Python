def metade(n=0, v=False):
    res = n / 2
    if v:
        return moeda(res)
    else:
        return res


def dobro(n=0, v=False):
    res = n * 2
    if v:
        return moeda(res)
    else:
        return res


def aumentar(n=0, t=0, v=False):
    res = n + (n / 100 * t)
    if v:
        return moeda(res)
    else:
        return res


def diminuir(n=0, t=0, v=False):
    res = n - (n / 100 * t)
    if v:
        return moeda(res)
    else:
        return res


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')

