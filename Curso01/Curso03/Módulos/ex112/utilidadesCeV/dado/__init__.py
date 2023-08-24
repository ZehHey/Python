def leiaDinheiro(num):
    ok = False
    valor = 0
    while not ok:
        n = str(input(num)).strip().replace(',', '.')
        if n.isalpha() or n == '':
            print('\033[0;31mERRO!\033[m')
        else:
            ok = True
            return float(n)


def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!\033[m')
            print('Digite um valor inteiro')
        if ok:
            break
    return valor