def leiaInt(num):
    ok = False
    while not ok:
        try:
            n = str(input(num))
            a = int(n)
            ok = True
            return a
        except (ValueError, TypeError):
            print(f'\033[1;4;31mErro! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            ok = True
            return 0


def linha(tam=50):
    return '-' * tam


def titulo(msg):
    print(linha())
    print(f'{msg:^50}')
    print(linha())


def menu(i, t):
    print(f'\033[33m{i} - \033[34m{t}\033[m')


